# Base preservada — P03, determinações HUM e retificações

Revisão documental de 13/11/2026. Esta projeção preserva as decisões e seus limites no snapshot `0cc6456fbd7613b9a4369d60684d0fe1170a2ed2` do PR #9. O grau de definição é de produto em Discovery. Uma condição funcional aceita não demonstra implementação, pipeline, controle corporativo, autorização operacional ou ratificação. As respostas posteriores do P04 devem ser lidas no registro próprio desta consolidação; o histórico abaixo não é apagado por elas.

## Fontes e regra de leitura

| Fonte | Referência imutável | Natureza e destino neste documento |
|---|---|---|
| BP-S01 | [P03-CONHECIMENTO](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md) | Consolidação temática r1 de manifestações reproduzidas; alimenta P03.1–22, colaterais, DoD, S1/S2/S3 e catálogo. |
| BP-S02 | [CADERNO-ED11](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md) | Reprodução curada das edições de trabalho, não transcrição original autenticada; origem histórica dos aceites de BP-S01 e da evolução registrada adiante. |
| BP-S03 | [REGISTRO D02](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/REGISTRO.md) | Ledger D02-doc-2; alimenta HUM-01–11 e dependências D02-PEN. As naturezas variam por unidade. |
| BP-S04 | [RETIFICAÇÕES D02](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/RETIFICACOES.md) | Precedência explícita de D02-RET-001–006 sobre projeções antigas, preservadas historicamente. |
| BP-S05 | [ESCLARECIMENTOS-ONBOARDING](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md) | Dois casos sintéticos aceitos com condições; alimenta a seção de cenários. Não corresponde a testes executados. |

Cada linha abaixo aponta a fonte por ID e seção/edição; a tabela acima fornece o caminho inverso fonte→destinos. Falta de acesso às mensagens históricas originais é limitação de proveniência, não motivo para transformar aceites suficientemente reproduzidos em propostas. Uma recomendação sem manifestação humana continua proposta.

## P03 — decisões por pergunta e condições de uso

Saldo preservado de BP-S01: vinte perguntas resolvidas funcionalmente (P03.1–19 e P03.21), P03.20/C-P03-07 adiados e P03.22 com direção aceita e desenho concreto postergado. As três questões transversais têm aceite no alcance descrito adiante. Este saldo não elimina engenharia, provas e autorizações futuras.

