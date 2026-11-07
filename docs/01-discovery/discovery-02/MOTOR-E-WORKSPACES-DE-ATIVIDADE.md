# Motor de Onboarding e workspaces de atividade

**Registro:** D02-ESP-001 · **Revisão:** 1 · **Data:** 07/11/2026 · **Estado:** especificação funcional em Discovery, publicada para revisão. Este adendo delimita o recorte inicial do motor e a relação com o workspace futuro. Os critérios observáveis abaixo são uma tradução funcional da relação e continuam sujeitos ao refinamento de D02-PEN-001/002.

## Proveniência

- **Direção direta do usuário nesta conversa.** Priorizar a entrega de um motor na máquina de trabalho que obtenha os repositórios GitHub especificados e produza bases de conhecimento por repositório e por Sigla. Incorporar às especificações a relação apresentada entre esse motor e os workspaces de atividade.
- **Fonte documental de produto.** [03_workspaces_de_atividade.md](https://chatgpt.com/space/file/libfile_bf76604522208191a034a3b222a85db8), §§1–4, com destaque para P-008 (forma e relação estrutural ainda abertas) e P-009/E-001 (decisão de inclusão pelo engenheiro). A fonte descreve a seleção por atividade como proposta. O vínculo privado identifica a origem documental.
- **Base do Discovery.** [Registro D02](REGISTRO.md) HUM-01/02/04/05/06/08/09, [Registro D01](../discovery-01/REGISTRO.md) sobre Git canônico, revisões por ambiente e pendências, e [AX-06 a AX-08](../../fundacao/axiomas-arquiteturais.md#ax-06). Base da proposta: `8bbd93151640865995fa8a8dfe3d2d5db15da6ec`.

## Fronteiras da primeira entrega

| Escopo | Função |
|---|---|
| Hierarquia do conhecimento | Micro é o repositório individual. Meso é o repositório Git da Sigla/conta, com os Micro como submódulos. Macro é a raiz Git com os Meso como submódulos, prevista na topologia mais ampla. |
| Execução do motor | O engenheiro especifica os repositórios. O motor obtém e analisa o material autorizado e produz bases Micro e Meso. A base Meso explicita o conjunto efetivamente analisado e as lacunas de cobertura. |
| Workspace de atividade | O engenheiro reúne os repositórios pertinentes a uma demanda. A seleção pode atravessar Siglas e reaproveita o conhecimento produzido pelo motor. A forma do workspace, sua relação estrutural com a hierarquia e a existência de estado próprio continuam em aberto. |

A primeira entrega tem como saídas as bases Micro e Meso. A seleção de conhecimento para uma tarefa é o uso futuro dessas saídas. O motor deve preservar a distinção entre pertencimento organizacional a uma Sigla e relação técnica entre componentes. A primeira relação orienta a consolidação Meso. A segunda orienta a investigação de fluxos, dependências e contratos, inclusive entre Siglas.

## Comportamento funcional

1. **Delimitar e registrar cobertura.** Associar o conhecimento ao repositório e à revisão Git analisada. Tornar explícitos o material lido, o escopo parcial da Sigla, as fontes inacessíveis e as pendências que afetam o uso. Um commit conhecido e uma implantação em determinado ambiente são evidências distintas.
2. **Produzir conhecimento reutilizável.** Permitir localizar conhecimento por repositório, revisão, evidência e relação técnica. A base Micro orienta a navegação até as fontes. A base Meso consolida a visão do conjunto analisado e aponta para os Micro relevantes. No uso por atividade, a seleção recupera o contexto suficiente para a tarefa, incluindo evidências, contratos e pendências que alterem seu resultado.
3. **Registrar relações que ultrapassam o escopo.** Uma fonte analisada pode evidenciar uma dependência de outro repositório. Registrar a origem da evidência e distinguir o que ela sustenta do que depende de investigar o outro lado. A descoberta de uma relação, a inclusão no workspace e a autorização de leitura são decisões distintas. Para uma atividade, o agente sugere a inclusão de um repositório relacionado já mapeado, e o engenheiro decide. Valem as fronteiras de permissão e a vedação de refatoração no onboarding definidas no D02.
4. **Preservar a validade das referências.** Quando uma mudança afetar o conhecimento, aplicar a direção de atualização e revalidação de HUM-08. O recorte inicial deve permitir identificar a revisão analisada e a evidência usada. Os gatilhos e mecanismos de atualização da primeira entrega serão especificados separadamente.

## Verificação funcional candidata

Em um cenário sintético, A e B pertencem a Siglas diferentes e são os repositórios indicados para onboarding. Uma fonte de A evidencia uma dependência de C, fora do conjunto indicado. Espera-se que as bases registrem a cobertura de A e B e a evidência sobre C com seus limites. Uma atividade que consuma essas bases deve conseguir localizar o contrato relevante sem carregar toda a documentação das duas Siglas. Se C já estiver mapeado e for pertinente, o agente pode sugerir sua inclusão, explicando por que ela ajudaria. Cabe ao engenheiro decidir. Esse cenário descreve um critério a validar, sem resultado de execução.

## Em aberto

- Forma de informar repositórios, Siglas e revisões e como representar cobertura incompleta e dependências entre Siglas.
- Formato das bases, índices, granularidade das evidências e critérios de compreensão suficiente.
- Se o workspace contém referências, conteúdo próprio ou estado de atividade, e como apresentar a seleção, a sugestão de inclusão e as lacunas ao engenheiro.
- Alcance da primeira entrega quanto à atualização incremental, autenticação e publicação remota.
