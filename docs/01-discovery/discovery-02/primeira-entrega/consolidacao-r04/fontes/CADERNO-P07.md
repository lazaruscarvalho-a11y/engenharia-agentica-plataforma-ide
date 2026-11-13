# Caderno de discovery R04 — P07

Fonte: sessão `01a1d60a-f1ae-7173-94cb-03aec33bf344`, “Retomar discovery da Plataforma/IDE”, recuperada em três páginas até `hasMore=false`.
Reprodução autorizada de manifestações sobre requisitos do produto e respostas editoriais; não contém ferramentas, raciocínio privado, credenciais, código do banco ou transcrições de reuniões corporativas.

## Como interpretar

Este caderno conserva a evolução textual para não perder perguntas, respostas, exemplos, sugestões, justificativas, condições e consequências. Não é uma lista de decisões automaticamente aprovadas. Uma resposta do assistente mantém sua autoria; sugestões só têm aceite no alcance das manifestações humanas ligadas no registro. Textos de estado “não persistido” e dúvidas intermediárias são históricos do instante da mensagem. A leitura vigente está em [registro](../REGISTRO-DECISOES.md), [saldo](../SALDO-P01-P09.md) e [retificações](../HISTORICO-E-RETIFICACOES.md).

O vocabulário histórico é preservado literalmente; a redação operacional nova adota branch, homologação e produção, usando versão/commit/verificação/validação quando necessário. Dois envelopes automáticos da retomada foram retirados, preservando os pedidos efetivos e os hashes originais no inventário. Não há autenticação retroativa de transcrições históricas externas.

<a id="r04-u018"></a>

## R04-U018 — Usuário

Mensagem: `01a1d676-36e3-78b0-88f1-da323776bea9` · turno: `01a1d676-36a0-7161-b596-e9adf69e09e5`.

Ótimo, fechamos P06. Vamos para o próximo grupo de pendências e dúvidas.


---

<a id="r04-a018"></a>

## R04-A018 — Assistente

Mensagem: `msg_0e7fa371be357a1b016af76a728a7087d2a8f3fa5b82aa5b77` · turno: `01a1d676-36a0-7161-b596-e9adf69e09e5`.

O próximo grupo é **P07 — Extensões por escopo**. Ele trata da inclusão, descoberta, utilização e manutenção de **skills, instruções, comportamentos, documentação e ferramentas**, inclusive via MCP, associados a repositórios, Siglas, Workspaces ou arquitetura.

