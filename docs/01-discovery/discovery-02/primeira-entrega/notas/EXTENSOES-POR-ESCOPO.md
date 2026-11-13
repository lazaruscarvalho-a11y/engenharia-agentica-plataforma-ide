# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](../consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](../consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](../consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Inclusão de capacidades por escopo após o onboarding

**Revisão 1 · Direção de produto para a primeira entrega.** O usuário deve poder acrescentar skills, instruções, comportamentos e documentação a um **repositório, Sigla, Workspace ou arquitetura**, inclusive depois de seu onboarding e de sua internalização. O caso do IBM ODM inclui também uma ferramenta disponibilizada via MCP e as orientações que tornam seu uso compreensível. A manifestação desta conversa é a fonte direta da direção. O caso serve de referência para o Discovery.

## O que cabe ao agente

**Na inclusão**, o agente deve conduzir a incorporação segundo a estrutura, as configurações e os padrões da Plataforma. Deve ficar claro a qual escopo o acréscimo pertence, o que ele oferece e como, quando e por que se aplica. Assim, duas equipes podem dotar seus repositórios de capacidades diferentes e encontrá-las de uma maneira consistente.

**No uso**, o agente deve mapear e compreender os recursos daquele escopo e recorrer aos que forem pertinentes à atividade. Isso vale tanto para uma interação direta quanto para um trabalho que alcance esse escopo por uma dependência, dentro ou fora de um Workspace. A descoberta conserva a origem da capacidade. Consultar documentação, incluir um repositório em um Workspace e executar uma operação de uma ferramenta seguem as permissões próprias de cada ação.

## Caso de referência do IBM ODM

Um repositório consulta diversas integrações, reúne os resultados e os envia ao IBM ODM. O ODM aplica regras de negócio e devolve uma resposta. Depois do onboarding, a equipe decide integrar um MCP ao repositório e acrescentar skills, documentação e instruções sobre seu uso. O vínculo é com aquele repositório. A função comum da Plataforma é dar suporte à incorporação e à recuperação desse conjunto quando o trabalho exigir.

| Situação ilustrativa | Comportamento esperado |
|---|---|
| Um engenheiro pergunta no repositório, fora de um Workspace, “De onde vem esta resposta?” | O agente distingue a preparação dos dados no repositório da decisão tomada no ODM. Localiza as orientações do repositório e usa os recursos aplicáveis, inclusive o MCP quando a investigação exigir uma operação disponível e autorizada. |
| Um Workspace refina uma mudança em outro serviço que consome a resposta. A atividade depende de saber onde uma regra é aplicada. | A partir da dependência, o agente chega ao repositório integrador e encontra a mesma documentação, as skills e o MCP. Pode assim investigar a questão mesmo quando a pessoa não conhece o nome da ferramenta. Se faltar acesso ou evidência para concluir, apresenta a lacuna assim que percebida. |
| Um segundo repositório da mesma Sigla participa de uma atividade independente do ODM. | Os padrões de organização continuam comuns aos dois repositórios. A capacidade do primeiro permanece identificada com sua origem e finalidade. |

## O que refinar depois

- Qual é o padrão mínimo para incorporar e validar cada tipo de contribuição, inclusive um MCP e suas instruções de uso?
- Como identificar uma dependência indireta relevante e recuperar a orientação correta quando mais de um escopo contribui para a atividade? Como apresentar sobreposições, conflitos e referências desatualizadas?
- Como reconhecer alterações e retiradas posteriores e refletir seu impacto nos escopos autorizados? Formatos, diretórios, índices e regras de precedência continuam em refinamento.

## Relação com os registros anteriores

O acervo R06 distingue recursos comuns da área local e a extensibilidade da própria Plataforma após a internalização (R01-REQ-005/006). Esta direção acrescenta a evolução de **cada escopo** pelo usuário, mediada pelo agente. O roteamento por dependência, a atualização do conhecimento e as permissões por operação são referências aplicáveis. A configuração de um MCP de domínio é compatível com o recorte de Devin e Claude Code como ferramentas de IA da primeira entrega. [Síntese do acervo R06](../evidencias/WORKSPACE-R06.md) · [Registro D02](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/01-discovery/discovery-02/REGISTRO.md) · [Escopo de ferramentas](FERRAMENTAS.md)
