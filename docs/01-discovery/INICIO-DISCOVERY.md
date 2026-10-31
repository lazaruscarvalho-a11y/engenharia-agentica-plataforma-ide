# Entrada vigente D02 — revisão documental 3

Continue pela [retomada D02](discovery-02/RETOMADA.md), suas [retificações](discovery-02/RETIFICACOES.md) e pelo manifesto D02. D01-R2 materialmente reconciliado; histórico integral ainda não recuperado. A exceção futura de execução local não autoriza executar aplicações nesta missão; nenhuma refatoração no onboarding. O conteúdo anterior abaixo é histórico ou roteiro geral subordinado à entrada D02.

## Histórico preservado e roteiro geral

# Percurso atualizado — D01-R2

Revisão 2 do [Discovery 01](discovery-01/README.md): E01..E36 reconciliados a partir de declaração reproduzida no pedido, sem presumir transcrição integral recuperada. As escolhas conceituais e suas propostas derivadas estão separadas no [registro](discovery-01/REGISTRO.md). O [Discovery 02](discovery-02/RETOMADA.md) tem entrada preparada para o Motor de Compreensão Profunda de Repositórios. Ver [pendências](discovery-01/REVISAO.md) e recibo R2 para o estado de fechamento.

As seções abaixo são roteiro e estados HISTÓRICOS anteriores à R2. Não usar suas classificações antigas para desfazer as retificações documentadas.

# Atualização de percurso — Discovery 01 e 02

30/10/2026. O roteiro abaixo é o snapshot inicial da fundação. A conversa posterior “Iniciar discovery funcional” produziu definições sobre onboarding/conhecimento; somente seus cinco turnos finais estão disponíveis nesta consolidação. Consulte o [Discovery 01](discovery-01/README.md), a [revisão e lacuna de completude](discovery-01/REVISAO.md) e a [entrada Discovery 02](discovery-02/RETOMADA.md). O texto histórico “nenhuma entrevista” abaixo não descreve a totalidade das conversas posteriores. Nenhum requisito derivado é aprovado implicitamente.

## Roteiro inicial preservado

# Discovery inicial da Plataforma/IDE

Versão 0.1.0 — preparado para início; nenhuma entrevista de produto executada por este arquivo. Fontes SRC-001/SRC-002. Trabalhar com exemplos sintéticos e relatos autorizados; o escopo do produto continua em refinamento.

## Objetivo da primeira etapa

Entender quem usa a plataforma, quais problemas enfrenta, como atravessa uma demanda e como deseja supervisionar agentes. Transformar necessidades em propostas verificáveis de negócio, comportamento e UX, preservando incertezas. A existência do harness de governança não significa que a IDE esteja desenvolvida.

## Mapa de investigação

| Frente | Perguntas de conversa natural | Artefato esperado e sinal de suficiência |
|---|---|---|
| Negócio e valor | Onde há espera, retrabalho, falha ou perda de contexto? Qual resultado faria diferença? | Problema, consequência e medida candidata; distinguir relato de evidência quantitativa |
| Perfis e autoridade | O que analista, PM, Tech Lead, SME e desenvolvedor precisam ver/fazer? Quem pode aprovar, redirecionar ou interromper? | Perfis propostos, responsabilidades e conflitos; não inventar modelo de acesso aprovado |
| Jornada atual | Como reunião/demanda vira história, investigação, código, teste e implantação? Onde há handoffs? | Jornada com ferramentas, entradas, saídas e pendências; informações IUQuali/TAAC/TestSpec continuam abertas |
| Jornada desejada | Qual passo a plataforma deveria executar, sugerir ou deixar para a pessoa? | Autonomia por ação, pré-condições, autorização e resultado verificável |
| Workspaces e repositórios | Como selecionar vários repositórios e entender sua relação? O que precisa estar visível ao abrir um workspace? | Propostas de organização, indexação e mapa técnico; condições de atualização/falha |
| Experiência visual da IDE | Como o engenheiro acompanha tarefas/agentes? O que vê primeiro? Como inspeciona fontes/diffs, aprova, pausa e retoma? | Fluxos e estados de tela, navegação e feedback; alternativas visuais com decisão explícita posterior |
| Conhecimento e reuniões | Que fontes autorizadas ajudam? Como mostrar contradições, dúvidas, decisões e links à origem? | Proveniência, confiança, atualização e acesso; não supor captura automática |
| Orquestração e execução | O que a plataforma coordena e o que Devin CLI/executor recebe? Como tratar dependências, falhas e paralelismo? | Contratos candidatos e fronteiras de responsabilidade; capacidade real a verificar |
| Qualidade e rastreabilidade | Como provar que uma necessidade foi implementada e testada? O que exige revisão independente? | Relação necessidade→decisão→requisito→tarefa→código→teste→evidência |
| Incidentes e hotfix | Que informação seria necessária para diagnosticar? Quem autoriza ação e produção? | Jornada excepcional com limites; sem acionar sistemas reais ou contornar GMUD/break-glass |
| Construção e internalização | O que validar externamente com mocks? O que só pode ser integrado no banco? | Fronteiras, contratos substituíveis e critérios de homologação futura |
| Riscos e não funcionais | Quais perdas seriam inaceitáveis? Quais metas de tempo, escala, acessibilidade, segurança e custo precisam de medida? | Registro de riscos e metas candidatas; sem números arbitrários aprovados |

