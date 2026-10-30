# Auditoria independente de produto, negócio, UX, método e proveniência

Data: 30/10/2026. Auditor: agente independente `/root/auditoria_produto`, sem autoria dos documentos examinados. Snapshot congelado: **`5f3a168849a9fc18a70e2dca9a20becb9ff39eb3`**. O HEAD local foi conferido antes da análise.

## Escopo e limite da conclusão

Foram lidos `AGENTS.md`, `ESTADO-ATUAL.md`, `README.md`, os oito documentos de `docs/fundacao/`, `docs/01-discovery/INICIO-DISCOVERY.md`, `docs/chatgpt/PRIMEIRA-SESSAO.md` e inventário/matriz/JSON da auditoria integral. Obrigações examinadas individualmente: F-001–F-024, F-027, F-045 e F-048, total de 27.

O oráculo de cobertura é o briefing desta auditoria, que enumera a visão ampla desejada, os relatos do banco e os limites da missão. O coordenador também forneceu o enunciado das sete etapas para conferência semântica. A leitura de `../snapshot-inicial.json` confirmou o registro local do retorno de SRC-002 com cinco turnos, `hasMore=false` e `nextCursor=null`; isso não recupera a concepção original completa. SRC-001 é descrita no repositório, mas seu texto integral e uma âncora imutável da mensagem atual não fazem parte deste snapshot. Portanto, esta auditoria não certifica transcrição literal nem exaustividade do histórico anterior.

A revisão é documental e estrutural. Não testa a futura IDE, conectores, Devin CLI, interfaces corporativas ou ambiente do banco. Não usa os relatórios históricos como prova transferível. O relatório final pendente desta rodada foi expressamente excluído de achados, pois será preenchido após as auditorias. Nenhuma fonte foi alterada; somente este relatório foi escrito.

## Resultado e achados

**Não foram identificados P0 ou P1 no escopo examinado. Foi identificado um P2.** A fundação restitui a visão de plataforma além do PGC, apresenta discovery de negócio e UX e diferencia intenções futuras de capacidades implementadas. Isso não constitui aceite do produto nem afirmação de ausência de defeitos.

### P2-PROD-001 — Fases 00–09 sem entradas e retornos explícitos para cada fase

**Obrigação:** F-020, fases com entradas, saídas, gates e retornos.

**Evidência:** `docs/fundacao/metodologia-fases.md:21–32` oferece as colunas “Objetivo e artefatos úteis” e “Gate de saída e retorno”, mas não especifica condições de entrada por fase. Retornos específicos aparecem na fase 02 (`:25`, retorno à 01) e na fase 06 (`:29`, retorno às 02–05); as demais dependem da orientação genérica de revisão em `:17` e `:38–40`. `docs/fundacao/construcao-internalizacao.md:42–51` possui entradas dos gates EXT/INT, porém não estabelece correspondência completa com as dez fases nem supre seus retornos. A leitura integral foi rechecada por busca focal de entradas/saídas/gates/retornos nos documentos de método, estratégia e discovery.

**Impacto:** ao retomar ou delegar uma fase, agentes podem inferir bases diferentes para iniciá-la ou para retornar após uma falha. Não impede iniciar discovery, mas deixa a obrigação literal parcialmente atendida.

**Correção proposta:** explicitar, para cada fase 00–09, entradas/revisões mínimas, saídas identificáveis, condição de passagem e condição/destino de retorno. Manter tudo como organização proposta; gates de produto, ratificação normativa e autorização produtiva continuam distintos. Não é necessário preencher decisões de produto ainda pendentes.

**Estado auditado:** F-020 = **Parcial** no commit congelado.

## Cobertura por obrigação

“Documentado” significa que o conteúdo requerido foi encontrado com limites coerentes; não significa implementação ou teste da capacidade futura. Referências abaixo são caminhos e linhas do snapshot congelado.

