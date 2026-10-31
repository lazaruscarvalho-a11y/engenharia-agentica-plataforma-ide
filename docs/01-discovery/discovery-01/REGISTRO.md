# Registro de definições — revisão 1

Este é o registro canônico exploratório D01. A matriz o referencia; não há requisitos normativos aprovados por este arquivo. Classes: **DEC** = decisão explícita no escopo da manifestação; **REL** = definição anterior relatada pelo assistente, sem fala original recuperada; **PROP** = detalhamento proposto; **HIP** = hipótese a verificar; **PEN** = pendência. Publicação, aprovação, implementação e vigência são dimensões separadas.

## Decisões explícitas recuperadas

| ID | Conteúdo e justificativa | Fonte e limite |
|---|---|---|
| D01-DEC-001 | Para obter informação do legado diante de lacuna na estrutura migrada, solicitar permissão do engenheiro e informá-lo da inconformidade persistente. Evita recuperação silenciosa e ocultação de perda/incompletude. | D01-S02-A, manifestação direta. Refere-se à futura Plataforma; não é exigência de nova aprovação para ler os documentos deste projeto já autorizados no pedido atual |
| D01-DEC-002 | Permitir conclusão do onboarding com inconformidades não críticas ainda não resolvidas, explicitamente catalogadas e controladas. | D01-S02-B responde à pergunta em A. Não autoriza concluir com falha crítica ou ocultar pendência; nomes de estados e critérios detalhados não foram aprovados nesse “Permitir” |
| D01-DEC-003 | A Plataforma pode classificar automaticamente a criticidade usando critérios rigorosos, objetivos e verificáveis, recorrendo ao engenheiro quando não determinar a criticidade com segurança. | D01-S02-C responde à pergunta em B. Fatores, taxonomia, limiares e mecanismos apresentados depois continuam candidatos |
| D01-DEC-004 | Consolidar o Discovery 01 e preparar continuidade para uma nova sessão dedicada ao Motor de Compreensão Profunda de Repositórios. | D01-S02-D/E e D01-S01. Autoriza documentação e publicação revisável conforme pedido; não aprova arquitetura, stack, requisitos derivados nem cria nova conversa automaticamente |

## Definições anteriores relatadas — preservar sem ratificar

| ID | Definição mencionada nas sínteses recuperadas | Fonte / certeza |
|---|---|---|
| D01-REL-001 | Compreensão profunda e incremental de repositórios como base do onboarding. | C/D; alinhada a CAP-002, mas método e aceite anteriores não recuperados |
| D01-REL-002 | Conhecimento Agent-First agnóstico a Devin, Claude e Copilot. | C/D; não demonstra adaptadores nem equivalência entre ferramentas |
| D01-REL-003 | Organização Git hierárquica Micro, Meso e Macro. | C/D; fronteiras, quantidade de repositórios e regra exata de herança não recuperadas |
| D01-REL-004 | Uso de Git Submodules nessa organização. | D; menção não prova desenho, contratos de atualização ou escolha humana original |
| D01-REL-005 | Compartilhamento seguro e reconciliação automática de conhecimento. | C/D; gatilhos, escopo, aprovações e conflitos permanecem desconhecidos |
| D01-REL-006 | Migração cuidadosa de documentação e instruções existentes. | C/D; preservar distinção entre informação e instrução executável |
| D01-REL-007 | Uso provisório da nova estrutura, inclusive para alterações autorizadas de código. | C/A; “autorizadas” é condição, não permissão genérica para modificar qualquer repositório |
| D01-REL-008 | Exclusão de artefatos originais sempre mediante aprovação expressa. | B/C; original não recuperado; manter restrição conservadora e não excluir nesta missão |
| D01-REL-009 | Segurança, autorizações, concorrência, inconsistências e consolidação do conhecimento integram o onboarding. | D; controles técnicos específicos e manifestações humanas correspondentes ausentes |

O registro REC-001 da fundação relata uma proposta humana anterior de camadas plataforma→conta/sigla→repositório. Isso não demonstra equivalência automática com Macro/Meso/Micro nem aprovação de Submodules. A correspondência precisa ser reconciliada em D01-PEN-002.

