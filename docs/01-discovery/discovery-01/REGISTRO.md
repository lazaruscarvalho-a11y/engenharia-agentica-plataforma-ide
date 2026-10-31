# Registro de definições — revisão 2 (D01-R2)

Registro canônico exploratório do Discovery 01. A revisão 1 permanece no [commit anterior](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/d9e48c3d36598d40f9d2e38caf836bccb5fac97f/docs/01-discovery/discovery-01/REGISTRO.md); alterações de classificação e desdobramentos constam de [RETIFICACOES.md](RETIFICACOES.md). Não há requisitos normativos aprovados, ratificação ou implementação por este registro.

## Proveniência e escopo

D01-S05 = declarações reproduzidas pelo usuário no pedido atual D01-R2 v2.0, arquivadas por âncora em [DOSSIE-REPRODUZIDO.md](../../../auditorias/discovery-01-r2/DOSSIE-REPRODUZIDO.md). A reprodução é suficiente para reconciliar materialmente a intenção/decisão declarada, mas **não comprova recuperação técnica da mensagem histórica original**. E01..E36 não são IDs de mensagens. Fontes D01-S02-A..E são as mensagens efetivamente recuperadas na revisão 1; não se inventa nova recuperação dessas falas nesta revisão.

IDs são identidades históricas estáveis, não tipos imutáveis: REL-001..008 conservam prefixo, agora com natureza retificada e evidência reproduzida; REL-009 é agrupador histórico desdobrado. Todas as definições abaixo têm revisão 2 documental e maturidade **EM DISCOVERY**. Decisão delimitada significa escolha de produto no escopo reproduzido, sem aprovar detalhes derivados. Publicação, aprovação, implementação e vigência são dimensões separadas.

## Definições reconciliadas por âncora

<a id="d01-int-001"></a>

### D01-INT-001 — Objetivo central do onboarding

**Revisão:** 2 · **Natureza:** Intenção explícita de produto · **Estado:** em discovery; escopo declarado preservado.

Importar, absorver, compreender, estruturar e utilizar o conhecimento de um ou mais repositórios, independentemente de organização, natureza, finalidade, linguagens ou tecnologias. Esse conhecimento subsidia explicações, esclarecimentos, investigação, planejamento, modificações de código, validações e demais funcionalidades. Não é garantia de compreensão perfeita de qualquer sistema.

**Fonte:** D01-S05/E01 (declaração reproduzida no pedido atual).

**Relações:** CAP-001, CAP-002, CAP-006, CAP-008; pendências D01-PEN-001, D01-PEN-007. Propostas/hipóteses derivadas: D01-PROP-012, D01-PROP-021.

<a id="d01-rel-001"></a>

### D01-REL-001 — Compreensão inicial profunda e contínua

**Revisão:** 2 · **Natureza:** Intenção explícita reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Buscar entendimento semelhante ao de um engenheiro experiente após estudar profundamente o sistema: finalidade/contexto de negócio, regras de negócio, fluxos/comportamentos, arquitetura/responsabilidades, linguagens/frameworks, componentes/estruturas, integrações/contratos, dependências internas/externas, infraestrutura/configurações, execução local, estratégias/procedimentos de testes, particularidades, limitações e riscos. Combinar investigação inicial ampla e enriquecimento incremental; aprofundar quanto viável e explicitar cobertura e limitações. Documentar execução local não a autoriza.

**Fonte:** D01-S05/E02 (declaração reproduzida no pedido atual).

**Relações:** CAP-002, CAP-006; pendências D01-PEN-001, D01-PEN-007. Propostas/hipóteses derivadas: D01-PROP-012, D01-PROP-021.

<a id="d01-rst-001"></a>

### D01-RST-001 — Execução local reservada ao engenheiro

**Revisão:** 2 · **Natureza:** Restrição expressa reproduzida · **Estado:** em discovery; escopo declarado preservado.

A decisão de executar a aplicação localmente cabe exclusivamente ao engenheiro responsável. A Plataforma pode documentar procedimentos e preparar análises; não pode instalar dependências, subir aplicações ou executar inicialização por iniciativa própria com base nessa intenção. Outras ações executáveis seguem suas autorizações próprias. Este registro não executa aplicação.

**Fonte:** D01-S05/E03 (declaração reproduzida no pedido atual).

**Relações:** CAP-013; pendências D01-PEN-001, D01-PEN-004, D01-PEN-008. Detalhamento técnico não escolhido por este registro.

<a id="d01-int-002"></a>

### D01-INT-002 — Paradigma Agent-First

**Revisão:** 2 · **Natureza:** Intenção explícita de produto · **Estado:** em discovery; escopo declarado preservado.

Preparar repositórios incorporados segundo Agent-First, relacionado pelo usuário a AI-centric, AI-based, Specification-Driven Development, Harness Engineering e AI-intent. Conhecimento concreto, conciso, hierarquizado, estruturado, padronizado e otimizado para consumo/atualização por agentes. A intenção inclui AGENTS.md, diretórios especializados, índices, esquemas e artefatos estruturados; não aprova árvore definitiva, schema específico nem armazenamento técnico.

