# Ecossistema atual de engenharia relatado

Versão documental: 0.1.0 · 30/10/2026 · **RELATO CONTEXTUAL, sem validação institucional**.

Fontes: SRC-001 e SRC-002, definidas no [registro de conhecimento](registro-conhecimento.md). O dossiê atual e sua reprodução na conversa de origem permitem reconstruir o contexto relatado, mas não comprovam procedimentos de todo o banco. Não foram inspecionados sistemas internos, documentos corporativos, credenciais ou repositórios do banco.

Este arquivo descreve o ambiente atual relatado. Capacidades desejadas da futura plataforma estão na [visão do produto](visao-produto.md) e no [catálogo](capacidades.md). Uma ferramenta citada aqui não é um conector implementado.

## Organização e fluxo de demanda

| ID | Informação relatada | Limite ou confirmação pendente |
|---|---|---|
| BAN-001 | Organização geral: squads → coordenações → gerências → superintendências → diretorias → CEO | Não há organograma oficial consultado; não extrapolar o relato para todas as unidades |
| BAN-002 | Analistas, Tech Leads, PMs, SMEs e desenvolvedores participam das demandas | Responsabilidade por artefato e aprovação varia e precisa ser mapeada |
| BAN-003 | Demandas passam por discussões, reuniões, esclarecimentos, alinhamentos entre squads, impedimentos e planejamento de sprint | Cerimônias, tempos, SLAs e critérios de entrada/saída não confirmados |
| BAN-004 | Features, histórias, bugs e tasks são gerenciados em ServiceNow/IuClick | Relação entre os nomes, tipos, campos, estados e APIs ainda não confirmada |
| BAN-005 | Microsoft Teams é usado em reuniões; gravações e transcrições foram citadas no contexto de discovery | Não presumir gravação universal, acesso, autorização, retenção ou API disponível |

Uma demanda pode exigir esclarecer regras e impactos com mais de uma squad. O relato sustenta a necessidade de mapear dependências e pendências; não informa um modelo completo de workflow ou uma política corporativa de transcrição.

## Repositórios e preparação de aplicações

| ID | Informação relatada | Limite ou confirmação pendente |
|---|---|---|
| BAN-006 | Os repositórios ficam no GitHub | Hospedagem, organizações, permissões e integrações internas não inspecionadas |
| BAN-007 | Novo repositório é solicitado por issue em repositório de provisionamento; pipeline realiza a criação | Template da issue, aprovadores, validações e contratos não disponíveis |
| BAN-008 | Templates incluem `iupipes.yml`, com linguagens, ferramentas, Terraform, contas AWS e identificação das equipes | Esquema real, campos obrigatórios e política de alteração desconhecidos |
| BAN-009 | Terraform é usado para infraestrutura | Módulos, estados, runners, políticas e organização das contas não confirmados |
| BAN-010 | Aplicações passam por cadastro no Defect Dojo, envolvendo a identificação sigla app e etapa de aprovação arquitetural | Não há comprovação do fluxo, APIs, taxonomia ou autoridade de aprovação |
| BAN-011 | São citados IUQuali, TAAC e TestSpec | Responsabilidades e relações são parcialmente desconhecidas; manter PEN-004 aberta |

`sigla app` é a denominação relatada. Não expandir a sigla nem inventar seu formato. Nomes internos não devem ser usados para inferir uma integração padrão de fornecedor.

## Desenvolvimento, qualidade e promoção

O encadeamento descrito foi:

`feature branch → GitHub Action → PR para develop → aprovações e verificações, incluindo análise estática/Sonar → PR para release/HOM → aprovação e automação → PR para main/PROD`.

Esse encadeamento é BAN-012. Ele não foi convertido em configuração deste repositório, não constitui ordem de execução desta missão e não prova que todos os sistemas do banco adotem exatamente o mesmo modelo de branches. O GitHub desta fundação tem seu próprio estado observado e PRs candidatos; não é um ambiente produtivo do banco.

BAN-013: a implantação produtiva descrita depende de associação com histórias do ServiceNow e de GMUD, com aprovações e janela permitida. Não foram confirmados responsáveis, número de aprovações, expiração, evidência exigida, fallback ou regra emergencial.

BAN-014: existe fluxo de incidentes, bugs e hotfix. Sua ordem detalhada e os vínculos exatos entre registros, branches e implantações precisam de validação. Nenhum processo de hotfix interno foi executado aqui.

BAN-015: Sonar foi mencionado entre verificações de qualidade. Cobertura, quality gates, tratamento de falso positivo, exceções e relação com IUQuali/TAAC/TestSpec não foram inspecionados. A presença do nome não garante que um teste esteja executado ou aprovado.

## Infraestrutura, operação e acesso

| ID | Informação relatada | Limite ou confirmação pendente |
|---|---|---|
| BAN-016 | Aplicações utilizam AWS e ambientes DEV/HOM/PROD | Serviços, regiões, redes, contas, limites e separação por aplicação não confirmados |
| BAN-017 | Produção possui controles de acesso e procedimentos excepcionais de break-glass | Não há autorização produtiva, credencial ou direito de break-glass para esta missão |
| BAN-018 | Datadog é a principal observabilidade relatada | Dashboards, monitores, logs, métricas, traces, integração com incidentes e retenção não inspecionados |

O relato de diagnósticos e correções desejados para a plataforma não prova a existência de um correlacionador entre ServiceNow, Datadog, AWS e GitHub. Esse comportamento é pretendido e depende de discovery, contratos e acesso autorizado.

## Perguntas para internalização e discovery

| Pendência | O que esclarecer | Evidência permitida a buscar |
|---|---|---|
| PEN-003 | Quais variações do processo existem entre squads e aplicações? | Descrição autorizada de uma jornada representativa; evitar generalização institucional |
| PEN-004 | O que IUQuali, TAAC e TestSpec fazem, e como se relacionam? | Documentação interna autorizada ou explicação do responsável; não supor atribuições |
| PEN-005 | Quais tipos, campos, estados e IDs de ServiceNow/IuClick são necessários? | Contratos e exemplos sanitizados aprovados internamente |
| PEN-006 | Como funcionam provisionamento por issue, `iupipes.yml`, sigla app e Defect Dojo? | Templates e esquemas sanitizados, sujeitos a autorização |
| PEN-007 | Quais aprovações, janelas e exceções regem GMUD, hotfix e produção? | Processo vigente e responsáveis internos; não substituir por hipótese técnica |
| PEN-008 | Quais acessos e dados poderão ser usados por adaptador? | Matriz de acesso e classificação aprovada no ambiente interno |

Faltas de acesso a essas evidências não bloqueiam a concepção externa com dados sintéticos e contratos propostos. Elas bloqueiam afirmações de fidelidade corporativa completa e a ativação de integrações reais.

## Regra de atualização

Uma nova informação deve preservar a origem, o escopo organizacional e a data do relato. Se houver divergência, registrar as versões e a pendência de reconciliação; não substituir silenciosamente um relato por recomendação do assistente. Um documento corporativo autorizado poderá confirmar ou corrigir o contexto, mediante registro de fonte e revisão. Até lá, BAN-001..BAN-018 têm natureza **FATO RELATADO**, não fato institucional verificado.
