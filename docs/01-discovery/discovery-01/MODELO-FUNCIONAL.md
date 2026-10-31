# Modelo funcional reconciliado do onboarding Agent-First

Revisão 2 · missão D01-R2. O [REGISTRO.md](REGISTRO.md) é a fonte canônica das definições; este documento organiza suas relações e fluxos. As âncoras E01..E36 remetem ao dossiê **reproduzido pelo usuário no pedido atual**, D01-S05, disponível no [acervo de evidência](../../../auditorias/discovery-01-r2/DOSSIE-REPRODUZIDO.md). Não são IDs de mensagens originais recuperadas. A qualidade da proveniência está em [FONTES.md](FONTES.md), e as mudanças de classificação em [RETIFICACOES.md](RETIFICACOES.md).

A [revisão 1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/d9e48c3d36598d40f9d2e38caf836bccb5fac97f/docs/01-discovery/discovery-01/MODELO-FUNCIONAL.md) permanece no histórico. Sua incerteza sobre a topologia conceitual é retificada pelo dossiê atual; a falta de detalhes técnicos não desfaz as escolhas declaradas. Nenhuma funcionalidade da Plataforma foi implementada por esta documentação.

## Objetivo e compreensão

O onboarding deve importar, absorver, compreender, estruturar e utilizar o conhecimento de um ou mais repositórios, independentemente de sua organização, natureza, finalidade, linguagens e tecnologias. O conhecimento subsidia explicações, esclarecimentos, investigação, planejamento, modificações de código autorizadas, validações e demais funcionalidades. É intenção de produto, sem garantia de compreender perfeitamente qualquer sistema (E01).

A profundidade desejada aproxima-se do entendimento que um engenheiro experiente obtém ao estudar um sistema: finalidade e contexto de negócio; regras; fluxos e comportamentos; arquitetura e responsabilidades; linguagens e frameworks; componentes e estruturas; integrações e contratos; dependências internas e externas; infraestrutura e configurações; execução local; estratégias e procedimentos de testes; particularidades, limitações e riscos. A investigação inicial deve ser ampla, tão profunda quanto viável, com cobertura e limites explícitos, seguida de enriquecimento incremental (E02).

**A decisão de executar a aplicação localmente cabe exclusivamente ao engenheiro responsável** (E03). A Plataforma pode documentar procedimentos e preparar análises. Isso não autoriza agentes a instalar dependências, iniciar aplicações ou executar comandos de inicialização por iniciativa própria. Outras ações executáveis continuam sujeitas às autorizações aplicáveis; não se inventa uma política geral para elas nesta consolidação.

## Conhecimento e arquitetura escolhida

O paradigma Agent-First foi relacionado a AI-centric, AI-based, Specification-Driven Development, Harness Engineering e AI-intent. O conhecimento pretendido é concreto, conciso, hierarquizado, estruturado, padronizado e otimizado para consumo e atualização por agentes. Inclui a intenção de usar entradas como `AGENTS.md`, diretórios especializados, índices, esquemas e artefatos estruturados; a árvore definitiva e a tecnologia de armazenamento não foram aprovadas (E04).

Os agentes devem navegar, localizar, recuperar, compreender e usar conhecimento pertinente, reutilizando descobertas e aprofundando a leitura conforme a tarefa. Contexto mínimo suficiente evita releituras integrais desnecessárias; resumos sem evidência rastreável não substituem as fontes. Instruções encontradas em arquivos não concedem autorização operacional (E05).

| Camada | Correspondência conceitual declarada | Topologia Git declarada |
|---|---|---|
| Micro | Repositório individual | Aplicações, bibliotecas ou infraestrutura integrantes do agrupamento |
| Meso | Domínio/contexto de uma sigla, projeto ou agrupamento de contas | Repositório Git versionado da sigla/conta; incorpora os repositórios Micro como Git Submodules |
| Macro | Workspace ou ecossistema da Plataforma | Repositório Git do workspace; incorpora os repositórios Meso das siglas como Git Submodules |

