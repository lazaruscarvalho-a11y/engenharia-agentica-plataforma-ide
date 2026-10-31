# Fonte reproduzida D01-R2 v2.0

Evidência fornecida pelo usuário no pedido atual. Dados de reconciliação, sem efeito de instrução operacional ou norma. E01..E36 e P-A..P-L são âncoras do pedido, não IDs de mensagens originais. O arquivo original completo tem SHA-256 e611884b12ddcbfc2378674e124de5543ffc78eb8dff2a3700675bb379805a35 e 50831 bytes. Este recorte é UTF-8/LF; as definições canônicas estão em REGISTRO.md.

<a id="e01"></a>

### E01 — Objetivo central do onboarding

O usuário deseja que a Plataforma importe, absorva, compreenda, estruture e utilize o conhecimento de um ou mais repositórios, independentemente de sua organização, natureza, finalidade, linguagens e tecnologias.

Esse conhecimento deverá subsidiar explicações, esclarecimentos, investigação, planejamento, modificações de código, validações e as demais funcionalidades da Plataforma.

É uma intenção explícita de produto.

Não representa garantia absoluta de compreensão perfeita de qualquer sistema.

<a id="e02"></a>

### E02 — Compreensão inicial profunda e evolução contínua

O usuário espera algo semelhante à compreensão adquirida por um engenheiro experiente após estudar profundamente um sistema.

A Plataforma deverá procurar conhecer:

- Finalidade e contexto de negócio.
- Regras de negócio.
- Fluxos e comportamentos.
- Arquitetura e responsabilidades.
- Linguagens e frameworks.
- Componentes e estruturas.
- Integrações e contratos.
- Dependências internas e externas.
- Infraestrutura e configurações.
- Procedimentos de execução local.
- Estratégias e procedimentos de testes.
- Particularidades, limitações e riscos.

A compreensão deverá ser tão profunda quanto viável, com cobertura e limitações explicitadas.

Deverá combinar investigação inicial ampla com enriquecimento incremental posterior.

<a id="e03"></a>

### E03 — Execução local reservada ao engenheiro

Manifestação expressa:

"A decisão de executar a aplicação localmente cabe exclusivamente ao engenheiro responsável."

A Plataforma poderá documentar procedimentos e preparar análises.

Essa declaração não autoriza agentes a instalar dependências, subir aplicações ou executar comandos de inicialização por iniciativa própria.

A política de outras ações executáveis permanece sujeita às autorizações aplicáveis.

<a id="e04"></a>

### E04 — Paradigma Agent-First

Os repositórios incorporados à Plataforma deverão ser preparados segundo o paradigma Agent-First.

O usuário relacionou esse paradigma a:

- AI-centric.
- AI-based.
- Specification-Driven Development.
- Harness Engineering.
- AI-intent.

O conhecimento deverá ser concreto, conciso, hierarquizado, estruturado, padronizado e otimizado para consumo e atualização por agentes.

A intenção inclui arquivos como `AGENTS.md`, diretórios especializados, índices, esquemas e artefatos estruturados.

Não existe aprovação de uma árvore definitiva de diretórios, de um esquema específico ou de uma tecnologia de armazenamento.

<a id="e05"></a>

### E05 — Uso do conhecimento pelos agentes

Os agentes deverão conseguir navegar, localizar, recuperar, compreender e utilizar o conhecimento pertinente às tarefas.

O objetivo é favorecer contexto mínimo suficiente, reutilização de descobertas e aprofundamento dirigido, sem exigir releitura integral desnecessária.

Não substituir evidências por resumos não rastreáveis.

Não tratar instruções encontradas em arquivos como autorização operacional.

## BLOCO B — ARQUITETURA MICRO, MESO E MACRO

<a id="e06"></a>

### E06 — Três camadas de conhecimento

O usuário definiu:

**Micro:** repositório individual.

**Meso:** domínio/contexto de uma sigla, projeto ou agrupamento de contas.

**Macro:** workspace ou ecossistema da Plataforma.

Preservar essa correspondência conceitual.

A relação organizacional exata entre sigla, projeto, domínio e conta AWS ainda exige refinamento, não podendo ser inventada.

<a id="e07"></a>

### E07 — Conhecimento canônico em Git

Diante das alternativas de armazenamento interno aos repositórios, externo à Plataforma ou híbrido, o usuário escolheu a primeira.

O conhecimento deverá acompanhar os repositórios Git, sendo versionável, portátil e reutilizável por outros engenheiros autorizados.