**Fonte:** D01-S05/E04 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-008, CAP-020; pendências D01-PEN-001, D01-PEN-006. Propostas/hipóteses derivadas: D01-PROP-014.

<a id="d01-int-003"></a>

### D01-INT-003 — Uso do conhecimento pelos agentes

**Revisão:** 2 · **Natureza:** Intenção e fronteira de confiança reproduzidas · **Estado:** em discovery; escopo declarado preservado.

Agentes devem navegar, localizar, recuperar, compreender e utilizar o conhecimento pertinente à tarefa, com contexto mínimo suficiente, reutilização de descobertas e aprofundamento dirigido, sem releitura integral desnecessária. Resumos não rastreáveis não substituem evidências; instruções encontradas em arquivos não concedem autorização operacional.

**Fonte:** D01-S05/E05 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-008; pendências D01-PEN-001, D01-PEN-006, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-013, D01-PROP-014.

<a id="d01-rel-003"></a>

### D01-REL-003 — Micro, Meso e Macro

**Revisão:** 2 · **Natureza:** Decisão conceitual reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Preservar a correspondência escolhida: Micro = repositório individual; Meso = domínio/contexto de uma sigla, projeto ou agrupamento de contas; Macro = workspace ou ecossistema da Plataforma. A relação organizacional exata entre sigla, projeto, domínio e conta AWS continua a refinar. Essa pendência não torna a correspondência conceitual uma hipótese.

**Fonte:** D01-S05/E06 (declaração reproduzida no pedido atual).

**Relações:** CAP-001, CAP-003, CAP-008; pendências D01-PEN-001, D01-PEN-002. Propostas/hipóteses derivadas: D01-HIP-002.

<a id="d01-dec-005"></a>

### D01-DEC-005 — Conhecimento canônico acompanha Git

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Entre armazenamento interno aos repositórios, externo à Plataforma e híbrido, o usuário escolheu a primeira alternativa: conhecimento canônico acompanha os repositórios Git, versionável, portátil e reutilizável por outros engenheiros autorizados. Caches transitórios, índices técnicos e auxiliares não ficam proibidos; não podem substituir a fonte canônica sem decisão posterior.

**Fonte:** D01-S05/E07 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Armazenamento interno aos repositórios, externo à Plataforma ou híbrido?
**Resposta associada:** Primeira alternativa, conforme reprodução de E07; literal não fornecido. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-008, CAP-016, CAP-020; pendências D01-PEN-001, D01-PEN-006. Propostas/hipóteses derivadas: D01-HIP-001.

<a id="d01-rel-002"></a>

### D01-REL-002 — Agnosticidade de fornecedores

**Revisão:** 2 · **Natureza:** Intenção/restrição reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Conhecimento tão independente quanto possível de fornecedores/executores. Alvos corporativos declarados: Devin, Claude e GitHub Copilot. Considerar convenções de instruções, skills, hooks e configurações, com adaptações específicas apenas quando necessárias; modelo canônico não depende de ferramenta específica. Formatos/contratos de adaptadores permanecem por especificar; alvos não comprovam disponibilidade, equivalência ou integração.

**Fonte:** D01-S05/E08 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-019, CAP-020; pendências D01-PEN-001, D01-PEN-006. Propostas/hipóteses derivadas: D01-HIP-001.

<a id="d01-rel-004"></a>

### D01-REL-004 — Repositório Meso e submódulos Micro

**Revisão:** 2 · **Natureza:** Decisão de topologia reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Cada sigla/conta possui seu próprio repositório Git versionado; repositórios de aplicações, bibliotecas e infraestrutura do agrupamento são Git Submodules desse repositório Meso. Escolha expressa de topologia desejada; clonagem, atualização, permissões e publicação ainda não especificadas. Não reduzir a escolha a mera menção de Submodules.

**Fonte:** D01-S05/E09 (declaração reproduzida no pedido atual).

**Relações:** CAP-001, CAP-008, CAP-012; pendências D01-PEN-001, D01-PEN-002, D01-PEN-003. Propostas/hipóteses derivadas: D01-HIP-002.

<a id="d01-dec-006"></a>

### D01-DEC-006 — Repositório Macro e submódulos Meso

**Revisão:** 2 · **Natureza:** Decisão de topologia reproduzida · **Estado:** em discovery; escopo declarado preservado.

O workspace também possui repositório Git e incorpora repositórios de sigla como submódulos: Workspace Git → siglas Git como Submodules → repositórios individuais como Submodules das siglas. O 'Sim' responde somente à pergunta se o Workspace deveria ter essa organização. Ponteiros não se sincronizam automaticamente; acesso ao pai não implica acesso ao conteúdo do submódulo.

**Fonte:** D01-S05/E10 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** O Workspace também deverá ter repositório Git incorporando os repositórios de sigla como submódulos?
**Resposta associada:** Sim. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-001, CAP-008, CAP-012; pendências D01-PEN-001, D01-PEN-002, D01-PEN-003. Propostas/hipóteses derivadas: D01-HIP-002.

<a id="d01-nec-001"></a>

### D01-NEC-001 — Conhecimento compartilhado e autonomia