| ID | Avaliação | Evidência e conclusão |
|---|---|---|
| F-001 | Documentado | `docs/fundacao/visao-produto.md:9–13,79–83`: plataforma integral, trabalho de engenharia e distinção expressa entre harness e IDE; não se reduz a governança. |
| F-002 | Documentado | `docs/fundacao/ecossistema-atual.md:13–19`: squads/hierarquia, analistas/TL/PM/SME/desenvolvedores e reuniões Teams; sem generalização institucional. |
| F-003 | Documentado | `docs/fundacao/ecossistema-atual.md:16`; `docs/fundacao/construcao-internalizacao.md:31`: ServiceNow/IuClick com features, histórias, bugs e tasks; contratos reais desconhecidos. |
| F-004 | Documentado | `docs/fundacao/ecossistema-atual.md:25–27`: provisionamento GitHub por issue/pipeline e `iupipes.yml`, com campos relatados e esquema ainda não confirmado. |
| F-005 | Documentado | `docs/fundacao/ecossistema-atual.md:28,52`; `docs/fundacao/construcao-internalizacao.md:34`: Terraform e AWS DEV/HOM/PROD. |
| F-006 | Documentado | `docs/fundacao/ecossistema-atual.md:29–32`: Defect Dojo, sigla app e aprovação arquitetural preservados sem inventar significado ou autoridade. |
| F-007 | Documentado | `docs/fundacao/ecossistema-atual.md:30,46,63`; `docs/fundacao/registro-conhecimento.md:74`: Sonar descrito e incertezas de IUQuali/TAAC/TestSpec preservadas em PEN-004. |
| F-008 | Documentado | `docs/fundacao/ecossistema-atual.md:38–46,52–56`: fluxo feature/develop/release-HOM/main-PROD, associação ServiceNow/GMUD/janela, incidentes/hotfix, Datadog e break-glass contextualizados sem configuração ou acesso pressupostos. |
| F-009 | Documentado | `docs/fundacao/visao-produto.md:45–49`; `docs/fundacao/capacidades.md:15–17`: workspaces multirrepositório, análise/indexação e limites de revisão/cobertura/obsolescência. |
| F-010 | Documentado | `AGENTS.md`; `docs/fundacao/roteamento-contexto.md:5–22`: pontos de entrada, seleção por assunto, dependências materiais, contexto mínimo suficiente e AGENTS; heurística não é limite rígido. |
| F-011 | Documentado | `docs/fundacao/visao-produto.md:51–55`; `docs/fundacao/capacidades.md:18–19`: reuniões/fontes autorizadas, requisitos, decisões, dúvidas e contradições; sem alegar ingestão real. |
| F-012 | Documentado | `docs/fundacao/capacidades.md:20`; `docs/fundacao/visao-produto.md:47,71`: demanda correlacionada a arquitetura, APIs, serviços, AWS, equipes e repositórios, com evidências e lacunas a refinar. |
| F-013 | Documentado | `docs/fundacao/visao-produto.md:57–61`; `docs/fundacao/capacidades.md:24–25`: plataforma retém coordenação e agentes/subagentes; Devin CLI é executor pretendido de viabilidade ainda não demonstrada. |
| F-014 | Documentado | `docs/fundacao/capacidades.md:27–30`; `docs/fundacao/visao-produto.md:63–67`: supervisão, aprovação/redirecionamento/interrupção, revisão/testes independentes e rastreabilidade; estados de cancelamento e evidência previstos para refinamento. |
| F-015 | Documentado | `docs/fundacao/visao-produto.md:69–73`; `docs/fundacao/construcao-internalizacao.md:51,61`: diagnóstico e hotfix com confirmação final explícita e controles corporativos; hipótese de causa não vira causa comprovada. |
| F-016 | Documentado | `docs/fundacao/construcao-internalizacao.md:5–22,47`: construção futura externa real inclui frontend/backend/persistência/motor/agentes; interface vazia não satisfaz a intenção. |
| F-017 | Documentado | `docs/fundacao/construcao-internalizacao.md:9–20,26–38,65`: conectores desacoplados, simuladores, contratos versionados, testes, documentação e empacotamento. |
| F-018 | Documentado | `docs/fundacao/construcao-internalizacao.md:5,48–61`: internalização posterior por autorizados, com contratos e homologação reais; uso externo sintético sem presumir serviços/dados internos. |
| F-019 | Documentado | `docs/fundacao/metodologia-fases.md:9–17`: as sete etapas correspondem semanticamente ao enunciado fornecido à auditoria, incluindo M-07 transversal. Não foi possível certificar redação literal do planejamento original integral. |
| F-020 | Parcial | Dez fases e gates constam em `docs/fundacao/metodologia-fases.md:23–32`; faltam entradas/retornos sistemáticos por fase. Ver P2-PROD-001. |
| F-021 | Documentado | `docs/01-discovery/INICIO-DISCOVERY.md:13–24,28–32`; `docs/fundacao/visao-produto.md:28–73`: negócio, perfis, jornadas, funcionalidades, navegação/estados/acessibilidade e supervisão visual são frentes explícitas; layout permanece aberto, como requerido para discovery. |
| F-022 | Documentado | `docs/fundacao/protocolo-sessoes.md:7–23,29–37`: conversa natural, brainstorm/proposta/decisão distintos, aceite parcial/revisão exata, sem aprovação herdada pelos detalhes do agente. |
| F-023 | Documentado | `docs/fundacao/registro-conhecimento.md:25–37,41–91`; `docs/fundacao/protocolo-sessoes.md:27–31`: classes, IDs, estados, fontes, revisão, decisões, hipóteses e pendências; publicação, implementação e verificação são dimensões separadas. |
| F-024 | Parcial, com limite declarado | `auditorias/fundacao-integral/INVENTARIO.md:18–21`; `docs/fundacao/registro-conhecimento.md:9–23,83`: origem e IDs recuperados descritos, truncamento/ausência do histórico integral honestos. A conferência literal completa permanece limitada; não é correto promover este item a Verificado. |
| F-027 | Documentado | `README.md:1–18`, `AGENTS.md` e `ESTADO-ATUAL.md`: entrada apresenta missão integral, método, discovery, maturidade, continuidade, estratégia externa/interna e governança auxiliar; não apenas PGC. |
| F-045 | Documentado | `docs/01-discovery/INICIO-DISCOVERY.md:26–53`; `docs/chatgpt/PRIMEIRA-SESSAO.md`: sequência, abertura concreta, uma pergunta útil por vez, formalização de requisito com fluxo/exceções/UX/aceite e critérios de avanço; não finge entrevista já executada. |
| F-048 | Verificado no alcance estrutural | `ESTADO-ATUAL.md` distingue fundação/IDE não implementada; `docs/fundacao/visao-produto.md:79–84` e `docs/fundacao/metodologia-fases.md:38–40` vedam antecipação material. A árvore Git examinada apresenta documentos e harness/verificadores/empacotador, sem entrega da IDE final. Esta conferência não atesta conteúdo fora do snapshot. |

