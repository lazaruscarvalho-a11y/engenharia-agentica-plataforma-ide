# Rota vigente R04 — 2026-11-13

Esta entrada remete à [consolidação da sessão P01–P09 R04](../consolidacao-r04/CONTINUIDADE.md), na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o recibo `auditorias/consolidacao-sessao-r04/RECIBO-PUBLICACAO.json` e leia pelo content_commit imutável. [Registro de definições](../consolidacao-r04/REGISTRO-DECISOES.md) · [saldo e adiamentos](../consolidacao-r04/SALDO-P01-P09.md).

O levantamento dos grupos está encerrado no alcance documentado; mecanismos/esquemas/avaliações/integrações concretos permanecem postergados. R04 prevalece sobre estados intermediários abaixo, preservando aceites P03/P04, natureza das fontes e limites normativos. Vocabulário de trabalho: branch, homologação e produção; versão/commit/verificação/validação quando necessário. Não inferir implementação nem atualização nativa do Projeto.

O conteúdo anterior abaixo é histórico, preservado literalmente. Seus hashes, propostas e pontos de retomada valem para seus snapshots. As demais restrições pertinentes continuam aplicáveis.

---

# Rota vigente R03 — 13/11/2026

Leia a [consolidação P03/P04 R03](../consolidacao-r03/BASE-P03-HUM.md) na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o manifesto R03 e o recibo posterior por commit imutável. P03 conserva seus aceites e adiamentos; P04 está funcionalmente encerrado no alcance qualificado pela fonte recuperada, com proveniência indireta dos aceites iniciais. P01–P09 têm catálogo granular e prompt de continuidade. A R03 distingue decisão, proposta, relato corporativo e comprovação; sem código de produto, merge, ratificação ou mudança de permissões.

O conteúdo abaixo é o snapshot anterior, preservado literalmente. Pontos de retomada, estados de entrevista e hashes anteriores valem para a revisão ali identificada; ler a sobreposição R03 para o saldo atual. Os manifestos D02-doc-2/R01/R02 permanecem históricos, sem certificar os novos bytes desta navegação.

---

# P03 — Conhecimento e suficiência

**Revisão temática 1 · Decisões de produto em Discovery · Primeira entrega, PE-03 e PE-04.**

O Motor de Onboarding produz uma base de conhecimento sobre o repositório e o estado efetivamente estudados. Sua unidade de entrega é o conhecimento sustentado pelas fontes autorizadas, com revisão, evidência e limites. O componente de interação atende a uma pergunta ou atividade posterior e decide que conhecimento recuperar para aquele pedido.

**Saldo de P03.** Das 22 perguntas originais, 20 estão resolvidas no alcance funcional (P03.1 a P03.19 e P03.21). P03.22 tem direção aceita e desenho concreto postergado. P03.20 e sua colateral C-P03-07 aguardam o refinamento de qualidade e custo. As questões transversais S1, S2 e S3 foram encerradas no alcance descrito abaixo. A continuidade da entrevista é o grupo [P04 — Atualidade, autoridade e compartilhamento](P04-ATUALIDADE.md).

