# Rota vigente R03 — 13/11/2026

Leia a [consolidação P03/P04 R03](../consolidacao-r03/P04-CONSOLIDADO.md) na branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Confira o manifesto R03 e o recibo posterior por commit imutável. P03 conserva seus aceites e adiamentos; P04 está funcionalmente encerrado no alcance qualificado pela fonte recuperada, com proveniência indireta dos aceites iniciais. P01–P09 têm catálogo granular e prompt de continuidade. A R03 distingue decisão, proposta, relato corporativo e comprovação; sem código de produto, merge, ratificação ou mudança de permissões.

O conteúdo abaixo é o snapshot anterior, preservado literalmente. Pontos de retomada, estados de entrevista e hashes anteriores valem para a revisão ali identificada; ler a sobreposição R03 para o saldo atual. Os manifestos D02-doc-2/R01/R02 permanecem históricos, sem certificar os novos bytes desta navegação.

---

# P04 · Atualidade, autoridade e compartilhamento do conhecimento

**Rodada aberta.** Há doze fichas. P04.1 a P04.5 e P04.7 a P04.12 apresentam as onze decisões que aguardam resposta do usuário. Em P04.6, o caso descrito já está coberto pelas decisões de P03. O próximo ponto de retomada é [P04.1 · Atualização incremental](#p04-rodada-1).

**Origem e leitura.** As perguntas desta rodada são as registradas na edição de trabalho 11 do caderno, em 8 de novembro de 2026. A linha de base consultada foi o commit `5f1d502a0b75fa24eb7616f930c2cf0415485ec8` da branch `proposta/d02-primeira-entrega-refinamentos`. Os IDs P04.1 a P04.12 são editoriais e permitem responder e retomar cada ficha. [Entrada da primeira entrega](../README.md) · [Agenda P04](../ESCOPO.md#pendencias) · [Decisões do P03](P03-CONHECIMENTO.md) · [Fonte histórica da rodada](historico/CADERNO-ED11.md#p04-abertura).

**Como usar as fichas.** “Ponto de partida” recupera as premissas documentadas. Os exemplos são sintéticos. “Recomendação para discussão” é proposta do assistente e aguarda deliberação no alcance de cada pergunta. Em P04.6, “Encaminhamento” remete ao caso já decidido. Ao receber uma resposta, registrar o ID, seu alcance e as dúvidas que efetivamente restarem.

**Cenário para P04.1–4.** A é uma API que grava propostas e pode publicar mensagens para revisão. Seu Micro descreve a revisão de código a1. O Meso de sua Sigla aponta a versão correspondente do repositório. Surge uma revisão a2. Em sequência, importa decidir o trabalho a refazer, o que suspender enquanto se investiga, que verificação restaura a validade e como reconhecer a composição final. A correção anterior ao push e a detecção de uma mudança externa têm momentos diferentes.

## I · Atualização e validade das bases

<a id="p04-rodada-1"></a>

**P04.1 · Atualização incremental**

Quando surge uma revisão nova, que parte do estudo precisa ser refeita e que parte pode ser reaproveitada?

*Ponto de partida.* O Motor tem a responsabilidade de produzir ou atualizar a base. O componente de interação pode perceber que a referência está antiga e sinalizar o problema. A revisão afetada deve ser revalidada e, sem monitor ativo, a descoberta ocorre na próxima leitura ou ciclo.

*Exemplo.* Em a1, A publicava propostas ativas. Em a2, só publica propostas ativas e prioritárias. Há também uma rotina noturna de expiração. Em outro tipo de mudança, uma configuração compartilhada passa a controlar tanto a publicação quanto a expiração.

*Impacto.* Se reestudar pouco, uma dependência indireta fica desatualizada. Se repetir todo o onboarding para cada alteração, o custo cresce mesmo para partes independentes.

*Recomendação para discussão.* Na execução autorizada de atualização, começar pelas diferenças entre as revisões e pelas dependências daquilo que mudou. Reutilizar unidades cuja evidência permaneça aplicável, registrar o que foi reexaminado e ampliar a investigação quando a base anterior ou o alcance da mudança não puderem ser determinados. A investigação volta ao inventário completo se for necessário para delimitar esse alcance.

[Especificação do Motor, §4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L26) · [HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-1)

<a id="p04-rodada-2"></a>

**P04.2 · Alcance da invalidação**

Enquanto a revisão nova está sendo estudada, quais afirmações e decisões devem deixar de ser usadas como atuais?

*Ponto de partida.* O ciclo detectar, invalidar, reconciliar e verificar já está definido. O ponto deste item é o efeito imediato da detecção sobre usos conhecidos.

*Exemplo.* O Micro de A diz “toda proposta ativa gera uma mensagem”. Uma história usa essa afirmação para calcular quantas mensagens um worker receberá. Um documento independente explica o prazo de expiração. Um segundo Workspace possivelmente usa a mesma estimativa, mas o agente não consegue consultá-lo.

*Impacto.* Paralisar a Sigla inteira retém conhecimento ainda válido. Deixar a estimativa antiga disponível como atual pode produzir uma decisão incorreta sobre capacidade.

*Recomendação para discussão.* Suspender o uso como atual da afirmação afetada e das conclusões que comprovadamente dependem dela. Identificar o impacto indireto ainda incerto e o destino inacessível, sem alegar que ele foi atualizado. Preservar as partes sustentadas por evidência independente.

[HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [D02-RET-004 · consistência multirrepositório](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md#L10) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-2)

<a id="p04-rodada-3"></a>

**P04.3 · Restabelecimento da validade**

Que evidência basta para voltar a usar uma afirmação que ficou desatualizada?

*Ponto de partida.* Corrigir sem intervenção adicional é permitido quando a correção está demonstrada. A nova redação precisa ser verificada no alcance do que afirma.

*Exemplo.* Na revisão a2, o agente localiza a condição de prioridade e os dois ramos. Uma proposta ativa e prioritária é publicada. Para uma proposta ativa sem prioridade, o fluxo se encerra sem publicação. Existe um teste executado em a1, mas nenhum registro autorizado mostra que uma proposta específica tenha sido publicada após a mudança.

*Impacto.* Uma prova fraca pode restaurar uma orientação incorreta. Exigir execução para toda explicação do código cria trabalho e pode exigir uma autorização sem relação com a pergunta.

*Recomendação para discussão.* Associar a afirmação à evidência pertinente da nova revisão, verificar as condições e as contraevidências que mudam o resultado e registrar qual alcance voltou a valer. O código pode sustentar a regra prevista em a2. Uma afirmação sobre execução efetiva exige sua própria evidência. Uma parte ainda inconclusiva conserva a ressalva.

[HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [D02-CT-05 · contrato candidato de consistência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L21) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-3)

<a id="p04-rodada-4"></a>

**P04.4 · Fechamento entre Micro, Meso e raiz**

Quando a atualização está concluída se o Micro já mudou, mas o Meso ainda referencia a revisão anterior?

*Ponto de partida.* Cada repositório tem revisão própria. O Meso referencia os Micro pertinentes. A raiz reflete mudanças que afetem o seu catálogo. Não se presume que várias escritas se concluam simultaneamente.

*Exemplo.* O Micro já descreve a2. O Meso ainda aponta para a1 porque sua atualização falhou. A responsabilidade “receber propostas” registrada na raiz continua correta.

*Impacto.* Quem abrir pelo Meso receberá o material de a1. Quem abrir o Micro diretamente poderá examinar a2. Chamar as duas visitas de “última versão” esconde qual composição o usuário realmente consultou.

*Recomendação para discussão.* Distinguir o resultado concluído no Micro da atualização de conjunto ainda pendente. Preservar a composição antiga identificada por revisão. Fechar a nova composição quando referências e materiais afetados forem conferidos e retomar da atualização que falhou. Só incluir a raiz na correção quando seu significado ou suas referências forem afetados.

[D02-RET-004 · consistência multirrepositório](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md#L10) · [D02-CT-05 · contrato candidato de consistência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L21) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-4)

## II · Contribuições de mais de uma pessoa ou agente

<a id="p04-rodada-5"></a>

**P04.5 · Contribuições concorrentes**

Se uma pessoa publica enquanto outra ainda trabalha sobre a mesma revisão antiga, o que a segunda precisa refazer antes de incorporar a sua contribuição?

*Ponto de partida.* Correções inequívocas têm tratamento autônomo. Um conflito sem solução exige preservar as declarações e apresentá-lo nos usos afetados. Falta aplicar essa regra à revisão-base que mudou durante o trabalho.

*Exemplo.* Duas pessoas partem do mesmo Micro. Uma passa a distinguir timeout de conexão e de leitura. A outra havia preparado, sobre a versão antiga, a alteração “o timeout é 5 s”. Aplicá-la diretamente pode apagar a distinção ou atribuir 5 s ao parâmetro errado.

*Impacto.* Uma atualização pode sobrescrever conhecimento correto mesmo sem o Git apontar conflito de texto. Em outros casos, as duas contribuições tratam de assuntos independentes e podem ser aproveitadas.

*Recomendação para discussão.* Reler a revisão vigente antes da incorporação, identificar qual parâmetro tem a evidência de 5 s e reaplicar apenas o que continua sustentado. Integrar partes independentes depois de conferi-las. Se as fontes não resolverem a ambiguidade, conservar as duas contribuições e solicitar o esclarecimento específico.

[HUM-09 · colaboração](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-09) · [D02-PEN-003 · revisões e concorrência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L121) · [Correção e conflito em P03](historico/CADERNO-ED11.md#saldo-p03-r9) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-5)

<a id="p04-rodada-6"></a>

**P04.6 · Esclarecimento reutilizável** · Coberto pelo P03 no caso central

Como incorporar o que se aprendeu em uma atividade para uso posterior?

*Ponto de partida.* O caso central tem resposta em P03. A explicação validada deve manter natureza, fonte, revisão, público e alcance. Para escrever, o agente reúne entendimento, origem, destino e efeito no mesmo pedido. O Analista da atividade pode autorizar o destino nomeado, inclusive de outra Sigla, se houver permissão efetiva. Correção documental inequívoca segue sua regra própria.

*Exemplo.* Em atividade de NC2, uma fonte de XP6 e o esclarecimento do Analista sustentam que uma regra se aplica ao canal agência. O Analista autoriza o destino nomeado. A unidade incorporada ao Micro identifica o canal e a revisão. Outra atividade que trate de aplicativo pode localizar a informação. Estender a regra ao aplicativo exige evidência pertinente.

*Impacto.* Uma frase aceita em uma conversa pode se tornar uma premissa ampla demais se o canal, o período ou a natureza da afirmação forem omitidos.

*Encaminhamento.* Aplicar o aceite existente. Silêncio gera pendência de autorização. A negativa descarta a incorporação naquele destino. A publicação da versão para outros consumidores é tratada em P04.11.

[D01-DEC-017 · esclarecimentos posteriores](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-017) · [Validação e escrita em P03](historico/CADERNO-ED11.md#saldo-p03-r8) · [Fechamento de P03](P03-CONHECIMENTO.md) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-6)

## III · Acesso, retenção e compartilhamento

<a id="p04-rodada-7"></a>

**P04.7 · Alcance e reuso de uma autorização**

Ao receber um segundo pedido, como o agente determina se uma autorização anterior ainda cobre a operação?

*Ponto de partida.* Autorizações podem ser pontuais ou reutilizáveis, individuais ou coletivas. A autorização de escrita de conhecimento pelo Analista já tem regra para seu caso. Acesso ao GitHub, consulta posterior ao legado, operação em outro serviço e distribuição têm alcances próprios.

*Exemplo.* Uma equipe recebe autorização reutilizável para consultar determinado contrato durante o refinamento da atividade X. Outro membro autorizado faz uma segunda consulta na mesma atividade. Depois surge o pedido de usar o contrato em Y ou copiar uma síntese para um público maior.

*Impacto.* Pedir confirmação a cada consulta torna inútil a concessão reutilizável. Aceitar qualquer pedido com base no mesmo acesso técnico extrapola o que a pessoa ou o grupo foi autorizado a fazer.

*Recomendação para discussão.* Para a nova operação, conferir concedente e autoridade, pessoa/grupo, fonte ou objeto, finalidade, ato, destinatários, vigência e direito efetivo. Reutilizar quando a concessão existente cobrir o caso. Se só a nova finalidade ou o público exceder o alcance, pedir apenas a autorização adicional pertinente.

[HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [D01-DEC-012 · concessão reutilizável](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-012) · [D01-DEC-013 · concessão coletiva](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-013) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-7)

<a id="p04-rodada-8"></a>

**P04.8 · Vencimento ou revogação**

O que deve acontecer com a cópia local e a síntese compartilhada quando a Plataforma souber que uma autorização terminou?

*Ponto de partida.* É necessário distinguir os direitos de consultar, conservar e compartilhar. A exclusão do original exige decisão expressa sobre objeto e revisão.

*Exemplo.* Um engenheiro perde acesso ao contrato de C. No dia anterior, havia guardado uma cópia local e produzido uma síntese para sua equipe. A equipe pode ter direito próprio, ainda válido, sobre o derivado. Em outro caso, a concessão original pode limitar também a retenção.

*Impacto.* Continuar consultando material com direito vencido e apagar uma síntese que a equipe pode legitimamente conservar são erros com efeitos diferentes.

*Recomendação para discussão.* Suspender o uso que dependia da concessão encerrada. Verificar separadamente o direito de retenção e uso de cada cópia ou derivado, indicar os destinos conhecidos e o responsável autorizado pela providência. Se os direitos forem incertos, suspender o uso dependente e registrar a pendência. Não prometer remoção de cópias fora do alcance operacional.

[HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [D02-PEN-004 · validade e revogação](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L122) · [D01-REL-008 · exclusão dos originais](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-rel-008) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-8)

<a id="p04-rodada-9"></a>

**P04.9 · Visibilidade dos identificadores**

O que um índice pode revelar sobre a existência de um repositório a quem tem acesso ao índice mas não ao repositório citado?

*Ponto de partida.* O catálogo de Siglas é legível independentemente da Sigla do leitor. Sua leitura não concede acesso a um destino privado. A decisão agora diz respeito aos identificadores que o documento pai já torna visíveis.

*Exemplo.* Um Meso legível pela equipe referencia C, privado para parte dos leitores. Mesmo sem abrir C, é possível ler no pai o nome ou caminho, a origem e o commit registrado. Ocultar o nome só na resposta do agente não remove o que já foi gravado no Git.

*Impacto.* O nome, isoladamente, pode revelar um projeto reservado. Restringir todos os nomes sem critério, por outro lado, impede localizar dependências que o leitor poderia legitimamente descobrir.

*Recomendação para discussão.* Definir a visibilidade da própria existência, dos identificadores e da revisão antes de incluí-los no pai. Se o público do pai for mais amplo que o permitido para esses dados, não gravar ali o identificador sensível. Usar outra origem autorizada ou referência menos reveladora quando permitida. A classificação padrão dos repositórios pertence a P01.

[Distribuição e acesso, metadados no pai](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/DISTRIBUICAO-E-ACESSO.md#L36) · [HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-9)

<a id="p04-rodada-10"></a>

**P04.10 · Conteúdo derivado e seu público**

Quando alguém pode ler a fonte, que comprovação é necessária para guardar ou compartilhar em outra base o que foi aprendido nela?

*Ponto de partida.* Acesso à fonte, retenção do derivado e redistribuição têm permissões distintas. Conhecimento compartilhável deve conservar origem e limites. Aqui importa o significado divulgado, além dos identificadores tratados em P04.9.

*Exemplo.* O time pode consultar o manual de um fornecedor e reter uma síntese em um Micro restrito. Uma frase dessa síntese revela a exceção que dispensa revisão manual. O Meso tem leitores adicionais.

*Impacto.* Resumir ou parafrasear uma regra pode expor exatamente o conteúdo restrito do original. Uma autorização válida para o Micro pode ser insuficiente para o Meso.

*Recomendação para discussão.* Conferir o direito de retenção e o público autorizado para cada destino. Se só a referência puder ser publicada, usar apenas os metadados permitidos. Se o compartilhamento for indeterminado, manter a parte autorizada utilizável e registrar a limitação no destino pertinente. A comprovação da política real cabe ao ambiente autorizado.

[D01-DEC-010 · referência e derivados](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-010) · [HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-10)

## IV · Publicação e consumo por outros agentes

<a id="p04-rodada-11"></a>

**P04.11 · Publicação e referência adotada**

Que marco permite a outra atividade tratar uma revisão verificada como referência compartilhada?

*Ponto de partida.* Git é canônico. Enviar uma contribuição de trabalho, passar na verificação pré-push, autorizar uma escrita e adotar a revisão como referência compartilhada têm efeitos distintos. A atribuição de Sigla pode orientar o catálogo imediatamente como declarada.

*Exemplo.* A revisão a2 da regra já foi verificada e enviada à branch da atividade. O Meso compartilhado ainda referencia a1. O engenheiro de outra atividade pergunta qual regra utilizar no refinamento dele.

*Impacto.* Sem indicar destino e revisão adotada, a resposta pode usar uma proposta como se ela já fosse a versão da equipe ou ignorar uma atualização de fato publicada.

*Recomendação para discussão.* Distinguir a revisão candidata verificável da que o destino autorizado adotou. Explicitar o ato e a autoridade de publicação, a revisão disponível e a confirmação do destino. Quando uma adoção automática estiver dentro de controles e autoridade já concedidos, evitar um novo aceite humano por padrão. A escolha do mecanismo e o alcance da publicação remota da v1 se articulam com P01.

[D01-DEC-007 · publicação canônica](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-007) · [HUM-09 · colaboração](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-09) · [Fechamento de P03](P03-CONHECIMENTO.md) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-11)

<a id="p04-rodada-12"></a>

**P04.12 · Representação parcialmente compreendida**

Que parte de uma base o componente de interação pode usar quando só entende parte da representação recebida?

*Ponto de partida.* P03 separou produção da base e uso nas interações. O formato físico e os adaptadores ficam para especificação. É possível definir o comportamento esperado antes de escolhê-los.

*Exemplo.* A nova revisão distingue “contrato conferido”, “fonte inacessível” e “fora da seleção”. Um agente antigo lê o nome e a existência do contrato, mas ignora esse estado. Em outra seção da mesma base, o timeout padrão e sua evidência permanecem inteiramente inteligíveis.

*Impacto.* Ignorar um estado desconhecido pode fazer o agente dizer que verificou o contrato. Recusar a base inteira também pode impedir uma resposta independente que ele conseguiria sustentar.

*Recomendação para discussão.* Usar as unidades cujo significado e condições críticas são recuperáveis. Para a parte incompatível, procurar representação compatível ou fonte autorizada. Se isso não for possível, informar o limite e suspender a conclusão dependente. Uma informação opcional desconhecida pode ser ignorada somente quando sua irrelevância para a conclusão for demonstrável.

[D02-PEN-005 · representação e adaptadores](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L123) · [D02-CT-02 · unidade de conhecimento, proposta](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L9) · [Ficha de abertura original](historico/CADERNO-ED11.md#p04-12)
