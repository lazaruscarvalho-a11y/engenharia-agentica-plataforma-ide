# Escopo integrado da primeira entrega — PE-01 a PE-09

Revisão R03 · 13/11/2026 · Discovery da Plataforma/IDE corporativa de Engenharia Agêntica. Base documental consultada: PR #9, branch `proposta/d02-primeira-entrega-refinamentos`, commit imutável `0cc6456fbd7613b9a4369d60684d0fe1170a2ed2`. Esta síntese conserva o perímetro funcional da R02 e aplica as decisões posteriores de P04 no alcance registrado em [P04-CONSOLIDADO](P04-CONSOLIDADO.md). Não demonstra produto implementado, pipeline examinada ou permissão operacional do banco.

## Propósito e funcionamento conjunto

A primeira entrega deve permitir obter a Plataforma na máquina de trabalho, produzir conhecimento rastreável de repositórios autorizados e usar esse conhecimento no refinamento de uma atividade com agentes. A raiz distribui recursos comuns e um catálogo de responsabilidades, escopo e domínio das Siglas. O Motor produz Micro por repositório e Meso por Sigla. O Workspace conserva o estado da atividade e recupera conhecimento pertinente ao pedido. O sistema evidencia relações técnicas; o Analista delimita a solução funcional. Arquitetura/Solução e Negócios têm necessidades reconhecidas, mas sua materialização ainda tem escolhas próprias.

O agente não deve carregar antecipadamente todas essas bases ao iniciar. A descoberta é gradual e dirigida; o mecanismo concreto foi postergado. Ao perceber dúvida, lacuna ou incoerência, ele a cataloga e informa prontamente. A ressalva volta a aparecer quando afetar direta ou indiretamente uma pergunta ou atividade, dentro ou fora do Workspace. Preservar contexto mínimo não permite omitir condição, exceção ou restrição que mude uma conclusão.

**Natureza:** perímetro e direções funcionais de Discovery; distribuição física, algoritmos, tecnologias, formatos, limiares e contratos operacionais permanecem candidatos onde não decididos expressamente. Fontes: [ESCOPO R02, abertura e §§1–3][escopo], [P03, §§2–5][p03] e P04/U3-C-P04-04.

## PE-01 — Distribuição, inicialização e acesso

**Fluxo aceito.** O engenheiro obtém a raiz comum no GitHub na primeira utilização e a atualiza ao iniciar. Publicar uma revisão dos mantenedores no remoto e receber essa revisão numa máquina são eventos distintos. A indisponibilidade de repositório privado de outra atividade não pode impedir a atualização da raiz comum.

Ao abrir um Workspace, a Plataforma busca as dependências pertinentes com a credencial do usuário, preservando a revisão referenciada por cada composição. Deve informar repositórios carregados, commits utilizados, falhas e cobertura parcial. Uma operação recursiva pode obter parte da árvore e falhar depois; o trabalho independente continua com sua limitação identificada. Atualizar submódulos não pode trocar silenciosamente a branch escolhida ou os ponteiros pretendidos.

**Relato corporativo, sem inspeção independente nesta missão.** A concessão de acesso é por Sigla e por serviço. Segundo o usuário, acesso GitHub da Sigla abrange seus repositórios; acesso AWS é independente. Repositório `internal` é legível ao público corporativo relatado. Branch de atividade isola contexto de trabalho, mas não cria público de leitura diferente daquele do repositório. Metadados de submódulo gravados no pai podem ser lidos no pai mesmo quando o destino é privado.

**Decisões posteriores de P04.** Aceitar publicidade corporativa de existência e identidade dos repositórios não cria acesso ao conteúdo privado. Consulta interna legitimamente acessível dispensa consentimento genérico adicional. Compartilhamento entre camadas tem padrão amplo somente para conhecimento legitimamente compartilhável, preservando proveniência e direitos reais. Aprovações específicas anteriormente definidas continuam aplicáveis.