| ID / estado | Definição preservada, condições e limites | Fonte e dependências |
|---|---|---|
| P03.1 — resolvida funcionalmente | Consolidar todo conhecimento suficientemente válido descoberto. Nas chamadas HTTP consumidas, recuperar URL/verbo, entradas com tipos e exemplos quando possível, saídas, headers, query/path parameters, timeout e status esperados. Explicar tratamento de respostas quando mudar conclusão material; não duplicar implementação sem necessidade. | BP-S01 §1/2; BP-S02 ed.2/4/7/8; C-P03-01/02. |
| P03.2 — resolvida funcionalmente | Finalidade do onboarding é fixa; o engenheiro indica a entrada. Examinar, conforme aplicável, responsabilidades, fluxos, regras, contratos, integrações, APIs, workers, tópicos/filas, banco, configurações, variáveis, bibliotecas/frameworks, infraestrutura e procedimentos documentados de operação/teste. AWS/Terraform são relato do ambiente, sem escolha universal de stack. | BP-S01 §1/3; BP-S02 ed.2/4/7/8; C-P03-03/08 e DoD corrigido. |
| P03.3 — resolvida funcionalmente | Ligar afirmação à revisão e à evidência mais específica permitida: arquivo/seção/classe/método/linha/coluna/cláusula/bloco de infraestrutura. Conservar as duas fontes quando a conclusão depender de ambas. | BP-S01 §1; BP-S02 ed.2; requisito transversal de rastreabilidade. |
| P03.4 — resolvida funcionalmente | Meso indexa responsabilidades dos Micro/submódulos e conduz a dúvida aos repositórios pertinentes, indicando material estudado/revisões/limites. Catálogo da raiz encaminha à Sigla desconhecida. Fronteira funcional de solução, inclusive entre Siglas, cabe ao Analista. | BP-S01 §1/5; BP-S02 ed.2–4/7–10, R6–R8/S3; P08 permanece próprio. |
| P03.5 — resolvida funcionalmente | Não exigir conhecer/provar o total de repositórios da Sigla. Buscar todos que forem encontráveis no acesso permitido e declarar busca/seleção efetiva, obtidos/analisados/falhas. Ausência na seleção não prova inexistência. | BP-S01 §1; BP-S02 ed.2; P03.7/9. |
| P03.6 — resolvida funcionalmente | Relação examinada por um lado registra sentido, contrato/evento observado, origem/revisão, limite e fonte necessária do outro lado. Agente pode sugerir inclusão de repositório na atividade; Engenheiro decide. | BP-S01 §1; BP-S02 ed.2/4; C-P03-01 e cenários A/B/C. |
| P03.7 — resolvida funcionalmente | Entradas: diretório local, repositórios arrastados à pasta, links GitHub ou busca por Sigla. Local conserva branch existente salvo escolha do Engenheiro e distingue alterações autorizadas do commit-base. Link remoto de raiz usa main; link de branch é escolha explícita. | BP-S01 §1; BP-S02 ed.2/4/5; C-P03-04/05; falha→P03.9. |
| P03.8 — resolvida funcionalmente | No ambiente relatado, o nome do repositório identifica obrigatoriamente sua Sigla. Motor identifica pertencimento e organiza a cópia; uso em atividade de outra Sigla não transfere pertencimento. | BP-S01 §1; BP-S02 ed.2/3; natureza contextual do relato. |
| P03.9 — resolvida funcionalmente | Parte material incompleta identifica revisão, conteúdo examinado, material faltante, motivo conhecido, consequência e retomada. Entregar parcela sustentada e delimitar a conclusão dependente. | BP-S01 §1; BP-S02 ed.2; não converter inacessibilidade em inexistência. |
| P03.10 — resolvida funcionalmente | Nova execução ou entendimento validado deve refletir-se no material pertinente da Sigla; Meso enriquece a partir de seus Micro sem apagar revisões conhecidas dos demais nem cobertura da rodada. | BP-S01 §1/4; BP-S02 ed.2/3; S1/S2/HUM-08. |
| P03.11 — resolvida funcionalmente | Na interação posterior, confrontar evidência com a ação concreta: explicitar o que pode afirmar/fazer e a decisão que depende de outra fonte. Não impor esse objetivo particular ao encerramento da produção. | BP-S01 §1/3; BP-S02 ed.2/8; fronteira produtor/interação. |
| P03.12 — resolvida funcionalmente | Comparar objeto, revisão, condições e natureza das fontes diante de divergência. Preservar interpretações/evidências concorrentes e a prova que as distinguiria. Teste documentado não equivale a execução observada. | BP-S01 §1/4; BP-S02 ed.2/8/9; S1/S3. |
| P03.13 — resolvida funcionalmente | Falta de suporte imprescindível à fidelidade ou delimitação da cobertura impede a conclusão dependente. Se criticidade continuar incerta após investigação autorizada, escalar ao Engenheiro. Parte independente pode ser entregue; uso posterior avalia impacto da ação concreta. | BP-S01 §1/3; BP-S02 ed.2/7/8; BP-S05. |
| P03.14 — resolvida funcionalmente, com premissa relatada | Release branch mais recente representa HOM segundo o processo relatado pelo usuário. Registrar commit examinado; interpretar evidência autorizada fornecida sobre implantação/configuração com componente/revisão/ambiente. Ocorrência específica requer sua própria evidência. | BP-S01 §1; BP-S02 ed.2–5; C-P03-06; C-P04-08 posterior complementa o relato, sem comprovar pipeline. |
| P03.15 — resolvida funcionalmente | Intervenção leva menor pergunta útil, hipóteses compatíveis, referências, tentativas autorizadas e decisão afetada. Separar dúvida factual da revisão e escolha futura de produto. | BP-S01 §1; BP-S02 ed.2; HUM-02/03. |
| P03.16 — resolvida funcionalmente | Catalogar/comunicar lacuna ou incoerência tão logo percebida, com informação sustentada, limitação e próxima ação. Avisar se continua sozinho ou precisa de decisão humana agora. | BP-S01 §1; BP-S02 ed.2/3; BP-S05. |
| P03.17 — resolvida funcionalmente | Reapresentar ressalva em usos direta ou indiretamente dependentes, inclusive fora do Workspace; explicar relação e consequência concreta. Relação hipotética continua identificada com evidência faltante. | BP-S01 §1; BP-S02 ed.2; BP-S05. |
| P03.18 — resolvida funcionalmente | Primeira entrega prioriza Motor sem interface gráfica própria construída pela equipe. Agente explica afirmação afetada, fonte, limitação e próxima ação; detalhe deve ser recuperável por assunto. | BP-S01 §1; BP-S02 ed.2; não escolhe layout final. |
| P03.19 — resolvida funcionalmente | Interação investiga até resposta suficientemente fundamentada pela natureza, escopo, critérios e implicações do pedido; reporta inconclusões e oferece aprofundamento conforme Engenheiro. Produção encerra pelo DoD próprio. | BP-S01 §1/3; BP-S02 ed.2/8. |
| P03.20 — adiada | Métodos/testes/resultados esperados/responsáveis/provas de segurança, precisão e confiabilidade das bases aguardam refinamento. Não atribuir taxa de qualidade ou benchmark. | BP-S01 §1/6; BP-S02 ed.2/7/8; C-P03-07/R10. |
| P03.21 — resolvida funcionalmente, execução futura condicionada | Solicitação excepcional de executar aplicação local só após dúvida intransponível e tentativas autorizadas esgotadas; oferecer resposta direta do Engenheiro, explicitar dúvida/tentativas/finalidade/ambiente/dados/pré-requisitos/comandos/efeitos e obter permissão por ocorrência. Esta missão não executa aplicações. | BP-S01 §1; BP-S02 ed.2/3; HUM-03 e RET-001. A segunda resposta rotulada P03.2 foi vinculada editorialmente a P03.21 por posição/assunto, sem alterar o original. |
| P03.22 — direção aceita, desenho postergado | Documentos/referências devem favorecer navegação, leitura, compreensão, explicação e modificação autorizada por qualquer agente, buscando profundidade/qualidade/rapidez/precisão e menor ACU/tokens/contexto/recursos. Formato físico, granularidade, índices e instruções concretas não escolhidos. | BP-S01 §1/6; BP-S02 ed.2/4/5/7/8; R5; P02/D02-PEN-005. |

