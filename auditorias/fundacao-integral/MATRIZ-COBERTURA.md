# Matriz inicial de cobertura

Fonte SRC-001 (pedido desta missão), detalhada por obrigação. Estados serão reavaliados na auditoria. Documentado descreve intenção/processo, não comportamento da IDE. Implementado e Verificado exigem evidência executável. Parcial indica parte demonstrada. Bloqueado depende de acesso; Não inspecionável indica ferramenta sem visibilidade; Ausente e Fora do escopo não são sucesso.

|ID|Obrigação|Arquivo|Estado inicial|
|---|---|---|---|
|F-001|Visão integral e lacuna além do PGC|[fonte](../../docs/fundacao/visao-produto.md)|Documentado|
|F-002|Banco: squads, hierarquia, PM/TL/SME e reuniões Teams|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-003|ServiceNow/IuClick: features, histórias, bugs, tasks|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-004|Provisionamento GitHub via issue e iupipes.yml|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-005|Terraform e AWS DEV/HOM/PROD|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-006|Defect Dojo, sigla app e aprovação arquitetural|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-007|Sonar; IUQuali/TAAC/TestSpec com incerteza preservada|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-008|feature→develop→release/HOM→main/PROD; GMUD, janela, incidentes/hotfix, Datadog, break-glass|[fonte](../../docs/fundacao/ecossistema-atual.md)|Documentado|
|F-009|Workspaces, indexação e análise de repositórios|[fonte](../../docs/fundacao/capacidades.md)|Documentado|
|F-010|AGENTS e contexto ótimo/mínimo suficiente|[fonte](../../docs/fundacao/roteamento-contexto.md)|Documentado|
|F-011|Ingestão autorizada reuniões, requisitos, decisões, dúvidas/contradições|[fonte](../../docs/fundacao/capacidades.md)|Documentado|
|F-012|Correlação histórias, arquitetura, APIs, AWS e equipes|[fonte](../../docs/fundacao/capacidades.md)|Documentado|
|F-013|Plataforma coordenadora, Devin CLI executor; agentes/subagentes|[fonte](../../docs/fundacao/visao-produto.md)|Documentado|
|F-014|Supervisão, interrupção, testes independentes e rastreabilidade|[fonte](../../docs/fundacao/capacidades.md)|Documentado|
|F-015|Diagnóstico incidente e hotfix produtivo com autorização específica|[fonte](../../docs/fundacao/construcao-internalizacao.md)|Documentado|
|F-016|Construção futura externa REAL: frontend/backend/persistência/orquestração/agentes|[fonte](../../docs/fundacao/construcao-internalizacao.md)|Documentado|
|F-017|Conectores desacoplados, mocks, contratos, testes, docs e empacotamento|[fonte](../../docs/fundacao/construcao-internalizacao.md)|Documentado|
|F-018|Internalização posterior por autorizados; sem dados/serviços internos agora|[fonte](../../docs/fundacao/construcao-internalizacao.md)|Documentado|
|F-019|Sete etapas da metodologia do usuário|[fonte](../../docs/fundacao/metodologia-fases.md)|Documentado|
|F-020|Fases 00–09 com entradas/saídas/gates/retornos|[fonte](../../docs/fundacao/metodologia-fases.md)|Documentado|
|F-021|Negócio, perfis, jornadas, funcionalidades e UX visual da IDE|[fonte](../../docs/01-discovery/INICIO-DISCOVERY.md)|Documentado|
|F-022|Conversa natural: brainstorm não aprova; detalhes não herdam aprovação|[fonte](../../docs/fundacao/protocolo-sessoes.md)|Documentado|
|F-023|IDs, estados, revisão de decisões/documentos, hipóteses e pendências|[fonte](../../docs/fundacao/registro-conhecimento.md)|Documentado|
|F-024|Proveniência original disponível e limitação do histórico|[fonte](../../auditorias/fundacao-integral/INVENTARIO.md)|Parcial|
|F-025|Inventário main/PRs/commits/arquivos, integridade e permissões reais|[fonte](../../auditorias/fundacao-integral/baseline-remoto.json)|Verificado|
|F-026|Branch/PR revisável, trabalho anterior e cadeia preservados|[fonte](../../auditorias/fundacao-integral/INVENTARIO.md)|Parcial|
|F-027|README/AGENTS/ESTADO abrangendo produto inteiro|[fonte](../../README.md)|Documentado|
|F-028|Instruções Permanentes exatas e enxutas|[fonte](../../docs/chatgpt/INSTRUCOES-PERMANENTES.md)|Documentado|
|F-029|Manifesto curado: prioridades/versões/limites e ausência de sync automática|[fonte](../../docs/chatgpt/MANIFESTO-FONTES.md)|Documentado|
|F-030|Projeto ChatGPT efetivamente configurado ou pendência honesta|[fonte](../../docs/chatgpt/CONFIGURACAO.md)|Bloqueado|
|F-031|Reutilizar piloto C1 sem falsificar aceite/ratificação|[fonte](../../harness/governanca_assistida/fluxo.py)|Verificado|
|F-032|C0/C1 exploratório: IDs/esquemas/proveniência/propostas/decisões|[fonte](../../harness/governanca_assistida/fundacao.py)|Parcial|
|F-033|Preparação changeset, aprovação delimitada e bloqueio C2/C3|[fonte](../../harness/governanca_assistida/fundacao.py)|Parcial|
|F-034|CAS, revisão antiga e concorrência|[fonte](../../harness/governanca_assistida/test_fundacao.py)|Parcial|
|F-035|Idempotência e conflito de payload/operation ID|[fonte](../../harness/governanca_assistida/test_fundacao.py)|Parcial|
|F-036|Escrita/releitura, recibos, persistência e recuperação de outro processo|[fonte](../../harness/governanca_assistida/test_fundacao.py)|Parcial|
|F-037|Timeouts e falhas antes/depois da gravação; sem repetição cega|[fonte](../../harness/governanca_assistida/test_fundacao.py)|Parcial|
|F-038|Aprovação parcial, ambígua, fonte indireta e revisão alterada|[fonte](../../harness/governanca_assistida/test_fluxo.py)|Verificado|
|F-039|Injeções, sensíveis sintéticos, perda de contexto|[fonte](../../harness/governanca_assistida/test_fundacao.py)|Parcial|
|F-040|Verificações documentais executáveis|[fonte](../../harness/verificar_fundacao.py)|Parcial|
|F-041|Auditoria independente após congelar arquivos, com correção P0/P1|[fonte](../../auditorias/fundacao-integral/RELATORIO-FINAL.md)|Parcial|
|F-042|49 CA PGC sem falsa aprovação operacional|[fonte](../../docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/verificacoes/casos-adversariais.json)|Verificado|
|F-043|Nova conversa independente sem respostas antecipadas se possível|[fonte](../../auditorias/fundacao-integral/RELATORIO-FINAL.md)|Parcial|
|F-044|Segurança/permissões, sem merge/ratificação/ativação/mudanças de proteção|[fonte](../../auditorias/fundacao-integral/RELATORIO-FINAL.md)|Parcial|
|F-045|Primeira sessão discovery pronta e critérios formalização/aceitação|[fonte](../../docs/01-discovery/INICIO-DISCOVERY.md)|Documentado|
|F-046|Orquestração com arquivos exclusivos, interfaces e auditores distintos|[fonte](../../auditorias/fundacao-integral/INVENTARIO.md)|Verificado|
|F-047|Recibo remoto SHA/PR/releitura de arquivos e main inalterada|[fonte](../../auditorias/fundacao-integral/RECIBO-PUBLICACAO.json)|Parcial|
|F-048|Não desenvolver IDE final antes refinamento/aprovação|[fonte](../../ESTADO-ATUAL.md)|Verificado|
