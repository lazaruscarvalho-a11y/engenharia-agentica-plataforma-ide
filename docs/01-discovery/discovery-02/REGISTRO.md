# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](primeira-entrega/consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](primeira-entrega/consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Regra operacional vigente

Prontidão para Discovery significa conseguir ler a documentação vigente e recuperar corretamente decisões, restrições, pendências de produto e ponto de continuidade. RG e os demais gates da consolidação PM-R5 não são pendências nem bloqueios da entrevista. Não reexecutá-los para liberar o Discovery e não exigir INTEGRALMENTE_COMPROVADO para conversar. Somente um impedimento atual, material e demonstrado pode bloquear a etapa que dele dependa. Ver [PRONTIDAO](PRONTIDAO.md).

# Registro canônico D02 — revisão documental 2

Consolidação PM-D02-CONSOL-001 R5, 31/10/2026. **Em discovery, sem ratificação normativa, aprovação de implementação ou capacidade funcional demonstrada.** Este ledger possui IDs, natureza, proveniência, validade, autoridade, maturidade, propostas e pendências. Os axiomas AX têm dono temático em [axiomas-arquiteturais.md](../../fundacao/axiomas-arquiteturais.md). Modelo/blueprint/contratos são projeções ou propostas, sem definições humanas concorrentes.

Fonte curada D02-S01 = PM R5 §4, preservado em [entradas](../../../auditorias/discovery-02-incorporacao/entradas/PROMPT-MASTER-DISCOVERY-02-R5.md). Fonte D02-S04 = D01-R2 no commit `e37af725a162c577cfa9ffde286d0fcf69294429`. O autor atribuído das determinações reproduzidas é o usuário; sua identidade histórica não foi autenticada independentemente. O pedido vigente autentica o escopo desta missão, sem provar cada mensagem histórica. Reprodução não é natureza nem aprovação técnica retroativa. Acesso integral ao anexo curado; acesso às mensagens originais parcial/inacessível. Confronto literal com original: NOT_RUN. Cobertura semântica será avaliada contra reproduções e D01, não contra transcrição inexistente.

Todas as unidades abaixo: revisão documental 1; validade vigente apenas no escopo de discovery; maturidade EM DISCOVERY; autoridade de direção de produto ou proposta conforme natureza. Nenhum registro concede acesso operacional. [FONTES](FONTES.md) discrimina os seis eixos e limitações; [MATRIZ](MATRIZ.md) relaciona elementos, destinos e regressões.

<a id="hum-01"></a>

## HUM-01 — Profundidade e qualidade

Natureza: Intenção/direção de produto reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.1; revisão fonte R5.

Investigar amplamente os repositórios e aprofundar quanto viável: aspectos técnicos, execução documentada, testes, documentação, regras de negócio, arquitetura, relações e conhecimento existente. Explicar responsabilidades, fluxos, contratos, dependências, regras e riscos com suportes e contraevidências. Construir evidências exatas por repositório/commit/arquivo/linhas/contrato; avaliar precisão e segurança da absorção. Declarar escopo lido/não lido, exclusões, inacessibilidades, contraditórios e limites. Integralidade é intenção de cobertura; não prova compreensão perfeita nem autoriza execução.

<a id="hum-02"></a>

## HUM-02 — Autonomia fundamentada

Natureza: Direção de produto reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.2; revisão fonte R5.

Investigar autonomamente fontes autorizadas e dependências pertinentes, formular hipóteses e esgotar esclarecimento documental legítimo antes de escalar. Pedir intervenção por impedimento material, autoridade necessária ou decisão de produto realmente ambígua. Reduzir tarefas rotineiras do engenheiro, sem ampliar acesso ou substituir evidência por confiança.

<a id="hum-03"></a>

## HUM-03 — Execução local excepcional futura

Natureza: Decisão/restrição humana reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.3; revisão fonte R5.

