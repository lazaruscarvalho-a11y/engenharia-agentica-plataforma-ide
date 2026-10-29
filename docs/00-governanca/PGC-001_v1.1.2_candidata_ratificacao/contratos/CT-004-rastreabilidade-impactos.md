# CT-004 — Rastreabilidade, impactos e invalidação

**Versão:** 1.0.2 · **Estado:** PROPOSTO · **Norma:** PGC-001 v1.1.2  
**Dono exclusivo:** cálculo, classificação e verificação de impactos. **Não** publica arquivos; fornece alterações de invalidação ao CT-003.

## 1. Objetivo

Preservar relações versionadas entre necessidades, fontes, decisões, requisitos, experiência visual, arquitetura, planos de implementação, testes e evidências. Detectar quando uma alteração exige reavaliação de seus dependentes, impedindo o uso silencioso de documentos reconhecidamente incompatíveis.

Uma relação conhecida não prova que todas as relações possíveis foram descobertas. O sistema deve diferenciar cobertura comprovada de dependências mapeadas de alegação impossível de completude absoluta.

## 2. Relações e versões

Empregar o modelo CT-002: `source_record_id`, `target_record_id/external_ref`, `relation_type`, `source_revision`, `target_revision?`, `evidence_ref`, `confidence_class`, `state`. Relações importantes: `originated_from`, `depends_on`, `implements`, `constrains`, `replaces`, `complements`, `contradicts`, `verifies`, `affects`, `references`.

Artefatos derivados devem guardar um **DependencySnapshot** das revisões e, quando necessário, digests das fontes críticas usadas em sua construção. Não basta comparar nomes de arquivos. Mudanças de path não invalidam relações que usam IDs lógicos estáveis.

## 3. Estado de atualidade (`freshness_state`)

- `CURRENT`: revisões críticas conhecidas foram reavaliadas; não garante descoberta de toda dependência externa.
- `POTENTIALLY_STALE`: alguma origem mudou e impacto material ainda não foi resolvido.
- `STALE`: incompatibilidade com origem vigente confirmada.
- `UNDER_REVALIDATION`: verificação em andamento, sem reabilitar automaticamente uso crítico.
- `BLOCKED`: artefato inadequado para usos críticos determinados até nova validação.

Transições exemplares: `CURRENT → POTENTIALLY_STALE` na publicação de alteração potencialmente impactante; `POTENTIALLY_STALE → UNDER_REVALIDATION → CURRENT` se conformidade reatestada; `UNDER_REVALIDATION → STALE/BLOCKED` se falhar; `STALE/BLOCKED → UNDER_REVALIDATION` após correção candidata. **Somente** validação com evidências altera a condição para `CURRENT`. Não substituir `freshness_state` por `maturity_state` ou `verification_state`.

## 4. Gatilhos e cálculo

Gatilhos: requisito/decisão/contrato alterado, aprovação revogada com efeitos, fonte essencial contradita, dependência descoberta, política modificada, mudança arquitetural material ou teste invalidado.

Ao receber uma proposta de alteração sobre revisão `R0`:
1. Identificar objetos alterados e sua versão.
2. Percorrer relações diretas e, de forma controlada, transitivas (detecção de ciclos e limite de escopo explícito).
3. Classificar cada relação: `IMPACTO_CONFIRMADO`, `IMPACTO_POTENCIAL`, `NAO_MATERIAL`, `INDETERMINADO`, com justificativa.
4. Produzir `ImpactPlan` com dependentes, revisões-base, flags obrigatórias, riscos e verificações propostas.
5. Encaminhar ao CT-003, **antes da publicação**, um conjunto `required_invalidations` de dependentes conhecidos que ainda não foram atualizados/revalidados.
6. Após gravação e antes de ativação, exigir que as flags estejam no snapshot que o manifesto ativará. Depois da ativação, disparar revalidações permitidas sem tratar sua execução tardia como substituto das marcas de invalidação obrigatórias.

Dependentes não descobertos não podem ser magicamente marcados; prever checagem na leitura comparando snapshot de dependência conhecido contra revisões vigentes, além de verificações periódicas quando implementadas.

## 5. Visibilidade atômica das invalidações

A **ativação normativa** da revisão `R1` e das marcações mínimas de invalidação dos dependentes conhecidos deve tornar-se **visível como um único estado lógico** por intermédio do manifesto efetivo de CT-003. Um commit `R1` ainda não vigente pode estar publicado sem autorizar leitores críticos a tratar seu conteúdo como norma. É proibido publicar o novo requisito, manter planos antigos como `CURRENT` no estado visível e só depois rebaixá-los.

Duas estratégias aceitáveis, condicionadas a testes:
- Preparar requisito e flags dos dependentes **no mesmo ChangeSet/snapshot**, tornando-os vigentes somente via ativação condicional.
- Utilizar o `EffectiveManifest` oficial de CT-002 para associar `R1` e lista de invalidações como **uma única unidade vigente** consultada por todos os leitores críticos; nenhum leitor pode ignorar o manifesto.

O CT-003 é o único publicador. CT-004 não modifica o repositório diretamente.

### 5.1. Proibição de janela de vigência inconsistente — EM-004

Na leitura normativa crítica, a revisão vigente de um requisito e os estados `freshness_state` de seus dependentes devem ser resolvidos no **mesmo snapshot efetivo**. Conteúdo recém-publicado mas ainda não ativado não deve disparar ações críticas nem invalidar retroativamente o estado da versão anterior. Caso uma gravação tenha passado por pós-verificação e falhado no portão de ativação, os dependentes continuam com a condição publicada no manifesto anterior; a candidata e suas flags ficam aguardando ativação. Falha de pós-verificação bloqueia ativação, com registro do defeito.
## 6. Revalidação e uso seguro

Cada dependente sinalizado deve ter resultado: revisado sem mudança, atualizado, bloqueado ou pendente, com evidências, revisão da origem, revisor/controle e data quando disponível. Um plano de implementação ou teste `STALE/BLOCKED` não pode ser fonte de conformidade nem autorizar ação crítica; exceções exigem política e autorização explícitas. Tarefas independentes podem continuar se análise de impacto demonstrar ausência de dependência material.

Revisão de requisito não obriga descartar todo o código anterior: exige avaliar diferenças e repetir verificações afetadas. Aprovado/código implementado não implica CURRENT sem verificação compatível com as fontes vigentes.

## 7. Revogação e conteúdo histórico

Revogar aprovação não apaga decisão e publicação históricas; gera evento para nova análise de impacto. CT-003 registra o ChangeSet que suspende/sinaliza dependentes quando exigido. Manter trilha `decision A → replaced_by B`, inclusive motivos e revisões; preservar dados conforme a política de retenção.

## 8. Falhas e limites

Grafo incompleto → declarar cobertura conhecida e pendências; ciclo → evitar recursão infinita; relação inválida → bloquear ou isolar o impacto; falha na análise crítica → impedir publicação que dependa de invalidação obrigatória; arquivo derivado removido → registrar referência inválida, não inventar evidência. O limite do algoritmo deve ser configurado e auditado, não usado para ocultar impacto conhecido.

**Aceite:** CA-09, CA-10, CA-27, CA-28, CA-30, CA-34, CA-37, CA-46 e CA-47. Cada avaliação deve demonstrar quais dependentes foram analisados e o estado oficial simultaneamente visível.