**Aberto.** Classificação padrão de Workspaces e mapas, exceções de público, mecanismo de inicialização/atualização, recuperação de falhas, autenticação por operação, alcance da publicação remota e relação física entre raiz local, clone comum e Macro Git. A raiz local e o Macro possuem papéis distintos; sua identidade física não foi decidida. Não aplicar `main` do repositório de Workspaces como se fosse, por isso, branch de implantação de uma aplicação.

**Vínculos:** P01.1–7; P04.7–11; P05.5; P08.1/6; D02-PEN-003/004. Fontes: [ESCOPO R02, PE-01][escopo], [Distribuição e acesso r3][distribuicao], P04/U3-C-P04-01/02/03/05/06.

## PE-02 — Ferramentas, modalidades e portabilidade

**Decisão de recorte.** Suporte específico na primeira entrega a Devin Web, Devin CLI, Devin Desktop e Claude Code. A justificativa documentada é o uso frequente e consistente dessas ferramentas no ambiente relatado. GitHub Copilot, presente no panorama anterior, foi retirado desse recorte e pode ser avaliado posteriormente. Agnosticidade do núcleo e do conhecimento permanece direção transversal.

A Plataforma deve providenciar obtenção ou atualização necessária para usar a última versão das ferramentas ao iniciar. O usuário relata estruturas corporativas para isso; origem dos downloads e procedimento interno não foram especificados nem executados nesta missão. A atualização da raiz distribui os componentes comuns, mas não comprova a versão efetivamente em uso em cada modalidade.

O fluxo em que se abre terminal na raiz e se inicia `devin` ou `claude` é referência concreta da experiência CLI. Não presume mesma cópia local nem contexto automático em Web e Desktop. O comportamento funcional pretendido é comum; a obtenção efetiva dos recursos requer especificação por modalidade. Configurações `.devin/` e `.claude/` são exemplos de adaptações possíveis, sem conteúdo ou operações de preparação aprovados por este documento.

**Aberto.** Capacidade por tarefa/modalidade, descoberta de conhecimento, configuração específica, comprovação de versão, falhas de atualização e recuperação. RTK, Caveman, Context-Mode, Serena, Tree-sitter, SCIP, Joern e ripgrep constam no PDF histórico como ferramentas consideradas, não como stack escolhida ou capacidade demonstrada. Custos e qualidade por modalidade pertencem à avaliação postergada.

**Vínculos:** P02.1–5; P01.4/5; P03.20/22 e C-P03-07; D02-PEN-005. Fontes: [Ferramentas r1][ferramentas], [ESCOPO R02, PE-02][escopo], [PDF histórico, §§6 e 9][pdf], P04/U3-C-P04-04/09/10.

## PE-03 — Motor produtor, Micro, Meso e catálogo

**Definição funcional aceita.** O Motor produz a base do repositório e do estado efetivamente estudados. O engenheiro indica repositórios por diretório local, arraste para a pasta da Plataforma, links GitHub ou busca por Sigla. Pasta local conserva branch e diferenças autorizadas pertinentes em relação ao commit-base. Link remoto para a raiz usa `main`; link de branch específica é escolha explícita. Falha de obtenção gera cobertura parcial identificada.

O Motor investiga responsabilidades, fluxos, regras, código, contratos, integrações, APIs, workers, mensageria, bancos, configurações, bibliotecas, infraestrutura e procedimentos de execução/testes documentados conforme aplicabilidade. Durante onboarding, não refatora, renomeia nem reorganiza a aplicação. Conhecer o procedimento de execução não autoriza executá-lo.

Micro corresponde ao repositório individual. Meso é repositório específico da Sigla/conta, com Micro como submódulos. Macro é workspace Git com Meso como submódulos. Não há sincronização de ponteiros, acesso ou redistribuição implícitos. Pertencimento organizacional, dependência técnica e participação na mesma solução são relações diferentes.

O Meso indexa responsabilidades para conduzir ao Micro pertinente e identifica revisões e cobertura. O usuário dispensou conhecer ou provar o total de repositórios da Sigla; isso não dispensa relatar seleção, busca efetiva, material obtido, analisado e falhas conhecidas. O catálogo da raiz integra a primeira entrega, é legível independentemente da Sigla e pode orientar roteamento por atribuição ainda declarada, mantendo origem e revisão. Corroboração exige evidência própria.

