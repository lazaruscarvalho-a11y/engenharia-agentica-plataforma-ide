# Decisões, perguntas em aberto e continuidade

<a id="a13-001"></a>

As agendas de onboarding (F1), documentação visual (F2), memória (F3) e núcleo de engenharia (F4) usam identificadores e critérios próprios. Aqui, as perguntas permanecem junto do efeito que teriam na decisão ou da evidência que falta. Uma decisão posterior prevalece na dimensão que ela resolveu. As questões restantes podem ser retomadas por tema, conforme a necessidade do engenheiro.

<a id="retomada"></a>

## De que revisão partir

<a id="a13-002"></a>

F4 registrava P04.1 como retomada histórica e propunha antecipar insumos para P03.22, P03.20 e PE-06/07. Os sete blobs identificavam arquivos, e o PR aberto descrevia aquele momento. A sugestão de estudo não altera a ordem do discovery.

<a id="a13-003"></a>

Na branch D02 (`8bbd93151640865995fa8a8dfe3d2d5db15da6ec`), D02-PEN-001/002 tratam de suficiência e apresentação. Para a base desta edição (`1082b9640ef70f311362ffc2d33b60c488dadc1b`), a rota R04 conserva a D02 histórica e consolida as 77 perguntas de P01–P09. P04 encerrou-se no alcance documentado; P04.1–5 conservam o limite de proveniência original. P01.4, P03.20/P03.22, P05.5, P06.6 e P09.4 têm adiamentos expressos. Recuperar a decisão e o refinamento do objeto escolhido evita repetir a entrevista. [Saldo P01–P09](../../consolidacao-r04/SALDO-P01-P09.md) · [Refinamentos postergados](../../consolidacao-r04/REFINAMENTOS-POSTERGADOS.md) · [Continuidade R04](../../consolidacao-r04/CONTINUIDADE.md).

<a id="sucessoes"></a>

## O que já foi respondido e o que ainda depende de escolha

<a id="a13-004"></a>