**Revisão:** 2 · **Natureza:** Necessidade declarada · **Estado:** em discovery; escopo declarado preservado.

Dezenas de engenheiros de uma mesma sigla podem produzir conhecimento e mudanças simultaneamente. Compartilhar entre autorizados, evitando cópias divergentes e perda de descobertas, preservando autonomia e segurança do trabalho individual. Workspaces de uso individuais, compartilhados ou ambos permanecem em refinamento; isso não reabre a existência dos repositórios canônicos.

**Fonte:** D01-S05/E11 (declaração reproduzida no pedido atual).

**Relações:** CAP-001, CAP-008, CAP-010, CAP-013; pendências D01-PEN-001, D01-PEN-003. Propostas/hipóteses derivadas: D01-PROP-015.

<a id="d01-rel-005"></a>

### D01-REL-005 — Consolidação predominantemente automática

**Revisão:** 2 · **Natureza:** Decisão de intenção reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Preferir incorporação majoritariamente automática de descobertas, com intervenção humana quando necessária. Resolver conflitos ao máximo usando fatos e evidências e pedir revisão/aprovação do que não conseguir resolver com segurança. Confiança verbal de LLM não é prova suficiente. Gatilhos, protocolo e alcance de publicação automática continuam em refinamento; a escolha não é autorização irrestrita para merge.

**Fonte:** D01-S05/E12 (declaração reproduzida no pedido atual).

**Contexto da escolha reproduzida:** E12 informa a escolha de incorporação majoritariamente automática, com intervenção humana quando necessária. O pedido não fornece a pergunta literal, alternativas completas ou resposta literal; não são reconstruídas. A escolha não se estende a detalhes posteriores.

**Relações:** CAP-008, CAP-013, CAP-015, CAP-016; pendências D01-PEN-001, D01-PEN-003. Propostas/hipóteses derivadas: D01-PROP-015, D01-PROP-016.

<a id="d01-rst-002"></a>

### D01-RST-002 — Barreiras contra conhecimento incorreto

**Revisão:** 2 · **Natureza:** Exigência de confiabilidade reproduzida · **Estado:** em discovery; escopo declarado preservado.

Aplicar controles rigorosos contra alucinações, inferências não comprovadas, contradições, incoerências, conflitos de versões, perda silenciosa de conhecimento e consolidação de informação incorreta. Critérios, classificadores, verificadores e limiares concretos permanecem por especificar; a exigência não comprova controle implementado ou infalível.

**Fonte:** D01-S05/E13 (declaração reproduzida no pedido atual).

**Relações:** CAP-008, CAP-015, CAP-016; pendências D01-PEN-001, D01-PEN-003, D01-PEN-005, D01-PEN-007. Propostas/hipóteses derivadas: D01-PROP-007, D01-PROP-016, D01-PROP-021.

<a id="d01-dec-007"></a>

### D01-DEC-007 — Trabalho separado da publicação canônica

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Consolidação automática somente após verificações e controles; pushes de trabalho separados da publicação oficial/canônica. 'Sim, concordo' responde a essa pergunta, estabelecendo separação de preparação, validação e publicação. Não concede permissão irrestrita para merge nem alteração de branches protegidas.

**Fonte:** D01-S05/E14 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Consolidação automática somente após verificações e controles, mantendo pushes de trabalho separados da publicação oficial?
**Resposta associada:** Sim, concordo. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-008, CAP-012, CAP-013, CAP-016; pendências D01-PEN-001, D01-PEN-003. Propostas/hipóteses derivadas: D01-PROP-016, D01-PROP-017.

<a id="d01-ctx-001"></a>

### D01-CTX-001 — Autonomia atual para GitHub Actions

**Revisão:** 2 · **Natureza:** Restrição de ambiente relatada · **Estado:** em discovery; escopo declarado preservado.

Usuário relata não ter atualmente autonomia para criar novas pipelines no GitHub Actions corporativo. Não é política institucional universal nem proibição permanente. Motor próprio de validação da IDE é recomendação arquitetural, não implementação aprovada; verificações locais não garantem bloqueio de pushes fora da Plataforma.

**Fonte:** D01-S05/E15 (declaração reproduzida no pedido atual).

**Relações:** CAP-012, CAP-015, CAP-019; pendências D01-PEN-001, D01-PEN-003, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-017.

<a id="d01-ctx-002"></a>

### D01-CTX-002 — CI/CD, scheduled, GMUD e hotfix

**Revisão:** 2 · **Natureza:** Fluxo corporativo relatado · **Estado:** em discovery; escopo declarado preservado.

Relato variável por repositório: commit em feature branch → Action → PR para develop após sucesso → aprovação e duas Actions relacionadas à promoção para release → PR para main após resultados necessários → Action da main → parada em scheduled → preparação/aprovação de GMUD no ServiceNow/IUClick → continuação da Action na janela autorizada. Há hotfix produtivo associado a bug/incidente ServiceNow com caminho próprio de pipeline para main. Relato contextual, sem validação institucional, configuração universal ou autorização produtiva.

**Fonte:** D01-S05/E16 (declaração reproduzida no pedido atual).