**Fronteira aceita produtor/consumidor.** Para concluir o onboarding, demonstrar entrada, cobertura de descoberta, comportamentos materiais, consolidação do conhecimento válido, rastreabilidade/coerência, tratamento de lacunas e entrega. Não exigir objetivo particular do engenheiro nem êxito de uma consulta posterior por outro agente para encerrar o produtor. A interação posterior avalia a suficiência para a pergunta ou ação concreta.

**Representação.** Manter origem principal por fato. Explicar condições e efeitos materiais; usar referência canônica suficiente e autorizada quando ela preservar toda a resposta; manter implementação interna no código quando não alterar efeitos materiais; explicitar lacunas e contraevidências. O desenho de documentos, índices, formatos e granularidade está postergado em P03.22. Avaliação formal de segurança, precisão, confiabilidade e custo está adiada em P03.20/C-P03-07.

**Vínculos:** P03.1–22 e C-P03-01..08; P01/P02/P04; D02-PEN-001/002/005. Fontes: [P03 temático, §§1–7][p03], [D02-ESP-001, fronteiras e comportamento][esp], [BASE-P03-HUM](BASE-P03-HUM.md). D02-ESP-001 e o PDF são históricos nos pontos posteriormente refinados.

## PE-04 — Evidência, ressalvas, validade e manutenção

**Conduta funcional aceita.** Cada afirmação é ligada à revisão e ao suporte mais específico possível. Explicitar material examinado, exclusões, inacessibilidades, contradições, condições e limites. Uma chamada de A a C sustenta a relação observada do lado de A; não comprova a implementação interna de C. Falta de acesso direto, falta de onboarding, referência indireta e conhecimento histórico legítimo são estados distintos.

**Aceites delimitados A/B/C.** A pode concluir onboarding com ressalva quando: (a) emite `codigoSegmento` para B e C, mas não se sabe se C aceita sua ausência; ou (b) existem duas regras locais para calcular segmento e falta evidência sobre quando aplicar cada uma. Em ambos, todas as dúvidas percebidas devem ficar definidas, localizadas, detalhadas e referenciadas no próprio A. O aceite não autoriza retirar o campo, escolher precedência da regra ou generalizar a ressalva para qualquer lacuna. A ação posterior depende de evidência pertinente.

Pendência crítica impede a conclusão dependente. O agente entrega a parte independente, comunica prontamente a limitação e investiga fontes autorizadas. Persistindo criticidade incerta, leva ao engenheiro a menor pergunta útil, com tentativas, hipóteses e evidências. A primeira entrega inclui o fluxo excepcional de pedir execução local futura por dúvida intransponível após esgotar investigação autorizada; deve oferecer esclarecimento direto como alternativa e detalhar finalidade, ambiente, dados, comandos e efeitos. A execução requer permissão específica por ocorrência. Nesta missão documental, aplicações não são executadas.

**Manutenção e colaboração.** HUM-08 exige detectar mudança, invalidar afetados, reconciliar e verificar antes de restaurar validade. Sem monitor demonstrado, detecção ocorre na próxima leitura/ciclo. Composição multirrepositório explicita commits e ponteiros; não promete atomicidade física. O requisito de atualização/revalidação do conhecimento antes de cada push refere-se ao conteúdo exato candidato; nova alteração invalida a prova. Esse mecanismo determinístico ainda precisa ser construído e demonstrado.

S1 permite corrigir autonomamente no destino autorizado somente quando a evidência demonstra a inconsistência e determina a correção. S2 exige pedido de incorporação de novo entendimento com entendimento, origem, destino e efeito; confirmação abrangente basta, direitos reais permanecem, silêncio gera pendência e negativa descarta aquele destino. S3 conserva declarações concorrentes, origem, revisão e consequência até reconciliação fundamentada. A dispensa P04 de consentimento genérico de leitura não elimina S2.