Na IDE futura, somente diante de dúvida, pendência ou necessidade de esclarecimento intransponível após tentativas autorizadas esgotadas, pode-se pedir permissão específica ao engenheiro para subir a aplicação localmente. O engenheiro pode responder diretamente em alternativa. Documentar dúvida, tentativas, finalidade, ambiente/dados, pré-requisitos, comandos e efeitos previstos; solicitar apenas insumos faltantes necessários se a dependência for real. Conhecer como executar não autoriza executar. Esta missão documental proíbe solicitar/usar a exceção para executar aplicações. Retifica D01-RST-001 no alcance descrito em RETIFICACOES.md, preservando a decisão e a autoridade humana.

<a id="hum-04"></a>

## HUM-04 — Nenhuma refatoração no onboarding

Natureza: Decisão/restrição humana reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.4; revisão fonte R5.

Durante onboarding/importação: absolutamente nenhuma refatoração da aplicação, renomeação de APIs, reorganização de arquivos ou modernização oportunista. A orientação Agent-Centric passa a valer desde a importação para modificações e implementações posteriores autorizadas no escopo efetivamente necessário; não exige reestruturar todo arquivo tocado, dependência ou repositório. Mudança arquitetural adicional depende de especificação e escopo próprios.

<a id="hum-05"></a>

## HUM-05 — Topologia Micro/Meso/Macro

Natureza: Decisão conceitual/topológica reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.5; revisão fonte R5.

Conhecimento canônico em Git. Micro é o repositório individual. Meso é um repositório específico por sigla/conta e contém Micro como Git submodules. Macro é workspace com repositório Git e contém Meso como submodules. A relação organizacional fina sigla/conta/projeto/domínio continua a refinar sem reabrir essa escolha. Não há sincronização de ponteiros, acesso herdado ou direito de redistribuição implícitos. Clonagem, atualização, permissões e UX ainda exigem especificação. D01-REL-004 e D01-DEC-006 sustentam a topologia; a síntese genérica D01-REL-003 deve ser lida pela retificação D02.

<a id="hum-06"></a>

## HUM-06 — Autorizações herdadas do D01

Natureza: Síntese editorial de decisões e intenções D01-R2. Modo: Síntese do documento D01-R2 consultado, não declaração humana direta integral no pedido R4/R5. Fonte: D02-S01 §4.6; revisão fonte R5.

Preservar separadamente: inventário/leitura inicial autorizados no onboarding; consulta posterior ao legado diante de lacuna, que exige permissão e aviso de inconformidade; buscas exteriores, precedidas de finalidade/fonte/escopo e autorização; execução; escrita/publicação; armazenamento derivado; redistribuição; exclusão. Uso provisório Agent-First é permitido e referência preferencial/padrão, mantendo originais; consultas e código nessa fase dependem do escopo autorizado e não significam verificação definitiva. Exclusão sempre requer aprovação expressa do objeto/revisão. Sistemas inacessíveis podem ser estudados por fontes indiretas autorizadas, sem inventar implementação interna ou exigir submódulo para todo sistema. Preservar referência externa e incorporar só derivado legitimamente armazenável e compartilhável. Suportar autorização pontual/reutilizável e individual/coletiva sem criar acesso inexistente, permanência irrestrita ou direito fora de escopo. Identidade, validade, revogação, schema e mecanismo de fiscalização são propostas a especificar; registros segregados são controles desta missão, sem etiqueta de decisão técnica humana.

<a id="hum-07"></a>

## HUM-07 — Dez axiomas

Natureza: Direções de produto reproduzidas; semântica operacional candidata. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.7; revisão fonte R5.

