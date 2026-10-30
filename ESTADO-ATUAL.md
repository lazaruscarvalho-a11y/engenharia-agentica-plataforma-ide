# Estado integral — 30/10/2026
Fundação em branch de proposta `proposta/fundacao-integral-pm-fund-001-003`, derivada de `piloto/governanca-assistida` em f2189bf9481a48fb6281844326d35501952ebd0e. main observado: ba820cbb7b92bd570e4848c4ca7eff48c44f04cd, só .gitkeep. Nenhum merge autorizado.

## Produto e fase
Queremos uma Plataforma/IDE corporativa que coordene conhecimento, discovery, repositórios, engenharia, agentes, testes e operação supervisionada. [Visão](docs/fundacao/visao-produto.md), [capacidades](docs/fundacao/capacidades.md) e [construção externa/internalização](docs/fundacao/construcao-internalizacao.md) descrevem intenção e maturidade; frontend/backend/IDE final NÃO IMPLEMENTADOS nesta missão. Escolhas de tecnologia, requisitos detalhados, UX e métricas aguardam discovery e aprovação de produto.

Fase 00: documentação e harness inicial preparados para revisão e auditoria. Fase 01: [primeira sessão de discovery pronta](docs/01-discovery/INICIO-DISCOVERY.md); pode começar como exploração C0/C1 sem ratificação normativa. Fases 02–09: [mapa e gates](docs/fundacao/metodologia-fases.md), sem execução antecipada.

## Conhecimento e continuidade
[Ecossistema atual](docs/fundacao/ecossistema-atual.md) contém relatos do banco, não verificação interna ou requisitos da IDE. [Registro](docs/fundacao/registro-conhecimento.md) distingue decisões de intenção, hipóteses e pendências. Fontes SRC-001/002/003 e limitação do histórico constam do [inventário](auditorias/fundacao-integral/INVENTARIO.md). A conversa recuperada tem cinco turnos, um truncado; não foi possível recuperar toda a transcrição original.

[Protocolo de sessões](docs/fundacao/protocolo-sessoes.md) e [roteamento](docs/fundacao/roteamento-contexto.md) orientam recuperação por documentos e revisão exata. Só alegar persistência com recibo e releitura do destino. Não há captura contínua de todas as conversas nem sincronização automática das Fontes.

## ChatGPT
[Instruções permanentes](docs/chatgpt/INSTRUCOES-PERMANENTES.md) prontas; manifesto e procedimento estão em docs/chatgpt. **Projeto NÃO CONFIGURADO nesta missão:** conector não expõe edição de Instruções/Fontes; navegador acessível mostra login e não possui sessão autenticada. O projeto retornado por list_projects é de outro assunto. Nenhum projeto foi criado, alterado ou recebido fontes.

## Governança e harness
PGC-001 v1.1.3 e CT-001..CT-008 v1.0.3 continuam PROPOSTOS/NÃO RATIFICADOS. v1.1.2, ZIPs e recibos históricos preservados. PRs #1–#4 permanecem encadeados; esta proposta depende de #4. Aprovação de PR não é ratificação. Nenhum manifesto de ativação ou aceite humano foi preenchido.

[Piloto C1 original](harness/governanca_assistida/OPERACAO.md): preparação, verificação, diário, Gateway assistido e recibos. GOV-REG-0001 tem aceite exploratório histórico específico, preservado; não aceita outras revisões ou este incremento. Aceite operacional completo do piloto permanece pendente.

[Extensão da fundação](harness/governanca_assistida/OPERACAO-FUNDACAO.md): captura C0 e adaptador SQLite LOCAL/SINTÉTICO para ensaiar o contrato C1 existente. Não é conector remoto novo nem autenticação humana. Não habilita C2/C3, produção ou publicação normativa. Fonte documental nunca concede permissão.

## Verificação e riscos
A [matriz](auditorias/fundacao-integral/MATRIZ-COBERTURA.md) e o [relatório final](auditorias/fundacao-integral/RELATORIO-FINAL.md) distinguem documentação, implementação local e evidência executada. Relatórios anteriores são históricos, não prova transferível. Os 49 CA operacionais PGC permanecem NOT_RUN. Recuperação por outro processo é ensaio técnico; nova conversa real de usuário é distinta.

GET proteção main retornou 403; branch lista protected=false; rulesets retornam 403 de disponibilidade de plano. Não foi alterada qualquer configuração administrativa. Usar só dados sintéticos; sem credenciais ou material interno.

## Próxima ação e decisões humanas
Pode-se iniciar agora discovery pela pergunta inicial do roteiro, nesta conversa, usando a branch proposta como snapshot e sem promover ideias a requisitos aprovados. Configurar o Projeto ChatGPT exige sessão autenticada/interface autorizada, com pacote já preparado. Revisar/mesclar a cadeia de PRs e eventual ratificação são decisões humanas separadas, sem necessidade de interromper brainstorm ou discovery. Ambiguidades de produto serão resolvidas durante o refinamento, não inventadas nesta fundação.