**Branch e ambiente.** O usuário informou que main recebe mudanças após pipeline que efetivamente implanta em PROD e que o processo correspondente associa releases a HOM; a última release é a referência de HOM no universo relatado. Preservar essa premissa de seleção, com commit exato. Não declarar inspeção independente da pipeline, configuração efetiva ou ocorrência concreta. O estado utilizado inclui diferenças locais pertinentes e a composição escolhida, sem promoção silenciosa de outra branch.

**Vínculos:** P03.9/11–17/19–21; P04.1–12 e dez colaterais finais; HUM-03/06/08/09; D02-PEN-001..005. Fontes: [Onboarding com ressalvas][ressalvas], [P03, §§3–4][p03], [HUM e pendências D02][registro], [P04-CONSOLIDADO](P04-CONSOLIDADO.md).

## PE-05 — Workspace, atividade e história

**Definição R06.** Workspace é o contexto em que Negócios, Tech Lead e analistas técnicos refinam uma atividade. Atividade é o conjunto de histórias e tasks em trabalho. Sua pasta conserva fontes recebidas, hipóteses, requisitos, decisões e pendências. Estado documental, revisão do código das aplicações e status de histórias no sistema corporativo podem evoluir separadamente.

Na área local, Workspaces aparecem em `workspaces/` na raiz. No Git, cada Sigla possui repositório para seus Workspaces. O agente pergunta e o engenheiro informa a Sigla do time ou analista executor; a branch é criada nesse repositório mesmo que a atividade envolva aplicações de outras Siglas. Cada branch de Workspace contém na raiz apenas a pasta da atividade, sem outros Workspaces.

O agente começa pelo material associado à atividade, segue pistas até índices e bases pertinentes e pergunta à pessoa solicitante somente quando persiste lacuna. Sugere inclusão de repositório; o engenheiro decide e o agente efetiva como submódulo se autorizado. Sugere vínculo de Sigla; o Analista permite, disponibilizando seus índices, sem incluir automaticamente todos os repositórios. Outro Workspace pode ser consultado para histórico/entendimento dentro dos direitos efetivos.

Uma feature pode participar de vários Workspaces; cada história, task, subtask ou bug pertence a um único Workspace. Aprovação delimitada do refinamento cabe ao Analista e tem marco diferente do término da atividade. Ao terminar a atividade, o time escolhe excluir a branch ou arquivar a pasta em `workspaces/` na main do repositório de Workspaces. Isso não constitui autorização desta missão para excluir branches.

**Aberto.** Sinal de término se precisar ser representado, quem efetiva o vínculo da Sigla permitido, controles de acesso ao histórico, layout interno e conteúdo mínimo de retomada, apresentação de sugestões e identidade física entre repositório de Workspaces e Meso. O estado próprio da atividade já foi definido; não recolocá-lo como hipótese por ler adendo mais antigo.

**Vínculos:** P05.1–6; P01.1/3; P06; P03/S2; P04. Fontes: [Workspace-R06][r06], [ESCOPO R02, PE-05][escopo], [Distribuição e acesso][distribuicao].

## PE-06 — Atuação por etapa e integrações de trabalho

**Direção de primeira entrega.** A Plataforma deve coordenar interpretação, investigação, atuação e resposta conforme a etapa e o objetivo de cada item. Inclui refinar negócio/produto, definir requisitos, histórias, tasks, subtasks e bugs e planejar arquitetura/software, recursos AWS, repositórios, mudanças de aplicações, testes e validações. Quantidade de agentes, sua distribuição entre componentes e mecanismo de orquestração permanecem abertos.

Analista, de negócios ou não, aprova formalmente a conclusão do refinamento no alcance especificado, por iniciativa própria ou após pergunta do agente. Após o refinamento aprovado, histórias são criadas e associadas às features. ServiceNow/IUClick é o destino funcional definido para criar, modificar e alterar status de histórias. Mecanismos, transições, gatilhos e autoridade de cada operação ainda precisam de especificação. A operação definida para histórias não estende automaticamente a mesma integração a tasks, subtasks e bugs.

