# Registro de conhecimento, decisões, hipóteses e pendências

Versão documental: 0.1.0 · 30/10/2026 · **Consolidação inicial com limites de proveniência explícitos**.

## Fontes e limites

| ID | Fonte | Alcance efetivamente disponível | Limite |
|---|---|---|---|
| SRC-001 | Pedido atual do usuário nesta missão, de 30/10/2026, incluindo o dossiê e limites de autorização | Instrução direta para executar PM-FUND-001→002→003, preservar trabalho, implementar fundação e preparar discovery | O dossiê resume relatos anteriores; não é evidência institucional dos processos do banco |
| SRC-002 | Conversa `6add5e12-021c-83e8-9d16-2a4917ea9700`, “Reescrita do fluxo de trabalho”, recuperada por `read_thread` | Cinco turnos disponíveis; respostas sobre dinâmica, Instruções/Fontes, lacuna e Prompts-Mestres | Resposta `ecf720a8-dc21-4bdf-82e5-9bb590be4f7d` limitada a 20.000 caracteres; recuperação não contém a transcrição integral inicial de concepção |
| SRC-003 | Repositório privado `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`, inventário remoto da missão | Branches, PRs e arquivos consultados em revisões identificáveis | Estado observado muda; verificar commit e branch antes de persistir; arquivo em branch não está necessariamente em `main` |

