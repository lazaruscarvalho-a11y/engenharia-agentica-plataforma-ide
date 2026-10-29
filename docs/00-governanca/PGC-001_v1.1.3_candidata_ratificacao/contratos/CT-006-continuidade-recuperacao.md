# CT-006 — Sessões, continuidade, operações pendentes e recuperação

**Versão:** 1.0.3 · **Estado:** PROPOSTO · **Norma:** PGC-001 v1.1.3  
**Dono exclusivo:** coordenação de sessões e retomada de trabalho. **Não** executa publicação diretamente: utiliza a API/contrato CT-003.

## 1. Objetivo e limitação honesta

Uma conversa nova deve recuperar o estado documentado acessível sem presumir memória integral, monitoramento automático de todas as sessões ou sincronização não implementada. A obrigação de **capturar automaticamente** contribuições só pode ser operacionalizada se `capture_mode=CAPTURA_AUTOMATICA_CONECTADA` e um mecanismo real, acessível e autorizado receber o conteúdo e puder persistir seu resultado. Por padrão, `CAPTURA_ASSISTIDA_NA_SESSAO` captura semanticamente apenas no contexto presente, sem afirmar gravação.

Na ausência de escrita, produzir proposta de alteração e declarar `NAO_PERSISTIDO`. Não afirmar que uma fila ou arquivo inexistente guarda decisões para retomada futura.

### 1.1. Modos de captura e status real — EM-005

`DESABILITADA`: não iniciar registro automático. `CAPTURA_ASSISTIDA_NA_SESSAO` (**padrão inicial**): interpretar mensagens acessíveis e produzir candidatos; persistir C0/C1 só se houver ferramenta, autorização e recibo; sem isso, indicar `NAO_PERSISTIDO`. `CAPTURA_AUTOMATICA_CONECTADA`: exige ingestão de sessões por conector explícito autorizado, mecanismos de deduplicação, política de dados, CT-003 para escrita e monitoramento de falhas; não se deve presumir esse modo apenas por criar um Projeto do ChatGPT.

Para registros C0/C1, o resultado deve indicar ao menos `capturado_semanticamente`, `persistido_exploratorio` ou `nao_persistido`, com comprovante quando houver gravação. Persistir não significa aprovar. Falhas de ingestão não podem ser escondidas nem prometidas como sincronizadas em sessões futuras.
## 2. Inicialização orientada à tarefa

Ao iniciar atividade que dependa do Projeto:
1. Identificar intenção (esclarecimento, brainstorming, requisito, revisão, execução).
2. Ler instruções do Projeto e PGC-001 vigente acessível.
3. Consultar o **EffectiveManifest vigente**, `ESTADO-ATUAL.md` e índices pertinentes conforme CT-007; quando não houver manifesto (antes da ratificação), distinguir expressamente o estado PROPOSTO.
4. Recuperar registros normativos relevantes pela **referência ativa do manifesto**, além da revisão do repositório, decisões vigentes, dependências e pendências; não presumir que o HEAD é a política em vigor.
5. Registrar no contexto de execução quais revisões foram consultadas.
6. Informar materialmente limitações de acesso, contradições e desatualizações que afetem a resposta.
7. Trabalhar sem cerimônia desnecessária em perguntas simples.

O contexto insuficiente deve gerar consulta adicional ou pendência explícita; **não** preencher documentos não lidos por palpite.

## 3. Estado de atividade e estado de publicação

`WorkItem` é uma entidade de coordenação separada do `ChangeSet`: `work_id`, `goal`, `domain`, `context_refs`, `base_repo_revision`, `owner`, `dependencies`, `progress_state`, `related_change_id?`, `next_action`, `retry_count`, `last_observed_receipt`, `updated_at`.

`progress_state`: `PLANEJADO`, `EM_EXECUCAO`, `AGUARDANDO_INFORMACAO`, `AGUARDANDO_AUTORIZACAO`, `BLOQUEADO`, `CONCLUIDO`, `CANCELADO`. Esse estado não substitui `publication_state` nem `verification_state`. Uma tarefa pode estar CONCLUIDA no preparo de proposta, enquanto publicação permanece não realizada.

