# Registro de decisões e requisitos — R04

Data: 2026-11-13 · branch `proposta/d02-primeira-entrega-refinamentos` · PR #9 · base imutável `5b9550b56d0929109231863b4546936e1b4d7ee1`.
Fonte primária: manifestações humanas desta sessão; aceites por referência ligam explicitamente a resposta à sugestão anterior. Cadernos conservam o texto de perguntas, respostas, exemplos, recomendações e análises, inclusive as alternativas que não foram escolhidas.

Naturezas distintas: definições humanas no alcance explícito; propostas não aceitas; relatos corporativos sem inspeção; análises editoriais; adiamentos; mecanismos ainda não demonstrados. O encerramento dos grupos é de levantamento/definição, não construção, aceite técnico, operação corporativa ou ratificação.

## Precedência e leitura

P03 conserva os vinte itens funcionais herdados, o DoD separado da interação, S1/S2/S3, uma origem principal por fato e o requisito pré-push. P04 conserva o fechamento no alcance documentado: P04.1–5 com aceites humanos originais não recuperados; P04.6 apoiado em P03; manifestações posteriores recuperadas com seus limites. R04 não autentica retroativamente esses originais.

Os aceites atuais estão individualizados abaixo. Uma explicitação editorial de consequência não recebe autoria humana literal; observar as qualificações. Não interpretar o encerramento de um grupo como aprovação das alternativas não escolhidas ou dos mecanismos postergados.

<a id="r04-dec-001"></a>

## R04-DEC-001 — P01.1

