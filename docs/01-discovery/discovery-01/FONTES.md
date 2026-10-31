# Fontes, proveniência e alcance

## Inventário desta consolidação

| ID | Fonte | Revisão/alcance | Limite |
|---|---|---|---|
| D01-S01 | Pedido direto desta sessão de consolidação | 30/10/2026; conversa referenciada `6ae50704-83b0-83e9-93d8-9d7efddba3aa` | Autoriza documentação, branch/PR e conferência; não ratifica produto ou PGC |
| D01-S02 | Conversa “Iniciar discovery funcional” pelo leitor de chats | Cinco turnos retornados; pedido com turnLimit=10 e máximo de 20.000 caracteres por item; `hasMore=false`, `nextCursor=null`, anexos vazios | Retorno final é um recorte; ausência de cursor não demonstra que a conversa original só teve cinco turnos |
| D01-S03 | GitHub privado `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide` | PR #5 aberto/draft; branch `proposta/fundacao-integral-pm-fund-001-003`; commit `f8d7c60955a1250ae4d94a428386787f4aaa24b0` | Estado de proposta; main `ba820cbb7b92bd570e4848c4ca7eff48c44f04cd` só tem `.gitkeep` |
| D01-S04 | Tentativa de leitura da conversa pelo navegador disponível | URL da conversa redirecionou à página inicial com “Entrar” | Histórico integral e Fontes nativas não inspecionados; sem alteração de conta/permissões |

Os IDs D01-S* não substituem os SRC-* da fundação. A data é a da consolidação no fuso do usuário; não se atribui horário de aprovação ou identidade corporativa a mensagens sem essa evidência.

## Mensagens recuperadas, em ordem cronológica

| Referência | Turno / mensagem humana | Resposta do assistente | Evidência utilizável |
|---|---|---|---|
| D01-S02-A | `f8bcf234-c95c-41a8-9cde-ada62fe8c07f` | `49ca4242-807d-418f-80a2-b73bb57cfa9d` | Usuário exige permissão do engenheiro para obter informação do legado e comunicação da inconformidade; resposta acrescenta fluxo e exemplo propostos |
| D01-S02-B | `8b00bd22-cb88-4485-8586-fa3edb14a354` | `d207d0d2-84b2-473f-b73c-f0fcb66d9a87` | “Permitir” responde à pergunta anterior sobre concluir com pendências não críticas; a resposta seguinte apresenta estados propostos e pergunta sobre classificação |
| D01-S02-C | `cbff402a-8ed6-4527-8406-cd52a8f36a3b` | `1e5191f0-c5af-4a18-a94d-53a1142be6b8` | “Sim” responde à classificação automática com critérios rigorosos e recurso ao engenheiro quando incerta; taxonomia, fatores e guardrails são elaborados depois |
| D01-S02-D | `508cf064-98a0-4f08-8ad5-79ded5c9fdeb` | `bedc4cee-8a8b-4728-a0ca-71c700f7e59a` | Usuário concorda com a direção de aprofundamento e pergunta sobre nova sessão; assistente recomenda persistência e enumera temas anteriores |
| D01-S02-E | `c4213106-3030-4907-9cc9-f52d57d7277c` | `92c9ba91-3183-49d2-b177-fc796c95112a` | Pedido de consolidação completa; resposta afirma encaminhamento, mas não comprova persistência |

Referência de leitura: [conversa de origem](chatgpt-conversation://6ae50704-83b0-83e9-93d8-9d7efddba3aa). Para localizar, usar UUID de turno/mensagem, autor e contexto; não inventar numeração de todos os turnos anteriores. O preview da conversa é redundante com o fim recuperado e não acrescenta evidência de decisões.

## Documentos consultados em D01-S03

Todos os caminhos abaixo foram lidos pelo SHA imutável acima, por ferramenta GitHub. Os exemplos internos são relatos previamente sanitizados; não foram revalidados institucionalmente.

| Grupo | Caminhos | Uso nesta consolidação |
|---|---|---|
| Entrada | `AGENTS.md`, `ESTADO-ATUAL.md`, `RETOMADA.md` | Escopo, restrições, fase e cadeia de propostas |
| Continuidade | `docs/continuidade/MANIFESTO.json` | Identidade e hashes do conjunto anterior; não alterar nem reinterpretar seu recibo |
| Distribuição | `docs/chatgpt/MANIFESTO-FONTES.md` | Seleção de fontes e atualização manual/verificada; sem sync presumida |
| Discovery | `docs/01-discovery/INICIO-DISCOVERY.md` | Roteiro anterior; texto “nenhuma entrevista” corresponde ao snapshot anterior |
| Produto | `docs/fundacao/visao-produto.md`, `capacidades.md` | JOR-001 e CAP-001/002/003/005/006/008/010/012/013/015/016/019/020 |
| Método | `docs/fundacao/protocolo-sessoes.md`, `roteamento-contexto.md`, `registro-conhecimento.md`, `metodologia-fases.md` | Classes, fontes, revisão, sete etapas e fases 00–09 |
| Contexto | `docs/fundacao/PROVENIENCIA-RECUPERADA.md`, `ecossistema-atual.md`, `construcao-internalizacao.md` | Intenção corporativa, camadas plataforma→conta/sigla→repositório relatadas e construção externa sintética |
| Contratos candidatos | `docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/contratos/CT-003-publicacao-concorrencia.md`, `CT-005-seguranca-autorizacao.md`, `CT-007-organizacao-contexto.md` | Comparação de publicação, autorização e contexto; não ativação normativa |

Links estáveis: [estado consultado](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/f8d7c60955a1250ae4d94a428386787f4aaa24b0/ESTADO-ATUAL.md), [manifesto consultado](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/f8d7c60955a1250ae4d94a428386787f4aaa24b0/docs/continuidade/MANIFESTO.json), [PR #5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/pull/5).

## Como completar a proveniência

Recuperar exportação autorizada ou leitura integral dos turnos anteriores de D01-S02; inventariar cada definição com autoria, texto e contexto. Confrontar D01-REL-001..009 com as falas originais. Se o usuário apenas concordou com uma ideia antes de detalhes novos, reconhecer só o escopo efetivamente aceito. Registrar divergências e revisões sem apagar este recorte. Não publicar transcrições corporativas ou segredos para preencher a lacuna.

Nenhum conteúdo ausente é reconstruído como citação. GitHub, Fontes anexadas, campo Instruções, memória e histórico de chats são superfícies distintas; uma gravação neste repositório não atualiza automaticamente as demais.
