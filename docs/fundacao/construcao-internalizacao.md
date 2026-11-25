# Construção externa e internalização

Versão documental: 0.1.0 · 30/10/2026 · **Direção declarada com detalhamento de engenharia proposto**.

Fontes SRC-001 e SRC-002. A intenção é construir externamente uma plataforma real e portátil, depois integrar os serviços específicos do banco no ambiente interno por profissionais autorizados. A missão atual implementa a fundação para especificar essa plataforma; não inicia o produto final antes do refinamento e aprovação dos requisitos.

## Entrega externa pretendida

Uma interface visual isolada ou uma estrutura vazia não satisfará a intenção declarada. A construção progressiva deverá contemplar frontend, backend, persistência, motor de orquestração, agentes, conectores desacoplados, mocks/simuladores, testes, documentação e empacotamento. Stack, formato de distribuição, hospedagem, estratégia de identidade e licenças ainda precisam de decisão.

| Componente futuro | Responsabilidade a especificar | Evidência externa proposta |
|---|---|---|
| Frontend/IDE | Workspaces, demandas, código/contexto, execução e supervisão | Jornadas completas com estados, acessibilidade, falhas e recuperação |
| Backend e domínio | Requisitos, fontes, revisões, decisões, permissões e rastreabilidade | APIs e comportamento testados, sem depender apenas da apresentação |
| Persistência | Dados, histórico, conflitos, retenção, recuperação e integridade | Escrita/releitura, migração e recuperação com dados sintéticos |
| Motor de orquestração | Planos, tarefas, dependências, agentes, cancelamento e evidências | Execução isolada, concorrência, timeout, interrupção e retomada |
| Agentes/executores | Trabalho especializado sob escopo e orçamento definidos | Contrato de tarefa e resultado, testes independentes, erros reconhecidos |
| Conectores | Adaptar serviços externos sem acoplar o domínio a um fornecedor | Porta documentada, simulador e teste de contrato por versão |
| Empacotamento | Instalação reproduzível, configuração e operação | Artefato versionado, inventário de dependências e roteiro validado |
| Documentação | Operação, contratos, limites, segurança e evolução | Referências coerentes com comportamento efetivo e versão do pacote |

Esta tabela define o que deverá ser especificado e demonstrado em fases futuras; não certifica que os componentes existam agora.

## Fronteira entre domínio e conectores

Recomendação arquitetural para a fase de contratos: expor portas de domínio para repositório, gestão de demanda, reunião/transcrição, observabilidade, infraestrutura e executor. O domínio deverá tratar resultados e erros documentados, sem exigir formatos internos de um fornecedor. Adaptadores reais e simuladores deverão implementar a mesma versão do contrato, com diferenças e limites explícitos.

| Família | Integração pretendida ou contexto relatado | O que pode ser desenvolvido externamente | Dependência interna |
|---|---|---|---|
| Repositórios/CI | GitHub, provisionamento por issue, `iupipes.yml`, PRs e checks | Contratos propostos e repositórios sintéticos; testes com acesso autorizado | Templates, políticas, esquemas e identidades corporativas |
| Demanda | ServiceNow/IuClick | Modelo sintético de feature/história/bug/task, IDs e estados propostos | APIs, taxonomia real, permissões e transições vigentes |
| Reuniões | Teams, gravações e transcrições | Fixtures sintéticas de reunião e extração com proveniência | Consentimento, classificação, retenção, APIs e escopo permitido |
| Qualidade/arquitetura | Sonar, Defect Dojo, sigla app, IUQuali/TAAC/TestSpec | Interfaces e cenários genéricos claramente marcados como hipóteses | Responsabilidades reais, contratos e gates corporativos |
| Infraestrutura | Terraform e AWS DEV/HOM/PROD | Simuladores, planos e fixtures sem conta ou segredo corporativo | Contas, serviços, redes, políticas, identidade e autorização |
| Observabilidade/incidente | Datadog e ServiceNow | Logs, métricas, traces e incidentes sintéticos correlacionáveis | Acesso a telemetria, dados, severidade e processo vigente |
| Executor | Devin CLI, conforme visão pretendida | Contrato e simulador de execução; prova técnica isolada se disponível | Disponibilidade, licença, credencial, política e capacidades reais |