A visibilidade dos Workspaces é a do repositório compartilhado: internal ou private e seus efeitos. O time responsável pelo repositório de Workspaces da Sigla decide, inclusive na discordância entre times. Branches da atividade e conteúdo arquivado acompanham o público do repositório.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004), [R04-U006](fontes/CADERNO-P01.md#r04-u006), [R04-U008](fontes/CADERNO-P01.md#r04-u008).

**Sugestão, pergunta ou análise vinculada:** [R04-A003](fontes/CADERNO-P01.md#r04-a003), [R04-A004](fontes/CADERNO-P01.md#r04-a004), [R04-A005](fontes/CADERNO-P01.md#r04-a005), [R04-A006](fontes/CADERNO-P01.md#r04-a006), [R04-A007](fontes/CADERNO-P01.md#r04-a007).

**Condição/qualificação:** U004 inicialmente atribuía a escolha ao time criador do Workspace; U006 escolhe visibilidade compartilhada; U008 aceita expressamente o responsável sugerido em A007. Não foi escolhida segregação por participante nem repositórios separados por visibilidade.

**Consumidores conhecidos:** P05.3, P05.5, P09.7.

<a id="r04-dec-002"></a>

## R04-DEC-002 — P01.2

A descoberta e leitura dos mapas seguem internal/private e as consequências do repositório de publicação; referência a destino privado não concede leitura desse destino.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004).

**Sugestão, pergunta ou análise vinculada:** [R04-A003](fontes/CADERNO-P01.md#r04-a003), [R04-A004](fontes/CADERNO-P01.md#r04-a004).

**Refinamento posterior:** Destino e organização concreta no refinamento da camada arquitetural.

**Consumidores conhecidos:** P08.6, P09.7.

<a id="r04-dec-003"></a>

## R04-DEC-003 — P01.3

Raiz comum de distribuição, instalação local e Macro são a mesma estrutura: o repositório Macro clonado do GitHub, sob o qual estarão Mesos, Micros, skills, camadas e configurações. Permanece a topologia existente por submódulos.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004).

**Sugestão, pergunta ou análise vinculada:** [R04-A004](fontes/CADERNO-P01.md#r04-a004).

**Refinamento posterior:** Layout, obtenção incremental e mecanismos de atualização; identidade física Workspace/Meso continua não escolhida.

**Consumidores conhecidos:** P02.2, P05.5, P03.22.

<a id="r04-dec-004"></a>

## R04-DEC-004 — P01.4

Clone inicial preservado. A preparação conjunta no primeiro uso diário foi apresentada como sugestão para refinamento posterior. O gatilho diário foi depois definido para atualização das modalidades de IA em P02.4; não se transfere automaticamente esse aceite para todo Macro/MCP/skill/recurso.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004), [R04-U010](fontes/CADERNO-P02.md#r04-u010), [R04-U011](fontes/CADERNO-P02.md#r04-u011).

**Sugestão, pergunta ou análise vinculada:** [R04-A004](fontes/CADERNO-P01.md#r04-a004), [R04-A005](fontes/CADERNO-P01.md#r04-a005), [R04-A009](fontes/CADERNO-P02.md#r04-a009), [R04-A010](fontes/CADERNO-P02.md#r04-a010), [R04-A011](fontes/CADERNO-P02.md#r04-a011).

**Condição/qualificação:** Sugestão original não final: git pull e atualização de Devin CLI/Claude Code/ferramentas/MCPs/skills; não é rotina implementada.

**Refinamento posterior:** Preparação de Macro/MCPs/skills, unidade por instalação/máquina/modalidade, alterações locais, resultado parcial e relação com verificações durante o trabalho.

**Consumidores conhecidos:** P02.4, P02.5, P03-PUSH.

<a id="r04-dec-005"></a>

## R04-DEC-005 — P01.5

Falhas devem apresentar aviso, estado/commit confirmado, trabalho independente que pode continuar e ação dependente que aguarda recuperação. Aplicar as regras existentes de suficiência, evidências e ressalvas.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004).

**Sugestão, pergunta ou análise vinculada:** [R04-A004](fontes/CADERNO-P01.md#r04-a004).

**Refinamento posterior:** Mecanismos e ensaios de recuperação.

**Consumidores conhecidos:** P02.5, P07.5.

<a id="r04-dec-006"></a>

## R04-DEC-006 — P01.6

Usar o acesso existente do usuário à conta corporativa GitHub. Direitos efetivos continuam por operação e destino. A impressão de autenticação normalmente já presente é relato/expectativa, não inspeção do ambiente.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004).

**Sugestão, pergunta ou análise vinculada:** [R04-A004](fontes/CADERNO-P01.md#r04-a004), [R04-A005](fontes/CADERNO-P01.md#r04-a005).

**Refinamento posterior:** Procedimentos corporativos, operações concretas e demais ferramentas DataDog, AWS, ServiceNow/IUClick, ContentStack/CMS e outras; aprofundamento posterior.

**Consumidores conhecidos:** P06.6, P06.7, P07.5.

<a id="r04-dec-007"></a>

## R04-DEC-007 — P01.7

Alinhar estudo, novos entendimentos, conhecimento, instruções e detalhes às estruturas, princípios, diretrizes e critérios da Base de Conhecimento da camada. Preparar na branch local e enviar junto às demais alterações ou isoladamente mediante autorização de git commit e git push.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004), [R04-U006](fontes/CADERNO-P01.md#r04-u006).

**Sugestão, pergunta ou análise vinculada:** [R04-A003](fontes/CADERNO-P01.md#r04-a003), [R04-A004](fontes/CADERNO-P01.md#r04-a004), [R04-A005](fontes/CADERNO-P01.md#r04-a005), [R04-A006](fontes/CADERNO-P01.md#r04-a006).

**Condição/qualificação:** O esclarecimento U006 resolve o alcance funcional do envio. Não introduz abertura obrigatória de PR do produto. S1/S2/S3 e atualização/revalidação pré-push são preservados; autorizar esta publicação não executa operações de aplicações.

**Refinamento posterior:** Pipeline, coordenação técnica multirrepositório e passagem a homologação/produção.

<a id="r04-dec-008"></a>

## R04-DEC-008 — P01.7

Vocabulário transversal: utilizar branch, homologação e produção no contexto do fluxo. Para identidade documental/técnica, utilizar versão, commit de referência, verificação ou validação conforme o significado. A instrução tem alcance pretendido para todas as sessões do Projeto.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U006](fontes/CADERNO-P01.md#r04-u006).

**Sugestão, pergunta ou análise vinculada:** [R04-A006](fontes/CADERNO-P01.md#r04-a006).

**Condição/qualificação:** Não reescrever fontes históricas nem substituir a palavra dentro de nomes de arquivos ou citações antigas. Não aplicar convenção de deploy de aplicações à main documental indiscriminadamente.

**Refinamento posterior:** Aplicação nativa no Projeto ChatGPT não executada; o pacote no Git fica preparado para essa manutenção.

**Consumidores conhecidos:** todos os grupos, docs/chatgpt/INSTRUCOES-PERMANENTES.md.

<a id="r04-dec-009"></a>

## R04-DEC-009 — P02.1

Base funcional comum para o máximo possível de ferramentas de IA: definições, instruções, configurações, parametrizações e recursos permitem lidar de maneira semelhante com a Plataforma e suas operações. Aproveitar particularidades por adaptações explícitas.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U010](fontes/CADERNO-P02.md#r04-u010).

**Sugestão, pergunta ou análise vinculada:** [R04-A009](fontes/CADERNO-P02.md#r04-a009), [R04-A010](fontes/CADERNO-P02.md#r04-a010).

**Condição/qualificação:** A expressão toda ferramenta é direção de compatibilidade, não prova de suporte universal.

**Refinamento posterior:** Capacidades e adequações concretas por modalidade.

**Consumidores conhecidos:** P03.22, P07.1, P06.5.

<a id="r04-dec-010"></a>

## R04-DEC-010 — P02.1

Suporte específico da primeira entrega permanece Devin Web, Devin CLI, Devin Desktop e Claude Code. GitHub Copilot não é acrescentado a esse recorte; permanece possibilidade posterior.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U011](fontes/CADERNO-P02.md#r04-u011).

**Sugestão, pergunta ou análise vinculada:** [R04-A010](fontes/CADERNO-P02.md#r04-a010), [R04-A011](fontes/CADERNO-P02.md#r04-a011).

**Condição/qualificação:** O “Não” de U011 responde à pergunta contextualizada de A010 sobre inclusão do Copilot; não nega o objetivo amplo de portabilidade.

<a id="r04-dec-011"></a>

## R04-DEC-011 — P02.2, P02.3

Descoberta do conhecimento e preparação das configurações seguem a base comum com adaptações específicas. A descoberta gradual de P04 é preservada. Conteúdo, arquivos, momento de preparação, destinos e procedimentos concretos ficam postergados.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U010](fontes/CADERNO-P02.md#r04-u010).

**Sugestão, pergunta ou análise vinculada:** [R04-A009](fontes/CADERNO-P02.md#r04-a009), [R04-A010](fontes/CADERNO-P02.md#r04-a010).

**Refinamento posterior:** Representação, instruções de entrada por modalidade, obtenção do estado correto e escopo material das configurações.

**Consumidores conhecidos:** P03.22, P07.2.

<a id="r04-dec-012"></a>

## R04-DEC-012 — P02.4

No primeiro uso diário, atualizar cada modalidade para a última versão disponível. Diferenças temporárias de versão entre engenheiros são expressamente aceitas.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U010](fontes/CADERNO-P02.md#r04-u010), [R04-U011](fontes/CADERNO-P02.md#r04-u011).

**Sugestão, pergunta ou análise vinculada:** [R04-A009](fontes/CADERNO-P02.md#r04-a009), [R04-A010](fontes/CADERNO-P02.md#r04-a010), [R04-A011](fontes/CADERNO-P02.md#r04-a011).

**Condição/qualificação:** Retifica a expectativa inicial de igualdade contínua. Não foi escolhida versão-alvo corporativa uniforme. A atualização do Macro não comprova atualização de executável/serviço.

**Refinamento posterior:** Mecanismos, origem corporativa da distribuição, comprovação de versão/resultado, Web/Desktop/CLI e falhas.

<a id="r04-dec-013"></a>

## R04-DEC-013 — P02.5

Aplicar a regra aceita aos cenários das modalidades: mensagem identifica componente afetado, o que foi confirmado, trabalho que continua e condição para retomar a ação dependente.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U010](fontes/CADERNO-P02.md#r04-u010).

**Sugestão, pergunta ou análise vinculada:** [R04-A009](fontes/CADERNO-P02.md#r04-a009), [R04-A010](fontes/CADERNO-P02.md#r04-a010).

**Refinamento posterior:** Cenários, meios de comprovação e recuperação.

**Consumidores conhecidos:** P07.5.

<a id="r04-dec-014"></a>

## R04-DEC-014 — P03.20

Em etapa mais madura, um agente de IA (ChatGPT) definirá cenários de testes minuciosos, críticos, criteriosos e rigorosos. Agentes de IA também executarão e avaliarão resultados com base nas definições, requisitos e critérios estabelecidos.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A012](fontes/CADERNO-P03.md#r04-a012), [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Condição/qualificação:** Define responsáveis e sequência, não uma execução atual nem independência automaticamente comprovada entre autores/avaliadores.

**Refinamento posterior:** Casos concretos, fontes, resultados esperados, procedimentos, evidências e critérios quantitativos.

<a id="r04-dec-015"></a>

## R04-DEC-015 — P03.20

C-P03-07 segue o mesmo encaminhamento: comparar futuramente qualidade, tempo, contexto, recursos e custo por tarefa/modalidade. Considerar produzir, consultar e manter, preservando condições e exceções materiais.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A012](fontes/CADERNO-P03.md#r04-a012), [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Refinamento posterior:** Alternativas, medições disponíveis, condições de comparação e compromissos; sem benchmark/limiar aprovado.

**Consumidores conhecidos:** P03.22, P02.1.

<a id="r04-dec-016"></a>

## R04-DEC-016 — P03.22

Detalhamento concreto posterior por agentes, orientado pelas definições existentes. Comparar agrupamentos pela finalidade da consulta e manutenção do significado, usando os casos de P03.20/C-P03-07.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A012](fontes/CADERNO-P03.md#r04-a012), [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Refinamento posterior:** Entrada, unidades, arquivos, formatos, índices, instruções, estrutura física e descoberta gradual.

<a id="r04-dec-017"></a>

## R04-DEC-017 — P03.22

Percurso aceito de manutenção: encontrar a regra → localizar sua origem → alterar no escopo autorizado → identificar referências afetadas → verificar o resultado.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A012](fontes/CADERNO-P03.md#r04-a012), [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Refinamento posterior:** Mecanismo concreto.

**Consumidores conhecidos:** P07.4, P08.5.

<a id="r04-dec-018"></a>

## R04-DEC-018 — P03.22

Preparar futuramente um pequeno Micro e um Meso que o encaminhe, demonstrando consulta rápida de parâmetro e compreensão/modificação de regra com condições, exceções e referências afetadas; comparar para fundamentar a estrutura.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A012](fontes/CADERNO-P03.md#r04-a012), [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Condição/qualificação:** Não reintroduz consulta bem-sucedida de outro agente como DoD do produtor.

**Refinamento posterior:** Produção dos exemplares, ensaios e escolha da estrutura.

<a id="r04-dec-019"></a>

## R04-DEC-019 — P03.20, P03.22

Pontos que exigem concretização factual ficam para refinamentos posteriores: a etapa atual é levantamento, definição e detalhamento de requisitos. Os exemplos não autorizam implementar/executar aplicações.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U013](fontes/CADERNO-P03.md#r04-u013).

**Sugestão, pergunta ou análise vinculada:** [R04-A013](fontes/CADERNO-P03.md#r04-a013).

**Refinamento posterior:** Contratos produtor/consumidor, correspondência ao estado, garantia pré-push e recuperação/composição multirrepositório.

**Consumidores conhecidos:** todos os grupos.

<a id="r04-dec-020"></a>

## R04-DEC-020 — P05.1

O time declara explicitamente o encerramento da atividade, identificando alcance e destino dos itens restantes. O agente pode reunir informações e apontar pendências antes. O término é distinto da aprovação do refinamento; destino de branch/pasta conserva R06.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A014](fontes/CADERNO-P05.md#r04-a014), [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Refinamento posterior:** Registro do encerramento e mecanismos de arquivamento; não autoriza excluir branches nesta missão.

<a id="r04-dec-021"></a>

## R04-DEC-021 — P05.2

O próprio agente efetiva o vínculo de Sigla autorizado pelo Analista com direitos disponíveis e informa resultado ou impedimento. Não implica incluir todos os repositórios nem reinstalar consentimento genérico de leitura.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A014](fontes/CADERNO-P05.md#r04-a014), [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Refinamento posterior:** Arquivos, obtenção dos índices e mecanismo de vínculo.

<a id="r04-dec-022"></a>

## R04-DEC-022 — P05.3

Consulta histórica segue R06, P01 e P04: direitos efetivos, origem, alcance e contexto histórico preservados; itens conservam pertencimento original. Não se cria controle adicional de leitores.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U004](fontes/CADERNO-P01.md#r04-u004), [R04-U006](fontes/CADERNO-P01.md#r04-u006), [R04-U008](fontes/CADERNO-P01.md#r04-u008), [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A014](fontes/CADERNO-P05.md#r04-a014), [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Condição/qualificação:** Regra herdada aplicada editorialmente em A014/A015; não há nova mensagem humana exclusiva de P05.3 nem licença para promover decisão antiga automaticamente a atual.

**Refinamento posterior:** Descoberta e recuperação material do histórico.

<a id="r04-dec-023"></a>

## R04-DEC-023 — P05.4

Retomada deve recuperar objetivo/alcance, fontes/evidências, requisitos e decisões vigentes, hipóteses descartadas/substituídas e motivos, pendências/impedimentos/dependências, estado do trabalho, branches/commits/composição e próxima ação/escolha necessária.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A014](fontes/CADERNO-P05.md#r04-a014), [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Refinamento posterior:** Layout, formatos, recuperação e ensaio por agente.

**Consumidores conhecidos:** P06.4.

<a id="r04-dec-024"></a>

## R04-DEC-024 — P05.5

Repositório de Workspaces deve organizar, indexar e rotear seu conteúdo e relações para que analistas em outras máquinas/sessões obtenham, compreendam e trabalhem com agentes nos Workspaces sem remapear integralmente o entendimento válido. Abrange relações entre Micro, Meso, tarefas, atividades e refinamentos.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Condição/qualificação:** O “de certa maneira, sim” é especificado pelo próprio usuário como função de roteamento. Não basta para afirmar identidade física com Meso. Reuso não dispensa revalidar mudanças relevantes.

**Refinamento posterior:** Identidade física do repositório Workspace com Meso, índices, recuperação e manutenção.

**Consumidores conhecidos:** P06.4, P08.3, P09.4.

<a id="r04-dec-025"></a>

## R04-DEC-025 — P05.6

Sugestão de inclusão informa repositório/Sigla, razão/evidência, lacuna ou tarefa atendida, branch/commit pertinente quando conhecido, direitos/condições faltantes, limitações que permanecerão e continuidade independente. O Engenheiro decide; agente registra decisão e efetiva inclusão autorizada.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015).

**Sugestão, pergunta ou análise vinculada:** [R04-A014](fontes/CADERNO-P05.md#r04-a014), [R04-A015](fontes/CADERNO-P05.md#r04-a015).

**Refinamento posterior:** Apresentação, armazenamento e inclusão concreta.

<a id="r04-dec-026"></a>

## R04-DEC-026 — P06.1

Identificar etapa por item pelo último marco comprovado, decisões registradas e trabalho pendente; permitir correção explícita pelo usuário. Status corporativo pode integrar os sinais; papel concreto definido na integração.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Refinamento posterior:** Estrutura de estados e mecanismo de enquadramento.

<a id="r04-dec-027"></a>

## R04-DEC-027 — P06.1

Haverá registro/atualização de progresso entre etapas, fases e pontos de cada tarefa, desde refinamento até deploy em produção.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Condição/qualificação:** Abrange acompanhamento do ciclo; não é autorização de deploy ou especificação pronta da pipeline.

**Refinamento posterior:** Níveis, marcos/evidências, interrupção/retorno e relação entre estado documental, branch e status corporativo.

<a id="r04-dec-028"></a>

## R04-DEC-028 — P06.2

Propor avanço quando resultados exigidos estiverem demonstrados e pendências materiais tiverem tratamento compatível; apresentar fundamento, avaliar dúvidas, riscos, lacunas e insuficiências e respeitar ato humano aplicável. Analista aprova refinamento.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Condição/qualificação:** Avaliar pendências não significa exigir ausência absoluta de toda pendência independente.

**Refinamento posterior:** Condições concretas de transições e demais atos pertinentes.

<a id="r04-dec-029"></a>

## R04-DEC-029 — P06.3

Mudança de etapa anterior: recuperar definição anterior/nova manifestação; distinguir esclarecimento/correção/decisão/conflito; identificar dependentes; reexaminar partes atingidas; informar efeito sobre etapa atual; preservar continuidade independente. Mensagem nos testes pode afetar outras etapas.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Refinamento posterior:** Rastreamento e propagação concreta.

**Consumidores conhecidos:** P07.4, P08.5.

<a id="r04-dec-030"></a>

## R04-DEC-030 — P06.4

Retomar item usando o conteúdo de P05.4, identificando sua etapa e conferindo o estado que fundamenta a próxima ação, inclusive mudanças relevantes desde a interrupção.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U015](fontes/CADERNO-P05.md#r04-u015), [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Condição/qualificação:** Conteúdo herdado de P05/P04; não houve nova pergunta humana exclusiva de P06.4.

**Refinamento posterior:** Recuperação, conciliação com status corporativo e demonstração.

<a id="r04-dec-031"></a>

## R04-DEC-031 — P06.5

Agentes prepararão futuramente exemplo encadeado da mesma demanda para detalhar competências, fontes, entregáveis e critérios observáveis por etapa.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Refinamento posterior:** Exemplos e avaliação concretos em articulação com P03.

<a id="r04-dec-032"></a>

## R04-DEC-032 — P06.5

Agentes assumirão papéis específicos conforme contexto, atividade e etapa do Workspace/tarefa: negócios, PM, PA, PO, arquitetura, engenharia, cloud/AWS, QA, testes, deploy e outras dimensões pertinentes; interpretarão e responderão conforme esses papéis.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Condição/qualificação:** Papéis de atuação não conferem automaticamente autoridade humana, permissões operacionais ou independência entre avaliadores.

**Refinamento posterior:** Catálogo, competências, sinais de troca, transferência de contexto, quantidade e distribuição dos agentes.

<a id="r04-dec-033"></a>

## R04-DEC-033 — P06.6

Na integração futura, elaborar matriz por operação: gatilho, responsável, condições, efeito e evidência de sucesso, fundamentada no contrato real. Nomes de estados, APIs e autenticação não são escolhidos agora.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Refinamento posterior:** Contratos, estados, direitos efetivos, falhas e resultados incertos.

<a id="r04-dec-034"></a>

## R04-DEC-034 — P06.7

Suporte corporativo da entrega abrange também tasks, subtasks e bugs, além de histórias, com operações aplicáveis a especificar por tipo.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U017](fontes/CADERNO-P06.md#r04-u017).

**Sugestão, pergunta ou análise vinculada:** [R04-A016](fontes/CADERNO-P06.md#r04-a016), [R04-A017](fontes/CADERNO-P06.md#r04-a017).

**Condição/qualificação:** O “Sim, também” aceita a ampliação funcional descrita em A016; não comprova conector ou igualdade de contratos entre tipos.

**Refinamento posterior:** Operações/estados/relacionamentos concretos por tipo.

<a id="r04-dec-035"></a>

## R04-DEC-035 — P07.1

Extensões: finalidade, origem/escopo, versão/commit, aplicabilidade, entradas/resultados pertinentes, pré-requisitos/dependências, operações/limites, exemplo e verificação proporcional ao tipo. Diferenciar instrução/documento de ferramenta executável.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U019](fontes/CADERNO-P07.md#r04-u019).

**Sugestão, pergunta ou análise vinculada:** [R04-A018](fontes/CADERNO-P07.md#r04-a018), [R04-A019](fontes/CADERNO-P07.md#r04-a019).

**Refinamento posterior:** Campos, arquivos e procedimentos de verificação.

<a id="r04-dec-036"></a>

## R04-DEC-036 — P07.2

Descobrir por necessidade/fontes do trabalho; seguir relações até escopo ofertante; verificar aplicabilidade; conservar origem; explicar pertinência. Não aplicar recurso de um repositório indiscriminadamente à Sigla.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U019](fontes/CADERNO-P07.md#r04-u019).

**Sugestão, pergunta ou análise vinculada:** [R04-A018](fontes/CADERNO-P07.md#r04-a018), [R04-A019](fontes/CADERNO-P07.md#r04-a019).

**Refinamento posterior:** Índices, sinais e mecanismo de descoberta gradual.

<a id="r04-dec-037"></a>

## R04-DEC-037 — P07.3

Identificar orientações/origens/condições; conciliar por contexto/evidência; aplicar compatíveis; preservar/apresentar incompatibilidade material; solicitar esclarecimento ao responsável competente quando necessário; registrar fundamento/alcance da resolução. Não presumir que o mais local vence.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U019](fontes/CADERNO-P07.md#r04-u019).

**Sugestão, pergunta ou análise vinculada:** [R04-A018](fontes/CADERNO-P07.md#r04-a018), [R04-A019](fontes/CADERNO-P07.md#r04-a019).

**Condição/qualificação:** Autoridade operacional continua distinta de orientação. A frase copiada “ainda precisamos definir aplicação” foi lida em A019 como concretização futura, pois a conduta funcional foi expressamente aceita.

**Refinamento posterior:** Casos concretos, identificação do responsável pelo assunto e eventual hierarquia automática.

<a id="r04-dec-038"></a>

## R04-DEC-038 — P07.4

Atualização/substituição/retirada: identificar mudança/recurso, preservar histórico legítimo, localizar consumidores conhecidos e avaliar impacto, informar orientações aplicáveis, atualizar/revalidar atingidos, preservar independente e identificar ação que aguarda.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U019](fontes/CADERNO-P07.md#r04-u019).

**Sugestão, pergunta ou análise vinculada:** [R04-A018](fontes/CADERNO-P07.md#r04-a018), [R04-A019](fontes/CADERNO-P07.md#r04-a019).

**Refinamento posterior:** Detecção, rastreamento, atualização e recuperação.

<a id="r04-dec-039"></a>

## R04-DEC-039 — P07.5

Agente explica contexto, ferramenta/operação, detalhes pertinentes, impedimento e causa conhecida de forma coesa, objetiva e clara para o engenheiro compreender e intervir/sugerir solução. Distinguir observação, causa comprovada e causa ainda não determinada; indicar impacto, evidência necessária, continuidade independente e retomada.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U019](fontes/CADERNO-P07.md#r04-u019).

**Sugestão, pergunta ou análise vinculada:** [R04-A018](fontes/CADERNO-P07.md#r04-a018), [R04-A019](fontes/CADERNO-P07.md#r04-a019).

**Condição/qualificação:** A distinção causa conhecida/desconhecida e a continuidade são explicitações editoriais sustentadas por P03/P04/P02; não uma nova frase humana literal.

**Refinamento posterior:** Apresentação, contratos reais e mecanismos.

<a id="r04-dec-040"></a>

## R04-DEC-040 — P08.1

Descoberta arquitetural compreende relação entre diferentes repositórios/aplicações, particularidades, efeitos, consequências e propriedades. Analista delimita alcance/abrangência com ajuda, instruções, explicações e sugestões do agente.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Refinamento posterior:** Procedimento de descoberta e representação concreta.

**Consumidores conhecidos:** P09.4.

<a id="r04-dec-041"></a>

## R04-DEC-041 — P08.2

Registrar finalidade, entradas/situações, resultados, componentes/relações, papel de compartilhados, variantes/retornos/caminhos, fronteiras/partes desconhecidas e alcance confirmado pelo Analista. Distinguir confirmado, candidato e desconhecido.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Refinamento posterior:** Representação e demonstração.

<a id="r04-dec-042"></a>

## R04-DEC-042 — P08.3, P08.1

Solução terá referência estável, identificação, reutilização e acesso; será um repositório próprio e comporá uma camada da Plataforma.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Condição/qualificação:** A escolha de base arquitetural própria decorre da manifestação explícita em P08.3 em conjunto com P08.1; mapas candidatos permanecem úteis durante descoberta, sem voltar a tratar a camada como apenas hipótese.

**Refinamento posterior:** Identificadores, nomes, organização física, equivalência/duplicidade e evolução da identidade.

<a id="r04-dec-043"></a>

## R04-DEC-043 — P08.4

Conhecimento da composição/solução/arquitetura segue estados de produção, homologação e branch atual conforme modificações locais do engenheiro, no mesmo princípio de Micro/Meso. Preservar composição efetivamente estudada, commits/ponteiros, diferenças locais e lacunas conforme P04.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Condição/qualificação:** Não presume três repositórios físicos; não prova configuração/implantação de aplicações. Convenção main/PROD e release/HOM continua relato humano de P04.

**Refinamento posterior:** Armazenamento/versionamento físico e comprovação das correspondências.

<a id="r04-dec-044"></a>

## R04-DEC-044 — P08.5

Identificar mudanças em componentes/relações; examinar efeito conjunto; atualizar/revalidar evidências no escopo autorizado; localizar dependentes; levar ao Analista mudanças na finalidade/fronteira/comportamento acordado ou dúvida material; preservar independente e identificar parte aguardando.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Refinamento posterior:** Detecção, propagação e verificação.

<a id="r04-dec-045"></a>

## R04-DEC-045 — P08.6

A solução não tem representante formal. Identificar, descobrir, criar ou commitar seu repositório não torna a pessoa responsável permanente; tampouco contribuições diretas ou mudanças indiretas em Meso/Micro participantes.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U021](fontes/CADERNO-P08.md#r04-u021).

**Sugestão, pergunta ou análise vinculada:** [R04-A020](fontes/CADERNO-P08.md#r04-a020), [R04-A021](fontes/CADERNO-P08.md#r04-a021).

**Condição/qualificação:** Rejeita a proposta anterior de time mantenedor formal. Autoria/proveniência, direitos reais e competência do Analista para delimitação continuam distintos; não inferir responsabilidade formal para Negócios por analogia.

**Refinamento posterior:** Mecanismos colaborativos, conflitos, continuidade, publicação e recuperação.

<a id="r04-dec-046"></a>

## R04-DEC-046 — P09.1

Adotar o exemplo sintético do canal existente que envia à análise manual e do novo canal: distinguir política abrangente de contingência/especificidade do canal. Caso serve para definir capacidade de recuperar significado/alcance/justificativa/consequência; não fixa a regra real do exemplo.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Refinamento posterior:** Elaboração e avaliação detalhadas por agentes.

<a id="r04-dec-047"></a>

## R04-DEC-047 — P09.2

Fundamentar entendimentos em fontes pertinentes com origem/natureza/alcance/temporalidade; distinguir implementado, declarado, hipótese e decisão futura; preservar contradições/contraevidência; buscar suporte material; entregar parcela sustentada com lacunas.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Condição/qualificação:** Não foi aprovada hierarquia universal de fontes; código sustenta o comportamento evidenciado, não toda generalização para novos públicos/canais.

**Refinamento posterior:** Fontes corporativas específicas e mecanismos.

<a id="r04-dec-048"></a>

## R04-DEC-048 — P09.3

Qualquer pessoa pode dar esclarecimentos. Receber a contribuição sem exigir classificação prévia em papel competente; preservar autoria quando identificada, contexto, alcance, fundamento, divergências e efeito na atividade.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Condição/qualificação:** Observação explícita retifica a proposta de restringir o fornecimento a papéis competentes. Não transforma toda declaração em fato comprovado nem revoga S2/aprovação do refinamento pelo Analista.

**Refinamento posterior:** Representação e tratamento operacional dos esclarecimentos.

<a id="r04-dec-049"></a>

## R04-DEC-049 — P09.4

Recuperação transversal por conceitos/regras e suas relações com produtos, processos, jornadas, soluções e aplicações; permitir caminho inverso partindo da atividade/aplicação. Manter origem principal por fato e referências/derivados verificáveis, com descoberta gradual.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Refinamento posterior:** Unidade organizadora, taxonomia, identificadores, formatos e armazenamento. Repositório próprio de Negócios não foi escolhido.

<a id="r04-dec-050"></a>

## R04-DEC-050 — P09.5

Resposta suficiente: significado; finalidade/justificativa conhecidas; condições/público/exceções/limites; fontes/fundamento; vigência; relação com implementado; consequência para atividade; lacunas/conflitos/próxima ação; autoria da manifestação quando identificada. Profundidade ajustada à necessidade.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Condição/qualificação:** P09.3 troca a exigência de responsável formal por autoria quando identificada; informação ausente continua limitação, não apagamento do trabalho independente.

**Refinamento posterior:** Formato e representação.

<a id="r04-dec-051"></a>

## R04-DEC-051 — P09.6

Distinguir vigência de orientação e estado implementado: registrar temporalidade conhecida, histórico/substituições e relação aos estados de código; identificar diferenças materiais e revalidar afetados; apresentar incerteza quando faltar suporte.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Refinamento posterior:** Registro temporal e integração com branch, homologação e produção.

<a id="r04-dec-052"></a>

## R04-DEC-052 — P09.7

Aplicar direitos efetivos de fontes/destinos e internal/private conforme P01/P04; preservar origem/alcance/restrições conhecidas, preferir referências suficientes, considerar público do destino e apresentar fonte inacessível como lacuna. Sem nova classificação de leitores ou consentimento genérico por consulta.

**Natureza/estágio:** definição/aceite humano no alcance descrito; requisito/direção de discovery; concretização não comprovada.

**Fonte humana:** [R04-U023](fontes/CADERNO-P09.md#r04-u023).

**Sugestão, pergunta ou análise vinculada:** [R04-A022](fontes/CADERNO-P09.md#r04-a022), [R04-A023](fontes/CADERNO-P09.md#r04-a023).

**Refinamento posterior:** Mecanismos nos recursos/destinos concretos.

<a id="r04-her-p03-1"></a>

## R04-HER-P03-1 — P03.1

Consolidar todo conhecimento suficientemente válido descoberto. Nas chamadas HTTP consumidas, recuperar URL/verbo, entradas com tipos e exemplos quando possível, saídas, headers, query/path parameters, timeout e status esperados. Explicar tratamento de respostas quando mudar conclusão material; não duplicar implementação sem necessidade.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/2; BP-S02 ed.2/4/7/8; C-P03-01/02.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-2"></a>

## R04-HER-P03-2 — P03.2

Finalidade do onboarding é fixa; o engenheiro indica a entrada. Examinar, conforme aplicável, responsabilidades, fluxos, regras, contratos, integrações, APIs, workers, tópicos/filas, banco, configurações, variáveis, bibliotecas/frameworks, infraestrutura e procedimentos documentados de operação/teste. AWS/Terraform são relato do ambiente, sem escolha universal de stack.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/3; BP-S02 ed.2/4/7/8; C-P03-03/08 e DoD corrigido.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-3"></a>

## R04-HER-P03-3 — P03.3

Ligar afirmação à revisão e à evidência mais específica permitida: arquivo/seção/classe/método/linha/coluna/cláusula/bloco de infraestrutura. Conservar as duas fontes quando a conclusão depender de ambas.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; requisito transversal de rastreabilidade.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-4"></a>

## R04-HER-P03-4 — P03.4

Meso indexa responsabilidades dos Micro/submódulos e conduz a dúvida aos repositórios pertinentes, indicando material estudado/revisões/limites. Catálogo da raiz encaminha à Sigla desconhecida. Fronteira funcional de solução, inclusive entre Siglas, cabe ao Analista.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/5; BP-S02 ed.2–4/7–10, R6–R8/S3; P08 permanece próprio.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-5"></a>

## R04-HER-P03-5 — P03.5

Não exigir conhecer/provar o total de repositórios da Sigla. Buscar todos que forem encontráveis no acesso permitido e declarar busca/seleção efetiva, obtidos/analisados/falhas. Ausência na seleção não prova inexistência.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; P03.7/9.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-6"></a>

## R04-HER-P03-6 — P03.6

Relação examinada por um lado registra sentido, contrato/evento observado, origem/revisão, limite e fonte necessária do outro lado. Agente pode sugerir inclusão de repositório na atividade; Engenheiro decide.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2/4; C-P03-01 e cenários A/B/C.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-7"></a>

## R04-HER-P03-7 — P03.7

Entradas: diretório local, repositórios arrastados à pasta, links GitHub ou busca por Sigla. Local conserva branch existente salvo escolha do Engenheiro e distingue alterações autorizadas do commit-base. Link remoto de raiz usa main; link de branch é escolha explícita.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2/4/5; C-P03-04/05; falha→P03.9.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-8"></a>

## R04-HER-P03-8 — P03.8

No ambiente relatado, o nome do repositório identifica obrigatoriamente sua Sigla. Motor identifica pertencimento e organiza a cópia; uso em atividade de outra Sigla não transfere pertencimento.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2/3; natureza contextual do relato.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-9"></a>

## R04-HER-P03-9 — P03.9

Parte material incompleta identifica revisão, conteúdo examinado, material faltante, motivo conhecido, consequência e retomada. Entregar parcela sustentada e delimitar a conclusão dependente.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; não converter inacessibilidade em inexistência.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-10"></a>

## R04-HER-P03-10 — P03.10

Nova execução ou entendimento validado deve refletir-se no material pertinente da Sigla; Meso enriquece a partir de seus Micro sem apagar revisões conhecidas dos demais nem cobertura da rodada.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/4; BP-S02 ed.2/3; S1/S2/HUM-08.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-11"></a>

## R04-HER-P03-11 — P03.11

Na interação posterior, confrontar evidência com a ação concreta: explicitar o que pode afirmar/fazer e a decisão que depende de outra fonte. Não impor esse objetivo particular ao encerramento da produção.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/3; BP-S02 ed.2/8; fronteira produtor/interação.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-12"></a>

## R04-HER-P03-12 — P03.12

Comparar objeto, revisão, condições e natureza das fontes diante de divergência. Preservar interpretações/evidências concorrentes e a prova que as distinguiria. Teste documentado não equivale a execução observada.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/4; BP-S02 ed.2/8/9; S1/S3.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-13"></a>

## R04-HER-P03-13 — P03.13

Falta de suporte imprescindível à fidelidade ou delimitação da cobertura impede a conclusão dependente. Se criticidade continuar incerta após investigação autorizada, escalar ao Engenheiro. Parte independente pode ser entregue; uso posterior avalia impacto da ação concreta.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/3; BP-S02 ed.2/7/8; BP-S05.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-14"></a>

## R04-HER-P03-14 — P03.14

Release branch mais recente representa HOM segundo o processo relatado pelo usuário. Registrar commit examinado; interpretar evidência autorizada fornecida sobre implantação/configuração com componente/revisão/ambiente. Ocorrência específica requer sua própria evidência.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2–5; C-P03-06; C-P04-08 posterior complementa o relato, sem comprovar pipeline.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-15"></a>

## R04-HER-P03-15 — P03.15

Intervenção leva menor pergunta útil, hipóteses compatíveis, referências, tentativas autorizadas e decisão afetada. Separar dúvida factual da revisão e escolha futura de produto.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; HUM-02/03.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-16"></a>

## R04-HER-P03-16 — P03.16

Catalogar/comunicar lacuna ou incoerência tão logo percebida, com informação sustentada, limitação e próxima ação. Avisar se continua sozinho ou precisa de decisão humana agora.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2/3; BP-S05.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-17"></a>

## R04-HER-P03-17 — P03.17

Reapresentar ressalva em usos direta ou indiretamente dependentes, inclusive fora do Workspace; explicar relação e consequência concreta. Relação hipotética continua identificada com evidência faltante.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; BP-S05.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-18"></a>

## R04-HER-P03-18 — P03.18

Primeira entrega prioriza Motor sem interface gráfica própria construída pela equipe. Agente explica afirmação afetada, fonte, limitação e próxima ação; detalhe deve ser recuperável por assunto.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2; não escolhe layout final.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-19"></a>

## R04-HER-P03-19 — P03.19

Interação investiga até resposta suficientemente fundamentada pela natureza, escopo, critérios e implicações do pedido; reporta inconclusões e oferece aprofundamento conforme Engenheiro. Produção encerra pelo DoD próprio.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1/3; BP-S02 ed.2/8.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p03-21"></a>

## R04-HER-P03-21 — P03.21

Solicitação excepcional de executar aplicação local só após dúvida intransponível e tentativas autorizadas esgotadas; oferecer resposta direta do Engenheiro, explicitar dúvida/tentativas/finalidade/ambiente/dados/pré-requisitos/comandos/efeitos e obter permissão por ocorrência. Esta missão não executa aplicações.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md).

**Condição/qualificação:** BP-S01 §1; BP-S02 ed.2/3; HUM-03 e RET-001. A segunda resposta rotulada P03.2 foi vinculada editorialmente a P03.21 por posição/assunto, sem alterar o original.

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-1"></a>

## R04-HER-P04-1 — P04.1

Reaproveitar conhecimento cuja validade permaneça demonstrável para a nova revisão; investigar alterações e dependências afetadas. Economia de trabalho não permite presumir validade porque um arquivo ficou igual. Alcance incremental e métodos ainda precisam de demonstração.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** C1-A3, aceite anterior relatado; HUM-08; engenharia posterior

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-2"></a>

## R04-HER-P04-2 — P04.2

Ao detectar mudança, impedir o uso como atual das afirmações afetadas e das conclusões dependentes; preservar informação independente. Registrar impacto indireto incerto e destino inacessível, sem alegar atualização nele.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** C1-A3, aceite anterior relatado; HUM-08

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-3"></a>

## R04-HER-P04-3 — P04.3

Restabelecer a validade somente por evidências pertinentes à afirmação e ao estado estudado. Código pode sustentar comportamento previsto; ocorrência executada exige sua evidência. Parte inconclusiva conserva ressalva.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** C1-A3, aceite anterior relatado; HUM-08

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-4"></a>

## R04-HER-P04-4 — P04.4

Distinguir atualização individual Micro de composição Micro/Meso/raiz. Identificar revisões e ponteiros, manter composição anterior identificada, registrar falha e retomar a etapa incompleta. Corrigir raiz se significado ou referência forem afetados. Não prometer atomicidade física.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** C1-A3, aceite anterior relatado; D02-RET-004; U3/C-P04-05 reforça correspondência

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-5"></a>

## R04-HER-P04-5 — P04.5

Quando a base mudar, reexaminar o significado das contribuições antes de incorporar. Reler revisão vigente, aproveitar partes independentes verificadas, preservar divergências que a evidência não resolve. Ausência de conflito textual não prova compatibilidade semântica.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** C1-A3, aceite anterior relatado; P03/S1/S3

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-6"></a>

## R04-HER-P04-6 — P04.6

Esclarecimento reutilizável preserva fonte, natureza, revisão, condição e público. Para novo entendimento, pedido único ao Analista com entendimento, origem, destino e efeito; silêncio gera pendência, negativa descarta aquele destino. Correção inequívoca segue S1.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** P03/S2, C1-A1/A3/A4; U3/C-P04-01 mantém aprovações específicas

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-7"></a>

## R04-HER-P04-7 — P04.7

Eliminar consentimento genérico adicional para ler fontes internas já legitimamente acessíveis. Manter aceites específicos de decisões humanas, operações sensíveis e alterações já expressamente definidas. Não derivar direitos de uma cópia disponível.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U3/C-P04-01, decisão direta; substitui leitura absoluta de U2

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-8"></a>

## R04-HER-P04-8 — P04.8

Dispensar controle próprio de expiração; reconhecer restrições reais encontradas. Conhecimento pode permanecer quando conservação e distribuição continuam legítimas; perda de fundamento impede uso da cópia. Ausência de expiração não é irrevogabilidade.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U3/C-P04-02, decisão direta; delimita U1/U2

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-9"></a>

## R04-HER-P04-9 — P04.9

Aceitar publicidade corporativa da existência e identidade dos repositórios; leitura do índice não cria acesso ao destino. Classificação padrão de Workspaces/mapas permanece em P01.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U2/P04.9 e U3/C-P04-03; decisão direta

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-10"></a>

## R04-HER-P04-10 — P04.10

Circulação legítima entre camadas como padrão, sem aprovações repetitivas; origem principal por fato, preferir referências suficientes e autorizadas, proteger segredos/dados/direitos de terceiros, conservar origem/revisão/alcance/restrições conhecidas.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U3/C-P04-03/07, decisão direta; delimita 'sem limitações' de U2

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-11"></a>

## R04-HER-P04-11 — P04.11

Conhecimento reflete estado efetivamente usado: branch, commit-base e alterações locais pertinentes. Cada atividade mantém revisão/composição escolhida, sem promoção silenciosa de outra branch. Preservar ponteiros pretendidos dos submódulos.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U1/P04.11, U2/P04.11 aceita recomendação; A3 e U3/C-P04-05/08

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.

<a id="r04-her-p04-12"></a>

## R04-HER-P04-12 — P04.12

Usar informações independentes suficientemente compreendidas. Nunca usar como premissa informação de significado material não recuperado; buscar outra evidência autorizada ou apresentar limitação e suspender conclusão dependente.

**Natureza/estágio:** herança funcional R03; não é novo aceite humano R04; preservado no alcance documentado.

**Fonte herdada imutável:** [R03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md).

**Condição/qualificação:** U3/P04.12, decisão direta; não confundir Git atualizado e compreensão

**Refinamento posterior:** Provas/mecanismos futuros e limites históricos da R03 preservados.