Os dez rótulos são Agent-Centric, Agent-Oriented, AI-Intent, SDD, Harness Engineering, Contexto Mínimo Necessário, Roteamento de Contexto, Contexto-Ótimo, AI-Based Architecture e agnosticidade de modelo/agente/ferramenta. O dono das definições temáticas é docs/fundacao/axiomas-arquiteturais.md, AX-01..AX-10 revisão 1. Nomes, direção, interpretação proposta, tecnologia exemplificativa, dependências e evidência de capacidade são classes distintas. Sem ratificação PGC/CT, stack aprovada, garantia de eficácia ou capacidade implementada.

<a id="hum-08"></a>

## HUM-08 — Atualização e drift

Natureza: Direção/restrição de produto reproduzida. Modo: Declaração reproduzida pelo usuário na missão R4, conforme dossiê R5; original histórico não recuperado. Fonte: D02-S01 §4.8; revisão fonte R5.

Mudança agêntica deve atualizar ou revalidar conhecimento afetado no mesmo ciclo commit/PR, antes de fechar, relacionando código/contrato/conhecimento/validação. Multirrepositório explicita commits e ponteiros em transação lógica verificável, sem prometer atomicidade física. Inconsistência mantém o ciclo dependente aberto/bloqueado. Drift tem quatro estágios com entrada/saída/prova: detectar alteração externa; invalidar conhecimento afetado e impedir uso como atual; reconciliar conteúdo/relações; verificar nova revisão contra evidências. Detecção não corrige; reconciliação sem verificação não restaura validade. Sem monitor real, detecção ocorre na próxima leitura/ciclo executado. Mecanismos técnicos são candidatos.

<a id="hum-09"></a>

## HUM-09 — Colaboração, papéis e pendências

Natureza: Síntese editorial de decisões/intenção D01-R2. Modo: Síntese do documento D01-R2 consultado, não declaração humana direta integral no pedido R4/R5. Fonte: D02-S01 §4.9; revisão fonte R5.

Compartilhar e consolidar entre autorizados preservando autonomia, concorrência, revisão-base, publicação controlada e rastreabilidade. Push de trabalho não publica conhecimento aprovado. Esclarecimentos/correções do engenheiro depois do onboarding retroalimentam Micro/Meso/Macro pertinentes com autorização e validação. Catalogar pendências estruturadas, hierarquizadas, instrutivas e disponíveis por relevância em cada leitura/ciclo, sem carregar tudo sempre. D01-NEC-001, REL-005, DEC-007, DEC-016 e DEC-017 sustentam a direção; algoritmo, gatilhos e modalidade de workspace continuam candidatos.

<a id="hum-10"></a>

## HUM-10 — Nomes de documentos futuros

Natureza: Proposta editorial preservada do índice material R3. Modo: Reconstrução/síntese editorial indicada no PM; não decisão técnica humana. Fonte: D02-S01 §4.9; revisão fonte R5.

AGENTES.MD e PENDENCIAS.MD são nomes propostos para artefatos da IDE futura: finalidade, contrato e reconhecimento por ferramentas ainda a definir. São distintos de AGENTS.md operacional; não renomeá-lo, substituí-lo ou criar colisões, inclusive em sistemas sem distinção de maiúsculas. Nenhum desses dois artefatos futuros é criado nesta consolidação.

<a id="hum-11"></a>

## HUM-11 — Maturidade e backlog

Natureza: Síntese editorial de limites e direção de discovery. Modo: Reconstrução/síntese editorial indicada no PM; não decisão técnica humana. Fonte: D02-S01 §4.10; revisão fonte R5.

Investigar e especificar produto completo, UX, regras de negócio, permissões, estados, exceções, segurança, evidências e operação, sem antecipar implementação. Conclusão com pendências não críticas preserva catálogo/ressalvas; criticidade requer critérios rigorosos e incerteza material escala. Taxonomia, limiares, layout, stack e mecanismos candidatos não são decisões aprovadas. Relatos do banco/CI-CD/GMUD/scheduled/ambientes/acesso não são políticas universais nem implantação comprovada.

## Propostas de engenharia e dependências abertas

