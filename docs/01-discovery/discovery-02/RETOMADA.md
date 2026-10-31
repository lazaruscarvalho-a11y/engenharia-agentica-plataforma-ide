# Discovery 02 — Motor de Compreensão Profunda de Repositórios

Entrada preparada em 30/10/2026. **Discovery 02 ainda não executado por este arquivo.** Não houve criação automática de nova conversa. A direção foi aceita no histórico; os métodos abaixo são roteiro proposto, não arquitetura aprovada.

## Recuperação verificável

Repositório: `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`.
Branch desta consolidação: `proposta/discovery-01-onboarding-agent-first`.
Base herdada: `f8d7c60955a1250ae4d94a428386787f4aaa24b0`, PR #5. Consultar [recibo D01](../../../auditorias/discovery-01/RECIBO-PUBLICACAO.json) nessa branch e ler os documentos pelo `content_commit` imutável indicado; não usar nome de branch como versão suficiente. O próprio recibo é publicado em commit posterior e verificado separadamente na entrega.

1. Ler [ESTADO-ATUAL](../../../ESTADO-ATUAL.md), [índice D01](../discovery-01/README.md), [fontes](../discovery-01/FONTES.md), [registro](../discovery-01/REGISTRO.md) e [revisão](../discovery-01/REVISAO.md).
2. Conferir [manifesto D01](../discovery-01/MANIFESTO.json) e hashes do recibo pelo commit exato. Manifestos anteriores correspondem a conjuntos diferentes.
3. Expandir para [visão](../../fundacao/visao-produto.md), [capacidades](../../fundacao/capacidades.md) e [matriz D01](../discovery-01/MATRIZ.md) conforme a investigação.
4. Declarar a lacuna D01-PEN-001: só os cinco turnos finais foram recuperados; detalhes REL continuam a reconciliar. Não rediscutir decisões explícitas como se fossem desconhecidas, nem promover os relatos a decisões.

PGC/CT continuam NÃO RATIFICADOS, CA NOT_RUN. Main permanece fora da cadeia documental enquanto não houver merge autorizado. Usar exemplos sintéticos; sem acesso empresarial ou alterações de permissões. Fontes anexadas no Projeto são snapshots: verificar versão própria; esta publicação não realizou upload nem sincronização.

## Objetivo e fronteira

Investigar como agentes leem, analisam, interpretam e compreendem sistemas e convertem descobertas em conhecimento confiável. O foco desloca-se da organização/migração para o processo de compreensão, preservando decisões D01-DEC-001..003 sobre legado, ressalvas e classificação. Não iniciar implementação integral nem escolher stack antes de requisitos e critérios pertinentes.

| Frente proposta | Perguntas de investigação | Saída candidata |
|---|---|---|
| Exploração | Como começar num repositório desconhecido? Quais arquivos e evidências priorizar? Como reconhecer o que ficou fora? | Estratégia de exploração e registro de cobertura por revisão |
| Arquitetura e domínio | Como identificar componentes, regras, fluxos, contratos e dependências? Como distinguir código observado de intenção documental? | Achados com localização, hipótese, contradição e validação |
| Agentes e especialidades | Que tarefas precisam de agentes/subagentes? Como coordenar escopo e verificar resultado sem duplicação? | Responsabilidades, dependências e contrato de resultado propostos |
| Extração e consolidação | Quando um achado vira conhecimento? Como verificar omissões, inferências falsas e conflitos? | Fluxo de evidência→achado→verificação→proposta de conhecimento |
| Contexto e custo | Como recuperar contexto suficiente por tarefa? Como limitar custo sem ocultar dependência crítica? | Estratégias comparáveis com medidas candidatas, sem meta arbitrária |
| Incrementalidade | O que invalidar quando código, dependência ou instrução muda? Como lidar com merge/rebase e ponteiros? | Plano incremental com proveniência e detecção de obsolescência |
| Qualidade | O que significa compreensão profunda? Como medir cobertura e confiabilidade além da confiança verbal do modelo? | Oráculos e fixtures com respostas de referência revisáveis |

## Primeiro caso sintético sugerido

Um `servico-pedidos-exemplo` recebe uma requisição, valida uma regra, persiste estado e publica um evento. Um `consumidor-exemplo` reage ao evento; há uma falha de recuperação, documentação parcialmente obsoleta e uma dependência não evidente. Nenhum código dessa fixture foi criado nesta entrega.

Primeira pergunta para a nova sessão: **“Ao abrir esse sistema pela primeira vez, o que o engenheiro precisa que a Plataforma consiga explicar e demonstrar com evidências antes de confiar numa alteração?”**

Partir de uma expectativa concreta do usuário e explorar progressivamente fluxo, negócio, arquitetura, contrato e falhas. Não apresentar uma lista de técnicas como solução já escolhida. Se um detalhe depender das falas D01 ausentes, abrir pendência localizada e continuar frentes independentes.

## Registro e conclusão da rodada propostos

Cada achado deve distinguir fonte observada, relato, inferência, decisão e pendência; registrar repositório/revisão/localização, escopo analisado e não analisado. Erro de acesso, código gerado, documentação obsoleta, instrução hostil e mudança concorrente são cenários a investigar. Métricas e limiares serão candidatos até decisão explícita.

Resultado esperado do Discovery 02: entendimento do problema e dos critérios de confiança, alternativas de exploração/verificação, requisitos candidatos, mapa de riscos/pendências e plano de ensaios sintéticos. A aprovação de implementação e qualquer integração corporativa são etapas separadas. Publicar trabalho autorizado em branch/PR, verificar bytes pelo commit e emitir recibo, preservando continuidade entre sessões.
