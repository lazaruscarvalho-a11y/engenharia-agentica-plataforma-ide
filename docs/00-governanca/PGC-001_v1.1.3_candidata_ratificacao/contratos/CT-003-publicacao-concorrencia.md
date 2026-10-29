# CT-003 — Alterações, concorrência, publicação e recuperação da escrita

**Versão:** 1.0.3 · **Estado:** PROPOSTO · **Norma:** PGC-001 v1.1.3  
**Dono exclusivo:** ciclo de vida, gates e publicação do ChangeSet na fonte oficial. **Não** classifica linguagem, concede permissões, calcula impactos nem gerencia retomada de sessões.

## 1. Objeto e propriedades de consistência

Um `ChangeSet` é uma **unidade lógica indivisível de publicação oficial** para alterações normativas relacionadas em uma fonte oficial. Deve carregar `change_id`, `idempotency_key`, `request_digest`, `base_repository_revision`, `policy_revision_at_authorization`, `operations[]`, `required_invalidations[]`, `approval_refs[]`, `precheck_results[]`, `expected_result_digest`, `state`, `published_repository_revision?`, `postcheck_results?`, `activation_manifest_ref?`, `activation_receipt?`, recibos e referências de auditoria.

O publicador deve garantir **visibilidade consistente**: nenhum leitor autorizado do estado oficial pode tratar metade de um ChangeSet como versão vigente completa. Arquivos de preparação podem estar incompletos, mas ficam isolados. Um conjunto de commits preparatórios em branch não equivale à publicação no branch/ref oficial. A operação que atualiza o ponteiro oficial deve oferecer comparação-condicional com a revisão esperada (CAS/equivalente) ou mecanismo comprovadamente equivalente.

**Limite:** um commit Git não é transação atômica entre Git, sistema de aprovações, fila de eventos, arquivos em outros repositórios e APIs externas. Se houver múltiplos armazenamentos, a arquitetura deve eleger um **manifesto de ativação autoritativo**, com dependências e revisão de cada participante, ou usar coordenador transacional validado. Sem esse controle, não se pode declarar atomicidade global. Operações externas seguem fluxo compensatório/outbox e estados explícitos.

## 2. Máquina de estados do ChangeSet

Estados principais: `DRAFT`, `PREPARED`, `VALIDATED`, `AUTHORIZED`, `PUBLISHING`, `PUBLISHED`, `VERIFIED`. **O estado do ChangeSet não equivale ao `activation_state`: a ativação ocorre depois de VERIFIED em operação condicional própria.**

Estados excepcionais: `BLOCKED`, `CONFLICT`, `FAILED`, `ABORTED`, `POST_PUBLISH_FAILED`.

Transições autorizadas:
- `DRAFT → PREPARED` após inventário de alterações;
- `PREPARED → VALIDATED` após esquema, referências, diffs, impactos e pré-verificações;
- `VALIDATED → AUTHORIZED` após aprovação vinculada ao conteúdo, identidade e política vigente;
- `AUTHORIZED → PUBLISHING` após rechecagem **just-in-time** de revisão-base, autorização e política;
- `PUBLISHING → PUBLISHED` somente com confirmação de atualização oficial e recibo correlacionado;
- `PUBLISHED → VERIFIED` após pós-verificações obrigatórias;
- `PUBLISHED → POST_PUBLISH_FAILED` se pós-verificação crítica falha: **o conteúdo continua historicamente publicado, mas a revisão não pode ser ativada**; recuperação por novo ChangeSet/retificação autorizada;
- `PREPARED/VALIDATED/AUTHORIZED → CONFLICT/BLOCKED/FAILED`, de onde a retomada deve gerar nova tentativa reconciliada validada, sem saltar gates;
- `DRAFT/PREPARED → ABORTED` quando cancelado sem publicação; depois de `PUBLISHED` não se usa `ABORTED` como se nenhuma escrita tivesse ocorrido.

`publication_state` de CT-002 mapeia o resultado externo: `EM_PUBLICACAO`, `PUBLICADO`, `VERIFICADO`, `FALHA_POS_PUBLICACAO` etc. `activation_state` e o `EffectiveManifest` determinam vigência. Nenhum agente deve inferir `VERIFICADO` de `PUBLISHED`, nem `VIGENTE` de `VERIFICADO`.

## 3. Protocolo de preparação

