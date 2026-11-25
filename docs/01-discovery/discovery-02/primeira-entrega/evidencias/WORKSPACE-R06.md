# Workspace de Atividades · referência da revisão R06

Esta síntese reúne as definições da revisão R06 do caderno de Workspace necessárias para interpretar a primeira entrega. O caderno original mantém as fontes das rodadas, a matriz de rastreabilidade e o histórico de retificações. Os identificadores abaixo preservam o vínculo com esses registros. [Escopo da primeira entrega](../ESCOPO.md) · [Índice do pacote](../README.md)

## Atividade, estado e localização

O Workspace é o contexto no qual Negócios, Tech Lead e analistas técnicos refinam uma atividade. **Atividade** é o conjunto de histórias e tasks em que o Workspace trabalha. A pasta do Workspace conserva o estado desse trabalho, desde as fontes recebidas até hipóteses, requisitos, decisões e pendências. Por exemplo, a equipe pode fornecer uma transcrição de reunião e pedir que seja guardada para o refinamento. O estado registrado na pasta, a revisão do código nas aplicações e o status de cada história no sistema corporativo podem evoluir separadamente. Origem documental em `WS-F01/S1`, `WS-P02`, `WS-P03` e `WS4-P02`.

| Onde | Regra da R06 |
|---|---|
| Área de trabalho local | A pasta `workspaces/` fica na raiz da área local. Essa área reúne também as Siglas e os recursos usados pela Plataforma, como skills, MCPs, documentação, instruções e ferramentas. A localização interna desses recursos continua para detalhamento. `WS-P03` |
| Repositório Git a usar | Cada Sigla possui um repositório que reúne seus Workspaces. A branch da atividade é criada no repositório da **Sigla do time ou analista executor**. O agente pergunta e o Engenheiro informa a Sigla, mesmo quando as aplicações envolvidas pertencem a outras. `WS-P01`, `WS6-F01`, `WS6-D01` |
| Branch em trabalho | Uma branch dedicada a cada Workspace contém na raiz a pasta daquela atividade e nenhum outro Workspace. Um repositório por Workspace foi uma hipótese anterior, substituída por `WS-P01`. |
| Encerramento | Ao concluir a atividade, o time escolhe excluir a branch ou arquivar a pasta em `workspaces/` na `main` do repositório de Workspaces. A aprovação do refinamento acontece em outro momento. `WS-P01`, `WS-P08` |

## Como o agente consulta e como se decide um vínculo

Para responder a um pedido, o agente parte do material já associado à atividade. Se for insuficiente, procura pistas no pedido, consulta as bases e os índices pertinentes das Siglas e chega aos repositórios relacionados. Quando persistir uma lacuna, pede à **pessoa solicitante** o esclarecimento que falta e retoma a investigação. Esse percurso, descrito em `WS-F01/S1`, permite consultar informação antes de propor incorporá-la à atividade.

| Objeto | O que foi definido | Fonte |
|---|---|---|
| Repositório | O agente sugere a inclusão de um repositório mapeado pertinente. O Engenheiro decide e, se permitir, o agente efetua a inclusão como submódulo. A escrita no código exige a autoridade correspondente. | `E-001`, `WS-F01/S2`, `WS-P01`, `WS-P05` |
| Sigla | O agente sugere, o Analista permite e o vínculo torna seus índices consultáveis. Os repositórios da Sigla continuam sujeitos à seleção individual. | `WS-P05`, `WS4-P04` |
| Outro Workspace | Uma atividade pode consultar outra para obter histórico ou entendimento. Os itens conservam seu pertencimento original e o acesso depende dos direitos efetivos sobre o material. | `WS4-P05` |

## Do refinamento ao trabalho nas aplicações

Uma feature pode participar de vários Workspaces. Cada história, task, subtask ou bug pertence a um único Workspace. O Analista, de negócios ou não, aprova formalmente a conclusão do refinamento no escopo especificado. Pode fazê-lo por iniciativa própria ou após uma pergunta do agente. Depois disso, criam-se as histórias e elas são associadas às features. A Plataforma usará o ServiceNow/IUClick para **criar, modificar e alterar o status de histórias**. Mecanismos técnicos, transições e permissões serão especificados nos Discoveries pertinentes. A aprovação do refinamento não autoriza por si só uma dessas escritas. Origens em `WS-P04`, `WS-P06`, `WS-P08`, `WS4-P02` e `WS4-P03`.

## O que a revisão encerrou e o que segue em aberto

`WS4-P01` foi encerrada pela resposta `WS6-F01`, tratada em `WS6-D01`. Está definido quem fornece a Sigla e em qual repositório a branch será criada. Para este recorte da R06, continuam para o Discovery pertinente o sinal de término do conjunto de histórias e tasks, caso precise ser representado, a execução material do vínculo de uma Sigla já permitido pelo Analista, os controles específicos de acesso ao histórico, o layout interno dos dados, a inicialização da Plataforma e os contratos de integração corporativa. A R06 tampouco decide se o repositório de Workspaces e o de conhecimento Meso são fisicamente o mesmo repositório.

**Mapa para conferir o caderno de origem.** Na área `revisao_R06/`, a síntese funcional está em `documentos/03_workspaces_de_atividade.md`. As respostas estão em `resposta_workspace.md`, `respostas_workspace_R04.md`, `respostas_workspace_R05.md` e `resposta_workspace_R06.md`. O tratamento das respostas e a precedência entre rodadas estão em `registro_de_decisoes.md` e `registro_de_pendencias.md`.
