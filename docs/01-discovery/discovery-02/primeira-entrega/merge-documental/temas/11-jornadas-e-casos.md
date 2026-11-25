# Jornadas para testar o que a plataforma pode explicar

Cada jornada identifica uma pergunta, a evidência que permitiria responder e o limite do resultado. Alfa e Beta são exemplos sintéticos. J01–J09 são percursos propostos em F4. Os relatos sobre homologação conservam sua natureza de relato na fonte autorizada. As demonstrações abaixo empregam componentes fictícios e deixam aberta a comprovação operacional.

<a id="casos"></a>
## Três sistemas no desenho não significam três sistemas investigados

Em Alfa/Beta (F1), Alfa recebe uma proposta, valida campos e publica um evento somente sob uma condição de canal. Beta consome o evento e consulta um serviço externo. A evidência nos dois repositórios pode sustentar a emissão condicionada e o contrato de delegação. Para explicar a política externa de elegibilidade, falta a fonte do outro lado. A comparação de duas respostas exige preservar canal, contrato, revisão e público.

O adendo D02-ESP-001 r1 descreve A e B em Siglas distintas e C fora da seleção. O critério proposto é recuperar o contrato pertinente sem carregar toda a documentação das duas Siglas, registrar a cobertura e explicar por que incluir C ajudaria a questão atual. O agente sugere com a lacuna, revisão conhecida, direitos necessários e consequência de prosseguir com a parte independente. O engenheiro decide a inclusão. Vincular Sigla tem autoridade distinta. O cenário D02 de Micro-A/Micro-B emprega revisões, lacuna e teste inconclusivo próprios. Os três casos permitem comparar o raciocínio e permanecem cenários distintos. [Fronteira do produtor](03-onboarding-e-compreensao.md#fronteira).

Fontes da passagem · A11-001–003, A11-012, A12-003, D02-ESP-001 r1, edição de S2 · [MODELO-FUNCIONAL, L43–45](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MODELO-FUNCIONAL.md#L43-L45) · [MOTOR-E-WORKSPACES-DE-ATIVIDADE, L28–31](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L28-L31).

<a id="inventario"></a>
## J01. Onboarding de entradas heterogêneas

Um engenheiro indica três repositórios e revisões, por exemplo um serviço Java/Spring, um consumidor Kotlin/Kafka e uma definição Terraform. O motor inventaria configurações e builds, localiza símbolos e confronta a documentação preliminar com contratos e evidências de relação. Se o grafo apenas sugere uma ligação entre serviço e infraestrutura, informe a lacuna e sua consequência assim que aparecer. O resultado esperado é um Micro por entrada e um Meso para o conjunto sustentado, com cobertura e estado real de publicação. O onboarding preserva a aplicação. Uma relação inferida não deve virar aresta confirmada na vista.

Fontes da passagem · A11-004 · [BASE-P03-HUM, L46–64](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L46-L64).

<a id="campo"></a>
## J02. É possível retirar um campo de evento?

Na revisão examinada, o emissor envia o campo sintético `categoriaEvento` e há evidência do tratamento dado pelo receptor conhecido. O impacto de retirar o campo ainda precisa ser verificado. Um possível terceiro consumidor está fora do recorte. A busca recupera direção da relação, contrato e revisões, eventual pendência e os direitos de divulgação. O produtor pode explicar o que envia e o receptor investigado pode explicar como trata ausência. Antes de retirar o campo, ainda falta a evidência pertinente do outro receptor ou a delimitação do trabalho à parte independente. Se até a existência do terceiro for restrita, ajuste a comunicação ao público.

Fontes da passagem · A11-005 · [BASE-P03-HUM, L66–75](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L66-L75).

<a id="duplicidade"></a>
## J03. Reenvio, duplicidade ou duas solicitações legítimas?

O Analista pergunta em quais situações reprocessar uma solicitação poderia criar uma duplicidade. As investigações propostas confrontam identidade e canal de negócio, contratos e tratamento técnico, concorrência, timeout, recuperação e o caso de duas solicitações legítimas. O coordenador agrega as dúvidas antes de as reapresentar à pessoa competente. Uma explicação pode vir de qualquer pessoa com conhecimento pertinente. O aceite do refinamento pertence ao humano com competência para aquele objeto. Criar história ou gravar no sistema de trabalho demanda a autorização correspondente.

Fontes da passagem · A11-006 · [CADERNO-P09, L206–216](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/fontes/CADERNO-P09.md#L206-L216).

<a id="timeout"></a>
## J04. Alterar um timeout para dez segundos

Comece pela configuração e pelos consumidores relevantes. Verifique retry, backoff, política de falha e compromisso de latência quando puderem mudar o efeito. Uma investigação curta pode bastar. Paralelizar só faz sentido quando há perguntas verificáveis independentes que compensem o custo. Se persistir conflito com o contrato, apresente a divergência antes da alteração. Uma operação que falhou e um contrato cujo significado ainda está em aberto devem ter registros distintos.

Fontes da passagem · A11-007 · [REGISTRO-DECISOES, L962–975](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L962-L975).

<a id="servicos"></a>
## J05. Evolução coordenada em dois serviços

A jornada futura parte de especificação validada, plano aceito e permissão específica para implementar. Cada implementador recebe seu escopo. O revisor confronta diffs com a especificação e a integração reconcilia contratos e testes entre serviços. Uma falha impede a promoção da parcela afetada e permite conservar trabalho independente. Antes de push, o conhecimento afetado precisa de atualização ou revalidação vinculada ao candidato exato. Uma nova edição do candidato invalida a prova que dependia dos bytes anteriores. Um teste local só demonstra a operação executada no ambiente examinado.

Fontes da passagem · A11-008 · [BASE-P03-HUM, L81–87](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L81-L87).

<a id="delegacao"></a>
## J06. O consumidor envia uma pergunta a um motor de regras

A monta a solicitação, um serviço de decisão seleciona os identificadores e A despacha o que recebeu. O código de A pode sustentar a montagem, o mapeamento, a reação a falha e o despacho. A efetiva seleção de identificadores para uma entrada exige evidência própria do recurso externo, da revisão e das condições. O total de destinos possíveis não determina quantos o recurso retornou. Parâmetros, procedimentos, configuração externa e eventos podem determinar o resultado em outros exemplos.

A navegação Micro/Meso pode localizar um contrato ou uma referência a um mecanismo especializado. É preciso verificar se aquela modalidade, ambiente e identidade têm acesso legítimo para a operação pertinente. A existência de um conector configurado não comprova leitura, execução ou versão em uso.

Fontes da passagem · A11-009, F4-L2612 · [REGISTRO-DECISOES, L892–904](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L892-L904) · [P04-CONSOLIDADO, L25–29](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L25-L29).

<a id="mudancas"></a>
## J07–J09. Revisão, nova exceção e acesso parcial

| Jornada | O que precisa sobreviver na passagem para o próximo leitor |
|---|---|
| J07. Uma assinatura ou erro mudou de a1 para a2 | As conclusões em a1 conservam valor histórico. Trace o impacto nas unidades, consumidores, testes, Micros, Meso e Workspaces. Revalide a parte atingida antes de restabelecer seu uso atual. |
| J08. Surge uma exceção por canal durante o planejamento | Preserve a declaração, autoridade, alcance e evidências. Localize histórias, critérios, opções e testes afetados. Retorne à aprovação aplicável quando o novo entendimento mudar o que havia sido aceito. |
| J09. Pesquisa entre Siglas com material restrito | Use somente os índices, contratos e relações permitidos. Se C estiver fora do alcance, informe o limite divulgável. Inacessibilidade não comprova inexistência. Inclusão na atividade e leitura do conteúdo são independentes. |

As nove jornadas constituem uma série de exemplos de F4. Identificadores de autoria e cabeçalhos no original situam a respectiva passagem. O relato que as sucede introduz outro objeto de investigação e conserva sua origem própria.

Fontes da passagem · A11-010–012, U088 · [P04-CONSOLIDADO, L27–38](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L38) · [MODELO-FUNCIONAL, L43–45](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/MODELO-FUNCIONAL.md#L43-L45).

<a id="procedimento"></a>
## Conhecer um procedimento de teste não concede permissão para executá-lo

Em uma reprodução sintética, B prepara dados fictícios de teste e fornece um identificador a A. A ligação operacional pode ser conhecida pelo engenheiro antes de aparecer no código de A. O que B implementa pertence ao Micro de B quando sustentado. A relação com A deve indicar direção, origem, revisão e condições. Um procedimento versionado pode explicar como preparar um cenário, sob quais pré-requisitos e como verificar o resultado. Transformá-lo em skill dependeria de aprovação e de demonstrar utilidade para reúso.

A depender da autoridade, o agente pode orientar, preparar um plano ou executar só a operação especificamente autorizada. O relato sobre um teste realizado em outro contexto não demonstra a correspondência sistemática entre identificador e resultado nem autoriza usar dados reais. Fora de Workspace, permanecem em aberto o responsável por autorizar incorporação, o destino primário e o público do novo entendimento. A granularidade do procedimento, a conservação de dados e as verificações exigem refinamento. [Questão de competência](05-evidencias-e-memoria.md#sem-atividade).

Fontes da passagem · A11-013–015, U086 · [BASE-P03-HUM, L77–91](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L77-L91) · [REGISTRO-DECISOES, L1088–1100](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L1088-L1100).

<a id="metodos"></a>
## Como verificar uma decisão externa

Para um exemplo fictício de delegação a um motor de regras, separe fluxo e categoria enviados, identificadores devolvidos e despacho local. Investigue retornos vazios, desconhecidos, duplicados, erro e ausência de ação conforme a evidência disponível. O contrato ilustrativo preserva a diferença entre como A usa o identificador recebido e por que o motor escolhe devolvê-lo. O desenho permite comparar meios de verificação sem operar um serviço real.

| Meio | Escopo e condição |
|---|---|
| Código do consumidor e contratos | Descrevem montagem, tratamento esperado, falha e despacho naquela revisão. |
| Mocks e testes existentes | Delimitam casos e resultados simulados. O comportamento do recurso externo requer outra prova. |
| Exportação versionada ou tabela de regras | Demonstra o declarado naquela versão. Para atribuí-la a um ambiente, verificar a implantação correspondente. |
| Explicação de especialista | Registrar procedência, condições, limites e eventuais divergências. A execução não decorre da declaração. |
| Rastros ou observações permitidos | Sustentam a ocorrência identificada no ambiente, versão e entradas documentados. |
| Simulação ou chamada controlada | Precisam de ambiente, credenciais, entrada sintética e autorização para aquela operação e efeitos. Uma chamada de leitura aparente também pode produzir efeitos. |

Se a pergunta for apenas sobre o despacho local, o motor pode entregar a parcela sustentada com ressalva. Para alterar a política de seleção, apresente a evidência adicional exigida. [Investigação adaptativa](06-investigacao-e-contexto.md#parada).

Fontes da passagem · A11-016–018, U087 · [REGISTRO-DECISOES, L892–904](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L892-L904) · [BASE-P03-HUM, L66–75](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L66-L75).

<a id="ensaio"></a>
## Experimento de memória entre pessoas, máquinas e clientes

Uma pessoa registra a investigação com pergunta, significado, fontes principais, condições, composição e percurso verificável. Ela publica quando autorizada. Outra pessoa sincroniza a revisão em outra máquina, reconstrói o índice, troca de cliente ou agente e reformula a pergunta. Confira que a investigação recuperada é a pertinente e que as condições ainda permitem usar cada afirmação.

No catálogo F3, CA01 exercita a paráfrase, CA06 a recuperação na segunda máquina, CA18 a troca de agente ou modalidade e CA24 a troca combinada de pessoa, máquina e cliente. Varie também canal ou negação para testar a rejeição em CA02. Para CA22, altere uma dependência e exija que a resposta distinga a parte reaproveitada, a revalidada e a pendente. O tempo total e a correção do reúso precisam ser observados no ensaio. Esses critérios pertencem a F3 e permanecem propostos, distintos dos cenários visuais e dos 49 critérios operacionais da fundação. [Condições de reúso](05-evidencias-e-memoria.md#reuso) · [Avaliação e evidências](12-avaliacao-riscos-e-provas.md).

Fontes da passagem · A11-019–020 · [REGISTRO-DECISOES, L228–258](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L228-L258).

[Voltar à entrada de discovery](../README.md)