**Relações:** CAP-012, CAP-017, CAP-018, CAP-019; pendências D01-PEN-001, D01-PEN-008. Detalhamento técnico não escolhido por este registro.

<a id="d01-dec-008"></a>

### D01-DEC-008 — Código e implantação por ambiente

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Distinguir conhecimento do código em branches e conhecimento das versões efetivamente implantadas em DEV, HOM e PROD. Main não comprova implantação em PROD. Concordância responde à distinção, sem escolher modelo técnico de verificação de deployments.

**Fonte:** D01-S05/E17 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Distinguir conhecimento de código em branches e das versões efetivamente implantadas em DEV/HOM/PROD?
**Resposta associada:** Concordância reproduzida; literal não fornecido em E17. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-002, CAP-006, CAP-008, CAP-012; pendências D01-PEN-001, D01-PEN-006, D01-PEN-007, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-018.

<a id="d01-int-004"></a>

### D01-INT-004 — Contextos multirrepositório heterogêneos

**Revisão:** 2 · **Natureza:** Intenção de comportamento reproduzida · **Estado:** em discovery; escopo declarado preservado.

Suportar funcionalidade desenvolvida em feature branches de vários repositórios enquanto componentes consideram comportamentos de versões produtivas ou de homologação de outros sistemas. Não presumir mesma branch, versão ou ambiente em todos os repositórios de uma tarefa. Modelo detalhado de contexto composto permanece candidato.

**Fonte:** D01-S05/E18 (declaração reproduzida no pedido atual).

**Relações:** CAP-001, CAP-002, CAP-006, CAP-008; pendências D01-PEN-001, D01-PEN-006, D01-PEN-007. Propostas/hipóteses derivadas: D01-PROP-018.

<a id="d01-dec-009"></a>

### D01-DEC-009 — Reprodução controlada e integração real

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Contemplar ambas alternativas: reprodução controlada de contratos/comportamentos por simulações ou mocks e integrações reais quando houver acesso e autorização apropriados. Escolha de produto não concede acesso interno, HOM/PROD ou serviços de outras equipes.

**Fonte:** D01-S05/E19 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Reprodução controlada/simulações ou integrações reais autorizadas?
**Resposta associada:** Ambas, conforme reprodução de E19; literal não fornecido. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-006, CAP-019, CAP-020; pendências D01-PEN-001, D01-PEN-007, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-018.

<a id="d01-int-005"></a>

### D01-INT-005 — Sistemas externos sem acesso à implementação

**Revisão:** 2 · **Natureza:** Intenção com contexto relatado · **Estado:** em discovery; escopo declarado preservado.

Em organização com numerosas equipes, repositórios e fronteiras de acesso, compreender interfaces e dependências de sistemas mesmo sem acesso a código/implementação, na medida das fontes autorizadas. Exemplos: Camunda, IBM ODM, APIs de outras equipes, plataformas/serviços corporativos restritos. Só documentação não comprova compreensão da implementação interna; nenhum sistema foi acessado nesta missão.

**Fonte:** D01-S05/E20 (declaração reproduzida no pedido atual).

**Relações:** CAP-002, CAP-006, CAP-019; pendências D01-PEN-001, D01-PEN-006, D01-PEN-007, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-019.

<a id="d01-int-006"></a>

### D01-INT-006 — Fontes documentais indiretas

**Revisão:** 2 · **Natureza:** Intenção de fontes indiretas reproduzida · **Estado:** em discovery; escopo declarado preservado.

Considerar GitHub Pages, SharePoint, contratos, testes, documentação técnica e outras fontes autorizadas; nem todo sistema precisa ser importado como submódulo Git. Catálogo federado é proposta técnica, não formato ou armazenamento aprovado. Identificar uma fonte não autoriza consultá-la.

**Fonte:** D01-S05/E21 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-006, CAP-019; pendências D01-PEN-001, D01-PEN-006, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-019.

<a id="d01-dec-010"></a>

### D01-DEC-010 — Referência externa e derivado legítimo

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Preservar a referência externa e consolidar no Git da sigla somente conhecimento derivado legitimamente armazenável e compartilhável. 'Sim' responde a essa alternativa. Preservar origem, versão, escopo, autorização, limites e atualidade. Acesso técnico/leitura não equivale a autorização para copiar ou redistribuir.

**Fonte:** D01-S05/E22 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Preservar referência externa e consolidar no Git da sigla só derivado legitimamente armazenável e compartilhável?
**Resposta associada:** Sim. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-003, CAP-008, CAP-013, CAP-016; pendências D01-PEN-001, D01-PEN-004, D01-PEN-006, D01-PEN-008. Propostas/hipóteses derivadas: D01-PROP-019.

<a id="d01-dec-011"></a>

### D01-DEC-011 — Buscas exteriores com autorização prévia

**Revisão:** 2 · **Natureza:** Decisão restritiva expressa reproduzida · **Estado:** em discovery; escopo declarado preservado.