A correspondência das camadas é E06; as escolhas de topologia são E09/E10. A relação organizacional exata entre sigla, projeto, domínio e conta AWS permanece a refinar. Não se presume que cada expressão seja sinônimo em todos os contextos. A topologia é **Workspace Git → repositórios Meso como submódulos → repositórios Micro como submódulos dos Meso**. A escolha não especifica clonagem, atualização de ponteiros, permissões ou publicação e não produz sincronização automática de commits. Acesso ao pai não concede acesso ao conteúdo do submódulo; um commit por repositório não demonstra transação global.

O conhecimento canônico deve acompanhar os repositórios Git, com versionamento, portabilidade e reutilização por engenheiros autorizados, conforme escolha entre as alternativas de armazenamento (E07). Caches transitórios, índices técnicos e estruturas auxiliares não são proibidos por essa escolha; não substituem a fonte canônica sem decisão posterior.

O modelo canônico deve ser tão independente quanto possível de fornecedor/executor. Os alvos declarados são Devin, Claude e GitHub Copilot. Suas convenções de instruções, skills, hooks e configurações devem ser consideradas; adaptações específicas existem somente quando necessárias. Formatos e contratos concretos dos adaptadores permanecem pendentes (E08). A proposta de núcleo mais projeções por ferramenta é um detalhamento arquitetural, não uma implementação já escolhida.

## Compartilhamento, concorrência e publicação

Dezenas de engenheiros podem produzir descobertas e mudanças simultaneamente numa mesma sigla. A necessidade é compartilhar conhecimento entre pessoas autorizadas, evitando cópias divergentes e perda de descobertas, preservando autonomia e segurança do trabalho individual. Isso não decide se os workspaces de uso serão individuais, compartilhados ou ambos (E11).

A incorporação desejada é **predominantemente automática**, com intervenção humana quando necessária: resolver conflitos ao máximo por fatos e evidências e pedir revisão ou aprovação do que não puder ser resolvido com segurança (E12). Há exigência de barreiras rigorosas contra alucinações, inferências não comprovadas, contradições, incoerências, conflitos de versões, perda silenciosa e consolidação de informação incorreta. Confiança verbal de LLM não é prova suficiente; critérios, verificadores, classificadores e limiares ainda precisam de especificação (E13).

A decisão E14 aceita consolidação automática somente após verificações e controles, mantendo pushes de trabalho separados da publicação canônica. Preparação, validação e publicação permanecem distintas. Não autoriza merge irrestrito ou mudança de branches protegidas. Deduplicação, revisão-base, integridade, validação independente, idempotência, controle de acesso e recuperação são propostas de mecanismos para concretizar essa intenção; seus protocolos não foram aprovados em detalhe.

O usuário relatou falta atual de autonomia para criar novas pipelines no GitHub Actions corporativo (E15). Um motor de validação próprio da IDE é recomendação a refinar; verificações locais não equivalem a barreira remota contra pushes feitos fora da Plataforma. A restrição relatada não é proibição permanente de futura integração autorizada.

## Branches, ambientes e dependências heterogêneas

O fluxo corporativo descrito em E16 é **relato contextual**, sujeito à natureza de cada repositório: commit em feature branch → Action → PR para develop após sucesso → aprovação e duas Actions relacionadas à promoção para release → PR para main após resultados necessários → Action da main → parada em `scheduled` → preparação e aprovação da GMUD no ServiceNow/IUClick → continuação da Action na janela autorizada. Também foi relatado hotfix produtivo associado a bug/incidente ServiceNow, com caminho próprio de pipeline para main. Não é uma política institucional universal verificada nem configuração desta missão.

A Plataforma deve distinguir código em branches das versões efetivamente implantadas em DEV, HOM e PROD. **Código em `main` não comprova implantação em PROD**; a verificação de deployments ainda deve ser especificada (E17).

Uma funcionalidade pode envolver vários repositórios em feature branches e, ao mesmo tempo, depender de comportamentos de versões em HOM ou PROD de outros sistemas. Não se presume branch, versão ou ambiente uniforme entre os participantes. O modelo técnico de contexto composto permanece candidato (E18).