**Raiz, Macro e Workspace.** DEC-003 reúne a raiz comum, a instalação local e o Macro no mesmo repositório Git. Os submódulos conservam a composição escolhida. O repositório de Workspaces organiza contexto e relações de atividades e permite retomada noutra máquina. Continua aberta a identidade física Workspace/Meso, assim como o destino físico de Negócios. O adendo D02-ESP r1 ainda indagava sobre estado, lugar de trabalho e seleção de Sigla. R06 e DEC-020–024 responderam a essas partes; DEC-006/007 delimitam autenticação e envio pelo Git. O mecanismo de acesso a histórico e os detalhes de implementação conservam saldo próprio. [Camadas e fronteiras](02-camadas-e-workspaces.md#fronteira).

<a id="identidade-solucao"></a>

<a id="a13-005"></a>

**Solução e Negócios.** No PE-08, a Solução possui referência estável, identidade e repositório próprio para descoberta e reutilização. A alternativa “somente evidências ou mapa?” pertence a F4 e à discussão A020. U021 e RET-08 esclarecem o compromisso posterior. Durante a descoberta, mapas candidatos e evidências podem preceder a delimitação pelo Analista com ajuda do agente. Quem criou ou alterou a base não representa formalmente a Solução. **Que identificadores, critérios de duplicidade e regra de evolução permitem decidir se uma descoberta pertence à Solução existente?** Essa é a parcela aberta de R04-PEN-042. Negócios tem perguntas próprias sobre origem, competência e destino físico. [Trilha de PE-08](01-visao-e-autoridade.md#pe08) · [DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040), [DEC-041](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-041), [DEC-042](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-042), [DEC-045](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-045).

<a id="a13-006"></a>

**Validade e publicação.** Detectar drift implica suspender o uso das afirmações afetadas como atuais e revalidá-las antes de restaurar a validade. A direção pede verificação determinística do conteúdo exato antes de cada push. Mudança no candidato invalida as provas dependentes. Ainda é preciso definir o mecanismo e demonstrar quais caminhos cobre. Um hook isolado não comprova cobertura universal; um commit não demonstra implantação.

<a id="a13-007"></a>

**Fontes e derivados.** A base distingue leitura ordinária já autorizada, armazenamento, indexação, retenção, publicação e redistribuição. R04 não institui temporizador próprio para as autorizações. Dados ou metadados de projeto privado dependem de direito real, inclusive em cache. Revogação na origem pode interromper novo acesso, mas não recolhe automaticamente clones já distribuídos. [Validade e acesso](07-validade-acesso-e-publicacao.md).

<a id="autoridade"></a>

## Que decisão precisa de uma pessoa

<a id="a13-008"></a>

**Compreensão suficiente e apresentação.** D02-PEN-001/002, ONB-PEN-03/04 e Q07 convergem na pergunta: que evidência permite encerrar a produção com ressalva e como o engenheiro reconhece a conclusão insegura? A definição de pronto já separa produção de interação futura. Demonstrar comportamento sustentado, premissa que falta, efeito e próxima intervenção. Se a lacuna só atinge uma parte, preservar a parte sustentada. Orçamento esgotado, uma lacuna nomeada ou o êxito de uma consulta futura isolada não definem suficiência. A forma de apresentação continua aberta. [Onboarding](03-onboarding-e-compreensao.md).

<a id="a13-009"></a>

**Qualidade.** F1 registra a direção forte de preservar qualidade, profundidade, precisão, performance e eficiência. F4 propõe avaliar benefício sem piora significativa. A passagem não aprova uma tolerância de degradação. Para cada classe de tarefa, esclarecer quais propriedades são indispensáveis e que compensações a pessoa competente admite; custo médio menor pode ocultar queda em uma classe crítica.

<a id="a13-010"></a>

**Competência fora de atividade.** Qualquer pessoa pode esclarecer. Incorporar nova compreensão, com finalidade, entendimento, origem, destino e efeito identificados, depende de competência sobre aquele objeto. No protocolo de conhecimento, S1 é correção inequívoca autorizada, S2 é novo entendimento e S3 é conflito. Sem Workspace e sem Analista da atividade identificado, manter a contribuição candidata e o conflito registrado. Silêncio preserva a pendência. Negativa impede aquela escrita. Quem pode autorizar para esse público e destino? [QD-AD-31](#qd-ad-31) · [ED-LAC-02](#ed-lac-02).

<a id="a13-011"></a>

**Procedimento entre repositórios.** Se um serviço consumidor depende de outro para preparar dados sintéticos, o procedimento interno de cada um pode ter fonte no próprio Micro. Quem responde pela instrução transversal, para qual público e onde ela pode ser consultada? Registrar ambiente, finalidade, pré-requisitos, limites e referências permitidas. Vínculo funcional não estende a autorização de leitura. O caso detalhado permanece na origem identificada por QD-AD-04.

<a id="a13-012"></a>

**Coordenação.** Quais papéis e operações atendem o primeiro recorte e, se houver despacho externo, quem mantém o estado da tarefa? Devin Web/CLI/Desktop e Claude Code são os clientes previstos, e Copilot permanece possibilidade posterior. Abertura de CLI ou plano hierárquico não demonstram pausa, cancelamento ou retomada. Execução de CI/CD e GMUD depende de autoridade e especificação próprias. [Papéis e delegação](08-papeis-e-delegacao.md).

<a id="a13-013"></a>

**Documentação visual.** Quem precisa consultar ou editar o resultado e qual formato atende à tarefa? A manutenção do modelo autoritativo e dos ajustes de layout pede responsável competente, sem atribuição automática a quem criou a Solução. O piloto de três vistas e o reparo de um draw.io existente são propostas comparativas. [Exportação e regeneração](09-documentacao-visual.md#exportacao).

<a id="evidencias"></a>

## O que exige levantamento ou ensaio

<a id="a13-014"></a>

**Compatibilidade.** Identificar operação, configuração, versão e modalidade; observar retornos, efeitos, falhas e limites. Capacidade de aninhar agentes em determinada oferta de Claude não prova a mesma profundidade em Devin, Agent Teams ou outra configuração. ONB-PEN-05–09, Q09 e ED-LAC-03 remetem a contratos, extensões, artefatos e precedência.

<a id="a13-015"></a>

**Comparação.** ONB-PEN-10–14 e Q11–13 exigem amostras adequadas, mesma tarefa, condições frias/aquecidas, falha, retomada, versão, licenças e instrumentação. Na fundação usam-se dados sintéticos. O catálogo visual propõe um piloto posterior com materiais reais, sob direitos pertinentes. DISC-EA-26 pergunta quem autoriza e revalida licenças de componentes, dependências transitivas e extensões. Ter um manifesto ajuda a identificar o objeto, mas não atribui autoridade sobre redistribuição. [Avaliação](12-avaliacao-riscos-e-provas.md).

<a id="a13-016"></a>

**Memória.** Antes de definir granularidade, índice local ou compartilhado, embeddings, grafo e limiares, conhecer os destinos legítimos, composição Git, alterações locais, concorrência e perguntas materiais. Negação, exceções e condições em português exigem ensaio próprio. Um registro similar só permite reutilizar as afirmações cuja evidência se mantém aplicável. [Memória](05-evidencias-e-memoria.md).

<a id="a13-017"></a>

**Regra externa.** O código do consumidor pode comprovar tratamento de uma resposta sem revelar a política que a selecionou. Conferir versões e ambiente da regra, se houver direito de consultar. No caso de motor de regras, documento, RuleApp, ruleset, log, simulação e execução com efeitos constituem fontes ou operações distintas. Preservar a conclusão sobre o lado observável; declarar dependência externa e efeito na suficiência.

<a id="a13-018"></a>

**Diagrama.** Um caso de dificuldade visual pede pergunta, revisão das relações, meio de leitura e evidência do problema. Só exigir versão CodeWiki/Devin ou desenho anterior quando a comparação selecionada depender deles. Visão consolidada, de repositório e de integração são três propostas de teste, sem resultado registrado.

<a id="agendas"></a>

## Como usar as agendas originais

<a id="a13-019"></a>

As 101 entradas abaixo conservam as seis famílias de origem. F2 usa VIS como localizador editorial. Os ED-LAC registram tensões, classificações históricas ou lacunas de evidência. O enunciado pertence à edição original, e uma resposta posterior se aplica somente à parcela indicada. D02-PEN-001/002 são referências correlatas, não duas linhas adicionais ou gates desta entrevista.

<a id="a13-020"></a>

Os dois prompts históricos de F4 e o checklist do adendo reúnem destinatário, limites e nove episódios POS. Servem para recuperar o motivo das perguntas. Em uma nova atividade, confirmar a revisão e formular a pergunta do recorte pertinente. A sugestão de F1 é explicitar o resultado a preservar, a evidência necessária, o contrato e um cenário sintético.

### Onboarding · F1

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="onb-pen-01"></a> ONB-PEN-01 | O que contará como preservação de qualidade em cada atividade? | Resultados esperados, condições críticas e forma de demonstrar sustentação. | DEC-015 · F1-T22R02 |
| <a id="onb-pen-02"></a> ONB-PEN-02 | Como operacionalizar a intenção de não prejuízo? | Decisão explícita sobre critérios de não regressão, dimensões sem compensação e eventual tolerância. | DEC-015 · F1-T22R03 |
| <a id="onb-pen-03"></a> ONB-PEN-03 | O que diferencia compreensão suficiente de lacuna insegura? | Critérios por comportamento e dependência, vinculados ao DoD e às perguntas D02 pertinentes. | DEC-014, DEC-018 · F1-T22R04 |
| <a id="onb-pen-04"></a> ONB-PEN-04 | Como mostrar cobertura, limites e próximos passos? | Refinamento de UX compatível com clientes da primeira entrega e com o papel do engenheiro. | DEC-018, DEC-039 · F1-T22R05 |
| <a id="onb-pen-05"></a> ONB-PEN-05 | Qual será o contrato comum e quais extensões permanecerão específicas? | Casos de uso, campos, identidade, erros, efeitos e preservação dos recursos especializados. | DEC-009, DEC-035 · F1-T23R02 |
| <a id="onb-pen-06"></a> ONB-PEN-06 | Como demonstrar compatibilidade por agente e modalidade? | Matriz de operações e ambientes, estados, versões observáveis e cenários verificáveis. | DEC-009, DEC-010 · F1-T23R03 |
| <a id="onb-pen-07"></a> ONB-PEN-07 | Qual conjunto mínimo de ferramentas acrescenta valor? | Comparação de capacidades, sobreposição, qualidade, custo e manutenção; sem obrigar todas. | DEC-015 · F1-T23R04 |
| <a id="onb-pen-08"></a> ONB-PEN-08 | Como conservar e disponibilizar artefatos nativos? | Direitos, destinos, referências, expiração, compartilhamento de arquivos e reconstrução. | DEC-035, DEC-052 · F1-T23R05 |
| <a id="onb-pen-09"></a> ONB-PEN-09 | Como conciliar hooks skills e instruções? | Cobertura real, precedência, custo, ativação e tratamento das diferenças de cliente. | DEC-037 · F1-T23R06 |
| <a id="onb-pen-10"></a> ONB-PEN-10 | Qual conjunto sintético representará os casos iniciais? | Diversidade necessária, regras conhecidas, exceções, limitações e critérios de cobertura. | DEC-014, DEC-018 · F1-T24R02 |
| <a id="onb-pen-11"></a> ONB-PEN-11 | Como comparar qualidade e custo de forma justa? | Referência nativa, repetições, condições frias e aquecidas, métricas e interpretação. | DEC-015 · F1-T24R03 |
| <a id="onb-pen-12"></a> ONB-PEN-12 | Como tratar falhas retomada e substituição? | Contratos por operação, efeitos repetíveis, dependências, cancelamento e estados incertos. | DEC-013, DEC-023 · F1-T24R04 |
| <a id="onb-pen-13"></a> ONB-PEN-13 | Como revalidar mudanças em ferramentas e configurações? | Vínculo entre revisão, comportamento, derivados e evidência, inclusive a exigência pré-push da base. | DEC-038 · F1-T24R05 |
| <a id="onb-pen-14"></a> ONB-PEN-14 | Quais versões licenças e destinos são admissíveis? | Componentes concretos, termos aplicáveis, direitos e controles corporativos pertinentes. | DEC-035, DEC-052 · F1-T24R06 |

### Documentação visual · F2

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="vis-01"></a> VIS-01 | Projeto e versão do CodeWiki efetivamente utilizado. | Quais artefatos e integrações podem ser reaproveitados. | DEC-035 · F2-T12R02 |
| <a id="vis-02"></a> VIS-02 | Documentação consolidada, páginas por repositório e arquivos draw.io. | Escopo da extração e do piloto. | DEC-035, DEC-052 · F2-T12R03 |
| <a id="vis-03"></a> VIS-03 | Exemplos concretos e contexto em que os diagramas serão lidos. | Ajustes, formato e motor mais adequados. | DEC-040 · F2-T12R04 |
| <a id="vis-04"></a> VIS-04 | Dependências disponíveis e forma de acesso aos arquivos. | Fluxo executável por CLI e eventual MCP. | DEC-009, DEC-010 · F2-T12R05 |
| <a id="vis-05"></a> VIS-05 | Acesso ao código, revisão e evidências de integrações. | Grau de confirmação das relações modeladas. | DEC-040, DEC-047, DEC-052 · F2-T12R06 |
| <a id="vis-06"></a> VIS-06 | Necessidade de site, SVG, PDF ou edição em draw.io. | Formatos e verificação de exportação. | DEC-040 · F2-T12R07 |
| <a id="vis-07"></a> VIS-07 | Divisão por domínio, sistema, repositório ou projeto. | Identidades e responsabilidade pelas definições. | DEC-041, DEC-042 · F2-T12R08 |
| <a id="vis-08"></a> VIS-08 | Quem atualizará o modelo e como tratará ajustes manuais. | Fonte autoritativa e procedimento de regeneração. | DEC-044, DEC-045 · F2-T12R09 |

### Memória e investigação · F3

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="q01"></a> Q01 | Destino e granularidade dos registros de memória. | Público, origem principal, relações entre camadas e fluxo S1 a S3. | DEC-016, DEC-049 · F3-T19R02 |
| <a id="q02"></a> Q02 | Esquema, identidade e estados do registro. | Casos reais de resposta, contradição, revalidação e compatibilidade. | DEC-016, DEC-049 · F3-T19R03 |
| <a id="q03"></a> Q03 | Sincronização Git e reconstrução dos índices. | Composição adotada, submódulos, referências especiais e mudanças locais. | DEC-003, DEC-024 · F3-T19R04 |
| <a id="q04"></a> Q04 | Índice local, serviço compartilhado ou combinação. | Volume, máquinas, concorrência, conectividade e custo de manutenção. | DEC-015, DEC-024 · F3-T19R05 |
| <a id="q05"></a> Q05 | Modelo de embeddings e busca híbrida. | Testes em português, código, siglas, negação e condições de negócio. | DEC-015 · F3-T19R06 |
| <a id="q06"></a> Q06 | Relações iniciais e cobertura do grafo. | Fontes de cada relação, indexadores disponíveis e casos de impacto. | DEC-040, DEC-041 · F3-T19R07 |
| <a id="q07"></a> Q07 | Política de expansão e suficiência. | Tipos de tarefa, evidências obrigatórias, exceções e criticidade. | DEC-014, DEC-050 · F3-T19R08 |
| <a id="q08"></a> Q08 | Orçamento e limiares de reutilização. | Qualidade, latência e custo em cenários representativos. | DEC-015 · F3-T19R09 |
| <a id="q09"></a> Q09 | Integração por cliente e modalidade. | Provas de configuração, execução, acesso, persistência e retomada. | DEC-009, DEC-010 · F3-T19R10 |
| <a id="q10"></a> Q10 | Autorizações de serviço e conteúdo derivado. | Controles existentes, identidade e circulação legítima entre destinos. | DEC-001, DEC-002, DEC-052 · F3-T19R11 |
| <a id="q11"></a> Q11 | Instrumentação e avaliação. | Dados disponíveis, minimização de conteúdo sensível e critérios revisados. | DEC-014, DEC-015 · F3-T19R12 |
| <a id="q12"></a> Q12 | Versões, edições e licenças da stack. | Componentes efetivamente distribuídos e termos aplicáveis. | DEC-035 · F3-T19R13 |
| <a id="q13"></a> Q13 | Garantia determinística anterior a cada push. | Mecanismo que vincula a prova ao candidato exato, cobre conhecimento e referências afetados e detecta mudanças posteriores. | Direção para prova determinística pré-push existente. Falta demonstrar cobertura dos mecanismos e vinculação aos bytes candidatos. DEC-038, DEC-044 · F3-T19R14 |
| <a id="q14"></a> Q14 | Forma física de Workspace e Negócios. | Refinamento das escolhas explicitamente mantidas em aberto na base. | Macro/raiz não responde à identidade física Workspace/Meso nem decide repositório de Negócios. DEC-003, DEC-024, DEC-049 · F3-T19R15 |

### Primeira entrega · F4

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="disc-ea-01"></a> DISC-EA-01 | Qual é a unidade mínima canônica de conhecimento: página, afirmação, comportamento, entidade, evento ou combinação? | P03.22 | DEC-016, DEC-049 · F4-L3532 |
| <a id="disc-ea-02"></a> DISC-EA-02 | Como atribuir IDs estáveis e relações tipadas sem duplicar a autoridade da fonte? | P03.22 / P04 | DEC-041, DEC-049 · F4-L3533 |
| <a id="disc-ea-03"></a> DISC-EA-03 | Como vincular fatos a commits, alterações locais, estado do Meso e versões de implantação? | P03 / P04 | DEC-043, DEC-051 · F4-L3534 |
| <a id="disc-ea-04"></a> DISC-EA-04 | Quando uma alteração invalida fato, aresta, índice e pacote derivado? | P04.1–P04.5 | DEC-038, DEC-044 · F4-L3535 |
| <a id="disc-ea-05"></a> DISC-EA-05 | Como controlar acesso/retensão/distribuição de nós, arestas, metadados e resumos entre Siglas? | PE-01 / P04.7–P04.10 | DEC-001, DEC-002, DEC-052 · F4-L3536 |
| <a id="disc-ea-06"></a> DISC-EA-06 | Que critérios objetivos de qualidade, cobertura, precisão e custo serão obrigatórios para o Motor? | P03.20 / C-P03-07 | DEC-015 · F4-L3537 |
| <a id="disc-ea-07"></a> DISC-EA-07 | Como distinguir fato observado, inferência, documento aprovado e evidência de produção? | PE-03 / PE-04 / PE-09 | DEC-047, DEC-051 · F4-L3538 |
| <a id="disc-ea-08"></a> DISC-EA-08 | Qual é o formato comum de contratos de comportamento e sua regra de precedência? | PE-02 / PE-06 / PE-07 | DEC-035, DEC-037 · F4-L3548 |
| <a id="disc-ea-09"></a> DISC-EA-09 | Como resolver contextos e skills na inicialização, na troca de etapa e na delegação? | PE-05 / PE-06 / PE-07 | DEC-011, DEC-036 · F4-L3549 |
| <a id="disc-ea-10"></a> DISC-EA-10 | Quais restrições exigem controle efetivo fora do modelo e onde esse controle pode ser imposto? | PE-01 / PE-04 / PE-06 | DEC-033, DEC-052 · F4-L3550 |
| <a id="disc-ea-11"></a> DISC-EA-11 | Qual a matriz real de capacidades entre Devin CLI/Web/Desktop e Claude Code na versão corporativa? | PE-02 | DEC-009, DEC-010 · F4-L3551 |
| <a id="disc-ea-12"></a> DISC-EA-12 | Como provar conformidade de comportamento com tolerância à variabilidade dos modelos? | PE-06 / P03.20 | DEC-014, DEC-015 · F4-L3552 |
| <a id="disc-ea-13"></a> DISC-EA-13 | Como incorporar/substituir skills e MCPs específicos sem drift nem ampliação indevida de autoridade? | PE-07 | DEC-035, DEC-037, DEC-038 · F4-L3553 |
| <a id="disc-ea-14"></a> DISC-EA-14 | Qual catálogo inicial mínimo de papéis atende a primeira entrega? | PE-06 | DEC-032 · F4-L3563 |
| <a id="disc-ea-15"></a> DISC-EA-15 | Como especificar tarefa delegada, contexto mínimo, permissões, dependências e entrega? | PE-06 / PE-05 | DEC-032, DEC-033 · F4-L3564 |
| <a id="disc-ea-16"></a> DISC-EA-16 | Quando escolher execução direta, delegação pontual, paralelismo e orquestração externa? | PE-06 | DEC-015, DEC-032 · F4-L3565 |
| <a id="disc-ea-17"></a> DISC-EA-17 | Como detectar conflitos semânticos entre serviços/contratos, além de colisões de arquivos? | PE-06 / PE-08 | DEC-029, DEC-044 · F4-L3566 |
| <a id="disc-ea-18"></a> DISC-EA-18 | Como reconhecer oportunidades de paralelismo escondidas e quando replanejar? | PE-06 | DEC-029, DEC-032 · F4-L3567 |
| <a id="disc-ea-19"></a> DISC-EA-19 | Como calcular custo e ganho marginal sem números arbitrários e sem sobrecarregar tarefas pequenas? | P03.20 / PE-06 | DEC-015 · F4-L3568 |
| <a id="disc-ea-20"></a> DISC-EA-20 | O que será persistido entre sessões e como sobreviver a falhas/interrupções? | PE-05 / PE-06 / P04 | DEC-023, DEC-030 · F4-L3569 |
| <a id="disc-ea-21"></a> DISC-EA-21 | Qual a localização física e responsabilidade de raiz de instalação, Macro, Meso e repositório de Workspaces? | PE-01 / PE-05 | DEC-003 já fixa raiz/instalação/Macro. Workspace/Meso, caches e layout restante seguem em refinamento. DEC-003, DEC-024 · F4-L3579 |
| <a id="disc-ea-22"></a> DISC-EA-22 | Até onde o PE-08 materializa a visão de arquitetura de uma solução? | PE-08 | A camada e o repositório foram definidos. Permanecem a representação concreta, o alcance de cada descoberta e o mecanismo de identidade. [PE-08](#identidade-solucao). DEC-040, DEC-041, DEC-042, DEC-045 · F4-L3580 |
| <a id="disc-ea-23"></a> DISC-EA-23 | Que fontes/autoridades definem conhecimento de Negócios, e qual sua unidade de organização? | PE-09 | Qualquer pessoa pode esclarecer, com autoria quando identificada e escopo registrado. Autoridade para cada incorporação e unidade física seguem a esclarecer. DEC-045, DEC-047, DEC-048, DEC-049, DEC-052 · F4-L3581 |
| <a id="disc-ea-24"></a> DISC-EA-24 | Como adaptar motor/sandbox/CLIs a máquinas e serviços corporativos (versões, download e permissão)? | PE-01 / PE-02 | DEC-012, DEC-035 · F4-L3582 |
| <a id="disc-ea-25"></a> DISC-EA-25 | Quais operações da visão de implementação, testes e CI/CD entram em qual release, sob quais autorizações? | PE-06 / visão maior | DEC-019, DEC-032, DEC-033 · F4-L3583 |
| <a id="disc-ea-26"></a> DISC-EA-26 | Como autorizar e revalidar licenças, dependências transitivas e extensões externas? | PE-02 / PE-07 | Falta identificar titular e procedimento de autorização, inclusive para dependências transitivas e redistribuição. DEC-035, DEC-038 · F4-L3584 |

### Adendo de discovery · F4

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="qd-ad-01"></a> QD-AD-01 | Quais unidades de conhecimento podem ser editadas independentemente e quais precisam de uma origem principal? | Define granulação documental e revalidação. · P03.22. | DEC-016, DEC-049 · F4-L3604 |
| <a id="qd-ad-02"></a> QD-AD-02 | Como representar afirmação, evidência, fonte, versão externa, relação, procedimento e capacidade sem confundir naturezas? | Evita inferência apresentada como fato. · P03.22/PE-07/09. | DEC-041, DEC-047 · F4-L3605 |
| <a id="qd-ad-03"></a> QD-AD-03 | Quais estados qualitativos distinguem relatado, inferido, documentado, testado, aprovado e observado em ambiente? | Define alcance de cada conclusão. · P03/P04. | DEC-047, DEC-051 · F4-L3606 |
| <a id="qd-ad-04"></a> QD-AD-04 | Qual é a origem principal do procedimento que conecta dois repositórios? | Evita duplicação e define direitos de publicação. · PE-03/05/07. | DEC-049, DEC-052 · F4-L3607 |
| <a id="qd-ad-05"></a> QD-AD-05 | O que pode ser retido/indexado a partir de fala, documento, transcrição, massa de teste ou log? | Direitos e dados sensíveis. · P04.7–10, PE-09. | DEC-052 · F4-L3608 |
| <a id="qd-ad-06"></a> QD-AD-06 | Qual o tratamento de declaração humana com autoridade limitada ou conflitante? | Preserva S1/S2/S3 sem estender seu alcance. · P03/P04. | DEC-037, DEC-048, DEC-052 · F4-L3609 |
| <a id="qd-ad-07"></a> QD-AD-07 | Como diferenciar conhecimento reutilizável de dados transitórios de uma atividade? | Determina destino e vida útil. · PE-05/07. | DEC-023, DEC-049 · F4-L3610 |
| <a id="qd-ad-31"></a> QD-AD-31 | Quem autoriza incorporação quando o conhecimento surge **fora de Workspace** e não há Analista de atividade identificado? | Não extrapolar S2 nem permitir publicação sem autoridade. · P03 S2, P04, PE-07. | Sem atividade e sem titular identificado, a incorporação fica candidata. Silêncio não é aceite. DEC-007, DEC-048, DEC-052 · F4-L3611 |
| <a id="qd-ad-08"></a> QD-AD-08 | Onde fica fisicamente raiz operacional, Macro Git, cache, índices e materialização seletiva? | Evita acesso indiscriminado e acoplamento ao layout. · PE-01/P03.22. | DEC-003 responde à raiz/Macro. Layout de cache, índices e materialização seletiva continua a definir. DEC-003, DEC-024 · F4-L3621 |
| <a id="qd-ad-09"></a> QD-AD-09 | Qual evento exige verificar metadados remotos, diff de código ou evidência de implantação? | Evita sincronização desnecessária e afirmação de atualidade falsa. · P04.1. | DEC-043, DEC-051 · F4-L3622 |
| <a id="qd-ad-10"></a> QD-AD-10 | Quando o Workspace usa commit pinado, branch móvel ou árvore local com alterações? | Define fidelidade da composição. · PE-01/05/P04. | DEC-023, DEC-043 · F4-L3623 |
| <a id="qd-ad-11"></a> QD-AD-11 | Como tratar submódulo inacessível no pai e metadados que revelam sua existência? | Segurança de catálogo e Git. · PE-01/P04.9/10. | DEC-001, DEC-002, DEC-052 · F4-L3624 |
| <a id="qd-ad-12"></a> QD-AD-12 | Como classificar cache e índices derivados para retenção, exclusão e revogação? | Direito de consulta ≠ retenção/redistribuição. · P04.7–10. | DEC-052 · F4-L3625 |
| <a id="qd-ad-13"></a> QD-AD-13 | Quais invariantes de contexto L0 são inegociáveis e quais regras/skills devem ser adiadas? | Evita prompt gigante e perda de orientação obrigatória. · PE-02/06/07. | DEC-011, DEC-035, DEC-036 · F4-L3626 |
| <a id="qd-ad-14"></a> QD-AD-14 | Como medir que recuperação “ótima” preserva condições e exceções, não somente tokens? | Define métricas de suficiência. · P03.20/22. | DEC-015 · F4-L3627 |
| <a id="qd-ad-15"></a> QD-AD-15 | Qual isolamento pode ser realmente aplicado a shell, ferramentas e modalidades remotas? | Promessas de segurança dependem de enforcement real. · PE-01/02/04. | DEC-009, DEC-033 · F4-L3628 |
| <a id="qd-ad-16"></a> QD-AD-16 | Quais eventos externos invalidam conhecimento sem qualquer commit de código? | Rulesets, flags, configuração e processos humanos mudam. · P04.1–4/PE-07. | DEC-051 · F4-L3629 |
| <a id="qd-ad-17"></a> QD-AD-17 | Como registrar a fronteira entre a integração implementada e uma decisão tomada por regra externa? | Delimita o que o consumidor permite explicar. PE-03/P03.6. | DEC-047, DEC-051 · F4-L3639 |
| <a id="qd-ad-18"></a> QD-AD-18 | Quais fontes ODM estão realmente acessíveis: documentos, RuleApps, rulesets, logs, simulações e versões implantadas? | Não presumir funcionamento ou credenciais corporativas. · PE-03/07. | DEC-043, DEC-052 · F4-L3640 |
| <a id="qd-ad-19"></a> QD-AD-19 | Como distinguir leitura de fonte externa, simulação e execução remota com efeitos? | Autorizações distintas. · P03.21/P04. | DEC-033, DEC-052 · F4-L3641 |
| <a id="qd-ad-20"></a> QD-AD-20 | O que satisfaz a definição de pronto do onboarding quando a regra de seleção pertence a outro sistema? | Evita obrigar execução e evita conclusão indevida. · P03 DoD/P03.13. | DEC-018, DEC-047 · F4-L3642 |
| <a id="qd-ad-21"></a> QD-AD-21 | Qual catálogo mínimo de papéis, critérios e entregáveis cabe na primeira entrega? | Evita criação de agentes sem especialização real. · PE-06. | DEC-032 · F4-L3652 |
| <a id="qd-ad-22"></a> QD-AD-22 | Como um agente propõe novas tarefas derivadas sem criar executores fora da política global? | Separa descoberta e autorização de execução. · PE-06/04. | DEC-032, DEC-033 · F4-L3653 |
| <a id="qd-ad-23"></a> QD-AD-23 | O grafo de tarefas deve ter um único dono de estado entre sessão nativa e scheduler externo? | Evita múltiplas fontes concorrentes de verdade. · PE-06. | DEC-032 · F4-L3654 |
| <a id="qd-ad-24"></a> QD-AD-24 | Que mecanismos Claude Code/Devin, por modalidade, comprovam aninhamento, pausa, retomada e gestão de concorrência? | Compatibilidade real, não assumida. · PE-02/06. | DEC-009, DEC-010, DEC-015 · F4-L3655 |
| <a id="qd-ad-25"></a> QD-AD-25 | Como identificar conflito de contrato entre repositórios sem exigir sempre verificação manual completa? | Necessário para paralelismo de escrita. · PE-06/08. | DEC-029, DEC-044 · F4-L3656 |
| <a id="qd-ad-26"></a> QD-AD-26 | Quais sinais justificam dividir, unir, repriorizar, suspender ou cancelar tarefas? | Base para replanejamento proporcional. · PE-06. | DEC-028, DEC-029 · F4-L3657 |
| <a id="qd-ad-27"></a> QD-AD-27 | Como conectar premissas/evidências do conhecimento às tarefas e testes que as utilizaram? | Permite reparação dirigida, estilo TMS. · P03.22/P04/PE-05/06. | DEC-029, DEC-044 · F4-L3658 |
| <a id="qd-ad-28"></a> QD-AD-28 | Como evitar thrashing de replanejamentos, agentes órfãos e duplicação de efeitos? | Qualidade, custo e continuidade. · PE-06. | DEC-029, DEC-030 · F4-L3659 |
| <a id="qd-ad-29"></a> QD-AD-29 | Como garantir estados consistentes ao retomar após falha parcial em vários repositórios? | Git não oferece atomicidade física entre repos. · PE-05/06/P04. | DEC-013, DEC-023, DEC-030 · F4-L3660 |
| <a id="qd-ad-30"></a> QD-AD-30 | Em quais condições um orquestrador externo é superior aos mecanismos nativos? | Evita dependência precoce de Gas City/LangGraph/Temporal. · PE-02/06, P03.20. | DEC-015, DEC-032 · F4-L3661 |

### Tensões e lacunas de evidência · F4

| ID | Pergunta, necessidade ou tensão da origem | Efeito, evidência ou relação original | Alcance da comparação |
|---|---|---|---|
| <a id="ed-lac-01"></a> ED-LAC-01 | Tensão de sequenciamento, já reconhecida nas fontes; nenhum roteiro proposto substitui a retomada formal. | A §20.2 e B §§21, 22.1, 23 preservam P04.1, embora proponham antecipar contratos P03.22 e avaliação P03.20. · Conferir continuidade vigente e decidir encaixe dos impactos transversais. DISC-EA-01/06; QD-AD-01/14. | Consultar continuidade R04 para o estado da primeira entrega; P04.1 tem alcance histórico. DEC-014, DEC-019, DEC-023 · F4-L4082 |
| <a id="ed-lac-02"></a> ED-LAC-02 | Lacuna de autorização. O YAML não resolve quem aprova sem Workspace; sua indicação de Analista vale no contexto em que S2 identifica essa autoridade. | B §§6.2–6.3, AD-EA-35, QD-AD-31 e CT-AD-27; o apêndice A usa aprovação por Analista em exemplo que admite sessão direta. · Identificar titular, destino, finalidade e autoridade competente fora de atividade; manter candidato até definição. | Titular fora do Workspace segue aberto. DEC-007, DEC-048, DEC-052 · F4-L4083 |
| <a id="ed-lac-03"></a> ED-LAC-03 | Especificação posterior atribuída à documentação externa, sem evidência corporativa nem nova consulta nesta sessão. Não é contradição demonstrada, nem garantia vigente. | A §§12.4–12.5 e 15 descreve capacidades genéricas; B §13.5 afirma aninhamento Claude com profundidade padrão no recorte consultado. · Validar versão, modalidade, configuração e limites; não extrapolar para Devin ou Agent Teams. DISC-EA-11; QD-AD-24; CT-AD-22. | Profundidade, aninhamento e controle dependem da revisão e modalidade efetivas. DEC-009, DEC-010 · F4-L4084 |
| <a id="ed-lac-04"></a> ED-LAC-04 | O texto histórico indagava sobre a identidade física da raiz, do Macro, do Meso e do repositório de Workspaces. | A §§2.2–2.3 e anexo F; B §§2.1, 7.3 e QD-AD-08. · Definir layout e ownership sem alterar topologia ou regras R06 por inferência. DISC-EA-21. | Raiz, instalação e Macro são a mesma distribuição por DEC-003. O saldo específico é Workspace/Meso e o layout ainda aberto. DEC-003, DEC-024 · F4-L4085 |
| <a id="ed-lac-05"></a> ED-LAC-05 | Tensão de integração: iniciar devin/claude diretamente não prova que um orquestrador externo controla a sessão. | A §§15.1, 15.4; B §§14.5, 17.4. · Demonstrar interfaces, dono do estado, cancelamento, retomada e política por modalidade. DISC-EA-16/20; QD-AD-23/30. | Abertura direta de CLI não demonstra controle externo da sessão. DEC-015, DEC-032 · F4-L4086 |
| <a id="ed-lac-06"></a> ED-LAC-06 | Lacuna de validade: HEAD, diff e hook não garantem atualidade semântica, deploy, revogação ou enforcement de todos os pushes. | A §§6.4, 16.5; B §§8.4–8.6, 11.7. · Definir eventos externos, critérios de invalidação/revalidação e controles do conteúdo exato; P04 permanece aberto no recorte herdado. DISC-EA-03/04/05; QD-AD-09/12/16. | Conservar o requisito de verificação exata no push. Hook ou HEAD isolado não prova validade de implantação ou revogação. DEC-043, DEC-051 · F4-L4087 |
| <a id="ed-lac-07"></a> ED-LAC-07 | Lacuna de revisão normativa: URLs de branch são mutáveis; blobs são objetos de arquivo, não um commit completo; PR #9 aberto é observação histórica. | A anexo E; B cabeçalho e apêndice G. · Confirmar commit, fonte vigente e eventual sucessor antes de usar como aceite atual. Não houve consulta remota nesta auditoria. | PR e branch são móveis. Blob identifica arquivo. Para conferir conteúdo e sucessão, usar o commit e a árvore identificados. DEC-019, DEC-023 · F4-L4088 |
| <a id="ed-lac-08"></a> ED-LAC-08 | Lacuna empírica: capacidades publicadas, licenças relatadas, benchmarks e fundamentos não demonstram integração, segurança nem desempenho empresarial. | A §§9–11, 15, 18; B §§13.5, 16–17, 19 e bibliografia. · Ensaios e decisões apropriados, por versão e ambiente; nenhuma PoC ou integração corporativa foi executada aqui. | DEC-014/015 encaminham avaliação futura. Faltam ensaios e decisões apropriados à versão e ao ambiente. DEC-014, DEC-015 · F4-L4089 |


<a id="agenda-memoria"></a>

## Como a agenda informa um ensaio

Na proposta F3, definir registro de memória, publicação/sincronização e política de investigação antes de selecionar o conjunto mínimo de ferramentas. CA01–CA24 pertencem ao catálogo F3. Um ensaio futuro poderia incluir pergunta reaproveitável, exceção que impede o reuso, alteração de dependência e retomada em outra máquina; escala e responsáveis ainda pedem definição. Similaridade alta pode esconder uma condição alterada; um grafo parcial pode omitir impacto e um índice antigo pode encaminhar a evidência vencida. Identificar componentes e edições separadamente. F3 distingue licenciamento de Serena por componente, mudança de dependências em CocoIndex v1, comportamento do Entire a partir de 0.10.0 preservando configurações anteriores até alteração de backend e a necessidade de conferir distribuição de Phoenix e Redis. São relatos de pesquisa da edição, sem adoção decorrente.

<a id="sequencia-historica"></a>

### Sequência de refinamento proposta em F4

A sequência histórica de dez passos começava por confirmar base e autoridade, modelar conhecimento, tratar validade e circulação, experimentar produção/recuperação em Micro, Meso e caso entre repositórios e especificar os contratos comuns/adaptações. Seguiam-se papéis e delegação, validação da atividade entre etapas, refinamento de Arquitetura/Solução e Negócios, avaliação de integração e custo e só então definição estável de implementação e pastas. A proposta de adoção tecnológica considerava licença, compatibilidade, qualidade funcional, isolamento, recuperação, custo e benefício, atualização, reversão e decisão de titular autorizado. A escolha poderia variar por tarefa e linguagem. Compare o saldo R04 antes de reutilizar qualquer parte dessa sequência.

## Como localizar os detalhes nas fontes

Na pasta `detalhes/` do ZIP corrigido v0, os limites abaixo vão da primeira âncora ou passagem até o fim real do último corpo no mesmo caderno. Unidades intercaladas podem pertencer a outras fichas. A matriz conserva os conjuntos exatos; a coluna de origem informa as unidades extremas como pontos de entrada. A última coluna explicita a relação com a regra desta página ou a função de uma passagem auxiliar.

| Seção na origem | Caderno dentro de `detalhes/` e limites inclusivos | Origens extremas | Contribuição ou função no destino |
|---|---|---|---|
| <a id="u102"></a> 12 Questões abertas e refinamento · F1 | 13-decisoes-e-continuidade/f1-12.md · L5–56 | F1-P320 · F1-P329 | Quatorze entradas de onboarding preservam pergunta e evidência necessária por atividade. F1 sugere começar pelo resultado a preservar, derivar evidência e só então composição e cenários sintéticos. Critérios e compensações materiais dependem de decisão humana. [Passagem integrada](#onb-pen-01). |
| <a id="u103"></a> 10 Recomendações e escolhas pendentes · F2 | 13-decisoes-e-continuidade/f2-10.md · L5–45 | F2-P161 · F2-P169 | Oito itens do catálogo visual relacionam dados a uma escolha: projeto e versão, materiais e defeitos, dependências, revisão das relações, saída, divisão e manutenção. VIS é localizador editorial. Um teste de vista só requer os insumos pertinentes. [Passagem integrada](#vis-01). |
| <a id="u104"></a> 12 Decisões pendentes e continuidade · F3 | 13-decisoes-e-continuidade/f3-12.md · L5–54 | F3-P342 · F3-P351 | Quatorze perguntas ligam o contrato da memória, sincronização, investigação e critérios de teste. F3 propõe partir dos contratos, comparar composição mínima com CA01..24 e ensaiar reutilização, exceção, mudança da dependência e retomada em outra máquina. Escala e responsáveis ainda não definidos. [Passagem integrada](#agenda-memoria). |
| <a id="u105"></a> 23. Questões abertas e agenda de decisões · parte 2 · F4 | 13-decisoes-e-continuidade/f4-cap-23-02.md · L9–19 | F4-L3664 · F4-L3669 | A agenda F4 preserva como recorte inicial distribuição, Micro/Meso, lacunas, Workspace e critérios. Orquestração durável, banco temporal, backend cloud e automação integral de PR/GMUD não decorrem da inclusão de uma hipótese no catálogo. [Passagem integrada](#a13-012). |
| <a id="u106"></a> 23. Questões abertas e agenda de decisões · F4 | 13-decisoes-e-continuidade/f4-cap-23.md · L7–199 | F4-L3510 · F4-L3655 | DISC-EA organiza perguntas de contrato, interoperabilidade, delegação e infraestrutura. QD-AD as distribui também entre autoridade, materialização/contexto, investigação de sistema externo e adaptação. A divisão é da fonte; cada linha abaixo conserva sua relação com o recorte PE/P. [Passagem integrada](#agendas). |
| <a id="u107"></a> 23. Questões abertas e agenda de decisões · F4 | 13-decisoes-e-continuidade/f4-cap-23.md · L200–205 | F4-L3656 · F4-L3661 | As linhas finais QD-AD-25..30 perguntam por conflito semântico entre repositórios, mudança de escopo, efeitos de premissas sobre tarefas/testes, repetição de efeitos, recuperação sem atomicidade física e comparação com orquestração nativa. São perguntas concretas do adendo, com motivos próprios, distintas das oito ED-LAC. [Passagem integrada](#qd-ad-25). |
| <a id="u108"></a> 24. Dependências, continuidade e orientação para futuras sessões · parte 2 · F4 | 13-decisoes-e-continuidade/f4-cap-24-02.md · L9–22 | F4-L3816 · F4-L3826 | O histórico de continuidade conserva clientes da primeira entrega, definição de pronto do produtor, topologia e composição, competência para vínculo de repositório/Sigla, classes de contribuição e comunicação precoce de lacunas. DEC-003/042 atualizam só os objetos que resolveram. [Passagem integrada](#a13-020). |
| <a id="u109"></a> 24. Dependências, continuidade e orientação para futuras sessões · parte 2 · F4 | 13-decisoes-e-continuidade/f4-cap-24-02.md · L23–83 | F4-L3827 · F4-L3875 | A lista final exige distinguir revisão de código e evidência de implantação, preservar os direitos sobre procedimentos e tratar MAPE-K, TMS e nomes de motores como alternativas. A retomada indica os nove episódios POS, origens, jurisdição do aceite, prova e pendências. [Passagem integrada](#a13-020). |
| <a id="u110"></a> 24. Dependências, continuidade e orientação para futuras sessões · F4 | 13-decisoes-e-continuidade/f4-cap-24.md · L7–195 | F4-L3672 · F4-L3813 | O roteiro histórico vincula hipóteses de contratos, validade, produção e recuperação, adaptadores, delegação, Workspace, arquitetura e negócio a experimentos antes de decidir stack e estrutura. A ordem e os prompts de F4 conservam sua função histórica; o fechamento R04 permanece a entrada dos grupos da primeira entrega. [Passagem integrada](#sequencia-historica). |