O saldo foi recuperado no [catálogo P07](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/PENDENCIAS-P01-P09.md#p07-1) e na [definição de extensões por escopo](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/94b5e42960713670d1519a74fe8dd0f7b3afc03e/docs/01-discovery/discovery-02/primeira-entrega/notas/EXTENSOES-POR-ESCOPO.md).

A capacidade de acrescentar esses recursos, inclusive depois do onboarding, já está prevista. Agora precisamos definir seu comportamento funcional. Formatos, diretórios, configurações, instalação e mecanismos concretos podem permanecer para refinamento posterior.

| Item | Questão |
|---|---|
| **P07.1** | Quais informações tornam uma extensão compreensível e apta à incorporação? |
| **P07.2** | Como reconhecer sua pertinência, inclusive por dependências indiretas? |
| **P07.3** | Como tratar orientações incompatíveis entre escopos? |
| **P07.4** | Como tratar atualização, substituição ou retirada de uma extensão? |
| **P07.5** | O que entregar quando a extensão é conhecida, mas sua operação está impedida? |

As sugestões abaixo permanecem propostas.

**P07.1 — Que informações devem acompanhar uma extensão?**

Uma instrução de leitura e uma ferramenta capaz de realizar operações possuem exigências diferentes. Ambas precisam ser compreensíveis no contexto da Plataforma.

Sua definição de P01.7 já exige alinhar o conteúdo:

> “às estruturas, princípios, diretrizes e critérios da Base de Conhecimento da Camada em questão”

A pendência é definir o conteúdo funcional mínimo desse alinhamento.

**Proposta de informações:**

- **Finalidade:** o que o recurso oferece e qual necessidade atende.
- **Origem e escopo:** a quem pertence e onde sua definição principal é mantida.
- **Versão ou commit pertinente:** qual estado do recurso está sendo utilizado.
- **Aplicabilidade:** quando, por que e em quais condições utilizá-lo.
- **Entradas e resultados esperados:** quando forem pertinentes ao tipo de recurso.
- **Pré-requisitos e dependências:** o que precisa estar disponível.
- **Operações e limites:** o que o recurso permite fazer, respeitados os direitos efetivos.
- **Exemplo de utilização e forma de verificação:** proporcionais ao tipo de contribuição.

**Exemplo documental:** um repositório integrador passa a disponibilizar instruções e um MCP para consultar regras no IBM ODM. O agente precisa compreender a finalidade do conjunto, sua relação com o integrador, quando a consulta é pertinente e quais operações estão disponíveis.

**Sugestão:** adotar esses elementos como requisitos de compreensão, diferenciando o detalhamento conforme o tipo de extensão. Os campos, arquivos e procedimentos de verificação serão definidos posteriormente.

**Pergunta central:** **esse conjunto é suficiente para caracterizar uma extensão ou deseja acrescentar alguma informação funcional?**

**P07.2 — Como descobrir uma extensão pertinente sem conhecer seu nome?**

A descoberta deve funcionar tanto por pedido direto quanto pelas relações da atividade, inclusive fora de um Workspace.

Você já definiu em C-P04-04:

> “Ao iniciar o Agente dentro do repositório da Plataforma ele não deverá automaticamente ler as bases de conhecimentos dos repositórios, siglas, do Macro, dos Workspaces, Arquiteturas e regras de negócio.”

E encaminhou:

> “um mecanismo de descoberta gradual, direcionada e otimizada de contexto e conhecimentos de todas as camadas.”

A questão de P07 é aplicar essa direção aos recursos acrescentados em cada escopo.

**Exemplo documental:** o engenheiro trabalha em um consumidor e pergunta onde determinada decisão é tomada. O agente encontra uma dependência com o integrador e, por esse caminho, chega às instruções e ao recurso do ODM. O engenheiro não precisou conhecer previamente o nome da extensão.

**Sugestão de comportamento:**

- Partir da necessidade e das fontes associadas ao trabalho.
- Seguir as relações pertinentes até o escopo que oferece o recurso.
- Verificar as condições que o tornam aplicável.
- Conservar sua origem.
- Explicar por que o recurso é pertinente à questão.

Uma extensão disponível em um repositório não precisa ser aplicada indiscriminadamente a todos os trabalhos da Sigla.

**Pergunta central:** **adotamos essa descoberta orientada pela necessidade e pelas dependências, com explicação da pertinência e preservação da origem?**

Os índices, sinais de descoberta e mecanismos de recuperação ficam para depois.

**P07.3 — Como tratar orientações incompatíveis entre escopos?**

Uma atividade pode encontrar orientações comuns do Macro, específicas da Sigla, próprias do repositório e associadas ao Workspace. Precisamos estabelecer como agir quando elas aparentarem exigir comportamentos diferentes.

**Exemplo sintético:** uma orientação da Sigla indica um procedimento de consulta, enquanto a documentação do repositório indica outro. Pode haver uma adaptação legítima, uma condição específica, desatualização ou conflito real.

A existência de uma orientação mais específica não demonstra, sozinha, que ela resolve a incompatibilidade.

**Sugestão de comportamento:**

- Identificar as orientações, suas origens e condições de aplicação.
- Verificar se podem ser conciliadas pelo contexto ou por evidências.
- Aplicar as partes compatíveis.
- Preservar e apresentar a incompatibilidade material que continuar sem solução.
- Solicitar esclarecimento ao responsável competente quando uma decisão for necessária.
- Registrar o fundamento e o alcance da resolução.

Essa proposta se apoia no tratamento de conflitos de P03, mas ainda precisamos definir sua aplicação às extensões.

**Pergunta central:** **adotamos essa resolução por contexto, fundamento e responsabilidade competente, deixando eventual hierarquia automática de precedência para refinamento posterior?**

**Sugestão:** começar por essa abordagem, sem presumir que “o mais local sempre vence”. Também permanece distinta a autoridade para operar: uma orientação sobre como usar uma ferramenta não concede os direitos necessários à operação.

**P07.4 — Como tratar atualização, substituição ou retirada de uma extensão?**

As decisões anteriores já exigem revalidar consumidores quando o significado do conhecimento muda.

Em C-P04-07, você confirmou:

> “Quando o significado mudar, os consumidores afetados precisam ser revalidados conforme P04.1–P04.4.”

Para extensões, precisamos aplicar isso às atividades que dependem de instruções, ferramentas e comportamentos alterados.

**Exemplo sintético:** uma história foi planejada utilizando determinada operação de um MCP. Depois, o recurso é substituído ou essa operação deixa de estar disponível. A referência histórica continua explicando o planejamento anterior, mas a continuidade da tarefa precisa considerar a alteração.

**Sugestão de comportamento:**

- Identificar a mudança e o recurso afetado.
- Preservar o histórico pertinente.
- Localizar os consumidores conhecidos e avaliar o impacto.
- Informar quais orientações continuam aplicáveis.
- Atualizar ou revalidar as partes atingidas.
- Preservar o trabalho independente e identificar a ação que aguarda tratamento.

A preservação histórica continua sujeita às condições legítimas já definidas em P04.

**Pergunta central:** **adotamos esse tratamento para atualização, substituição e retirada de extensões?**

O rastreamento dos consumidores, a detecção das mudanças e a recuperação serão concretizados posteriormente.

**P07.5 — O que entregar quando o agente encontra o recurso, mas não consegue operá-lo?**

O agente pode conseguir ler uma orientação e compreender a finalidade de uma ferramenta, mas encontrar um impedimento para executar a operação necessária.

**Exemplo documental:** a documentação mostra que o integrador prepara os dados e que o ODM aplica uma regra. O agente consegue explicar essa divisão, mas não dispõe da condição necessária para consultar a regra específica no ODM.

P03/P04/P02 já orientam a continuidade independente e a apresentação das limitações. A aplicação proposta às extensões é:

- Entregar o que as fontes acessíveis sustentam.
- Identificar o recurso e a operação impedida.
- Informar o motivo conhecido.
- Explicar qual conclusão depende dessa operação.
- Indicar a evidência necessária para prosseguir, eventualmente obtida por pessoa ou recurso autorizado.
- Preservar a continuidade do trabalho independente.

**Sugestão de mensagem:** “As fontes consultadas mostram que o integrador envia estes dados ao ODM. A regra aplicada ao caso permanece sem confirmação porque a consulta necessária está indisponível. Podemos continuar esta parte independente; a conclusão sobre a regra depende da evidência indicada.”

**Pergunta central:** **esse resultado é suficiente para o caso de uma extensão conhecida cuja operação esteja impedida?**

As operações corporativas concretas, suas condições de acesso e os procedimentos de recuperação permanecem para a especificação posterior.

Você pode responder pelos IDs **P07.1 a P07.5**. Nesta rodada, as escolhas dizem respeito ao comportamento e às informações necessárias; os mecanismos continuam reservados.

---

<a id="r04-u019"></a>

## R04-U019 — Usuário

Mensagem: `01a1d67f-dd2a-7fc0-a547-0883cf0e5dc3` · turno: `01a1d67f-dcbb-7c33-85cd-b3eee41aaa6b`.

P07.1: Seguir sua sugestão: adotar esses elementos como requisitos de compreensão, diferenciando o detalhamento conforme o tipo de extensão. Os campos, arquivos e procedimentos de verificação serão definidos posteriormente.



P07.2: Seguir sua sugestão:&#x20;

- Partir da necessidade e das fontes associadas ao trabalho.
- Seguir as relações pertinentes até o escopo que oferece o recurso.
- Verificar as condições que o tornam aplicável.
- Conservar sua origem.
- Explicar por que o recurso é pertinente à questão.

Uma extensão disponível em um repositório não precisa ser aplicada indiscriminadamente a todos os trabalhos da Sigla.



P07.3: Seguir sua sugestão:&#x20;

- Identificar as orientações, suas origens e condições de aplicação.
- Verificar se podem ser conciliadas pelo contexto ou por evidências.
- Aplicar as partes compatíveis.
- Preservar e apresentar a incompatibilidade material que continuar sem solução.
- Solicitar esclarecimento ao responsável competente quando uma decisão for necessária.
- Registrar o fundamento e o alcance da resolução.

Essa proposta se apoia no tratamento de conflitos de P03, mas ainda precisamos definir sua aplicação às extensões. Começar por essa abordagem, sem presumir que “o mais local sempre vence”. Também permanece distinta a autoridade para operar: uma orientação sobre como usar uma ferramenta não concede os direitos necessários à operação.



P07.4: Seguir sua recomendação:&#x20;

- Identificar a mudança e o recurso afetado.
- Preservar o histórico pertinente.
- Localizar os consumidores conhecidos e avaliar o impacto.
- Informar quais orientações continuam aplicáveis.
- Atualizar ou revalidar as partes atingidas.
- Preservar o trabalho independente e identificar a ação que aguarda tratamento.

A preservação histórica continua sujeita às condições legítimas já definidas em P04.



P07.5: O Agente deverá explicar o contexto, a ferramenta, seus respectivos detalhes e informações, a causa do impedimento, e todos os demais dados de forma coesa, objetiva e clara, para que o engenheiro entenda faacilmente o que houve e possa interferir ou dar alguma sugestão ou solução.


---

<a id="r04-a019"></a>

## R04-A019 — Assistente

Mensagem: `msg_0e7fa371be357a1b016af76cbf2ba087d2895d3491a5c7642a` · turno: `01a1d67f-dcbb-7c33-85cd-b3eee41aaa6b`.

**As respostas encerram as cinco fichas de P07 no nível funcional desta etapa. Não identifiquei nova dúvida que exija resposta humana agora.** Permanecem os mecanismos concretos e suas demonstrações, conforme o adiamento estabelecido.

| Item | Definição consolidada |
|---|---|
| **P07.1** | Extensões devem apresentar as informações necessárias à compreensão de finalidade, origem, escopo, aplicabilidade, dependências, operações e limites, com detalhamento proporcional ao tipo. |
| **P07.2** | A descoberta parte da necessidade, percorre relações pertinentes, verifica aplicabilidade, preserva a origem e explica a pertinência. |
| **P07.3** | Incompatibilidades são examinadas por contexto e evidências; partes compatíveis podem ser aplicadas; conflitos remanescentes são apresentados e encaminhados ao responsável competente. |
| **P07.4** | Mudanças exigem identificar o recurso afetado, preservar histórico pertinente, avaliar consumidores conhecidos e atualizar ou revalidar as partes atingidas. |
| **P07.5** | O impedimento deve ser explicado de maneira suficiente para o engenheiro compreender a situação e poder intervir, sugerir uma alternativa ou fornecer uma solução. |

**Precisões importantes da análise**

Em **P07.3**, seu aceite estabelece a aplicação funcional desse tratamento às extensões. A frase “ainda precisamos definir sua aplicação às extensões” fica compreendida como detalhamento posterior dos casos e mecanismos. A lista aceita já determina a conduta esperada.

Permanece sem escolha uma hierarquia automática entre escopos. Por enquanto, a resolução segue contexto, evidências e responsabilidade competente, sem presumir que a orientação mais local prevalece.

Em **P07.5**, sua resposta acrescenta uma exigência de comunicação: o agente deve tornar o impedimento compreensível e útil à intervenção do engenheiro.

Essa explicação deverá reunir, conforme pertinente:

- Contexto e objetivo do trabalho.
- Ferramenta e operação envolvidas.
- O que foi efetivamente observado.
- Causa demonstrada ou indicação de que ela ainda não foi determinada.
- Consequências para a tarefa.
- Informações necessárias à intervenção.
- Trabalho independente que pode continuar e condição para retomar a parte impedida.

**Exemplo:** o agente conhece a ferramenta, mas uma consulta falha. Deve explicar a operação, o resultado observado e seu impacto. Se a causa não estiver comprovada, apresenta essa limitação e qual informação ajudaria a esclarecê-la.

A possibilidade de intervenção humana não altera a regra já aceita de continuidade do trabalho independente.

**Pendências mantidas para refinamento posterior**

1. **Representação das extensões:** campos, arquivos, formatos, identificadores e instruções específicas.
2. **Descoberta e aplicabilidade:** índices, relações, recuperação gradual e verificação das condições de uso.
3. **Conflitos:** exemplos concretos, identificação do responsável conforme o assunto e eventual proposta de precedência automática.
4. **Manutenção:** detecção de mudanças, rastreamento de consumidores, atualização, retirada e recuperação.
5. **Operação e comunicação:** contratos reais, condições de acesso, tratamento de falhas e apresentação dos impedimentos.
6. **Demonstração:** cenários e avaliações futuras conduzidos por agentes, seguindo o encaminhamento de P03.

**P07 pode ser encerrado nesta etapa de levantamento e definição**, conservando essas pendências de concretização. As definições permanecem nesta conversa; ainda não foram persistidas no GitHub.
