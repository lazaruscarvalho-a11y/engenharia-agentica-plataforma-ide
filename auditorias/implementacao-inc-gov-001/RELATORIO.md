# Implementação inicial do fluxo assistido

**INC-GOV-001 v0.1.0 — 30/10/2026. Implementação inicial disponível; aceite operacional pendente. PGC NÃO RATIFICADO. Sem merge na principal.**

## Autorização e escopo

O usuário aprovou a proposta INC-GOV-001 v0.1.0 e suas três escolhas: dados sintéticos, um registro por vez e branch de piloto separada. A proposta aceita está preservada no commit `50a37b409370bae058b6514dd2d5ba99726c416f`, arquivo `docs/06-execucao/propostas/INC-GOV-001-fluxo-assistido.md`, SHA-256 `0f54a70e51c226ae67421bcc05d08d921f847e6d7cb2fdecf5201c40ed3805b5`. A manifestação foi recebida diretamente nesta conversa em 30/10/2026. Sua referência técnica individual e horário de emissão não foram fornecidos nesta entrega; não foram inventados nem convertidos em um aceite de registro futuro.

O pedido autoriza implementar, testar e preparar a operação assistida. Nenhuma decisão humana simulada dos ensaios é apresentada como consentimento real. O primeiro registro sintético aguarda apresentação do pacote final e aceite próprio, conforme GOV-RF-004 da proposta aprovada.

## Entrega técnica

O [núcleo](../../harness/governanca_assistida/fluxo.py) prepara conteúdo determinístico, vincula revisão e hash, verifica escopo, coordena escrita condicional pelo adaptador, controla repetição por diário local e separa conteúdo, aceite, recibo e índice. Há tratamento de conflito, timeout, falha de releitura, recibo pendente e recuperação sem reenvio cego.

O [roteiro de operação](../../harness/governanca_assistida/OPERACAO.md) define a adaptação assistida às ferramentas GitHub. A biblioteca usa o contrato Gateway; a suíte local usa MemoryGateway. Não foi criado cliente autônomo de rede, sistema independente de identidade ou publicação em segundo plano. No adaptador manual, o operador consulta a fonte humana e aplica a mesma sequência aos comandos do conector; a integração real de um registro aceito ainda precisa ser demonstrada.

Os modelos não preenchidos não são aceites ou recibos reais. A [entrada do piloto](../../docs/01-discovery/governanca-assistida/INICIO.md) permite a uma conversa futura identificar o que existe e o que ainda falta. O leitor de snapshots recupera conteúdo e recibo, mas sempre marca a origem do aceite como não revalidada na sessão.

## Evidências executadas

1. **14/14 ensaios locais aprovados**, com gateway e manifestações humanas explicitamente simulados. Eles exercitam os dez grupos GOV-T-001..010: caminho positivo, ambiguidade, recusa, aceite parcial, alteração de bytes, revogação, permissão, CAS, timeouts, duplicação, retomada, caminhos inseguros, conteúdo suspeito e reparação com histórico. [Saída integral](testes-locais.txt).
2. **Recuperação em processo isolado aprovada**, recebendo somente uma exportação de commits e o commit de entrada, sem diário ou histórico de chat. Conteúdo, ID e estado não normativo conferiram. [Evidência](retomada-processo-isolado.json). Esse ensaio usa uma fixture aceita de forma simulada e não é nova conversa real.
3. **Ensaio diferencial real de escrita condicional no GitHub**, apenas sobre uma fixture técnica em `ensaios/controle-condicional.json`. Uma atualização para descendente válido, com revisão esperada antiga, retornou erro e preservou o HEAD; a mesma atualização, com a revisão esperada correta, teve sucesso confirmado. O conector retornou GraphQL UNKNOWN na tentativa antiga; o estado foi consultado antes da nova operação. [Respostas e limites](conector-cas-real.json). A fixture não constitui registro humano aceito.

Não foram executados os 49 CA do PGC. A suíte acima não os aprova por equivalência nem certifica controles normativos. Execução local nativa: Windows.

## Situação dos critérios

| Critério | Evidência obtida | O que falta para aceite operacional |
|---|---|---|
| GOV-CA-001 | Acesso ao repositório privado, branch e commits consultados; PGC permanece candidato. | Vincular o contexto à primeira rodada de registro real. |
| GOV-CA-002 | ID estável e sucessão exercitados localmente. | Registro sintético efetivamente aceito e recuperável no remoto. |
| GOV-CA-003 | Modelo e preparação do pacote, texto e hashes implementados. | Apresentar o pacote final de registro ao usuário. |
| GOV-CA-004 | Rejeição de ambiguidade, parcialidade e fonte indireta exercitadas em simulação. | Aceite humano específico, com fonte verificável e escopo exato. |
| GOV-CA-005 | Alteração de um byte bloqueada nos ensaios; recibo separado. | Confrontar o conteúdo humano aceito com o commit de registro. |
| GOV-CA-006 | Restrições locais exercitadas; ensaio diferencial do conector real sem mover a principal. | Aplicar o controle na publicação do registro aceito. |
| GOV-CA-007 | Releitura e falha de integridade exercitadas localmente; entrega de código será reobtida no remoto. | Recibo real do registro aceito, com comparação de bytes. |
| GOV-CA-008 | Estados separados no código e fixtures; nenhum manifesto ou ratificação criado. | Conferir os estados na demonstração real. |
| GOV-CA-009 | Leitor e recuperação em processo isolado aprovados. | Nova conversa real, iniciada pelo usuário, lendo somente o repositório e declarando fontes inacessíveis. |
| GOV-CA-010 | Timeouts, não repetição e idempotência exercitados localmente. | Conferir recibos da rodada real e registrar limites de acesso observados. |
| GOV-CA-011 | Marcadores sintéticos, origem indireta e classificação fora do piloto recusados nos ensaios. | Revisão humana do conteúdo exato do caso real. Não há detecção universal de segredos. |
| GOV-CA-012 | Falha pós-commit e correção com revisão anterior preservada exercitadas localmente. | Revisão humana das evidências e aceite do incremento; nenhuma eliminação de histórico é presumida. |

## Limites e próxima rodada

A implementação é assistida e o atestado HumanReview depende de consulta humana externa ao código. Um campo JSON não comprova identidade ou vontade do usuário. O diário local não é fila global nem mutex; um operador por vez é condição do piloto. Arquivos históricos de inventário descrevem seus commits originais e não devem ser apresentados como inventário desta implementação.

A próxima rodada apresenta GOV-REG-0001 e seu pacote final para aceite. Se aceito, o operador publica registro/aceite, relê por commit, registra recibo/índice e entrega o caminho de retomada. O incremento só poderá ser declarado concluído após as evidências previstas e a demonstração em nova conversa. A autorização atual não ratificou o PGC nem autorizou merge na principal.
