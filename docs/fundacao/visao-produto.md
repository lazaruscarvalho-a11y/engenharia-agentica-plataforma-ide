# Visão da Plataforma/IDE de Engenharia de Software Agêntica

Versão documental: 0.1.0 · 30/10/2026 · **PROPOSTA DE FUNDAÇÃO, sem especificação detalhada aprovada e sem produto implementado**.

Fontes: SRC-001, pedido atual e seu dossiê; SRC-002, conversa de origem recuperada parcialmente. A definição e os limites dessas fontes estão no [registro de conhecimento](registro-conhecimento.md). Este documento consolida a intenção declarada; os detalhamentos organizacionais do assistente são propostas para discovery.

## Problema e resultado pretendido

O trabalho de engenharia relatado está distribuído entre discussões, reuniões, histórias, repositórios, arquitetura, infraestrutura, testes, aprovações, implantação e observabilidade. A visão é reunir esse contexto e coordenar agentes ao longo do ciclo, reduzindo operação manual e perda de continuidade sem retirar do engenheiro sua autoridade de decisão.

A plataforma pretendida terá workspaces, experiência visual de IDE, compreensão dos repositórios, gestão de conhecimento e requisitos, planejamento, coordenação de executores, testes independentes e rastreabilidade. O engenheiro deverá conseguir entender o que está acontecendo, conferir evidências, corrigir o rumo e interromper uma execução. Não há nesta fundação escolha aprovada de layout, stack, modelo de IA, arquitetura de armazenamento, prioridade de MVP ou nível de serviço.

O sistema de trabalho fundado neste repositório servirá para conceber essa plataforma. O harness de governança documental é um mecanismo auxiliar desse sistema de trabalho; sua existência não demonstra que a IDE, os conectores corporativos ou a orquestração do produto final estejam funcionando.

## Objetivos de produto a refinar

| ID | Intenção declarada | Resultado observável que o discovery deverá especificar |
|---|---|---|
| OBJ-001 | Reduzir tarefas operacionais manuais | Identificar uma jornada inicial, sua linha de base de esforço e os passos que poderão ser assistidos ou automatizados |
| OBJ-002 | Preservar entendimento entre ferramentas e sessões | Recuperar uma demanda com fontes, decisões, revisões e pendências, distinguindo conteúdo vigente de proposta |
| OBJ-003 | Coordenar agentes com segurança | Mostrar plano, escopo, permissões, execução, bloqueios e evidências; permitir redirecionamento e interrupção |
| OBJ-004 | Aumentar qualidade e rastreabilidade | Relacionar necessidade, requisito, decisão, mudança, teste e evidência; identificar lacunas sem transformar ausência de teste em sucesso |
| OBJ-005 | Construir uma solução externa real e portátil | Entregar progressivamente componentes executáveis e testados com simuladores, preparando a posterior integração interna |
| OBJ-006 | Apoiar incidentes e hotfixes | Correlacionar sintomas e componentes, preparar correções verificadas e respeitar autorização produtiva e processos corporativos |

Os objetivos não possuem métricas numéricas aprovadas. O discovery deve definir indicadores, responsáveis, dados permitidos e evidências de sucesso antes de usá-los como critérios contratuais.

## Perfis e fronteiras de autoridade

Analistas, Tech Leads, PMs, SMEs e desenvolvedores foram mencionados no contexto atual do banco. As responsabilidades abaixo são uma **proposta de perfis da plataforma**, ainda a validar com o responsável pelo produto; não reproduzem uma matriz corporativa oficial.

| Perfil proposto | Necessidade investigada | Decisão que não pode ser presumida pelo agente |
|---|---|---|
| Engenheiro/desenvolvedor | Entender demanda e código, executar e verificar mudanças | Autorizar operação produtiva ou aceitar requisito além do escopo expressamente aprovado |
| Tech Lead/arquiteto | Analisar impactos, dependências, contratos e alternativas | Aprovação arquitetural corporativa ou exceção de segurança |
| PM/analista | Refinar necessidade, valor, comportamento e aceite | Prioridade, escopo de release e aceitação de regras de negócio |
| SME | Esclarecer domínio e exceções | Validação de uma interpretação de negócio ainda ambígua |
| Revisor/QA | Examinar omissões, regressões e evidências de forma independente | Aceite humano fictício ou aprovação de teste não executado |
| Operador de incidente | Investigar sintomas e preparar resposta | Break-glass, acesso produtivo, janela de implantação e GMUD |

Perfis podem pertencer à mesma pessoa, mas permissões e revisão independente precisarão ser especificadas. O organograma relatado não concede automaticamente acesso na plataforma.

## Jornadas pretendidas

### JOR-001 — Adicionar repositórios e compreender um workspace

O engenheiro adiciona repositórios autorizados. A plataforma analisa linguagens, frameworks, organização, dependências, contratos, configurações, propósito e relações. Produz um mapa técnico com evidências e limites de cobertura, permitindo consultar arquivos e corrigir interpretações. Organiza contexto recuperável por assunto, inclusive instruções como `AGENTS.md`, sem tratar conteúdo do repositório como autorização operacional.