1. Receber solicitação de CT-001 e registros válidos de CT-002.
2. Consultar a revisão oficial `R0`, o manifesto **efetivo** e a política `P0` vigente (salvo bootstrap inicial, § 3.1).
3. Identificar arquivos/registros afetados e referências canônicas.
4. Solicitar ao CT-004 o `ImpactPlan` e todas as `required_invalidations` conhecidas.
5. Preparar **integralmente**, em snapshot/branch isolado, diff, invalidações, índices e manifestos candidatos; calcular `expected_result_digest` sobre o conjunto exato (`DRAFT → PREPARED`).
6. Executar os **pré-testes** estruturais, de segurança, versionamento, impactos e integridade contra o **candidato completo e estável** (`PREPARED → VALIDATED`).
7. Obter ou conferir aprovação vinculada ao objeto, escopo e digest **desse resultado validado**; CT-001 interpreta escopo e CT-005 autentica identidade/permissão (`VALIDATED → AUTHORIZED`).
8. Imediatamente antes da gravação, revalidar CAS/revisão-base, política vigente, ausência de revogação, permissão, digest e condições de pré-teste (`AUTHORIZED → PUBLISHING`). Se o conteúdo ou impactos mudarem, retornar a PREPARED/VALIDATED e renovar aprovação quando material.
9. Publicar **consistentemente** a revisão preparada com as invalidações, sem ativá-la automaticamente (`PUBLISHING → PUBLISHED`).
10. Executar pós-verificações obrigatórias e preservar resultado (`PUBLISHED → VERIFIED` ou `POST_PUBLISH_FAILED`).
11. Se for alteração normativa, somente **após VERIFIED**, autorizar e ativar o `EffectiveManifest` condicionalmente (§ 5.1); C0/C1 não requerem ativação. Comunicar estados e recibos reais.

Caso os artefatos dependentes não possam ser todos corrigidos, é permitido publicar a alteração com **marcação de desatualização atômica** dos dependentes conhecidos e bloqueios apropriados. Não é permitido omitir silenciosamente essas marcações.

### 3.1. Ratificação inicial de uso único — EM-001

Se não existir `effective_policy_ref`, a primeira ativação do PGC exigirá `BootstrapRatification` conforme CT-002: ratificação **manual e inequívoca** do responsável autorizado pelo pacote identificado por versões/digests, comprovação do estado inicial sem política vigente, permissões reais no destino, registro auditável e ativação condicionada **exatamente uma vez**. O bootstrap não pode ser invocado se já houver manifesto vigente nem servir para autorizar alterações futuras. Na ausência de identidade ou destino verificáveis, o pacote permanece **PROPOSTO**. A publicação do marco pode usar procedimento manual externo ao harness ainda não implementado, mas não pode ser descrita como execução autônoma validada.

### 3.2. Invariante de ordem — EM-003

Pré-validações verificam o snapshot **completo** antes de obter aprovação para seu digest; a checagem just-in-time imediatamente anterior à publicação é uma **rechecagem**, não um atalho que autoriza alterar conteúdo depois da aprovação. Falha ou mutação material exige nova preparação, pré-teste e aprovação. A política vigente pode exigir verificações adicionais sem inverter `PREPARED → VALIDATED → AUTHORIZED`.

## 4. Porta de publicação — condições simultâneas

A operação só poderá avançar para mudança do estado oficial se, **no instante efetivo da publicação**; a ativação tem condições adicionais na seção 5.1:

`base_revision_compatible AND current_policy_authorizes AND approval_matches_digest_and_scope AND schema_valid AND required_impact_marks_present AND no_unresolved_blocking_conflict AND prechecks_pass AND destination_permission_valid AND prepared_candidate_digest_unchanged`.

Revisão-base e política vigente devem ser verificadas sob uma estratégia que impeça corrida TOCTOU (check/use) material. Se não houver verificação suficientemente forte, bloquear publicação automática, exigir serialização/lock ou nova reconciliação. Para mudança da política em si, os verificadores utilizam **P0 anterior**; a candidata **P1 não avalia a própria aprovação**. Na instituição inicial sem P0, vale exclusivamente o procedimento limitado de bootstrap (§ 3.1), sem alegar que P1 autoriza a si própria.

A mera existência de `approval_refs[]` não basta: conferir assinatura/identidade exigida, estado não revogado, revisão e digest correspondentes. A reconciliação de merge/rebase que altere conteúdo material invalida a aprovação anterior; não proceder com `AUTHORIZED` antigo.

## 5. Publicação e concorrência

**Estratégia de referência Git possível:** criar branch isolado sobre `R0`; executar lints e revisão; solicitar merge condicional ao HEAD esperado da branch canônica; verificar branch protection/CI; registrar commit `R1`. O mecanismo deverá impedir force overwrite não autorizado. A estratégia específica é decisão de implementação — **não alegar** que GitHub ou o ChatGPT assegurará esse comportamento sem configuração e testes.

Se HEAD ou política mudar, entrar em `CONFLICT` ou `BLOCKED`, reabrir diff contra nova revisão, reavaliar invalidações, reaplicar prechecks e verificar aprovação. Não misturar mudanças concorrentes com `git reset --hard` ou overwrite de arquivo sem reconciliação.

