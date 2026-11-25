# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](../consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](../consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](../consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Atuação do agente por etapa na primeira entrega

**Revisão 1 · Direção de produto em Discovery.** A primeira entrega da Plataforma deve orquestrar como o agente interpreta uma mensagem, investiga o assunto, atua e responde conforme a etapa e o objetivo da atividade no Workspace. O usuário requer essa capacidade já na primeira entrega e pede que a orquestração seja consistente, clara, detalhada e resiliente. O termo *papel* descreve aqui a atuação esperada naquele momento. A quantidade de agentes, a distribuição de responsabilidades técnicas e o mecanismo de orquestração continuam em refinamento.

## Alcance da decisão

O trabalho inclui refinar questões de negócio e produto, definir requisitos e funcionalidades e criar ou detalhar histórias, tasks, subtasks e bugs. Abrange também o planejamento de arquitetura e software, incluindo criar recursos AWS e repositórios, estabelecer relações entre eles, modificar aplicações existentes e planejar testes e validações. O planejamento pode descrever ações concretas e suas dependências. Sua execução efetiva em repositórios, sistemas corporativos ou ambientes AWS continua sujeita à especificação e às autorizações correspondentes.

A referência do Motor já define a produção de conhecimento Micro e Meso. O Workspace utiliza o conhecimento pertinente para refinar a atividade. Esta manifestação explicita uma capacidade da primeira entrega da **Plataforma**. A alocação dessa responsabilidade entre o Motor, o Workspace e outros componentes permanece aberta. [Retomada do Motor e da Arquitetura](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md)

## Como perceber a diferença de atuação

Considere a mensagem sintética **“O mesmo pedido de abertura não pode gerar duas contas.”** A tabela exemplifica comportamentos que poderão ser avaliados. Os nomes das etapas e as respostas abaixo são propostas de refinamento.

| Trabalho em curso | O que o agente procura esclarecer ou produzir |
|---|---|
| Refinar a regra de negócio | Esclarecer o que identifica o mesmo pedido e o que distingue uma repetição de um novo pedido legítimo. Se isso estiver indefinido, registrar a dúvida e seu impacto. |
| Definir a história | Usar a definição acordada para redigir o comportamento esperado e critérios de aceite observáveis. Registrar as subtasks que já puderem ser justificadas. Se houver relato de defeito, distinguir o resultado esperado do comportamento efetivamente observado. |
| Planejar arquitetura e software | Localizar onde o pedido é identificado e quais repositórios e contratos participam da abertura. Investigar em quais pontos uma repetição pode ocorrer. Planejar alterações nos componentes afetados e, se a análise justificar, a criação de recursos AWS ou repositórios. |
| Planejar testes e validações | Descrever como verificar que o reenvio de um pedido que já abriu uma conta não cria outra e que dois pedidos legítimos continuam distinguíveis. Indicar qual evidência permitiria conferir cada resultado. |

## Pontos para o Discovery da orquestração

1. **Identificação e transição de etapa.** Especificar de quais sinais o agente dispõe para reconhecer a etapa de cada item, quando pode propor uma transição e como o usuário corrige um enquadramento inadequado. O status de uma história pode ser uma evidência a considerar. Sua suficiência ainda precisa ser examinada.
2. **Tratamento de mensagens que atravessam etapas.** Descrever como agir, por exemplo, quando uma mensagem enviada durante o planejamento técnico retifica a regra de negócio. Um cenário candidato exige localizar a definição afetada e indicar quais critérios, decisões técnicas e testes precisam de revisão.
3. **Continuidade e recuperação.** Definir quais evidências, decisões, revisões e pendências devem acompanhar a passagem entre etapas ou a retomada de uma atividade interrompida. As dúvidas, lacunas, pendências e incoerências percebidas devem ser catalogadas e apresentadas ao usuário o mais brevemente possível, conforme direção anterior da sessão.
4. **Verificação do comportamento.** Para cada atividade, especificar o que o agente precisa saber fazer, quais fontes pode consultar, quais resultados deve entregar e como o usuário reconhece um resultado suficiente. A aprovação formal do refinamento cabe ao Analista. A mudança de papel do agente conserva as responsabilidades e permissões aplicáveis.

## Origem e continuidade

A fonte desta nota é a manifestação direta do usuário sobre o tratamento das mensagens “de acordo com a etapa em que se está”. No acervo R06, o documento `04_refinamento_e_metodo_geral.md`, §§ 7–8, já registra a participação no refinamento e o preparo por atividade em R01-REQ-007, R01-ORI-004 e R01-ORI-005. A pendência **R01-P007** pede a especificação das competências de cada frente e de como verificá-las. A manifestação atual dá à orquestração desse comportamento escopo explícito de primeira entrega. A especificação dos papéis e de suas transições continua aberta. [Síntese do acervo R06](../evidencias/WORKSPACE-R06.md)

A direção é comum a Devin Web, CLI e Desktop e a Claude Code, respeitando o recorte de ferramentas e a agnosticidade já registrados. [Escopo de ferramentas da primeira entrega](FERRAMENTAS.md)
