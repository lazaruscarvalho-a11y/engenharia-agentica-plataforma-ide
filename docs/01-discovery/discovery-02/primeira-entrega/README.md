# Primeira entrega da Plataforma/IDE de Engenharia Agêntica

**Comece aqui para continuar o Discovery da primeira entrega.** O perímetro funcional da revisão 1 está fechado em nove frentes. Há decisões sobre como a Plataforma deve se comportar e pontos ainda a especificar. O trabalho seguinte é aprofundar uma frente por vez, registrar o saldo de cada rodada e revisar o conjunto quando as nove tiverem sido percorridas. A regra de comunicar lacunas assim que percebidas continua valendo durante todo o percurso.

| Para fazer o quê | Ler |
|---|---|
| Entender a entrega, os estados e suas fronteiras | [Escopo da primeira entrega](ESCOPO.md#mapa) e [princípios e limites](ESCOPO.md#limites) |
| Começar uma sessão sobre uma frente | [Roteiro por frente e revisão geral](roteiro/REFINAMENTO-E-REVISAO.md) e [agenda de pendências](ESCOPO.md#pendencias) |
| Consultar o que já foi aceito sobre suficiência e avisos | [Dois casos de onboarding de A e o momento de comunicar lacunas](evidencias/ESCLARECIMENTOS-ONBOARDING.md) |
| Recuperar o Workspace sem depender da conversa de origem | [Referência funcional R06](evidencias/WORKSPACE-R06.md) |
| Situar o exemplo da empresa envolvendo Devin | [Síntese funcional de acesso a ferramentas](evidencias/DEVIN-FERRAMENTAS.md) |
| Conferir origem e integridade do pacote inicial | [Manifesto da publicação](MANIFESTO.json) e [fontes do escopo](ESCOPO.md#fontes) |

## Situação na abertura deste ciclo

| Frente | Ponto de partida da próxima rodada |
|---|---|
| PE-01 · Distribuição e acesso | Fluxo de atualizar a raiz ao iniciar e carregar a atividade ao abrir aceito. A visibilidade padrão dos repositórios de Workspaces continua em decisão. [Distribuição, revisão 3](notas/DISTRIBUICAO-E-ACESSO.md) |
| PE-02 · Ferramentas de IA | Devin Web, CLI e Desktop e Claude Code. Especificar o suporte, a atualização e a verificação por modalidade. [Ferramentas](notas/FERRAMENTAS.md) |
| PE-03 · Motor | Saídas Micro e Meso definidas. Produzir um exemplo de cada e estabelecer o conteúdo mínimo verificável. [Especificação do Motor](../MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) |
| PE-04 · Evidências e pendências | Momento do aviso e dois casos concretos acordados. Refinar os critérios gerais de suficiência, criticidade e revalidação. [Esclarecimentos](evidencias/ESCLARECIMENTOS-ONBOARDING.md) |
| PE-05 · Workspace | R06 consolidou estado, estrutura, papéis e ciclo de vida. Retomar os detalhes operacionais residuais. [Síntese R06](evidencias/WORKSPACE-R06.md) |
| PE-06 · Atuação por etapa | O agente adapta interpretação, investigação e resposta. Definir transições, recuperação e entregáveis de cada atividade. [Atuação por etapa](notas/ATUACAO-POR-ETAPA.md) |
| PE-07 · Extensões | Inclusão pós-onboarding por escopo e recuperação direta ou indireta definidas. Refinar padrões, conflitos e permissões. [Extensões e caso ODM](notas/EXTENSOES-POR-ESCOPO.md) |
| PE-08 · Arquitetura/Solução | A relação técnica mapeada e a fronteira funcional decidida pelo Analista estão diferenciadas. Deliberar qual saída arquitetural a primeira entrega deverá oferecer. [Contexto do Motor e da Arquitetura](../RETOMADA-MOTOR-E-ARQUITETURA.md) |
| PE-09 · Negócios | A necessidade faz parte do escopo a refinar. Organização transversal, autoridade e forma de representação continuam abertas. [Conhecimento de Negócios](notas/NEGOCIOS.md) |

**Primeira rodada sugerida:** PE-03 com P03. Usar os dois cenários já aceitos em PE-04 como premissas. Dado um repositório conhecido apenas por suas fontes, o que o exemplo de base Micro precisa mostrar para o engenheiro conseguir explicar uma integração, conferir sua evidência e reconhecer o limite de sua conclusão? Usar a saída Meso para testar como se declaram os demais repositórios e as lacunas da Sigla.

## Mensagem para iniciar um novo chat

> Vamos aprofundar uma frente da primeira entrega da Plataforma/IDE de Engenharia Agêntica. Use o GitHub conectado e o repositório `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`. Comece pela branch `proposta/d02-primeira-entrega-refinamentos`. Confirme o HEAD, leia por esse SHA `docs/01-discovery/discovery-02/primeira-entrega/README.md` e siga os links relativos na mesma revisão. Se esta branch já tiver sido integrada, localize a revisão sucessora e comprove a continuidade antes de usá-la.
>
> Se eu indicar uma frente PE, trabalhe nessa frente. Se eu não indicar, use o ponto de retomada registrado. Antes da primeira pergunta, recupere as definições vigentes dessa frente, as pendências relacionadas e o que já foi respondido. Aprofunde uma questão concreta por vez, com exemplos e critérios observáveis. Consulte outras frentes apenas quando houver uma dependência que possa mudar a resposta. Ao fim, apresente decisões, propostas, pendências, impactos e próxima pergunta. Diferencie o que ficou em conversa do que foi publicado em Git. Depois das nove frentes, faça a revisão geral prevista no roteiro.

## Atualização da continuidade

Esta proposta deriva da revisão `766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455` da branch `proposta/d02-motor-workspaces-atividade` (PR #8). A [entrada D02](../RETOMADA.md) e o [estado da consolidação anterior](../../../../ESTADO-ATUAL.md) situam a fundação. Para esta primeira entrega, as definições adicionais estão no [escopo](ESCOPO.md) e nas notas deste diretório. O manifesto vincula os bytes da edição inicial às suas origens. Os commits posteriores registram o que mudar.

No encerramento de cada rodada, atualizar a [agenda e o histórico do escopo](ESCOPO.md#revisoes) e indicar aqui a frente, a revisão produzida, o que ainda condiciona seu fechamento e o ponto exato de retomada. Uma alteração autorizada deve ser reaberta pelo commit publicado e comparada com o conteúdo revisado. O [roteiro](roteiro/REFINAMENTO-E-REVISAO.md) define o confronto transversal e o entregável final.