Informar buscas exteriores ao engenheiro e executá-las somente com autorização apropriada. Pode identificar necessidade de consulta, mas deve apresentar finalidade, fonte pretendida e escopo antes de executá-la. Não confundir com consulta posterior ao legado (DEC-001) nem autorização de escrita/redistribuição. Esta decisão da futura Plataforma não exige novo aceite para as fontes já autorizadas nesta missão.

**Fonte:** D01-S05/E23 (declaração reproduzida no pedido atual).

**Relações:** CAP-006, CAP-013, CAP-019; pendências D01-PEN-001, D01-PEN-004, D01-PEN-008, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-019.

<a id="d01-dec-012"></a>

### D01-DEC-012 — Autorização pontual e reutilizável

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Suportar ambas modalidades: autorização pontual e autorização reutilizável. 'Permito ambas as modalidades' responde a essas alternativas. Reutilizável não significa permanente, irrestrita ou válida fora do escopo; validade, revogação, identidade e aplicação concreta continuam a especificar.

**Fonte:** D01-S05/E24 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Autorizações pontuais e autorizações reutilizáveis?
**Resposta associada:** Permito ambas as modalidades. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-013, CAP-019; pendências D01-PEN-001, D01-PEN-004, D01-PEN-008. Detalhamento técnico não escolhido por este registro.

<a id="d01-dec-013"></a>

### D01-DEC-013 — Autorização individual e coletiva

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Suportar permissões individuais e coletivas para equipes ou siglas. 'Suportar ambas' responde somente a essas alternativas. Coletivas respeitam autoridade do concedente e permissões corporativas efetivas; um registro da Plataforma não cria direito de acesso inexistente.

**Fonte:** D01-S05/E25 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Permissões individuais e coletivas para equipes/siglas?
**Resposta associada:** Suportar ambas. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-013, CAP-019; pendências D01-PEN-001, D01-PEN-004, D01-PEN-008. Detalhamento técnico não escolhido por este registro.

<a id="d01-rel-006"></a>

### D01-REL-006 — Absorção e migração cuidadosa do legado

**Revisão:** 2 · **Natureza:** Intenção determinada reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Inventariar, compreender, reconciliar e adaptar documentação, skills, instruções, configurações e outros artefatos preexistentes à estrutura Agent-First. Intenção de substituir estruturas originais redundantes, informando o que foi identificado, preservado, transformado, descartado ou permaneceu inconclusivo. Buscar compreensão máxima e admitir limites; descarte identificado no relatório não autoriza apagar o original, que segue REL-008.

**Fonte:** D01-S05/E26 (declaração reproduzida no pedido atual).

**Relações:** CAP-002, CAP-003, CAP-008; pendências D01-PEN-001, D01-PEN-006, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-020, D01-HIP-003.

<a id="d01-rel-008"></a>

### D01-REL-008 — Exclusão dos originais sempre aprovada

**Revisão:** 2 · **Natureza:** Decisão restritiva reproduzida; classe retificada · **Estado:** em discovery; escopo declarado preservado.

Exclusão de artefatos originais preexistentes sempre exige aprovação explícita do engenheiro responsável. 'Sempre exija' responde à escolha entre aprovação sempre e exclusão automática após migração bem-sucedida. Identificar objeto e revisão; mudança material posterior exige nova avaliação. Aprovar migração, padrão Agent-First ou leitura não aprova exclusão. Nenhuma exclusão executada nesta missão.

**Fonte:** D01-S05/E27 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Excluir originais sempre com aprovação humana ou automaticamente após migração bem-sucedida?
**Resposta associada:** Sempre exija. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-008, CAP-013; pendências D01-PEN-001, D01-PEN-004. Propostas/hipóteses derivadas: D01-PROP-020.

<a id="d01-rel-007"></a>

### D01-REL-007 — Uso provisório preservando originais

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida; desdobramento · **Estado:** em discovery; escopo declarado preservado.

Permitir avaliar e utilizar a nova estrutura Agent-First antes da conclusão da migração e exclusão dos originais, mantendo os originais preservados. 'permitir o uso provisório' responde a essa pergunta. Uso provisório não declara conhecimento definitivamente verificado. O antigo composto sobre código foi desdobrado em DEC-014 sem apagar a revisão anterior.

**Fonte:** D01-S05/E28 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Permitir uso provisório antes da conclusão/exclusão dos originais?
**Resposta associada:** permitir o uso provisório Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-003, CAP-008, CAP-013; pendências D01-PEN-001, D01-PEN-004, D01-PEN-005. Propostas/hipóteses derivadas: D01-PROP-005, D01-PROP-020.

<a id="d01-dec-014"></a>

### D01-DEC-014 — Consultas e código autorizado na fase provisória

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

Permitir ambas funcionalidades na estrutura provisória: consultas/explicações e alterações reais de código em escopo autorizado. 'PErmitir ambas' responde às alternativas imediatamente apresentadas. Uso provisório não dá permissão genérica para modificar código nem elimina controles próprios da operação.

**Fonte:** D01-S05/E29 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Uso provisório só para consultas/explicações ou também alterações reais de código em escopo autorizado?
**Resposta associada:** PErmitir ambas Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-012, CAP-013; pendências D01-PEN-001, D01-PEN-004. Detalhamento técnico não escolhido por este registro.