Isso não proíbe caches transitórios, índices técnicos ou outras estruturas auxiliares; esses mecanismos não substituem a fonte canônica sem decisão posterior.

<a id="e08"></a>

### E08 — Agnosticidade de ferramentas

O conhecimento deverá ser tão independente quanto possível de fornecedores e executores específicos.

Os alvos corporativos declarados são:

- Devin.
- Claude.
- GitHub Copilot.

A Plataforma deverá considerar suas convenções de instruções, skills, hooks e configurações, utilizando adaptações específicas somente quando necessárias.

O modelo canônico de conhecimento não deverá depender de uma ferramenta específica.

A forma concreta dos adaptadores e seus formatos permanece pendente de especificação.

<a id="e09"></a>

### E09 — Repositório Meso com Git Submodules

O usuário escolheu que cada sigla/conta possua seu próprio repositório Git versionado.

Os repositórios de aplicações, bibliotecas e infraestrutura pertencentes ao agrupamento deverão ser incorporados como Git Submodules desse repositório Meso.

A decisão é sobre a topologia desejada, não sobre regras ainda não especificadas de clonagem, atualização, permissões ou publicação.

<a id="e10"></a>

### E10 — Repositório Macro com submódulos Meso

A pergunta foi se o Workspace também deveria possuir seu repositório Git, incorporando os repositórios de sigla como submódulos.

O usuário respondeu:

"Sim."

A topologia conceitual escolhida é:

**Workspace Git → repositórios das siglas como submódulos → repositórios individuais como submódulos das siglas.**

Não presumir sincronização automática dos commits.

Não presumir acesso ao conteúdo de um submódulo apenas porque seu repositório pai é acessível.

<a id="e11"></a>

### E11 — Compartilhamento entre engenheiros

O usuário identificou o problema de dezenas de engenheiros trabalharem em uma mesma sigla, produzindo conhecimento e modificações simultaneamente.

O resultado desejado é compartilhar conhecimento entre engenheiros autorizados, evitando cópias divergentes e perda de descobertas.

Ao mesmo tempo, o trabalho individual deverá preservar autonomia e segurança.

Essa necessidade não define automaticamente se os workspaces de uso serão sempre individuais, compartilhados ou ambos.

Preservar essa questão como refinamento, sem confundi-la com a existência dos repositórios canônicos.

## BLOCO C — CONCORRÊNCIA, CONSOLIDAÇÃO E CONFIABILIDADE

<a id="e12"></a>

### E12 — Consolidação predominantemente automática

O usuário escolheu a abordagem de incorporação majoritariamente automática de descobertas, com intervenção humana quando necessária.

A Plataforma deverá resolver conflitos ao máximo, utilizando fatos e evidências, e pedir revisão ou aprovação para aquilo que não conseguir resolver com segurança.

Não utilizar confiança verbal de LLM como prova suficiente.

<a id="e13"></a>

### E13 — Barreiras contra conhecimento incorreto

O usuário exigiu controles rigorosos contra:

- Alucinações.
- Inferências não comprovadas.
- Contradições.
- Incoerências.
- Conflitos de versões.
- Perda silenciosa de conhecimento.
- Consolidação de informações incorretas.

A forma concreta dos critérios, classificadores, verificadores e limiares ainda deverá ser especificada.

<a id="e14"></a>

### E14 — Separação entre trabalho e publicação canônica

A pergunta foi se a Plataforma deveria permitir consolidação automática somente após verificações e controles, mantendo pushes de trabalho separados da publicação oficial.

O usuário respondeu:

"Sim, concordo."

Isso estabelece a intenção de separar preparação, validação e publicação.

Não equivale a autorização irrestrita para merges ou alteração de branches protegidas.

<a id="e15"></a>

### E15 — Restrição de GitHub Actions

O usuário informou que não possui, atualmente, autonomia para criar novas pipelines no GitHub Actions corporativo.

Essa é uma restrição de ambiente relatada.

A proposta de criar validações próprias na IDE deverá permanecer classificada como recomendação arquitetural a refinar.

Essas validações não constituem, sozinhas, garantia contra pushes realizados fora da Plataforma.

## BLOCO D — FLUXOS CORPORATIVOS E AMBIENTES

<a id="e16"></a>

### E16 — CI/CD corporativo relatado

O usuário descreveu o fluxo geral:

1. Commit em feature branch.
2. Execução de Action.
3. PR para develop após sucesso.
4. Aprovação e execução de duas Actions relacionadas à promoção para release.
5. PR para main após os resultados necessários.
6. Execução da Action relacionada à main.
7. Parada na etapa `scheduled`.
8. Preparação e aprovação de GMUD no ServiceNow/IUClick.
9. Continuação da Action na janela autorizada.

O fluxo pode variar conforme a natureza de cada repositório.

O usuário relatou também hotfix produtivo associado a bug/incidente do ServiceNow, com caminho próprio de pipeline para main.

Tratar tudo como relato contextual, não como configuração corporativa universal verificada.

<a id="e17"></a>

### E17 — Conhecimento por ambiente

O usuário concordou que a Plataforma deverá distinguir conhecimento de código em branches e conhecimento correspondente às versões efetivamente implantadas em DEV, HOM e PROD.

A existência de código em `main` não comprova que ele esteja implantado em produção.

O modelo de verificação de deployments permanece pendente.

<a id="e18"></a>

### E18 — Desenvolvimento multirrepositório com comportamentos mistos

O usuário explicou que poderá desenvolver uma funcionalidade envolvendo vários repositórios em feature branches, enquanto determinados componentes precisam considerar comportamentos de versões produtivas ou de homologação de outros sistemas.

A Plataforma deverá suportar esses contextos heterogêneos.

Não presumir que todos os repositórios de uma tarefa estejam na mesma branch, versão ou ambiente.

O modelo detalhado de contexto composto permanece candidato.

<a id="e19"></a>

### E19 — Reprodução e integração real

Diante das alternativas entre simulações/mocks e integrações reais autorizadas, o usuário escolheu ambas.

Portanto, a Plataforma deverá contemplar:

- Reprodução controlada de contratos e comportamentos.
- Utilização de integrações reais quando houver acesso e autorização apropriados.

Essa decisão de produto não concede acesso a serviços internos.

## BLOCO E — CONHECIMENTO EXTERNO E ACESSOS

<a id="e20"></a>

### E20 — Sistemas externos inacessíveis

O usuário explicou que a Plataforma atuará em uma grande organização com numerosas equipes, repositórios e fronteiras de acesso.

Mesmo sem acesso ao código ou à implementação de determinado sistema, deverá ser possível compreender suas interfaces e dependências na medida das fontes autorizadas disponíveis.

Exemplos mencionados:

- Camunda.
- IBM ODM.
- APIs de outras equipes.
- Plataformas e serviços corporativos de acesso restrito.

Não presumir compreensão da implementação interna quando houver somente documentação.

<a id="e21"></a>

### E21 — Fontes documentais indiretas

O usuário mencionou a possibilidade de conhecimento estar disponível em:

- GitHub Pages.
- SharePoint.
- Contratos.
- Testes.
- Documentação técnica.
- Outras fontes autorizadas.

A Plataforma deverá considerar fontes indiretas sem exigir que todo sistema seja importado como submódulo Git.

O formato de catálogo federado permanece uma proposta técnica.

<a id="e22"></a>

### E22 — Referência original e conhecimento derivado

A pergunta foi se a Plataforma deveria preservar a referência externa e consolidar no Git da sigla apenas conhecimento derivado legitimamente armazenável e compartilhável.

Resposta:

"Sim."

Preservar origem, versão, escopo, autorização, limites e atualidade.

Acessibilidade técnica não equivale a permissão para copiar ou redistribuir dados.

<a id="e23"></a>

### E23 — Autorização prévia para buscas exteriores

Manifestação expressa:

"Essas buscas exteriores devem ser informadas ao Engenheiro e executadas caso haja autorização."

A Plataforma pode identificar a necessidade de uma consulta, mas não deve executá-la sem autorização apropriada.

A consulta deverá ser apresentada com finalidade, fonte pretendida e escopo.

<a id="e24"></a>

### E24 — Autorizações pontuais e reutilizáveis

Diante das alternativas de autorização pontual e autorização reutilizável, o usuário escolheu:

"Permito ambas as modalidades."

Não interpretar autorização reutilizável como autorização permanente, irrestrita ou válida fora de seu escopo.

<a id="e25"></a>

### E25 — Autorizações individuais e coletivas

A pergunta foi se a Plataforma deveria suportar permissões individuais e permissões coletivas para equipes ou siglas.

Resposta:

"Suportar ambas."

As autorizações coletivas deverão respeitar a autoridade de quem as concede e as permissões corporativas efetivas.