A escolha de produto contempla tanto reprodução controlada de contratos/comportamentos, por simulações e mocks, quanto integrações reais com os acessos e autorizações apropriados. Essa escolha não concede acesso real a serviços internos (E19). Referências separadas para código em desenvolvimento, implantação, comportamento de referência, contratos e simulações são uma proposta técnica para representar a heterogeneidade.

## Conhecimento externo e autorização

A organização relatada tem muitas equipes, repositórios e fronteiras de acesso. A Plataforma deve compreender interfaces e dependências de sistemas cujo código ou implementação não estejam acessíveis, na medida das fontes autorizadas disponíveis. Camunda, IBM ODM, APIs de outras equipes e plataformas/serviços restritos foram exemplos; documentação da interface não demonstra compreensão da implementação interna (E20).

GitHub Pages, SharePoint, contratos, testes, documentação técnica e outras fontes autorizadas podem oferecer conhecimento indireto. Não se exige que todo sistema seja importado como submódulo Git; o catálogo federado sugerido é proposta de formato (E21).

A fonte externa deve permanecer como referência. No Git da sigla, consolidar somente conhecimento derivado legitimamente armazenável e compartilhável, preservando origem, versão, escopo, autorização, limites e atualidade. Acessibilidade técnica não é permissão de copiar ou redistribuir (E22).

| Ação/modalidade | Definição declarada | Limite preservado |
|---|---|---|
| Buscar/consultar fonte exterior | Informar ao engenheiro e executar caso haja autorização; apresentar finalidade, fonte pretendida e escopo (E23) | Identificar necessidade de consulta não autoriza realizá-la |
| Autorização pontual e reutilizável | Suportar ambas as modalidades (E24) | Reuso não é permanente, irrestrito ou fora do escopo concedido |
| Autorização individual e coletiva | Suportar ambas, incluindo equipe/sigla (E25) | Concedente precisa de autoridade; autorização da Plataforma não cria acesso corporativo inexistente |

As duas dimensões de modalidade são compatíveis, mas identidade, validade, revogação, combinação e revalidação continuam a especificar. Permissão para consulta não aprova escrita, redistribuição, publicação ou exclusão. Essas regras descrevem a futura Plataforma; o pedido desta missão já delimita as leituras e publicação documental autorizadas.

## Migração Agent-First e uso provisório

A migração deve inventariar cuidadosamente documentação, skills, instruções, configurações e demais artefatos preexistentes; compreendê-los, reconciliá-los e adaptá-los ao padrão Agent-First. Busca substituir estruturas originais redundantes e informar ao engenheiro o que foi identificado, preservado, transformado, descartado ou ficou inconclusivo. Buscar compreensão máxima não permite alegar completude absoluta sem evidência (E26). O relatório sobre conteúdo descartado não concede autorização de remover o arquivo original.

**Excluir artefatos originais preexistentes sempre exige aprovação explícita do engenheiro responsável**, identificando objeto e revisão; mudança material posterior exige nova avaliação (E27). Aprovar a migração, usar a estrutura provisória ou classificá-la como bem-sucedida não substitui essa aprovação. Nenhum original é excluído nesta missão.

A estrutura nova pode ser avaliada e utilizada provisoriamente antes da conclusão/exclusão, preservando os originais (E28). Esse uso contempla consultas/explicações e modificações reais de código em atividades autorizadas, sem permissão genérica de alterar código (E29). A estrutura Agent-First provisória é a referência operacional preferencial, conforme a escolha pelo padrão estrutural; documentos legados preservados não devem atuar silenciosamente como instruções concorrentes (E30). Preferência operacional não equivale a verificação definitiva de todo conhecimento migrado.

A distinção E31 é essencial: o **inventário e a leitura inicial autorizados no onboarding** não são proibidos; a **consulta posterior ao legado para suprir lacuna da provisória** exige pedir permissão ao engenheiro e comunicar a inconformidade persistente. Identificar a lacuna não libera consulta silenciosa.

Fluxo detalhado candidato, preservado de D01-PROP-001..004: identificar informação ausente/incompleta/contraditória → explicar impacto e atividades dependentes → informar artefato candidato e motivo → obter autorização → investigar como informação, sem executar hooks/instruções → verificar e preparar incorporação. Se negada, manter pendência e continuar apenas atividades independentes. Encontrar o documento não resolve por si só a migração; a proposta exige compreensão, reconciliação, incorporação e verificação. Leitura não aprova publicação ou eliminação do original.