**Exemplo proposto.** A frase “o mesmo pedido não pode abrir duas contas” pede esclarecer identidade do pedido no negócio, traduzir regra acordada em critérios na história, investigar componentes/contratos no planejamento e descrever evidências de reenvio e pedidos legítimos no teste. Os nomes das etapas e respostas concretas são propostas, não máquina de estados aprovada. Se a regra mudar durante o planejamento, recuperar a decisão anterior e os efeitos sobre história, critérios, arquitetura e testes é cenário de refinamento.

**Aberto.** Sinais por item, transições, mensagens entre etapas, recuperação após interrupção, saídas e suficiência por atividade, além dos contratos corporativos. Mudança de papel não altera permissões. Planejamento pode conter ações concretas e dependências; executar exige especificações e autorizações próprias.

**Vínculos:** P06.1–7; R01-P007; P05; P03/S2; P02; P04. Fontes: [Atuação por etapa][etapa], [Workspace-R06, refinamento e trabalho][r06], [ESCOPO R02, PE-06][escopo].

## PE-07 — Extensões por escopo

**Direção aceita.** Mesmo após onboarding e internalização, usuário deve poder acrescentar skills, instruções, comportamentos, documentação e ferramentas, inclusive via MCP, a repositório, Sigla, Workspace ou arquitetura. O agente conduz a inclusão segundo padrões da Plataforma, identificando origem, escopo, finalidade e quando/como aplicar. Descobre o recurso por pergunta direta ou dependência, dentro ou fora de Workspace.

O caso de referência é um integrador que reúne resultados e os envia ao IBM ODM, recebe decisão e posteriormente ganha MCP e instruções de uso. Uma atividade num consumidor pode alcançar esse recurso pela dependência mesmo que a pessoa desconheça seu nome. O agente distingue preparação de dados no repositório, regra aplicada no ODM e evidência efetivamente obtida. Consulta à documentação, inclusão do repositório e operação de ferramenta são objetos separados; acesso à instrução não autoriza operar ODM.

**Aberto.** Contrato mínimo por tipo de contribuição, reconhecimento por escopo, pertinência indireta, precedência, sobreposições/conflitos, atualização/retirada e efeito nos consumidores. O suporte a extensões no escopo arquitetura não decide se a primeira entrega terá base arquitetural materializada. Extensibilidade da Plataforma e extensões de conhecimento/capacidades de cada repositório são direções relacionadas, mas distintas.

**Vínculos:** P07.1–5; P02; P03.22; P04; P08. Fontes: [Extensões por escopo][extensoes], [ESCOPO R02, PE-07][escopo], [Referência funcional Devin][devin].

## PE-08 — Arquitetura e delimitação de solução

**Direções registradas.** O sistema mapeia relações técnicas. O Analista delimita a solução funcional: finalidade, resultados, variantes e relações pertencentes ao recorte. Uma solução pode atravessar Siglas, ter ramos, retornos, ciclos, múltiplas entradas e processamento assíncrono. Um componente pode participar de várias soluções com papéis diferentes. Conectividade técnica sozinha não prova identidade de solução.

No cenário histórico sintético, A chama B, B publica evento para C e C retorna resultado a A; B também atende outra solução e C tem acesso parcial. O sistema pode preservar evidência dos vínculos e suas revisões; a confirmação funcional e o trecho técnico ainda não demonstrado continuam identificados separadamente. Dois mapas podem referenciar a mesma operação de C sem manter duas origens independentes do fato.

**Escolha ainda aberta.** Motor já conserva evidências de relações; decidir se o primeiro recorte apenas prepara essa evidência, propõe mapas candidatos ao Analista ou entrega base arquitetural verificável. Nome, identidade, unidade, início/fim, composição por revisão/ambiente, grau de profundidade, titularidade entre Siglas, manutenção e publicação dependem dessa escolha. A direção conceitual de base de ponta a ponta não aprova esquema ou topologia física.

**Vínculos:** P08.1–6; P01.2/7; P03; P04; P07; P09. Fontes: [PDF histórico, §§3 e 7–8][pdf], [Retomada Motor/Arquitetura, direções 4–6][arquitetura], [ESCOPO R02, PE-08][escopo].

## PE-09 — Conhecimento de Negócios