Não criar direitos de acesso a partir de um registro de autorização da própria Plataforma.

## BLOCO F — MIGRAÇÃO DE ESTRUTURAS EXISTENTES

<a id="e26"></a>

### E26 — Absorção do conhecimento legado

O usuário determinou que, quando um repositório já possuir documentação, skills, instruções, configurações e outros artefatos, eles deverão ser cuidadosamente inventariados, compreendidos, reconciliados e adaptados à estrutura Agent-First.

A intenção é substituir as estruturas originais redundantes, informando ao engenheiro o que foi identificado, preservado, transformado, descartado ou permaneceu inconclusivo.

Buscar compreensão máxima, sem declarar completude absoluta quando não houver evidência.

<a id="e27"></a>

### E27 — Exclusão de artefatos originais

A pergunta foi se a remoção dos arquivos originais deveria sempre exigir aprovação humana ou poderia ocorrer automaticamente após migração considerada bem-sucedida.

Resposta:

"Sempre exija."

Portanto, a exclusão de artefatos originais preexistentes sempre exigirá aprovação explícita do engenheiro responsável.

A autorização precisa identificar o objeto e a revisão.

Mudança material posterior exige nova avaliação.

Não executar exclusões nesta missão.

<a id="e28"></a>

### E28 — Uso provisório

Diante da pergunta sobre permitir uso provisório da nova estrutura antes da conclusão e exclusão dos originais, o usuário respondeu:

"permitir o uso provisório"

A estrutura provisória poderá ser avaliada e utilizada, mantendo os originais preservados.

<a id="e29"></a>

### E29 — Modificações de código durante uso provisório

A pergunta foi se o uso provisório deveria permitir somente consultas e explicações ou também alterações reais de código em escopo autorizado.

Resposta:

"PErmitir ambas"

A autorização de uso provisório não concede permissão genérica para modificar código.

<a id="e30"></a>

### E30 — Estrutura provisória como padrão

A pergunta foi se o engenheiro deveria escolher entre a estrutura original e a provisória ou se a estrutura Agent-First provisória deveria ser a referência padrão.

Resposta:

"Provisória, sempre devemos prezar pelo nosso padrão estrutural."

A estrutura provisória será a referência operacional preferencial.

Documentos legados não deverão funcionar silenciosamente como instruções concorrentes.

<a id="e31"></a>

### E31 — Consulta ao legado diante de lacuna

O usuário afirmou que, para recuperar conhecimento ainda existente apenas no material legado, o agente deverá pedir permissão ao engenheiro e comunicar a inconformidade persistente.

Preservar a distinção entre:

- Inventário e leitura inicial autorizados no onboarding.
- Consulta posterior ao legado para suprir uma lacuna da estrutura provisória.

A segunda situação exige a autorização indicada pelo usuário.

Não interpretar essa decisão como proibição de inventariar o legado durante o onboarding autorizado.

<a id="e32"></a>

### E32 — Conclusão com inconformidades não críticas

A pergunta foi se o onboarding poderia ser concluído com pendências não críticas catalogadas, em vez de exigir a resolução integral de todas as inconformidades.

Resposta:

"Permitir."

A decisão não autoriza ocultar pendências, eliminar evidências ou considerar uma falha crítica como resolvida.

<a id="e33"></a>

### E33 — Classificação automática de criticidade

A pergunta foi se a Plataforma poderia classificar autonomamente inconformidades mediante critérios rigorosos, objetivos e verificáveis, recorrendo ao engenheiro quando não conseguir determinar a criticidade com segurança.

Resposta:

"Sim."

A taxonomia, os limiares e os critérios técnicos detalhados apresentados posteriormente continuam candidatos.

## BLOCO G — RESPONSABILIDADES TRANSVERSAIS E CONTINUIDADE

<a id="e34"></a>

### E34 — Gestão estruturada e contínua de pendências

O usuário determinou que dúvidas, conflitos, impedimentos e lacunas identificados durante a importação sejam catalogados de forma:

- Estruturada.
- Hierarquizada.
- Instrutiva.
- Detalhada.
- Rastreável.
- Disponível aos agentes e engenheiros envolvidos.

A cada leitura ou ciclo de execução, os agentes deverão identificar rapidamente as pendências relevantes e comunicar seu estado ao engenheiro.

Essa exigência deverá ser representada individualmente no registro documental.

Não presumir que todo ciclo de execução precisa carregar integralmente todos os registros de pendência no contexto do modelo.

