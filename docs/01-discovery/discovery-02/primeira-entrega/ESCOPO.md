# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Rota vigente R03 — 13/11/2026

Leia a [consolidação P03/P04 R03](consolidacao-r03/ESCOPO-INTEGRADO.md) na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o manifesto R03 e o recibo posterior por commit imutável. P03 conserva seus aceites e adiamentos; P04 está funcionalmente encerrado no alcance qualificado pela fonte recuperada, com proveniência indireta dos aceites iniciais. P01–P09 têm catálogo granular e prompt de continuidade. A R03 distingue decisão, proposta, relato corporativo e comprovação; sem código de produto, merge, ratificação ou mudança de permissões.

O conteúdo abaixo é o snapshot anterior, preservado literalmente. Pontos de retomada, estados de entrevista e hashes anteriores valem para a revisão ali identificada; ler a sobreposição R03 para o saldo atual. Os manifestos D02-doc-2/R01/R02 permanecem históricos, sem certificar os novos bytes desta navegação.

---

# Primeira entrega da Plataforma/IDE de Engenharia Agêntica

**Escopo funcional de referência · revisão 2 · 8 de novembro de 2026**

A primeira entrega deve permitir que um engenheiro obtenha a Plataforma em sua máquina, compreenda repositórios autorizados por meio do Motor de Onboarding e use esse conhecimento para refinar uma atividade com agentes no Workspace. A equipe deve conseguir rastrear decisões, encontrar os recursos específicos de cada contexto e receber cada dúvida, lacuna ou incoerência assim que o agente a perceber. Quando uma atividade depender desse ponto, o agente deve voltar a mostrá-lo com a consequência para a decisão em curso.

**O que está fechado.** Esta revisão fixa o perímetro da primeira entrega conforme as definições e direções trazidas até o encerramento desta conversa. Os próximos refinamentos partem deste texto. Podem detalhar o comportamento ou acrescentar conteúdo em nova revisão, com a origem e o impacto identificados. O projeto segue na etapa de Discovery e refinamento (M-01, fase 01). A especificação executável, os aceites de implementação e a comprovação operacional têm marcos próprios.

A revisão 2 incorpora as decisões das rodadas de [P03](refinamentos/P03-CONHECIMENTO.md) e abre a entrevista de [P04](refinamentos/P04-ATUALIDADE.md). A divisão entre o Motor produtor do conhecimento e o componente que o consulta rege as formulações sobre objetivo e recuperação. Os demais grupos continuam com seus próprios estados.

