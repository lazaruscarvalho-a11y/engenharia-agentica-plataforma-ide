# CT-002 — Modelo de registros, identificadores, versões e proveniência

**Versão:** 1.0.3 · **Estado:** PROPOSTO · **Norma:** PGC-001 v1.1.3  
**Dono exclusivo:** esquemas, identidade lógica, proveniência e tipos de versionamento. **Não** decide o que foi aprovado nem publica arquivos.

## 1. Objetivo e estrutura canônica

Definir representações que agentes independentes possam produzir e validar sem inventar semânticas incompatíveis. O armazenamento pode ser Markdown com metadados estruturados, JSON/YAML ou banco de dados; a escolha da tecnologia é aberta, mas a **semântica dos registros e validações abaixo é obrigatória**.

**Entidades:** `KnowledgeRecord` (IDEA, DECISION, REQUIREMENT, RESTRICTION, RISK, PENDING, EVIDENCE), `Source`, `Relationship`, `Approval`, `ChangeSet`, `OperationReceipt`, `PolicyRevision`, `EffectiveManifest`, `BootstrapRatification`, `DependencySnapshot` e `ValidationReport`. Entidades têm esquemas especializados com `schema_version` explícito.

## 2. Campos e estados ortogonais

Registro mínimo:

```yaml
schema_version: '1.0.2'
record_id: 'urn:pgc:rec:uuid-exemplo' # identidade imutável
human_id: RF-AGT-007                # alias legível, único após publicação
kind: REQUIREMENT
canonical_ref: docs/03-requisitos/agentes.md#rf-agt-007
record_revision: 3
maturity_state: APROVADO
freshness_state: CURRENT
implementation_state: NAO_INICIADO
verification_state: NAO_VERIFICADO
activation_state: VIGENTE           # somente se apontado pelo manifesto ativo
source_refs: [SRC-0007]
relationship_refs: [REL-0013]
content_digest: 'sha256:<valor-calculado>'
```

O exemplo é ilustrativo e não constitui requisito aprovado nem hash verdadeiro. `publication_state` pertence à **revisão/ChangeSet publicado**, não deve ser inferido apenas do campo `maturity_state`. `approval_state` pertence à aprovação vinculada à revisão. Campos desconhecidos não são preenchidos por hipótese; registrar ausência conforme a política de validação por tipo.

### Vocabulário de estados

| Dimensão | Valores iniciais | Dono da regra de transição |
|---|---|---|
| `maturity_state` | CAPTURADO, EM_ANALISE, PROPOSTO, APROVADO, SUSPENSO, DESCARTADO, SUBSTITUIDO | CT-001 |
| `approval_state` | NAO_REQUERIDA, PENDENTE, VALIDA, REVOGADA, EXPIRADA, INVALIDADA_POR_MUDANCA, REJEITADA | CT-001 + CT-005 |
| `publication_state` | NAO_PUBLICADO, EM_PUBLICACAO, PUBLICADO, VERIFICADO, FALHA_POS_PUBLICACAO, BLOQUEADO, ABORTADO | CT-003 |
| `activation_state` | NAO_APLICAVEL, PENDENTE_ATIVACAO, VIGENTE, SUSPENSA, SUBSTITUIDA, INDETERMINADA | CT-003 (referência/manifesto de vigência) |
| `freshness_state` | CURRENT, POTENTIALLY_STALE, STALE, UNDER_REVALIDATION, BLOCKED | CT-004 |
| `implementation_state` | NAO_INICIADO, EM_EXECUCAO, CONCLUIDO, BLOQUEADO, NAO_APLICAVEL | Ciclo de execução, futuro contrato de implementação |
| `verification_state` | NAO_VERIFICADO, EM_VERIFICACAO, APROVADO_NOS_TESTES_DEFINIDOS, REPROVADO, INCONCLUSIVO, NAO_APLICAVEL | CT-008 (e avaliações de produto) |

A implementação deve rejeitar transições inválidas, **distinguir a revisão publicada da revisão vigente** e proibir equivalência entre os estados de dimensões diferentes e não tratar `APROVADO_NOS_TESTES_DEFINIDOS` como ausência universal de defeitos. Os valores podem evoluir somente por migração de esquema controlada.

## 3. Quatro identificações distintas de versão