Referência navegável de SRC-002: [conversa de origem](chatgpt-conversation://6add5e12-021c-83e8-9d16-2a4917ea9700). Fontes de SRC-003 devem usar links e SHAs do inventário/recibo da missão; não usar o título de um PR como prova de comportamento.

Âncoras úteis de SRC-002:

- `2469f322-1dd2-43be-bc02-39d671fe99f7`: dinâmica de conversas naturais, formalização gradual, recuperação e persistência assistida.
- `6d528f60-f7f9-4ee7-a952-e3ab5c453bb6`: papéis distintos de Instruções, Fontes e GitHub, sem supor sincronização.
- `6739f6d0-965a-410f-96fd-ecd801b37b11`: diagnóstico de concentração na governança e falta de transferência integral de contexto.
- `ecf720a8-dc21-4bdf-82e5-9bb590be4f7d`: dossiê e PM-FUND-001 na parte recuperada; o fim do conteúdo não está integralmente disponível.
- `9e271389-9ab1-4809-8098-8a331a7d05a8`: afirmação histórica de encaminhamento; não é prova de execução nem de resultado desta missão.

Não foi possível reconstruir exaustivamente todas as falas originais de produto a partir desse retorno. A reconciliação usa SRC-001 e a parcela disponível de SRC-002, sem inventar citações ou aprovações anteriores. O usuário não precisa reconstituir o histórico para a fundação prosseguir; qualquer ausência material permanece registrada como pendência.

## Classes de conhecimento

| Classe | Significado | Regra de uso |
|---|---|---|
| FATO OBSERVADO | Estado conferido diretamente em ferramenta e revisão identificada | Associar evidência, data, escopo e limite da observação |
| FATO RELATADO | Informação atribuída ao usuário ou outra fonte, sem inspeção institucional | Preservar atribuição e incerteza; não generalizar |
| INTENÇÃO DECLARADA | Direção ou comportamento desejado pelo usuário | Orienta discovery, sem aprovar todos os detalhes funcionais |
| DECISÃO EXPLÍCITA | Escolha ou autorização inequívoca com escopo delimitado | Vincular fonte/revisão; não ampliar para detalhes derivados |
| HIPÓTESE | Explicação ou desenho que precisa de validação | Identificar teste ou pergunta que poderá confirmar/refutar |
| RECOMENDAÇÃO | Proposta do assistente ou revisor | Não atribuir aceite humano sem manifestação correspondente |
| PENDÊNCIA | Dado, decisão ou evidência ainda ausente | Registrar impacto, próximo passo e se bloqueia alguma ação |

Estados de trabalho propostos: capturado → em refinamento → em revisão → aprovado no escopo explícito → substituído ou revogado. Rejeitado e suspenso também devem ser preservados. Publicado, implementado e verificado são dimensões separadas: publicar uma proposta não a aprova; executar um teste não ratifica uma política.

## Decisões e intenções delimitadas

| ID | Registro | Classe/estado | Fonte | Alcance e limite |
|---|---|---|---|---|
| DEC-FUND-001 | Executar a missão integral de fundação, auditoria e inicialização com autonomia útil | Decisão explícita para esta missão | SRC-001 | Autoriza trabalho ordinário reversível, branch, commits, PRs, testes e agentes; não autoriza merge, ratificação ou mudança de permissões |
| DEC-FUND-002 | Preservar trabalho anterior, revalidar o remoto e manter distinção entre branches e `main` | Decisão explícita para esta missão | SRC-001 | Não sobrescrever pacotes/histórico nem tratar presença em branch como vigência |
| DEC-FUND-003 | Preparar e testar fundação e harness assistido inicial reutilizando piloto | Decisão explícita para esta missão | SRC-001 | C0/C1 exploratório, dados sintéticos, sem ativação normativa C2/C3; resultado depende de evidência |
| DEC-FUND-004 | Não desenvolver a IDE final antes de refinar e aprovar requisitos | Decisão explícita para esta missão | SRC-001 | Permite testes técnicos isolados para a fundação; não autoriza preencher lacunas materiais de produto por conveniência |
| DEC-FUND-005 | GitHub é a referência versionada; Instruções enxutas e Fontes curadas apoiam sessões | Intenção declarada reconfirmada no pedido | SRC-001/002 | Fontes carregadas são cópias com versão; não presumir sincronização ou configuração nativa efetiva |
| INT-001 | Construir Plataforma/IDE agêntica real com supervisão humana, agentes e rastreabilidade | Intenção declarada | SRC-001/002 | Visão consolidada; critérios e prioridade de cada capacidade ainda pendentes |
| INT-002 | Construir externamente componentes reais e desacoplados; integrar sistemas específicos internamente | Intenção declarada | SRC-001/002 | Não pressupõe acesso corporativo nem escolha tecnológica aprovada |
| INT-003 | Usar metodologia de sete etapas e organizar fases 00–09 | Método declarado e organização solicitada nesta missão | SRC-001/002 | Detalhes de gates e artefatos propostos pelos agentes devem continuar identificados como proposta |
| INT-004 | Conversar naturalmente e formalizar progressivamente ideias, requisitos e decisões | Intenção declarada | SRC-001/002 | Brainstorm e concordância genérica não aprovam detalhes adicionados depois |

DEC-FUND registra autorização de trabalho, não um registro de ratificação do PGC. Nenhuma assinatura ou aceite humano é preenchido por este arquivo.

## Hipóteses e recomendações para validar

| ID | Proposição | Natureza | Como validar/refutar |
|---|---|---|---|
| HIP-001 | Uma jornada inicial pequena poderá reduzir esforço e revelar contratos antes de ampliar módulos | Recomendação de engenharia | Comparar valor, risco e esforço de jornadas no discovery; decisão do responsável pelo produto |
| HIP-002 | Portas de domínio e simuladores substituíveis facilitarão internalização | Recomendação arquitetural | Testes de contrato e prova de substituição após requisitos/arquitetura; confrontar contratos internos reais |
| HIP-003 | Mapa de evidências e revisões reduzirá interpretações incorretas de agentes | Hipótese de qualidade | Ensaios com fontes conflitantes/obsoletas e avaliação independente |
| HIP-004 | Acompanhamento visual por agentes/tarefas permitirá supervisão útil | Hipótese de UX | Protótipos e tarefas com usuários; medir entendimento, redirecionamento e interrupção |
| HIP-005 | Devin CLI atenderá ao papel de executor especializado da plataforma | Hipótese de viabilidade sobre mecanismo pretendido | Confirmar disponibilidade, contrato, permissões, erros, custo e testes isolados; não presumir integração |

Não há decisão aprovada de MVP, layout lateral, banco de dados, framework frontend, barramento, cloud externa, modelo de IA ou tecnologia de busca nesta consolidação.

## Pendências de produto, contexto e acesso

| ID | Questão | Impacto | Próxima ação e condição de bloqueio |
|---|---|---|---|
| PEN-001 | Qual jornada e problema têm prioridade para a primeira fatia de produto? | Escopo, valor e sequência | Refinar com responsável pelo produto no discovery; bloqueia priorização material, não documentação da visão |
| PEN-002 | Quem usa, decide, revisa e aprova em cada jornada? | Perfis, permissões e UX | Mapear atores e cenários; bloqueia modelo definitivo de autoridade |
| PEN-003 | Quais partes do relato valem para quais squads/aplicações? | Fidelidade ao ambiente atual | Obter exemplos e fontes autorizadas; bloqueia generalização institucional |
| PEN-004 | O que fazem IUQuali, TAAC e TestSpec e como se relacionam? | Qualidade e integração | Consultar responsável/documento interno autorizado; não inventar funções |
| PEN-005 | Quais schemas, estados e APIs reais regem ServiceNow/IuClick? | Conector e domínio de demanda | Descobrir contrato internamente; simulador externo deve continuar declarado proposto |
| PEN-006 | Quais contratos reais regem provisionamento, `iupipes.yml`, sigla app e Defect Dojo? | Onboarding de aplicações e integração | Validar templates/esquemas autorizados; bloqueia integração real |
| PEN-007 | Quais gates regem GMUD, hotfix, produção, rollback e break-glass? | Segurança e operação | Confirmar processo e responsáveis internos; bloqueia ação produtiva |
| PEN-008 | Quais dados e acessos serão permitidos por ambiente/conector? | Segurança, retenção e arquitetura | Política e acesso autorizados internamente; externo continua sintético |
| PEN-009 | Como autorizar, reter e interpretar reuniões/transcrições? | Privacidade, qualidade e proveniência | Definir escopo, consentimento e critérios; não importar dados reais sem autorização |
| PEN-010 | Devin CLI estará disponível e adequado? | Executor/orquestração | Verificação técnica e contratual; não bloqueia interface abstrata e mocks propostos |
| PEN-011 | Qual UX, navegação, layout e comportamento de supervisão atendem aos perfis? | Especificação visual e funcional | Jornadas, protótipos e revisão; não selecionar layout implicitamente |
| PEN-012 | Quais RNFs, stack, distribuição e requisitos de internalização serão adotados? | Arquitetura e empacotamento | Refinar fases 04/05/09; bloqueia arquitetura definitiva, não discovery |
| PEN-013 | Há fonte integral anterior além dos cinco turnos recuperados? | Exaustividade de proveniência | Incorporar se ficar acessível; registrar divergências; não alegar recuperação exaustiva |
| PEN-014 | Ratificação do PGC e aceite operacional completo do piloto estão pendentes | Governança | Revisão humana conforme escopo e controles aplicáveis; esta missão não ratifica nem preenche aceite |
| PEN-015 | Configuração nativa de Instruções/Fontes está efetivamente acessível? | Inicialização do Projeto ChatGPT | Inspecionar controle disponível; declarar NÃO CONFIGURADO sem prova de escrita/releitura |

## Preservação e evolução

Cada novo registro deve conter ID estável, classe, conteúdo, fonte localizável, revisão, estado, relações e limites de autoridade. Mudança de entendimento deve preservar o registro anterior e explicar substituição, impacto e evidência. Não renumerar IDs para ocultar rejeições ou duplicidades.

Ao propor um requisito, vincular a capacidade CAP, jornada JOR, objetivo OBJ e fontes; registrar regras, estados, exceções, dependências e critérios de aceite. Quando uma decisão for parcial, apenas os itens inequivocamente cobertos podem mudar de estado. Detalhes do assistente continuam propostas. Conflitos ou revisão antiga exigem reconciliação, sem reaproveitar automaticamente aceite de outro conteúdo.

A persistência deve ser confirmada no destino por revisão e hashes; uma promessa em conversa ou arquivo local não é recibo de GitHub. Uma sessão nova deve recuperar o estado a partir de fontes versionadas e verificar sua revisão, sem presumir acesso ao histórico ou sincronização automática.