<a id="d01-dec-015"></a>

### D01-DEC-015 — Provisória como referência operacional padrão

**Revisão:** 2 · **Natureza:** Decisão explícita reproduzida · **Estado:** em discovery; escopo declarado preservado.

A estrutura Agent-First provisória é a referência operacional preferencial/padrão. 'Provisória, sempre devemos prezar pelo nosso padrão estrutural' responde à escolha entre original e provisória. Legados preservados não funcionam silenciosamente como instruções concorrentes. Diante de lacuna, seguir DEC-001; padrão não implica exclusão dos originais.

**Fonte:** D01-S05/E30 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Escolher entre estrutura original e provisória ou usar provisória como referência padrão?
**Resposta associada:** Provisória, sempre devemos prezar pelo nosso padrão estrutural. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-003, CAP-008, CAP-013; pendências D01-PEN-001, D01-PEN-004, D01-PEN-006, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-002, D01-PROP-014.

<a id="d01-dec-001"></a>

### D01-DEC-001 — Consulta posterior ao legado

**Revisão:** 2 · **Natureza:** Decisão explícita diretamente recuperada e reproduzida · **Estado:** em discovery; escopo declarado preservado.

Ao recuperar informação ainda apenas no material legado diante de lacuna do conhecimento migrado, pedir permissão ao engenheiro e comunicar a inconformidade persistente. Inventário/leitura inicial autorizados no onboarding são distintos da consulta posterior para suprir lacuna; a segunda exige a permissão declarada. Não proíbe inventário inicial autorizado nem autoriza escrita, execução ou exclusão. Fonte direta anterior D01-S02-A; D01-S05/E31 acrescenta a distinção contextual.

**Fonte:** D01-S05/E31 (declaração reproduzida no pedido atual).

**Relações:** CAP-008, CAP-013, CAP-016; pendências D01-PEN-001, D01-PEN-004, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-001, D01-PROP-002, D01-PROP-003.

<a id="d01-dec-002"></a>

### D01-DEC-002 — Conclusão com pendências não críticas

**Revisão:** 2 · **Natureza:** Decisão explícita diretamente recuperada e reproduzida · **Estado:** em discovery; escopo declarado preservado.

Permitir conclusão do onboarding com inconformidades não críticas explicitamente catalogadas e controladas, em vez de exigir resolver todas antes da conclusão. 'Permitir' responde à pergunta anterior dessa alternativa. Não ocultar pendências, eliminar evidências ou considerar falha crítica resolvida. Nomes dos estados e máquina de transições posteriores são propostas. Fonte direta D01-S02-B, pergunta em A; D01-S05/E32.

**Fonte:** D01-S05/E32 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Concluir com pendências não críticas catalogadas ou exigir resolver todas antes?
**Resposta associada:** Permitir. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-008, CAP-013, CAP-015; pendências D01-PEN-001, D01-PEN-005, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-003, D01-PROP-005, D01-PROP-009.

<a id="d01-dec-003"></a>

### D01-DEC-003 — Classificação automática fundamentada

**Revisão:** 2 · **Natureza:** Decisão explícita diretamente recuperada e reproduzida · **Estado:** em discovery; escopo declarado preservado.

Classificar autonomamente inconformidades por critérios rigorosos, objetivos e verificáveis, recorrendo ao engenheiro quando não determinar a criticidade com segurança. 'Sim' responde à pergunta sobre essa classificação e escalonamento; taxonomia, limiares e critérios técnicos detalhados apresentados posteriormente continuam candidatos. Fonte direta D01-S02-C, pergunta em B; D01-S05/E33.

**Fonte:** D01-S05/E33 (declaração reproduzida no pedido atual).

**Pergunta antecedente reproduzida:** Classificar autonomamente com critérios rigorosos, objetivos e verificáveis, recorrendo ao engenheiro se incerto?
**Resposta associada:** Sim. Não se estende a detalhamentos apresentados depois.

**Relações:** CAP-002, CAP-008, CAP-013, CAP-015; pendências D01-PEN-001, D01-PEN-005, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-006, D01-PROP-007, D01-PROP-008.

<a id="d01-dec-016"></a>

### D01-DEC-016 — Pendências estruturadas e contínuas

**Revisão:** 2 · **Natureza:** Determinação de produto reproduzida · **Estado:** em discovery; escopo declarado preservado.

Catalogar dúvidas, conflitos, impedimentos e lacunas da importação de forma estruturada, hierarquizada, instrutiva, detalhada, rastreável e disponível a agentes e engenheiros envolvidos. A cada leitura ou ciclo de execução, agentes identificam rapidamente pendências relevantes e comunicam seu estado ao engenheiro. Não exige carregar integralmente todos registros no contexto de todo ciclo; índices e roteamento permanecem por especificar.

**Fonte:** D01-S05/E34 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-005, CAP-008, CAP-013, CAP-016; pendências D01-PEN-001, D01-PEN-005, D01-PEN-006, D01-PEN-007, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-009, D01-PROP-014.

<a id="d01-dec-017"></a>

### D01-DEC-017 — Esclarecimentos e retroalimentação contínua

