# Papéis, autoridade e delegação de tarefas

A decisão sobre papéis especializados se aplica à perspectiva adotada pelo agente durante uma atividade. A distribuição em processos, o catálogo de perfis e a implementação do escalonador são propostas do dossiê F4. Na descoberta de uma Solução, o Analista delimita o alcance com ajuda do agente. A pessoa que inicia a descoberta ou registra um commit conserva a autoria de sua contribuição, sem ganhar representação formal da Solução. A atribuição de uma contribuição feita fora de uma atividade aguarda refinamento próprio. [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040) · [R04-DEC-045](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-045) · [Autoridade em PE-08](01-visao-e-autoridade.md#pe08).

<a id="abertura"></a>

<a id="a08-001"></a>

Quem recebe uma tarefa, quem pode autorizá-la e quem verifica o resultado são perguntas diferentes. A R04 registra a atuação em papéis específicos conforme a atividade e a etapa do Workspace. O catálogo de papéis, a escolha de um escalonador e os mecanismos que decidiriam quando abrir novas frentes permanecem propostas. [Origem A08-001](#origem-a08-001).

<a id="papeis"></a>
## Quem atua e com que autoridade

<a id="a08-002"></a>

A **etapa** situa o trabalho no ciclo de engenharia. O **papel** define a responsabilidade e o método. A **skill** descreve um procedimento reutilizável. A **ferramenta** permite executar uma operação. O **contrato da tarefa** reúne objetivo, entradas, critérios, limites, revisão e autorização. A **instância do agente** assume o contrato no runtime disponível. A **autoridade humana ou corporativa** decide aprovações, vínculos, execução, escrita e publicação conforme o caso. Uma pessoa pode fornecer esclarecimento independentemente de cargo pré-classificado. Registre o contexto e o alcance do relato, o fundamento disponível e as divergências. Atribua a autoria quando identificada. A incorporação do esclarecimento segue o aceite pertinente. [Origem A08-002](#origem-a08-002).

| Responsabilidade candidata | Entrega e limite |
|---|---|
| <a id="a08-003"></a> Analista de Negócios, Engenheiro de Requisitos | Investigar finalidade, política, jornada, exceções e responsáveis. Especificar fronteiras, condições e critérios verificáveis. O Analista humano conserva o aceite formal do refinamento no exemplo de reenvio de pedido. [Origem A08-003](#origem-a08-003). |
| <a id="a08-004"></a> Investigador Técnico, Arquiteto de Soluções | O primeiro investiga integrações e revisões, registrando indícios, hipóteses e lacunas, em regra sem escrita no código. O segundo compara alternativas, dependências, riscos e compromissos técnicos. A decisão corporativa requer a autoridade correspondente. [Origem A08-004](#origem-a08-004). |
| <a id="a08-005"></a> Planejador de Implementação, Engenheiro de Software | Decompor a mudança aprovada e sequenciar tarefas. Implementar dentro da especificação, do plano e dos artefatos autorizados. A entrega registra alterações, efeitos, verificações e falhas. [Origem A08-005](#origem-a08-005). |
| <a id="a08-006"></a> Engenheiro de Testes, Revisor Técnico | Projetar cenários, extremos e regressões. Distinguir o planejado do efetivamente executado, incluindo revisão, alcance e resultado. O revisor confronta especificação, diffs, evidências e políticas. Uma fonte errada, comum a dois agentes, pode levá-los à mesma conclusão incorreta. [Origem A08-006](#origem-a08-006). |
| <a id="a08-007"></a> Curador de Conhecimento, Coordenador de Atividade | Reconciliar fatos, fontes e correções, com autorização quando houver publicação ou circulação. Coordenar dependências, custos, limites, síntese e divergências. Se o fundamento de uma decisão material divergir, a coordenação apresenta as posições e seus impactos à pessoa competente. A curadoria preserva autoria e autoridade nas duas versões. [Origem A08-007](#origem-a08-007). |

<a id="a08-008"></a>

A mesma instância pode assumir um papel temporariamente. Uma única pergunta pode pedir três investigações independentes, como política de identidade do pedido, implementação de idempotência e testes de concorrência. A implementação subsequente aguarda sua especificação aprovada. Em documentação visual, a atribuição de Devin é examinar os materiais, editar definições e operar os geradores. A fidelidade às fontes e a legibilidade da vista exigem conferência própria. [Origem A08-008](#origem-a08-008).

<a id="contrato"></a>
## O que contratar e como aceitar a devolução

<a id="a08-009"></a>

A proposta de perfil combina etapa, papel, instruções globais, atividade, fontes, revisões, ferramentas, permissões e saída esperada. A tarefa explicita quatro dimensões. A **obrigação** determina o que entregar. O **limite** especifica o que excede o escopo. A **capacidade** identifica recursos e conhecimento disponíveis. A **conclusão** descreve a prova necessária e como uma lacuna afeta o fechamento. A conformidade se verifica pelas operações e entregas observáveis nos clientes. [Origem A08-009](#origem-a08-009).

<a id="a08-010"></a>

Por exemplo, o contrato hipotético de investigador `repository-investigator` atribui `TASK-203` à investigação das dependências de `REG-042`, com manifesto de revisões e recuperação seletiva. Permite leitura segundo o acesso efetivo, veda escrita e exige aprovação para execução remota. O resultado precisa identificar impactos evidenciados, hipóteses ainda sem verificação, lacunas com consequência, próximas verificações e cobertura. Uma inspeção estática delimita o que se conhece do código. O exemplo exige evidência adicional para afirmar comportamento em execução. [Origem A08-010](#origem-a08-010).

<a id="a08-011"></a>

Para transportar esse contrato de um cliente a outro, o núcleo mantém escopo e obrigações comuns. Adaptadores de ferramenta traduzem parâmetros, respostas e erros. Adaptadores de cliente acomodam instruções, hooks, skills e permissões efetivos. A devolução identifica origem, versão, transformação, cobertura, falha e limite da conclusão. Se o cliente recebe um caminho inacessível ou perde uma capacidade avançada, deve declarar a parte que conseguiu verificar e a limitação encontrada. Se houver alternativa compatível, pode indicá-la. Se o cliente for incompatível e não houver alternativa, deve registrar a incompatibilidade. O orçamento pode encerrar o trabalho com uma condição material ainda pendente. [Origem A08-011](#origem-a08-011).

<a id="delegacao"></a>
## Como descobrir e distribuir trabalho independente

<a id="a08-012"></a>

A árvore de objetivos expressa a decomposição lógica. O grafo de dependências determina a ordem e permite arestas entre ramos. O **planejador** descobre tarefas e condições. O **escalonador** identifica as prontas, distribui recursos e acompanha a execução. O **executor** realiza as operações autorizadas. O **validador** confronta o que recebe com os critérios. A hierarquia pode ser profunda sem reservar um processo ou um agente-gerente por nó ou repositório. [Origem A08-012](#origem-a08-012).

<a id="a08-013"></a>

A estratégia candidata começa por reconhecimento de baixo custo. Ela procura subtarefas com entradas e saídas claras, hipóteses que possam ser examinadas separadamente e razões para revisão independente. Compara especialização, caminho crítico, permissão, recursos compartilhados, custo de contexto, inicialização e integração. Pode escolher busca programática, execução direta, uma delegação, leituras paralelas, execução por dependências ou escrita isolada sob autorização. Reavalia a escolha após descobertas materiais. Uma solicitação de timeout de dez segundos pode revelar retry, backoff, consumidores e conflito de SLA. Um algoritmo de três mil linhas fortemente sequencial pode se beneficiar apenas de revisão pontual. [Origem A08-013](#origem-a08-013).

<a id="a08-014"></a>

Num exemplo sintético, um serviço encaminha um pedido a um motor de regras externo. Analisar o contrato de envio, a regra candidata e o consumidor do retorno pode produzir uma avaliação de impacto. O impacto alimenta o plano de mudança e o de testes antes da validação integrada. Uma nova regra descoberta pelo investigador gera **proposta de tarefa** com revisão, motivo, dependências, riscos e saída. A coordenação confere duplicação, autorização, prioridade, disponibilidade e conflito antes do despacho. O descobridor pode continuar outra investigação ou aguardar. [Origem A08-014](#origem-a08-014).

<a id="a08-015"></a>

Worktrees podem separar edições; duas branches ainda podem alterar de modo incompatível um DTO e seu consumidor, uma regra compartilhada ou uma infraestrutura externa. Outros conflitos atingem a premissa, a autoridade para publicar ou a associação entre teste e versão. O integrador necessita de contratos, revisões, resultados e evidências. Para efeitos mutáveis, os controles candidatos incluem leases ou locks com expiração e reconciliação, estado persistido quando necessário e idempotência. Na retomada, consultar o resultado de uma ação externa incerta evita duplicação. F4-L1798 propõe isolar mudanças em worktrees, branches ou ambientes e reconciliar diffs e contratos. O objeto a aceitar ao final é a revisão integrada. Uma alteração autorizada no produtor e outra no consumidor podem compilar separadamente e divergir quanto ao significado de um valor. O reparo exige voltar ao contrato e aferir a combinação. [Origem A08-015](#origem-a08-015).

<a id="replanejamento"></a>
## Como reagir quando uma premissa muda

<a id="a08-016"></a>

O projeto propõe relacionar três conjuntos. O grafo de **conhecimento** contém afirmações, fontes, revisões e validade. O grafo de **tarefas** contém objetivos, dependências, estados, executores e resultados. A **fundamentação** liga a criação ou conclusão de uma tarefa às evidências, premissas e decisões que a sustentaram. Assim, uma mudança no conjunto de regras de um sistema externo pode atingir testes e planos mesmo que o consumidor permaneça no mesmo commit. O exemplo de 300 respostas que utilizam uma regra ilustra a busca de dependentes; o número é hipotético e cada parte precisa de avaliação de impacto. [Origem A08-016](#origem-a08-016).

<a id="a08-017"></a>

1. **Detectar e situar.** Registrar evento, origem, revisão e condição que perdeu validade. Entre os gatilhos propostos estão correção de requisito, fonte ou acesso indisponível, nova dependência, teste inesperado, bloqueio e limitação de recursos. Sem monitor ativo, a descoberta ocorre na próxima leitura ou ciclo. O registro identifica a primeira evidência disponível da mudança. [Origem A08-017](#origem-a08-017).
<a id="a08-018"></a>

2. **Determinar impacto.** Localizar tarefas, critérios, histórias, especificações e testes apoiados na premissa. Isolar o material atingido, preservar as partes cuja independência pode ser demonstrada e evitar promover silenciosamente o resultado obsoleto. [Origem A08-018](#origem-a08-018).
<a id="a08-019"></a>

3. **Reparar o plano.** Ajustar uma tarefa local, reconstruir uma subárvore ou mudar estratégia e caminho crítico, conforme o alcance. Versionar a mudança e reconciliar resultados produzidos sob o plano anterior. Requisito, autoridade, vínculo, custo ou risco acima do concedido requerem decisão humana específica. O restante autorizado pode prosseguir. A decisão funcional sobre o repositório da Solução permanece vigente. Se mudar sua finalidade ou fronteira acordada, o Analista conduz a delimitação com apoio do agente. Permanece em aberto como identificar duplicidade ou evolução da mesma Solução. [Autoridade em PE-08](01-visao-e-autoridade.md#pe08). [Origem A08-019](#origem-a08-019).
<a id="a08-020"></a>

4. **Testar a utilidade do ajuste.** Verificar custo marginal, progresso, ciclos, tarefas órfãs, estagnação e reabertura desnecessária. Janelas de observação, orçamento e cooldown são mecanismos candidatos. Tempo até conclusão validada, custo com coordenação/retrabalho, oportunidades perdidas, conflitos e retomada precisam ser medidos em tarefas comparáveis. [Origem A08-020](#origem-a08-020).

<a id="a08-021"></a>

MAPE-K fornece a separação entre monitorar, analisar, planejar e executar com conhecimento compartilhado. HTN representa decomposição hierárquica. O DAG representa dependências e o escalonador despacha as tarefas prontas conforme os recursos disponíveis. Bazel e Nx ilustram reexecução incremental, e o trabalho de Jon Doyle sobre TMS fundamenta o vínculo entre premissas e conclusões. Execução durável, reconstrução do estado por eventos e auditoria respondem a necessidades diferentes. São fundamentos ou referências estudadas. A escolha da coordenação nativa ou externa ainda depende de demonstrar integração, durabilidade, controle e custo em cada modalidade, preservando a experiência de iniciar diretamente `devin` ou `claude`. [Origem A08-021](#origem-a08-021).

## Como reencontrar as evidências

As notas numeradas estão no ZIP corrigido v0, em `rastreabilidade/temas/08.md`. Cada nota identifica as unidades usadas no bloco e seu índice de origem. A [consulta de origens](../consulta-origens.md) identifica as edições e permite partir de uma unidade. Os localizadores em tabelas incluem a linha do cabeçalho. A ligação a um bloco registra uso daquela passagem no texto.

<details>
<summary>Notas e antecedentes por passagem</summary>

| Passagem | Nota no ZIP v0 | Antecedente ou limite da comparação |
|---|---|---|
| <a id="origem-a08-001"></a> [A08-001](#a08-001) | `n1` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |
| <a id="origem-a08-002"></a> [A08-002](#a08-002) | `n2` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-048](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-048) |
| <a id="origem-a08-003"></a> [A08-003](#a08-003) | `n3` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-004"></a> [A08-004](#a08-004) | `n4` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040) |
| <a id="origem-a08-005"></a> [A08-005](#a08-005) | `n5` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-006"></a> [A08-006](#a08-006) | `n6` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-007"></a> [A08-007](#a08-007) | `n7` | [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-008"></a> [A08-008](#a08-008) | `n8` | [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-009"></a> [A08-009](#a08-009) | `n9` | [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |
| <a id="origem-a08-010"></a> [A08-010](#a08-010) | `n10` | Ver a fonte e o grau de autoridade da passagem. |
| <a id="origem-a08-011"></a> [A08-011](#a08-011) | `n11` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-039](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-039) |
| <a id="origem-a08-012"></a> [A08-012](#a08-012) | `n12` | [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |
| <a id="origem-a08-013"></a> [A08-013](#a08-013) | `n13` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) |
| <a id="origem-a08-014"></a> [A08-014](#a08-014) | `n14` | [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |
| <a id="origem-a08-015"></a> [A08-015](#a08-015) | `n15` | [R04-DEC-005](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-005) · [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) |
| <a id="origem-a08-016"></a> [A08-016](#a08-016) | `n16` | [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) |
| <a id="origem-a08-017"></a> [A08-017](#a08-017) | `n17` | [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) |
| <a id="origem-a08-018"></a> [A08-018](#a08-018) | `n18` | [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) · [R04-DEC-044](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-044) |
| <a id="origem-a08-019"></a> [A08-019](#a08-019) | `n19` | [R04-DEC-028](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-028) · [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) · [R04-DEC-044](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-044) |
| <a id="origem-a08-020"></a> [A08-020](#a08-020) | `n20` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-029](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-029) · [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) |
| <a id="origem-a08-021"></a> [A08-021](#a08-021) | `n21` | [R04-DEC-031](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-031) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |

</details>

<details>
<summary>Localizar as seções, tabelas e exemplos nos originais</summary>

Cada linha identifica o recorte titular. Os IDs das extremidades permitem abrir a composição exata da faixa no Repasse 2, em `indices-origem/faixas.csv` e `matriz.jsonl`. As linhas intermediárias seguem a seleção daquela ficha. Títulos delimitam a seção e casos, tabelas e registros preservam sua natureza original.

| Faixa | Da primeira à última unidade da ficha | O que procurar |
|---|---|---|
| <a id="faixa-u054-01"></a> U054-01 | `F4-L476` | Introduz responsabilidades de arquitetura e contratos transversais do dossiê. |
| <a id="faixa-u054-02"></a> U054-02 | `F4-L478 … F4-L483` | A decomposição descreve capacidades lógicas que podem ficar na mesma implementação. |
| <a id="faixa-u054-03"></a> U054-03 | `F4-L485 … F4-L507` | O mapa separa onde se registra conhecimento, onde se decide o encaminhamento e onde a operação é executada. |
| <a id="faixa-u054-04"></a> U054-04 | `F4-L509 … F4-L515` | O plano de controle só impõe autoridade nos percursos que efetivamente consegue controlar. |
| <a id="faixa-u054-05"></a> U054-05 | `F4-L517 … F4-L532` | O número de responsabilidades do mapa não fixa serviços, instâncias ou pessoas. |
| <a id="faixa-u054-06"></a> U054-06 | `F4-L534 … F4-L565` | Unidades distintas precisam compartilhar objetivo, autoridade, revisão e critério de conclusão. |
| <a id="faixa-u054-07"></a> U054-07 | `F4-L567 … F4-L591` | Um inventário de capacidades permite selecionar quem investiga, executa, verifica e conserva evidências. |
| <a id="faixa-u054-08"></a> U054-08 | `F4-L593 … F4-L596` | Os exemplos dos apêndices permitem discutir contratos e retomada no contexto de proposta. |
| <a id="faixa-u055-01"></a> U055-01 | `F4-L1609` | Abre o catálogo de papéis e contratos propostos. |
| <a id="faixa-u055-02"></a> U055-02 | `F4-L1611 … F4-L1616` | Situa papéis e entregas no ciclo da atividade e no grau de autorização. |
| <a id="faixa-u055-03"></a> U055-03 | `F4-L1618 … F4-L1630` | Etapa, papel, procedimento, ferramenta, instância e pessoa autorizadora identificam objetos diferentes. |
| <a id="faixa-u055-04"></a> U055-04 | `F4-L1632 … F4-L1649` | O catálogo ilustra responsabilidades de negócio, especificação, arquitetura, implementação, testes, revisão, curadoria e coordenação. |
| <a id="faixa-u055-05"></a> U055-05 | `F4-L1651 … F4-L1657` | Uma tarefa pode reunir várias perspectivas e a mesma instância pode assumir responsabilidades temporárias. |
| <a id="faixa-u055-06"></a> U055-06 | `F4-L1659 … F4-L1665` | Orientar a investigação significa pedir método, evidências e justificativas observáveis. |
| <a id="faixa-u055-07"></a> U055-07 | `F4-L1667 … F4-L1673` | Compor o perfil pela atividade evita entregar todas as instruções e informações a cada papel. |
| <a id="faixa-u055-08"></a> U055-08 | `F4-L1675 … F4-L1687` | Investigação, alteração e verificação exigem operações, autorizações e saídas diferentes. |
| <a id="faixa-u055-09"></a> U055-09 | `F4-L1689 … F4-L1698` | Obrigação, limite, capacidade e prova de conclusão tornam a devolução avaliável. |
| <a id="faixa-u055-10"></a> U055-10 | `F4-L1700 … F4-L1706` | O nome de um papel deixa em aberto competência humana, operação autorizada e acesso efetivo. |
| <a id="faixa-u055-11"></a> U055-11 | `F4-L1708 … F4-L1711` | O exemplo de tarefa identifica regra, revisão, restrição de escrita e verificação pendente. |
| <a id="faixa-u055-12"></a> U055-12 | `F4-L1743` | O fecho distingue os contratos de quem implementa, projeta testes e compara alternativas arquiteturais. Assumir o papel de arquiteto não confere aprovação corporativa. |
| <a id="faixa-u056-01"></a> U056-01 | `F4-L1919` | Continua a investigação de como encaminhar trabalho novo descoberto durante uma tarefa. |
| <a id="faixa-u056-02"></a> U056-02 | `F4-L1921 … F4-L1934` | A descoberta pode originar uma proposta que retorna à coordenação com sua dependência e seu motivo. |
| <a id="faixa-u056-03"></a> U056-03 | `F4-L1936 … F4-L1939` | A primeira espécie de conflito descrita nesta parcela é a disputa pelo mesmo recurso físico, como arquivo, worktree, branch ou índice. Os demais tipos prosseguem na faixa seguinte. |
| <a id="faixa-u057-01"></a> U057-01 | `F4-L1940 … F4-L1949` | Contratos, estado externo, premissas, autoridade e prova podem conflitar entre repositórios. Uma worktree isolada requer reconciliação posterior, inclusive quando o conflito é semântico. |
| <a id="faixa-u057-02"></a> U057-02 | `F4-L1951 … F4-L1966` | Comparar execução direta, consultas programáticas e delegação proporcional ao benefício pretendido. |
| <a id="faixa-u057-03"></a> U057-03 | `F4-L1968 … F4-L1983` | O modelo de tarefa proposto vincula objetivo, insumo, predecessor, revisão, efeito e aceite. |
| <a id="faixa-u057-04"></a> U057-04 | `F4-L1985 … F4-L2007` | O grafo candidato torna explícitos produtores e consumidores de resultado entre os ramos. |
| <a id="faixa-u057-05"></a> U057-05 | `F4-L2009 … F4-L2029` | A escolha de delegar depende da independência real, do custo marginal e da capacidade de integração. |
| <a id="faixa-u057-06"></a> U057-06 | `F4-L2031 … F4-L2039` | Definir quem inicia, recebe, cancela e reconcilia as tarefas antes de ampliar a coordenação. |
| <a id="faixa-u057-07"></a> U057-07 | `F4-L2041 … F4-L2050` | Separar escrita concorrente e tratar colisão, expiração e repetição de efeito. |
| <a id="faixa-u058-01"></a> U058-01 | `F4-L1746` | Abre a proposta de decomposição e escalonamento seletivo. |
| <a id="faixa-u058-02"></a> U058-02 | `F4-L1748 … F4-L1753` | Posiciona o paralelismo como estratégia a avaliar para uma tarefa e um recorte. |
| <a id="faixa-u058-03"></a> U058-03 | `F4-L1755 … F4-L1768` | Contabilizar especialização e caminho crítico junto ao custo de preparação, contexto e integração. |
| <a id="faixa-u058-04"></a> U058-04 | `F4-L1770 … F4-L1789` | Dependência, autoridade, recurso compartilhado e evidência exigida podem limitar a divisão. |
| <a id="faixa-u058-05"></a> U058-05 | `F4-L1791 … F4-L1802` | O conjunto de estratégias vai de execução direta a mudanças isoladas. Em F4-L1798, worktrees, branches ou ambientes distintos exigem depois reconciliar os diffs e os contratos. |
| <a id="faixa-u058-06"></a> U058-06 | `F4-L1804 … F4-L1825` | A árvore de finalidade e as arestas de dependência servem a perguntas diferentes no mesmo plano. |
| <a id="faixa-u058-07"></a> U058-07 | `F4-L1827 … F4-L1849` | Verificar se a tarefa está pronta e seus consumidores podem interpretar o contrato de saída. |
| <a id="faixa-u058-08"></a> U058-08 | `F4-L1851 … F4-L1864` | A matriz distingue colisão de arquivos, contrato incompatível, infraestrutura compartilhada, conhecimento concorrente, divergência de negócio e condição temporal. Cada linha apresenta uma resposta candidata. |
| <a id="faixa-u058-09"></a> U058-09 | `F4-L1866 … F4-L1872` | Acompanhar recurso, limite, estado da operação e resultados que devem retornar à integração. |
| <a id="faixa-u058-10"></a> U058-10 | `F4-L1874 … F4-L1883` | Fazer reconhecimento inicial e reavaliar a estratégia diante de nova evidência material. |
| <a id="faixa-u058-11"></a> U058-11 | `F4-L1885 … F4-L1909` | Verificar viabilidade, risco de interferência, independência e ganho líquido antes de delegar. |
| <a id="faixa-u058-12"></a> U058-12 | `F4-L1911 … F4-L1916` | Uma atividade pode atravessar vários repositórios e apresentar diferentes áreas de investigação. A hierarquia de responsabilidades pode exigir poucos executores, conforme custo e necessidade reais. |
| <a id="faixa-u059-01"></a> U059-01 | `F4-L2198` | Cabeçalho sobre execução durável, reconstrução por eventos e auditabilidade. A seção prossegue na faixa seguinte. |
| <a id="faixa-u059-02"></a> U059-02 | `F4-L2200 … F4-L2208` | Retomar um trabalho, reconstruir seu estado e auditar o ocorrido exigem evidências diferentes. |
| <a id="faixa-u059-03"></a> U059-03 | `F4-L2210 … F4-L2234` | Combinar dependências entre tarefas com vínculos entre conclusões e premissas usadas. |
| <a id="faixa-u059-04"></a> U059-04 | `F4-L2236 … F4-L2239` | Identificar evento, origem, efeito e parcela que deve retornar à validação. |
| <a id="faixa-u059-05"></a> U059-05 | `F4-L2268` | Uma proposta de tarefa não inicia o executor. Uma conclusão obtida no plano anterior exige reconciliação se mudarem as premissas. A retomada durável pode exigir estado persistente e versionado. |
| <a id="faixa-u060-01"></a> U060-01 | `F4-L2053` | Abre a parte do dossiê que relaciona replanejamento e fundamentos de computação. |
| <a id="faixa-u060-02"></a> U060-02 | `F4-L2055 … F4-L2060` | Situa mudança de premissa em relação ao plano e às definições já validadas. |
| <a id="faixa-u060-03"></a> U060-03 | `F4-L2062 … F4-L2068` | Uma mudança que atinge a especificação reabre o aceite pertinente antes de alteração produtiva. |
| <a id="faixa-u060-04"></a> U060-04 | `F4-L2070 … F4-L2076` | A necessidade relatada é reagir a uma descoberta que altera o trabalho ainda em curso. |
| <a id="faixa-u060-05"></a> U060-05 | `F4-L2078 … F4-L2086` | O reparo proposto limita a reabertura ao conjunto atingido e preserva o que segue sustentado. |
| <a id="faixa-u060-06"></a> U060-06 | `F4-L2088 … F4-L2105` | Eventos podem decorrer de entrada alterada, dependência nova, falha, restrição de acesso ou de recurso. |
| <a id="faixa-u060-07"></a> U060-07 | `F4-L2107 … F4-L2118` | Distinguir ajuste de tarefa, reparo de ramo e mudança de estratégia. |
| <a id="faixa-u060-08"></a> U060-08 | `F4-L2120 … F4-L2128` | Custo, estabilidade e progresso orientam a revisão de um plano que muda repetidamente. |
| <a id="faixa-u060-09"></a> U060-09 | `F4-L2130 … F4-L2136` | Mudança de finalidade, autoridade ou requisito aprovado requer o competente no respectivo escopo. |
| <a id="faixa-u060-10"></a> U060-10 | `F4-L2138 … F4-L2144` | Os fundamentos acadêmicos esclarecem funções da proposta e deixam em aberto a tecnologia. |
| <a id="faixa-u060-11"></a> U060-11 | `F4-L2146 … F4-L2154` | MAPE-K relaciona observação, análise, planejamento e atuação com conhecimento compartilhado. |
| <a id="faixa-u060-12"></a> U060-12 | `F4-L2156 … F4-L2162` | HTN representa decomposição hierárquica de objetivos. |
| <a id="faixa-u060-13"></a> U060-13 | `F4-L2164 … F4-L2170` | Reparar um plano busca reaproveitar uma parte válida diante de um evento localizado. |
| <a id="faixa-u060-14"></a> U060-14 | `F4-L2172 … F4-L2178` | Um DAG explicita precedências e permite despachar tarefas disponíveis conforme recursos. |
| <a id="faixa-u060-15"></a> U060-15 | `F4-L2180 … F4-L2188` | A computação incremental explicita o que recalcular. O impacto semântico pode exigir outra investigação. |
| <a id="faixa-u060-16"></a> U060-16 | `F4-L2190 … F4-L2195` | TMS relaciona premissas e conclusões e orienta a revisão quando muda uma justificativa. |

</details>
