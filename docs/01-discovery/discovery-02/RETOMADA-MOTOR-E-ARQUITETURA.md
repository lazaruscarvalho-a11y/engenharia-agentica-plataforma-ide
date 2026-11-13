# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](primeira-entrega/consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](primeira-entrega/consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Retomada do Discovery do Motor e da Arquitetura

> **Primeira entrega — sequência deste Discovery.** A [entrada da primeira entrega](primeira-entrega/README.md) reúne o escopo fechado para refinamento, as decisões posteriores e o roteiro para os próximos chats. O registro abaixo conserva o contexto e as perguntas da revisão 1 do Motor.

**Registro:** D02-CONT-MOTOR-001 · **Revisão:** 1 · **Data:** 07/11/2026 · **Estado:** continuidade de produto em Discovery na proposta do PR #8.

Leia esta entrada depois da [retomada D02](RETOMADA.md) e junto à [especificação de motor e workspaces D02-ESP-001](MOTOR-E-WORKSPACES-DE-ATIVIDADE.md). A [consolidação integral da sessão](referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf) reúne definições, exemplos, questões abertas e referências. O registro abaixo acrescenta as direções posteriores à D02-ESP-001 e organiza o próximo refinamento. A especificação histórica e os manifestos dos snapshots anteriores permanecem como evidência de suas revisões.

## Fonte e estado

| Referência | Natureza e uso |
|---|---|
| Conversa de refinamento de 07/11/2026 | Fonte direta das direções atuais. A consolidação em PDF distingue manifestações, interpretações e pendências. |
| [D02-ESP-001](MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) | Primeira incorporação revisável da relação motor e workspaces, publicada em `23711b042faca15bd1be53e8a89fb35010006148`. |
| [D02](REGISTRO.md) e [axiomas](../../fundacao/axiomas-arquiteturais.md) | Base anterior consultada em `8bbd93151640865995fa8a8dfe3d2d5db15da6ec`. As retificações D02 governam as formulações históricas pertinentes. |
| Arquivo de Workspaces do panorama BASE-01 | Fonte privada utilizada na revisão 1, em particular P-008 e P-009/E-001. A [síntese R06 disponível no repositório](primeira-entrega/evidencias/WORKSPACE-R06.md) preserva as decisões posteriores pertinentes ao escopo da primeira entrega. |

## Direções de produto para preservar

1. **Primeira entrega local.** O engenheiro indica os repositórios GitHub. O motor obtém o material autorizado, ingere, investiga, estrutura e consolida uma base por repositório e uma por Sigla. Forma do motor, stack, entrada concreta e contrato de saída seguem em aberto. A análise deve respeitar a vedação de refatoração durante onboarding, as autorizações por operação e o Git como referência canônica do conhecimento.
2. **Micro e Meso.** A base Micro representa e roteia o conhecimento do repositório, incluindo finalidade, lógica, regras, bibliotecas, ferramentas, versões, execução e testes. A base Meso indexa os repositórios, registra relações conhecidas e o contexto compartilhado, como informações sobre a conta AWS da Sigla. A consulta parte das bases e alcança a fonte quando a evidência ou a atividade exigir. A cobertura precisa explicitar revisões analisadas, lacunas e fontes inacessíveis. Pertencimento à Sigla e dependência técnica são relações distintas.
3. **Raiz da Plataforma.** Organiza o acesso e o contexto comum. Diretórios de agentes, skills, MCP, documentação e instruções essenciais são exemplos prováveis. Sua organização física, precedência e relação entre pasta local e Macro Git permanecem abertas.
4. **Base de Conhecimento de Arquitetura.** Nome provisório. Descreve uma solução de ponta a ponta por meio dos repositórios participantes e de documentação própria sobre o comportamento conjunto. Pode atravessar Siglas e representar ramos, retornos, ciclos e fluxos assíncronos. Um repositório pode integrar várias soluções. A estrutura transversal é uma interpretação funcional. Sua materialização e sua inclusão na primeira entrega seguem abertas.
5. **Workspace de atividade.** É a área em que se estudam e estabelecem requisitos e critérios de aceite e teste e se selecionam os repositórios, Siglas e arquiteturas pertinentes. Pode consultar Micro, Meso, Arquitetura e Raiz conforme a atividade e a autorização. O papel funcional inclui os artefatos da demanda. A forma de persistir conteúdo ou estado próprio segue em refinamento.
6. **Autoridade.** O sistema mapeia os repositórios e suas relações técnicas. O Analista decide a delimitação funcional da solução. O engenheiro decide se um repositório relacionado sugerido pelo agente entra no workspace e concede as autorizações operacionais que lhe competem. Um mapa candidato fundamentado e perguntas sobre ambiguidades materiais são propostas para reduzir o esforço de revisão. Confirmação funcional e comprovação técnica têm estados distintos.
7. **Agent-First em todo o conjunto.** Todas as estruturas, pastas, arquivos, configurações, documentos e unidades de conhecimento devem ser legíveis, navegáveis, compreensíveis, trabalháveis, modificáveis e explicáveis por agentes. Aplicar AI-Intent, Agent-Based, Agent-Oriented, SDD, roteamento, contexto mínimo necessário e contexto-ótimo. Agentes orquestram e mantêm os artefatos dentro das permissões e responsabilidades. A meta é maximizar profundidade, precisão, rapidez e abrangência pertinentes à tarefa com o mínimo de recursos necessário para preservar qualidade, evidência e segurança.

