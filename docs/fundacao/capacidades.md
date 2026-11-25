# Catálogo inicial de capacidades e maturidade

Versão documental: 0.1.0 · 30/10/2026 · Fontes SRC-001 e SRC-002.

Este catálogo cobre a visão de produto e distingue o que foi documentado do que funciona. Não é uma lista de requisitos detalhados aprovados, backlog priorizado ou aceite da IDE. IDs CAP são estáveis; uma revisão deverá manter histórico se alterar escopo ou desdobrar uma capacidade.

## Como ler a maturidade

**Documentado:** intenção ou comportamento desejado consolidado com fonte. **Refinado:** critérios, estados e exceções especificados e revisados, ainda sem implicar aceite. **Aprovado:** decisão humana explícita vinculada à revisão e ao escopo exato. **Implementado:** componente executável identificável. **Verificado:** teste executado com resultado e evidência na versão indicada. **Integrado internamente:** adaptador real validado no ambiente do banco por autoridade competente.

Nenhuma capacidade da IDE nesta tabela está marcada implementada, verificada ou integrada. Provas isoladas do harness assistido serão avaliadas separadamente na auditoria da fundação. Fase e resultado futuro indicados são propostas de encaminhamento, não agenda aprovada.

| ID | Capacidade pretendida | Fonte/objetivo | Maturidade atual | Próximo refinamento e oráculo futuro | Dependências |
|---|---|---|---|---|---|
| CAP-001 | Workspaces com múltiplos repositórios e escopo autorizado | SRC-001/002; OBJ-001/002 | Documentado | Definir criação, seleção, remoção, permissões, identidade e estados vazios; demonstrar jornada com repositórios sintéticos | PEN-001, PEN-002 |
| CAP-002 | Análise e indexação de linguagens, frameworks, estruturas, dependências e propósito | SRC-001/002; OBJ-002 | Documentado | Explicitar cobertura e revisão-base, localizar evidência de cada inferência e detectar índice obsoleto | CAP-001; dados permitidos |
| CAP-003 | Contexto recuperável e roteamento por assunto, incluindo `AGENTS.md` | SRC-001/002; OBJ-002 | Documentado | Definir contexto mínimo suficiente, prioridades, conflitos e limites; recuperar fontes corretas sem depender do histórico do chat | CAP-002/008 |
| CAP-004 | Ingestão autorizada de reuniões, gravações, transcrições e anotações | SRC-001/002; OBJ-001/002 | Documentado | Definir consentimento, classificação, retenção, qualidade e atribuição; usar fontes sintéticas com proveniência | PEN-008/009; adaptador Teams |
| CAP-005 | Descoberta de requisitos, decisões, contradições, dúvidas e pendências | SRC-001/002; OBJ-002/004 | Documentado | Distinguir fala, hipótese e decisão; evitar promoção de brainstorm; comparar extração com fontes e revisão independente | CAP-003/004/008 |
| CAP-006 | Correlação da demanda com arquitetura, APIs, serviços, AWS e equipes | SRC-001/002; OBJ-002/006 | Documentado | Definir mapa de impacto com evidências, confiança, lacunas e revisão; testar relações falsas e dependências ausentes | CAP-002/005; PEN-003/008 |
| CAP-007 | Refinamento e especificação de requisitos de negócio, funcionais e não funcionais | SRC-001/002; OBJ-004 | Documentado | Cobrir regra, estado, exceção, dependência, fonte e critério de aceite; revisar ambiguidades e impactos | Método de sete etapas; CAP-005 |
| CAP-008 | Gestão de conhecimento, IDs, estados, proveniência, decisões e histórico | SRC-001/002; OBJ-002/004 | Documentado para a IDE | Especificar transições e autoria; preservar revisões e resolver divergências; não equiparar piloto C1 à capacidade final | Modelo do domínio; políticas aprovadas |
| CAP-009 | Planejamento de implementação, testes e validações com dependências e oráculos | SRC-001/002; OBJ-003/004 | Documentado | Mapear requisito→tarefa→teste e definir limite de tentativas, saída e escalonamento | CAP-007/008 |
| CAP-010 | Orquestração de agentes/subagentes com paralelismo útil e isolamento | SRC-001/002; OBJ-003 | Documentado | Especificar tarefa, arquivos, contexto, permissões, dependências, cancelamento e integração; testar colisões e recuperação | CAP-003/009/013 |
| CAP-011 | Devin CLI como executor especializado, sob coordenação da plataforma | SRC-001/002; OBJ-003 | Documentado; viabilidade não demonstrada | Confirmar contrato e disponibilidade; testar sucesso, erro, timeout, resultado incerto e troca por simulador | PEN-010; CAP-010/019 |
| CAP-012 | Implementação de código em mudanças isoladas, revisão e integração com GitHub/CI/CD | SRC-001/002; OBJ-003/004 | Documentado | Definir branches, PRs, status e limites por ambiente; conferir diff e revisão-base sem promover para produção | CAP-009/010/015 |
| CAP-013 | Supervisão humana com visibilidade, aprovação, redirecionamento e interrupção | SRC-001/002; OBJ-003 | Documentado | Definir autoridade, escopo e expiração de aprovação; distinguir cancelamento solicitado e confirmado; testar permissões | PEN-002; CAP-010/014 |
| CAP-014 | Experiência visual da IDE, navegação, componentes, estados e acessibilidade | SRC-001/002; OBJ-001/003 | Documentado; layout em aberto | Refinar jornadas e protótipos, incluindo erro, conflito, ausência de dados e recuperação; validar compreensão do usuário | PEN-001/002/011 |
| CAP-015 | Qualidade, revisão e testes independentes, regressões e efeitos colaterais | SRC-001/002; OBJ-004 | Documentado | Definir independência, cobertura, ambientes e oráculos; registrar falha e não executado sem falso sucesso | CAP-007/009/012 |
| CAP-016 | Rastreabilidade integral necessidade→decisão→requisito→mudança→teste→evidência | SRC-001/002; OBJ-002/004 | Documentado | Consultar cadeia em ambas as direções e detectar elos ausentes ou revisão incompatível | CAP-008/012/015 |
| CAP-017 | Diagnóstico de incidentes correlacionando ServiceNow, Datadog, AWS e repositórios | SRC-001/002; OBJ-006 | Documentado; integrações reais ausentes | Separar sintoma, hipótese e causa comprovada; testar dados incompletos, cronologia e acesso somente leitura | PEN-007/008; CAP-006/019 |
| CAP-018 | Preparação de correção/hotfix com testes e autorização produtiva explícita | SRC-001/002; OBJ-006 | Documentado; produção não autorizada | Especificar plano, evidência, rollback, GMUD, janela e aprovação; bloquear execução sem condições corporativas | CAP-013/015/017; PEN-007 |
| CAP-019 | Conectores desacoplados e substituíveis por simuladores | SRC-001/002; OBJ-005 | Documentado | Definir portas, schemas, erros, identidade, idempotência e versionamento; rodar testes de contrato por adaptador | PEN-005/006/008/010 |
| CAP-020 | Plataforma externa real, portátil, empacotada e pronta para internalização progressiva | SRC-001/002; OBJ-005 | Documentado; produto final não iniciado | Validar frontend/backend/persistência/motor/agentes/conectores com jornada completa; depois homologar internamente | Requisitos/arquitetura aprovados; CAP-001..019 |

