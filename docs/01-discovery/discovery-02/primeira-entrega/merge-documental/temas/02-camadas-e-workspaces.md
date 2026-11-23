# Camadas, composição e ciclo do Workspace

<a id="a02-001"></a>

A Sigla identifica o pertencimento organizacional do Micro. A Solução descreve uma finalidade e relações funcionais. O Workspace registra a composição e o estado de uma atividade. Consultar um Micro de outra Sigla não altera o pertencimento nem o associa à atividade. Quando um vínculo muda, reexamine os consumidores que dependiam dele.

<a id="camadas"></a>

## Onde encontrar o conhecimento

| Camada | Responsabilidade e limites |
|---|---|
| <a id="a02-002"></a> Micro | Conhecimento do repositório individual no estado estudado. Identificar símbolos, contratos, configuração, comportamento, evidências, cobertura e incertezas. A forma como um consumidor trata uma resposta explica o lado observado do contrato. A seleção feita por um provedor externo exige evidência desse outro lado. |
| <a id="a02-003"></a> Meso | O repositório específico da Sigla/conta referencia Micros como submódulos. Encaminha perguntas por responsabilidade, revisão e dependência demonstrada. A entrega inicial do motor cobre o conjunto efetivamente estudado; o universo total de repositórios do domínio pode ser desconhecido. |
| <a id="a02-004"></a> Macro | O repositório Macro clonado é a raiz comum de distribuição e instalação. Referencia os Mesos como submódulos. Cada commit do Macro fixa os ponteiros dos Mesos, que por sua vez fixam os dos Micros. O catálogo distribui e localiza a origem responsável. Buscar uma entrada não exige centralizar cópias de todos os documentos, materializar todos os filhos ou conceder leitura privada. [DEC-003](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-003). |
| <a id="a02-005"></a> Workspace | Contexto persistente de uma atividade conduzida por time ou analista de uma Sigla. Composição, fontes, objetivos, pendências, hipóteses descartadas e motivos permitem continuar entre clientes e máquinas. A coincidência física entre repositório de Workspaces e Meso permanece em aberto (R04-RET-06). |
| <a id="a02-006"></a> Solução | A finalidade delimitada pelo Analista pode atravessar várias Siglas. A camada tem referência estável e repositório próprio. A composição identifica relações, entradas, resultados, componentes compartilhados, caminhos, variações, retornos e partes desconhecidas. Uma mudança de relação leva a examinar consumidores e dependências. |
| <a id="a02-007"></a> Negócios | Conecta políticas, produtos, conceitos, regras, públicos, temporalidade e exceções às jornadas, Soluções e consumidores técnicos. Uma declaração preserva autoria identificada, fundamento, alcance e divergências. A existência de um repositório de Solução não decide repositório nem governança de Negócios. |

<a id="a02-008"></a>

F4 propõe quatro planos lógicos de atuação, capacidades, controle e fundação persistente. Descrevem responsabilidades transversais às camadas de conhecimento. Discovery, refinamento e planejamento identificam momentos do ciclo. Um bloco desenhado pode representar papel ou responsabilidade sem exigir serviço, pasta ou agente próprio. O harness fornece contexto e controles adequados ao papel e à etapa.

<a id="camada-solucao"></a>

## Quem delimita uma Solução