1. **`record_id`**: identifica o objeto lógico para sempre; não muda ao renomear ou mover arquivo.
2. **`record_revision`** e `content_digest`: identificam conteúdo de uma revisão da entidade; revisão vigente separada da candidata.
3. **`repository_revision`**: identifica instantâneo/commit da fonte documental oficial e serve como base para controle de concorrência.
4. **`policy_revision`**: identifica o conjunto de regras **vigente** usado para autorizar uma operação, inclusive alterações ao próprio protocolo.

Uma quinta versão, `schema_version`, indica o formato dos registros. Nenhuma delas pode ser substituída pelo nome do arquivo ou pela data. Referências devem explicitar qual tipo de versão representam.

## 4. Digest e aprovação

O `content_digest` é calculado sobre uma representação canônica do **conteúdo normativo do objeto aprovado**, incluindo IDs, regra e escopo, com normalização definida no harness; excluir apenas metadados voláteis explicitamente permitidos. O mesmo algoritmo e normalização são usados em preparação, aprovação e pré-publicação. Alteração que preserve aparência mas modifique significado não pode ser ignorada com alegação de 'editorial'.

`Approval` mínimo: `approval_id`, `approval_kind` (`INTENCAO_PRODUTO` ou `REVISAO_NORMATIVA`), `actor_identity_ref`, `authority_context`, `source_event_ref`, `object_id`, `object_revision`, `content_digest`, `scope`, `decision`, `conditions`, `policy_revision_used`, `issued_at`, `approval_state`, `revocation_ref?`, `evidence_ref`. **Condicionalidade obrigatória por tipo:** para `REVISAO_NORMATIVA`, `object_id`, `object_revision`, `content_digest` e `scope` são obrigatórios e devem corresponder ao snapshot preparado. Para `INTENCAO_PRODUTO`, `source_event_ref`, `scope` restrito às palavras realmente decididas e identidade de origem são obrigatórios; `object_revision`/`content_digest` normativos não são aplicáveis até existir revisão formal. A intenção deve ser associada a um registro de decisão com sua própria identidade, sem inventar `content_digest` de documento não aprovado. A autenticidade é verificada por CT-005; a semântica por CT-001. Expiração ou revogação deve bloquear novos usos, sem apagamento do histórico.

**Data de emissão — EM-008:** no objeto `Approval`, `issued_at` possui a mesma semântica de CT-001 §6: instante da emissão pela autoridade, em ISO 8601 com fuso, distinto de criação de rascunho, publicação e ativação. `created_at` não é alias desse campo. A ausência ou ambiguidade em dados legados exige evidência e mapeamento explícito; não preencher por inferência.

### 4.1. Modelo de vigência — EM-004

`EffectiveManifest` registra `manifest_id`, `manifest_revision`, `effective_policy_ref`, `effective_record_refs`, `repository_revision`, `parent_manifest_revision?`, `activation_cas_token`, `activated_at` e `activation_receipt`. **Somente** a referência/manifesto oficialmente ativado determina a revisão normativa vigente; uma revisão com `publication_state=PUBLICADO` ou mesmo `VERIFICADO` sem ativação continua não vigente. Conteúdos C0/C1 usam `activation_state=NAO_APLICAVEL`.

A atualização do manifesto deve ser condicional e consistente; sua semântica é definida no CT-003. Se a operação de ativação retornar timeout e não for possível identificar o estado efetivo, usar `activation_state=INDETERMINADA` e bloquear alegações de vigência. Não pode haver duas revisões simultaneamente vigentes para o mesmo `record_id` no mesmo escopo. A revisão anterior só se torna `SUBSTITUIDA` após ativação comprovada de sua sucessora.

`BootstrapRatification` (somente na primeira instituição) contém `bootstrap_id`, `actor_identity_ref`, `authorization_evidence_ref`, `package_manifest`, `package_digest`, `first_effective_manifest_ref`, `no_prior_effective_policy_evidence`, `activation_receipt`, `issued_at`. Não pode existir uma segunda ratificação inicial válida quando já houver política vigente. A ratificação em papel/diálogo **não** substitui permissão efetiva de escrita.
## 5. Fonte canônica única

Manter um **registro de identidades canônicas**: `record_id -> canonical_ref` na revisão oficial. Um `record_id` não pode apontar para duas fontes canônicas ativas; dois registros diferentes não podem reivindicar o mesmo `human_id` no mesmo namespace. Mudança de caminho atualiza apenas a referência, não a identidade. CT-007 gerencia a disposição física; CT-003 impõe a unicidade no gate de publicação.