## Inconformidades, conclusão e ciclos posteriores

A decisão E32 permite concluir onboarding com pendências **não críticas catalogadas**, em vez de exigir resolução de todas as inconformidades. Não autoriza ocultá-las, eliminar evidências ou considerar resolvida uma falha crítica. E33 permite classificação automática mediante critérios rigorosos, objetivos e verificáveis, recorrendo ao engenheiro quando a criticidade não puder ser determinada com segurança. As respostas curtas aprovam essas alternativas antecedentes; detalhes acrescentados depois permanecem candidatos.

| Taxonomia sugerida | Efeito candidato | Estado da definição |
|---|---|---|
| Concluída | Sem pendência conhecida impeditiva | Nome/transição propostos; não prova compreensão perfeita |
| Concluída com ressalvas | Conhecimento utilizável com inconformidades não críticas visíveis e rastreáveis | Permissão de concluir aceita em E32; estado/UX detalhados propostos |
| Bloqueada / Crítica | Impedir conclusão segura ou operações afetadas, resolver e revalidar | Critérios, alcance do bloqueio e transições a especificar |
| Indeterminada / Revisão necessária | Investigar ou pedir avaliação antes de liberar dependentes | Recurso ao engenheiro aceito em E33; taxonomia/fluxo propostos |

Segurança, perda de conhecimento, alteração de comportamento, integridade de instruções, dependências e consequências para agentes são fatores sugeridos para classificação. Comparação de versões, verificações determinísticas e testes independentes, quando possíveis, são guardrails propostos. Quantidade de pendências ou confiança declarada pelo modelo não bastam. Referência documental quebrada e perda de instrução de segurança são exemplos a avaliar pelo impacto; não constituem regras universais de criticidade aprovadas. Bloqueios proporcionais, justificativas visíveis, artefatos afetados, evidências, medidas de resolução e revisão humana que preserve controles são detalhamentos candidatos.

**Gestão contínua de pendências (E34):** dúvidas, conflitos, impedimentos e lacunas da importação devem ser catalogados de modo estruturado, hierarquizado, instrutivo, detalhado, rastreável e disponível a agentes/engenheiros envolvidos. A cada leitura ou ciclo, os agentes devem identificar rapidamente as pendências relevantes e comunicar o estado ao engenheiro. Isso não exige carregar todas as pendências integralmente em cada contexto; índices e roteamento ainda serão especificados. A conclusão com ressalvas não encerra nem oculta esse acompanhamento.

**Retroalimentação posterior (E35):** o engenheiro pode fornecer novas informações, esclarecimentos, diretrizes e decisões depois do onboarding. O conhecimento pertinente deve retroalimentar Micro, Meso e Macro com verificações, proveniência, autorização, consistência e publicação canônica. A exigência não implementa execução assíncrona nem autoriza publicação sem controles ou sobrescrita silenciosa; mecanismos duráveis e gatilhos seguem pendentes.

## Jornada organizada — sequência ainda proposta

As escolhas de produto acima permanecem distintas desta decomposição de engenharia, que organiza P-A/P-J sem impor uma máquina de estados aprovada.

| Etapa candidata | Resultado esperado e fronteira |
|---|---|
| Delimitar escopo | Repositórios/revisões e fontes autorizados; registrar acesso ausente sem inventar conhecimento |
| Inventariar e compreender | Artefatos preexistentes, código e fontes disponíveis; análise ampla com evidência, limites e pendências; sem execução local por iniciativa do agente |
| Estruturar | Conhecimento canônico em Git nas camadas escolhidas, com agnosticidade e adaptação necessária; sem árvore definitiva inventada |
| Reconciliar | Comparar origem/destino, perdas, duplicações e contradições; preparar contribuições sob controles, distintas da publicação canônica |
| Usar provisoriamente | Preferir a nova estrutura, preservar originais, sinalizar lacunas e respeitar autorizações de código e de consulta posterior ao legado |
| Classificar e concluir | Critérios objetivos e recurso humano se incerto; conclusão com pendências não críticas rastreáveis; demais estados ainda candidatos |
| Consolidar e atualizar | Publicação controlada; exclusão somente com aprovação própria; pendências e esclarecimentos retroalimentam o conhecimento relevante continuamente |