Este registro consolida as manifestações do usuário reproduzidas no caderno, preservando o objeto de cada aceite. Os IDs decimais são índices editoriais do Discovery. O grau de definição aqui registrado é funcional. Implementação da IDE, validação operacional, formatos, limiares e autorizações sobre serviços reais têm marcos e evidências próprios. [Entrada da entrega](../README.md) · [Escopo e agenda](../ESCOPO.md#pendencias) · [Fonte integral e fechamento do P03](historico/CADERNO-ED11.md#fechamento-p03).

## 1. Decisões por pergunta

Os números de edição nas tabelas remetem às rodadas preservadas no [histórico integral](historico/CADERNO-ED11.md). Os detalhes compartilhados por mais de um item têm sua definição principal nas seções 2 a 5 deste registro.

| ID | Resultado funcional vigente | Origem |
|---|---|---|
| P03.1 | Consolidar no onboarding todo conhecimento suficientemente válido identificado. Para uma chamada HTTP consumida, permitir recuperar URL, verbo, campos de entrada com tipos e exemplos quando possível, campos de saída, headers, parâmetros de consulta, variáveis de caminho, configurações de timeout e status esperados. Explicar o tratamento dado pelo próprio repositório às respostas quando ele muda uma conclusão material. A política de explicação, referência e enriquecimento está na seção 2. | Ed. 2, 4, 7 e 8; C-P03-01/02, R1/R2. |
| P03.2 | A finalidade do onboarding é fixa. O Engenheiro indica o que importar. O Motor examina, conforme aplicável, responsabilidades, fluxos, regras, contratos de entrada e saída, integrações, APIs, workers, tópicos, filas, bancos, configurações, variáveis, bibliotecas, frameworks, recursos de infraestrutura e procedimentos documentados de operação e teste. O uso frequente de AWS e Terraform foi relatado pelo usuário para seu ambiente. O DoD corrigido está na seção 3. | Ed. 2, 4, 7 e 8; C-P03-03/08, R4. |
| P03.3 | Relacionar cada afirmação à revisão e à evidência tão específica quanto o material permitir, do geral ao particular. Uma referência pode chegar a arquivo, seção, classe, método, linha, coluna, cláusula contratual ou bloco de infraestrutura. Quando a explicação requer duas fontes, manter ambas. | Ed. 2. |
| P03.4 | O Meso reúne os repositórios da Sigla como submódulos e indexa suas responsabilidades para conduzir uma dúvida até os Micro pertinentes. O índice identifica o material estudado, suas revisões e os limites conhecidos. O catálogo da raiz encaminha o assunto à Sigla quando ela for inicialmente desconhecida. A delimitação funcional de uma solução, inclusive entre Siglas, compete ao Analista. | Ed. 2–4, 7–10; R6–R8, S3. |
| P03.5 | O usuário dispensou conhecer ou provar o total de repositórios da Sigla. Uma busca pode abranger todos os repositórios que o agente consiga encontrar dentro do acesso permitido. O resultado identifica a seleção ou busca efetiva, o que foi obtido e analisado e as falhas conhecidas. | Ed. 2; P03.7 e P03.9. |
| P03.6 | Na relação examinada por um lado, registrar sentido, contrato ou evento observado, origem e revisão, limite da conclusão e o que teria de ser consultado no outro lado. O agente pode sugerir a inclusão de um repositório pertinente na atividade; a decisão cabe ao Engenheiro. | Ed. 2 e 4; C-P03-01. |
| P03.7 | Quatro entradas: indicação de repositórios em diretório local, repositórios arrastados para a pasta da Plataforma, links GitHub ou busca por Sigla no GitHub. A pasta local usa a branch em que está, salvo indicação do Engenheiro, e retrata a cópia de trabalho autorizada com alterações locais distinguidas do commit-base. O link remoto para a raiz usa `main`; um link de branch específica é escolha explícita. Falha de obtenção segue P03.9. | Ed. 2, 4 e 5; C-P03-04/05. |
| P03.8 | Segundo o usuário, o nome do repositório identifica obrigatoriamente sua Sigla no ambiente descrito. O Motor identifica esse pertencimento e organiza a cópia na pasta correspondente. A participação em atividade de outra Sigla preserva o pertencimento original. | Ed. 2 e 3. |
| P03.9 | Para cada parte material incompleta, indicar revisão, conteúdo examinado, material faltante, motivo conhecido, consequência e ponto de retomada. Entregar a parte sustentada. Delimitar a conclusão que depende da fonte ausente. | Ed. 2. |
| P03.10 | Uma nova execução ou um novo entendimento validado sobre um repositório deve refletir-se no material pertinente de sua Sigla. O Meso se enriquece conforme os seus Micro. Preservar a revisão conhecida dos demais repositórios e a cobertura da rodada. | Ed. 2 e 3; S1. |
| P03.11 | Na interação posterior, confrontar a evidência com a ação concreta pretendida. O agente explica o que pode afirmar ou fazer com segurança e quais decisões ainda dependem de outra fonte. | Ed. 2; distinção produtor/consumidor da ed. 8. |
| P03.12 | Diante de divergência, confrontar objeto, revisão, condições e natureza das fontes. Preservar evidências e interpretações concorrentes e identificar a evidência necessária para distingui-las. Teste documentado e execução observada sustentam afirmações diferentes. | Ed. 2, 8 e 9; S1/S3. |
| P03.13 | Durante a produção, a falta de suporte imprescindível à fidelidade da base ou à delimitação de sua cobertura impede a conclusão dependente. Se a criticidade continuar incerta após investigação autorizada, levar a dúvida ao Engenheiro. Na interação, avaliar o impacto sobre a pergunta ou ação quando ela existir. O agente pode entregar o trabalho independente. | Ed. 2 e 7, com a correção da ed. 8; [casos aceitos de A](../evidencias/ESCLARECIMENTOS-ONBOARDING.md). |
| P03.14 | Regra de pipeline **relatada pelo usuário** para os repositórios em questão: a release branch mais recente representa o código de HOM. Registrar o commit efetivamente examinado. A primeira entrega pode interpretar evidência autorizada de implantação ou configuração fornecida pelo Engenheiro, delimitando componente, revisão e ambiente. Atribuir uma ocorrência a uma requisição precisa de evidência daquela ocorrência. | Ed. 2–5; C-P03-06. |
| P03.15 | Quando necessária intervenção, levar a menor pergunta útil, as hipóteses ainda compatíveis, as referências, as tentativas autorizadas e a decisão afetada. Diferenciar dúvida factual sobre a revisão de escolha de produto futura. | Ed. 2. |
| P03.16 | Catalogar e comunicar cada lacuna ou incoerência tão logo percebida, com a informação sustentada, a limitação e a próxima ação. O aviso explicita se o agente pode continuar sozinho ou se uma decisão humana é necessária naquele momento. | Ed. 2 e 3. |
| P03.17 | Reapresentar uma ressalva nas perguntas e atividades em que houver dependência direta ou indireta, inclusive fora do Workspace. Mostrar a relação concreta e a consequência para o pedido atual. Se a ligação ainda for hipótese, explicitar o que falta para confirmá-la. | Ed. 2. |
| P03.18 | A primeira entrega prioriza o Motor sem interface gráfica própria construída pela equipe. O agente apresenta em linguagem direta a afirmação afetada, a fonte, a limitação e a próxima ação. A informação de detalhe deve ser acessível por assunto. | Ed. 2. |
| P03.19 | Ao atender a um pedido, investigar até haver resposta suficientemente fundamentada conforme sua natureza, escopo, critérios e implicações. Reportar dúvidas e inconclusões e oferecer aprofundamento conforme a resposta do Engenheiro. Para encerrar o onboarding, usar o DoD do produtor da seção 3. | Ed. 2 e 8. |
| P03.20 | **Avaliação adiada.** O usuário reservou a definição de testes, métodos, resultados esperados, responsáveis e provas de segurança, precisão e confiabilidade das bases. | Ed. 2, 7 e 8; C-P03-07/R10. |
| P03.21 | A primeira entrega oferecerá o fluxo de solicitação excepcional de execução local da aplicação estudada nas condições de HUM-03. Após esgotar investigações autorizadas diante de uma dúvida intransponível, oferecer esclarecimento direto pelo Engenheiro. Para propor execução, indicar dúvida, tentativas, finalidade, ambiente, dados, pré-requisitos, comandos e efeitos e obter permissão específica por ocorrência. | Ed. 2 e 3; [HUM-03](../../REGISTRO.md#hum-03). A segunda resposta rotulada “P03.2” na primeira rodada foi vinculada a P03.21 pelo assunto e pela posição. |
| P03.22 | O conjunto de documentos e referências deve favorecer navegação, leitura, compreensão, explicação e modificação autorizada por qualquer agente, com profundidade, qualidade, rapidez e precisão, buscando menor consumo de ACUs, tokens, contexto e recursos. A direção funcional foi aceita; a estrutura física, a granularidade, os formatos, os índices e as instruções concretas ficam **postergados**. | Ed. 2, 4, 5, 7 e 8; R5. |

## 2. Fronteira e manutenção do conhecimento Micro

O produtor consolida todo entendimento suficientemente válido descoberto na revisão estudada. A origem principal de edição de um fato deve permitir que o restante da base o referencie sem duplicações independentes.

1. **Explicar.** Registrar condição, regra, efeitos e exceções quando sua omissão puder mudar a explicação, o contrato, uma ação ou a segurança de uma mudança. Explicar efeitos materiais descobertos pela combinação de fontes.
2. **Referenciar.** Quando uma fonte canônica, autorizada, legível, exata e ligada à revisão já contiver a resposta inteira, o Micro pode encaminhar ao trecho suficiente. Se a omissão de um campo nulo mudar a mensagem emitida, explicitar esse comportamento mesmo que a implementação do serializador permaneça no código.
3. **Preservar a implementação em sua fonte.** Escolhas internas que mantenham os mesmos efeitos, contratos e limites materiais podem ficar no código. A regra ou o componente correspondente continua localizável pelo Micro.
4. **Qualificar a lacuna.** Registrar e comunicar insuficiência material, contradição, origem inacessível, impacto ou fronteira desconhecidos. Separar ausência de evidência na seleção de prova de inexistência.

Descobertas posteriores, aprofundamentos e lacunas esclarecidas retroalimentam a base no escopo legitimamente validado. Preservar origem, revisão, evidência e natureza de cada afirmação. A aprovação de uma resposta pelo Analista alcança somente o conteúdo aprovado. Uma hipótese permanece identificada e uma regra a ser criada é uma decisão para o futuro. A seção 4 distingue correção, incorporação e reconciliação. [Política aceita e DoD corrigido](historico/CADERNO-ED11.md#saldo-p03-r8) · [Registros HUM-06 e HUM-08/09](../../REGISTRO.md#hum-06).

## 3. Definition of Done do Motor

**Condição de conclusão.** Para o repositório e o estado examinados, o Motor produziu a base segundo os padrões definidos e pode demonstrar a cobertura, a proveniência e a integridade de seus resultados, com os limites da produção claramente registrados.

| Critério aceito | O que a produção precisa demonstrar |
|---|---|
| **1. Identificar a entrada** | Repositório, revisão ou estado local com suas diferenças em relação ao commit-base, fontes acessíveis, alcance e limites de autorização. |
| **2. Demonstrar a cobertura de descoberta** | Confrontar as fontes pertinentes ao tipo de repositório para encontrar responsabilidades, fluxos e indícios independentes. Dar destino aos indícios materiais, às áreas fora do recorte e às fontes inacessíveis. |
| **3. Compreender os comportamentos materiais** | Registrar entradas, condições, decisões, alternativas, exceções, efeitos e ausência de ação, delimitando o lado estudado nas integrações. |
| **4. Consolidar o conhecimento válido** | Tornar recuperável o que a revisão sustenta por explicação ou referência suficiente. Registrar as incertezas ao identificá-las, sem adiar silenciosamente um fato relevante já sustentado. |
| **5. Conferir rastreabilidade e coerência** | Do comportamento encontrado, alcançar a explicação, referência ou ressalva; da afirmação, voltar à evidência correspondente à revisão. Conferir condições omitidas, contradições e referências quebradas. |
| **6. Tratar lacunas** | Determinar o efeito sobre a fidelidade da produção e sua cobertura, comunicar assim que percebido, preservar a parte independente e recorrer ao Engenheiro quando a criticidade persistir após investigação autorizada. |
| **7. Entregar o resultado** | Produzir os artefatos Micro/Meso pertinentes conforme o contrato de saída e identificar revisões, referências, cobertura, ressalvas e estado efetivo de entrega ou publicação. |

**Estados aceitos.** *Concluído no recorte* quando os critérios aplicáveis estiverem demonstrados; *concluído com ressalvas* quando as pendências estiverem delimitadas e controladas e a base permanecer fiel; *parcial ou impedido na parte dependente* quando faltar suporte indispensável à produção ou à delimitação de sua cobertura; *aguardando esclarecimento* quando a criticidade da produção continuar incerta. O primeiro aviso acompanha a descoberta, sem esperar o encerramento da execução.

O componente de **interação** interpreta o pedido posterior e aplica as skills, instruções e procedimentos para navegar, consultar fontes autorizadas, responder e propor enriquecimentos. A verificação de integridade de uma referência pertence ao produtor. O êxito de uma consulta de outro agente e o fornecimento de um objetivo particular pelo Engenheiro foram retirados das condições de fechamento do onboarding na edição 8.

**Aceites delimitados.** A pode concluir o onboarding nos dois casos documentados, desde que todas as dúvidas percebidas fiquem definidas, localizadas, detalhadas e referenciadas no próprio A. No primeiro, A envia um campo a B e C e permanece desconhecido se C aceita sua ausência. No segundo, há duas regras em A para calcular o segmento e a seleção entre elas continua incerta. A ação posterior de retirar o campo ou mudar a regra exige evidência adequada à ação. [Esclarecimentos do onboarding](../evidencias/ESCLARECIMENTOS-ONBOARDING.md).

## 4. Escrita, conflitos e atualização antes de cada push

| Operação | Regra no alcance aceito | Origem |
|---|---|---|
| **S1 · Correção documental** | Se a evidência pertinente demonstrar a inconsistência **e** determinar a correção, o agente corrige no destino autorizado, verifica o resultado e conserva rastreabilidade, sem pedir permissão pontual adicional. Se apenas a divergência estiver demonstrada, preserva as fontes e questiona quando necessário. Esse aceite vale para conhecimento, inclusive a correção documental anterior ao push. | Ed. 9; interpretação conjunta das respostas S1 e S3. |
| **S2 · Incorporação de novo entendimento** | O agente solicita ao Analista da atividade autorização para escrever, apresentando em um só pedido **entendimento, origem, destino e efeito da escrita**. Uma confirmação que cubra os quatro elementos basta. O Analista pode autorizar destino nomeado em outra Sigla desde que a escrita seja permitida no repositório. Silêncio gera pendência. Negativa descarta a incorporação no destino negado. Lacuna factual independente e originais mantêm seus tratamentos próprios. | Ed. 7–10; R2/R3, S2. |
| **S3 · Conflito e reconciliação** | Catalogar na camada e no ponto afetados, preservar as duas declarações com origem e revisão e indicar exatamente a divergência. Nas atividades direta ou indiretamente dependentes, apresentá-la com detalhes, instruções e referências. Quando evidência ou decisão as reconciliar, registrar por que a atribuição passa a valer e com qual alcance. Se o conflito continuar sem fundamento para arbitragem, ele permanece explícito nas consultas afetadas. | Ed. 8–10; R6, S3. |
| **Atualização anterior a todo push** | Toda mudança de código precisa refletir-se em todo conhecimento cujo significado se altere. A exigência do produto é que a atualização ou revalidação documental anteceda cada push com garantia determinística vinculada ao conteúdo exato candidato ao envio. Mudança posterior invalida a prova. Demonstrar impacto inclusive sobre referências. Admitir revalidação registrada com evidência de ausência de impacto quando aplicável. | Ed. 4–9; C-P03-02/04, R9, S1. |
| **Validade e composição** | A produção, a verificação, o envio de uma contribuição e sua adoção como referência compartilhada têm estados próprios. Em múltiplos repositórios, explicitar commits, ponteiros e dependências da composição. Para divergência externa detectada, invalidar o uso como atual, reconciliar e verificar antes de restaurar validade. Sem monitor demonstrado, a detecção ocorre na próxima leitura ou ciclo. | HUM-08/09, D02-RET-004, ed. 8–11; P04.1–5 e P04.11 aprofundarão os mecanismos. |

A permissão de escrita do produto observa os direitos reais do destino. Acesso ao pai, leitura, armazenamento derivado, redistribuição e publicação têm alcances próprios. O inventário inicial segue a autorização do onboarding. O retorno posterior ao legado requer aviso e permissão no escopo aplicável; uma busca externa também requer finalidade e autorização pertinentes. O onboarding preserva a aplicação e os originais. Controles de todos os clientes de envio, verificação semântica, aplicação corporativa de barreiras e recuperação de composições parciais requerem mecanismos e provas futuras. [Retificações D02](../../RETIFICACOES.md) · [Registro D02](../../REGISTRO.md).

## 5. Catálogo da raiz e responsabilidades da Sigla

O **catálogo da raiz da Plataforma integra a primeira entrega**. Para cada Sigla, o conteúdo mínimo indicado é responsabilidade, escopo e domínio. Quando o agente conhece o assunto e ainda desconhece a Sigla, o catálogo pode encaminhá-lo a uma ou mais Siglas. Se já conhece a Sigla, o Meso indica que repositórios respondem pela etapa relevante. A base Micro apropriada sustenta a resposta sobre a aplicação. Uma solução compõe evidências de vários componentes para descrever a jornada delimitada funcionalmente pelo Analista.

- Qualquer pessoa pode originar uma declaração de responsabilidade. Uma atribuição inicialmente sem contestação pode orientar o roteamento **imediatamente como declarada**, conservando origem e revisão. Corroboração exige suporte próprio.
- Qualquer pessoa no contexto da Plataforma pode ler o catálogo, independentemente da Sigla. Os acessos e operações sobre fontes privadas, submódulos e serviços associados continuam vinculados aos direitos da origem e do destino.
- Alterações pertinentes dos Mesos devem refletir-se na raiz. Invalidar a entrada afetada ao detectar divergência e indicar a última origem/revisão verificável até reconciliar e verificar. Tratar contradições pelo fluxo S3.
- A identidade física entre raiz de instalação e Macro Git, a implementação da propagação, a concorrência e os controles corporativos seguem nos refinamentos correspondentes. Expor uma relação em um índice continua condicionado à possibilidade de divulgar sua existência e identificadores.

[Decisão de inclusão e atualização do catálogo](historico/CADERNO-ED11.md#saldo-p03-r8) · [Aceites finais S2 e S3](historico/CADERNO-ED11.md#fechamento-p03).

## 6. Rastreio das oito colaterais

| ID | Saldo e exemplo do efeito | Fonte no caderno |
|---|---|---|
| C-P03-01 | **Aceito.** A explicação da resposta da integração alcança as condições, os caminhos e os efeitos materiais encontrados dentro de A, incluindo encerramento sem publicação. Para o receptor seguinte valem os limites de P03.6. | Ed. 3–4; P03.1. |
| C-P03-02 | **Aceito.** Uma origem principal por fato, referências nos demais pontos e atualização de todo significado afetado. | Ed. 4; P03.1, P03.12, P03.22. |
| C-P03-03 | **Direção aceita.** Cobrir aspectos e unidades tanto quanto possível e declarar os limites. A edição 8 fixou o DoD da produção, sem pressupor uma pergunta particular de uso. | Ed. 4 e 8; P03.2. |
| C-P03-04 | **Aceito.** Quando o objeto é a pasta indicada, retratar a cópia de trabalho examinada, incluindo alterações autorizadas e arquivos novos pertinentes, distinguindo-a do commit-base. A exigência de atualização anterior a todo push tem regras próprias na seção 4. | Ed. 4–5, 7–9; P03.7 e R9. |
| C-P03-05 | **Aceito.** Um link GitHub que nomeia explicitamente outra branch escolhe essa branch; o link remoto para a raiz mantém o padrão `main`. Falta de acesso é tratada como cobertura parcial. | Ed. 4–5; P03.7. |
| C-P03-06 | **Aceito.** Registrar parâmetro, padrão declarado no código, ponto de substituição e valor efetivo se houver evidência autorizada, ou seu desconhecimento quando faltar. A forma física desse registro segue em P03.22. | Ed. 5; P03.14. |
| C-P03-07 | **Adiado.** Comparação entre representações quanto a precisão, tempo, recursos e custo por tarefa e modalidade de agente pertence à futura avaliação de P03.20. | Ed. 4–8 e fechamento da ed. 10. |
| C-P03-08 | **Aceito no que se aplica.** Para mensageria, documentar contrato, origem/destino conhecidos e efeitos do processamento, inclusive sucesso, duplicidade ou falha quando demonstrados. Para banco, operação, dados lidos/alterados e efeitos de resultados relevantes, inclusive vazio ou erro. | Ed. 4; P03.1–2. |

## 7. Precedência, impactos e ponto de retomada

A referência de partida da entrevista foi o escopo funcional r1 da branch de refinamentos em `5f1d502a0b75fa24eb7616f930c2cf0415485ec8`. Este fechamento registra as respostas posteriores. As edições 1–11 do caderno são versões editoriais de trabalho; a revisão temática deste documento é outra identidade. Um exemplo ou recomendação assume estado de decisão apenas quando houve manifestação humana no alcance correspondente.

| Edição do caderno | Como usar |
|---|---|
| 1–2 | Agenda de 77 perguntas e primeira rodada das 22 de P03, com respostas, limites e registros C-P03. [Primeira rodada](historico/CADERNO-ED11.md#saldo-p03-r2). |
| 3–5 | Aceites sobre Sigla pelo nome, enriquecimento de Meso, aviso, exceção de execução, fronteira Micro, versões HOM e estado local. [Terceira edição](historico/CADERNO-ED11.md#saldo-p03-r3) · [Quarta edição](historico/CADERNO-ED11.md#saldo-p03-r4) · [Quinta edição](historico/CADERNO-ED11.md#saldo-p03-r5). |
| 6–7 | Inventário do saldo, aceite de P03.13, enriquecimento, catálogo na raiz, pré-push, DoD então candidato e exemplar ilustrativo de navegação. [Inventário](historico/CADERNO-ED11.md#pendencias-restantes-p03) · [Quinta rodada](historico/CADERNO-ED11.md#saldo-p03-r7). |
| 8 | Correção do DoD e da fronteira produtor/interação; P03.1 e P03.2 encerradas funcionalmente. O texto anterior que pedia objetivo particular ou consulta por outro agente para concluir o onboarding é histórico. [DoD corrigido](historico/CADERNO-ED11.md#saldo-p03-r8). |
| 9–10 | Correção autônoma inequívoca, pedido único de incorporação, negativa e silêncio, conflito e reconciliação. Fechamento sobre autoridade entre Siglas e uso imediato de atribuição declarada. [Sétima rodada](historico/CADERNO-ED11.md#saldo-p03-r9) · [Fechamento](historico/CADERNO-ED11.md#fechamento-p03). |
| 11 | Abertura integral do grupo P04. P04.6 herda a resposta ao caso central de incorporação. P04.1–5 e P04.7–12 contêm as 11 escolhas a deliberar. [Roteiro da entrevista](P04-ATUALIDADE.md) · [Fichas da edição 11](historico/CADERNO-ED11.md#p04-abertura). |

**Dependências.** PE-01 trata dos acessos e destinos da raiz e dos repositórios. PE-02 recebe o requisito de portabilidade e os limites das modalidades. PE-04 e o grupo P04 aprofundam validade, revalidação, composição e compartilhamento. PE-05 e PE-06 consomem as bases em atividades e retomadas. PE-07 aplica origem e permissões às extensões. PE-08 mantém a decisão sobre o nível de materialização arquitetural da primeira entrega. PE-09 mantém as escolhas próprias sobre fontes e autoridade de negócio. O índice do Meso e o catálogo de Siglas não decidem essas frentes por analogia.

**Próxima decisão.** P04.1 — ao encontrar uma nova revisão de um repositório já estudado, em que condições o Motor pode reaproveitar as unidades de conhecimento e quando deve ampliar a investigação? [Continuar em P04](P04-ATUALIDADE.md).