## Sequência recomendada de conversas

1. Um caso concreto de demanda e suas dores; identificar resultado, atores e jornada atual.
2. Jornada desejada e graus de autonomia; explorar supervisão humana e critérios de confiança.
3. Workspace/IDE visual: mapa de telas, informação prioritária, navegação, painel de agentes, inspeção de fontes/diffs, aprovação/interrupção e recuperação.
4. Módulos e limites: conhecimento, requisitos, planejamento, execução, qualidade, infraestrutura, observabilidade e incidentes; separar capacidades essenciais, posteriores e ainda incertas.
5. Requisitos de negócio e critérios mensuráveis; revisão das propostas e impactos, iniciando a fase 02 quando houver base suficiente.

São roteiros de conversa, não exigência de cinco novos chats. Prosseguir na sessão atual conforme foco/contexto; novas conversas são opção de organização do Projeto, com recuperação pelos artefatos.

## Formalização sem aprovação implícita

Registrar uma proposta quando a informação tiver impacto duradouro, com fonte e revisão. Para formalizar requisito candidato, obter: problema/objetivo, ator, gatilho, pré-condições, fluxo principal, alternativas/erros, dados, permissões, comportamento visual, dependências, resultado observável e critério de aceite. Item desconhecido vira pendência ligada ao requisito, com impacto e responsável quando conhecido.

Um critério de aceite descreve cenário e resultado testável; não basta “funciona bem”. Exemplo sintético: “Quando uma tarefa depende de outra ainda em execução, a interface indica a dependência e não apresenta a tarefa dependente como concluída”. Esse exemplo é proposta, não RF aprovado.

Revisar negócio, UX, viabilidade, segurança e teste por frentes distintas. Aprovação deve delimitar item/revisão/escopo; aceitar um layout não aprova integrações produtivas. Mudança posterior cria revisão e análise dos requisitos/fluxos/testes afetados. Persistir por ferramenta autorizada e emitir recibo somente após releitura.

## Critérios para avançar

- Problemas, atores e fronteiras do produto estão compreendidos e referenciados.
- Jornadas prioritárias têm passos, supervisão, exceções e estados visuais identificados.
- Cada capacidade tem maturidade explícita e prioridade proposta, com justificativa.
- Pendências materiais, riscos e dependências de acesso interno estão visíveis.
- Propostas de negócio podem ser revisadas sem depender de memória da conversa.
- Decisões do usuário estão separadas de detalhes sugeridos; nenhuma aprovação humana foi preenchida por agente.

O assistente inicia pelo roteiro de [PRIMEIRA-SESSAO](../chatgpt/PRIMEIRA-SESSAO.md). Ao encerrar um trecho relevante, apresentar o que foi entendido e a próxima pergunta útil, com atualização documental autorizada e comprovada quando houver escrita.