**Necessidade incluída para refinamento.** Recuperar contexto de produto, jornada e operação que não se deduz integralmente da evidência das aplicações. Código e testes podem demonstrar encaminhamento implementado sem explicar a finalidade da política, seu público ou a operação humana posterior.

**Cenário proposto.** Uma resposta do ODM leva um canal antigo à análise manual. Ao projetar canal novo, a mesma implementação pode representar política do produto ou contingência temporária do canal original. Fonte legítima e responsável de negócio precisam esclarecer a diferença; ela altera história, critérios e responsabilidade. Ausência dessa fonte conserva lacuna, sem transformar código em política universal.

**Hipótese, não organização aprovada.** Dimensão transversal consultável pelo Workspace, com percurso de regra/conceito a jornadas/soluções e caminho inverso. Não decorrem daí pasta, repositório, hierarquia ou público de leitura definidos. Permanecem pergunta inicial, fonte, autoridade, unidade de organização, saída mínima, vigência, revisão e público. Não escolher produto/domínio/processo/jornada por inferência.

**Vínculos:** P09.1–7; P08; P03/S2; P04; P01. Fontes: [Negócios r1][negocios], [ESCOPO R02, PE-09][escopo].

## Evolução material e leitura de fontes históricas

| Fonte anterior e ponto | Estado preservado | Refinamento que prevalece e efeito |
|---|---|---|
| PDF de 07/11, §1.2 e §8.1: entrada GitHub e forma de indicar revisões aberta | Snapshot histórico íntegro | P03.7 aceita quatro entradas, distingue estado local, main padrão e branch explícita. Credenciais e tratamento técnico continuam abertos. |
| PDF §1.4: presença da exceção de execução local no Motor inicial em aberto | Não inventar que estivesse incluída nesse momento | P03.21 a inclui como fluxo excepcional da primeira entrega nas condições HUM-03. Não autoriza execução nesta missão. |
| PDF §2.5 e D02-ESP-001: estado persistido/conteúdo próprio do Workspace por desenhar | Registro histórico do alcance então discutido | R06 fixa estado próprio, repositório por Sigla executora e branch por Workspace. Layout e mecanismos seguem em aberto. |
| PDF §6.2 inclui Copilot na agnosticidade de ferramentas | Direção histórica ampla preservada | Nota Ferramentas recorta suporte específico a Devin e Claude Code na primeira entrega, sem abandonar agnosticidade do núcleo. |
| PDF §§4/6/8 e modelo D02 candidato: avaliação por tarefa/mudança | Propostas e consumidor posterior continuam pertinentes | P03 edição 8 separa DoD do produtor do objetivo particular/consulta posterior; não usar o texto antigo para reabrir P03.1/2. |
| PDF §5.2 e HUM-06: modalidades de autorização herdadas | Operações e direitos distintos são preservados | P04/U3 elimina consentimento genérico adicional para leitura interna acessível; mantém aceites específicos, retenção/distribuição legítimas e ausência de direitos novos. |
| PDF §5.1: branch/commit/implantação distintos | Distinção probatória permanece | P04/U3-C-P04-08 acrescenta convenção main/PROD e release/HOM no universo relatado; não transforma relato em inspeção de pipeline. |
| PDF §§3/8: base arquitetural e fronteiras em aberto | Necessidade e responsabilidades registradas | PE-08/P08 mantêm a decisão sobre materialização inicial; P03/catalogação e P07/extensão não a fecham por analogia. |
| ESCOPO R02: P04 aberto e retomada P04.1 | Retrato correto da R02 | R03 registra fechamento funcional no alcance recuperado, com fonte indireta dos aceites P04.1–5 e mecanismos posteriores; próxima sessão pode escolher outro grupo. |
| Diagrama da primeira entrega, escopo r2 | Resumo visual de produção, organização e refinamento | Não é especificação exaustiva. “Arquitetura — base em decisão” e “Negócios — em refinamento” preservam as escolhas abertas; setas não comprovam sincronização, integração ou autoridade. |

