# Manifesto curado das Fontes do Projeto

## Atualização de continuidade — 30/10/2026

A entrada atual da proposta é [RETOMADA.md](../../RETOMADA.md), acompanhada de [MANIFESTO de continuidade](../continuidade/MANIFESTO.json) e [proveniência recuperada](../fundacao/PROVENIENCIA-RECUPERADA.md). O empacotador atualizado inclui esses arquivos e o registro CONT-REG-0001 nas Fontes de fundação. O recibo do novo pacote deve informar seu commit próprio; não atribuir os hashes do pacote antigo à nova versão. O restante deste documento preserva o procedimento e a seleção originais como histórico.

Versão do manifesto: 0.1.0, 30/10/2026. Estado: PREPARADO; Projeto ChatGPT NÃO CONFIGURADO nesta verificação. É um manifesto de distribuição de contexto, sem efeito normativo. Fontes primárias da reconciliação: SRC-001 (pedido atual) e SRC-002 (cinco turnos recuperados da conversa de origem; resposta PM truncada a 20.000 caracteres, sem acesso ao planejamento original completo).

## Autoridade, revisão e atualização

Repositório oficial: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide . A branch desta fundação é proposta; não substitui `main`. O pacote distribuído deve informar commit imutável e hashes exatos em recibo próprio. Não usar nome de branch como prova suficiente de versão.

O conteúdo de [INSTRUCOES-PERMANENTES.md](INSTRUCOES-PERMANENTES.md) é o texto exato para o campo Instruções; não carregar o PGC inteiro nesse campo. As Fontes contêm o contexto. Instruções, Fontes, GitHub, estado de persistência e vigência são verificações separadas.

## Seleção inicial

| Prioridade | Documento no repositório | Versão/estado | Uso e limite |
|---|---|---|---|
| P0 | [ESTADO-ATUAL.md](../../ESTADO-ATUAL.md) | Snapshot da fundação; verificar commit do pacote | Fase, próximos passos, limites e evidências atuais; não prova ratificação |
| P0 | [roteamento-contexto.md](../fundacao/roteamento-contexto.md) | 0.1.0 proposta | Entrada por tema e dependências |
| P0 | [visao-produto.md](../fundacao/visao-produto.md) | Fundação proposta; versão no documento | Visão integral e fronteiras; não especificação aprovada |
| P0 | [ecossistema-atual.md](../fundacao/ecossistema-atual.md) | Relatos com proveniência | Contexto do banco; não norma corporativa verificada |
| P0 | [capacidades.md](../fundacao/capacidades.md) | Catálogo inicial com maturidade | Distingue pretendido, documentado e comprovado |
| P0 | [metodologia-fases.md](../fundacao/metodologia-fases.md) | 0.1.0 proposta | Sete etapas e dez fases, gates e revisão |
| P0 | [protocolo-sessoes.md](../fundacao/protocolo-sessoes.md) | 0.1.0 proposta | Conversas, formalização e persistência |
| P0 | [registro-conhecimento.md](../fundacao/registro-conhecimento.md) | Registro inicial com fontes e estados | Decisões, hipóteses e pendências; não inferir aprovação |
| P1 | [construcao-internalizacao.md](../fundacao/construcao-internalizacao.md) | Estratégia proposta | Plataforma real externa e integração interna futura |
| P1 | [INICIO-DISCOVERY.md](../01-discovery/INICIO-DISCOVERY.md) | 0.1.0 proposta | Primeira conversa de negócio e UX, critérios de formalização |
| P1 | [README.md](../../README.md) e [AGENTS.md](../../AGENTS.md) | Snapshot da fundação | Navegação e orientações de agentes |
| P1 | [índice PGC v1.1.3](../00-governanca/PGC-001_v1.1.3_candidata_ratificacao/README.md) e [PGC-001](../00-governanca/PGC-001_v1.1.3_candidata_ratificacao/PGC-001.md) | 1.1.3 candidata NÃO RATIFICADA | Consultar quando assunto exigir governança; sem ativação por upload |
| P2 | CT-001..CT-008 em `docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/contratos/` | 1.0.3 candidatos | Recuperação por contrato relacionado, sem repetição nas Instruções |
| P2 | Auditorias da fundação e [operação assistida](../../harness/governanca_assistida/OPERACAO.md) | Versão/commit nas evidências | Verificar alegações técnicas; testes do piloto não equivalem aos 49 CA |

Caso o Projeto imponha limite de quantidade/tamanho, conferir a limitação real na UI e consolidar o conjunto P0 em uma fonte com índice e proveniência; manter arquivos originais no GitHub. Não afirmar limite fixo sem confirmação. Orçamento inicial sugerido: P0 disponível para recuperação, leitura inicial de estado/roteamento mais documentos do tema; é uma escolha operacional, não limite técnico do produto.

## Procedimento de atualização

1. Escolher o commit/escopo autorizado e conferir diffs; não promover versão candidata a vigente.
2. Gerar pacote com os documentos selecionados, manifesto de caminhos, tamanho e SHA-256, commit e horário real de geração. Se algum caminho faltar, interromper o empacotamento e registrar erro.
3. Na configuração acessível, substituir/adicionar as cópias afetadas; preservar origem e verificar que versões antigas não continuam oferecendo instruções conflitantes.
4. Ler as fontes na nova conversa e confirmar versão/estado, visão, método e próxima ação. Registrar o resultado real e o acesso utilizado.
5. Atualizar recibo de distribuição: Projeto alvo, arquivos carregados, versões/hashes, momento e prova de releitura. Sem isso, manter NÃO CONFIGURADO ou CONFIGURAÇÃO NÃO VERIFICADA.

A documentação oficial [Projects and chats](https://learn.chatgpt.com/docs/projects), consultada em 30/10/2026, descreve Instruções compartilhadas e Fontes do Projeto; acesso a arquivo e sincronização de conversa são coisas distintas. A existência de arquivo neste repositório não comprova upload, aplicação das Instruções nem atualização automática.