O Analista delimita a finalidade e a abrangência da descoberta com auxílio do agente. Diante de evidência nova, manter o que é independente, revalidar a composição afetada e levar alteração de finalidade, fronteira ou comportamento acordado ao Analista. Distinguir estado estudado em branch, homologação e produção com evidência própria. Criar ou commitar a base não transforma uma pessoa em representante formal. [Autoridade em PE-08](01-visao-e-autoridade.md#pe08) · [DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040), [DEC-041](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-041), [DEC-042](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-042), [DEC-043](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-043), [DEC-044](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-044), [DEC-045](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-045).

<a id="workspace"></a>

## Como a atividade ganha ou perde componentes

<a id="a02-009"></a>

O engenheiro indica a Sigla do time ou analista executor. R06 descreve repositório de Workspaces por Sigla, branch por atividade, uma única pasta da atividade na raiz e área local de trabalho em `workspaces/`. O time que responde pelo repositório decide sua visibilidade. A branch própria não isola leitores. Uma feature pode participar de vários Workspaces; história, task, subtask ou bug pertence a um. [Workspace R06](../../evidencias/WORKSPACE-R06.md).

<a id="fronteira"></a>

<a id="a02-010"></a>

**Uma relação evidenciada, uma inclusão no Workspace e uma permissão de leitura são decisões distintas.** A linha 25 de D02-ESP na edição S2 tem o mesmo texto no espelho Git. Registrar origem, revisão pertinente quando conhecida, qual lado sustenta a relação e o que depende de investigar o outro. Para um repositório relacionado, o agente propõe a inclusão e apresenta justificativa, lacuna, direitos faltantes, limitações e o que ainda pode prosseguir. O engenheiro decide; o registro conserva a decisão. O vínculo de Sigla exige permissão do Analista e pode ser efetivado pelo agente. Outro Workspace pode ser consultado como histórico sob direitos legítimos. Cache ou consulta bem-sucedida não cria vínculo, direito sobre o outro lado ou autorização de escrever/refatorar. A S3 verificou o corpo Git, e a observação da edição nativa citada pertence a S2. [Adendo](../../../MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [R06](../../evidencias/WORKSPACE-R06.md) · [DEC-021](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-021), [DEC-025](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-025).

<a id="a02-011"></a>

O aceite do refinamento permite que a atividade avance. O encerramento requer decisão expressa do time. No fluxo futuro de R06, o time pode então escolher excluir a branch ou arquivar a pasta em main do repositório de Workspaces. A consulta posterior ao histórico depende dos direitos efetivos. Esta descrição funcional não dispara arquivamento nem exclusão. [Continuidade e saldos](13-decisoes-e-continuidade.md).

<a id="bootstrap"></a>

## Como obter somente a composição necessária

<a id="a02-012"></a>

Na jornada CLI, o engenheiro obtém a distribuição autorizada, inicia o cliente e pede onboarding, abre atividade ou formula pergunta avulsa. Cada cliente carrega as regras e os recursos reconhecidos naquela revisão. A retomada por outro cliente depende do que pôde ser versionado e recuperado. Web e Desktop exigem verificar shell, raiz, credenciais, hooks e ordem de carregamento próprios.

<a id="a02-013"></a>

F4 ilustra a área local com `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.devin/`, `contracts/`, `skills/`, `engines/`, `adapters/` e `workspaces/`. Uma convenção de nome requer verificação de suporte e precedência pelo cliente. Os nomes propostos `AGENTES.MD` e `PENDENCIAS.MD` para conhecimento futuro têm outra função. A presença de qualquer arquivo isolado não comprova aplicação da instrução.

<a id="a02-014"></a>

No exemplo ilustrativo de três Siglas e 165 repositórios, clonar e indexar tudo para responder a uma única pergunta misturaria sete condições: divulgação no catálogo, acesso real, conhecimento disponível, código materializado, revisão verificada, pertinência à tarefa e contexto entregue ao modelo. O primeiro uso diário de uma modalidade de IA tem regra própria e não impõe atualizar todos os MCPs, skills e submódulos.

<a id="a02-015"></a>

Resolva pelo commit do pai antes de comparar estados. Consultar uma referência remota, buscar objetos e atualizar uma árvore de trabalho são operações diferentes. Seguir o HEAD de cada filho pode produzir uma combinação que nunca esteve presente no pai. F4 propõe avaliar materialização por caminho, partial clone, sparse-checkout, cache e worktrees conforme custo, direitos e efeitos sobre trabalho local.

<a id="a02-016"></a>

O gerenciador proposto recebe finalidade, escopo, identidade e revisão. Descobre e inspeciona referências, resolve a composição, materializa o necessário, verifica a revisão e registra faltas e mudanças locais. Limpeza de temporários depende de direito de exclusão e de preservação de estado e evidências para retomada. As operações `discover`, `inspect`, `resolve`, `materialize`, `verify`, `refresh` e `release` ilustram um desenho sujeito a validação.


<a id="informacao"></a>

## Que registro pode sustentar a próxima ação

Uma fonte primária identifica o que se observou, em qual revisão e com que autoridade. No conhecimento canônico, a afirmação validada aponta sua origem e explicita alcance e ressalvas. Um índice textual, grafo ou vetor ajuda a encontrar esse conhecimento; é reconstruível, precisa identificar revisão e classificação de divulgação, e pode ter de ser invalidado na revogação. O estado de execução guarda hipótese, tarefa, saída e progresso. Incorporá-lo como novo conhecimento depende do ato autorizado. Até nomes de arquivos ou embeddings podem expor conteúdo privado. Cache operacional tem alcance e vida útil próprios.

Quatro planos propostos distribuem o trabalho entre atuação (papel, etapa, habilidades e contexto), capacidades (produzir, recuperar, materializar, testar e validar), controle (direitos, integridade, estados e auditoria) e fundação persistente (fontes, Git, índices e estado autorizado). A proposta admite outras implementações. Uma árvore hierárquica de objetivos pode alimentar um DAG com dependências entre tarefas; o plano não concede autoridade, não exige uma instância de agente por nó e não resolve atomicidade entre repositórios.

<a id="modalidades"></a>

### O que um adaptador precisa demonstrar

Na CLI local de Claude Code, conferir ordem de carga, regras por diretório, políticas gerenciadas, hooks, permissão, limite de subagentes e diferença entre aninhamento e Teams. Na CLI local de Devin, verificar herança de configuração, isolamento, concorrência e custo na revisão usada. Em Devin Web e Desktop verificar acesso real a raiz, shell, credenciais e atualização. O bootstrap proposto inicia o cliente, identifica versão e recursos por interface suportada, oferece catálogo seletivo, recebe a tarefa/etapa e só então compõe o contexto e o contrato de entrega. Sem ativação demonstrada naquela modalidade, preservar a limitação.

## Como localizar os detalhes nas fontes

Na pasta `detalhes/` do ZIP corrigido v0, os limites abaixo vão da primeira âncora ou passagem até o fim real do último corpo no mesmo caderno. Unidades intercaladas podem pertencer a outras fichas. A matriz conserva os conjuntos exatos; a coluna de origem informa as unidades extremas como pontos de entrada. A última coluna explicita a relação com a regra desta página ou a função de uma passagem auxiliar.

| Seção na origem | Caderno dentro de `detalhes/` e limites inclusivos | Origens extremas | Contribuição ou função no destino |
|---|---|---|---|
| <a id="t02-u013-01"></a> 07 Responsabilidades por camada · F3 | 02-camadas-e-workspaces/f3-07.md · L5–6 | F3-P126 | Identifica a tabela de F3 sobre responsabilidades das camadas e o alcance de contribuições que passam de uma para outra. [Passagem integrada](#camadas). |
| <a id="t02-u013-02"></a> 07 Responsabilidades por camada | 02-camadas-e-workspaces/f3-07.md · L8–35 | F3-T10R01 · F3-P131 | Micro contém o contexto de cada repositório. Meso seleciona Micros e dependências conhecidas; Macro encaminha à origem. Workspace reúne o estado persistente da atividade, Solução organiza o conhecimento entre repositórios e Negócios preserva finalidade e vigência. A entrada por uma camada não cria autoridade para publicar em outra. [Passagem integrada](#camadas). |
| <a id="t02-u014-01"></a> 2. Linha de base funcional e Workspace · F4 | 02-camadas-e-workspaces/f4-cap-02.md · L7–8 | F4-L351 | Título da seção da linha de base F4 sobre primeira entrega e atividades. [Passagem integrada](#workspace). |
| <a id="t02-u014-02"></a> 2. Linha de base funcional e Workspace | 02-camadas-e-workspaces/f4-cap-02.md · L10–19 | F4-L353 · F4-L358 | R06 separa consulta e vínculo ao Workspace. A visibilidade pertence ao repositório e o encerramento exige decisão expressa do time; são qualificações posteriores da base histórica. [Passagem integrada](#workspace). |
| <a id="t02-u014-03"></a> Linha de base do projeto: o que os registros consultados realmente dizem | 02-camadas-e-workspaces/f4-cap-02.md · L21–31 | F4-L360 · F4-L366 | F4 remete ao escopo de primeira entrega e à revisão de Workspace que consultou. Tratar o link de branch como localizador histórico; a regra corrente de composição e encerramento depende das decisões R04 identificadas nesta página. [Passagem integrada](#workspace). |
| <a id="t02-u014-04"></a> Nove frentes documentadas | 02-camadas-e-workspaces/f4-cap-02.md · L33–53 | F4-L368 · F4-L384 | PE-01..09 situam distribuição, modalidades, produtor Micro/Meso, evidência, atividade, atuação por etapa, extensões, Solução e Negócios. A dúvida histórica sobre criar a camada de Solução foi sucedida por DEC-042; o desenho do mecanismo de identidade continua pendente. [Passagem integrada](#camadas). |
| <a id="t02-u014-05"></a> Estado de Workspace já definido | 02-camadas-e-workspaces/f4-cap-02.md · L55–69 | F4-L386 · F4-L394 | R06 previa repositório de Workspaces por Sigla, branch por atividade e pasta única. R04 identifica quem decide visibilidade e término. Preservar a pergunta física Workspace/Meso sem convertê-la em indeterminação sobre o contexto funcional da atividade. [Passagem integrada](#workspace). |
| <a id="t02-u014-06"></a> Fronteira do primeiro recorte | 02-camadas-e-workspaces/f4-cap-02.md · L71–81 | F4-L396 · F4-L402 | Compreensão, refinamento, histórias e planejamento compõem o recorte inicial. A visão de execução, CI/CD e GMUD requer especificação e controles próprios. [Passagem integrada](#workspace). |
| <a id="t02-u014-07"></a> Requisitos que já possuem direção herdada e não devem ser “aprovados de novo” | 02-camadas-e-workspaces/f4-cap-02.md · L83–90 | F4-L404 · F4-L407 | Onboarding preserva o código. Comunicar cedo a lacuna; só o conhecimento do conjunto estudado compõe a entrega do produtor. Partir do contexto da atividade e solicitar inclusão quando ela se justificar. Uma consulta não formaliza a associação. [Passagem integrada](#fronteira). |
| <a id="t02-u015-01"></a> 3. Entidades, camadas e planos lógicos · F4 | 02-camadas-e-workspaces/f4-cap-03.md · L7–8 | F4-L410 | Cabeçalho de taxonomia de entidades, planos e momentos da engenharia em F4. [Passagem integrada](#a02-008). |
| <a id="t02-u015-02"></a> 3. Entidades, camadas e planos lógicos | 02-camadas-e-workspaces/f4-cap-03.md · L10–19 | F4-L412 · F4-L417 | F4 distingue escopos como Micro/Workspace, categorias de informação, planos operacionais e etapas da engenharia. As classificações se cruzam sem estabelecer hierarquia física entre elas. [Passagem integrada](#informacao). |
| <a id="t02-u015-03"></a> Entidades fundamentais e fronteiras de contexto | 02-camadas-e-workspaces/f4-cap-03.md · L21–52 | F4-L419 · F4-L440 | A linha de base preserva fronteira organizacional, finalidade da atividade e relações funcionais por objetos diferentes. Aplicar a sucessão da raiz e do repositório da Solução no seu objeto; Negócios e Workspace/Meso têm saldos próprios. [Passagem integrada](#camadas). |
| <a id="t02-u015-04"></a> Separar quatro camadas de informação | 02-camadas-e-workspaces/f4-cap-03.md · L54–73 | F4-L442 · F4-L455 | Fonte primária, conhecimento canônico, índice derivado e estado de execução têm autoridades, validade e direitos diversos. Recriar um índice ou recuperar uma sessão não aprova o conhecimento que seus registros citam. [Passagem integrada](#informacao). |
| <a id="t02-u015-05"></a> Planos operacionais lógicos — [PROPOSTA] | 02-camadas-e-workspaces/f4-cap-03.md · L75–90 | F4-L457 · F4-L468 | Quatro planos propostos separam papel e contexto; serviços de compreensão, recuperação e validação; autorização, integridade e auditoria; fontes, Git, índices reconstruíveis e estado persistente. O runtime externo limita o controle da plataforma. [Passagem integrada](#informacao). |
| <a id="t02-u015-06"></a> Ciclo de engenharia — uma terceira dimensão | 02-camadas-e-workspaces/f4-cap-03.md · L92–99 | F4-L470 · F4-L473 | Discovery, refinamento, histórias e aceites, planejamento técnico e de testes, implementação, revisão, PR, CI/CD, homologação e GMUD identificam momentos do trabalho. Deles não se infere um repositório, executor ou permissão por etapa. [Passagem integrada](#a02-008). |
| <a id="t02-u016-01"></a> 5. Jornada do engenheiro, bootstrap e modalidades · F4 | 02-camadas-e-workspaces/f4-cap-05.md · L7–8 | F4-L599 | Cabeçalho de F4 que reúne jornada do usuário, invocação e diferenças de modalidade. [Passagem integrada](#bootstrap). |
| <a id="t02-u016-02"></a> 5. Jornada do engenheiro, bootstrap e modalidades | 02-camadas-e-workspaces/f4-cap-05.md · L10–19 | F4-L601 · F4-L606 | O cliente externo lê apenas interfaces suportadas; a plataforma expõe recursos e registra destinos autorizados. Verificar por modalidade carregamento, delegação e controle. [Passagem integrada](#a02-012). |
| <a id="t02-u016-03"></a> Jornada de referência | 02-camadas-e-workspaces/f4-cap-05.md · L21–36 | F4-L608 · F4-L621 | A jornada proposta passa por obter a raiz, abrir o terminal, iniciar o cliente, carregar instruções suportadas, formular a tarefa, consultar contexto/motores, registrar evidências em destinos autorizados e retomar por conhecimento versionado. [Passagem integrada](#a02-012). |
| <a id="t02-u016-04"></a> A fronteira que importa | 02-camadas-e-workspaces/f4-cap-05.md · L38–53 | F4-L623 · F4-L634 | O agente interpreta a intenção em seu runtime; a plataforma oferece capacidades verificadas; o adaptador traduz o contrato para a modalidade; a autoridade corporativa concede direitos sobre o destino. Presença de um arquivo não prova aplicação. [Passagem integrada](#modalidades). |
| <a id="t02-u016-05"></a> Matriz de capacidades por agente, modalidade e versão | 02-camadas-e-workspaces/f4-cap-05.md · L55–91 | F4-L636 · F4-L658 | Comparar ordem de carga, regras por diretório, skills, MCPs, hooks, políticas, aninhamento, concorrência e recuperação na versão real de cada cliente. Recurso documentado em Claude Code, Devin CLI ou Teams não comprova equivalência entre modalidades. [Passagem integrada](#modalidades). |
| <a id="t02-u016-06"></a> Possível organização física e bootstrap (estritamente ilustrativos) | 02-camadas-e-workspaces/f4-cap-05.md · L93–136 | F4-L660 · F4-L695 | A árvore ilustrativa local distingue entradas de cliente, adaptadores, contratos e Workspaces. Suporte, precedência e comportamento dependem de cada cliente; o layout de F4 não congela P03.22 nem define o repositório remoto de Workspaces. [Passagem integrada](#a02-013). |
| <a id="t02-u016-07"></a> Bootstrap comportamental candidato | 02-camadas-e-workspaces/f4-cap-05.md · L138–152 | F4-L697 · F4-L707 | O bootstrap candidato identifica versão e contexto, oferece catálogo seletivo e aplica o contrato da tarefa com direitos efetivos. Provar ativação por modalidade; sem mecanismo confiável, tratar a capacidade como desejada. [Passagem integrada](#modalidades). |
| <a id="t02-u017-01"></a> 10. Catálogo, materialização seletiva e topologia Git · F4 | 02-camadas-e-workspaces/f4-cap-10.md · L7–8 | F4-L1234 | Título do capítulo de catálogo, materialização e composição Git. [Passagem integrada](#bootstrap). |
| <a id="t02-u017-02"></a> 10. Catálogo, materialização seletiva e topologia Git | 02-camadas-e-workspaces/f4-cap-10.md · L10–19 | F4-L1236 · F4-L1241 | A escala do catálogo requer identificação divulgável e seleção por objetivo; cada condição tem sua evidência. Falta de acesso não invalida o trabalho independente. [Passagem integrada](#a02-014). |
| <a id="t02-u017-03"></a> Cenário e preocupação — [MANIFESTAÇÃO NOVA] | 02-camadas-e-workspaces/f4-cap-10.md · L21–35 | F4-L1243 · F4-L1251 | O caso de três Siglas e 165 repositórios ilustra cardinalidade elevada e acesso parcial. O requisito é comportar variação de escala, sem prometer aquele número como capacidade medida. [Passagem integrada](#a02-014). |
| <a id="t02-u017-04"></a> Separação operacional obrigatória — [PROPOSTA] | 02-camadas-e-workspaces/f4-cap-10.md · L37–59 | F4-L1253 · F4-L1269 | Catálogo, acesso, conhecimento disponível, código materializado, revisão verificada, pertinência e contexto entregue têm efeitos diferentes. Leitura não inclui retenção e escrita. Branch local ou conteúdo presente não confirma homologação, árvore limpa ou análise concluída. [Passagem integrada](#a02-014). |
| <a id="t02-u017-05"></a> Inicialização leve e carregamento progressivo — preservar PE-01 | 02-camadas-e-workspaces/f4-cap-10.md · L61–75 | F4-L1271 · F4-L1279 | Ao abrir a atividade, obter dependências pertinentes com as credenciais do engenheiro, apresentar faltas e permitir aprofundamento. Descoberta leve e obtenção seletiva são propostas para evitar atualização indiscriminada. [Passagem integrada](#a02-014). |
| <a id="t02-u017-06"></a> Submódulos não equivalem a checkout de tudo | 02-camadas-e-workspaces/f4-cap-10.md · L77–94 | F4-L1281 · F4-L1294 | O ponteiro no pai fixa a composição. Comparar referência remota, obter objetos e alterar a árvore são atos distintos: identificar avanço não demonstra impacto semântico, implantação ou autorização para alterar trabalho local. [Passagem integrada](#a02-015). |
| <a id="t02-u017-07"></a> Capacidade candidata: Gerenciador de Materialização e Revisões | 02-camadas-e-workspaces/f4-cap-10.md · L96–119 | F4-L1296 · F4-L1313 | Descobrir, inspecionar, resolver composição e materializar são operações ilustrativas. Antes de baixar/indexar, verificar direito; ao falhar, registrar revisões, alcance e próximo passo. Atualizar projeções afetadas; limpar somente temporários legitimamente descartáveis. [Passagem integrada](#a02-016). |
| <a id="t02-u017-08"></a> Caches e índices | 02-camadas-e-workspaces/f4-cap-10.md · L121–128 | F4-L1315 · F4-L1318 | Separar catálogo divulgável, Git canônico, índice reconstruível, material da atividade e cache com ACL e vida útil. Nomes de arquivos ou embeddings podem expor informação privada. Conservar classificação de divulgação e revisão no índice. [Passagem integrada](#informacao). |
| <a id="t02-u018-01"></a> Glossário e mapa de responsabilidades · F4 | 02-camadas-e-workspaces/f4-glossario-e-mapa-de-resp.md · L7–8 | F4-L4009 | Título do glossário de conceitos da edição F4. Os termos são de leitura e carecem de contrato próprio para formar capacidade operacional. [Passagem integrada](#informacao). |
| <a id="t02-u018-02"></a> Glossário e mapa de responsabilidades | 02-camadas-e-workspaces/f4-glossario-e-mapa-de-resp.md · L10–51 | F4-L4011 · F4-L4047 | Reconstrução de estado por eventos, continuidade após falha e auditoria têm finalidades diferentes. HTN decompõe objetivos; DAG organiza dependências. Um papel descreve uma responsabilidade e pode ser assumido por executores distintos. Ler o glossário histórico de raiz/Solução com as decisões posteriores da R04. [Passagem integrada](#informacao). |
| <a id="t02-u018-03"></a> Como localizar requisitos, pendências e validações | 02-camadas-e-workspaces/f4-glossario-e-mapa-de-resp.md · L53–55 | F4-L4049 | A rota F4 parte do mapa lógico e dos nove contratos, cruza requisitos AD-EA com cenários CT-AD, PoCs e questões DISC-EA/QD-AD. Um destino PE ou P03/P04 indicado no índice é sugestão de encaixe, sujeita à decisão competente. [Passagem integrada](#a02-008). |