O PDF histórico foi consultado por extração das onze páginas. Sua identidade: 112596 bytes, SHA-256 `9b06d50e2f98355c2d0c5eefa8e4d1d35266cc52b15a499155c2fa75063099dd`, blob Git `d655c43ed83491f9e3e4355460dd6fc7f40bdb73`. A extração textual serve ao confronto semântico; a inspeção visual do diagrama foi realizada pelo coordenador. O PDF cita BASE-01, ZIPs, 98 segmentos, 299 unidades e ensaios históricos: são registros atribuídos àquele snapshot, não medições refeitas aqui. Referências originais privadas e mensagens históricas não recuperadas não são declaradas relidas por esta síntese.

## Dependências e fronteiras de continuidade

O catálogo granular [PENDENCIAS-P01-P09](PENDENCIAS-P01-P09.md) preserva as 77 perguntas. P03 tem vinte respostas resolvidas funcionalmente, P03.20/C-P03-07 adiados e P03.22 com direção aceita/desenho postergado. P04 está funcionalmente encerrado no alcance documentado; suas provas de engenharia e a proveniência original dos primeiros aceites têm estados próprios. Não fechar P01/P02/P05–P09 por analogia.

Recomendação metodológica: definir o recorte de saída P08.1 antes de escolher armazenamento/publicação de mapas; usar uma pergunta de negócio P09.1 antes de escolher organização; confrontar um cenário compartilhado entre P02/P03.22/P07 para descoberta e adaptação por modalidade. Isso não é prioridade de negócio aprovada. Perguntas independentes podem avançar sem aguardar todas as frentes.

O produto completo pretendido inclui execução supervisionada, PR/CI-CD, incidentes, hotfix e GMUD, além das capacidades de compreensão/refinamento/planejamento deste recorte. A fundação documental e o harness assistido não demonstram essas capacidades. Sem stack, UI final, SLA ou limiares aprovados. PGC-001 v1.1.3 e CT-001..CT-008 v1.0.3 permanecem NÃO RATIFICADOS; 49 CA operacionais NOT_RUN. Teste documental e ensaio de retomada não são teste operacional da IDE nem nova conversa real de usuário.

## Rastreabilidade inversa deste documento

| Fonte consultada | Informações incorporadas e destino |
|---|---|
| ESCOPO R02 §§1–3 e agenda | Perímetro de nove frentes, graus de definição e limites; PE-01..09 e continuidade |
| P03 temático §§1–7 e esclarecimentos onboarding | Entradas, DoD, catálogo, ressalvas, escrita, pré-push, versões; PE-03/04 |
| R06 e nota Distribuição r3 | Estado/ciclo de vida/vínculos do Workspace e fluxo de acesso; PE-01/05/06 |
| Nota Ferramentas r1 | Recorte, atualização e adaptações; PE-02 |
| Nota Atuação r1 | Requisito por etapa, exemplos propostos e contratos pendentes; PE-06 |
| Nota Extensões r1 e referência Devin | Incorporação/descoberta por escopo e permissões por operação; PE-07 |
| Nota Negócios r1 | Necessidade, cenário sintético e hipótese transversal; PE-09 |
| D02-ESP-001 e retomada Motor/Arquitetura | Micro/Meso, relações técnicas, autoridade e perguntas históricas; PE-03/08 e evolução |
| PDF histórico §§1–10 | Contexto anterior, cenários arquiteturais, candidatos e limitações; PE-02/03/08 e evolução |
| Diagrama r2 | Leitura visual resumida e limites; evolução |
| HUM/retificações D02 e P04/U3 | Fronteiras de autoridade, topologia, atualização e refinamentos posteriores; PE-01/03/04 e continuidade |

[escopo]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md
[p03]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md
[distribuicao]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/notas/DISTRIBUICAO-E-ACESSO.md
[ferramentas]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/notas/FERRAMENTAS.md
[r06]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/evidencias/WORKSPACE-R06.md
[etapa]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/notas/ATUACAO-POR-ETAPA.md
[extensoes]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/notas/EXTENSOES-POR-ESCOPO.md
[negocios]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/notas/NEGOCIOS.md
[devin]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/evidencias/DEVIN-FERRAMENTAS.md
[ressalvas]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md
[esp]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md
[arquitetura]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md
[pdf]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf
[registro]: https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/REGISTRO.md