## Coerência entre as frentes

- **Negócio e produto:** OBJ, JOR e CAP oferecem encadeamento inicial suficiente para iniciar investigação. Prioridade de MVP, métricas e papéis definitivos ficam explicitamente pendentes; não foram inventados para encerrar a missão.
- **UX:** a experiência visual é central e inclui navegação, supervisão, diffs/fontes, estados de erro/conflito/recuperação e acessibilidade. A ausência de telas finais aprovadas é compatível com esta fase; os exemplos de painel lateral permanecem ideias.
- **Método:** as sete etapas e a sequência 00–09 são coerentes com o escopo atual. M-07 transversal, provas técnicas delimitadas e devolução ao refinamento evitam transformar a organização em autorização de construir. A ressalva operacional é P2-PROD-001.
- **Conhecimento e autoridade:** relato do banco, intenção do usuário, hipótese/recomendação e decisão explícita são separados. O material não generaliza ferramentas conhecidas para toda a instituição nem atribui funções inventadas a IUQuali/TAAC/TestSpec.
- **Proveniência:** a limitação de SRC-002 é propagada para estado, inventário e registro, sem alegar recuperação integral. Para continuidade mais auditável, convém acrescentar futuramente uma âncora estável de SRC-001 e mapear afirmações materiais a mensagens/trechos recuperados, sem inventar nem exigir reconstrução humana do histórico.
- **Capacidade e autorização:** nenhuma CAP da IDE é promovida a implementada/verificada/integrada. Mock não é homologação interna; PR não é merge/ratificação; aceite histórico do piloto não aprova este incremento; hotfix e break-glass não são permissões permanentes.

## Checagens executadas e reprodutibilidade

1. `git rev-parse HEAD`, `git status --short`, árvore completa via `git ls-tree -r --name-only` e metadados do commit: o snapshot inicial corresponde ao SHA declarado.
2. Leitura integral dos documentos listados, seguida de busca focal para rechecagem do achado de método e dos limites de proveniência. A primeira leitura conjunta extensa foi repartida para evitar depender de saída truncada.
3. Checagem local somente leitura: **13 documentos, 66 links relativos examinados, nenhum destino de arquivo ausente**. Não foram verificados fragmentos/âncoras, URLs remotos ou todos os links dos pacotes históricos.
4. JSON da matriz: **27/27 IDs do escopo presentes; todos os caminhos associados existem**. Isso verifica estrutura, não suficiência do conteúdo nem execução de capacidades.
5. O retorno bruto local de SRC-002 foi consultado somente para metadados e confirmação do alcance. Não foi tratado como transcrição original exaustiva nem incorporado como fonte versionada ao repositório.

Não houve falha de execução que exigisse ultrapassar duas tentativas. Não foram rodados geradores históricos, testes corporativos, CA operacionais PGC ou ações remotas.