## Propostas de detalhamento preservadas

| ID | Conteúdo candidato | Origem e limite |
|---|---|---|
| D01-PROP-001 | Fluxo de recuperação: identificar lacuna → explicar impacto → informar engenheiro/artefato/motivo → obter permissão → investigar → verificar, reconciliar e preparar incorporação. | Assistente A; DEC-001 sustenta só permissão e comunicação; sequência completa é proposta |
| D01-PROP-002 | Consulta autorizada ao legado usa conteúdo como informação; não executa instruções, hooks ou procedimentos. Permissão de leitura não aprova publicação da correção nem exclusão do original. | Assistente A; consistente com fronteiras da fundação; sem nova concessão operacional |
| D01-PROP-003 | A inconformidade permanece até compreensão, reconciliação, incorporação e verificação. Negar consulta mantém pendência e libera apenas atividades independentes. | Assistente A; resolver lacuna não se resume a localizar documento |
| D01-PROP-004 | Bloqueios proporcionais ao impacto: impedir operações dependentes de conhecimento crítico ausente, permitindo trabalho independente. | Recomendação A; extensão a outros bloqueios requer refinamento |
| D01-PROP-005 | Estados de migração: Concluída, Concluída com ressalvas e Bloqueada. | Assistente B após a resposta humana; sem máquina de estados aprovada |
| D01-PROP-006 | Criticidade: Crítica bloqueia conclusão segura/operações afetadas e exige resolução/revalidação; Não crítica permite ressalvas; Indeterminada exige investigação ou avaliação humana antes de liberar dependentes. | Assistente C após “Sim”; sem limiar numérico aprovado |
| D01-PROP-007 | Avaliar segurança, perda de conhecimento, comportamento, integridade de instruções, dependências e consequências para agentes. Não usar somente confiança declarada pelo LLM; combinar verificações determinísticas, comparação de versões, evidências e testes independentes quando possível. | Guardrails propostos C; critérios objetivos são exigência aceita em DEC-003, lista/mecanismo não |
| D01-PROP-008 | Explicar classificação, artefatos afetados, evidências e medidas de resolução. Intervenção humana pode corrigir erro de classificação sem dispensar automaticamente controles técnicos/corporativos. | Assistente C; apresentação e protocolo de revisão ainda propostos |
| D01-PROP-009 | Após conclusão com ressalvas, manter pendências rastreáveis, comunicar limitações aos agentes e permitir resolução posterior. | Assistente B; operacionaliza DEC-002, sem detalhe de UX aprovado |
| D01-PROP-010 | Aviso de IDE com lacuna, documento legado candidato, impacto e ações de autorizar/negar consulta. | Exemplo sintético A; não é layout, tela nem controle implementado |
| D01-PROP-011 | Discovery 02 investiga exploração de código, arquitetura/regras/fluxos/dependências, agentes especializados, extração/verificação/consolidação, roteamento/custo/incrementalidade e métricas de compreensão. | Recomendação D e direção aceita; questões e método continuam exploratórios |

## Hipóteses propostas nesta consolidação

| ID | Hipótese nova, sem atribuição ao usuário | Evidência futura necessária |
|---|---|---|
| D01-HIP-001 | Um núcleo de conhecimento independente de executor, com projeções por ferramenta, preserva semântica entre agentes. | Comparar interpretações e perda de informação em fixtures sintéticas; validar precedência, sem escolher stack |
| D01-HIP-002 | Fixar revisões dos níveis de conhecimento e registrar proveniência permitirá detectar obsolescência e conflitos sem propagar conteúdo indevido. | Cenários de revisão divergente, revogação de acesso e atualização concorrente; avaliar custo e granularidade |
| D01-HIP-003 | Um inventário origem→destino com verificações por item permite detectar lacunas de migração e sustentar a criticidade. | Migração sintética com perda, contradição, duplicação e referência quebrada injetadas; medir falsos positivos/negativos |

Todas as pendências têm ID e encaminhamento em [REVISAO.md](REVISAO.md). Nenhum dos desenhos deste conjunto escolhe banco de dados, busca vetorial, parser, framework, executor definitivo ou arquitetura distribuída.