Documentos agregadores podem referenciar registros canônicos, mas reproduções textuais não se tornam novas fontes de autoridade. Um dado que exista apenas em uma proposta não é registro normativo vigente.

## 6. Proveniência e confiança

`Source` deve admitir: `source_id`, `source_type` (usuario-direto, arquivo, transcricao, documentacao, pesquisa, ferramenta, inferencia), `locator`, `source_version_or_snapshot`, `retrieved_at?`, `accessibility_state` (ACCESSIBLE, INACCESSIBLE, REMOVED, UNKNOWN), `data_classification`, `authority_level`, `verification_level`, `usage_permission`, `retention_policy_ref`, `evidence_excerpt_ref?`.

**Três eixos separados:** (i) **proveniência** — de onde veio; (ii) **autoridade** — quem pode determinar regra; (iii) **confiança factual** — quanto foi validado. Exemplo: usuário pode ter autoridade para escolher UX, mas sua fala sobre endpoint interno sem evidência é um relato e não documentação de API confirmada.

Se a fonte se tornar inacessível, preservar marcador `INACCESSIBLE` e não fabricar link ou trecho. Dados sensíveis não devem ser replicados indiscriminadamente para garantir rastreabilidade: registrar hash/referência ou evidência saneada quando necessário e autorizado.

## 7. Relações e snapshots de dependência

`Relationship`: `relationship_id`, `source_record_id`, `target_record_id` ou `external_ref`, `relation_type` (`originated_from`, `depends_on`, `implements`, `constrains`, `replaces`, `complements`, `contradicts`, `verifies`, `affects`, `references`), `evidence_ref?`, `confidence_class`, `source_revision`, `target_revision?`, `state`.

`DependencySnapshot`: revisões dos registros de origem e dependências críticas usadas por um artefato derivado, com avaliação de atualidade segundo CT-004. Relações circulares são permitidas somente onde semanticamente válidas; os algoritmos precisam detectar ciclos para evitar processamento infinito.

## 8. ChangeSet e recibos

`ChangeSet` contém `change_id`, `idempotency_key`, `request_digest`, `base_repository_revision`, `policy_revision_at_authorization`, lista de operações e documentos, invalidações de CT-004, aprovações, prechecks, status, `published_repository_revision?`, `postcheck_results?` e `activation_receipt?`. O `idempotency_key` associado a **payload diferente** é erro, não autorização para segunda ação.

`OperationReceipt` contém identidade e resultado de leitura/escrita/comparação/publicação; distingue operação enviada, execução concluída, publicação verificada e estado desconhecido após timeout.

### 8.1. Modelo de captura — EM-005

Uma configuração `CapturePolicy` mantém `capture_mode`, escopo das fontes, permissão de ingestão, classificação de dados, destinos permitidos, deduplicação e mecanismo durável (quando houver). `CAPTURA_ASSISTIDA_NA_SESSAO` é o modo inicial; `CAPTURA_AUTOMATICA_CONECTADA` requer conector funcional, autorização, recibos e política de retenção. A captura sem armazenamento durável deve produzir `NAO_PERSISTIDO` e não criar referências fictícias.
## 9. Esquemas e migrações

Cada tipo deve ter esquema formal verificável (por exemplo JSON Schema) antes da implementação operacional de gravação normativa. Regras de validação: IDs únicos, campos obrigatórios por tipo, vocabulários, tipos, relacionamento válido, revisões, digest, autoridade e referência canônica.

Mudança incompatível no esquema exige migração versionada e reversão/recuperação testada; um agente não pode reinterpretar silenciosamente registros antigos. Campos sensíveis precisam de política de armazenamento, saneamento e retenção conforme CT-005.

## 10. Falhas e aceite

Falhas: ID duplicado → bloquear; tipo/estado inválido → bloquear ou manter proposta não publicada; fonte ausente → marcar inacessível; digest divergente → invalidar aprovação; registro canônico duplicado → rejeitar; esquema incompatível → exigir migração; origem incerta → manter evidência como não confirmada.

**Aceite:** CA-11, CA-26, CA-27, CA-30, CA-32, CA-33, CA-39, CA-42, CA-43, CA-46 e CA-49; medição conforme CT-008.