Mock aprovado em teste de contrato não prova integração interna. O contrato proposto deverá ser reconciliado com o real, mantendo rastreabilidade das incompatibilidades e seus impactos no domínio e na UX.

## Gatilhos e gates propostos

| Gate | Entrada necessária | Resultado a demonstrar | Impeditivo que exige decisão ou acesso |
|---|---|---|---|
| EXT-01 — Recorte de produto | Discovery e prioridade explícita | Jornada, perfis, limites e critérios de valor definidos | Ambiguidade material de escopo ou prioridade |
| EXT-02 — Especificação | Requisitos, UX e restrições revisados | Comportamentos, estados, falhas, contratos e aceite rastreáveis | Regras de negócio ou permissões ainda indefinidas |
| EXT-03 — Plano executável | Arquitetura e qualidade aprovadas no alcance necessário | Tarefas isoladas, testes, dependências, contextos e limites de execução | Decisões arquiteturais materiais pendentes |
| EXT-04 — Construção externa | Plano autorizado | Plataforma executável com frontend/backend/motor/persistência e simuladores, verificada por testes independentes | Falha crítica ou evidência insuficiente |
| INT-01 — Admissão interna | Pacote externo e documentação | Revisão de segurança, licença, dados, dependências e implantação no processo do banco | Autorização e regras internas |
| INT-02 — Adaptação | Contratos e acessos autorizados | Conectores reais reconciliados e testados nos ambientes permitidos | Acesso essencial ou contrato real indisponível |
| INT-03 — Homologação | Integração e requisitos corporativos | Jornadas e falhas reais homologadas com rastreabilidade | Aceite dos responsáveis competentes |
| INT-04 — Operação produtiva | Homologação e processos aplicáveis | Evidências de autorização, GMUD/janela e plano de recuperação | Confirmação final explícita e aprovações corporativas |

Os gates acima são propostas de engenharia para detalhar nas fases próprias. Nenhum deles cria autorização produtiva, ratifica PGC ou substitui controles corporativos.

## Dados e operação permitidos

Externamente, trabalhar com dados sintéticos e fontes públicas ou expressamente autorizadas. Não presumir acesso a código interno, gravações, transcrições, logs, segredos, credenciais ou informações de clientes. Dados sintéticos podem exercitar classificação, detecção de marcadores sensíveis e falhas; isso não comprova um sistema universal de prevenção de vazamentos.

O ambiente externo deverá poder demonstrar uma jornada sem usar credenciais corporativas. Configuração, identidades e segredos reais deverão permanecer separados do pacote distribuível. A importação ao banco não dispensa nova análise de dependências, acessos, políticas e riscos.

Operações em produção, mudanças de infraestrutura, acionamento de break-glass e implantação de hotfix não estão autorizados nesta missão. A futura plataforma deverá preparar e verificar mudanças, mas a passagem produtiva depende da confirmação final do engenheiro e das aprovações corporativas aplicáveis.

## Critérios de portabilidade a especificar

Propostas para a arquitetura: configuração por ambiente; versionamento de schemas e contratos; migrações e backup/restauração; observabilidade do próprio motor; limites de custo e recursos; comportamento quando um conector está indisponível; instalação e atualização reproduzíveis; inventário de dependências e licenças; substituição de executor sem alterar a semântica de aprovação; possibilidade de operação com simuladores em ambiente isolado.

Nenhum formato como container, Kubernetes, serviço gerenciado ou desktop foi escolhido implicitamente. PEN-012 reserva essas decisões para requisitos não funcionais, arquitetura e internalização.
