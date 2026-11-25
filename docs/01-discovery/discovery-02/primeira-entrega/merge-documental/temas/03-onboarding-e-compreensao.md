# Que conhecimento o onboarding entrega?

O Motor produz conhecimento para um repositório em uma revisão identificada (Micro) e para as relações efetivamente examinadas na Sigla ou conta (Meso). Quando o engenheiro precisa decidir sobre uma alteração, pode partir dessas entregas e saber até onde teve cobertura. A primeira entrega prioriza o motor. Interface própria, mecanismos de indexação e medições comparativas seguem em refinamento.

<a id="produtor"></a>
## Produzir o conhecimento e depois consumi-lo

O onboarding começa por um objeto e um estado cuja investigação foi autorizada, mesmo sem uma pergunta sobre aquele código. Preserva a aplicação. A descoberta pode melhorar a documentação e apontar uma oportunidade de mudança, mas refatorar o código fica fora do onboarding. O Meso referencia os Micros como submódulos e o Macro referencia os Mesos. A mesma Sigla pode agrupar componentes sem dependência técnica entre si.

O consumidor entra depois, com uma tarefa, um público e uma composição particulares. Procura o trecho pertinente do Micro pelo Meso, recupera condições e volta às fontes se o novo objetivo as exigir. Uma consulta bem-sucedida ajuda a avaliar utilidade. Os critérios de conclusão do produtor dizem respeito ao conhecimento que ele entregou e à sua cobertura. O histórico da revisão e o registro de um teste permitem recuperar o que foi observado naquela ocasião. Uma execução na composição atual precisa de prova própria. [Reutilização parcial](05-evidencias-e-memoria.md#reuso).

Fontes da passagem · A03-001–003, U022, U025 · [MOTOR-E-WORKSPACES-DE-ATIVIDADE, L13–26](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L13-L26) · [BASE-P03-HUM, L52–64](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L52-L64).

<a id="entrada"></a>
## Fixar a entrada e a cobertura examinada

Identifique repositório, Sigla, revisão, diretório e filtros, alterações locais relevantes, escopo de leitura, destino permitido e finalidade. Em um repositório híbrido, caracterize cada subsistema pela sua organização, linguagens, configurações, integrações, acervo existente, direitos, limitações dos analisadores e significado de negócio. Build, contrato, infraestrutura declarada, testes e documentação podem oferecer entradas diferentes. Um termo repetido em duas Siglas exige evidência de que tem o mesmo significado. O engenheiro pode dar as informações na forma disponível.

A cobertura discrimina o material localizado, lido, inacessível e fora da entrada. Uma branch móvel requer a revisão observada. A leitura de um módulo deixa os demais identificados no saldo. O adendo Motor e Workspaces distingue, em sua edição r1, a produção do Micro/Meso e a recuperação da parcela necessária à atividade. Na manutenção, DEC-017 acrescenta a busca dos consumidores afetados. DEC-018 conserva para demonstração futura a comparação concreta entre Micro e Meso. O critério de qualidade requer série de evidências por revisão, material lido, limites e questões abertas.

Fontes da passagem · A03-004–006, A03-010, A07-003, A07-007, U023, D02-ESP-001 r1, edição de S2 · [BASE-P03-HUM, L52–55](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L52-L55) · [MOTOR-E-WORKSPACES-DE-ATIVIDADE, L13–30](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L13-L30).

<a id="capacidades"></a>
## Escolher evidências e capacidades por subsistema

Um termo exato pode bastar para localizar um evento. Navegação simbólica localiza a declaração e os chamadores. Uma análise de relações pode sugerir o consumidor. A explicação precisa reconstruir entradas, condições, alternativas, exceções, efeitos e caminhos em que nada acontece. Uma lacuna do parser ou uma aresta ausente em um grafo parcial pede outra fonte. Se duas ferramentas fazem a mesma indexação, justifique o custo pela cobertura adicional ou pelo que um método verifica independentemente. Empacotamento de texto, por exemplo com Repomix, pode ajudar o transporte e ainda exigir seleção do trecho pertinente.

Para ONB-RF-01, a proposta distingue o recurso anunciado, sua configuração, seu acesso real e uma demonstração da operação na modalidade examinada. Uma integração anunciada para Web pode estar instalada na CLI e mesmo assim não abrir o arquivo produzido. Registre cliente, modo, versão observável, operação, resultado e limitações. Na preparação proposta em F1, ONB-RF-01–04 ligam essa disponibilidade à caracterização revisável do repositório, à justificativa de compor capacidades e à identidade exata da entrada. Uma ferramenta com o mesmo índice pode valer o custo quando cobre outra linguagem ou oferece verificação independente. Ao entregar, identifique quais capacidades sustentaram a conclusão e quais componentes do Meso ficaram fora.

Fontes da passagem · A03-007–010, U019, F1-P106 · [BASE-P03-HUM, L52–60](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L52-L60) · [BASE-P03-HUM, L46–60](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L46-L60).

<a id="formatos"></a>
## De saída de ferramenta a afirmação verificável

Cada afirmação identifica seu objeto, origem principal, revisão e localizador preciso. Para código, preserve símbolo, componente, arquivo e convenção de linha, coluna ou byte. O contrato declara um comportamento. Teste ou observação sustenta um resultado nas condições e na revisão examinadas. A apresentação pode normalizar essas fontes mantendo sua origem editável, formatos especializados, condições, limites, divergências e relações entre derivados.

Uma ponte precisa interpretar entrada, saída, retorno vazio, erro e leitura parcial conforme o contrato da ferramenta. Abrir só o cabeçalho, receber um caminho local em cliente remoto ou gerar um resumo de outro resumo exige explicitar o alcance. Duas sínteses do mesmo grafo compartilham a origem do fato. Uma delas ainda pode revelar uma exceção ou acrescentar uma verificação independente identificável. Se a discordância for sobre revisão, filtro, ambiente ou método, conserve as posições e a conclusão dependente até poder explicar a diferença. Na transformação, confira que direção, negação, condição e revisão sobreviveram. Aprofunde quando uma dessas diferenças alterar o resultado. Registre o custo e as fronteiras da investigação para que o consumidor consiga decidir se precisa de mais evidência.

Fontes da passagem · A03-012–013, U020, U021 · [REGISTRO-DECISOES, L850–862](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L850-L862) · [BASE-P03-HUM, L46–60](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L46-L60).

<a id="codewiki"></a>
## Identidade da ferramenta no estudo visual

Três registros alimentam perguntas diferentes. O catálogo F2 relata documentos por repositório e uma visão combinada usada para diagramas. F1 relata separadamente um teste breve sem artefatos suficientes para reproduzi-lo. F1 também estuda um projeto público identificado como FSoft-AI4Code/CodeWiki. Antes de atribuir o resultado visual ou o teste local a esse projeto, seria preciso identificar a distribuição e versão usadas, os insumos, a configuração e as saídas. A comparação de qualidade, tempo e custo por tarefa e modalidade permanece futura. [Critérios para vistas](09-documentacao-visual.md).

Fontes da passagem · A03-011 · [REGISTRO-DECISOES, L228–258](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L228-L258).

<a id="fronteira"></a>
## Documentar o lado observado de uma relação

No exemplo sintético de F1, Alfa valida uma proposta e emite um evento sob condição de canal. Beta o consome e delega uma decisão a outro serviço. É possível explicar a condição de Alfa, o contrato e a chamada de Beta. A política do serviço externo depende de sua própria evidência. No caso ilustrativo de um motor de regras que retorna identificadores para despacho, compreender a montagem e o tratamento do retorno pode bastar para explicar a aplicação local. Alterar a seleção exigiria uma evidência pertinente da versão e das regras externas.

Para incluir outro repositório na atividade, o agente explica o indício, o que falta, a revisão se conhecida, os direitos necessários, as limitações remanescentes e como continuaria. O engenheiro decide a inclusão e sua decisão fica registrada. Observar a dependência, incluir o repositório e obter leitura do outro lado são atos distintos. O vínculo da Sigla tem competência própria do Analista. A documentação da Solução tem repositório próprio e escopo delimitado pelo Analista com auxílio do agente. Esses atos conservam seus respectivos objetos. [Composição da atividade](02-camadas-e-workspaces.md) · [Jornadas de fronteira](11-jornadas-e-casos.md#casos).

Fontes da passagem · A03-014–015 · [MOTOR-E-WORKSPACES-DE-ATIVIDADE, L21–30](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L21-L30) · [BASE-P03-HUM, L66–75](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L66-L75).

<a id="conclusao"></a>
## Quando concluir a produção ou pedir esclarecimento

Os sete critérios de P03 cobrem a identificação da entrada e do estado, a cobertura da descoberta, a explicação dos comportamentos materiais, a consolidação de conhecimento válido, a rastreabilidade e coerência nos dois sentidos, o tratamento de lacunas e a entrega dos artefatos no estado real. Condições, alternativas, efeitos, exceções e ausências de ação fazem parte da explicação.

| Estado do produtor | Evidência e consequência |
|---|---|
| Concluído no recorte | Os sete critérios aplicáveis podem ser demonstrados para a entrada identificada. |
| Concluído com ressalvas | A cobertura e a fidelidade ainda se sustentam, a fronteira tem evidência e as lacunas estão delimitadas. |
| Parcial ou impedido | Falta uma evidência indispensável. Entregue as parcelas comprovadamente independentes e identifique a decisão impedida. |
| Aguardando esclarecimento | A investigação autorizada deixou dúvida sobre a criticidade de uma lacuna. Apresente o que já foi confrontado e a pergunta que pode resolvê-la. |

A forma de exibir os estados é proposta. Se mudar uma dependência, suspenda a validade atingida. Uma ferramenta opcional que falhou pode ceder lugar a outra fonte adequada. Uma falha de controle obrigatório suspende a operação dependente. Se o artefato não chegou ao destino, indique o estado da entrega.

Fontes da passagem · A03-016–020, U024 · [BASE-P03-HUM, L46–64](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L46-L64).

<a id="aviso"></a>
## Avisar o engenheiro e reabrir os consumidores

Comunique a lacuna material assim que aparecer. Localize a fonte, explique a consequência para a atividade e o que permitiria prosseguir. Quem recuperar uma conclusão dependente deve encontrar a mesma ressalva. Um processamento encerrado pode ter produzido material ainda por verificar. Um conhecimento validado pode continuar apenas local. Um arquivo publicado pode perder atualidade. D02-PEN-001/002 e ONB-PEN-03/04 conservam o refinamento das evidências de compreensão suficiente e de como apresentar uma lacuna ao engenheiro.

Ao detectar alteração material, identifique o que dependia da premissa, impeça seu uso como atual, reconcilie e verifique antes de restaurar a validade. Sem monitoramento comprovado, a detecção ocorre na leitura ou ciclo seguinte. Uma mudança agêntica revalida ou atualiza o conhecimento no mesmo ciclo de commit/PR. O push de trabalho registra a revisão enviada. A aprovação do conteúdo mantém seu próprio fundamento. [Validade por afirmação](07-validade-acesso-e-publicacao.md#drift).

Fontes da passagem · A03-021–022 · [REGISTRO, L125–133](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/REGISTRO.md#L125-L133) · [REGISTRO, L81–88](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/REGISTRO.md#L81-L88).

[Voltar à entrada de discovery](../README.md)