### Hashes SHA-256 dos documentos de produto/método lidos

| Arquivo | SHA-256 |
|---|---|
| `AGENTS.md` | `434269224d24cf8927d9c98a64e7c61463582ce87a19f4e863f6aab91e63ab33` |
| `ESTADO-ATUAL.md` | `c5dcf4b766ad1b5d24e598ba08815397348aaaf18294ee9c393976c27e63c3bc` |
| `README.md` | `d59ae0efe00c17ccf83ae3fb319e056c3e9a920002822d807f714287c76b7bc4` |
| `docs/fundacao/capacidades.md` | `eafadbd4e10de4ab3f3f397b1c74d18230fc42e7ae5237f50ac2917f72a8f3b1` |
| `docs/fundacao/construcao-internalizacao.md` | `a9384ac36e52b49664f5afda51e84301a2c8dd239dcd13d0806dfa400dc0aef6` |
| `docs/fundacao/ecossistema-atual.md` | `ffc855b144062aa1d1d200e5f2a9aadb284f40ea3503b2956ce8f613d86cd2fe` |
| `docs/fundacao/metodologia-fases.md` | `06129000b2ac2ccdd0eaa2eed2d5248f3e07527735da4f00e5ccdf88751196d0` |
| `docs/fundacao/protocolo-sessoes.md` | `4e598caaca0141e0c864f4c45bcd7498b948c333600a0e9e9428d8824e693579` |
| `docs/fundacao/registro-conhecimento.md` | `05a64f5b2912a01feaf84e3cdc55b61b7e45a5aa8355f18a11d6314f81bb6b0d` |
| `docs/fundacao/roteamento-contexto.md` | `51630ea37f9f65b6b86ff445087891f8c49285f34401675f393fe0c2ea93d1af` |
| `docs/fundacao/visao-produto.md` | `79c185bde0b2034bb75efe7a7da0e0251271d457f9365d1691f1b5b839760a38` |
| `docs/01-discovery/INICIO-DISCOVERY.md` | `3585caafc3684c93e7cec9e424c2bf2b22a83488bcbb048bfe26ac3adada46cb` |
| `docs/chatgpt/PRIMEIRA-SESSAO.md` | `4431da66a878f0c8d4126c41f748e4a8f50620c595e521357027ea3fc594a0b4` |

## Disposição

A base documental examinada permite iniciar discovery exploratório C0/C1, preservadas as autorizações do fluxo específico de persistência. Não é especificação aprovada da IDE. Recomenda-se corrigir o P2 de F-020 e reexaminar somente o delta correspondente. F-024 deve permanecer Parcial enquanto a evidência original integral não estiver disponível; a limitação não deve ser ocultada por um estado de sucesso.


## Rechecagem independente do delta — P2-PROD-001 corrigido

Data: 30/10/2026. Escopo restrito à correção de `docs/fundacao/metodologia-fases.md`, ainda no diretório de trabalho sobre o commit-base `5f3a168849a9fc18a70e2dca9a20becb9ff39eb3`. SHA-256 da versão reexaminada: **`8d958a4ecd5feb44d03b8679224ea52d3f6e8243f5cda69dbee11942882a234a`**. Esta seção registra a versão corrigida separadamente; o achado e os hashes anteriores permanecem como evidência do snapshot original.

A nova tabela em `docs/fundacao/metodologia-fases.md:36–51` explicita entrada mínima, saída verificável e retorno quando o gate falhar para **todas as dez fases, 00–09**. A leitura do diff e a leitura integral do trecho confirmaram correspondência com os objetivos e gates anteriores. A fase 08 continua dependendo de plano autorizado e revisões exatas; a fase 09 mantém profissionais autorizados e bloqueio produtivo até os controles reais. Retornos preservam revisão e histórico, sem aprovação automática da versão alterada.

Uma checagem estrutural somente leitura confirmou dez linhas, IDs 00–09 sem lacunas, três campos preenchidos em cada fase e preservação integral do texto anterior fora do bloco acrescentado. Não foram encontrados problemas adicionais no delta examinado; não foi repetida a auditoria integral nem executado teste da futura plataforma.

**Disposição atualizada:** P2-PROD-001 está **corrigido no alcance documental**. F-020 passa de **Parcial** no snapshot original a **Documentado** nesta versão corrigida. A recomendação anterior de correção do P2 fica atendida. F-024 permanece **Parcial** pelos limites de proveniência já descritos. Não há P0/P1/P2 aberto identificado no escopo desta auditoria após esta rechecagem; isso não constitui garantia de ausência de defeitos ou aceite do produto.