## Política de produção e DoD retificado

Fonte BP-S01 §2–3, BP-S02 [edição 8](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#saldo-p03-r8). O produtor registra conhecimento suficientemente válido encontrado na revisão estudada e conserva uma origem principal de edição por fato. Regra, condição, efeitos e exceções precisam de explicação quando omiti-los mudar conclusão, contrato, ação ou segurança. Pode referenciar uma fonte canônica autorizada, legível, exata e vinculada à revisão quando ela contiver a resposta inteira. Implementação interna sem efeito material diferente pode permanecer no código, desde que localizável. Lacunas materiais, contradições, origem inacessível e fronteiras desconhecidas permanecem explícitas.

Exemplo de condição material: se omitir campo nulo altera a mensagem emitida, o efeito deve constar da explicação; o serializador pode continuar em sua fonte. Descoberta posterior retroalimenta a base somente no alcance validado, com origem/revisão/evidência/natureza. Aprovar uma resposta não aprova conteúdo não abrangido; hipótese não vira fato e regra a criar permanece decisão futura.

| ID de projeção | Critério aceito do produtor | Demonstração exigida pelo comportamento futuro |
|---|---|---|
| P03-DOD-01 | Identificar entrada | Repositório, revisão ou estado local/diferenças, fontes acessíveis, alcance e limites. |
| P03-DOD-02 | Cobertura de descoberta | Confrontar fontes pertinentes ao tipo de repositório; dar destino a indícios materiais, fora do recorte e inacessibilidades. |
| P03-DOD-03 | Comportamentos materiais | Entradas, condições, decisões, alternativas, exceções, efeitos e ausência de ação; delimitar lado estudado na integração. |
| P03-DOD-04 | Consolidar conhecimento válido | Recuperar por explicação ou referência suficiente; registrar incerteza ao percebê-la, sem adiar fato já sustentado. |
| P03-DOD-05 | Rastreabilidade e coerência | Comportamento→explicação/referência/ressalva e afirmação→evidência na revisão; conferir omissões materiais, contradições e links. |
| P03-DOD-06 | Tratar lacunas | Determinar efeito sobre fidelidade/cobertura, avisar cedo, preservar parcela independente e escalar criticidade ainda incerta após investigação autorizada. |
| P03-DOD-07 | Entregar resultado | Artefatos Micro/Meso pertinentes com revisões, evidências, cobertura, ressalvas e estado efetivo de entrega/publicação. |

Os IDs P03-DOD são projeções editoriais desta consolidação, sem nova decisão. Estados aceitos: **concluído no recorte**, quando aplicáveis demonstrados; **concluído com ressalvas**, com pendências delimitadas/controladas e base fiel; **parcial ou impedido na parte dependente**, por suporte indispensável ausente; **aguardando esclarecimento**, por criticidade ainda incerta. Aviso acompanha descoberta, não espera fim da execução.

A edição 8 retirou do DoD do onboarding o objetivo particular fornecido pelo Engenheiro e o sucesso de consulta por outro agente. O produtor verifica integridade da referência; o consumidor/interação navega e aplica evidência ao pedido posterior. A redação anterior fica histórica. Critérios acima não representam resultados de testes desta missão.

## Cenários aceitos e seus limites

Fonte BP-S05, relacionada a P03.6/9/13/16/17 e D02-PEN-001/002. São exemplos sintéticos, não aplicações reais nem autorização de mudança.

| ID editorial | Evidência e aceite | Limitação preservada e ação posterior |
|---|---|---|
| P03-CEN-A | A emite codigoSegmento para B e C; há evidência de A e do tratamento em B, e relação com C visível pelo lado de A. A pode concluir onboarding com ressalva. | Falta comprovar se C aceita ausência. Todas as dúvidas percebidas ficam definidas/localizadas/detalhadas/referenciadas em A. Retirar campo exige investigar evidência pertinente de C; B não prova C. |
| P03-CEN-B | A contém regra de segmento pelo cadastro e outra pela proposta. Ambas podem ser registradas com referências. A pode concluir com ressalva. | Seleção/precedência continua incerta; nomes não a comprovam. Alterar regra depende de evidência própria. Condição documental do aceite permanece. |

Comunicar a lacuna o mais brevemente possível, mesmo antes de conhecer todos os usos afetados. Ao descobrir dependência de história, sinalizar no Workspace; na consulta ou atividade direta/indiretamente dependente, inclusive fora dele, reapresentar consequência concreta. Retirar codigoSegmento exemplifica dependência direta; mudar tarifa que varia por segmento exemplifica indireta. O aceite não se estende automaticamente a outros casos. D01-DEC-002 permite ressalvas não críticas; D01-DEC-003 exige critérios rigorosos/objetivos/verificáveis para criticidade e escalonamento se incerta.

## Escrita, incorporação e conflito

Fonte BP-S01 §4–5; BP-S02 ed.7–10 e [fechamento P03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#fechamento-p03). Estes aceites têm objetos diferentes.

| ID | Regra aceita e fronteira |
|---|---|
| S1 | Correção autônoma quando evidência demonstra inconsistência **e determina a correção**. Corrigir em destino autorizado, verificar e preservar rastreabilidade sem nova permissão pontual. Divergência sem solução determinada exige preservar fontes e esclarecer quando necessário. Inclui correção documental pré-push. |
| S2 | Novo entendimento: pedir ao Analista da atividade autorização de escrita com entendimento, origem, destino e efeito no mesmo pedido. Uma confirmação abrangente basta. Pode abranger outra Sigla se a escrita for efetivamente permitida. Silêncio gera pendência; negativa descarta incorporação no destino negado. Originais e lacuna factual independente mantêm tratamento próprio. |
| S3 | Conflito: preservar ambas as declarações com origem/revisão na camada/ponto afetados, explicitar divergência e informar atividades direta/indiretamente dependentes. Reconciliação registra fundamento e alcance; conflito sem fundamento de arbitragem continua explícito. |
| P03-PUSH | Atualizar/revalidar todo conhecimento cujo significado mudou **antes de cada push**. Produto exige garantia determinística vinculada ao conteúdo exato candidato; mudança posterior invalida prova. Verificar impacto sobre referências; ausência de impacto pode ser revalidada com evidência registrada. Mecanismo, cobertura de clientes e fiscalização corporativa ainda precisam ser demonstrados. |
| P03-COMP | Produzir, verificar, enviar contribuição e adotar referência compartilhada são estados diferentes. Composição explicita commits/ponteiros/dependências. Drift detectado invalida uso como atual; reconciliar e verificar antes de restaurar validade. Sem monitor demonstrado, detectar na próxima leitura/ciclo. |

O catálogo da raiz integra a primeira entrega: para cada Sigla, responsabilidade, escopo e domínio. Qualquer pessoa pode originar declaração; atribuição inicialmente incontestada orienta imediatamente **como declarada**, com origem/revisão. Corroboração requer suporte. Catálogo é legível no contexto da Plataforma independentemente da Sigla, sem criar acesso ao destino privado. Meso encaminha aos Micro e raiz à Sigla; delimitar solução continua com o Analista. Mudança pertinente no Meso reflete-se na raiz, invalidando entrada afetada até reconciliação/verificação. Identidade física raiz de instalação/Macro, propagação, concorrência e controles continuam para refinamento.

S2 é autorização específica de incorporação, distinta do consentimento genérico para leitura interna ordinária posteriormente descartado no P04. Regras de consulta posterior ao legado e busca externa do snapshot permanecem históricas e devem ser interpretadas com a retificação posterior do P04 no seu alcance exato, sem ampliar acesso, executar, excluir, publicar normativamente ou reintroduzir consentimento repetitivo para leitura acessível.

## Oito colaterais de P03

Todas têm fonte BP-S01 §6 e edições indicadas de BP-S02; cada uma aponta de volta ao P03 afetado, e as linhas P03 acima as referenciam em sentido inverso.

| ID / estado | Conteúdo e condição | Origem / destinos |
|---|---|---|
| C-P03-01 — aceita | Explicar condições, caminhos e efeitos materiais da resposta de integração dentro de A, inclusive encerrar sem publicar; receptor seguinte conserva limite de evidência de P03.6. | Ed.3–4 → P03.1/6. |
| C-P03-02 — aceita | Uma origem principal por fato, referências nos demais pontos e atualização de todo significado afetado. | Ed.4 → P03.1/12/22; P03-PUSH. |
| C-P03-03 — direção aceita | Cobrir aspectos/unidades tanto quanto possível e declarar limites. DoD ed.8 é da produção e dispensa pergunta particular de uso. | Ed.4/8 → P03.2/DOD. |
| C-P03-04 — aceita | Pasta indicada é cópia de trabalho examinada, com alterações autorizadas e novos arquivos pertinentes distinguidos do commit-base. Pré-push tem regra própria. | Ed.4–5/7–9 → P03.7/PUSH. |
| C-P03-05 — aceita | Link explícito de branch a escolhe; link de raiz usa main. Inacessibilidade vira cobertura parcial. | Ed.4–5 → P03.7/9. |
| C-P03-06 — aceita | Parâmetro, padrão de código, ponto de substituição e valor efetivo quando evidenciado ou seu desconhecimento. Forma física continua postergada. | Ed.5 → P03.14/22. |
| C-P03-07 — adiada | Comparar representações por precisão, tempo, recursos e custo por tarefa/modalidade. Sem benchmark ou limiar aceito. | Ed.4–8/fechamento ed.10 → P03.20. |
| C-P03-08 — aceita no aplicável | Mensageria: contrato, origem/destino conhecidos, efeitos de sucesso/duplicidade/falha demonstrados. Banco: operação, dados lidos/alterados, efeitos relevantes inclusive vazio/erro. Não inventar caminhos não evidenciados. | Ed.4 → P03.1/2. |

## HUM-01–11 — natureza, direção e ressalvas

Fonte BP-S03 por âncora hum-NN. Todas têm validade no Discovery e maturidade EM DISCOVERY; nenhuma concede acesso operacional. D02-S01 é dossiê PM R5 §4, reprodução curada de declarações da missão R4, sem autenticação independente das mensagens históricas. A fonte direta consultada aqui é o ledger, não as mensagens originais.

| ID / natureza no ledger | Conteúdo preservado e condição | Destinos/impactos |
|---|---|---|
| HUM-01 — intenção/direção reproduzida | Compreensão ampla e profunda viável de técnica, procedimentos documentados, testes, negócio, arquitetura e relações; evidências exatas, contraevidências, escopo lido/não lido, exclusões e limites. Integralidade é intenção, não perfeição nem execução autorizada. | P03.1–3/5/9/12; DOD; D02-PEN-001. |
| HUM-02 — direção reproduzida | Investigar autonomamente fontes autorizadas antes de escalar. Intervenção por impedimento material, autoridade ou escolha ambígua. Não ampliar acesso nem substituir evidência por confiança. | P03.13/15/19; S1/S3. |
| HUM-03 — decisão/restrição reproduzida | Exceção futura de execução local por ocorrência após dúvida intransponível, alternativas e tentativas autorizadas; resposta direta é alternativa. Conhecer comandos não autoriza usá-los. Missão documental proíbe aplicações. | P03.21; RET-001; D02-PEN-004. |
| HUM-04 — decisão/restrição reproduzida | Nenhuma refatoração, renomeação, reorganização ou modernização no onboarding. Agent-Centric orienta mudanças posteriores autorizadas no necessário, sem reestruturação oportunista. | P03.2/7; RET-003. |
| HUM-05 — escolha topológica reproduzida | Git canônico; Micro individual, Meso repo por Sigla/conta com Micro submodules, Macro workspace Git com Meso submodules. Sem sync/acesso/redistribuição implícitos. Relação organizacional fina e mecanismos continuam abertos. | P03.4/10; RET-002; D02-PEN-003. |
| HUM-06 — síntese editorial D01-R2 | Distingue leitura inicial, retorno ao legado, exterior, execução, escrita/publicação, retenção/derivação, redistribuição e exclusão. Provisório Agent-First não comprova definitivo. Fontes indiretas permitidas sem inventar implementação. Direitos efetivos não são criados por autorização. Identidade/validade/schema/fiscalização são propostas; P04 posterior refina consentimentos internos e expiração. | S2/P03.21; P04; D02-PEN-004. |
| HUM-07 — direções reproduzidas; semântica candidata | Agent-Centric, Agent-Oriented, AI-Intent, SDD, Harness Engineering, Contexto Mínimo Necessário, Roteamento de Contexto, Contexto-Ótimo, AI-Based Architecture e agnosticidade de modelo/agente/ferramenta. Definições AX-01–10 têm dono no documento de axiomas; rótulo não aprova stack nem prova eficácia. | P03.22; P02/P07; D02-PEN-005. |
| HUM-08 — direção/restrição reproduzida | Código/contrato/conhecimento/validação no mesmo ciclo commit/PR antes de fechar. Composição multirrepositório verificável com commits/ponteiros, sem atomicidade física prometida. Drift: detectar→invalidar→reconciliar→verificar; detectar não corrige e reconciliar sem verificar não restaura. | P03-PUSH/COMP; RET-004; P04.1–5/11. |
| HUM-09 — síntese editorial D01-R2 | Colaboração entre autorizados preserva autonomia, concorrência, revisão-base, publicação controlada e rastreabilidade. Push de trabalho não publica aprovado. Esclarecimentos retroalimentam camadas com autorização/validação. Pendências disponíveis por relevância sem carregar tudo ou supor segundo plano. | S1/S2/S3; P03.10/16/17; P04/P05/P06. |
| HUM-10 — proposta editorial | AGENTES.MD e PENDENCIAS.MD são nomes futuros candidatos, distintos do AGENTS.md operacional. Contratos e reconhecimento por ferramentas pendentes; não substituir/renomear nem criar colisões de caixa. | P03.22; D02-PEN-005. |
| HUM-11 — síntese editorial de limites | Produto/UX/regras/permissões/estados/exceções/segurança/evidências/operação devem ser refinados. Ressalvas não críticas podem coexistir com conclusão; criticidade incerta escala. Layout/stack/taxonomia/limiares são candidatos; relatos de banco não são política universal nem implantação comprovada. | P03.13/18/20; P04–P09; limites desta consolidação. |

HUM-06/09 não são mensagens diretas integrais; HUM-10 não é decisão humana; HUM-11 não é autorização de construir. Preservar esse atributo evita atribuir aprovação retroativa às sínteses. Os sete D02-PROP-001–007 continuam propostas de fluxo, unidades/evidência, roteamento, controles, consistência, UX e contratos/nomeação; mecanismos concretos seguem nos documentos originais e em D02-PEN-001–006.

## Retificações, histórico e precedência

Fonte BP-S04. Documentos e recibos D01/R1/R2/PM-R5 conservam seus próprios snapshots; esta projeção não recertifica suas evidências. Ausência da transcrição integral D01-PEN-001/B continua limite histórico, sem reabrir a reconciliação material A.

| ID | Antes → vigente, motivo/fonte registrada | Impactos e regressão a evitar |
|---|---|---|
| D02-RET-001 | D01-RST-001 reservava execução exclusivamente ao Engenheiro; HUM-03 abre futura solicitação excepcional específica depois das tentativas autorizadas, com alternativa de resposta direta e efeitos explicitados. | Não excluir exceção futura com frase antiga; não usar exceção para executar na missão documental. |
| D02-RET-002 | Síntese Meso genérica D01-REL-003 subordinada a HUM-05 e D01-REL-004/DEC-006: repo específico por Sigla/conta e submodules Micro/Meso nos níveis pertinentes. | Não rebaixar topologia a hipótese nem inferir sync/acesso/redistribuição. |
| D02-RET-003 | Preparação Agent-First antiga detalhada por HUM-04/AX-01: absolutamente nenhuma refatoração no onboarding; orientação para mudanças posteriores autorizadas no escopo. | Toque documental não autoriza reorganizar aplicação. |
| D02-RET-004 | Atualização contínua antiga detalhada por HUM-08: mesmo ciclo commit/PR; composição explícita; detectar→invalidar→reconciliar→verificar. | Não tratar detecção como correção, reconciliação como prova ou postergar atualização dependente silenciosamente. P03-PUSH acrescenta o requisito funcional anterior a cada push. |
| D02-RET-005 | Manifesto CONT-REG-0001 e hashes antigos preservados em histórico; ponte ativa CONT-REG-0002 registra ordem humana da missão, sem aprovação de produto nem efeito normativo. | Verificar identidade das entradas correntes sem alterar hashes históricos; novo registro não é aceite C1, implementação, ratificação ou pipeline. |
| D02-RET-006 | Determinação direta de 01/11/2026 redefine prontidão: ler documentação vigente e recuperar decisões/restrições/pendências/retomada. Gates RG/PM-R5 não bloqueiam entrevista. | Só impedimento atual material demonstrado bloqueia etapa dependente; não exigir INTEGRALMENTE_COMPROVADO para conversar nem dar aceite técnico retroativo a ensaios. |

| Marco histórico BP-S02 | Evolução preservada → destino atual |
|---|---|
| Ed.1–2 | Agenda de 77 perguntas e primeira rodada P03 → tabela P03 e catálogo de pendências. |
| Ed.3–5 | Sigla pelo nome, enriquecimento Meso, comunicação, execução excepcional, fronteira Micro, HOM e estado local → P03.6–10/14/16/21 e colaterais. |
| Ed.6–7 | Saldo, P03.13, catálogo da raiz, pré-push e DoD então candidato → seções DOD, catálogo, P03-PUSH. Exemplar de navegação permanece ilustrativo. |
| Ed.8 | Retificação material produtor/interação; encerra P03.1/2 funcionalmente → DoD vigente. |
| Ed.9–10 | Correção inequívoca, pedido único, silêncio/negativa, conflito e autoridade entre Siglas → S1/S2/S3. |
| Ed.11 | Abertura do P04; P04.6 herda S2 central → registro posterior do P04, preservando abertura como histórica. |

## Dependências e critérios editoriais de manutenção

PE-01/P01 detalha públicos, destinos e distribuição; PE-02/P02 recebe portabilidade/modalidades; PE-03 e PE-04/P04 recebem evidência, validade e composição; PE-05/P05 e PE-06/P06 consomem a base em atividades/retomadas; PE-07/P07 aplica origem e direitos a extensões; PE-08/P08 conserva escolha da materialização arquitetural; PE-09/P09 conserva fontes e autoridade de negócio. Catálogo/Meso não encerram esses grupos por analogia.

Como regra editorial desta consolidação, mudança futura deve identificar ID afetado, fonte/revisão/natureza, antes/depois, alcance, consumidores e prova pertinente; manter histórico substituído e atualizar ligações. Essa regra de manutenção não é um mecanismo técnico aprovado da IDE. Antes de alegar nova capacidade, buscar evidência específica; aprovação documental, execução de teste, implantação e autorização corporativa permanecem estados separados.
