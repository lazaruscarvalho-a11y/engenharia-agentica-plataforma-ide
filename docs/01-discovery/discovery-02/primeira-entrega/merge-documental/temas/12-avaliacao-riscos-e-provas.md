# Critérios, cenários e alcance das provas

A R04 encaminha a definição e a execução de cenários por agentes em etapa posterior e pede avaliação de qualidade, tempo, contexto, recursos e custo por tarefa e modalidade. Os catálogos F1–F4 desenvolvem essa direção com situações, métricas e comparações que permanecem propostas. Para cada resultado, o leitor precisa conseguir identificar objeto, revisão, referência, condição de acesso, denominador e responsável pela avaliação. [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [Avaliação candidata D02](../../../AVALIACAO.md).

<a id="abertura"></a>

<a id="a12-001"></a>

Este capítulo orienta a leitura dos critérios de qualidade, cenários, riscos e provas de conceito. As fontes descrevem resultados a demonstrar. As avaliações precisam identificar a tarefa, a referência usada para julgar sua execução e o alcance da conclusão. [Origem A12-001](#origem-a12-001).

<a id="prova"></a>
## O que cada verificação permite concluir

| Pergunta | Evidência pertinente | Limite da conclusão |
|---|---|---|
| <a id="a12-002"></a> A integração entregou a saída anunciada? | Campos, revisão, efeito, estado de erro e acesso pelo cliente. No exemplo de CodeWiki via MCP, Devin ainda precisa conseguir abrir o caminho devolvido. | Um transporte funcional pode entregar uma referência ilegível. Abrir o arquivo ainda deixa por verificar a compreensão do conteúdo. [Origem A12-002](#origem-a12-002). |
| <a id="a12-003"></a> A explicação é sustentada e cobre o recorte? | Confrontar afirmações com trechos e revisões, condições, exceções e contraevidências. Verificar quais indícios materiais foram tratados e quais fontes foram excluídas. | Um recorte finito tem limites. Nem duas respostas derivadas do mesmo grafo constituem duas origens independentes, nem a falta de uma aresta prova ausência de relação. [Origem A12-003](#origem-a12-003). |
| <a id="a12-004"></a> O resultado serve à tarefa? | Comparação de qualidade, tempo, contexto e custo com uma referência competente. Para memória, distinguir recuperação de um registro relevante, reuso aplicável, parcial ou indevido. | Uma resposta anterior pode perder aplicabilidade por mudança de canal, negação ou exceção. O consumo posterior é avaliado separadamente da conclusão do onboarding. No cenário CA22 de F3, registre quais parcelas continuaram sustentadas, quais exigiram nova verificação e quais continuam em aberto. Por exemplo, uma descrição de interface confirmada pode seguir utilizável enquanto uma decisão derivada de regra externa alterada aguarda revalidação. [Memória e evidências](05-evidencias-e-memoria.md). [Origem A12-004](#origem-a12-004). |
| <a id="a12-005"></a> Uma vista explica a arquitetura? | Validar a definição, conferir elementos e relações com fontes do sistema e inspecionar o resultado renderizado no meio de uso. | Um modelo aceito pelo validador ainda pode descrever o sistema incorretamente ou usar uma apresentação ilegível. Para uma vista exportada, teste se o leitor reconhece as relações e se o mantenedor consegue regenerar a mesma seleção e estilo depois de mudar uma relação. [Conversão e regeneração](09-documentacao-visual.md#exportacao). [Origem A12-005](#origem-a12-005). |

<a id="a12-006"></a>

No produtor Micro/Meso, a conclusão exige identificar composição e autoridade, demonstrar cobertura, explicar comportamentos e exceções, rastrear evidências e tratar lacunas. Uma pendência externa delimitada pode permitir entrega com ressalvas quando os critérios aplicáveis estiverem demonstrados. Dependência indispensável mantém parcial ou impedida a parcela atingida. Se a criticidade continuar incerta após investigação autorizada, cabe esclarecimento pelo engenheiro. [Origem A12-006](#origem-a12-006).

<a id="comparacao"></a>
## Como comparar alternativas em condições equivalentes

<a id="a12-007"></a>

A direção herdada de R04-DEC-015 é comparar qualidade, tempo, contexto, recursos e custo por tarefa e modalidade, considerando produção, consulta e manutenção. F1 propõe observar uso nativo competente, integração mínima e otimizações adicionais, com os mesmos direitos e exigências de qualidade. Registre revisão, entradas, ambiente, configuração, estado dos índices e caches, versões observáveis e recursos. Uma variação indisponível para controle deve acompanhar o resultado. Estratégias diferentes podem cumprir a mesma obrigação. [Origem A12-007](#origem-a12-007).

<a id="a12-008"></a>

F4 discrimina o que se acrescentaria em E0–E7. E0 usa Git, shell, busca e leitura direta. E1 adiciona análise especializada; E2, produção documental; E3, recuperação determinística; E4, busca semântica; E5, delegação nativa; E6, planejamento orientado; E7, coordenação externa candidata. O adendo também apresenta uma escala A–G que parte de uma referência convencional, passa por índices, recuperação, delegação e plano global e chega ao replanejamento por eventos. Essas duas séries servem a comparações próprias. Na comparação A–G proposta em F4, as afirmações técnicas precisam ser efetivamente confrontadas com um gabarito validado por engenheiros. Um ensaio pontuado somente por LLM permanece incompleto mesmo quando esse gabarito foi arquivado. [Origem A12-008](#origem-a12-008).

<a id="a12-009"></a>

Meça o resultado validado, incluindo espera, revisão, retrabalho, chamadas, processamento, armazenamento e manutenção. Distinga primeira execução, reconstrução e índice aquecido. Descrições persistentes de ferramentas, hooks, schemas e skills podem gerar custo e interferência fora da chamada que os motivou. Um hook pode acrescentar tempo de processamento mesmo sem injetar tokens. Compare o conjunto efetivamente habilitado. Uma queda no volume de tokens não demonstra economia proporcional de ACUs. [Origem A12-009](#origem-a12-009).

<a id="a12-010"></a>

Para interpretar qualidade, preserve o denominador. Para medir cobertura, divida as fontes materiais examinadas pelas fontes materiais previstas e acessíveis no recorte. Precisão compara relações corretas com relações avaliadas. Recall compara relações relevantes encontradas com as conhecidas na referência. Para medir fundamentação, divida o número de afirmações materiais que têm evidência adequada e localizável pelo total de afirmações materiais avaliadas. Registre a latência de cada etapa (F3 propõe P50/P95, F4 inclui p99) e o intervalo até detecção, invalidação e revalidação. No conjunto de testes de autorização, o resultado esperado é zero divulgações indevidas, incluindo as verificações de metadados, cache e conteúdo derivado. Ao avaliar delegação, inclua conflitos semânticos, oportunidades perdidas, propagação de erro e retomada após interrupção. [Origem A12-010](#origem-a12-010).

<a id="a12-011"></a>

Repita por tipo de tarefa, repositório, linguagem e modalidade. A ausência de diferença observada pode ser inconclusiva. Uma média favorável pode ocultar perda material de precisão em uma classe crítica. Margens, amostra e dimensões em que a compensação é admissível continuam abertas. R04-DEC-014 prevê que, em etapa mais madura, um agente prepare cenários e agentes executem e avaliem os resultados. A sequência preserva o responsável definido, mas o oráculo concreto, os procedimentos e a independência do julgamento ainda precisam ser demonstrados. F1-P198 pede conservar a variação entre repetições e entre tipos de tarefa e repositório. Resultados inconclusivos permanecem identificados no conjunto avaliado. Cabe ao refinamento definir repetições, equivalência e margens por classe antes de concluir pela adoção. [Origem A12-011](#origem-a12-011).

<a id="cenarios"></a>
## Qual família de critérios consultar

| Objeto | Famílias e exemplos de verificação |
|---|---|
| <a id="a12-012"></a> Pontes entre agentes e ferramentas | Os 24 ONB-CA de F1 cobrem contrato/portabilidade, compreensão/diversidade, segurança/falhas/validade e qualidade/eficiência/conclusão. Incluem caminho ilegível, resultado vazio versus truncado, expiração de job, perda de exceção no resumo, efeito anterior a um hook, timeout após possível escrita e orçamento insuficiente. São cenários propostos, distintos dos 49 critérios operacionais da fundação. [Origem A12-012](#origem-a12-012). |
| <a id="a12-013"></a> Memória, reuso e composição Git | F3 CA01–CA24 inclui equivalência sob paráfrase, exceção material, dependência direta/indireta, independência demonstrada, reconstrução em outra máquina e limites de publicação. CA21–24 explicitam ausência de memória aplicável, reuso parcial, tratamento diferente de S1/S2 e troca de pessoa, máquina e cliente. CA22 pertence a F3. A regra de apresentação das três parcelas é candidata e o ensaio operacional continua pendente. [Memória e evidências](05-evidencias-e-memoria.md). [Origem A12-013](#origem-a12-013). |
| <a id="a12-014"></a> Contratos, autoridade, recuperação e execução adaptativa | F4 relaciona 35 requisitos candidatos AD-EA a questões, jornadas, 27 cenários CT-AD e PoCs. AD-EA-35 e CT-AD-27 aparecem junto à contribuição fora de Workspace. Outros casos estudam evidência de uma regra externa, impacto de revisão fora do Git, saturação de custo, retomada e mudança posterior à validação de um candidato a push. [Origem A12-014](#origem-a12-014). |
| <a id="a12-015"></a> Documentação visual | F2 propõe três vistas do material representativo: conjunto, repositório e integração. C01–C10 verificam fidelidade, pergunta atendida, rótulos, conexões, agrupamento, navegação, validação técnica, preservação na conversão, regeneração e esforço. Alterar uma relação comprovada e regenerar revela o custo de manutenção. Não há pesos, nota mínima nem meta universal de zero cruzamentos. [Origem A12-015](#origem-a12-015). |

<a id="pocs"></a>
## Quais provas de conceito sustentariam uma decisão

<a id="a12-016"></a>

O dossiê A de F4 encadeia sete PoCs. A produz Micro verificável de um serviço pequeno e registra divergências dos analisadores. B reúne dois Micros num Meso, com vínculo incerto e terceiro repo inacessível. C compara recuperação por ID/grafo com leitura direta. D investiga busca semântica complementar, distinguindo relações úteis e falsas sob orçamento comparável. E testa adaptadores Claude Code/Devin CLI. F mede ganhos e perdas segundo o tipo de tarefa. G investiga alteração de revisão, revogação, contrato rompido e instrução injetada. A saída pretendida é uma decisão por ferramenta, acompanhada de evidências. [Origem A12-016](#origem-a12-016).

<a id="a12-017"></a>

O adendo B nomeia outra série, POC-AD-A–J. Começa com bootstrap leve, materialização seletiva e recuperação de uma exceção em outro Micro. Prossegue com incorporação autorizada de procedimento externo, dependência de motor de regras, mudança de regras sem novo commit do consumidor e comparação de paralelismo nativo. Os três últimos ensaios investigam hierarquia lógica com limites de poder, reparação do plano atingido e interrupção com efeitos pendentes. Cada linha contém insumos e decisão condicionada. A ordem de PoCs é proposta técnica e não altera o roteiro de Discovery. [Origem A12-017](#origem-a12-017).

<a id="riscos"></a>
## Como ligar risco, contramedida e decisão de adoção

<a id="a12-018"></a>

O registro R01–R16 do dossiê descreve causa, efeito, contramedida a avaliar e situação. O adendo traz vinte riscos com mitigação e evidência esperada. ED-RB-01–20 localiza suas linhas e preserva o complemento de cada uma. Por exemplo, R03 e ED-RB-20 exigem olhar para nomes, arestas e caminhos já expostos em um repositório pai. R08 e ED-RB-13 exigem verificar incompatibilidade de contrato entre serviços mesmo quando os arquivos alterados são distintos. R10, R11 e R15 conservam dependência do fornecedor, licenças e divergência entre instruções. A criticidade real e o aceite da mitigação dependem de arquitetura, dados e ambiente concretos. [Origem A12-018](#origem-a12-018).

<a id="a12-019"></a>

Antes de selecionar um componente, as propostas pedem licença e edição identificadas, uso corporativo permitido, compatibilidade na modalidade efetiva, manutenção, isolamento, recuperação, atualização, rollback, substituição e ganho frente à referência. A evidência acompanha a versão e a tarefa. Mesmo quando os resultados técnicos são favoráveis, o componente continua candidato até que o responsável autorizado registre a decisão de promovê-lo no escopo avaliado. Perda material mantém a adoção no recorte afetado pendente de correção ou decisão explícita. Para representações visuais, é necessário conferir a distribuição efetiva do editor, servidor ou motor de layout. Os números de benchmarks de fornecedor não bastam para aprovar uma combinação. [Origem A12-019](#origem-a12-019).

<a id="fundacao"></a>

## Qual foi o alcance da verificação da fundação?

A Fonte 03 da edição D02-doc-2 reúne documentos de fundação, versões candidatas e ensaios com escopos próprios. A edição reproduzida no Git permite consultar o conteúdo identificado por S2. A situação presente das Fontes exige conferência na superfície do Projeto.

| Objeto | O que a evidência sustenta |
|---|---|
| PGC-001 v1.1.2 e CT-001..008 v1.0.2 | A revisão anterior permanece preservada com as peças e resultados que lhe pertencem. |
| PGC-001 v1.1.3 e CT-001..008 v1.0.3 | Candidatos não ratificados. Modelo de ratificação e parecer documental têm alcance próprio. |
| Piloto C1 | O aceite específico cobre o registro indicado no respectivo recibo. C2 e C3 seguem sujeitos às respectivas autorizações. |
| 49 critérios operacionais | A autoverificação documental de R04 registra **49 NOT_RUN**. Nenhum dos cenários ou das leituras desta incorporação muda esse resultado. |

[Verificação documental de R04](../../consolidacao-r04/VERIFICACAO.md) · [Índice da revisão v1.1.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/7385e67f64a8cf5725b5ee8f2f8a0e928651183a/docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/README.md) · [Fonte 03 da edição identificada](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/7385e67f64a8cf5725b5ee8f2f8a0e928651183a/docs/chatgpt/pacotes/D02-doc-2/Fontes/03-FUNDACAO-E-CANDIDATOS.md).

## Como reencontrar as evidências

As notas numeradas estão no ZIP corrigido v0, em `rastreabilidade/temas/12.md`. Cada nota identifica as unidades usadas no bloco e seu índice de origem. A [consulta de origens](../consulta-origens.md) identifica as edições e permite partir de uma unidade. Os localizadores em tabelas incluem a linha do cabeçalho. A ligação a um bloco registra uso daquela passagem no texto.

<details>
<summary>Notas e antecedentes por passagem</summary>

| Passagem | Nota no ZIP v0 | Antecedente ou limite da comparação |
|---|---|---|
| <a id="origem-a12-001"></a> [A12-001](#a12-001) | `n1` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) |
| <a id="origem-a12-002"></a> [A12-002](#a12-002) | `n2` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a12-003"></a> [A12-003](#a12-003) | `n3` | [R04-DEC-041](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-041) · [R04-DEC-047](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-047) |
| <a id="origem-a12-004"></a> [A12-004](#a12-004) | `n4` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-046](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-046) · [R04-DEC-050](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-050) |
| <a id="origem-a12-005"></a> [A12-005](#a12-005) | `n5` | [R04-DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040) · [R04-DEC-041](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-041) |
| <a id="origem-a12-006"></a> [A12-006](#a12-006) | `n6` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) |
| <a id="origem-a12-007"></a> [A12-007](#a12-007) | `n7` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a12-008"></a> [A12-008](#a12-008) | `n8` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a12-009"></a> [A12-009](#a12-009) | `n9` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a12-010"></a> [A12-010](#a12-010) | `n10` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a12-011"></a> [A12-011](#a12-011) | `n11` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a12-012"></a> [A12-012](#a12-012) | `n12` | [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a12-013"></a> [A12-013](#a12-013) | `n13` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-024](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-024) · [R04-DEC-046](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-046) |
| <a id="origem-a12-014"></a> [A12-014](#a12-014) | `n14` | [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) · [R04-DEC-032](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-032) · [R04-DEC-048](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-048) |
| <a id="origem-a12-015"></a> [A12-015](#a12-015) | `n15` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-040](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-040) |
| <a id="origem-a12-016"></a> [A12-016](#a12-016) | `n16` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-018](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-018) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) |
| <a id="origem-a12-017"></a> [A12-017](#a12-017) | `n17` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-019](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-019) · [R04-DEC-033](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-033) |
| <a id="origem-a12-018"></a> [A12-018](#a12-018) | `n18` | [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) · [R04-DEC-044](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-044) · [R04-DEC-052](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-052) |
| <a id="origem-a12-019"></a> [A12-019](#a12-019) | `n19` | [R04-DEC-014](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-014) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |

</details>

<details>
<summary>Localizar as seções, tabelas e exemplos nos originais</summary>

Cada linha identifica o recorte titular. Os IDs das extremidades permitem abrir a composição exata da faixa no Repasse 2, em `indices-origem/faixas.csv` e `matriz.jsonl`. As linhas intermediárias seguem a seleção daquela ficha. Títulos delimitam a seção e casos, tabelas e registros preservam sua natureza original.

| Faixa | Da primeira à última unidade da ficha | O que procurar |
|---|---|---|
| <a id="faixa-u089"></a> U089 | `F1-P196 … F1-P198` | RF27 em F1-P196–198 propõe comparar integração e uso nativo competente sob tarefa, revisão, acesso e ambiente compatíveis. Avaliar qualidade e custo total de produção, consulta e manutenção. Preservar variações por tentativa, categoria de tarefa e repositório, incluindo inconclusivos. Equivalência, margens, repetições e adoção seguem pendentes. |
| <a id="faixa-u090"></a> U090 | `F1-P203 … F1-P220` | Os requisitos de qualidade derivados de F1 cobrem portabilidade e evolução, segurança e confiabilidade, qualidade da compreensão, eficiência e experiência. Cada aspecto requer demonstração no recorte. |
| <a id="faixa-u091"></a> U091 | `F1-P282 … F1-P308` | O plano de F1 distingue evidência de execução, significado e compreensão. Propõe referência de comparação, dimensões de qualidade e custo, repetição por condição e critérios de adoção ou revisão. |
| <a id="faixa-u092"></a> U092 | `F1-P309 … F1-P319` | Os 24 ONB-CA ligam cenário e resultado esperado às famílias de requisitos de F1. São quatro grupos, sobre portabilidade, compreensão, falhas/validade e qualidade/eficiência/conclusão. |
| <a id="faixa-u093"></a> U093 | `F2-P137 … F2-P147` | O piloto F2 distingue três vistas, critérios C01–C10, edição/licença do componente e impacto de regenerar após uma alteração. A escolha de motor segue a pergunta do leitor. Pesos e meta universal de cruzamentos permanecem abertos. |
| <a id="faixa-u094"></a> U094 | `F3-P317 … F3-P341` | F3 enumera CA01–24 e a demonstração conjunta de troca de pessoa, máquina e cliente. Recuperação, reuso parcial, circulação, reconstrução e custo têm métricas próprias. O registro deve preservar casos inconclusivos. |
| <a id="faixa-u095"></a> U095 | `F4-L2926 … F4-L3018` | O catálogo F4 conserva AD-EA-01–35 como requisitos candidatos. Os vínculos com jornadas, cenários e experiências assinalam como verificar a hipótese, sem declarar cumprimento. |
| <a id="faixa-u096"></a> U096 | `F4-L3160 … F4-L3205` | F4 documenta CT-AD-27 e, depois, CT-AD-08–12. São cenários sobre competência fora de atividade, origem de complemento, contradição humana, recurso fornecido e delimitação entre um consumidor e sua regra externa com ou sem evidência posterior. |
| <a id="faixa-u097"></a> U097 | `F4-L3208 … F4-L3293` | CT-AD-13–23 tratam de mudança externa sem commit, complexidade emergente ou sequencial, proposta de tarefa, conflito entre contratos, requisito alterado, reinício, revogação, diferenças entre clientes e invalidação de premissa. |
| <a id="faixa-u098"></a> U098 | `F4-L3296 … F4-L3333` | CT-AD-24–26 tratam de replanejamento excessivo, saturação de custo e mudança de revisão entre validação e push. A seção propõe medir distribuições e comparar estratégias A–G com confronto efetivo das respostas com um gabarito validado por engenheiros. |
| <a id="faixa-u099"></a> U099 | `F4-L3021 … F4-L3157` | A série E0–E7 compara recursos acrescentados à referência. F4 também propõe métricas de produção, recuperação e delegação, cenários adversariais e CT-AD-01–07, sobre inicialização seletiva, composição, acesso restrito, revisão remota, falta de conexão, exceção e contribuição humana. |
| <a id="faixa-u100"></a> U100 | `F4-L3336 … F4-L3444` | Sete PoCs A–G e dez POC-AD-A–J têm insumos e decisões condicionadas próprios. O encadeamento proposto não altera a ordem do discovery e o desenho de um ensaio permanece sem resultado operacional. |
| <a id="faixa-u101"></a> U101 | `F4-L3447 … F4-L3507` | R01–R16 do dossiê e as vinte linhas do adendo identificam riscos, consequências e contramedidas candidatas. As linhas do adendo pedem também evidência de efetividade. Preserve a revisão e o alcance de cada conjunto. |

</details>