A estratégia de índices e roteamento continua a especificar.

<a id="e35"></a>

### E35 — Esclarecimentos posteriores e retroalimentação contínua

O usuário determinou que o engenheiro possa fornecer informações, esclarecimentos, diretrizes e decisões em momentos posteriores ao onboarding.

As informações pertinentes deverão retroalimentar o conhecimento Micro, Meso e Macro.

A incorporação deverá respeitar verificações, proveniência, autorização, consistência e publicação canônica.

A exigência de atualização contínua não autoriza execução assíncrona inexistente, publicação sem controles nem sobrescrita silenciosa.

Os mecanismos duráveis e os gatilhos concretos continuam a especificar.

<a id="e36"></a>

### E36 — Encerramento do Discovery 01 e continuidade do Discovery 02

O usuário concordou em encerrar e consolidar o Discovery 01 antes de aprofundar o Motor de Compreensão Profunda de Repositórios em outra sessão.

A razão expressa é preservar o trabalho produzido, evitando perda de contexto, decisões e detalhes.

O usuário autorizou a execução da consolidação e posteriormente solicitou a elaboração e a revisão rigorosa do Prompt-Master corretivo.

A nova missão deverá preparar a retomada, sem antecipar o Discovery 02 nem aprovar sua arquitetura.

---

# 5. INVENTÁRIO DAS PROPOSTAS E RECOMENDAÇÕES DO ASSISTENTE

A reconciliação não deverá preservar apenas decisões humanas.

Também deverá inventariar propostas técnicas relevantes que surgiram durante o Discovery, para que possam ser retomadas e avaliadas sem reconstruir a conversa.

Verifique especialmente os seguintes grupos:

**P-A — Processo de onboarding**

Importação, inventário, descoberta, análise, estruturação, organização hierárquica, roteamento de contexto, aplicação do conhecimento e atualização incremental.

**P-B — Modelo de conhecimento**

Separação entre fatos observados, comportamentos verificados, relatos, hipóteses, interpretações, dependências, incertezas e evidências.

**P-C — Arquivos Agent-First**

`AGENTS.md` como entrada/roteador, documentação especializada, índices, manifestos, esquemas, skills e configurações específicas de ferramentas.

Não presumir que essa árvore já foi aprovada.

**P-D — Adaptadores de agentes**

Conhecimento agnóstico, projeções específicas para Devin, Claude e Copilot e configurações mínimas necessárias.

**P-E — Compartilhamento e concorrência**

Descobertas locais, contribuições candidatas, conhecimento compartilhado, deduplicação, reconciliação de conflitos e integração versionada.

**P-F — Guardrails de consolidação**

Proveniência, validação independente, atualidade, controle de acesso, revisão-base, integridade, idempotência, segurança e recuperação.

**P-G — Validação sem novas GitHub Actions**

Motor de validação próprio da Plataforma, com possível integração futura aos controles remotos corporativos.

Não declarar que verificações locais são equivalentes a bloqueios no servidor.

**P-H — Composição de ambientes**

Referências distintas para código em desenvolvimento, versões implantadas, comportamentos de referência, contratos e simulações.

**P-I — Conhecimento externo**

Catálogo de sistemas, referências documentais, conhecimento derivado, classificação de acesso e verificação de atualidade.

**P-J — Migração controlada**

Inventário origem→destino, classificação de artefatos, comparação semântica, preservação de conhecimento, análise de skills e hooks, relatórios de migração e exclusão autorizada.

**P-K — Estados e UX**

Provisório, concluído, concluído com ressalvas, bloqueado, crítica, não crítica, indeterminada, revisão necessária e demais estados sugeridos.

Não transformar taxonomias sugeridas em máquinas de estado aprovadas.

**P-L — Critérios de compreensão e qualidade**

Cobertura conhecida, evidências, explicações fundamentadas, impacto de alterações, testes sintéticos, verificação independente e limites de confiança.

Para cada grupo, determine:

1. Qual contribuição material foi proposta.
2. Se houve manifestação humana que aceitou a intenção.
3. O que permaneceu apenas como detalhamento do assistente.
4. Se já existe registro correspondente.
5. Se há duplicidade, contradição ou omissão.
6. Qual o encaminhamento documental necessário.

Não é necessário criar um registro para cada frase ilustrativa.

O objetivo é preservar propostas materialmente relevantes, evitando burocracia excessiva e duplicação.

---