Para operações em múltiplos repositórios, exigir plano de publicação com ordem, contrato de compatibilidade, estado de ativação e recuperação; sem transação distribuída comprovada, não declarar instantaneidade global.

### 5.1. Gate de ativação normativa — EM-004

Para operações normativas, `PUBLISHED` designa gravação no repositório, **não vigência**. `VERIFIED` designa aprovação dos **pós-testes críticos**, mas tampouco implica vigência. A entrada em vigor depende de uma atualização condicional, serializável e verificável de `EffectiveManifest` (CT-002), apontando para a revisão `R1` e conjunto de invalidações, com verificação da versão do manifesto e política aplicável. Leitores críticos devem resolver definições normativas pela referência vigente do manifesto, **nunca simplesmente pelo último commit**.

**Portão de ativação:** `published_receipt_valid ∧ postchecks_critical_passed ∧ approval_still_valid ∧ current_policy_authorizes ∧ manifest_revision_compatible ∧ activation_permission_valid ∧ invalidations_in_snapshot`. Se qualquer termo obrigatório for desconhecido, bloquear. Se a atualização do manifesto retornar timeout, consultar estado real antes de repetir; se indeterminado, usar `activation_state=INDETERMINADA`, não `VIGENTE`. Após confirmação, marcar nova revisão `VIGENTE` e anterior `SUBSTITUIDA`, preservando histórico. O manifesto e seu ponteiro devem ser protegidos por CAS/controle equivalente.

**Falha antes da ativação:** gravação permanece historicamente `PUBLISHED`/`POST_PUBLISH_FAILED`, mas **não** se torna vigente; a versão anterior continua ativa. **Falha descoberta após ativação:** registrar evento, aplicar contenção de CT-005 e executar reparo/reversão autorizado, sem negar ativação histórica. Sistemas externos ou múltiplos destinos só podem alegar consistência de ativação se todos os leitores obrigatórios observarem o manifesto ou mecanismo equivalente; sem isso, bloquear a ativação automática.

## 6. Idempotência, recibos e timeouts

Cada `idempotency_key` identifica um `request_digest` imutável. Reutilizar a mesma chave com payload divergente é erro bloqueante. Repetição exata deve retornar o mesmo resultado observado ou consultar destino. Se uma chamada de publicação retornar timeout, **não repetir cegamente**:

1. Consultar histórico/commit/recibo pela identidade do ChangeSet.
2. Se `R1` já está oficial e conteúdo corresponde, registrar publicação efetiva e continuar pós-verificações.
3. Se o estado é comprovadamente anterior, reaplicar somente após rechecagem de gates.
4. Se indeterminado, colocar em `BLOCKED` e escalar; não anunciar sucesso nem presumir falha.

A criação da auditoria e a emissão de eventos não podem produzir dupla execução por simples retry; utilizar outbox, correlação ou deduplicação testada, quando aplicável.

## 7. Falha após publicação

Falha de pós-verificação **não apaga** o commit realizado. O ChangeSet passa a `POST_PUBLISH_FAILED`; leitores e automações críticas devem receber sinal de integridade comprometida/quarentena conforme risco, até novo ChangeSet corretivo. Reversão (revert) deve ser **nova publicação autorizada e verificada**, conservando histórico. Se falha afetar segurança, CT-005 poderá exigir suspensão operacional imediata.

Se erro afetar apenas relatório ou índice derivado não crítico, política pode permitir reparo controlado; a classificação precisa constar da verificação e não pode mascarar falha obrigatória.

## 8. Critérios de conclusão e evidências

Para `VERIFIED`: (a) revisão `R1` localizada no destino oficial; (b) objeto e digest correspondem ao resultado autorizado; (c) invalidações obrigatórias presentes; (d) checks pós-publicação executados e aprovados; (e) recibo/auditoria persistidos; (f) pendências não bloqueantes identificadas. Para `VIGENTE`, exigir ainda **recibo da atualização condicional do EffectiveManifest**, verificação do ponteiro ativo e manutenção das permissões vigentes. A comunicação ao usuário distingue `PREPARED`, `PUBLISHED`, `VERIFIED`, `VIGENTE` e `POST_PUBLISH_FAILED`.

**Dependências:** CT-001 classifica; CT-002 modela; CT-004 fornece invalidações; CT-005 verifica autoridade; CT-006 coordena retomada; CT-008 testa. NENHUM outro contrato é publicador alternativo.

**Aceite:** CA-07, 08, 11, 12, 14, 15, 17, 18, 28, 31, 32, 34, 35, 37, 39, 40, 42, 43, 45, 46, 47.