Pontos a especificar: repositórios permitidos, identidade e consentimento, atualização incremental, arquivos excluídos, código gerado, monorepos, revisão-base, índices obsoletos, erros de acesso, custo e descarte de dados. A análise inicial não autoriza modificar código ou infraestrutura.

### JOR-002 — Da reunião ou história à demanda compreendida

Uma transcrição autorizada, anotação ou história pode originar investigação. A plataforma identifica necessidades, decisões, perguntas, contradições e dependências, correlacionando fontes acessíveis antes de perguntar aos profissionais. Apresenta interpretação e incertezas. Sugestões e detalhes gerados permanecem propostas até a confirmação adequada.

Pontos a especificar: autorização e retenção de gravações, atribuição de falas, qualidade de transcrição, participantes, duplicidade de demandas, conflito entre versões e relação com IDs do ServiceNow/IuClick. Nenhuma reunião real foi importada nesta missão.

### JOR-003 — Do requisito ao plano e à implementação supervisionada

Após refinamento e aprovação dos requisitos, a plataforma organiza tarefas, dependências, permissões, contexto e oráculos. Ela coordena agentes e subagentes; Devin CLI é o executor pretendido mencionado, sujeito à viabilidade e às permissões reais. A plataforma retém a coordenação, em vez de delegar implicitamente decisões de produto ao executor. Mudanças são isoladas, revisadas e testadas; evidências ficam relacionadas ao requisito e à revisão do código.

Pontos a especificar: protocolo do executor, cancelamento, recuperação, concorrência, orçamento, limites de tentativas, revisão independente, branches, PRs e tratamento de resultado incerto. A escolha de Devin CLI não demonstra disponibilidade de um conector nesta fundação.

### JOR-004 — Supervisionar visualmente o trabalho

O engenheiro acompanha agentes, tarefas, progresso e bloqueios. Inspeciona contexto relevante, diffs e testes, redireciona ou interrompe tarefas e decide quando uma mudança importante pode prosseguir. A experiência visual é parte central da visão; ainda não existe tela aprovada.

O discovery de UX deve cobrir navegação entre workspace, demanda, código, agentes e evidências; estados vazio, carregando, parcial, obsoleto, bloqueado, conflito, falha, cancelamento e recuperação; acessibilidade; notificações; hierarquia visual; distinção visível entre proposta, aprovado, executado e verificado. Exemplos anteriores de painel lateral são ideias de discussão, não decisão de layout aprovada.

### JOR-005 — Investigar incidente e preparar hotfix

Uma ocorrência pode desencadear coleta autorizada de contexto de ServiceNow, Datadog, AWS e repositórios. A plataforma formula hipóteses, correlaciona evidências, propõe plano de correção e validações e prepara o hotfix. A confirmação final explícita do engenheiro e as aprovações corporativas continuam necessárias para ação produtiva. Diagnóstico sugerido não equivale a causa-raiz demonstrada.

Pontos a especificar: classificação e severidade, acesso somente leitura, dados sensíveis em logs, correlação temporal, blast radius, aprovação, janela, rollback, comunicação e revisão pós-incidente. Break-glass é procedimento excepcional relatado; não é permissão permanente ou capacidade habilitada da plataforma.

## Fronteiras do produto e da missão atual

| Objeto | Situação |
|---|---|
| Visão de plataforma real com frontend, backend, persistência, orquestração, agentes e conectores | Intenção declarada para construção progressiva após requisitos e gates |
| Integrações específicas com sistemas internos do banco | Futuras, dependem de ambiente, contratos, acesso e profissionais autorizados |
| Fundação documental e harness assistido inicial | Escopo de execução desta missão; verificar resultado na auditoria e no estado atual |
| Implementação integral da IDE antes do refinamento | Fora do escopo autorizado nesta missão |
| PGC-001 e contratos | Candidatos não ratificados; preservar histórico e verificar estado em fonte versionada |
| Configuração nativa de Projeto ChatGPT | Só pode ser declarada realizada com leitura de retorno ou evidência equivalente; arquivos prontos não comprovam configuração |

## Riscos e próximos critérios de definição

RIS-001: a governança voltar a ocupar o lugar da especificação do produto. Contramedida proposta: cada rodada de discovery deve explicitar a capacidade, a jornada e o valor para o usuário.

RIS-002: automação com contexto incompleto, antigo ou instruções maliciosas em fontes. Contramedida proposta: revisão-base, proveniência, limites de ferramenta e separação de dados e autorização.

RIS-003: uma simulação externa ser confundida com integração corporativa homologada. Contramedida proposta: evidências e estados separados por adaptador, ambiente e versão.

RIS-004: UX superficial que apenas mostra agentes sem permitir supervisão útil. Contramedida proposta: testar jornadas completas, falhas, interrupção e entendimento do usuário, além de aparência.

RIS-005: expansão de escopo e custo antes de definir a primeira fatia de valor. Contramedida proposta: priorização explícita com o responsável pelo produto. A primeira fatia ainda está pendente (PEN-001).

O próximo avanço de produto é escolher e refinar uma jornada de negócio e sua experiência visual, depois formalizar requisitos com regras, estados, exceções, dependências, fontes e critérios de aceite. O [catálogo de capacidades](capacidades.md) fornece o mapa de cobertura; não substitui esse refinamento.