**Revisão:** 2 · **Natureza:** Determinação de produto reproduzida · **Estado:** em discovery; escopo declarado preservado.

Engenheiro pode fornecer informações, esclarecimentos, diretrizes e decisões depois do onboarding. Conteúdo pertinente retroalimenta Micro, Meso e Macro com verificações, proveniência, autorização, consistência e publicação canônica. Atualização contínua não autoriza execução assíncrona inexistente, publicação sem controles ou sobrescrita silenciosa. Mecanismos duráveis e gatilhos concretos permanecem por especificar.

**Fonte:** D01-S05/E35 (declaração reproduzida no pedido atual).

**Relações:** CAP-003, CAP-008, CAP-013, CAP-016; pendências D01-PEN-001, D01-PEN-003, D01-PEN-006, D01-PEN-007, D01-PEN-010. Propostas/hipóteses derivadas: D01-PROP-015, D01-PROP-016.

<a id="d01-dec-004"></a>

### D01-DEC-004 — Encerramento e continuidade

**Revisão:** 2 · **Natureza:** Decisão de continuidade diretamente recuperada e reproduzida · **Estado:** em discovery; escopo declarado preservado.

Encerrar e consolidar o Discovery 01 antes de aprofundar Motor de Compreensão Profunda de Repositórios em outra sessão, preservando contexto, decisões e detalhes. Usuário autorizou consolidação e elaboração/revisão rigorosa do Prompt-Master corretivo. Preparar retomada sem executar Discovery 02 ou aprovar sua arquitetura. Fontes anteriores D01-S02-D/E e D01-S01; pedido atual D01-S05/E36. Não cria nova conversa automaticamente.

**Fonte:** D01-S05/E36 (declaração reproduzida no pedido atual).

**Relações:** CAP-008, CAP-016; pendências D01-PEN-001, D01-PEN-007, D01-PEN-009. Propostas/hipóteses derivadas: D01-PROP-011.

<a id="d01-rel-009"></a>

### D01-REL-009 — Agrupador histórico desdobrado

**Revisão:** 2 · **Estado:** HISTÓRICO / DESDOBRADO; sem definição canônica independente ativa.

Na revisão 1, reunia segurança, autorizações, concorrência, inconsistências e consolidação por relato do assistente D01-S02-D. A nova evidência D01-S05 permite unidades próprias: REL-005 (consolidação), RST-002 (confiabilidade), DEC-007 (publicação), DEC-010..013 (fontes/permissões), DEC-016 (pendências) e DEC-017 (retroalimentação). Este agrupador mantém a identidade/história e aponta aos registros canônicos; não duplica suas definições. Controles técnicos específicos continuam propostas ou pendências.

## Propostas novas inventariadas, sem promoção a decisões

Os grupos P-A..P-L são inventário do pedido D01-S05, não prova de recuperação da formulação original do assistente. Registros novos abaixo têm revisão 1 e maturidade PROPOSTA EM DISCOVERY; não atribuem ao usuário o desenho técnico. Propostas antigas continuam com suas identidades e fontes logo adiante.

<a id="d01-prop-012"></a>

### D01-PROP-012 — Sequência operacional candidata

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-A.

Importação → inventário → descoberta/análise → estruturação → organização hierárquica → roteamento → aplicação do conhecimento → atualização incremental. A intenção geral é coberta por INT-001/002/003 e REL-001; sequência, etapas e gates concretos permanecem propostas.

<a id="d01-prop-013"></a>

### D01-PROP-013 — Modelo de evidências e conhecimento

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-B.

Distinguir fatos observados, comportamentos verificados, relatos, hipóteses, interpretações, dependências, incertezas e evidências. Estrutura de representação, campos e transições continuam candidatos; não equiparar hipótese a fato observado.

<a id="d01-prop-014"></a>

### D01-PROP-014 — Arquivos e navegação Agent-First

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-C.

AGENTS.md como entrada/roteador, documentação especializada, índices, manifestos, esquemas, skills e configurações específicas. INT-002/003 e DEC-016 sustentam intenção de organização/recuperação; árvore, schemas, precedência e estratégia de índices não aprovados.

<a id="d01-prop-015"></a>

### D01-PROP-015 — Contribuições locais e compartilhadas

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-E.

Separar descobertas locais, contribuições candidatas e conhecimento compartilhado; deduplicar, reconciliar conflitos e integrar por revisão. NEC-001, REL-005 e DEC-017 sustentam necessidade/intenção; algoritmo, granularidade e modalidade de workspace continuam candidatos.

<a id="d01-prop-016"></a>

### D01-PROP-016 — Guardrails de consolidação

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-F.

Proveniência, validação independente, atualidade, controle de acesso, revisão-base, integridade, idempotência, segurança e recuperação. RST-002 e DEC-007 exigem confiabilidade e separação de publicação; conjunto concreto de verificadores, protocolos e limiares não foi aprovado.

<a id="d01-prop-017"></a>

### D01-PROP-017 — Validação sem novas Actions corporativas

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-G.

Motor de validação próprio da Plataforma, com possível integração futura a controles remotos corporativos. Responde ao relato CTX-001; não foi aprovado em detalhe e não impede por si pushes fora da IDE nem equivale a barreira no servidor.

