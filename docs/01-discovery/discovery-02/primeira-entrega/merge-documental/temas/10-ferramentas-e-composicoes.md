# Ferramentas candidatas por finalidade

Parta da operação que o engenheiro precisa concluir. A R04 define clientes-alvo e prevê avaliação posterior dos resultados por tarefa. F1–F4 acrescentam candidatos para obter evidência, recuperar conhecimento, representar a Solução e orquestrar trabalho. A presença de uma ferramenta no catálogo registra uma alternativa estudada. Uma adoção depende da decisão sobre aquela operação, edição, licença e modalidade. [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015).

<a id="abertura"></a>

<a id="a10-001"></a>

A escolha depende da pergunta. Encontrar um símbolo, determinar quais consumidores serão afetados, recuperar uma decisão histórica e diagramar a arquitetura exigem evidências e operações diferentes. A composição local proposta para a memória compartilhada, o piloto de documentação visual e os estudos de orquestração têm finalidades próprias. As capacidades, licenças e versões abaixo são as registradas nas quatro fontes. A matriz proposta distingue **documentado**, **adaptado**, **demonstrado no recorte**, **limitado**, **não avaliado** e **incompatível no recorte**. [Origem A10-001](#origem-a10-001).

<a id="inspecao"></a>
## Como obter evidência do código e produzir documentação

| Pergunta | Recursos estudados e fronteira da evidência |
|---|---|
| <a id="a10-002"></a> Onde aparece um nome, expressão ou padrão? | **ripgrep** estabelece a referência simples para texto. **Zoekt** (T14) oferece índice de trigramas, expressões regulares e busca booleana para muitos arquivos. **ast-grep** encontra padrões sintáticos e retorna arquivo, intervalo e linguagem. Uma ocorrência pode iniciar a investigação de comportamento. [Origem A10-002](#origem-a10-002). |
| <a id="a10-003"></a> Onde está a definição, quem a referencia e qual é o alcance da busca? | **Serena** (T12) usa LSP ou backend JetBrains. LSP depende de ambiente e linguagem; o backend JetBrains requer plugin, IDE e projeto configurado e indexado. A aplicação tem licença GPL-3.0-or-later, SolidLSP tem licença MIT e o plugin JetBrains tem oferta comercial. **SCIP** (T13) é um formato de índice que exige indexador e consumidor. Cobertura entre repositórios varia inclusive entre Java e Kotlin. [Origem A10-003](#origem-a10-003). |
| <a id="a10-004"></a> Como encontrar dependências e selecionar trechos? | **CodeGraphContext** consulta relações, algumas heurísticas. Identificar backend, repositório e conclusão do job volátil. **Aider Repo Map** (T11) ranqueia símbolos sob um orçamento de tokens e serve de referência de desenho. **GitNexus** tem sobreposição com CodeGraphContext; a licença informada é PolyForm Noncommercial 1.0.0, com licenciamento específico para uso comercial. **Repomix** prepara recortes; filtros, compressão e remoção de comentários alteram o material recebido. [Origem A10-004](#origem-a10-004). |
| <a id="a10-005"></a> Como gerar um primeiro mapa documental? | **CodeWiki** pode organizar hierarquias, páginas Markdown e diagramas. Em F1 há um breve teste relatado sem versão, configuração ou identidade verificável da instalação. Em F2, CodeWiki 2.0 é a origem informada para o acervo usado na visualização. A associação ao projeto MIT FSoft-AI4Code/CodeWiki precisa de confirmação antes de atribuir recursos ao ambiente do usuário. Quando presentes e alinhados à revisão, `module_tree.json`, `metadata.json`, `temp/dependency_graphs` e `temp/artifact_index.json` complementam o texto. O exemplo de US$ 0,34 contra US$ 21,48 em Svelte compara atualização incremental e geração integral no cenário publicado pelos autores. [Origem A10-005](#origem-a10-005). |

<a id="composicao"></a>
## Qual composição foi proposta para recuperar e compartilhar conhecimento

<a id="a10-006"></a>

A recomendação local registrada em F3 combina **Git/GitHub** (T01) para distribuir registros legíveis, **SQLite com FTS5 e consultas recursivas** (T02) para texto, metadados e relações, **sqlite-vec** (T03) para vetores, **FastEmbed** (T04) para executar um modelo e lógica própria para recuperar e validar. Outra máquina poderia reconstruir os índices derivados a partir da revisão publicada à qual tem acesso. O banco ativo ficaria local. O piloto precisa medir reconstrução, concorrência, volume, acesso, capacidade das máquinas e validade da resposta. A base Git já integra o projeto anterior; o formato e o destino desta memória, a sincronização e a seleção da stack permanecem em aberto. [Origem A10-006](#origem-a10-006).

<a id="a10-007"></a>

**sqlite-vec** é pré-v1 no material consultado. **FastEmbed** depende de modelos disponíveis e de suas licenças. O modelo candidato **paraphrase-multilingual-MiniLM-L12-v2** (T05) produz vetores de 384 dimensões. É preciso conferir a combinação de biblioteca e modelo, sua revisão, normalização e comportamento com português, inglês, siglas internas, identificadores, negações e exceções. **LanceDB Embedded** (T06, edição aberta Apache-2.0) é variante para texto, metadados e vetores no processo da aplicação, distinta da oferta Enterprise; manter também SQLite exigiria responsabilidade própria. [Origem A10-007](#origem-a10-007).

| Quando a carga ou a pergunta muda | Alternativas e limites técnicos |
|---|---|
| <a id="a10-008"></a> A recuperação exige serviço compartilhado | **Qdrant** (T07) combina vetores, filtros e busca híbrida. **PostgreSQL + pgvector** (T08) pode aproveitar infraestrutura relacional existente; filtros em índices aproximados podem diminuir o conjunto recuperado. Ambos exigem política explícita de autorização e atualização. [Origem A10-008](#origem-a10-008). |
| <a id="a10-009"></a> As relações já identificadas exigem percursos mais complexos | **NetworkX** (T10) permite prototipar algoritmos em memória. **Neo4j** (T09) oferece travessias especializadas, com operação e condições por edição. Começar com SQL recursivo é uma hipótese de menor complexidade. A validade de uma relação precisa de origem, alcance e revisão, qualquer que seja a base. [Origem A10-009](#origem-a10-009). |
| <a id="a10-010"></a> É necessário rotear ou ampliar uma consulta | **LlamaIndex**, núcleo MIT (T15), seleciona recuperadores e segue referências modeladas. **Haystack**, núcleo Apache-2.0 (T16), permite rotas condicionais e recuperação de um documento pai a partir de fragmentos numa hierarquia preparada. **GraphRAG**, núcleo MIT (T19), reúne modos Local, Global, DRIFT e Basic; BYOG pode importar entidades e relações externas. **LightRAG** é alternativa híbrida/incremental. Medir qualidade e custo em relação ao índice simples. [Origem A10-010](#origem-a10-010). |
| <a id="a10-011"></a> A atualização de índices torna-se dispendiosa | **CocoIndex** (T18) permite transformações incrementais. A documentação v1 citada usa LMDB. PostgreSQL era exigido na v0 e a oferta Plus tem opções próprias. Sua linhagem de computação ajuda a descobrir o que recalcular; dependências semânticas também precisam de avaliação. Núcleo Apache-2.0. [Origem A10-011](#origem-a10-011). |
| <a id="a10-012"></a> É preciso acompanhar relações no tempo e recordar descobertas | **Graphiti** (T20, núcleo Apache-2.0) modela temporalidade. A integração exige autenticação e autorização efetivas para cada consulta. A chave de agrupamento `group_id` não substitui esses controles. **Mem0** (T21, núcleo Apache-2.0) e **Cognee** foram estudados para memória persistente. Hospedagem interna do motor não implica modelos locais, aprovação do conteúdo ou substituição da base documental. [Origem A10-012](#origem-a10-012). |
| <a id="a10-013"></a> Precisa-se recuperar a origem de uma decisão ou acelerar uma repetição | **Entire CLI** (T22, MIT) associa sessões e checkpoints a commits. Configurações novas desde 0.10.0 usam `refs/entire/checkpoints/…`; instalações anteriores podem usar a branch `entire/checkpoints/v1`. **RedisVL SemanticCache** (T23) recupera prompts similares com filtros e TTL. A licença de RedisVL é MIT; para Redis 8 ou posterior as opções registradas são AGPLv3, RSALv2 e SSPLv1. TTL regula retenção, e similaridade pede verificação própria. **LiteLLM** (T24, núcleo MIT e componentes Enterprise distintos) oferece SDK e gateway e só alcança chamadas por rotas suportadas. Em loops e conversas, cache semântico pode devolver saída antiga. F3-P261–264 distingue o cache de uma chamada da recuperação de uma investigação entre repositórios. Evitar a chamada só pode contabilizar economia naquela rota. Para retomar conhecimento, o segundo cliente ainda precisa recuperar proveniência, revisão, condições, acesso e efeito da investigação. [Reuso de evidências](05-evidencias-e-memoria.md). [Origem A10-013](#origem-a10-013). |

<a id="operacao"></a>
## Como integrar clientes, acompanhar resultados e coordenar agentes

<a id="a10-014"></a>

**MCP, API e CLI** (T28) podem expor buscar memória, obter evidência, expandir dependências e verificar validade. **Devin Web/CLI/Desktop** (T29) e **Claude Code** (T30) são clientes-alvo da base anterior. Transporte, ferramentas, instalação, hooks, observabilidade, ambiente e permissões precisam de teste na modalidade efetiva. Em F2, a documentação citada para o Devin inclui STDIO, SSE e HTTP, o que sugere uma possibilidade técnica; a CLI é um caminho a experimentar sem aquela integração. Um servidor disponível não obriga o cliente a usá-lo. A [síntese funcional do guia de Devin](../../evidencias/DEVIN-FERRAMENTAS.md) documenta o recorte da experiência relatada. A disponibilidade presente de acesso precisa de verificação pelos profissionais autorizados. [Origem A10-014](#origem-a10-014).

<a id="a10-015"></a>

**OpenFGA** (T25, Apache-2.0) foi estudado para autorização por relações quando os controles existentes forem insuficientes; exige identidade, modelo e vínculos sincronizados. Não revoga cópias já clonadas. **OpenTelemetry** (T26) pode observar caminhos instrumentados; as convenções GenAI têm versões e o cliente fechado limita a visibilidade. **Arize Phoenix** (T27, ELv2 no núcleo citado) apoiaria traces e experimentos com referência revisada. A nota do avaliador não estabelece a correção do caso. [Origem A10-015](#origem-a10-015).

<a id="a10-016"></a>

Para **coordenação**, F4 propõe começar por capacidades nativas. A referência de Claude Code descreve subagentes aninhados, com até três camadas abaixo da conversa por padrão. Profundidade e concorrência são configuráveis, com particularidades de modalidade e execução em primeiro ou segundo plano. Agent Teams é recurso distinto e experimental no recorte, sem equipes aninhadas criadas pelos membros. A profundidade equivalente por modalidade de Devin continua sem demonstração. **Gas City** organiza *beads* persistentes e *formulas* em grafo para trabalhos prontos; **Magentic** escolhe quem atua em seguida e pode replanejar diante de estagnação; **CrewAI** e **Deep Agents** integram o conjunto de alternativas. **LangGraph** (T17) representa estado e transições; retomada usa *checkpointer*, compartilhamento entre execuções usa *store*. **Temporal** trata workflows duráveis, retries e esperas; **Ray** distribui tarefas/atores sob limites de recursos. Um scheduler externo dependeria de deficiência mensurável e de um responsável claro por tarefas, estado, cancelamento e efeitos em caso de falha. [Origem A10-016](#origem-a10-016).

<a id="a10-017"></a>

**OpenSpec**, **OpenHands SDK** e **Theia AI** foram estudados, respectivamente, para especificações, componentes programáveis de agentes e referência de IDE. **CodeQL**, **Pact**, **Testcontainers** e **JaCoCo** verificam aspectos distintos, com cobertura, ambiente e autorização próprios. F3 identifica preliminarmente quatro recursos. **RTK** foi estudado pela compactação de saídas de comandos, logs e testes. **Context-Mode** mantém saídas extensas pesquisáveis e devolve trechos; declara Elastic License 2.0. **Caveman** reduz respostas e saídas de ferramentas. A referência preliminar a **ai-memory** diz respeito à memória em Markdown versionada em Git, ao índice derivado e ao compartilhamento e recuperação entre agentes. Antes de atribuir economia, identificar o projeto, medir o percurso completo e verificar se filtros preservam a evidência e as exceções materiais. [Origem A10-017](#origem-a10-017).

<a id="ferramentas-visuais"></a>
## Qual ferramenta visual corresponde à entrega pretendida

<a id="a10-018"></a>

O usuário relatou documentação por repositório, consolidado e arquivos draw.io com problemas visuais. As causas concretas dependem de examinar exemplos. A proposta para o piloto combina **LikeC4** (MIT) como modelo navegável e **D2** (MPL-2.0) como complemento para vistas estáticas. LikeC4 valida, constrói site estático, gera fontes D2 e exporta vistas; o fluxo suportado de importação inversa de draw.io não foi identificado no material. Para preservar a edição e o trabalho anterior, testar também a reparação de cópias em **draw.io Desktop**. O editor jgraph/drawio é Apache-2.0 e o Desktop GPL v3. Ao exportar para draw.io, verificar em separado os nós e relações da saída e as regras de inclusão, exclusão e estilo necessárias para regenerá-la. O piloto visual conserva os originais. A escolha de ferramenta segue aberta e a camada da Solução já tem repositório próprio. [Documentação visual](09-documentacao-visual.md#exportacao) · [Autoridade de PE-08](01-visao-e-autoridade.md#pe08). [Origem A10-018](#origem-a10-018).

<a id="a10-019"></a>

Para estudar o efeito do motor de disposição, F2 sugere comparar **TALA**, **ELK** e **Dagre** sobre a mesma vista. Cada ensaio começa pelos motores pertinentes à pergunta. A comparação se amplia se persistir uma dúvida relevante. As fontes registram a abertura do TALA em 7 de setembro de 2026 sob MPL-2.0 e a inclusão em D2 0.9.0; mudanças pequenas podem alterar o layout e diagramas grandes custar mais. ELK.js é EPL-2.0, Dagre é MIT, e as opções `elk` e `dagre` do D2 citado correspondem a implementações nativas em Go. **Structurizr** (projeto consolidado Apache-2.0) é alternativa para C4 formal. O comando local aberto e o núcleo de servidor compilável têm capacidades diferentes dos binários oficiais do comando server, sujeitos a licença. [Origem A10-019](#origem-a10-019).

<a id="a10-020"></a>

**Mermaid** favorece fluxos e sequências junto ao Markdown. Sua CLI MIT exporta SVG, PNG e PDF; o comportamento de ELK depende do tipo e versão, inclusive a partir de 12.0.0. **Excalidraw** (MIT) atende composição livre e dispõe de CLI para renderizar e converter diversos diagramas Mermaid em formas editáveis. **Graphviz** (EPL-2.0) é opção exploratória para DOT e layout; **Cytoscape.js** (núcleo e extensões oficiais MIT) exigiria desenvolvimento para uma interface própria. O teste precisa confrontar o artefato renderizado com suas fontes e avaliar manutenção e perdas de conversão. [Origem A10-020](#origem-a10-020).

<a id="decisao"></a>
## O que justificaria uma escolha

<a id="a10-021"></a>

Comparar combinações mínimas sob a mesma tarefa, revisão, acesso e ambiente, com uma referência nativa competente. O desenho E0–E7 de F4 progride da busca básica para análise especializada, produção documental, recuperação determinística e semântica, delegação nativa, planejamento dirigido e execução externa candidata. A avaliação inclui precisão, cobertura, evidências reencontráveis, custo de produzir e manter o conhecimento, latência, acesso e qualidade da resposta. A bibliografia de F4 organiza fontes do projeto e de ferramentas por finalidade; os resultados publicados pelos autores e as licenças citadas mantêm o alcance dos estudos de origem. A compatibilidade demonstrada num cliente deve ser registrada com sua versão e condições. [Origem A10-021](#origem-a10-021).

## Como reencontrar as evidências

As notas numeradas estão no ZIP corrigido v0, em `rastreabilidade/temas/10.md`. Cada nota identifica as unidades usadas no bloco e seu índice de origem. A [consulta de origens](../consulta-origens.md) identifica as edições e permite partir de uma unidade. Os localizadores em tabelas incluem a linha do cabeçalho. A ligação a um bloco registra uso daquela passagem no texto.

<details>
<summary>Notas e antecedentes por passagem</summary>

| Passagem | Nota no ZIP v0 | Antecedente ou limite da comparação |
|---|---|---|
| <a id="origem-a10-001"></a> [A10-001](#a10-001) | `n1` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-002"></a> [A10-002](#a10-002) | `n2` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-003"></a> [A10-003](#a10-003) | `n3` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-047](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-047) |
| <a id="origem-a10-004"></a> [A10-004](#a10-004) | `n4` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-047](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-047) |
| <a id="origem-a10-005"></a> [A10-005](#a10-005) | `n5` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-047](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-047) |
| <a id="origem-a10-006"></a> [A10-006](#a10-006) | `n6` | [R04-DEC-003](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-003) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-024](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-024) |
| <a id="origem-a10-007"></a> [A10-007](#a10-007) | `n7` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-008"></a> [A10-008](#a10-008) | `n8` | [R04-DEC-001](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-001) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a10-009"></a> [A10-009](#a10-009) | `n9` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-047](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-047) |
| <a id="origem-a10-010"></a> [A10-010](#a10-010) | `n10` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-049](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-049) |
| <a id="origem-a10-011"></a> [A10-011](#a10-011) | `n11` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) |
| <a id="origem-a10-012"></a> [A10-012](#a10-012) | `n12` | [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a10-013"></a> [A10-013](#a10-013) | `n13` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-023](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-023) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a10-014"></a> [A10-014](#a10-014) | `n14` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-015"></a> [A10-015](#a10-015) | `n15` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a10-016"></a> [A10-016](#a10-016) | `n16` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a10-017"></a> [A10-017](#a10-017) | `n17` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-018"></a> [A10-018](#a10-018) | `n18` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-042](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-042) |
| <a id="origem-a10-019"></a> [A10-019](#a10-019) | `n19` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-020"></a> [A10-020](#a10-020) | `n20` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a10-021"></a> [A10-021](#a10-021) | `n21` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) |

</details>

<details>
<summary>Localizar as seções, tabelas e exemplos nos originais</summary>

Cada linha identifica o recorte titular. Os IDs das extremidades permitem abrir a composição exata da faixa no Repasse 2, em `indices-origem/faixas.csv` e `matriz.jsonl`. As linhas intermediárias seguem a seleção daquela ficha. Títulos delimitam a seção e casos, tabelas e registros preservam sua natureza original.

| Faixa | Da primeira à última unidade da ficha | O que procurar |
|---|---|---|
| <a id="faixa-u071"></a> U071 | `F3-P265 … F3-P289` | T25–T30 de F3 tratam de autorização por relações, observação instrumentada, experimentos com referência, interfaces e clientes. OpenFGA, OpenTelemetry, Phoenix, MCP/API/CLI, Devin e Claude Code exigem verificação da operação e da modalidade discutidas. |
| <a id="faixa-u072"></a> U072 | `F3-P290 … F3-P296` | Formatos, submódulos, hooks e mecanismos de navegação têm funções distintas. RTK, Context-Mode, Caveman e ai-memory são menções preliminares. As alegações de economia dependem de identificar projeto, revisão e resultado obtido. |
| <a id="faixa-u073"></a> U073 | `F3-P198 … F3-P222` | T09–T14 de F3 distinguem Neo4j, NetworkX, Repo Map, Serena, SCIP e Zoekt. A indexação, o backend de linguagem e o escopo de consultas entre repositórios delimitam a resposta. |
| <a id="faixa-u074"></a> U074 | `F3-P163 … F3-T11R11` | A tabela 11 de F3 distribui recursos por responsabilidade, desde versionar registros e recuperar informações até autorizar, observar e integrar clientes. A classificação não escolhe uma stack. |
| <a id="faixa-u075"></a> U075 | `F3-P244 … F3-P264` | T20–T24 de F3 tratam de temporalidade, memória operacional, captura por commit e cache. Examine separadamente Git, procedência, prazo, permissão e aplicabilidade. LiteLLM cobre as chamadas que usam suas rotas. |
| <a id="faixa-u076"></a> U076 | `F3-P165 … F3-P197` | T01–T08 de F3 distinguem distribuição em Git, recuperação textual e vetorial, modelo/língua, base embarcada e serviço compartilhado. A edição e a licença de cada componente acompanham a proposta. |
| <a id="faixa-u077"></a> U077 | `F3-P223 … F3-P234` | T15 e T16 descrevem roteamento e recuperação por LlamaIndex e Haystack sobre fontes e hierarquias preparadas. A faixa abre T17, sobre a coordenação por estado do LangGraph. |
| <a id="faixa-u078"></a> U078 | `F3-P235 … F3-P243` | A continuação de T17 distingue checkpointer e store. T18 discute processamento incremental com CocoIndex. T19 descreve modos de consulta de GraphRAG e o preparo de fontes, modelos e índices. |
| <a id="faixa-u079"></a> U079 | `F3-P297 … F3-P299` | A tabela 13 de F3 lista tecnologias e serviços mencionados no cenário. Diferencia cliente futuro, fonte de evidência e dependência específica. Sua presença não autoriza acesso ao ambiente nem os torna componentes escolhidos. |
| <a id="faixa-u080"></a> U080 | `F3-P160 … F3-P162` | F3 abre o catálogo T01–T30 e explica a seleção, as atribuições e as ressalvas. Esses números são internos a F3, independentes dos temas deste merge. |
| <a id="faixa-u081"></a> U081 | `F3-P300 … F3-P316` | O recorte de primeira versão em F3 inclui registro, recuperação, validade, investigação, sincronização, integração e observação. Composição embarcada e compartilhada são alternativas condicionadas a escala, direitos, reconstrução, concorrência e custo. |
| <a id="faixa-u082"></a> U082 | `F4-L2776 … F4-L2824` | F4 compara ferramentas de verificação e opções de coordenação multiagente. Explica separadamente Gas City e Magentic e delimita o que os estudos científicos citados permitem extrapolar. |
| <a id="faixa-u083"></a> U083 | `F4-L2826 … F4-L2881` | A regra de adoção começa pelas capacidades nativas verificáveis por cliente e modalidade. A seção situa as ferramentas pesquisadas antes do dossiê e as alternativas pertinentes ao problema posterior de replanejamento. |
| <a id="faixa-u084"></a> U084 | `F4-L2884 … F4-L2923` | F4 explica o risco de várias ferramentas disputarem a coordenação e propõe um catálogo lógico mínimo de capacidades de investigação. O exemplo descreve possibilidades e responsabilidades, sem prescrever sua implantação. |
| <a id="faixa-u085"></a> U085 | `F4-L2663 … F4-L2773` | F4 compara analisadores, geradores de documentação, recuperação, navegação e recursos auxiliares. Discute sobreposição de ferramentas, verificação sem modelo de linguagem, limites dos benchmarks de CodeWiki e controles de acesso em componentes candidatos. |

</details>