**Navegação** · [Mapa do escopo](#mapa) · [Definições funcionais](#definicoes) · [Limites e princípios](#limites) · [Cenários de verificação](#cenarios) · [Pendências e próxima rodada](#pendencias) · [Controle de revisões](#revisoes) · [Fontes](#fontes)

<a id="mapa"></a>

## 1. Mapa do escopo

Os identificadores PE organizam este consolidado e permanecem estáveis nas próximas revisões. Os estados distinguem o comportamento já definido da necessidade cujo formato ainda depende de Discovery.

| Frente | Resultado esperado | Grau de definição |
|---|---|---|
| PE-01 · Distribuição e acesso | Atualizar a raiz da Plataforma e obter os recursos pertinentes ao abrir uma atividade. | Fluxo aceito. Visibilidade padrão e mecanismos ainda abertos. |
| PE-02 · Ferramentas de IA | Trabalhar com Devin Web, CLI e Desktop e com Claude Code, preservando a portabilidade do conjunto. | Recorte e objetivo de atualização definidos. Capacidades por modalidade a especificar. |
| PE-03 · Motor de Onboarding | Produzir conhecimento por repositório (Micro) e por Sigla (Meso), indicando revisão e cobertura. | DoD do produtor e fronteira funcional aceitos. Estrutura documental e avaliação formal postergadas. |
| PE-04 · Evidências e pendências | Catalogar e avisar assim que uma lacuna for percebida. Voltar a sinalizá-la quando afetar uma pergunta ou atividade. | Condutas, criticidade e alcance da evidência definidos no P03. Revalidação e adoção de revisões avançam em P04. |
| PE-05 · Workspace | Guardar e recuperar o refinamento de uma atividade, inclusive quando atravessa Siglas. | Organização, participantes, vínculos e ciclo de vida consolidados na R06. |
| PE-06 · Agente por etapa | Adaptar interpretação, investigação, atuação e resposta do negócio ao planejamento técnico e de testes. | Requisito da primeira entrega. Papéis, transições e recuperação a especificar. |
| PE-07 · Extensões por escopo | Incorporar e usar capacidades específicas depois do onboarding e da internalização. | Direção definida. Padrão de incorporação e resolução de conflitos em aberto. |
| PE-08 · Arquitetura/Solução | Investigar relações técnicas entre componentes e compreender o comportamento conjunto relevante à atividade. | Necessidade e autoridade definidas. A entrega de uma base arquitetural completa permanece em decisão. |
| PE-09 · Negócios | Incorporar ao refinamento o significado de negócio que excede a evidência das aplicações. | Necessidade incluída. Conteúdo mínimo, organização e validação em aberto. |

**Como as partes se relacionam.** A raiz distribui os recursos comuns. O Motor fornece as bases Micro e Meso. O Workspace reúne os itens da atividade e usa essas bases conforme a demanda. A arquitetura descreve como os componentes realizam uma solução. O conhecimento de Negócios deve ajudar a entender a finalidade e o contexto organizacional do que se está refinando. As extensões acompanham seus respectivos escopos. O agente usa essas fontes conforme a etapa e os acessos efetivos. Essa é uma relação funcional entre as partes. A estrutura física de diretórios ou repositórios só está definida nos pontos expressamente indicados a seguir.

<a id="definicoes"></a>

## 2. Definições funcionais

### PE-01 · Distribuição da raiz e acesso aos contextos

**Distribuição aceita.** A Plataforma é obtida de um repositório Git no GitHub. O usuário clona a raiz comum na primeira utilização e a atualiza ao iniciar. Uma publicação dos mantenedores na `main` e a obtenção dessa revisão em cada máquina são eventos distintos. O acesso a um repositório privado de outra atividade não pode ser pré-requisito para receber uma atualização da raiz. Scripts, programa, mecanismo de inicialização e tratamento de atualização malsucedida permanecem em refinamento.

**Carga da atividade.** Ao abrir um Workspace, a Plataforma busca as dependências pertinentes, com a credencial do usuário. Informa quais repositórios foram carregados, em qual revisão e onde o acesso faltou. A revisão pertinente de um submódulo é a referenciada pelo pai. Uma tentativa recursiva pode falhar depois de carregar parte da árvore. A Plataforma deve tornar visível a cobertura efetiva e permitir que o trabalho independente prossiga. O fluxo aceito especifica o resultado para o usuário. Os comandos de Git discutidos exemplificam maneiras de obtê-lo.

**Raiz e dados locais.** A raiz distribui configurações, documentação, instruções e os componentes comuns. A área local pode apresentar, sob uma mesma raiz, Workspaces, Siglas e aplicações mantidos em repositórios distintos. A relação física entre a raiz de instalação e a raiz Git Macro segue aberta. A visibilidade de cada fonte também se aplica aos documentos e índices gravados nela.

**Catálogo da raiz.** A primeira entrega inclui o índice de responsabilidades, escopo e domínio das Siglas, legível independentemente da Sigla do leitor. Uma atribuição pode orientar consultas imediatamente como declarada, conservando origem e revisão. O Meso encaminha ao Micro pela responsabilidade do repositório. [Registro do P03](refinamentos/P03-CONHECIMENTO.md)

**Modelo corporativo relatado pelo usuário.** O acesso é concedido por Sigla e por serviço. A concessão GitHub de uma Sigla abrange todos os seus repositórios. A concessão AWS da mesma Sigla é independente. Segundo o relato, um repositório `internal` pode ser lido por toda a empresa. A visibilidade informa quem pode ler. Escrita, execução, publicação e demais operações exigem a autorização correspondente.

| Situação | Efeito que o desenho deve preservar |
|---|---|
| Workspace guardado em repositório `private` da Sigla | Quem tem acesso GitHub à Sigla pode ler seus Workspaces e o histórico arquivado. A branch individual isola o contexto ativo da atividade. |
| Workspace guardado em repositório `internal` | Seu conteúdo versionado, inclusive requisitos e transcrições que tenham sido legitimamente armazenados, fica legível ao público corporativo desse repositório. |
| Pai legível com submódulo privado | O leitor pode ver o caminho, a URL e o commit registrados no pai. Ler o conteúdo do destino depende da credencial naquele repositório. Uma cópia de informação privada colocada no pai passa a estar exposta aos leitores do pai. |
| Pai privado inacessível com um descendente `internal` | A travessia termina no pai inacessível. O descendente pode ser consultado diretamente por outra origem autorizada. A revisão usada pelo pai depende de evidência acessível. |

As mesmas considerações alcançam catálogos de Siglas e mapas entre várias Siglas. O público de leitura da raiz, dos mapas e dos repositórios de Workspaces precisa ser escolhido de acordo com o material a publicar. O usuário aceitou os efeitos descritos e a carga seletiva. A classificação padrão continua pendente. Fontes [F4], [F8] e [S].

### PE-02 · Ferramentas suportadas e atualização

A primeira entrega dá suporte específico a **Devin Web, Devin CLI, Devin Desktop e Claude Code**. São dois grupos de ferramentas. O GitHub Copilot fica fora deste recorte. A justificativa apresentada é o uso frequente e consistente de Devin e Claude Code na empresa.

O núcleo, a governança, o conhecimento e os procedimentos devem permanecer agnósticos e independentes de fornecedor. Ao mesmo tempo, a Plataforma deve explorar ao máximo os recursos pertinentes de cada ferramenta. Configurações específicas como `.devin/` e `.claude/` na raiz dos repositórios são exemplos válidos. A forma de gerar, manter e autorizar essas configurações, assim como a correspondência entre recursos de modalidades distintas, requer especificação.

A cada inicialização, a Plataforma deve providenciar a obtenção ou atualização necessária para trabalhar com a última versão das ferramentas. Segundo o usuário, a máquina corporativa já possui estruturas para tratar desse ponto. A origem dos downloads e o procedimento corporativo ficaram para outro momento. A atualização da raiz distribui os componentes que cuidam das ferramentas. É preciso definir como verificar a versão efetivamente utilizada em cada modalidade, inclusive no acesso Web, e como apresentar a condição de falha. `.skills/`, RTK, Caveman e Context-Mode apareceram como exemplos de conteúdo ou ferramentas auxiliares. Fontes [F5], [F8] e [S].

### PE-03 · Motor de Onboarding e bases Micro e Meso

O Engenheiro pode indicar repositórios em diretório local, arrastá-los para a pasta da Plataforma, informar links GitHub ou pedir a busca dos repositórios de uma Sigla. A cópia local retrata a branch e as alterações autorizadas examinadas, distinguidas do commit-base. No GitHub, usa-se a main por padrão ou a branch explicitamente indicada no link. O Motor opera na máquina de trabalho, obtém o material autorizado e produz conhecimento reutilizável sobre os repositórios e suas Siglas. A análise abrange finalidade, regras de negócio, responsabilidades, fluxos, código, integrações, contratos, infraestrutura, testes e procedimentos de execução documentados. Durante o onboarding, a aplicação é preservada integralmente, sem refatorações, renomeações ou reorganizações. [F1] [F2]

O conhecimento canônico acompanha o Git. **Micro** corresponde ao repositório individual e orienta o agente até as fontes que sustentam cada conclusão. **Meso** é o repositório da Sigla ou conta, que reúne os Micro como submódulos. Sua base identifica quais repositórios e revisões foram analisados, o conhecimento que compartilham e as lacunas do conjunto. A topologia mais ampla prevê uma raiz Git **Macro** com os Meso como submódulos. O Motor priorizado entrega as bases Micro e Meso. O Workspace de uma atividade pode consumir conhecimento de várias Siglas conforme a demanda. Cada referência continua sujeita às permissões e à revisão a que se refere. [F1] [F2] [F3]

No cenário de referência, A e B são repositórios indicados para onboarding, pertencentes a Siglas diferentes. Uma fonte de A evidencia uma dependência de C, que ficou fora da seleção. O Motor registra o que observou em A sobre a relação com C e explicita o que exigiria examinar o outro lado. A relação técnica entre A e C pode ser relevante mesmo atravessando Siglas. Para a atividade, o agente pode sugerir a inclusão de C já mapeado e explicar sua utilidade. Cabe ao Engenheiro decidir a inclusão. [F1] [F2] [S]

A finalidade fixa do onboarding é produzir a base do repositório no estado examinado. O Motor verifica a cobertura e a integridade daquilo que entrega. Quando houver uma pergunta posterior, o componente de interação interpreta o pedido e consulta as bases. O registro do P03 descreve o DoD aceito, as quatro situações de conclusão e a incorporação de conhecimento novo. [Fechamento do P03](refinamentos/P03-CONHECIMENTO.md)

### PE-04 · Evidências, lacunas e validade do conhecimento

O agente vincula uma afirmação à revisão do repositório e à evidência pertinente, como arquivo, trecho, teste ou contrato. Expõe material inacessível, contradições e limites. Uma regra presente na branch da tarefa pode divergir daquela efetivamente implantada em homologação ou produção. O agente precisa identificar a referência usada em cada afirmação e obter evidência da implantação antes de atribuir o comportamento a um ambiente. [F1] [F2]

O usuário aceitou que **A conclua o onboarding com ressalva nos dois casos discutidos**, desde que todas as dúvidas, lacunas, pendências e insuficiências percebidas estejam bem definidas, localizadas, detalhadas e referenciadas no próprio repositório. No primeiro caso, A envia `codigoSegmento` para B e C. As fontes analisadas sustentam o tratamento de B e a emissão por A, mas deixam em aberto se C aceita a ausência do campo. No segundo, foram encontradas em A duas regras para calcular o segmento, uma a partir do cadastro e outra da proposta, e falta evidência sobre quando cada uma se aplica. O alcance do aceite é a conclusão do onboarding de A nessas condições. A segurança de retirar o campo ou modificar a seleção da regra exige evidência própria. [F1] [S]

O agente deve **catalogar e apresentar ao usuário, o mais brevemente possível, cada dúvida, lacuna, pendência ou incoerência assim que percebida**. O aviso deve explicar o ponto concreto e referenciar a evidência disponível, mesmo que o impacto ainda esteja em investigação. Ao detectar que uma história depende da lacuna, o agente já a sinaliza no contexto do Workspace. Ao refinar a história ou receber uma pergunta posterior, dentro ou fora do Workspace, volta a apresentá-la se houver dependência direta ou indireta. Por exemplo, um pedido para alterar uma tarifa pode depender da regra de segmento ainda incerta. Informar e continuar investigando legitimamente são ações compatíveis. [S]

Pendências não críticas identificadas e controladas admitem conclusão com ressalvas. Uma falha crítica para o objetivo impede a conclusão que dela depende. A classificação exige critérios objetivos e verificáveis. Quando a criticidade continua incerta após a investigação, a questão segue para o Engenheiro. A primeira entrega deve oferecer, após esgotar a investigação autorizada de uma dúvida intransponível, o fluxo de solicitação excepcional de execução local da aplicação, detalhando tentativas, finalidade, ambiente, dados, pré-requisitos, comandos e efeitos. O engenheiro pode esclarecer diretamente. Executar exige permissão específica. [F1] [S]

Uma alteração agêntica exige atualizar ou revalidar o conhecimento afetado no mesmo ciclo de commit ou PR, antes de fechá-lo. Em trabalho multirrepositório, registram-se os commits e ponteiros pertinentes. Diante de alteração externa, é preciso detectar a divergência, impedir que a informação afetada seja usada como atual, reconciliá-la e verificar a revisão corrigida. Na ausência de monitor, a detecção ocorre na próxima leitura ou ciclo. Permanecem para refinamento os mecanismos de atualização, a representação da evidência e a apresentação ao usuário de cobertura, incerteza e impacto. O momento do aviso já está definido. [F1] [F2] [S]

O requisito de produto exige verificação determinística para o conteúdo exato antes de todo push e atualização ou revalidação do conhecimento afetado. Para os repositórios sujeitos à pipeline relatada pelo usuário, a release branch mais recente identifica o código de homologação. A configuração externa efetiva e a ocorrência de um evento têm fontes próprias. O [registro do P03](refinamentos/P03-CONHECIMENTO.md) delimita também correção autônoma, autorização de incorporação entre Siglas e reconciliação de declarações.

### PE-05 · Workspace de Atividades

O **Workspace** é onde negócio, Tech Lead e analistas técnicos refinam juntos uma atividade, entendida como o conjunto de histórias e tasks em que vão trabalhar. Ali ficam os dados do refinamento, das fontes recebidas às hipóteses, decisões, dúvidas e requisitos consolidados. Uma transcrição do Teams que a equipe peça para guardar é um possível ponto de partida. O estado da atividade, a revisão do código de cada aplicação e o status de uma história no sistema corporativo representam informações diferentes.

Na máquina do engenheiro, os Workspaces aparecem em `workspaces/`, na raiz da área de trabalho. No Git, há um repositório de Workspaces por Sigla. O agente pergunta ao Engenheiro qual é a Sigla do time ou analista executor. Nesse repositório fica uma branch por Workspace, contendo na raiz apenas a pasta daquela atividade. Essa regra vale inclusive quando participam aplicações de outras Siglas. Ao abrir a atividade, o fluxo aceito prevê carregar as revisões pertinentes com a credencial do usuário, mostrar a cobertura obtida e apontar os acessos ausentes.

Para responder a um pedido, o agente começa pelo conhecimento já associado à atividade. Quando ele é insuficiente, segue as pistas do pedido até as bases e índices das Siglas e, em seguida, aos repositórios pertinentes. Se persistir uma lacuna, faz uma pergunta objetiva à pessoa que solicitou o trabalho e retoma a busca com o esclarecimento. A consulta a uma fonte e a decisão de associá-la ao Workspace são operações distintas.

| Objeto | Como entra no contexto da atividade |
|---|---|
| Repositório | O agente sugere, o Engenheiro decide e, se autorizado, o agente o inclui como submódulo. A permissão para alterar o código é verificada separadamente. |
| Sigla | O agente sugere e o Analista permite a vinculação. O efeito é disponibilizar seus índices para consulta. A execução material desse vínculo segue em aberto. |
| Outro Workspace | Pode ser consultado para recuperar histórico ou entender uma decisão, respeitando o acesso ao material. Os itens continuam pertencendo ao Workspace de origem. |

Uma feature pode participar de vários Workspaces. Cada história, task, subtask ou bug pertence a um único Workspace. Quando a **atividade termina**, o time escolhe entre excluir a branch ou arquivar a pasta em `workspaces/` na `main` do repositório de Workspaces da Sigla. O sinal operacional de término do conjunto, as regras específicas de acesso ao histórico e a estrutura interna dos dados ainda precisam de detalhamento.

**Fontes** — [F4], documento 03, §§ 1–6, e [S], fluxo aceito de carga por atividade.

### PE-06 · Refinamento e atuação do agente por etapa

A primeira entrega da Plataforma deve coordenar como o agente interpreta, investiga e responde conforme **o objetivo e a etapa do item em trabalho**. No refinamento, ele ajuda a equipe a esclarecer expressões genéricas, confrontar o pedido com o conhecimento disponível, levantar dúvidas e consolidar funcionalidades e critérios de aceite. A conclusão exige aprovação formal e delimitada de um Analista, de negócios ou não, por iniciativa própria ou após uma pergunta do agente. Essa aprovação encerra o refinamento. A conclusão da atividade e as autorizações para escrita ou promoção têm marcos próprios.

Após o refinamento aprovado, criam-se as histórias, que são associadas às features e orientam o desenvolvimento. O destino corporativo definido para criar, modificar e alterar o status de **histórias** é ServiceNow/IUClick. O agente também deve saber definir e detalhar tasks, subtasks e bugs. Os contratos corporativos, as transições e as permissões de cada operação dependem de Discovery específico. A operação definida para histórias não atribui automaticamente as mesmas integrações aos demais tipos.

A mesma frase pode exigir trabalhos diferentes. Diante de “o reenvio de um pedido não pode abrir duas contas”, no refinamento de produto o agente deve esclarecer o que identifica o mesmo pedido. Na história, transforma a regra acordada em comportamento observável. No planejamento de arquitetura e software, investiga as aplicações, contratos e dependências afetadas e pode propor criar repositórios ou recursos AWS e modificar componentes existentes. No planejamento de testes, especifica como verificar tanto o reenvio quanto dois pedidos legítimos e quais evidências demonstram cada resultado. A execução concreta depende das especificações e permissões aplicáveis.

A atuação precisa ser consistente e resiliente também quando uma mensagem corrige uma regra anterior ou o trabalho é interrompido. Permanecem para refinamento os sinais de etapa, suas transições, a recuperação das decisões e o critério de suficiência de cada entrega. A direção vale para Devin Web, CLI e Desktop e para Claude Code. A divisão entre agentes e componentes permanece aberta.

**Fontes** — [F4], documento 04, §§ 7–8, [F6] e [S], atuação por etapa na primeira entrega.

### PE-07 · Extensões de conhecimento e ferramentas por escopo

Mesmo depois do onboarding e da internalização, o usuário deve poder acrescentar **skills, instruções, comportamentos, documentação e ferramentas, inclusive via MCP**, a um repositório, uma Sigla, um Workspace ou uma arquitetura. O agente conduz a inclusão de forma estruturada, respeitando a organização, as configurações e os padrões da Plataforma. Isso deve dar consistência à forma de encontrar e usar capacidades diferentes entre equipes. Conhecer uma extensão requer saber a qual escopo pertence e como, quando e por que se aplica.

A recuperação deve funcionar tanto em perguntas diretas quanto em atividades que alcancem o recurso indiretamente, dentro ou fora de um Workspace. O agente mapeia as relações, consulta as instruções pertinentes e usa a capacidade quando a atividade a exigir, dentro das permissões. A extensibilidade da própria Plataforma dentro do banco e a evolução do conhecimento de um repositório são capacidades distintas.

**Caso de referência.** Um repositório agrega resultados de integrações e os envia ao IBM ODM, que aplica regras de negócio e devolve uma resposta. Depois do onboarding, a equipe integra ao repositório um MCP e acrescenta skills e instruções para seu uso. Um Analista que refina uma alteração no serviço consumidor pode chegar a essa capacidade pela dependência da atividade, mesmo sem saber que o MCP existe. O agente deve distinguir os dados preparados pela aplicação, a decisão tomada no ODM e as evidências a que teve acesso. A operação no ODM requer autoridade própria. Esse suporte específico ao domínio é compatível com o recorte das ferramentas de IA de PE-02. Fontes [F4], [F7] e [S].

### PE-08 · Arquitetura e solução

A base de Arquitetura/Solução, de nome provisório, descreve o comportamento conjunto dos componentes que atendem uma finalidade. Pode atravessar Siglas, incluir ramos, retornos, ciclos, integrações assíncronas e componentes compartilhados. Um repositório pode participar de várias soluções com papéis diferentes. Pertencer à mesma Sigla, ter uma dependência técnica e participar da mesma solução são relações distintas.

O sistema investiga e evidencia relações técnicas. O **Analista delimita a solução do ponto de vista funcional**. O Workspace deve poder relacionar o refinamento e o planejamento a essas informações quando pertinentes e autorizadas. Uma inferência técnica, a delimitação reconhecida por um Analista e a observação de um comportamento em determinado ambiente têm fontes diferentes.

**Decisão ainda necessária.** Preservar a evidência de uma relação está contemplado no Motor. O Discovery deve decidir se a primeira entrega também propõe mapas para o Analista ou entrega uma base arquitetural verificável. Identidade, fronteira, versões, manutenção e acesso dependem desse recorte. Suportar extensões por arquitetura em PE-07 e planejar mudanças arquiteturais em PE-06 deixam em aberto a materialização dessa base. Fontes [F2], [F3] e [S].

### PE-09 · Conhecimento de Negócios

O usuário quer incorporar à primeira entrega conhecimento sobre o **produto, a jornada e a operação do organismo maior que as aplicações compõem**. A leitura do código e dos testes revela parte das regras implementadas. Mesmo uma análise correta de todas as aplicações e de suas interações pode deixar em aberto o motivo de uma regra, a abrangência de uma política e o trabalho feito fora do software.

**Exemplo de uso proposto.** Uma resposta do ODM encaminha pedidos de um canal para análise manual. A implementação evidencia o encaminhamento. Para decidir se o mesmo deve ocorrer em um canal novo, a equipe precisa descobrir se a análise decorre de uma política válida para o produto ou de uma contingência específica do canal original. A resposta muda a história, seus critérios de aceite e a responsabilidade operacional. Na ausência de uma fonte adequada, o agente deve preservar a pergunta como lacuna.

A proposta em discussão é tratar Negócios como uma dimensão transversal, consultável pelo Workspace, ligando regras e conceitos às jornadas, soluções e equipes pertinentes e permitindo percorrer o caminho inverso. **A necessidade de incorporar esse conhecimento integra o escopo a refinar.** Organização por produto, domínio, processo ou jornada, fontes, autoridade de validação, revisão, vigência, acesso e saída mínima continuam em aberto. O exemplo do novo canal e o desenho transversal são hipóteses para a próxima rodada. Fontes [F3], [F9] e [S].

<a id="limites"></a>

## 3. Princípios e fronteiras da primeira entrega

| Tema | Direção aplicável |
|---|---|
| Legibilidade para agentes | Estruturas, instruções e unidades de conhecimento precisam ser navegáveis, trabalháveis, explicáveis e modificáveis por agentes dentro do escopo autorizado. A intenção, as restrições, as relações e os critérios de aceite devem ser recuperáveis. |
| Consumo de contexto | O agente deve começar pelo menor contexto suficiente e aprofundar por assunto, evidência e dependência. Custos de leitura ou resumos não justificam perder condições, exceções, contradições ou pendências que mudam a decisão. |
| Permissões e proveniência | Inventário inicial autorizado, consulta posterior ao legado com aviso e permissão, pesquisa externa com finalidade e autorização prévias, execução, escrita, publicação, armazenamento derivado, redistribuição e exclusão têm alcances distintos. O uso provisório Agent-First preserva os originais e seu estado. Excluir um original exige aprovação explícita do objeto e da revisão. |
| Colaboração | Esclarecimentos e correções posteriores alimentam os níveis pertinentes e autorizados, depois de validação. Um push de trabalho tem finalidade distinta da aprovação de conhecimento. No trabalho multirrepositório, o fechamento lógico explicita commits e ponteiros. |
| SDD e entrega interna | Código produtivo depende de especificação validada e das aprovações aplicáveis. O núcleo externo deve ser portátil e permitir validação com simuladores e dados sintéticos. Integrações reais, acesso a dados e homologação no banco dependem do ambiente e dos profissionais autorizados. |
| Fronteira com a visão completa da IDE | O escopo cobre compreensão, refinamento e planejamento das mudanças, da infraestrutura, dos testes e das validações. As vinte capacidades e cinco jornadas da visão maior também incluem implementação supervisionada, PR, CI/CD, incidentes, hotfix e GMUD. A extensão operacional dessas últimas frentes pertence a definições específicas. A interface final, stack, SLAs e limiares quantitativos continuam em Discovery. |

Os dez axiomas de referência são **Agent-Centric, Agent-Oriented, AI-Intent, SDD, Harness Engineering, Contexto Mínimo Necessário, Roteamento de Contexto, Contexto-Ótimo, AI-Based Architecture e agnosticidade de modelo, agente e ferramenta**. O registro AX-01 a AX-10 distingue a direção humana de interpretações e tecnologias candidatas. A fundação e o piloto C1 conservam seu escopo próprio. PGC-001 v1.1.3 e CT-001 a CT-008 v1.0.3 constam como candidatos não ratificados, e os 49 critérios operacionais constam como não executados. Fontes [F1], [F3] e [F10].

<a id="cenarios"></a>

## 4. Cenários para revisar a futura especificação

Estes cenários traduzem as definições em resultados observáveis. São exemplos documentais para refinamento de critérios de aceite. Não houve execução de testes de produto.

| Caso | Situação sintética | Resultado a verificar |
|---|---|---|
| C01 · Instalação e acesso parcial | A raiz está acessível e um repositório privado de outra Sigla está inacessível. | A raiz recebe a revisão comum. Ao abrir a atividade, o usuário sabe quais dependências carregou, suas revisões e qual falhou. Consegue prosseguir no trabalho independente. |
| C02 · Ferramentas | A máquina inicia a Plataforma com uma ferramenta local desatualizada. | A Plataforma obtém a atualização pelo mecanismo corporativo a especificar, ou apresenta o impedimento assim que o percebe. A verificação precisa considerar a modalidade usada. |
| C03 · Suficiência e aviso | A base de A mostra duas regras locais e uma chamada a C. Falta evidência para escolher a regra ou prever o efeito em C. | A base aponta os trechos, testes e limites. O aviso indica se o agente pode continuar ou precisa de decisão humana. O usuário recebe a pendência prontamente. Uma história que dependa indiretamente da conclusão volta a exibi-la no momento de uso. |
| C04 · Atividade entre Siglas | O time A executa uma demanda que também envolve uma aplicação da Sigla B. | O Engenheiro informa A para a branch, decide sobre incluir o repositório de B e o Analista permite o vínculo da Sigla B para consulta aos índices. O Analista da atividade pode autorizar a incorporação de conhecimento em destino explicitamente nomeado de outra Sigla, respeitada a escrita no repositório. A evidência de acesso ao código é distinta dessas decisões. |
| C05 · Papel e resiliência | Durante o planejamento técnico, o Analista corrige uma definição de negócio. | A futura especificação deve mostrar como o agente recupera a decisão anterior e identifica a história, os critérios e os testes que precisam de revisão. O mecanismo e os sinais de transição seguem para definição. |
| C06 · Extensão localizada | Um Workspace estuda um consumidor da resposta de um integrador que passou a usar MCP do ODM. | A investigação autorizada localiza a orientação do integrador pela dependência, preserva sua origem e distingue a consulta à documentação da permissão para operar a ferramenta. |
| C07 · Solução e Negócios | A evidência técnica demonstra a análise manual no canal antigo, mas alguém quer decidir a regra de um novo canal. | O mapa técnico ajuda a localizar o comportamento implementado. O agente distingue o que a área confirmou, o que depende de fonte autorizada e o efeito da lacuna sobre o requisito. |
| C08 · Atualidade | Uma mudança externa altera o contrato que fundamenta uma orientação do agente. | Ao detectar a mudança, o conhecimento afetado deixa de ser usado como atual. Volta a valer após reconciliação e verificação. Correção documental inequívoca pode ser autônoma. Divergência sem solução demonstrada preserva as declarações. |

<a id="pendencias"></a>

## 5. Agenda de refinamento

Os itens P01–P09 são índices editoriais desta revisão. Guardam as perguntas remanescentes com seu efeito sobre o escopo. D02-PEN-001/002 avançaram com as respostas da conversa sobre suficiência e aviso, e seguem abertas nos limites indicados.

| Item | Próxima definição necessária | Base já estabelecida |
|---|---|---|
| P01 · Raiz e acesso | Definir o mecanismo de inicialização, a localização física da raiz comum versus Macro, o alcance de autenticação/publicação remota e a classificação padrão dos repositórios de Workspaces e mapas de arquitetura. | O fluxo “atualizar a raiz ao iniciar, carregar a atividade ao abrir” está aceito. Os efeitos de `private` e `internal` estão compreendidos. |
| P02 · Ferramentas | Identificar os recursos suportados em cada modalidade, configuração específica, verificação de versão efetiva e conduta diante de atualização indisponível. | Prioridade de Devin e Claude Code e objetivo de usar a última versão definidos. Fonte de download e mecanismo corporativo ficam para o contexto interno. |
| P03 · Conhecimento e suficiência | Rodada encerrada. P03.22 segue para desenho concreto dos documentos e P03.20/C-P03-07 para avaliação de qualidade e custo. | [20 das 22 perguntas originais resolvidas, DoD e direções transversais](refinamentos/P03-CONHECIMENTO.md), no alcance de Discovery. |
| P04 · Atualidade, autoridade e compartilhamento | [Rodada aberta](refinamentos/P04-ATUALIDADE.md). Responder P04.1–5 e P04.7–12. | D02-PEN-003/004/005. P04.6 herda a incorporação de entendimento já definida no P03 para o caso central. |
| P05 · Workspace | Definir o sinal de término da atividade se ele precisar ser representado, quem efetiva o vínculo permitido de Sigla e as condições de acesso ao histórico de outro Workspace. Refinar layout interno e se o repositório de Workspaces acumula a função do Meso. | A R06 encerrou a dúvida sobre a Sigla que guarda a branch. O nome, o estado próprio, os vínculos e o ciclo de vida conhecidos estão em PE-05. |
| P06 · Agente e histórias | Definir sinais de etapa, mensagens que atravessam etapas, retorno após interrupção, saídas esperadas e critérios por atividade. Refinar o mecanismo ServiceNow/IUClick e estados, gatilhos e responsabilidades operacionais. | R01-P007 e R06. O Analista aprova o refinamento. A mudança de papel do agente não altera as permissões. |
| P07 · Extensões | Definir padrão por tipo, reconhecimento das contribuições por escopo, precedência, resolução de conflitos, atualização ou retirada e rastreio do impacto. | Incorporação mediada pelo agente, descoberta por dependência e caso ODM em PE-07. |
| P08 · Arquitetura | Decidir entre preservar evidências, propor mapas ou entregar uma base verificável no primeiro recorte. Detalhar escopo funcional, identidade, revisão e manutenção conforme essa escolha. | O sistema mapeia as relações técnicas. O Analista delimita a solução. |
| P09 · Negócios | Escolher uma pergunta que a análise técnica sozinha não resolva. Determinar fontes, responsáveis, organização e menor saída útil ao engenheiro e ao agente. | A necessidade pertence ao escopo. A posição e a transversalidade permanecem em investigação. |

**Retomada vigente.** Iniciar por [P04.1](refinamentos/P04-ATUALIDADE.md#p04-rodada-1) e determinar o alcance da atualização quando houver nova revisão de um repositório. As fichas do grupo mantêm premissas, exemplos, impactos e recomendações por ID.

<a id="revisoes"></a>

## 6. Como incorporar conteúdo em novas revisões

Esta é a referência de partida. Cada novo conteúdo pode ser ligado a uma frente PE existente ou abrir uma frente nova. Para dar continuidade sem perder o histórico:

1. Registrar a manifestação e sua origem. Identificar se esclarece um item, amplia ou reduz o escopo, retifica uma definição, resolve uma pendência ou permanece como proposta.
2. Relacionar os itens PE e P afetados. Se houver conflito, indicar a redação anterior e o impacto sobre outros escopos, autoridade, evidências e cenários. Conservar os identificadores anteriores.
3. Incorporar a decisão explícita no alcance em que foi tomada. Hipóteses do agente permanecem identificadas como propostas. Pedir intervenção para a decisão material que as fontes não resolvam.
4. Atualizar as seções correspondentes, o mapa, a agenda e os cenários afetados. Incrementar a revisão deste documento e registrar o que mudou e a base utilizada.
5. Distinguir revisão do documento, validação de requisitos, publicação oficial e implementação. Quando houver publicação Git autorizada, registrar branch, commit imutável e verificação por releitura.

| Revisão | Conteúdo e efeito |
|---|---|
| 2 | Fechamento de P03 e abertura de P04 sobre a revisão 1 no commit `5f1d502a0b75fa24eb7616f930c2cf0415485ec8`. Impactos principais em PE-01, PE-03 e PE-04 e nos cenários C03, C04 e C08. Proveniência no [caderno ED11](refinamentos/historico/CADERNO-ED11.md) e no [manifesto R02](refinamentos/MANIFESTO-R02.json). |
| 1 | Fechamento do recorte funcional desta conversa. Integra D02, a proposta do PR #8, os esclarecimentos R06, as cinco notas temáticas e as decisões sobre lacunas e comunicação imediata. Esta revisão consolida o conhecimento disponível para refinamento. |

<a id="fontes"></a>

## 7. Fontes e recuperação

Consultar também os [esclarecimentos sobre o onboarding](evidencias/ESCLARECIMENTOS-ONBOARDING.md), a [síntese do caso Devin](evidencias/DEVIN-FERRAMENTAS.md) e o [roteiro por frente](roteiro/REFINAMENTO-E-REVISAO.md).

<a id="manifestacoes"></a>

**S · Manifestações diretas nesta conversa.** O usuário aceitou o onboarding de A sob as condições documentadas em PE-04, estendeu o mesmo raciocínio à lacuna interna e determinou aviso assim que o ponto for percebido. Delimitou as ferramentas, a atualização na inicialização, a atuação por etapa e as extensões pós-onboarding. Relatou o modelo de acessos por Sigla, aceitou o fluxo da raiz e dos submódulos e levantou a dimensão de Negócios. Solicitou nesta rodada o fechamento do escopo e a possibilidade de acrescentar conteúdo depois. Os exemplos de tarifa, duplicidade de abertura e novo canal apresentados pelo assistente são ilustrativos.

| Referência | Uso e revisão consultada |
|---|---|
| [F1] · Base D02 | Registro HUM-01 a HUM-11 r1, com as seis retificações e os dez axiomas r1. D02-doc-2 em `proposta/discovery-02-consolidacao`, HEAD verificado `8bbd93151640865995fa8a8dfe3d2d5db15da6ec`. [Estado](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/ESTADO-ATUAL.md) · [Retificações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/01-discovery/discovery-02/RETIFICACOES.md) · [Axiomas](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/fundacao/axiomas-arquiteturais.md) |
| [F2] · Motor e Workspaces | D02-ESP-001 r1, adendo funcional. Registra as saídas Micro/Meso e o vínculo futuro com as atividades. As definições posteriores do Workspace são recuperadas na R06. |
| [F3] · Motor e Arquitetura | D02-CONT-MOTOR-001 r1, lido no HEAD `766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455` do [PR #8](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/pull/8), aberto e sem merge na consulta. |
| [F4] · Workspace R06 | Síntese local do recorte de `plataforma_workspace_R06.zip`. Referência funcional do recorte recebido. Documentos 03 e 04 da revisão R06, registro de decisões, registro de pendências e fontes das rodadas. |
| [F5] · Ferramentas | Nota da sessão, revisão 1. Atualiza o recorte histórico que também considerava o GitHub Copilot. |
| [F6] · Atuação por etapa | Nota da sessão, revisão 1. Retoma R01-REQ-007, R01-ORI-004/005 e a pendência R01-P007. |
| [F7] · Extensões por escopo | Nota da sessão, revisão 1. Preserva o caso de referência do IBM ODM. |
| [F8] · Distribuição e acesso | Nota da sessão, revisão 3. A revisão 2 incorporou o relato de acessos por Sigla. A revisão 3 registra o aceite do fluxo. |
| [F9] · Conhecimento de Negócios | Nota da sessão, revisão 1. Distingue a necessidade levantada da hipótese de organização transversal. |
| [F10] · Fundação e panorama | Catálogo de capacidades e jornadas da IDE e [método de trabalho](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/fundacao/metodologia-fases.md). Referência para situar a primeira entrega no produto completo. |

**Verificação e limite de persistência.** As Instruções do Projeto foram recebidas automaticamente. Foram consultados o estado versionado, a retomada e o manifesto D02 no commit da base, os documentos do PR no respectivo commit, a R06 e as cinco notas da sessão. Os SHA-256 das cinco Fontes 00–04 disponíveis nesta conversa coincidem com o [recibo versionado](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/auditorias/prontidao-discovery-02/FONTES-NATIVAS-APLICADAS.json). A especificação complementar do Motor também coincide com o blob do PR. O outro complemento do Projeto, a síntese de ferramentas do Devin, contextualiza a experiência relatada e não fixa o catálogo de integrações desta entrega. O pacote R06 e as notas têm identidades próprias. A edição desta branch conserva as definições da revisão 1. A cópia anterior ao envio registrava a ausência de persistência naquele momento. O [manifesto da publicação](MANIFESTO.json) identifica os arquivos de origem e os blobs da edição para Git. A conferência remota da publicação é registrada no PR associado a esta branch.

[F1]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/01-discovery/discovery-02/REGISTRO.md
[F2]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md
[F3]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md
[F4]: evidencias/WORKSPACE-R06.md
[F5]: notas/FERRAMENTAS.md
[F6]: notas/ATUACAO-POR-ETAPA.md
[F7]: notas/EXTENSOES-POR-ESCOPO.md
[F8]: notas/DISTRIBUICAO-E-ACESSO.md
[F9]: notas/NEGOCIOS.md
[F10]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/fundacao/capacidades.md
[S]: #manifestacoes