| ID | Fonte/direção de origem | Proposta preservada e limite | Dono de detalhamento |
|---|---|---|---|
| D02-PROP-001 | HUM-01/02, D01 P-A/P-L | Fluxo de compreensão com inventário, análise ampla, aprofundamento dirigido, confronto e avaliação por mudança pretendida; sequência/gates não aprovados | MODELO-FUNCIONAL.md |
| D02-PROP-002 | HUM-01/07, P-B/P-F | Unidades com evidência exata, incerteza, contraevidência e criticidade; schema/limiares candidatos | CONTRATOS-CANDIDATOS.md e AVALIACAO.md |
| D02-PROP-003 | HUM-05/09, P-C/P-D/P-E | Roteamento, projeções portáteis e contribuições concorrentes Micro/Meso/Macro; formato/algoritmo/gatilhos candidatos | MODELO-FUNCIONAL.md |
| D02-PROP-004 | HUM-06, P-I/P-J | Registros segregados de permissão, catálogo de referências/derivados e mapa de migração sem exclusão implícita; mecanismos candidatos | CONTRATOS-CANDIDATOS.md |
| D02-PROP-005 | HUM-08, P-H/P-G | Relações código/contrato/conhecimento e revisão composta; detecção de drift por ciclo; motor local não impõe barreira remota | MODELO-FUNCIONAL.md |
| D02-PROP-006 | HUM-09/11, P-K | UX de escopo, evidência, incerteza, pendência e intervenção proporcional, sem layout/máquina de estados aprovados | MODELO-FUNCIONAL.md e AVALIACAO.md |
| D02-PROP-007 | HUM-07/10 | Contratos legíveis por agentes e nomes futuros AGENTES.MD/PENDENCIAS.MD; schema, protocolos e reconhecimento pendentes | CONTRATOS-CANDIDATOS.md |

Detalhes acima são autoria editorial desta consolidação; não herdam aprovação humana das direções. Os grupos D01 P-A..P-L continuam canônicos no D01 e são projetados na matriz D02, sem alteração dos registros herdados.

## Pendências D02

| ID | Relações e questão aberta | Impacto e próximo trabalho |
|---|---|---|
| D02-PEN-001 | D01-PEN-007/005; HUM-01/02: que evidência permite compreender suficientemente uma mudança pretendida e quando a lacuna é insegura? | Refinar avaliação, cobertura/confiabilidade/custo; bloqueia critério operacional, não reconciliação D01 |
| D02-PEN-002 | D01-PEN-010; HUM-09/11: como tornar evidência, incerteza e dependências compreensíveis ao engenheiro? | Refinar UX e acessibilidade com cenário sintético; sem escolher tela por inferência |
| D02-PEN-003 | D01-PEN-002/003; HUM-05/08: revisões/ponteiros e concorrência multirrepositório | Contratos de clonagem, atualização, permissões e fechamento lógico a especificar |
| D02-PEN-004 | D01-PEN-004/008; HUM-03/06: autoridade, validade, revogação, dados e efeitos | Especificação futura; não pedir permissão para executar aplicação nesta missão |
| D02-PEN-005 | D01-PEN-006; HUM-07/10: schemas, índices, adaptadores e nomes futuros | Sem stack/protocolo/forma definitiva aprovada |
| D02-PEN-006 | D01-PEN-009; manutenção das cópias de referência | Manter revisão/identidade das Fontes quando houver nova publicação. Acesso autenticado e leitura foram observados em 01/11/2026; esta manutenção não é bloqueio da entrevista. Ver PRONTIDAO.md e recibo de aplicação da revisão. |

D01-PEN-001/A está materialmente reconciliado no escopo do recibo R2; B continua transcrição original integral não recuperada, limitação não bloqueante para conteúdo reproduzido suficiente. Não se reabrem escolhas conceituais por faltar algoritmo/original. Resultados históricos 8 checks/13 negativos não são novos testes D02; os 49 CA operacionais continuam NOT_RUN.