## Propostas técnicas preservadas para refinamento

O inventário completo e as relações com decisões estão no registro e na matriz. Esta visão mantém os grupos P-A..P-L sem convertê-los em escolhas de implementação.

| Grupo | Contribuição proposta / limite |
|---|---|
| P-A — Processo | Sequência de importação, inventário, descoberta, análise, estruturação, hierarquia, roteamento, uso e atualização; a intenção do onboarding é declarada, a decomposição é proposta |
| P-B — Modelo | Separar fatos observados, comportamentos verificados, relatos, hipóteses, interpretações, dependências, incertezas e evidências; schema a definir |
| P-C — Arquivos | `AGENTS.md` como entrada/roteador, documentação especializada, índices, manifestos, esquemas, skills e configurações; árvore concreta não aprovada |
| P-D — Adaptadores | Núcleo agnóstico e projeções/configurações mínimas para Devin, Claude e Copilot; agnosticidade declarada, contratos técnicos pendentes |
| P-E — Concorrência | Descobertas locais, contribuições candidatas, compartilhamento, deduplicação, reconciliação e integração versionada; mecanismos a definir |
| P-F — Guardrails | Proveniência, validação independente, atualidade, acesso, revisão-base, integridade, idempotência, segurança e recuperação; não certifica controle implementado |
| P-G — Validação | Motor próprio da Plataforma e eventual integração remota futura; não equivale a bloqueio de pushes externos |
| P-H — Ambientes | Referências distintas para desenvolvimento, implantação, comportamento, contratos e simulações; contexto composto é candidato |
| P-I — Externo | Catálogo de sistemas/fontes, conhecimento derivado, classificação de acesso e atualidade; catálogo federado não é decisão definitiva |
| P-J — Migração | Inventário origem→destino, classificação de artefatos, comparação semântica, preservação, análise de skills/hooks, relatórios e exclusão aprovada; protocolo detalhado a definir |
| P-K — Estados/UX | Provisório, concluído, ressalvas, bloqueado, crítica, não crítica, indeterminada e revisão necessária; não são máquina de estados ou layout aprovados |
| P-L — Qualidade | Cobertura conhecida, evidências, explicações fundamentadas, impacto, ensaios sintéticos, revisão independente e limites de confiança; métricas/limiares não escolhidos |

O esquema sugerido de um item migrado contém ID, origem/revisão, destino/revisão, natureza, evidência, estado, lacuna, operações afetadas, criticidade/justificativa/incerteza, referência de autorização quando houver, proposta de correção e verificação. Continua proposta, sem contrato de software aprovado. D01-HIP-001..003 e D01-PROP-001..011 são preservados no registro com seu estado, sem promoção automática.

## Continuidade e fronteira da missão

E36 determina consolidar D01 antes de aprofundar o Motor de Compreensão Profunda de Repositórios em nova sessão, preservando contexto, decisões e detalhes. A [entrada D02](../discovery-02/RETOMADA.md) prepara essa recuperação, sem executar o próximo Discovery ou aprovar sua arquitetura. A reconciliação material das fontes acessíveis e a recuperação técnica da transcrição integral são eixos distintos; refinamentos funcionais, técnicos ou corporativos não precisam ser resolvidos para preservar corretamente o que já foi declarado.

Esta missão é documental exploratória em branch/PR. Não concede acesso corporativo, execução de aplicações, pipelines, permissões, exclusão, merge, GMUD ou produção. PGC-001 v1.1.3 e CT v1.0.3 continuam NÃO RATIFICADOS; os 49 CA operacionais não são exercitados pelo modelo. Fontes do Projeto e GitHub têm revisões próprias; não se presume sincronização automática. Nenhuma árvore, parser, modelo de IA, banco, mecanismo vetorial, framework, algoritmo ou stack definitiva foi escolhido aqui.