## Cobertura de jornadas e frentes

| Jornada da visão | Capacidades principais | Áreas de especificação |
|---|---|---|
| JOR-001 — Workspace e compreensão técnica | CAP-001/002/003/006 | Descoberta técnica, arquitetura, contexto e UX |
| JOR-002 — Reunião/história para demanda compreendida | CAP-004/005/007/008/016/019 | Negócio, requisitos, fontes, conectores e dados |
| JOR-003 — Requisito para execução supervisionada | CAP-009/010/011/012/015/016 | Plano, execução, testes e integração |
| JOR-004 — Supervisão visual | CAP-013/014/016 | UX, permissões, estados e evidências |
| JOR-005 — Incidente/hotfix | CAP-006/017/018/019 | Operação, segurança, qualidade e internalização |

O contexto BAN-001..BAN-018 é insumo para descobrir contratos e restrições. Não cria obrigação de integrar todos esses sistemas na primeira versão. A prioridade e o recorte de MVP dependem de PEN-001; não foram escolhidos pelo assistente.

## Critério de evolução do catálogo

Para alterar a maturidade de uma capacidade, registrar: revisão do documento/requisito; decisão e autoridade quando houver aprovação; artefato executável e versão quando houver implementação; comando, ambiente, dados, oráculo, resultado e evidência quando houver teste; e autorização/ambiente corporativo quando houver integração interna. Uma demonstração visual, arquivo de configuração, teste com mock ou PR aberto comprova apenas seu alcance efetivo.

Os termos Implementado/Verificado/Parcial/Documentado/Ausente/Bloqueado/Não inspecionável/Fora do escopo usados na auditoria da missão qualificam entregáveis da fundação e suas provas. Não devem ser copiados automaticamente para a maturidade destas capacidades de produto.
