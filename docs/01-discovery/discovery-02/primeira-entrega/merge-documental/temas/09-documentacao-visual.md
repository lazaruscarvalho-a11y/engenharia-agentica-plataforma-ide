# Como representar e conferir a arquitetura de uma Solução

<a id="a09-001"></a>

A finalidade definida para a descoberta orienta a escolha da vista. A representação ajuda o Analista a avaliar o alcance e as relações que o agente encontrou. A decisão sobre a camada da Solução vale independentemente do software usado. As alternativas e capacidades de ferramentas descritas aqui são do estudo F2, edição de 22/11/2026. [Autoridade em PE-08](01-visao-e-autoridade.md#pe08).

<a id="origem"></a>

## Como saber o que o desenho representa

<a id="a09-002"></a>

F2 relata páginas por repositório, uma documentação consolidada e dificuldade para ler diagramas draw.io associados ao nome CodeWiki 2.0. Sem um diagrama original e o contexto de leitura, permanecem abertas as causas da dificuldade. O breve teste relatado em F1 também carece de identidade de versão e configuração.

<a id="a09-003"></a>

A pesquisa sobre FSoft-AI4Code/CodeWiki identifica como possíveis entradas `module_tree.json`, `metadata.json`, `temp/dependency_graphs`, `temp/artifact_index.json` e páginas Markdown. Identificar implementação, revisão e arquivos realmente disponíveis antes de atribuir essas saídas ao CodeWiki usado. F2 registra atualização incremental e consulta via MCP; a CLI fornece um ponto inicial a testar.

<a id="a09-004"></a>

A resposta MCP pode conter um caminho da área temporária `.codewiki/sessions`, removida ao encerrar. A prova de ponta a ponta precisa mostrar que a modalidade consegue abrir o arquivo a tempo e conservar legitimamente o material necessário. Shell, IDE, Browser e transporte STDIO/SSE/HTTP descritos no catálogo não demonstram leitura do retorno no ambiente concreto. [Integrações por cliente](04-integracoes-e-harness.md).

<a id="a09-005"></a>

Associe cada componente e relação a origem, revisão e natureza da evidência. Nome de módulo, chamada no código, inferência, confirmação humana e observação de implantação sustentam afirmações diferentes. Uma ligação pode atravessar Micros e Siglas; ausência de aresta em grafo parcial não demonstra inexistência. Um repositório pode abrigar mais de uma aplicação. Identificar composição, compartilhamentos, caminhos e partes ainda desconhecidas, e revalidar as relações após mudança. [Composição da Solução](02-camadas-e-workspaces.md#camada-solucao) · [DEC-041](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-041), [DEC-044](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-044).

<a id="vistas"></a>

## Qual pergunta a vista deve responder

| Vista proposta | Pergunta, conteúdo e limite da evidência |
|---|---|
| <a id="a09-006"></a> Ecossistema | Quais atores, sistemas e domínios participam e quais fronteiras continuam desconhecidas? Identificar as grandes integrações no escopo delimitado. |
| <a id="a09-007"></a> Conjunto | Como serviços, filas e bancos colaboram para produzir o resultado? Escolher recursos com evidência da participação na finalidade. |
| <a id="a09-008"></a> Integração | Quem envia e quem recebe? Explicitar direção, contrato, protocolo e sincronia somente onde sustentados. Encontrar o emissor não demonstra processamento pelo consumidor. |
| <a id="a09-009"></a> Repositórios | Onde vive o código de cada responsabilidade? Ligar módulos e componentes às revisões. Testar a correspondência com unidades implantadas quando isso importar. |
| <a id="a09-010"></a> Fluxo | O que acontece neste cenário? Registrar entradas, chamadas, decisões, retornos, erros e variações que a evidência permite explicar. |
| <a id="a09-011"></a> Infraestrutura | Em qual ambiente executam os componentes? Uma afirmação sobre produção precisa identificar a implantação. A branch mostra um estado do código. |

<a id="a09-012"></a>

Um modelo lógico pode se distribuir por arquivos e projetos se identidades e relações permanecerem coerentes. Em cada vista usar o nível de detalhe necessário ao leitor; texto complementar conserva razões, qualificadores e fronteiras que a figura não comunica. F2 sugere as seis vistas como opções. O piloto compara três.

<a id="ferramentas"></a>

## Que ferramenta comparar para cada finalidade

<a id="a09-013"></a>

F2 recomendou avaliar LikeC4 como modelo navegável e D2 como complemento para vistas estáticas, comparando também a melhoria do draw.io existente para o mesmo objetivo. Os exemplos de layout e as referências S01–S30 são do catálogo. A escolha, as condições de licença no uso pretendido e os ganhos no ambiente exigem avaliação específica.

| Opção no catálogo F2 | Comportamento documentado e condição a verificar |
|---|---|
| <a id="a09-014"></a> LikeC4 | Modelo textual com elementos e relações identificados, várias vistas, CLI de validação, site estático, exportação e consulta MCP opcional. Licença do núcleo registrada como MIT. Divisão entre projetos exige carregá-los no mesmo workspace para importar elementos de nível superior. Verificar versão, layout e acesso reais. |
| <a id="a09-015"></a> D2 | Linguagem e CLI para saídas estáticas, registrados como MPL-2.0. F2 lista SVG, PNG, PDF, PPTX e GIF. Comparar fidelidade e estilo ao derivar de LikeC4; a disponibilidade de um formato não prova preservação. |
| <a id="a09-016"></a> TALA, ELK, Dagre | TALA usa disposição ortogonal e posições calculadas ou indicadas. F2 registra a abertura de TALA em 07/09/2026 e inclusão no D2 0.9.0, MPL-2.0. ELK atende hierarquia, direção e portas; Dagre, grafos dirigidos. Distinguir implementações Go do D2 das bibliotecas ELK.js (EPL-2.0) e Dagre (MIT). Medir deslocamentos após pequenas mudanças e custo em grafos amplos. |
| <a id="a09-017"></a> Structurizr | Alternativa para C4 formal. F2 distingue projeto Apache-2.0, comando local sucessor do Lite sem autenticação/colaboração, servidor aberto compilável sem autenticação/RBAC e binários oficiais do servidor licenciados. Testar perdas em Mermaid, PlantUML, HTML, PNG e SVG. |
| <a id="a09-018"></a> Mermaid | Fluxo e sequência junto do Markdown; CLI MIT com SVG, PNG e PDF. F2 registra ELK padrão a partir de 12.0.0 em vários tipos (flowchart, state, class e entity relationship). C4 depende de ordem e configuração; conferir o renderizador efetivamente usado. |
| <a id="a09-019"></a> Excalidraw | Editor e CLI registrados como MIT. Edição livre, frames, PNG/SVG local e conversão de parte dos diagramas Mermaid em formas. A manutenção de identidades entre vistas permanece uma questão para modelo compartilhado. |
| <a id="a09-020"></a> draw.io | Preservar o original e ensaiar normalização, layout e exportação em cópia. Separar editor Apache-2.0, Desktop GPL v3 e condições dos demais ativos. O reparo pode reduzir a transição onde servir à mesma pergunta. |
| <a id="a09-021"></a> Graphviz e Cytoscape.js | Graphviz trabalha com grafos DOT e aparece no layout LikeC4; licença registrada como EPL-2.0. O núcleo e extensões oficiais de Cytoscape.js são registrados como MIT e permitem desenvolver exploração interativa com filtros. A interface e sua manutenção seriam trabalho adicional. |

<a id="exportacao"></a>

## O que permanece após exportar e regenerar

<a id="a09-022"></a>

Se LikeC4 for adotado, o arquivo ou conjunto autoritativo regerá a geração das vistas. Código, documentos e outras evidências continuam sustentando o significado arquitetural. Uma alteração de relação deve voltar ao modelo. Ajustes visuais exigem configuração reproduzível ou exceção editorial identificada. Registrar versões das fontes e ferramentas e saber qual saída regenerar em cada mudança.

<a id="a09-023"></a>

F2-P061 e F2-P134–136 distinguem dois testes. O draw.io recebe os nós e relações resultantes, em um arquivo por vista ou em abas. As regras de **inclusão, exclusão e estilo** que geraram a vista ficam no modelo. Uma imagem legível pode deixar de ser regenerável. CLI, editor e Playground não oferecem retorno suportado das alterações em draw.io; conversores de baixo nível exigiriam ensaio separado. Manter os originais e avaliar por vista reparo, reconstrução ou complemento. A pesquisa nominal de S2 em 290 arquivos textuais da R04, junto à leitura de P08 e dos refinamentos postergados, localizou a novidade nesse recorte. O resultado não exclui outros termos nem documenta capacidade atual fora daquela edição. [Decisão sobre a camada](01-visao-e-autoridade.md#pe08).

<a id="piloto"></a>

## Como conduzir a comparação proposta

<a id="a09-024"></a>

Inventariar materiais e revisões, extrair elementos e responsabilidades, reconciliar nomes, explicitar a pergunta, gerar a definição e a imagem e verificar três resultados separadamente. O validador da linguagem cobre diagnósticos de sintaxe, semântica e layout. A fidelidade de uma aresta depende de sua fonte. A leitura de rótulos e cruzamentos exige inspeção no meio real.

<a id="a09-025"></a>

Escolher três vistas representativas, incluindo uma com dificuldade concreta. Na consolidada, comparar LikeC4 e reparo do original; se C4 formal for decisivo, considerar Structurizr. Na de repositório, verificar o detalhe no conjunto. Na de integração, conferir sentido e tipo das conexões com os layouts D2 ou, para sequência, Mermaid. Ampliar a amostra quando a comparação deixar uma dúvida material.

<a id="a09-026"></a>

Os C01–C10 de F2 comparam fidelidade, resposta à pergunta, rótulos, conexões, hierarquia, navegação, validação, conversão, regeneração/manutenção e esforço. Conferir licença por componente. Alterar uma relação sustentada, regenerar e registrar tempo, perdas e ajustes. Pesos e notas mínimas permanecem abertos. Cortes impeditivos podem exigir vista mais seletiva; reduzir a fonte ou eliminar todo cruzamento tem custo de leitura. [Critérios e provas](12-avaliacao-riscos-e-provas.md).

<a id="instrucao"></a>

## O que o exemplo de instrução solicitava

<a id="a09-027"></a>

O catálogo contém uma instrução exemplificativa de quatro parágrafos seguida de complementos editoriais. Seu texto original permanece em F2 na seção 11. A forma imperativa pertence à tarefa hipotética documentada.

<a id="a09-028"></a>

O primeiro parágrafo enumerava documentação consolidada, páginas individuais, artefatos estruturados disponíveis e diagramas draw.io existentes. Para usá-los seriam necessários acesso e revisões aplicáveis.

<a id="a09-029"></a>

O segundo propunha LikeC4 para o modelo central e D2 com TALA/ELK para as vistas estáticas.

<a id="a09-030"></a>

O terceiro pedia preservar relações comprovadas, marcar inferências e divergências e evitar introduzir componentes sem fonte.

<a id="a09-031"></a>

O quarto propunha três vistas, validação, renderização, inspeção de legibilidade, sobreposições, cruzamentos e hierarquia e uma comparação antes de expandir.

<a id="a09-032"></a>

Os complementos da revisão acrescentam versões, direitos e licenças, perdas, a opção de reparar uma cópia e a comprovação de acesso a arquivos indicados pelo MCP. Definições textuais, imagens, comandos, referências e comparação C01–C10 são entregáveis sugeridos. O catálogo não registrou execução do piloto.

<a id="escolhas"></a>

## O que falta saber antes de escolher

<a id="a09-033"></a>

Identificar projeto e versão do CodeWiki, materiais, revisões, relações e direitos efetivamente disponíveis. Um benchmark ou uma instalação homônima não responde à pergunta.

<a id="a09-034"></a>

Identificar público, contexto de leitura, defeito observado e saída que precisa editar ou consumir, por exemplo site, SVG, PDF ou draw.io.

<a id="a09-035"></a>

Verificar dependências e caminhos que o Devin consegue acessar na modalidade indicada. Definir com os responsáveis autorizados a divisão por domínio ou projeto, a origem do modelo e o destino dos ajustes. Abrir o repositório da Solução não confere titularidade permanente sobre seus desenhos.

<a id="figura-historica"></a>

## Como ler o diagrama histórico da primeira entrega

A figura de Escopo r2/P03 mostra, em três colunas, o motor que produz Micro/Meso, a distribuição pelo Macro e pela raiz e o trabalho de Workspace, agente e equipe. As setas distinguem ação do agente e reflexo de mudança. Os benefícios no rodapé são potenciais. O rodapé ainda indaga a identidade física da raiz e o selo da Solução diz “BASE EM DECISÃO”. DEC-003 e DEC-042 responderam a esses objetos. A figura continua íntegra como registro daquela revisão; para a leitura corrente, aplicar os dois esclarecimentos e conservar em aberto a identidade física Workspace/Meso e o ferramental. [Diagrama histórico](../../referencias/Diagrama-Engenharia-Agentica.pdf) · [DEC-003](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-003), [DEC-042](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-042).


<a id="catalogo-visual"></a>

## O que foi pedido e o que o estudo acrescentou

F2 separa cinco necessidades de origem, doze funcionalidades propostas e sete detalhes editoriais. Essa distinção permite recomendar um piloto sem transformar preferências de layout em decisões do produto.

| Série do catálogo | Aplicação no trabalho com a vista |
|---|---|
| N01–N05 · necessidades | Reutilizar as páginas e a consolidação (N01), melhorar a leitura dos diagramas existentes (N02), investigar opções abertas utilizáveis com Devin (N03), reunir os assuntos, ferramentas e motivos num catálogo (N04) e conferir a fidelidade, clareza, organização e cobertura do conteúdo (N05). |
| F01–F04 · entrada e reconciliação | Analisar as fontes disponíveis, identificar elementos com responsabilidade explícita, qualificar direção e natureza das relações e resolver ou registrar divergências de nome, comportamento e fonte. |
| F05–F09 · leitura e formatos | Relacionar repositórios sem presumir um serviço por repositório; escolher níveis/públicos; oferecer navegação interativa quando útil; gerar saídas estáticas, sobretudo SVG; testar saída editável em draw.io quando exigida. |
| F10–F12 · operação e conferência | Testar edição/validação/geração pela CLI; consultar o modelo por MCP apenas se conveniente, disponível e acessível; verificar definição, correspondência com as fontes e leitura no protótipo antes de ampliar. |
| D01–D04 · reprodução | Ligar elemento e aresta à fonte, registrar a revisão, reconciliar IDs e nomenclatura e fixar versões, comandos, opções do motor e semente de layout quando aplicável. |
| D05–D07 · manutenção | Identificar o modelo autoritativo e os derivados, registrar perdas por conversão e comparar o custo de criar e manter a vista após uma pequena mudança. |

<a id="glossario-visual"></a>

O modelo reúne elementos, responsabilidades e relações. A vista seleciona o que responde à pergunta de um público. Layout dispõe formas e conexões; renderizar produz a representação visual. Uma DSL descreve o domínio, a CLI é a interface de comando e o MCP dá acesso a ferramentas/contexto por servidor. C4 organiza contexto, contêineres, componentes e código. A fonte autoritativa rege a geração da vista. A ida e volta exige suporte específico para devolver alterações ao modelo.

## Como localizar os detalhes nas fontes

Na pasta `detalhes/` do ZIP corrigido v0, os limites abaixo vão da primeira âncora ou passagem até o fim real do último corpo no mesmo caderno. Unidades intercaladas podem pertencer a outras fichas. A matriz conserva os conjuntos exatos; a coluna de origem informa as unidades extremas como pontos de entrada. A última coluna explicita a relação com a regra desta página ou a função de uma passagem auxiliar.

| Seção na origem | Caderno dentro de `detalhes/` e limites inclusivos | Origens extremas | Contribuição ou função no destino |
|---|---|---|---|
| <a id="u061"></a> 1 Contexto e objetivo · F2 | 09-documentacao-visual/f2-01.md · L5–32 | F2-P023 · F2-P028 | F2 registra a necessidade de alternativas abertas para uso com Devin e o relato de dificuldade de leitura. Os arquivos, a instalação e o problema visual concreto precisam ser identificados. As funcionalidades, formatos e ambiente continuam em estudo. [Passagem integrada](#a09-002). |
| <a id="u062"></a> 2 Resultados pretendidos e princípios · F2 | 09-documentacao-visual/f2-02.md · L5–41 | F2-P029 · F2-P036 | Os princípios P01–P08 de F2 cobrem evidência, modelagem textual, identidade compartilhada, níveis de detalhe, separação entre código e arquitetura, inspeção visual, preservação dos originais e comparação antes da expansão. Versões e identificação da fonte das vistas são explicitações editoriais. [Passagem integrada](#catalogo-visual). |
| <a id="u063"></a> 3 Catálogo de necessidades e funcionalidades · F2 | 09-documentacao-visual/f2-03.md · L5–62 | F2-P037 · F2-T05R08 | As cinco necessidades N01–N05, as doze funcionalidades propostas F01–F12 e os sete detalhamentos editoriais D01–D07 estão distinguidos e recuperáveis na seção. Conservam a sua procedência e a finalidade de avaliação. [Passagem integrada](#catalogo-visual). |
| <a id="u064"></a> 4 Visões arquiteturais propostas · F2 | 09-documentacao-visual/f2-04.md · L5–29 | F2-P046 · F2-P050 | Cada uma das seis vistas responde a uma pergunta. Começar com a visão geral e navegar para o detalhe. O piloto seleciona três vistas com o mesmo objetivo de comparação. [Passagem integrada](#vistas). |
| <a id="u065"></a> 5 Catálogo das ferramentas · F2 | 09-documentacao-visual/f2-05.md · L5–253 | F2-P051 · F2-P113 | LikeC4 e Structurizr modelam; D2 comunica vistas estáticas; TALA, ELK e Dagre dispõem os elementos. CodeWiki fornece insumos se a instalação corresponder e Devin opera as ferramentas. Outras dependências citadas no catálogo incluem Playwright para exportar imagens e geradores DOT e PlantUML. Uma dependência não foi por isso avaliada como escolha autônoma. [Passagem integrada](#ferramentas). |
| <a id="u066"></a> 6 Processo proposto para uso com Devin · F2 | 09-documentacao-visual/f2-06.md · L5–59 | F2-P114 · F2-P126 | As oito etapas propostas vão da relação dos insumos até a escolha argumentada. No meio, produzir inventário candidato, reconciliar identidades, construir modelo, gerar vistas, registrar diagnósticos e confrontar fontes e apresentação. Cada resultado depende dos artefatos e direitos reais. [Passagem integrada](#a09-024). |
| <a id="u067"></a> 7 Fonte autoritativa e formatos derivados · F2 | 09-documentacao-visual/f2-07.md · L5–47 | F2-P127 · F2-P136 | Documentos e código sustentam interpretação; o modelo rege as vistas; fontes D2 derivadas exigem comandos e ajustes identificados; site/imagens precisam acompanhar a mudança; draw.io exportado conserva os resultados no alcance demonstrável. [Passagem integrada](#exportacao). |
| <a id="u068"></a> 9 Precisões técnicas incorporadas · F2 | 09-documentacao-visual/f2-09.md · L5–48 | F2-P148 · F2-P160 | Precisões da revisão F2: TALA acompanha D2 0.9.0; licenças/recursos de Structurizr variam por componente; Excalidraw oferece CLI; reparo por layout/normalização do Desktop é alternativa; conferir versão do Mermaid, motor/implementação e limites de conversão. [Passagem integrada](#ferramentas). |
| <a id="u069"></a> 11 Instrução de trabalho para Devin · F2 | 09-documentacao-visual/f2-11.md · L5–41 | F2-P170 · F2-P179 | O exemplo histórico do catálogo propõe análise, composição LikeC4/D2, relações sustentadas e três vistas antes de expandir. O complemento editorial acrescenta licenças, versões, perdas, comparação com o reparo e prova dos caminhos devolvidos. [Passagem integrada](#instrucao). |
| <a id="u070"></a> 13 Glossário · F2 | 09-documentacao-visual/f2-13.md · L5–21 | F2-P183 · F2-T14R11 | A distinção entre modelo, vista, layout, renderização, fonte autoritativa e ida e volta evita interpretar uma saída visual correta como prova de regeneração. DSL, CLI, MCP e C4 mantêm no catálogo os seus sentidos instrumentais. [Passagem integrada](#glossario-visual). |