## Implicações operacionais a verificar

- Registrar dependências por relação observável, origem e revisão. Distinguir o que consta em código, o que a documentação declara e o que foi verificado em um ambiente. Uma relação identificada pode ser registrada com escopo parcial sem ampliar a importação.
- Permitir recuperar conhecimento por repositório, revisão, evidência e relação técnica. Propagar referências às fontes pertinentes em vez de repetir indistintamente todas as bases. Preservar contratos, decisões, exceções, contraevidências e pendências que alterem o resultado.
- Investigar fluxos pelos comportamentos acionados em cada contexto. Rotas, eventos e agendamentos são pontos de partida candidatos. Um componente compartilhado pode ter papéis diferentes. A finalidade e os desfechos delimitados pelo Analista orientam a seleção das relações que pertencem a cada solução.
- Preservar Git, proveniência, permissões distintas e conclusão com ressalvas apenas para pendências não críticas catalogadas. Revalidar conhecimento afetado por mudanças conforme HUM-08. O mecanismo de propagação a arquiteturas e o alcance da atualização incremental na primeira entrega ainda exigem definição.
- Avaliar profundidade e custo com tarefas observáveis. Reutilizar evidência válida e aprofundar quando lacunas, contradições ou riscos puderem mudar a conclusão. Métricas, limiares, formatos, ferramentas e algoritmos continuam candidatos.

## Próximo passo recomendado

Retomar D02-PEN-001/002 com um cenário sintético. O engenheiro indica A e B, de Siglas diferentes. A evidencia uma dependência de C, que ficou fora da importação. Acrescentar, se for útil para avaliar a arquitetura, um fluxo com retorno e um componente compartilhado por duas soluções. A fronteira funcional pode estar pendente de confirmação do Analista.

**Primeira pergunta:** ao abrir pela primeira vez a base Micro de um repositório desconhecido, quais perguntas precisam ser respondidas, com quais evidências, para você confiar nela como ponto de partida?

1. Produzir exemplos de Micro e Meso e especificar o conteúdo mínimo de cada saída.
2. Definir como distinguir compreensão suficiente, ressalva não crítica e lacuna que torna insegura a conclusão. Determinar como mostrar a cobertura e as evidências ao engenheiro.
3. Verificar se uma atividade consegue recuperar o contrato, a revisão e os limites pertinentes sem ler toda a Sigla.
4. Deliberar se a primeira entrega apenas preserva evidências arquiteturais, se propõe mapas candidatos para o Analista ou se já entrega uma base arquitetural verificável. Refinar identidade, fronteira, versões, manutenção e acesso da solução conforme o recorte escolhido.

## Integridade e leitura na próxima sessão

- PDF original da sessão, 112596 bytes. SHA-256 `9b06d50e2f98355c2d0c5eefa8e4d1d35266cc52b15a499155c2fa75063099dd`.
- Para recuperar a atualização, consultar o [PR #8](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/pull/8), identificar a revisão proposta e ler os documentos pelo commit correspondente. Esta entrada e o PDF complementam D02. Fontes do Projeto e Git são cópias com rotas próprias de atualização.