<a id="d01-prop-018"></a>

### D01-PROP-018 — Composição de ambientes e referências

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-H.

Referências distintas para código em desenvolvimento, versões implantadas, comportamentos de referência, contratos e simulações. DEC-008/009 e INT-004 escolhem distinção/suporte; modelo composto, evidência de deployment e mecanismos de reprodução continuam candidatos.

<a id="d01-prop-019"></a>

### D01-PROP-019 — Catálogo de conhecimento externo

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-I.

Catálogo de sistemas, referências documentais, conhecimento derivado, classificação de acesso e verificação de atualidade. INT-005/006 e DEC-010..013 sustentam comportamento; catálogo federado, armazenamento, revogação e contratos de acesso continuam propostas.

<a id="d01-prop-020"></a>

### D01-PROP-020 — Migração verificável e relatório

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-J.

Inventário origem→destino, classificação de artefatos, comparação semântica, preservação de conhecimento, análise de skills/hooks, relatórios e exclusão autorizada. REL-006/007/008 e DEC-014/015/001 delimitam escolhas; mecanismos de migração e schema do relatório continuam candidatos. HIP-003 preserva hipótese de eficácia desse mapa.

<a id="d01-prop-021"></a>

### D01-PROP-021 — Critérios de compreensão e qualidade

**Revisão:** 1 · **Natureza:** proposta/recomendação reproduzida · **Fonte:** D01-S05/P-L.

Cobertura conhecida, evidências, explicações fundamentadas, impacto de alterações, testes sintéticos, verificação independente e limites de confiança. REL-001/RST-002 demandam profundidade e confiabilidade; métricas, limiares e métodos específicos são candidatos do Discovery 02.

## Disposição dos doze grupos de propostas

| Grupo | Registros canônicos de propostas/hipóteses | Intenção aceita versus detalhe ainda proposto |
|---|---|---|
| P-A | D01-PROP-012 | INT-001 e REL-001 aceitam objetivo/profundidade; sequência não aprovada |
| P-B | D01-PROP-013 | Evidências e confiabilidade exigidas; schema não escolhido |
| P-C | D01-PROP-014 | Padrão/recuperação desejados; árvore, schema e índice continuam candidatos |
| P-D | D01-HIP-001 | REL-002 exige agnosticidade; projeções/adaptadores concretos são hipótese arquitetural |
| P-E | D01-PROP-015 | REL-005/NEC-001/DEC-017 preservam intenção; algoritmo e protocolo não aprovados |
| P-F | D01-PROP-016, D01-PROP-007/008 | Controles rigorosos aceitos; verificadores/limiares e UX candidatos |
| P-G | D01-PROP-017 | CTX-001 é restrição relatada; motor próprio é recomendação |
| P-H | D01-PROP-018 | DEC-008/009 e INT-004 são escolhas; formato composto é candidato |
| P-I | D01-PROP-019 | Fontes indiretas/permissões escolhidas; catálogo federado é proposta |
| P-J | D01-PROP-020, D01-HIP-003 | Migração e aprovação de exclusão delimitadas; mapa/relatório são propostas |
| P-K | D01-PROP-005/006/010 | Ressalvas e classificação automática aceitas; taxonomia, transições e telas não |
| P-L | D01-PROP-021, D01-PROP-011 | Profundidade/confiabilidade são intenções; métricas e método D02 não aprovados |

Não existe definição canônica paralela para cada grupo: esta tabela é índice de encaminhamento. Estados provisório/concluído/com ressalvas/bloqueado, crítica/não crítica/indeterminada e revisão necessária são rótulos candidatos, sem máquina de estados aprovada.

## Propostas e hipóteses da revisão 1 preservadas

As tabelas a seguir conservam conteúdo, IDs e fontes da revisão 1. Todas permanecem propostas/hipóteses; decisões agora individualizadas limitam a intenção e não aprovam automaticamente esses detalhes.

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

## Hipóteses preservadas da revisão 1

| ID | Hipótese nova, sem atribuição ao usuário | Evidência futura necessária |
|---|---|---|
| D01-HIP-001 | Um núcleo de conhecimento independente de executor, com projeções por ferramenta, preserva semântica entre agentes. | Comparar interpretações e perda de informação em fixtures sintéticas; validar precedência, sem escolher stack |
| D01-HIP-002 | Fixar revisões dos níveis de conhecimento e registrar proveniência permitirá detectar obsolescência e conflitos sem propagar conteúdo indevido. | Cenários de revisão divergente, revogação de acesso e atualização concorrente; avaliar custo e granularidade |
| D01-HIP-003 | Um inventário origem→destino com verificações por item permite detectar lacunas de migração e sustentar a criticidade. | Migração sintética com perda, contradição, duplicação e referência quebrada injetadas; medir falsos positivos/negativos |

Todas as pendências têm ID e encaminhamento em [REVISAO.md](REVISAO.md). Nenhum dos desenhos deste conjunto escolhe banco de dados, busca vetorial, parser, framework, executor definitivo ou arquitetura distribuída.