## 4. Registro durável de pendências

Se um ChangeSet ou decisão não puder ser publicado, registrar `PendingOperation` em armazenamento durável autorizado **quando disponível**: `operation_id`, `request_digest`, `base_revision`, `destination`, `candidate_ref`, `approval_refs`, `block_reason`, `last_known_state`, `recovery_action`, `created_at/updated_at`. Referir-se ao recibo CT-003, sem reproduzir segredos.

Se não houver armazenamento durável, emitir ao usuário artefato de proposta ou patch identificável (quando possível), informar que a pendência está somente na resposta ou arquivo fornecido e **não garantir** recuperação automática em outra conversa. Memória do ChatGPT não equivale a fila transacional.

## 5. Retomada depois de interrupção

1. Identificar `work_id`, `operation_id` e `change_id` existentes.
2. Consultar recibos duráveis, revisão oficial atual e **manifesto de ativação vigente**, se existir.
3. Para publicação incerta após timeout, **pedir ao CT-003 que consulte o destino antes de reenviar**.
4. Detectar alterações concorrentes, revisões de política e aprovações expiradas/revogadas.
5. Reavaliar contexto e dependências segundo CT-004.
6. Prosseguir somente com etapas pendentes; qualquer mudança material deve reentrar na validação e autorização.
7. Registrar status final ou bloqueio, com evidências.

Nunca afirmar rollback por apagar um registro do `WorkItem`: o commit e efeitos externos exigem confirmação e, se necessário, nova operação compensatória.

## 6. Limites de tentativas e escalonamento

O projeto deve estabelecer por tipo de operação: número máximo de novas tentativas, atraso/recuo, condição de falha permanente e responsável pelo escalonamento. Valores são configuração dependente de risco; **não estão aprovados neste contrato**.

Padrão seguro enquanto esses parâmetros não estiverem definidos: não repetir automaticamente publicação de estado desconhecido nem execução destrutiva. Uma tarefa que progride em investigação pode continuar com limites operacionais definidos no ambiente; não se permite loop indefinido sem evidência de progresso.

## 7. Sessões paralelas

Sessões podem elaborar candidatos paralelos sobre a mesma fonte, mas toda operação normativa deve passar pela verificação de revisão-base e autorização no CT-003. `ESTADO-ATUAL.md` é resumo e não pode funcionar como mutex/lock; o repositório/manifesto oficial continua sendo autoridade.

### 7.1. Distinção de revisão oficial e vigência — EM-004

Ao recuperar uma tarefa interrompida, diferenciar os recibos de gravação (`PUBLISHED`), pós-verificação (`VERIFIED`) e ativação (`VIGENTE`). Se uma revisão candidata foi publicada sem ativação, retomar pós-verificações ou gate de ativação por CT-003; **não** comunicar a candidata como regra vigente. Em timeout da ativação, solicitar ao CT-003 verificação do manifesto, sem repetir cegamente. Se o manifesto for inacessível, não reconstruir a política por dedução da conversa.
## 8. Encerramento e transparência

Ao finalizar trabalho relevante, reportar: objetivo, decisões e alterações propostas, revisão consultada, operações publicadas (com recibo), falhas/bloqueios, fontes ausentes, próximo passo. Não criar relatório burocrático para dúvida trivial. Estado comunicado deve refletir **o último estado comprovado**.

## 9. Exceções

- Fonte canônica inacessível → não presumir revisão atual.
- Timeout de gravação → consultar destino pelo CT-003; não duplicar.
- Confusão entre proposta e publicação → corrigir status, informar.
- Mudança em requisito durante execução → reavaliar trabalho antes de declarar conformidade.
- Operação parcialmente aplicada em destino externo → registrar quais efeitos foram observados e iniciar recuperação autorizada.
- Armazenamento de pendências indisponível → sinalizar risco de perda e entregar proposta utilizável.

**Aceite:** CA-09, CA-13 a CA-18, CA-29, CA-35, CA-36, CA-39, CA-46, CA-47 e CA-48. O teste de continuidade deve simular **nova sessão sem acesso ao histórico de chat**, utilizando somente fontes que seriam realmente acessíveis.
