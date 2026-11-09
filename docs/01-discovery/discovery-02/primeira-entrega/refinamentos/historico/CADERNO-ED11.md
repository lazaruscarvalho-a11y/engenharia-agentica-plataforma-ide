# Caderno de esclarecimentos da primeira entrega

**Discovery da Plataforma/IDE de Engenharia Agêntica · edição de trabalho 11 · 8 de novembro de 2026**

**Ponto de retomada · Grupo P04.** A [rodada de P04](#p04-abertura) apresenta as 12 fichas com os exemplos, impactos e referências. O [fechamento do P03](#fechamento-p03) preserva as decisões que já se aplicam.

**Base consultada.** Repositório `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`, branch `proposta/d02-primeira-entrega-refinamentos`, HEAD confirmado `5f1d502a0b75fa24eb7616f930c2cf0415485ec8`. A entrada, o escopo funcional r1, o roteiro e suas evidências foram lidos nessa revisão. P01–P09 são os índices da agenda oficial. A numeração decimal neste caderno é uma decomposição de trabalho, criada para responder e retomar cada ponto. Uma pergunta pode servir a mais de uma frente. [Entrada da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/README.md) · [Escopo e agenda](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#pendencias) · [Roteiro por frente](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/roteiro/REFINAMENTO-E-REVISAO.md)

## Como responder

A rodada atual é P04. A entrevista de P03 foi encerrada no alcance registrado. Você pode responder em linguagem livre, indicando o ID do item ou do esclarecimento colateral. Por exemplo, **“P04.1 — quando uma nova revisão mudar apenas um fluxo, o Motor deve…”**. Uma resposta pode aceitar a recomendação inteira, alterar uma condição ou decidir apenas o caso apresentado. Nas próximas rodadas, a resposta deve ser registrada com o seu alcance e confrontada com as perguntas dependentes. Se resolver três itens, basta responder uma vez. Se uma conclusão depender de verificar um fato do ambiente corporativo, cabe identificar a verificação e quem está autorizado a fazê-la.

**Agenda** indica que o tema está expressamente aberto nas fontes. **Desdobramento** indica uma pergunta que formulei para tornar um tema verificável ou expor uma ambiguidade com consequência prática. Esses rótulos identificam a origem das perguntas da edição 1. O registro de fechamento apresenta a situação atual do P03. As rodadas anteriores conservam os seus registros e exemplos. Os exemplos são sintéticos e as recomendações são propostas de produto. Um formato ilustrativo, uma recomendação ou uma resposta aplicada a um exemplo só vira decisão no alcance que você confirmar.

## Mapa das 77 perguntas de partida

| Grupo | Frente principal nesta leitura | IDs do caderno | Total | O que a resposta esclarece |
|---|---|---|---:|---|
| [P03 · Micro, Meso e suficiência](#fechamento-p03) | PE-03 e PE-04 | P03.1 a P03.22 | 22 | Exemplares, entradas, alcance da evidência e comunicação |
| [P04 · Atualidade, autoridade e compartilhamento](#p04-abertura) | PE-03 e PE-04 e seus consumidores | P04.1 a P04.12 | 12 | Mudança de revisão, concorrência, validade e direitos |
| [P01 · Distribuição e acesso](#p01-1) | PE-01 | P01.1 a P01.7 | 7 | Instalação, carga parcial, visibilidade e publicação |
| [P02 · Ferramentas de IA](#p02-1) | PE-02 | P02.1 a P02.5 | 5 | Suporte e evidência por modalidade |
| [P05 · Workspace](#p05-1) | PE-05 | P05.1 a P05.6 | 6 | Ciclo, associação, estrutura e histórico |
| [P06 · Atuação do agente e histórias](#p06-1) | PE-06 | P06.1 a P06.7 | 7 | Etapas, correções e contratos de histórias |
| [P07 · Extensões](#p07-1) | PE-07 | P07.1 a P07.5 | 5 | Descoberta, precedência, retirada e permissões |
| [P08 · Arquitetura/Solução](#p08-1) | PE-08 | P08.1 a P08.6 | 6 | Saída desta versão, fronteira e manutenção |
| [P09 · Conhecimento de Negócios](#p09-1) | PE-09 | P09.1 a P09.7 | 7 | Caso, fontes, autoridade, organização e vigência |

**34 perguntas aprofundam P03 e P04. As outras 43 cobrem os sete grupos restantes.** O total expressa a granularidade deste caderno. Novos exemplos ou respostas podem unir, resolver ou revelar outras questões. A sequência sugerida começa no Micro de A. A leitura das questões de outras frentes é opcional nesta rodada.

<a id="p04-abertura"></a>

## P04 · Rodada de refinamento sobre atualidade, autoridade e compartilhamento

**Edição de trabalho 11 · 8 de novembro de 2026.** A base oficial foi relida na branch `proposta/d02-primeira-entrega-refinamentos`, commit `5f1d502a0b75fa24eb7616f930c2cf0415485ec8`. P04 é um grupo da agenda, pertinente a PE-03 e PE-04 e a outras frentes que usam as bases. Os IDs P04.1 a P04.12 identificam as fichas editoriais do caderno. Manter os IDs permite rastrear a abertura original e as respostas seguintes. [Agenda P04](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#pendencias) · [Roteiro de refinamento](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/roteiro/REFINAMENTO-E-REVISAO.md) · [Fechamento de P03](#fechamento-p03)

**Como responder.** Há 12 fichas. Onze apresentam uma escolha residual. P04.6 recupera o comportamento já definido no P03 e dispensa resposta para o caso descrito. Responda por ID, em linguagem livre. As recomendações são propostas para sua apreciação. As referências ao Git são da revisão imutável; as decisões posteriores do P03 estão documentadas no próprio caderno. Os exemplos descrevem uso futuro com dados sintéticos.

**Cenário para P04.1–4.** A é uma API que grava propostas e pode publicar mensagens para revisão. Seu Micro descreve a revisão de código a1. O Meso de sua Sigla aponta a versão correspondente do repositório. Surge uma revisão a2. Em sequência, importa decidir o trabalho a refazer, o que suspender enquanto se investiga, que verificação restaura a validade e como reconhecer a composição final. A correção anterior ao push e a detecção de uma mudança externa têm momentos diferentes.

### I · Atualização e validade das bases

<a id="p04-rodada-1"></a>

**P04.1 · Atualização incremental**

Quando surge uma revisão nova, que parte do estudo precisa ser refeita e que parte pode ser reaproveitada?

*Ponto de partida.* O Motor tem a responsabilidade de produzir ou atualizar a base. O componente de interação pode perceber que a referência está antiga e sinalizar o problema. A revisão afetada deve ser revalidada e, sem monitor ativo, a descoberta ocorre na próxima leitura ou ciclo.

*Exemplo.* Em a1, A publicava propostas ativas. Em a2, só publica propostas ativas e prioritárias. Há também uma rotina noturna de expiração. Em outro tipo de mudança, uma configuração compartilhada passa a controlar tanto a publicação quanto a expiração.

*Impacto.* Se reestudar pouco, uma dependência indireta fica desatualizada. Se repetir todo o onboarding para cada alteração, o custo cresce mesmo para partes independentes.

*Recomendação para discussão.* Na execução autorizada de atualização, começar pelas diferenças entre as revisões e pelas dependências daquilo que mudou. Reutilizar unidades cuja evidência permaneça aplicável, registrar o que foi reexaminado e ampliar a investigação quando a base anterior ou o alcance da mudança não puderem ser determinados. A investigação volta ao inventário completo se for necessário para delimitar esse alcance.

[Especificação do Motor, §4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md#L26) · [HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [Ficha de abertura original](#p04-1)

<a id="p04-rodada-2"></a>

**P04.2 · Alcance da invalidação**

Enquanto a revisão nova está sendo estudada, quais afirmações e decisões devem deixar de ser usadas como atuais?

*Ponto de partida.* O ciclo detectar, invalidar, reconciliar e verificar já está definido. O ponto deste item é o efeito imediato da detecção sobre usos conhecidos.

*Exemplo.* O Micro de A diz “toda proposta ativa gera uma mensagem”. Uma história usa essa afirmação para calcular quantas mensagens um worker receberá. Um documento independente explica o prazo de expiração. Um segundo Workspace possivelmente usa a mesma estimativa, mas o agente não consegue consultá-lo.

*Impacto.* Paralisar a Sigla inteira retém conhecimento ainda válido. Deixar a estimativa antiga disponível como atual pode produzir uma decisão incorreta sobre capacidade.

*Recomendação para discussão.* Suspender o uso como atual da afirmação afetada e das conclusões que comprovadamente dependem dela. Identificar o impacto indireto ainda incerto e o destino inacessível, sem alegar que ele foi atualizado. Preservar as partes sustentadas por evidência independente.

[HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [D02-RET-004 · consistência multirrepositório](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md#L10) · [Ficha de abertura original](#p04-2)

<a id="p04-rodada-3"></a>

**P04.3 · Restabelecimento da validade**

Que evidência basta para voltar a usar uma afirmação que ficou desatualizada?

*Ponto de partida.* Corrigir sem intervenção adicional é permitido quando a correção está demonstrada. A nova redação precisa ser verificada no alcance do que afirma.

*Exemplo.* Na revisão a2, o agente localiza a condição de prioridade e os dois ramos: ativa e prioritária publica; ativa e sem prioridade encerra sem publicar. Existe um teste executado em a1, mas nenhum registro autorizado mostra que uma proposta específica tenha sido publicada após a mudança.

*Impacto.* Uma prova fraca pode restaurar uma orientação incorreta. Exigir execução para toda explicação do código cria trabalho e pode exigir uma autorização sem relação com a pergunta.

*Recomendação para discussão.* Associar a afirmação à evidência pertinente da nova revisão, verificar as condições e as contraevidências que mudam o resultado e registrar qual alcance voltou a valer. O código pode sustentar a regra prevista em a2. Uma afirmação sobre execução efetiva exige sua própria evidência. Uma parte ainda inconclusiva conserva a ressalva.

[HUM-08 · atualização e divergência entre revisões](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-08) · [D02-CT-05 · contrato candidato de consistência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L21) · [Ficha de abertura original](#p04-3)

<a id="p04-rodada-4"></a>

**P04.4 · Fechamento entre Micro, Meso e raiz**

Quando a atualização está concluída se o Micro já mudou, mas o Meso ainda referencia a revisão anterior?

*Ponto de partida.* Cada repositório tem revisão própria. O Meso referencia os Micro pertinentes. A raiz reflete mudanças que afetem o seu catálogo. Não se presume que várias escritas se concluam simultaneamente.

*Exemplo.* O Micro já descreve a2. O Meso ainda aponta para a1 porque sua atualização falhou. A responsabilidade “receber propostas” registrada na raiz continua correta.

*Impacto.* Quem abrir pelo Meso receberá o material de a1; quem abrir o Micro diretamente poderá examinar a2. Chamar as duas visitas de “última versão” esconde qual composição o usuário realmente consultou.

*Recomendação para discussão.* Distinguir o resultado concluído no Micro da atualização de conjunto ainda pendente. Preservar a composição antiga identificada por revisão. Fechar a nova composição quando referências e materiais afetados forem conferidos; retomar da atualização que falhou. Só incluir a raiz na correção quando seu significado ou suas referências forem afetados.

[D02-RET-004 · consistência multirrepositório](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md#L10) · [D02-CT-05 · contrato candidato de consistência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L21) · [Ficha de abertura original](#p04-4)

### II · Contribuições de mais de uma pessoa ou agente

<a id="p04-rodada-5"></a>

**P04.5 · Contribuições concorrentes**

Se uma pessoa publica enquanto outra ainda trabalha sobre a mesma revisão antiga, o que a segunda precisa refazer antes de incorporar a sua contribuição?

*Ponto de partida.* Correções inequívocas têm tratamento autônomo; conflito sem solução exige preservar as declarações e apresentá-lo nos usos afetados. Falta aplicar essa regra à revisão-base que mudou durante o trabalho.

*Exemplo.* Duas pessoas partem do mesmo Micro. Uma passa a distinguir timeout de conexão e de leitura. A outra havia preparado, sobre a versão antiga, a alteração “o timeout é 5 s”. Aplicá-la diretamente pode apagar a distinção ou atribuir 5 s ao parâmetro errado.

*Impacto.* Uma atualização pode sobrescrever conhecimento correto mesmo sem o Git apontar conflito de texto. Em outros casos, as duas contribuições tratam de assuntos independentes e podem ser aproveitadas.

*Recomendação para discussão.* Reler a revisão vigente antes da incorporação, identificar qual parâmetro tem a evidência de 5 s e reaplicar apenas o que continua sustentado. Integrar partes independentes depois de conferi-las. Se as fontes não resolverem a ambiguidade, conservar as duas contribuições e solicitar o esclarecimento específico.

[HUM-09 · colaboração](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-09) · [D02-PEN-003 · revisões e concorrência](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L121) · [Correção e conflito em P03](#saldo-p03-r9) · [Ficha de abertura original](#p04-5)

<a id="p04-rodada-6"></a>

**P04.6 · Esclarecimento reutilizável** · Coberto pelo P03 no caso central

Como incorporar o que se aprendeu em uma atividade para uso posterior?

*Ponto de partida.* O caso central tem resposta em P03. A explicação validada deve manter natureza, fonte, revisão, público e alcance. Para escrever, o agente reúne entendimento, origem, destino e efeito no mesmo pedido. O Analista da atividade pode autorizar o destino nomeado, inclusive de outra Sigla, se houver permissão efetiva. Correção documental inequívoca segue sua regra própria.

*Exemplo.* Em atividade de NC2, uma fonte de XP6 e o esclarecimento do Analista sustentam que uma regra se aplica ao canal agência. O Analista autoriza o destino nomeado. A unidade incorporada ao Micro identifica o canal e a revisão. Outra atividade que trate de aplicativo pode localizar a informação; para estender a regra ao aplicativo precisará de evidência pertinente.

*Impacto.* Uma frase aceita em uma conversa pode se tornar uma premissa ampla demais se o canal, o período ou a natureza da afirmação forem omitidos.

*Encaminhamento.* Aplicar o aceite existente. Silêncio gera pendência de autorização; negativa descarta a incorporação naquele destino. Não se solicita outra resposta nesta rodada para este caso. A publicação da versão para outros consumidores é tratada em P04.11.

[D01-DEC-017 · esclarecimentos posteriores](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-017) · [Validação e escrita em P03](#saldo-p03-r8) · [Fechamento de P03](#fechamento-p03) · [Ficha de abertura original](#p04-6)

### III · Acesso, retenção e compartilhamento

<a id="p04-rodada-7"></a>

**P04.7 · Alcance e reuso de uma autorização**

Ao receber um segundo pedido, como o agente determina se uma autorização anterior ainda cobre a operação?

*Ponto de partida.* Autorizações podem ser pontuais ou reutilizáveis, individuais ou coletivas. A autorização de escrita de conhecimento pelo Analista já tem regra para seu caso. Acesso ao GitHub, consulta posterior ao legado, operação em outro serviço e distribuição têm alcances próprios.

*Exemplo.* Uma equipe recebe autorização reutilizável para consultar determinado contrato durante o refinamento da atividade X. Outro membro autorizado faz uma segunda consulta na mesma atividade. Depois surge o pedido de usar o contrato em Y ou copiar uma síntese para um público maior.

*Impacto.* Pedir confirmação a cada consulta torna inútil a concessão reutilizável. Aceitar qualquer pedido com base no mesmo acesso técnico extrapola o que a pessoa ou o grupo foi autorizado a fazer.

*Recomendação para discussão.* Para a nova operação, conferir concedente e autoridade, pessoa/grupo, fonte ou objeto, finalidade, ato, destinatários, vigência e direito efetivo. Reutilizar quando a concessão existente cobrir o caso. Se só a nova finalidade ou o público exceder o alcance, pedir apenas a autorização adicional pertinente.

[HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [D01-DEC-012 · concessão reutilizável](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-012) · [D01-DEC-013 · concessão coletiva](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-013) · [Ficha de abertura original](#p04-7)

<a id="p04-rodada-8"></a>

**P04.8 · Vencimento ou revogação**

O que deve acontecer com a cópia local e a síntese compartilhada quando a Plataforma souber que uma autorização terminou?

*Ponto de partida.* É necessário distinguir os direitos de consultar, conservar e compartilhar. A exclusão do original exige decisão expressa sobre objeto e revisão.

*Exemplo.* Um engenheiro perde acesso ao contrato de C. No dia anterior, havia guardado uma cópia local e produzido uma síntese para sua equipe. A equipe pode ter direito próprio, ainda válido, sobre o derivado; ou a concessão original podia limitar também a retenção.

*Impacto.* Continuar consultando material com direito vencido e apagar uma síntese que a equipe pode legitimamente conservar são erros com efeitos diferentes.

*Recomendação para discussão.* Suspender o uso que dependia da concessão encerrada. Verificar separadamente o direito de retenção e uso de cada cópia ou derivado, indicar os destinos conhecidos e o responsável autorizado pela providência. Se os direitos forem incertos, suspender o uso dependente e registrar a pendência. Não prometer remoção de cópias fora do alcance operacional.

[HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [D02-PEN-004 · validade e revogação](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L122) · [D01-REL-008 · exclusão dos originais](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-rel-008) · [Ficha de abertura original](#p04-8)

<a id="p04-rodada-9"></a>

**P04.9 · Visibilidade dos identificadores**

O que um índice pode revelar sobre a existência de um repositório a quem tem acesso ao índice mas não ao repositório citado?

*Ponto de partida.* O catálogo de Siglas é legível independentemente da Sigla do leitor. Sua leitura não concede acesso a um destino privado. A decisão agora diz respeito aos identificadores que o documento pai já torna visíveis.

*Exemplo.* Um Meso legível pela equipe referencia C, privado para parte dos leitores. Mesmo sem abrir C, é possível ler no pai o nome ou caminho, a origem e o commit registrado. Ocultar o nome só na resposta do agente não remove o que já foi gravado no Git.

*Impacto.* O nome, isoladamente, pode revelar um projeto reservado. Restringir todos os nomes sem critério, por outro lado, impede localizar dependências que o leitor poderia legitimamente descobrir.

*Recomendação para discussão.* Definir a visibilidade da própria existência, dos identificadores e da revisão antes de incluí-los no pai. Se o público do pai for mais amplo que o permitido para esses dados, não gravar ali o identificador sensível; usar outra origem autorizada ou referência menos reveladora quando permitida. A classificação padrão dos repositórios pertence a P01.

[Distribuição e acesso, metadados no pai](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/DISTRIBUICAO-E-ACESSO.md#L36) · [HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [Ficha de abertura original](#p04-9)

<a id="p04-rodada-10"></a>

**P04.10 · Conteúdo derivado e seu público**

Quando alguém pode ler a fonte, que comprovação é necessária para guardar ou compartilhar em outra base o que foi aprendido nela?

*Ponto de partida.* Acesso à fonte, retenção do derivado e redistribuição têm permissões distintas. Conhecimento compartilhável deve conservar origem e limites. Aqui importa o significado divulgado, além dos identificadores tratados em P04.9.

*Exemplo.* O time pode consultar o manual de um fornecedor e reter uma síntese em um Micro restrito. Uma frase dessa síntese revela a exceção que dispensa revisão manual. O Meso tem leitores adicionais.

*Impacto.* Resumir ou parafrasear uma regra pode expor exatamente o conteúdo restrito do original. Uma autorização válida para o Micro pode ser insuficiente para o Meso.

*Recomendação para discussão.* Conferir o direito de retenção e o público autorizado para cada destino. Se só a referência puder ser publicada, usar apenas os metadados permitidos. Se o compartilhamento for indeterminado, manter a parte autorizada utilizável e registrar a limitação no destino pertinente. A comprovação da política real cabe ao ambiente autorizado.

[D01-DEC-010 · referência e derivados](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-010) · [HUM-06 · autorizações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-06) · [Ficha de abertura original](#p04-10)

### IV · Publicação e consumo por outros agentes

<a id="p04-rodada-11"></a>

**P04.11 · Publicação e referência adotada**

Que marco permite a outra atividade tratar uma revisão verificada como referência compartilhada?

*Ponto de partida.* Git é canônico. Enviar uma contribuição de trabalho, passar na verificação pré-push, autorizar uma escrita e adotar a revisão como referência compartilhada têm efeitos distintos. A atribuição de Sigla pode orientar o catálogo imediatamente como declarada.

*Exemplo.* A revisão a2 da regra já foi verificada e enviada à branch da atividade. O Meso compartilhado ainda referencia a1. O engenheiro de outra atividade pergunta qual regra utilizar no refinamento dele.

*Impacto.* Sem indicar destino e revisão adotada, a resposta pode usar uma proposta como se ela já fosse a versão da equipe ou ignorar uma atualização de fato publicada.

*Recomendação para discussão.* Distinguir a revisão candidata verificável da que o destino autorizado adotou. Explicitar o ato e a autoridade de publicação, a revisão disponível e a confirmação do destino. Quando uma adoção automática estiver dentro de controles e autoridade já concedidos, evitar um novo aceite humano por padrão. A escolha do mecanismo e o alcance da publicação remota da v1 se articulam com P01.

[D01-DEC-007 · publicação canônica](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-01/REGISTRO.md#d01-dec-007) · [HUM-09 · colaboração](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-09) · [Fechamento de P03](#fechamento-p03) · [Ficha de abertura original](#p04-11)

<a id="p04-rodada-12"></a>

**P04.12 · Representação parcialmente compreendida**

Que parte de uma base o componente de interação pode usar quando só entende parte da representação recebida?

*Ponto de partida.* P03 separou produção da base e uso nas interações. O formato físico e os adaptadores ficam para especificação. É possível definir o comportamento esperado antes de escolhê-los.

*Exemplo.* A nova revisão distingue “contrato conferido”, “fonte inacessível” e “fora da seleção”. Um agente antigo lê o nome e a existência do contrato, mas ignora esse estado. Em outra seção da mesma base, o timeout padrão e sua evidência permanecem inteiramente inteligíveis.

*Impacto.* Ignorar um estado desconhecido pode fazer o agente dizer que verificou o contrato. Recusar a base inteira também pode impedir uma resposta independente que ele conseguiria sustentar.

*Recomendação para discussão.* Usar as unidades cujo significado e condições críticas são recuperáveis. Para a parte incompatível, procurar representação compatível ou fonte autorizada; se não conseguir, informar o limite e suspender a conclusão dependente. Uma informação opcional desconhecida pode ser ignorada somente quando sua irrelevância para a conclusão for demonstrável.

[D02-PEN-005 · representação e adaptadores](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#L123) · [D02-CT-02 · unidade de conhecimento, proposta](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md#L9) · [Ficha de abertura original](#p04-12)

**Continuidade.** Primeiro ponto sugerido: P04.1, critério de reaproveitamento após mudança de revisão. O início desta entrevista não transforma nenhuma recomendação nova em decisão. As respostas de P03 preservam seu alcance; publicação deste caderno **NÃO PERSISTIDA no GitHub**.

<a id="fechamento-p03"></a>

## P03 · Fechamento da rodada de esclarecimentos

**Edição de trabalho 10 · 8 de novembro de 2026.** Fonte direta: os dois aceites do usuário sobre a competência do Analista da atividade e o primeiro uso de uma atribuição no catálogo. Esta edição encerra as duas escolhas que ficaram abertas na edição 9.

| Questão | Decisão | Aplicação sintética |
|---|---|---|
| **S2 · Destino em outra Sigla** | O Analista da atividade pode autorizar o destino explicitamente nomeado no pedido, desde que a escrita seja permitida no repositório. O pedido identifica entendimento, origem, destino e efeito da escrita. Uma confirmação que abranja os quatro elementos basta, inclusive entre Siglas. | O Analista de uma atividade de NC2 pode autorizar a incorporação no Micro de XP6 assim identificado. A travessia da Sigla, por si só, não exige outra aprovação. A permissão técnica continua sendo verificada no destino. |
| **S3 · Primeira declaração no catálogo** | Uma atribuição de responsabilidade sem contestação pode ser usada imediatamente para roteamento na condição de **declarada**, conservando sua origem e revisão. | Se a entrada declara que NC2 responde pela análise inicial de uma proposta, uma consulta já pode ser encaminhada a NC2 com essa proveniência. Havendo divergência posterior, preservam-se as declarações e suas referências; o agente apresenta o conflito nas atividades direta ou indiretamente afetadas e registra a base da reconciliação quando ela ocorrer. |

**Saldo do P03.** As escolhas S1–S3 estão resolvidas no alcance funcional discutido. Entre as 22 perguntas originais, 20 estão resolvidas (P03.1–P03.19 e P03.21). P03.22 mantém a direção aceita e o desenho concreto dos documentos postergado. P03.20 e sua colateral C-P03-07 aguardam o refinamento de avaliação de qualidade e custo. Esta rodada não introduz nova pergunta de produto para P03. Os mecanismos de engenharia e as provas operacionais já encaminhados permanecem para suas etapas.

### Retomada proposta · P04, atualidade, autoridade e compartilhamento

As 12 fichas de partida de P04 estão no caderno. Esta leitura de dependências preserva os aceites de P03 e identifica o recorte da próxima entrevista. Não atribui aceite novo aos mecanismos de P04.

| Itens de P04 | O que já orienta as respostas | Próximo detalhe que pode mudar o comportamento |
|---|---|---|
| [P04.1–4 · Revisões e atualização](#p04-1) | Conhecimento afetado por mudança exige atualização ou revalidação; mudança externa exige detectar, invalidar, reconciliar e verificar. Micro, Meso e referências pertinentes têm revisões próprias. | Quando reaproveitar material em uma nova revisão, quais consumidores reexaminar, qual evidência restaura validade e como explicar uma composição atualizada apenas em parte. |
| [P04.5–7 · Contribuições e autorização](#p04-5) | Correção inequívoca pode ser autônoma; divergência sem solução permanece explícita. Em enriquecimento, o Analista da atividade pode autorizar o destino nomeado, inclusive entre Siglas. | Reconciliação de contribuições concorrentes sobre a mesma revisão-base e comprovação da autoridade, do objeto e da vigência quando a operação extrapola o caso já aceito. |
| [P04.8–10 · Revogação e uso de dados](#p04-8) | O catálogo da raiz é legível independentemente da Sigla. Ler, reter e redistribuir são operações com alcances distintos. | Efeitos da revogação sobre material já obtido e conteúdo ou metadados que podem ser legitimamente exibidos a outro público. |
| [P04.11–12 · Publicação e compatibilidade](#p04-11) | A declaração inicial pode orientar o roteamento com origem e revisão. Contribuição de trabalho, verificação e publicação continuam tendo papéis próprios. | Evento que disponibiliza as demais categorias de conhecimento como referência validada e conduta do consumidor diante de uma representação apenas parcialmente compatível. |

**Registro desta edição.** A base oficial consultada permanece no commit `5f1d502a0b75fa24eb7616f930c2cf0415485ec8`, branch `proposta/d02-primeira-entrega-refinamentos`. O fechamento foi registrado neste caderno. **NÃO PERSISTIDO no GitHub.**

<a id="saldo-p03-r9"></a>

## P03 · Sétima rodada — correção, incorporação e reconciliação

**Edição de trabalho 9 · 8 de novembro de 2026.** Fonte direta: as três respostas do usuário aos assuntos S1, S2 e S3 da edição 8. O objeto é o conhecimento produzido ou mantido pela Plataforma. Os exemplos são sintéticos. A formulação operacional de “certeza” abaixo é a interpretação conjunta das respostas 1 e 3, apoiada nos critérios já vigentes de revisão, evidência e contraevidência. Não foi definido um classificador ou limiar de confiança.

| Assunto | Decisão desta rodada | Alcance |
|---|---|---|
| **1 · Correção do conhecimento** | O agente corrige sem pedir autorização pontual quando tem certeza da inconsistência e as evidências aplicáveis determinam a correção. Havendo dúvida material após investigar, formula a pergunta necessária. | Abrange a correção documental determinada antes de um push. Verificar a versão afetada, a correção e as referências pertinentes. A atualização continua sujeita às permissões efetivas do destino e ao controle pré-push para o estado exato. A regra de correção documental não concede autorização para mudar o código da aplicação ou uma decisão de produto. |
| **2 · Pedido de incorporação** | O agente apresenta, em um só pedido, o entendimento, sua origem, o destino e o efeito da escrita. Uma confirmação é suficiente quando a resposta cobre os quatro. Se houver negativa, descarta-se a incorporação naquele destino. Uma contradição ou lacuna factual independente conserva seu próprio estado. | Na ausência de resposta, continua valendo o registro de pendência. A recusa não deve virar aprovação pendente. Para mais de um destino, o aceite cobre apenas os destinos e efeitos efetivamente abrangidos, respeitados os direitos técnicos. A identidade do Analista competente em caso entre Siglas segue em aberto. |
| **3 · Conflito** | Preservar as duas declarações e suas referências, indicar exatamente onde divergem e, quando surgir evidência ou decisão que as reconcilie, registrar por que a nova atribuição passou a valer. Sem arbitragem prevista e enquanto permanecer a divergência, mantê-la explícita em toda consulta ou atividade afetada direta ou indiretamente. | O fechamento do conflito depende de fundamento que diferencie as declarações no escopo examinado. O histórico permanece rastreável. A conduta em conflito ficou definida. A entrada em vigência de uma declaração inicial sem contestação é uma decisão distinta. |

### Como aplicar em três casos

1. **Correção inequívoca.** Na revisão candidata de A, o ramo de publicação exige uma proposta ativa e prioritária. A base para essa mesma revisão ainda diz que qualquer proposta ativa publica. Com o escopo, a condição e a fonte conferidos, o agente atualiza a regra e os registros afetados sem intervenção humana adicional, verifica o resultado e o vincula à revisão antes do envio.
2. **Entendimento novo e destino identificado.** Durante uma atividade de NC2, o agente encontra em XP6 uma regra até então ausente da base. Em um único pedido, identifica a regra, a evidência de XP6 na revisão examinada, o Micro de XP6 como destino e o efeito da inclusão. A confirmação que cobre esses elementos basta para o ato. Sem resposta fica pendente; se houver negativa, a proposta é descartada naquele destino. Uma lacuna factual independente continua aparecendo quando uma atividade depender dela.
3. **Divergência comprovada e solução ainda desconhecida.** Dois Mesos reivindicam a mesma responsabilidade para a mesma etapa e período. O agente consegue comprovar a divergência, mas não encontra fundamentação que permita escolher um deles. Registra e apresenta as duas atribuições, explicita o efeito sobre o roteamento da atividade e pede esclarecimento quando necessário. Quando houver evidência ou decisão que esclareça a responsabilidade, registra a revisão, o novo alcance e o motivo da reconciliação. A separação evita que certeza sobre a existência do problema seja confundida com certeza sobre como corrigi-lo.

### Duas escolhas ainda materiais

**S2 · Analista competente entre Siglas.** A regra do pedido único está resolvida. Se uma atividade de NC2 descobrir uma regra nova sobre XP6 e o destino for o Micro de XP6, basta a aprovação do Analista que acompanha a atividade ou é necessária a aprovação de um Analista com responsabilidade pelo destino? A leitura ampla da regra anterior (“todos terão autoridade de escrita”) favorece admitir o Analista da atividade quando as permissões efetivas cobrem o destino. A competência entre Siglas, porém, não foi expressamente delimitada. Recomenda-se designar quem pode conceder a única autorização aplicável sem instituir dupla confirmação por padrão.

**S3 · Uso inicial de uma declaração sem conflito.** Uma pessoa informa que NC2 responde por determinada etapa e ainda não há declaração incompatível. O catálogo já pode encaminhar consultas para NC2 identificando que se trata de atribuição declarada, ou deve exigir confirmação antes do primeiro encaminhamento? Recomenda-se admitir uso provisório com origem, revisão e estado visíveis e conservar a distinção entre atribuição declarada e atribuição corroborada. Nenhuma decisão anterior obriga a nomear um árbitro universal para conflitos futuros.

**Saldo.** S1 está encerrado no alcance da correção documental. S2 e S3 estão resolvidos nas condutas descritas e têm, cada um, uma decisão residual acima. S4 e S5 conservam seus encaminhamentos de engenharia e avaliação. Entre as 22 perguntas originais do P03, 20 permanecem resolvidas no alcance funcional. P03.22 tem desenho concreto postergado. P03.20 e sua colateral C-P03-07 aguardam a etapa reservada. Esta edição atualiza o caderno de Discovery. **NÃO PERSISTIDO no GitHub.**

<a id="saldo-p03-r8"></a>

## P03 · Sexta rodada, DoD corrigido e pendências após os últimos aceites

**Edição de trabalho 8 · 8 de novembro de 2026.** Fonte direta: respostas do usuário a P03.1, P03.2 e R1–R10. O aceite de R4 se aplica à proposta anterior com as duas correções explícitas de P03.2. As classificações são avaliação editorial no alcance de Discovery; o registro desta rodada prevalece sobre formulações anteriores do caderno sobre objetivo do onboarding e recuperação pelo agente.

### Decisões e limites de cada resposta

| Resposta | Avaliação |
|---|---|
| **P03.1 e R1 · Resolvidos funcionalmente** | Todo conhecimento suficientemente válido identificado na produção deve ser consolidado durante o onboarding. O usuário aceita a recomendação de tornar a regra recuperável por explicação no Micro ou referência canônica exata, acessível e suficiente. Quando for preciso interpretar ou combinar fontes para compreender um efeito material, ele merece explicação própria. A mecânica interna que preserva os efeitos pode ficar no código. Incerteza percebida é registrada no momento. Descobertas posteriores, aprofundamentos e lacunas resolvidas alimentam a base no alcance validado. Como estruturar e explicitar cada unidade fica para P03.22. |
| **P03.2 e R4 · Resolvidos com retificação** | O onboarding tem uma finalidade fixa: produzir a base de conhecimento do repositório importado. O Engenheiro indica o material e a revisão conforme os modos já definidos. Ele não precisa formular uma pergunta nem fornecer um objetivo de uso para que o Motor decida o que estudar. O consumidor acionado na interação posterior é responsável por entender o pedido e aplicar as skills, instruções, diretrizes, documentação e padrões de navegação e consulta. Os demais critérios e os quatro resultados foram aceitos em R4, subordinados a essas duas correções. |
| **R2 · Resolvido** | Incorporar cada afirmação conforme seu alcance e sua natureza. A revisão técnica e as evidências sustentam o comportamento atual. Hipótese continua identificada como tal; uma regra nova aprovada para o futuro permanece decisão de produto. Um aceite parcial alcança apenas a parte expressamente aceita. |
| **R3 · Fluxo de autorização definido** | No escopo de escrita do conhecimento discutido, o usuário atribui autoridade de escrita a todos e o agente deve solicitar autorização ao Analista. Se obtida, efetiva a escrita no escopo permitido. Sem resposta, registra pendência. Diante de negativa, descarta a incorporação proposta. Não transformar a negativa em pedido pendente nem apagar o original ou uma lacuna factual independente. Destinos cruzados, alcance sobre atualizações obrigatórias e efetividade das permissões técnicas são questões distintas. |
| **R5 · Adiamento expresso** | Estrutura concreta do Micro fica para refinamento posterior. O exemplo navegável da edição 7 é material ilustrativo. Não prova que o layout foi escolhido, que existe agente consumidor implementado ou que o Motor precisa ensaiar o percurso para encerrar a produção. |
| **R6 · Conduta durante conflito definida** | Catalogar a divergência na camada e no ponto envolvidos. Em toda atividade que dependa dela direta ou indiretamente, o agente deve apresentar claramente o conflito, os detalhes, as instruções e as referências pertinentes. O primeiro aviso segue a regra já decidida. As partes independentes do trabalho podem continuar. A manifestação não estabelece quem ou que evidência encerra uma divergência irredutível, nem como uma nova declaração adquire vigência. |
| **R7 · Resolvido no uso da Plataforma** | O catálogo é legível por qualquer pessoa independentemente de sua Sigla. A leitura da entrada da raiz e a leitura ou escrita em um repositório referenciado são operações distintas. Não se infere publicação na internet, concessão de credencial ou alteração efetiva de controles corporativos. |
| **R8 · Aceito funcionalmente** | Se as atribuições dos Mesos mudarem, identificar a origem e a revisão, explicitar o alcance da divergência e a última situação verificável, invalidar o uso como atual do que mudou, reconciliar e verificar antes de restaurar a validade. A implementação da atualização e da concorrência segue em refinamento. |
| **R9 · Aceito funcionalmente** | A prova do pré-push precisa corresponder ao conteúdo exato enviado. Mudança posterior exige revalidação. Conferir semântica e referências: uma renomeação funcionalmente neutra que quebre o localizador exige reparo. Revalidação com evidência de ausência de impacto continua admitida para os casos pertinentes. Efetividade em clientes externos, composições multirrepositório e controles corporativos requer especificação e comprovação por profissionais autorizados. |
| **R10 · Sem decisão nova** | A resposta repetiu o título. A decisão anterior de adiar P03.20 e C-P03-07 permanece. Não foram definidos ensaios, métricas, executores ou aprovadores. |

**Saldo funcional das 22 originais.** 20 resolvidas (P03.1–P03.19 e P03.21), P03.22 com direção funcional aceita e desenho concreto postergado, P03.20 adiada. Os oito desdobramentos C-P03 mantêm sete respostas de direção/escopo e C-P03-07 adiada. Os pontos entre escrita, conflito, interação e publicação abaixo têm acompanhamento próprio, sem reabrir os 20 itens funcionais.

### Definition of Done do produtor · redação corrigida

**Uma execução do onboarding termina quando o Motor produz, para o repositório e o estado examinado, a base conforme os requisitos vigentes, demonstra a cobertura, a proveniência e a integridade dos resultados e registra claramente o que permaneceu insuficiente.** O recorte é determinado pelo material indicado, revisão e acesso autorizado. O objetivo permanente é a produção da base. O objetivo particular de uma consulta surge depois.

| Critério | Evidência mínima de cumprimento no recorte |
|---|---|
| **1. Identificar a entrada** | Identificar os repositórios, revisão ou estado local examinado, fontes acessíveis e fronteiras da autorização. A identificação diferencia o commit-base das alterações locais incluídas na análise. |
| **2. Demonstrar a cobertura de descoberta** | Confrontar as fontes pertinentes à natureza do repositório, como rotas, filas, agendamentos, infraestrutura, configuração, testes e contratos. Indicar o destino dos indícios materiais e o material inacessível ou fora do recorte. |
| **3. Compreender os comportamentos materiais** | Registrar responsabilidades, condições, decisões, alternativas, exceções, ausência de ação, efeitos e fronteiras externas sustentadas pelas fontes. Delimitar o lado efetivamente observado nas integrações. |
| **4. Consolidar o conhecimento válido** | Explicar o conhecimento material, ou apontar a fonte canônica que já o explicita suficientemente. Manter identificados aspectos inconclusivos, sem promover hipóteses a fatos nem adiar silenciosamente algo material e suficientemente validado. |
| **5. Conferir rastreabilidade e coerência** | Dos indícios e comportamentos encontrados chegar à unidade, evidência ou ressalva; de cada afirmação voltar à fonte da revisão correspondente. Conferir contradições, condições omitidas e referências quebradas. Uma verificação estrutural do produto gerado faz parte da produção. |
| **6. Tratar lacunas** | Catalogar e comunicar as lacunas assim que percebidas. Classificar se elas afetam a capacidade de produzir uma base fiel ou delimitar o que se compreendeu; quando a criticidade permanece incerta após as tentativas autorizadas, solicitar esclarecimento ao Engenheiro. O impacto sobre uma futura pergunta é avaliado pelo componente de interação quando ela existir. |
| **7. Entregar o resultado** | Produzir os artefatos Micro/Meso pertinentes conforme o contrato de saída, com identidades, revisões, referências, alcance, ressalvas e situação efetiva de entrega ou publicação. A estratégia de recuperação do consumidor e uma consulta bem-sucedida por outro agente ficam fora da condição de encerramento do produtor. |

**Estados aceitos, lidos com a retificação.** Concluído no recorte quando os critérios aplicáveis estão demonstrados; concluído com ressalvas quando as lacunas ficam delimitadas e não impedem a produção fiel no recorte; parcial/impedido na parte em que falte suporte indispensável à produção ou à delimitação da cobertura; aguardando esclarecimento quando a criticidade material da produção continua incerta. A preparação, a publicação e a validade de cada composição mantêm estados verificáveis próprios.

**Exemplo sintético.** Durante o onboarding, A demonstra que envia um campo a C. C não foi selecionado e o Motor não tem evidência de como ele lida com o campo ausente. O Motor conclui A com a ressalva documentada no próprio A nas condições já aceitas. Dias depois, uma pessoa pergunta ao agente se pode remover esse campo. O componente de interação recupera a evidência e identifica qual decisão depende de C. A pergunta posterior pode ficar impedida embora a produção original esteja concluída com ressalva. Se a fonte de A mudou, os critérios de atualidade se aplicam à revisão pertinente.

### Questões que ainda mudam o comportamento

| ID editorial | Questão, exemplo e recomendação para decisão |
|---|---|
| **S1 · Alcance da autorização de escrita de R3** | Foi definida para a incorporação do novo entendimento. Falta decidir se a mesma solicitação ao Analista vale também para produção inicial, correções documentais obrigatórias e atualização derivada Meso/raiz, e se uma autorização pode abranger os destinos de um mesmo ato. Exemplo: uma mudança adiciona “prioritária” à condição de publicação; o Analista nega a incorporação e a nova regra deixaria a base desatualizada. Recomendação: descartar o pedido negado, manter a negativa distinta de uma pendência de aprovação e não liberar o push do estado inconsistente. Delimitar no pedido os efeitos e destinos autorizados. Se o controle corporativo impedir uma escrita autorizada em produto, registrar o obstáculo operacional e retomar pela via autorizada. |
| **S2 · Aprovação, destino e Analista competente** | “A explicação está correta” valida o entendimento; “está correta e pode gravá-la no Micro de A” também autoriza uma escrita identificada. Falta definir quem autoriza quando a atividade é de uma Sigla e o destino de outra e como se escolhe o destino de conclusões de uso misto. Proposta: uma autorização expressa que já identifique o destino evita nova confirmação para o mesmo ato. Preservar a origem principal por fato; usar Workspace para decisões próprias da atividade, Micro para comportamento reutilizável de A, Meso/raiz para suas responsabilidades e referências. Permissões reais continuam por operação e repositório. |
| **S3 · Vigência e encerramento das divergências do catálogo** | Qualquer pessoa pode ser origem da declaração e o conflito deve ser apresentado nos usos afetados. Resta o ciclo antes e depois da sinalização. Uma nova atribuição sem conflito conhecido pode ser usada de imediato como declarada? Que esclarecimento ou autoridade permite resolver duas alegações contraditórias sobre a mesma etapa? Exemplo: duas Siglas podem participar de fases distintas; só há contradição se as declarações forem incompatíveis para o mesmo objeto e período. Proposta: manter as duas origens e revisões enquanto houver conflito, admitir esclarecimento com escopo e evidência e revalidar os consumidores autorizados. Onde a contradição for irredutível, falta definir quem pode decidir ou se ela permanece expressamente em aberto. |
| **S4 · Refinamento dos componentes, já encaminhado** | Definir posteriormente o contrato estrutural do Micro e a interface com o componente de interação: quais saídas o produtor garante e quais regras, instruções e skills o consumidor usa para consultar, aprofundar, reapresentar pendências e propor enriquecimentos. O fluxo funcional de enriquecimento já é desejado; divisão física, nome do componente e implementação ficam abertos. |
| **S5 · Verificação operacional e avaliação, já encaminhadas** | Demonstrar integridade dos índices e revisões, recuperação após escrita parcial e cobertura efetiva do controle pré-push nos caminhos corporativos. Em P03.20/C-P03-07/R10, ficam reservados método, responsáveis, provas de qualidade e comparação de custo. Esses trabalhos técnicos não são condições adicionais para encerrar a entrevista funcional do onboarding. |

**Retomada.** Primeira questão material: delimitar a autorização de R3 quando o conhecimento precisa ser atualizado por uma mudança de código antes do push. Depois, resolver os casos de vários destinos e de conflito irredutível do catálogo. Permanecem o adiamento do desenho de P03.22 e o de P03.20/C-P03-07. **NÃO PERSISTIDO no GitHub.** [Motor e Workspaces](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md) · [Critérios anteriores de evidência e ressalvas](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md) · [Direções e autorizações herdadas](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md)

<a id="saldo-p03-r7"></a>

## P03 · Quinta rodada de respostas e DoD candidato do onboarding

**Edição de trabalho 7 · 8 de novembro de 2026.** A fonte direta são as sete respostas do usuário ao inventário da edição 6. O aceite por referência foi confrontado com a recomendação efetivamente apresentada. O DoD e o exemplar abaixo foram preparados pelo assistente para revisão. As decisões das edições anteriores continuam no histórico, com a precedência do saldo mais recente.

### Avaliação das sete respostas

| Resposta | Decisão vigente na conversa | Alcance pendente |
|---|---|---|
| **1 · P03.1** | O Motor busca a maior compreensão possível das fontes autorizadas. Se, depois do onboarding, uma pergunta levar o agente a investigar a base e o repositório e a produzir entendimento novo, a aprovação da resposta pelo Analista, no cenário descrito, deve levar à incorporação desse conhecimento validado. Ele passa a integrar o conjunto seguindo os mesmos critérios de origem principal, revisão, evidência, estrutura, navegação, axiomas e manutenção. | A resposta define o enriquecimento posterior. Continua em aberto a fronteira inicial entre explicar, referenciar uma fonte declarativa, deixar o detalhe no código e declarar uma lacuna. O que ainda não foi descoberto e o que foi descoberto mas adiado exigem tratamento próprio. |
| **2 · P03.2** | O usuário acolheu a direção das sugestões e solicitou uma definição de pronto rigorosa e detalhada. | O DoD abaixo é candidato. Seu aceite e o vínculo com a política de P03.1 continuam abertos. |
| **3 · P03.13** | A concordância alcança as aplicações propostas. Impeder a conclusão cujo objetivo exige uma fonte indisponível; remeter a criticidade incerta ao Engenheiro após a investigação autorizada; entregar o trabalho independente. Os dois aceites históricos de A com ressalvas permanecem limitados aos seus casos e condições. | **Resolvido no alcance funcional.** |
| **4 · P03.22** | “Ok” foi aplicado à sequência proposta: estabelecer as operações de localizar, explicar, conferir, editar a origem e identificar referências afetadas; mostrar um exemplar Micro/Meso com dois percursos; escolher a estrutura concreta depois disso. Há um exemplar ilustrativo nesta edição. | A utilidade do exemplar e as escolhas de unidades, formatos, pastas, índices e instruções não receberam aceite antecipado. |
| **5 · P03.20 e C-P03-07** | O “Ok” confirma reservar testes, responsáveis, referências esperadas, métricas e comparação de custo para etapa posterior. Os casos sugeridos continuam candidatos. | **Adiado por decisão expressa.** |
| **6 · Catálogo na raiz** | A primeira entrega inclui o catálogo de Siglas. Como conteúdo mínimo, o usuário indicou responsabilidades, escopo e domínio. Qualquer pessoa pode ser origem de autoridade para a informação. O catálogo acompanha mudanças nas camadas Meso e a leitura pretendida abrange todo e qualquer público. | Especificar efeito da declaração individual, arbitragem de declarações contraditórias, limite concreto do público e publicação de metadados legitimamente compartilháveis. A participação de várias Siglas num assunto não é, por si só, conflito. |
| **7 · Controle antes do push** | A concordância foi aplicada às sugestões do item 7. Avaliar o impacto semântico, tratar a revisão exata, tornar a verificar se o conteúdo mudou e abranger caminhos de envio e composições pertinentes. Interpreta-se que a revalidação registrada com evidência de ausência de impacto satisfaz o caso de mudança que não altera conhecimento. É um aceite por referência à proposta do inventário. | Implementação, autoridade e prova de cobertura de todos os caminhos de envio, inclusive clientes externos e múltiplos repositórios, exigem especificação e validação interna. A permissão de push e a aprovação formal do conhecimento são atos distintos. |

**Saldo das 22 questões originais.** 18 resolvidas (.3, .4, .5, .6, .7, .8, .9, .10, .11, .12, .13, .14, .15, .16, .17, .18, .19, .21), três parciais (.1, .2, .22), uma adiada (.20). Das oito colaterais originais, .01–.06 e .08 foram respondidas no alcance discutido; .07 está adiada. O catálogo, o requisito de pré-push e as questões abaixo são rastreados pelo assunto de origem, sem aumentar a contagem das perguntas originais.

### P03.1 · Enriquecimento posterior, sem perda da proveniência

Exemplo sintético: a base explica que um worker grava pedidos válidos e ignora duplicatas. Um Engenheiro pergunta o que acontece quando a gravação foi concluída, mas a confirmação de processamento falhou. A investigação autorizada localiza a chave de deduplicação e uma condição que trata reenvios. Se a lacuna exigir consulta posterior a material legado, valem o aviso e a permissão pertinentes. O Analista aprova a explicação no alcance daquela revisão. Propõe-se incorporar a nova regra na unidade principal sobre reprocessamento, com a evidência, o alcance aceito e referências vindas dos fluxos que dela dependem. Uma referência já existente deve ser atualizada ou complementada para evitar criar duas origens de edição.

Se o Analista declarar que a regra **deverá mudar no futuro**, a resposta pode registrar uma decisão ou intenção de produto. Para afirmar o que a aplicação **faz hoje**, permanece necessária evidência da revisão. O aceite não concede direitos adicionais de armazenamento ou redistribuição de uma fonte restrita. Um entendimento pertinente a uma única atividade pode ter seu destino no Workspace. A localização de uma regra compartilhável entre repositórios ou Siglas depende do conteúdo e dos públicos de destino.

Quatro situações distintas sustentam a próxima deliberação. **Ainda não descoberto:** incorporar quando a investigação produzir conhecimento validado. **Já percebido, mas inconclusivo:** catalogar, localizar e comunicar desde o primeiro momento. **Conhecido, verificável e material, porém caro de documentar:** falta definir se algum adiamento deliberado é permitido e sob quais condições. **Fora do escopo de acesso ou compartilhamento:** registrar somente a referência e o limite que o escopo permite. Uma aceitação parcial precisa conservar quais afirmações foram aceitas; proposta ou divergência permanece identificada até resolução.

### P03.2 · Definition of Done candidato, por repositório e revisão

**Objeto de conclusão.** Delimitar repositório, objetivo, revisão Git ou estado local realmente examinado, escopo autorizado e revisão do conhecimento produzido. No onboarding amplo, o objetivo proposto é explicar as responsabilidades e os comportamentos materiais do repositório, suas condições, relações, riscos e limites. O resultado de uma rodada pode ser posteriormente enriquecido. Se a nova evidência contradisser uma afirmação existente, aplicar o ciclo de invalidação e revalidação antes de apresentá-la como atual.

| Verificação proposta | Evidência que o Motor precisa entregar | O que impede passar nessa verificação |
|---|---|---|
| **1. Identidade e escopo** | Objetivo declarado, identificação das fontes admitidas e efetivamente obtidas, commit e, se pertinente, alterações locais que compõem o estado analisado. | A afirmação mistura uma branch móvel, arquivos locais ou um ambiente sem identificar qual fonte a sustenta. Se o material mudar durante a rodada, fixar o recorte entregue e reconciliar antes de alegar atualidade sobre a nova revisão. |
| **2. Descoberta e cobertura** | Inventário por natureza aplicável e confronto de fontes disponíveis que possam revelar caminhos diferentes: rotas, consumidores, agendamentos, Terraform/configuração, contratos, persistência, testes, documentação e dependências. Dar destino aos indícios encontrados e registrar áreas não lidas e os motivos. | O Terraform declara uma rotina periódica que não aparece na análise nem como lacuna. O Motor ainda precisa seguir ou explicar esse indício antes do encerramento. Um repositório de infraestrutura é examinado por recursos, dependências e efeitos próprios. |
| **3. Caminhos materiais** | Para cada fluxo identificado, ligar gatilho e condições aos dados, decisões, efeitos, destinos, alternativas, falhas e ausência de ação que possam mudar a conclusão. Identificar o lado efetivamente examinado quando houver relação externa. | A base afirma que A sempre publica, embora exista um ramo em que a proposta cancelada se encerra sem publicação. Um ramo ainda não explicável exige ressalva explícita e avaliação de criticidade. |
| **4. Cobertura documental** | Cada comportamento material encontrado tem explicação, referência canônica suficiente ou lacuna identificada. A proposta de P03.1 permite manter mecânica interna no código quando sua omissão preserva as conclusões materiais. | Um contrato ou uma regra aparece no inventário, mas não se consegue localizá-lo a partir do Micro nem descobrir qual lacuna explica a ausência de cobertura. A suficiência de referência sem materialização ainda depende de aceite em P03.1. |
| **5. Conferência em dois sentidos** | De cada comportamento material descoberto chega-se à explicação, referência ou lacuna. De cada afirmação material chega-se ao suporte localizável na revisão estudada, incluindo contraevidência quando existir. Se uma condição muda o resultado, confrontar as descrições dos caminhos distintos. | A base cita um teste escrito como prova de execução, omite uma exceção sustentada ou atribui a produção algo observado apenas no código. Um mesmo problema já registrado pode ser referenciado em várias unidades sem duplicação. |
| **6. Lacunas e decisão de fechamento** | Para cada pendência percebida, registrar e comunicar assim que identificada a fonte, alcance, ação afetada, trabalho independente e ponto de retomada. Antes de concluir, verificar se ainda há indício material sem investigação ou destinação e aplicar o critério de P03.13. | Há questão indispensável ao objetivo sem resposta, ou criticidade que continua incerta após investigação autorizada. No primeiro cenário, o objetivo dependente está impedido; no segundo, aguarda esclarecimento. Não impedir entregas independentes. |
| **7. Entrega recuperável** | Micro utilizável a partir da entrada da revisão pertinente; Meso encaminha ao repositório correto e reflete a cobertura/resultado da rodada no escopo autorizado. Indicar revisões, ponteiros aplicáveis, situação de entrega/publicação, limitações e próxima ação. No caso aceito de A, a ressalva tem de permanecer definida e referenciada no próprio A. | A conclusão só existe no chat, o material aponta para outra revisão, ou o Meso é apresentado como atualizado sem evidência. O Micro pode estar preparado localmente enquanto publicação ou composição precisam de providência; distinguir esses resultados. |

**Regras para parar.** Encerrar a investigação daquele recorte quando todo indício material conhecido recebeu destino verificável, a conferência em dois sentidos foi atendida e o efeito das lacunas sobre o objetivo está delimitado. Nenhum percentual de arquivos, tokens, duração ou confiança verbal substitui essas condições. Cada verificação se aplica conforme a natureza do repositório; itens fora do escopo têm justificativa. Quando uma verificação não pode ser demonstrada, explicitar em que parte o trabalho está incompleto. Não se exige provar a inexistência de todo comportamento ainda desconhecido.

| Resultado candidato | Critério |
|---|---|
| **Concluído no recorte** | Critérios aplicáveis atendidos, material recuperável e sem ressalva material pendente para o objetivo declarado. |
| **Concluído com ressalvas** | Lacunas percebidas foram comunicadas e documentadas e ficaram delimitadas como não impeditivas para esse objetivo. Indicar cada ação que continua dependente. |
| **Parcial / objetivo dependente impedido** | Falta explicação indispensável ou verificação essencial ao objetivo. Entregar a parcela sustentada e indicar a evidência que permitiria retomar. |
| **Aguardando esclarecimento** | Não foi possível determinar a criticidade após investigar as fontes autorizadas. Formular a menor pergunta ao Engenheiro; o trabalho independente pode prosseguir. |

**Caso de aplicação.** A API e o worker de propostas já estão explicados. O Terraform revela uma rotina noturna de expiração. Enquanto essa pista estiver sem destino, o onboarding amplo ainda não atende ao critério de cobertura. Ao localizar o handler e comprovar que a rotina cancela propostas expiradas, o Motor passa a poder explicar o fluxo. Se o prazo vigente de HOM está inacessível, o onboarding amplo pode concluir com ressalva quando o valor específico não for indispensável ao objetivo e todos os demais critérios forem atendidos. Um pedido para determinar em quantos dias uma proposta será cancelada em HOM permanece impedido nessa conclusão. O mesmo conjunto de fontes produz resultados diferentes porque os objetivos são diferentes.

O DoD é uma proposta de regra de produto para cada execução. Sua aplicação não presume forma física aprovada, aprovação de rotina de todo onboarding pelo Analista, publicação remota, autorização de execução local nem validação operacional do Motor. A escolha de testes formais, avaliadores e indicadores permanece em P03.20.

### P03.22 · Exemplar mínimo de consulta e de edição

Dados, caminhos de arquivo e revisões são fictícios. As ligações abaixo são navegáveis dentro deste caderno e ilustram responsabilidades lógicas. A estrutura de arquivos do produto permanece por escolher.

<a id="ex7-meso"></a>

**Meso Alfa · revisão m1.** A responsabilidade “receber propostas e encaminhar o resultado da análise” remete ao [Micro de A, revisão a1](#ex7-micro).

<a id="ex7-micro"></a>

**Micro de A · revisão a1.** Pergunta pontual “quanto tempo A aguarda a análise?” remete à [configuração de espera](#ex7-config). Pergunta de edição “onde mudar a publicação de proposta cancelada?” remete à [regra de encaminhamento](#ex7-regra).

<a id="ex7-config"></a>

**Configuração de espera · origem editável da explicação do parâmetro.** A espera padrão nesta revisão é de 2 segundos e pode ser substituída por TIMEOUT_MS. Fonte sintética: A@a1, application.yml, seção analise.timeout. Um valor efetivo de ambiente requer evidência correspondente. [Voltar à entrada](#ex7-micro).

<a id="ex7-regra"></a>

**Regra de encaminhamento · origem editável da explicação da regra.** Na resposta PENDENTE, proposta ativa passa a AGUARDANDO e gera evento de revisão. Proposta cancelada registra o motivo e se encerra sem produzir esse evento. Fonte sintética: A@a1, TratadorDeAnalise.kt, método tratarPendente. Uma mudança nessa condição requer examinar [o uso da regra pelo fluxo e a referência no Meso](#ex7-impacto).

<a id="ex7-impacto"></a>

**Impacto da edição.** O fluxo encaminha o agente à definição principal da regra. A descrição do evento exige revalidação se o contrato do evento mudar; uma referência que permanece válida pode ser revalidada. O timeout tem origem independente. A composição deve mostrar a revisão de Micro pertinente no [Meso](#ex7-meso). Este exemplo testa a ideia em papel e não se atribui aprovação ao layout ou à execução de um ensaio.

### Inventário das questões remanescentes ou decorrentes

A numeração abaixo é editorial desta edição. Não acrescenta itens à contagem original de P03. Quando houver resposta suficiente na pergunta-mãe, o desdobramento pode ser encerrado junto.

| ID | Objeto e decisão residual | Recomendação ou limite |
|---|---|---|
| **R1 · P03.1** | Um contrato canônico versionado, legível e suficiente pode ser consultado por referência ou os seus dados precisam de projeção dentro do Micro? Em quais casos um entendimento já conhecido e material pode ser deliberadamente adiado? | Aceitar referência quando ela responder diretamente; explicar no Micro toda consequência material que exija interpretação. Admitir adiamento explícito apenas se a lacuna registrada não impedir o objetivo. |
| **R2 · Origem do conhecimento novo** | Quando o Analista aprova uma resposta com uma parte comprovada, uma hipótese e uma nova diretriz, qual parte se incorpora, em que natureza e para que revisão ou atividade? O que acontece se a aprovação for parcial, faltar ou houver discordância? | Transformar em afirmações delimitadas. Incluir o que foi validado na natureza pertinente, preservar candidatos/lacunas e reconciliar conflito com a fonte. O novo exemplo não estabelece exclusividade do Analista para toda atualização técnica. |
| **R3 · Destino e autorização** | Como decidir se o entendimento novo é local ao Workspace, reutilizável no Micro, compartilhado pelo Meso ou transversal, e como encaminhá-lo se o agente não puder escrever no destino? | Atualizar ou propor mudança na origem principal, propagar somente aos destinos legitimamente autorizados e conferir revisão e referências; manter estado pendente onde a incorporação não puder ser efetivada. |
| **R4 · DoD** | As sete verificações e os quatro resultados acima bastam para declarar o onboarding no recorte? Como registrar critério não aplicável, indício não examinado e Micro pronto com Meso pendente? | Rever o exemplo da rotina noturna. Manter os estados de investigação, entrega, publicação e validade distinguíveis. Proposta ainda sem aceite. |
| **R5 · Estrutura do Micro** | Os percursos sintéticos atendem às necessidades do agente? Quais responsabilidades merecem unidades separadas quando a regra é compartilhada por vários fluxos? | A engenharia deve propor a materialização após a revisão dos percursos. Formatos, diretórios, índices, reconhecimento do estado local e adaptadores permanecem técnicos. |
| **R6 · Catálogo e autoridade** | O registro de qualquer pessoa passa a valer diretamente ou entra com autoria e revisão para reconciliação? Quem decide quando duas declarações incompatíveis disputam o mesmo domínio na mesma finalidade? | Preservar contribuição de qualquer pessoa e sua proveniência. Permitir múltiplas Siglas candidatas quando o produto ou a etapa justificar e escalar somente contradição material não resolvível pelas fontes. |
| **R7 · Catálogo e público** | “Todo e qualquer público” alcança todo o público que usa a Plataforma no ambiente corporativo ou também públicos externos? Quais metadados estão legitimamente liberados para a amplitude pretendida? | O índice amplo pode expor a descrição autorizada de uma responsabilidade. Código privado, conteúdo do Meso, links sensíveis e credenciais mantêm direitos próprios. A intenção de acesso não é prova de publicação ou autorização corporativa efetiva. |
| **R8 · Atualização da raiz** | Quando dois Mesos mudarem ao mesmo tempo, um ficar inacessível ou uma atribuição for retirada, qual revisão da raiz pode voltar a ser usada como atual? | Reaproveitar a regra de invalidação, reconciliação e verificação. Tratar apenas as entradas afetadas, explicitar origem, revisão, indisponibilidade e último estado verificável. O mecanismo e o gatilho operacional ficam com P04. |
| **R9 · Pré-push** | Como comprovar ausência de impacto, validar referências que podem quebrar mesmo sem mudança funcional, abranger envios fora do Motor e reconhecer composição parcial em vários repositórios? | Prova vinculada ao conteúdo exato; mudança posterior invalida a prova. Ensaiar uma mudança real de regra e uma renomeação que quebre um localizador. Validação dos controles corporativos só no ambiente autorizado. |
| **R10 · Avaliação adiada** | Métodos, executores, resultados de referência e limites de qualidade/custo por modalidade ainda serão definidos. | Manter P03.20/C-P03-07 reservadas, incluindo um pedido simples, um multicomponente e um caso em que a resposta correta é reconhecer evidência insuficiente. |

**Sequência de retomada.** Delimitar R1 para evitar que uma regra descoberta e relevante seja omitida ou duplicada; em seguida rever o DoD proposto em R4 e o exemplar de R5. Os refinamentos de catálogo e de controle de envio seguem seus vínculos com as frentes de acesso, atualidade e publicação. **NÃO PERSISTIDO no GitHub.** [Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md) · [Motor e Workspaces](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Autoridade e revalidação](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md) · [Casos aceitos de A](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md)

<a id="pendencias-restantes-p03"></a>

## P03 · Inventário para responder ao que resta

**Edição de trabalho 6 · 8 de novembro de 2026.** Esta edição organiza o saldo da edição 5 para a entrevista. O pedido de inventário não trouxe novas decisões de produto. A base oficial de comparação continua no commit identificado na abertura. Exemplos e recomendações desta seção são propostas de refinamento.

| Momento e objeto | IDs ou tema | Quantidade |
|---|---|---:|
| Perguntas originais com definição parcial | P03.1, P03.2, P03.13 e P03.22 | 4 |
| Pergunta original adiada | P03.20, com a colateral C-P03-07 | 1 |
| Assuntos que surgiram na rodada e atravessam outras frentes | Catálogo temático da raiz e garantia documental anterior a todo push | 2 assuntos relacionados |
| Perguntas originais encerradas no alcance funcional | P03.3, .4, .5, .6, .7, .8, .9, .10, .11, .12, .14, .15, .16, .17, .18, .19, .21 | 17 |

Das oito colaterais, C-P03-01 a 06 e C-P03-08 foram respondidas no alcance em que surgiram. C-P03-07 é a comparação de custo adiada. A estrutura concreta do Micro e a implementação do controle anterior ao push conservam seu próprio trabalho técnico. O mapa das outras frentes no início do caderno continua disponível para as rodadas correspondentes.

### 1 · P03.1 — Fronteira de um fato individual

**Já definido.** Tipos de informações a recuperar sobre integrações HTTP, filas e banco, profundidade do exemplo da proposta ativa/cancelada, origem principal de edição por fato e rastreabilidade à revisão. O Micro será uma coleção navegável de documentos complementares.

**Decisão que falta.** O critério baseado na consequência de omitir um fato é suficiente para escolher entre explicar no Micro, apontar uma fonte, preservar o detalhe exclusivamente no código e declarar uma lacuna? Em especial, quando um contrato já contém uma resposta completa, uma rota precisa e autorizada até ele atende ao requisito de o agente não precisar reconstruir o conhecimento?

| Caso sintético | Encaminhamento sugerido e impacto |
|---|---|
| Um serializador omite um campo quando o valor é nulo. | Explicar a omissão e sua condição no Micro. Um leitor que esperar o campo presente pode avaliar incorretamente a compatibilidade com o consumidor. O corpo do método continua localizável no código. |
| Uma API tem 60 campos legíveis em contrato canônico. Dois só são obrigatórios para pessoa jurídica. | Referenciar a operação, a revisão e o esquema. Explicar a condição se ela exigir interpretação de mais de uma fonte. Se a fonte já a expressar claramente, a referência exata pode bastar. Outra opção é uma projeção verificável de mesma origem se o acesso direto ao contrato não atender ao uso pretendido. |
| Um helper privado foi dividido em dois sem alteração material nas respostas da aplicação, nas permissões ou nos limites operacionais. | Deixar a divisão interna no código. Acrescentar uma ficha individual gera manutenção sem modificar a explicação da regra. |
| As fontes lidas não permitem saber se uma operação pode ser repetida sem produzir duplicidade. | Registrar a lacuna e indicar a ação afetada. A consulta dirigida à fonte cabe se a dúvida for material, houver contradição, revisão alterada ou necessidade de sustentar uma modificação, sob as autorizações vigentes. |

**Fechamento proposto.** Aceitar a regra de quatro destinos, incluindo quando a referência canônica basta, ou explicitar um contraexemplo que exija outro tratamento. A edição física das informações pertence a P03.22.

### 2 · P03.2 — Cobertura suficiente para entregar o Micro de um repositório

**Já definido.** O Motor deve abarcar os aspectos e unidades de conhecimento tanto quanto possível. A abrangência inclui responsabilidades, regras, entradas, saídas, integrações, infraestrutura, configurações e meios de verificação pertinentes. Declara o que conseguiu examinar e as limitações identificadas.

**Decisão que falta.** Quando o pedido é apenas “faça o onboarding”, que evidência de cobertura permite encerrar aquela execução? A política de P03.1 orienta o tratamento de algo que o agente encontrou. Aqui importa também o risco de ele nunca encontrar uma entrada ou caminho importante.

**Exemplo.** Um repositório tem uma API que recebe propostas, um consumidor que processa reenvios e uma rotina noturna que cancela propostas expiradas. A API está muito bem explicada. Se a investigação começou e terminou nela, o Micro pode induzir outro agente a acreditar que uma proposta só é cancelada na API. Se o Motor identificou o agendamento, mas parte de sua configuração estava inacessível, o resultado precisa mostrar o que está comprovado e qual explicação ainda falta.

**Recomendação para deliberação.** Fixar fontes e revisão; inventariar entradas, saídas, recursos e responsabilidades encontradas; seguir caminhos que mudam o resultado, inclusive falha e ausência de ação. Ao encerrar, associar cada efeito material encontrado a uma explicação, referência suficiente ou lacuna. Em sentido inverso, conferir a fonte de cada afirmação material. Uma lacuna indispensável ao objetivo impede a conclusão correspondente, conforme P03.13. A entrega explicita o universo realmente examinado. Em situações fora da cobertura, o agente pode propor o aprofundamento cabível. A escolha de um total corporativo de repositórios da Sigla já foi dispensada.

**Impacto.** Sem um ponto de encerramento observável, a análise pode parar depois do primeiro fluxo ou consumir tempo crescente sem produzir uma conclusão mais segura. Falta validar este modo de demonstrar a cobertura para repositórios com perfis diferentes, como API, worker e infraestrutura.

### 3 · P03.13 — Aplicação da criticidade ao objetivo

**Já definido.** Uma lacuna é impeditiva se inviabiliza uma explicação indispensável ao objetivo ou impede delimitar com segurança o que foi compreendido. A incerteza material que persiste após a investigação autorizada chega ao Engenheiro. O restante independente pode prosseguir.

| Classificação e estado | Caso e ação |
|---|---|
| **Ressalva controlada · caso aceito** | A emite um campo para B e C, e há evidência sobre a emissão e o tratamento em B. A aceitação de campo ausente em C está desconhecida. Com a ressalva nas condições já decididas, A pode concluir seu onboarding. Retirar o campo depende de C. O segundo aceite histórico, sobre duas regras de segmento com seleção incerta, também permanece vigente no seu alcance. |
| **Impedimento · aplicação proposta** | O objetivo declarado é explicar por que uma proposta foi aprovada ou recusada. A só encaminha o resultado de um serviço de decisão inacessível. O Motor entrega a explicação do encaminhamento. A conclusão sobre o critério de aprovação fica impedida até haver fonte autorizada. Se o objetivo fosse apenas explicar o papel de A, a mesma ausência teria alcance diferente. |
| **Criticidade incerta · aplicação proposta** | O Engenheiro pede o “fluxo padrão”. O código evidencia um caminho automático e outro de revisão manual para um canal. Após investigar, continua incerto se aquele canal faz parte do objetivo da atividade. O agente mostra os dois caminhos e pergunta se a análise precisa abranger esse canal. |

**Decisão que falta.** Validar se o segundo caso deve impedir especificamente a explicação da aprovação e se o terceiro pede esclarecimento de escopo antes de declarar a análise suficiente. A consequência é evitar tanto uma conclusão sem evidência quanto a interrupção desnecessária do trabalho independente.

### 4 · P03.22 — Estrutura e percursos de leitura e edição

**Já definido.** O conhecimento será organizado para pessoas e agentes, com documentos complementares relacionados por natureza e finalidade. Cada fato terá uma origem principal para edição. O agente deve conseguir navegar, compreender, explicar e modificar dentro de seu escopo autorizado. A primeira entrega se apoia no Motor e nas ferramentas suportadas, sem uma interface gráfica própria.

**Decisões que faltam.** Definir como reconhecer a entrada da base e a revisão a que pertence; o que constitui uma unidade separada; onde localizar a definição editável de cada regra, a evidência e as exceções; quando seguir uma referência ou carregar outra unidade; e como realizar esses percursos ao abrir uma cópia local ou uma revisão em Git. A arquitetura documental deverá concretizar o formato ou composição de formatos, a granularidade dos arquivos, as referências e as instruções específicas de ferramenta que forem necessárias para as bases comuns.

**Exemplo de leitura e de edição.** Um agente quer apenas saber o timeout de uma API. Outro precisa alterar o tratamento de “proposta cancelada” e identificar os demais materiais atingidos. A entrada deve permitir ao primeiro chegar rapidamente ao parâmetro e ao segundo encontrar a origem da regra, a condição, os efeitos, a fonte e os consumidores conhecidos daquela informação. Um conjunto muito fragmentado exige abrir muitos documentos para explicar uma regra. Um arquivo extenso aumenta o custo de uma consulta simples. Uma explicação duplicada cria risco de apenas uma cópia ser corrigida.

**Recomendação para deliberação.** Concordar primeiro com as operações que o agente deve conseguir realizar: localizar, explicar, conferir, editar a origem e identificar as referências afetadas. À engenharia cabe apresentar um exemplar de Micro com os dois percursos e um Meso que encaminhe ao Micro correto. Só então selecionar entre Markdown, registros estruturados ou composição, pastas, nomes, índices e possíveis projeções geradas.

**Detalhamento de engenharia relacionado.** Já está decidido estudar a cópia local indicada. Falta representar com precisão quais alterações autorizadas e arquivos novos pertenciam ao estado estudado. Se o commit previa três tentativas e o estado local prevê cinco, outro agente precisa reconhecer qual fonte sustenta cada número. A escolha do mecanismo de identificação pode aguardar a especificação técnica.

### 5 · P03.20 e C-P03-07 — Como demonstrar qualidade e custo, na etapa reservada pelo usuário

**Decisão de sequência.** O usuário adiou testes, métodos, responsáveis e critérios quantitativos. A colateral de custo participa da avaliação e também informa a escolha de estrutura em P03.22. A entrevista pode seguir antes dessas definições.

**O que faltará especificar.** Quais tarefas e revisões comporão o ensaio; quem estabelece o resultado esperado, quem executa e quem valida; o que comprova precisão, segurança, recuperação da evidência e capacidade de reconhecer uma lacuna; e como comparar tempo, contexto, tokens ou ACUs quando disponíveis por ferramenta.

**Exemplo e impacto.** A base X permite encontrar o timeout com uma leitura, mas exige abrir várias unidades para explicar falha e reenvio. A base Y resolve o fluxo complexo numa leitura maior e traz informação demais para a consulta simples. Uma comparação representativa precisa de ambos os pedidos e de um caso em que a resposta correta seja admitir falta de evidência. Uma estrutura que perca uma exceção material já falha na qualidade do conteúdo. Entre as que preservam essa exceção, representar usos reais ajuda a decidir qual custo é aceitável. A recomendação é guardar esses casos como candidatos e não presumir hoje limiar, aprovador, ferramenta ou resultado.

### Assunto relacionado A · Catálogo de responsabilidades das Siglas na raiz

O Meso já tem a função de encaminhar uma dúvida para os repositórios pertinentes **dentro de uma Sigla conhecida**. O usuário propôs que a raiz encaminhasse o assunto para uma ou mais Siglas candidatas **quando a Sigla ainda é desconhecida**. A inclusão do catálogo na v1 permanece uma decisão de escopo.

**Exemplo e impacto.** “Abertura de contas” levaria a NC2 e depois aos Micro adequados. Quando duas Siglas participam de produtos semelhantes, um encaminhamento único sem justificativa pode esconder a segunda. Um índice amplo também pode expor, pelo próprio texto, metadados de um componente restrito.

**Decisões condicionais.** Se o catálogo entrar, definir a menor entrada útil por Sigla, a fonte com autoridade para declarar a responsabilidade, quem a mantém, como tratar sobreposição ou mudança de atribuição e o público que pode descobrir os metadados. A identidade física da raiz com o Macro segue em P01. O índice obrigatório dentro do Meso já foi decidido. Uma consulta adicional por relação técnica no Meso permanece uma possibilidade sujeita a demonstrar utilidade.

**Recomendação.** Deliberar primeiro sobre o percurso “assunto → Sigla → repositório”. Um exemplo sintético com duas Siglas pode mostrar se o catálogo merece entrar na v1 antes de desenhar sua estrutura.

### Assunto relacionado B · Garantia documental antes de todo push

O requisito é expresso: a atualização documental pertinente deve anteceder todo push, e todo dado cujo significado tenha mudado deve acompanhar a alteração. O estudo da cópia local antes do envio já foi definido. O saldo agora é **como demonstrar e aplicar essa garantia**.

| Ponto pendente | Exemplo e consequência | Encaminhamento sugerido |
|---|---|---|
| Evidência de impacto semântico | A regra passa de “proposta ativa” para “proposta ativa e prioritária”. Alterar apenas uma vírgula no Markdown faria um controle superficial passar. | Ligar o comportamento alterado, as unidades atingidas e a respectiva verificação ao conjunto exato de mudanças candidato ao envio. |
| Mudança sem impacto documental | Renomear uma variável privada pode preservar todos os comportamentos relevantes. | Deliberar se uma revalidação registrada como “sem impacto”, com evidência, atende ao requisito naquele caso. Isso ainda não foi aceito como exceção. |
| Mudança posterior à validação | O controle conferiu a versão com três tentativas; antes do envio, o código passou para cinco. | Tornar verificável qual conteúdo passou e exigir nova conferência se o conteúdo candidato mudar. |
| Outros clientes e múltiplos repositórios | Um desenvolvedor pode usar um cliente Git fora do Motor. Um Micro pode mudar enquanto o Meso continua apontando a revisão anterior. | Especificar quais controles autorizados cobrem todos os caminhos de envio e como verificar a composição pretendida por commits e ponteiros. Composição parcial deve ser identificável e o fechamento lógico dependente permanece aberto. |

**Limite da prova.** Uma barreira determinística pode comprovar que os controles definidos passaram para determinado estado. A fidelidade semântica exige examinar as afirmações e suas evidências. A cobertura dos caminhos fora do Motor depende de verificação no ambiente corporativo autorizado. Desenho do mecanismo, integração e provas ficam para a engenharia; a definição sobre aceitar a revalidação sem mudança de significado é uma questão de produto.

### Ordem sugerida e continuidade

Deliberar sobre P03.1, aplicar a política no onboarding completo de P03.2, confirmar os casos de P03.13 e então definir o exemplar navegável de P03.22. O catálogo da raiz e a aceitação de revalidação sem impacto podem ser tratados separadamente. P03.20/C-P03-07 permanece na etapa posterior escolhida pelo usuário.

A solicitação desta edição foi apresentar o saldo. As recomendações acima não alteram o status dos 22 itens. **NÃO PERSISTIDO no GitHub.** O registro da quarta rodada, as fontes e a história das perguntas aparecem a seguir.

<a id="saldo-p03-r5"></a>

## P03 · Quarta rodada e critério proposto para o conteúdo do Micro

**Edição de trabalho 5 · 8 de novembro de 2026.** Fonte desta rodada: manifestação direta do usuário sobre P03.1/.2, P03.14, C-P03-06 e C-P03-04. O critério de classificação a seguir é uma proposta do assistente para deliberação. Os exemplos são sintéticos.

### Saldo da rodada

| Item | Registro e alcance |
|---|---|
| **P03.1/.2 · Fronteira do conhecimento** | O usuário imagina documentos complementares, interligados e separados por natureza, objetivo, finalidade e conteúdo. Um único AGENTS.md na raiz não é o modelo pretendido. Não há definição de arquivos, nomes, formatos, hierarquia, tamanho, nem de um AGENTS.md obrigatório. Segue aberta a política para estabelecer o que explicar, referenciar ou deixar exclusivamente no código. O aceite dos dois caminhos de A e a direção de máxima cobertura possível permanecem válidos. |
| **P03.14 · Resolvido** | O Motor da primeira entrega pode interpretar a evidência de ambiente que o Engenheiro forneça por via autorizada. Segundo o usuário, a pipeline dos repositórios em questão faz com que a release branch mais recente identifique a versão atual do código em homologação. Entre release/v0.0.1 e release/v0.0.2, a referência de HOM é release/v0.0.2. Para uma conclusão rastreável, identificar também o commit efetivamente lido. Esse é um relato explícito sobre o ambiente corporativo, distinto de uma inspeção independente da pipeline. A regra resolve a seleção do código de HOM no seu escopo. Configurações externas efetivas e ocorrências individuais dependem das fontes correspondentes quando forem objeto da pergunta. |
| **C-P03-06 · Resolvido** | Aceito o conteúdo informativo sobre parâmetro configurável: identificar o parâmetro, o padrão no código, a possibilidade de substituição e o valor efetivo no ambiente caso esteja evidenciado ou seu desconhecimento quando falte evidência. O exemplo em linguagem natural serviu para delimitar significado. A forma de gravação segue aberta. |
| **C-P03-04 · Resolvido** | Quando o objeto do pedido é a pasta local, estudar a cópia de trabalho examinada, com suas alterações autorizadas, identificando as diferenças em relação ao commit-base. No exemplo, três tentativas pertencem ao commit e cinco ao estado local modificado. A análise não transforma a alteração local em commit ou versão publicada. A exigência de atualização antes de cada push mantém seu escopo próprio, com mecanismo e comprovação a especificar. |
| **P03.7 · Resolvido no alcance funcional** | As quatro entradas e os padrões de branch já estavam definidos. Um link remoto que especifique uma branch é escolha explícita. A distinção entre cópia local e commit-base acaba de ser resolvida. Falhas materiais de obtenção entram em P03.9. Regras de identificação e representação física do estado de trabalho terão detalhamento técnico próprio. |

**Situação cumulativa das 22 perguntas originais.** 17 resolvidas (.3, .4, .5, .6, .7, .8, .9, .10, .11, .12, .14, .15, .16, .17, .18, .19, .21), quatro parciais (.1, .2, .13, .22) e uma adiada (.20). No conjunto das oito colaterais, .01, .02, .03, .04, .05, .06 e .08 receberam definições no alcance discutido, inclusive a direção de cobertura de .03. A comparação de custo de .07 está adiada. A contagem não equivale à aprovação de mecanismos de validação ou formatos.

### Procedimento proposto · classificar fatos relativos a uma revisão

A decisão deve ser feita sobre o fato a recuperar e a ação que depende dele. Um único método pode conter uma regra obrigatória de negócio e uma escolha interna de implementação. Vários métodos podem, em conjunto, realizar uma só regra.

1. **Delimitar e inventariar.** Partir dos usos e responsabilidades do repositório. Percorrer as entradas e saídas reais da revisão, inclusive API, fila, agendamento, persistência, contrato com terceiros, infraestrutura, configuração, limites operacionais, testes e procedimentos pertinentes. Seguir os fluxos afetados, incluindo erros, alternativas e caminhos em que nada é enviado ou gravado. Indicar partes não lidas ou inacessíveis. Este inventário diminui o risco de deixar uma regra de fora antes de sequer aplicar o critério.
2. **Aplicar a pergunta de impacto.** Se o próximo agente desconhecer o fato, pode responder errado sobre a finalidade ou responsabilidade, os dados aceitos/emitidos, uma condição de decisão, o estado ou efeito produzido, o tratamento de erro, duplicidade, ordem, segurança, permissão, desempenho exigido, operação, dependência ou segurança de uma mudança? Pedir um exemplo concreto da diferença. Assuntos raramente consultados ainda entram quando a omissão muda a decisão.
3. **Escolher a representação mínima suficiente.** Se houver efeito material, o conjunto documental deve torná-lo recuperável. Uma explicação curta é necessária quando entender o efeito exige combinar código, condição, configuração e contrato. Se uma fonte declarativa canônica, legível, autorizada e versionada já responde integralmente à pergunta, basta oferecer a rota exata, o alcance e o significado pertinente. Se o fato só descreve o modo interno de realizar o mesmo comportamento e nenhum contrato, limite ou risco material muda no escopo analisado, o detalhe pode ficar somente no código.
4. **Tratar a incerteza.** Falta de acesso, contradição ou dúvida de impacto conserva o estado de lacuna. Registrar onde a investigação chegou, o que segue sustentado e qual ação exige nova evidência. Ao retornar a uma fonte, aplicar as permissões da operação e da fonte, incluindo a consulta posterior ao legado quando pertinente. Uma decisão editorial sobre o Micro não cria acesso.
5. **Conferir a cobertura nos dois sentidos.** Para cada efeito material encontrado, localizar a unidade que permite explicá-lo ou a ressalva que o delimita. Para cada afirmação material da base, localizar a evidência na revisão usada. Em uma regra com dois caminhos, variar a condição decisiva e verificar se a consulta aos documentos vinculados permite prever os dois resultados distintos, inclusive ausência de efeito. Esse é um critério de revisão documental proposto. Métodos formais, executores e métricas permanecem com a futura P03.20.

| Exemplo na revisão analisada | Resultado da classificação proposta |
|---|---|
| Ao receber PENDENTE, A grava e publica se a proposta está ativa e encerra sem publicar se está cancelada. | **Explicar.** Mostrar condição, ambos os efeitos e evidência. Um agente consultando as unidades pertinentes consegue explicar os dois resultados sem reconstituir a lógica no código. |
| Um esquema é a fonte canônica autorizada de 60 campos. Dois deles são obrigatórios somente em algumas condições. | **Referenciar o esquema e explicar a condição relevante** quando ela não for autoexplicativa no próprio contrato. Incluir ligação ao campo/cláusula na revisão, para chegar aos tipos e exemplos exigidos em P03.1. Se o artefato não for legível/estável para o público autorizado, um ponteiro isolado é insuficiente. |
| Uma variável privada de apoio muda de nome sem alterar contrato, resultado, efeito, custo operacional relevante ou limite conhecido. | **Somente código.** Não cabe uma ficha para a variável. A localização da regra ou do componente a que ela serve continua disponível. Uma condição equivalente dentro de um helper deve entrar na base se alterar um comportamento material. |
| Um serializador não envia codigoSegmento quando o valor é nulo. | **Explicar o efeito de omitir o campo.** O corpo do serializador pode ficar no código. A aceitação de campo ausente em C permanece uma questão sobre C. |
| Um worker detecta duplicatas pela chave do pedido. O código de sucesso mostra gravação e publicação, mas as fontes examinadas não esclarecem o que ocorre entre os dois atos em caso de falha. | **Explicar a deduplicação sustentada e registrar a lacuna de falha.** Uma conclusão de segurança sobre reenvio/atomicidade deve esperar a evidência que a sustente. |

Assim, “todo o conhecimento recuperável a partir do Micro” é uma propriedade da navegação. O agente começa por uma entrada enxuta, chega à informação funcional, operacional ou contratual conforme a pergunta e pode seguir até evidências ou unidades relacionadas. Uma regra tem uma origem principal de edição. Outras unidades apontam para ela. Referências cruzadas devem ligar responsabilidades, fluxos, regras, contratos, evidências e lacunas **quando houver relação real**. Não se exige um link entre todos os documentos. Um ciclo de referências que nunca apresenta a regra ou a evidência falha no critério de recuperação. Essas são responsabilidades lógicas possíveis, sem propor árvore física, extensão ou ferramenta obrigatória.

### Aplicação a HOM e à cópia local

Se coexistem release/v0.0.1 e release/v0.0.2 e o pedido é explicar **o código de HOM**, usar a regra corporativa informada, resolver a release/v0.0.2 ao commit lido e atribuir as conclusões a essa revisão. Isso é diferente do onboarding remoto genérico pela main ou por link de branch explicitamente escolhido. Se a fonte de HOM identifica o código que lê FILA_PEDIDOS e o padrão pedidos-padrao, já é possível explicar a regra da versão de homologação. Para afirmar qual fila efetivamente foi selecionada quando o valor é injetado fora do repositório, usar a configuração autorizada correspondente. Para afirmar que um pedido específico foi processado, é necessária evidência do evento. A representação física dessas informações permanece em aberto.

Se a pasta local tem uma edição que altera o limite de três para cinco tentativas, o resultado do estudo dessa pasta precisa distinguir o comportamento examinado localmente daquele sustentado pelo commit-base. Referências a outro agente devem preservar essa diferença e os direitos de acesso. Nenhum push ou execução de aplicação é necessário para entender a distinção.

**Retomada.** Submeter o critério de fronteira a deliberação em P03.1/.2 e confrontá-lo com casos limítrofes de API, worker e infraestrutura. O desenho físico do conjunto de documentos e a avaliação de custo permanecem para refinamentos próprios. **NÃO PERSISTIDO no GitHub.** [Especificação do Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md) · [Autorizações e atualização do conhecimento](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md)

<a id="saldo-p03-r4"></a>

## P03 · Terceira rodada de respostas e definição da camada de conhecimento

**Edição de trabalho 4 · 8 de novembro de 2026.** Fonte direta desta rodada: manifestação do usuário sobre P03.1/.2, .4, .14 e C-P03-01 a 08. O usuário identifica a definição da camada de conhecimento como antecedente ao fechamento de P03.1/.2. A aceitação dos casos específicos permanece válida. As seções anteriores estão preservadas como histórico.

### Decisões recebidas e ponto ainda em aberto

| Item | Saldo atual |
|---|---|
| **P03.1 e P03.2** | O objetivo é recuperar o conhecimento do repositório com profundidade, precisão, rapidez e menor custo. C-P03-01 resolve o caso dos dois caminhos de A ao receber 200/PENDENTE. C-P03-03 determina abranger todos os aspectos, dimensões e unidades de conhecimento tanto quanto possível e registrar lacunas. Falta validar a fronteira geral entre o que explicar na base, o que referenciar na fonte canônica e quando reler a fonte. |
| **P03.4 · Resultado funcional definido** | O Meso é índice das responsabilidades dos repositórios de uma Sigla. Para uma dúvida sobre abertura de contas já associada a NC2, deve encaminhar aos Micro pertinentes sem percorrer todos os repositórios da empresa. O enriquecimento do Meso acompanha o dos Micro, conforme P03.10. A composição funcional de uma solução permanece com Arquitetura/Solução. |
| **Raiz da Plataforma · Proposta do usuário** | A raiz poderia indexar responsabilidades, escopo e dados pertinentes de cada Sigla, permitindo encontrar a Sigla quando a consulta começa apenas pelo assunto. A inclusão na v1, conteúdo, manutenção e visibilidade desse índice ainda requerem definição. A proposta funcional não decide a relação física entre a raiz da instalação e o Macro Git. |
| **P03.14** | Permanece aberta a capacidade da v1 de interpretar uma prova de ambiente fornecida pelo Engenheiro. O exemplo do worker e da fila em homologação aparece abaixo. |
| **C-P03-01** | Sim expresso ao caso dos caminhos concretos em A. Condições, decisões, efeitos locais e evidências de ambos precisam ser recuperáveis. |
| **C-P03-02** | Uma origem principal para cada fato e referências nos demais lugares. Qualquer mudança de código deve atualizar todo dado de conhecimento cujo significado tenha sido alterado. A base deve refletir fielmente o repositório. Formatos seguem em avaliação. |
| **C-P03-03** | Definida a direção do onboarding amplo: abarcar todos os aspectos, dimensões e unidades de conhecimento tanto quanto possível e registrar dúvidas, incertezas, insuficiências e pendências. A completude efetiva deve ser demonstrada no escopo de cada uso. |
| **C-P03-04** | Novo requisito expresso: todo push deve ser precedido da atualização da base documental, com garantia determinística. A pergunta original sobre os arquivos locais sem commit continua aberta. O usuário não escolheu mecanismo técnico nem definiu a comprovação de ausência de impacto documental. |
| **C-P03-05** | Um link GitHub que indica uma branch específica é escolha explícita dessa branch. O link para a raiz continua com o padrão de usar main. |
| **C-P03-06** | Pergunta reformulada sobre o que registrar no Micro quando o código define um valor padrão e o valor efetivo depende do ambiente. A redação candidata aparece abaixo. |
| **C-P03-07** | Comparação de custo e qualidade adiada expressamente para refinamento posterior, junto da avaliação de P03.20. |
| **C-P03-08** | Aceitos mínimos por tipo, conforme aplicabilidade. Para fila/tópico, recuperar contrato, origem e destino conhecidos e efeitos observáveis em sucesso, falha ou duplicidade quando pertinentes. Para banco, recuperar operação, dados lidos/alterados e comportamento diante dos resultados materiais, por exemplo uma consulta vazia. |

No alcance das perguntas originais, há **15 itens resolvidos** (.3, .4, .5, .6, .8, .9, .10, .11, .12, .15, .16, .17, .18, .19, .21), **cinco parciais** (.1, .2, .7, .13, .22), **um em esclarecimento** (.14) e **um adiado** (.20). P03.4 fecha quanto à finalidade mínima. A ideia da raiz tem estado próprio de proposta. As colaterais acompanham a agenda original sem alterar o total de 22.

### Política de uso da base e viabilidade · recomendação para decisão

A autonomia pretendida é conseguir responder a uma pergunta sobre comportamento conhecido em determinada revisão, sem precisar reconstruir o fluxo a partir do código. A base deve permitir partir do índice, recuperar as unidades pertinentes e, quando estas cobrirem as condições, exceções, efeitos, evidências e limites materiais para o pedido, responder diretamente. Uma pergunta que extrapole essa cobertura exige outra ação.

| Situação | Tratamento proposto |
|---|---|
| **Como A trata PENDENTE?** | Explicar no Micro os dois caminhos já aceitos. Quando a proposta está ativa, A grava e publica. Quando está cancelada, encerra sem publicar. Identificar revisão e evidência. Uma consulta rotineira sobre esses caminhos pode ser respondida só com o Micro válido. |
| **Se o banco confirmar a gravação e o envio à fila falhar, o que acontece?** | Saber que A grava e publica no caminho de sucesso é insuficiente. Procurar primeiro conhecimento já validado sobre falhas e reenvio. Persistindo a lacuna, consultar pontualmente, no escopo autorizado, o fluxo de publicação, os testes e a configuração pertinentes. Registrar o que ficou inconclusivo e incorporar a explicação verificada nos níveis autorizados. |
| **Qual detalhe pode permanecer na fonte?** | A implementação linha a linha de um serializador, o esquema integral já mantido em arquivo canônico ou o corpo de uma função podem ser recuperados por referência de revisão, caminho e símbolo. Se o serializador omite um campo nulo e isso altera o contrato, o efeito da omissão merece explicação no Micro, ainda que a implementação detalhada permaneça no código. |
| **C aceita o campo ausente? Essa regra vale em produção?** | Uma chamada em A demonstra apenas o lado observável em A. O comportamento de C, a configuração implantada e a intenção de negócio podem exigir evidências próprias. O Micro deve informar o que se conhece, o que falta e qual decisão depende dessa informação. |

**Quando abrir a fonte.** O onboarding inicial já envolve leitura do material autorizado. Nas consultas posteriores, propõe-se voltar à fonte quando a informação material faltar, surgir contradição, mudar a revisão, for necessária evidência mais precisa ou uma alteração autorizada exigir conferir a implementação. Ler uma fonte corrente já autorizada e retornar a um artefato legado por lacuna de migração têm condições distintas. No segundo caso valem aviso de inconformidade e permissão. Um ponteiro conserva a origem e não amplia direitos. Corrigir ou ampliar o conhecimento requer validação e autorização apropriadas. [Especificação do Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Registro HUM](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md)

**O que é viável.** Extrair fatos explícitos, como uma rota ou configuração declarada, admite verificações mecânicas nos padrões reconhecidos. Reconstruir uma regra que atravessa handlers, persistência, callbacks e filas exige cruzar condições e efeitos em mais de uma fonte. Explicar uma condição real de execução pode exigir estado de banco, configuração externa, disponibilidade de outra aplicação ou evidência do ambiente. Duas instalações com o mesmo código podem apresentar resultados distintos. Com premissas e revisões delimitadas é viável buscar cobertura ampla e evidenciá-la; um relato textual não comprova, sozinho, equivalência completa para toda entrada e todo ambiente.

Para regras frequentes ou cuja interpretação errada muda uma decisão, a explicação preparada tende a compensar pelo reúso. Para detalhes voláteis ou raramente consultados, manter explicações duplicadas cobra atualização e amplia o risco de divergência. A economia depende do custo de produzir, manter, recuperar e ocasionalmente conferir o conhecimento ao longo das tarefas. A escolha das métricas permanece com a etapa posterior.

**Referência externa.** O relato da OpenAI descreve um índice curto e documentação aprofundada recuperada por assunto. O SWD-Bench, com 4.170 itens, examina se uma funcionalidade é descrita, se é possível localizar os arquivos e se há detalhes suficientes; seus autores observaram valor complementar do código. Gloaguen e colaboradores observaram em tarefas de programação que arquivos gerais de contexto aumentaram o custo de inferência em mais de 20% sem melhoria geral no sucesso. Os três trabalhos examinam intervenções diferentes e não medem o Motor do banco. [Relato da OpenAI](https://openai.com/index/harness-engineering/) · [SWD-Bench](https://arxiv.org/abs/2604.06793) · [Estudo da ETH Zürich](https://www.sri.inf.ethz.ch/publications/gloaguen2026agentsmd)

### Da dúvida ao repositório certo

O agente recebe a pergunta “quando uma abertura de conta segue para revisão?”. Se conhece NC2, começa no Meso de NC2. O índice das responsabilidades indica qual repositório recebe a proposta e qual decide o encaminhamento. A condição concreta vem da base Micro apropriada. Se começa só pelo assunto, o catálogo na raiz, caso aprovado, poderá indicar uma ou mais Siglas candidatas. Arquitetura/Solução é pertinente quando a necessidade é compreender a jornada composta por vários componentes. A associação a um tema não concede acesso nem pressupõe exclusividade da Sigla.

### Atualização documental antes de todo push

A determinação temporal recebida antecipa a verificação para antes de todo envio. Exemplo: A passa a exigir que a proposta esteja ativa e seja prioritária para publicar. A ficha que diz somente “ativa” precisa ser revisada e o impacto deve atingir quaisquer derivados que já reproduzissem aquela condição. Fazer uma alteração cosmética em um Markdown faria passar um controle baseado apenas na presença de um arquivo alterado, embora a regra ainda estivesse errada.

**Proposta de engenharia a avaliar:** exigir uma verificação vinculada exatamente ao conteúdo que se pretende enviar; bloquear o envio sem prova correspondente e repetir a validação quando o conteúdo candidato mudar. Uma barreira pode garantir que a verificação obrigatória ocorreu antes do push. A precisão semântica de cada conclusão exige suas próprias evidências e verificações. Cobrir todos os clientes pelos quais alguém pode enviar mudanças exige controles efetivos no ambiente autorizado. Um controle restrito ao Motor só alcança os envios que passam por ele. Aprovação de conhecimento e push de trabalho são atos distintos. A composição entre repositórios exige verificação de revisões e ponteiros. Nenhuma tecnologia nem alteração de pipeline foi aprovada nesta rodada. [HUM-08/09](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md)

A regra deixa em aberto a situação anterior ao envio: o último commit prevê três tentativas, a cópia local já foi alterada para cinco e ainda não há commit ou push. O onboarding daquela pasta deve estudar o commit ou a cópia de trabalho? Se estudar a cópia, precisa identificar a origem local da diferença. O tratamento de alterações cuja análise encontre zero impacto semântico também requer detalhamento antes da implementação do controle.

### P03.14 e C-P03-06 · Exemplo do worker que lê uma fila

No Git, o worker lê a fila indicada pela variável FILA_PEDIDOS. Se a variável estiver ausente, ele usa pedidos-padrao. Os nomes e valores são sintéticos.

**C-P03-06 pergunta o que escrever no Micro quando só o Git foi lido.** Redação proposta: “Este worker usa a fila indicada em FILA_PEDIDOS. Quando a variável não é definida, usa pedidos-padrao. A revisão examinada não informa qual fila ele usa em homologação.” Essa redação aplica os critérios de alcance e insuficiência já aceitos.

**P03.14 pergunta o que a primeira versão do Motor faz quando o Engenheiro entrega outra fonte.** O Engenheiro fornece um registro autorizado mostrando que, para o worker efetivamente rodando em homologação, naquela versão, FILA_PEDIDOS vale pedidos-hom-v2. A capacidade sugerida é ler o registro entregue e responder “nessa implantação, o worker está configurado para ler pedidos-hom-v2”, com referência à evidência recebida. Um exemplo de Terraform que apenas prevê a configuração sustentaria uma afirmação sobre a configuração pretendida. O valor configurado também não comprova que uma mensagem específica foi processada. A consulta automática à AWS por conta própria seria uma capacidade separada.

**Retomada.** Validar a fronteira entre explicação autossuficiente, referência canônica e lacuna declarada antes de fechar P03.1/.2. O catálogo na raiz, o comportamento de onboarding com alterações locais e a realização da garantia pré-push têm objetos distintos. **NÃO PERSISTIDO no GitHub.**

<a id="saldo-p03-r3"></a>

## P03 · Segunda rodada de esclarecimentos

**Edição de trabalho 3 · 8 de novembro de 2026.** Fonte direta desta rodada: a manifestação do usuário sobre P03.1, .2, .4, .8, .10, .14, .16 e .21 e o pedido de esclarecer as oito dúvidas colaterais do tópico 4. A edição 2 aparece abaixo como histórico. As recomendações e os exemplos desta edição são do assistente.

| Situação após a segunda rodada | Itens P03 | Total |
|---|---|---:|
| Resolvido no alcance funcional da pergunta | .3, .5, .6, .8, .9, .10, .11, .12, .15, .16, .17, .18, .19, .21 | 14 |
| Parcialmente resolvido | .1, .2, .7, .13, .22 | 5 |
| Função do Meso em reconsideração | .4 | 1 |
| Pergunta de escopo reformulada | .14 | 1 |
| Adiado por decisão expressa | .20 | 1 |

**O que mudou nesta rodada**

| Item | Definição e alcance |
|---|---|
| **P03.8 · Sigla pelo nome** | O usuário informa que o nome do repositório obrigatoriamente corresponde à Sigla a que ele pertence. O comportamento indicado para o Motor é extrair a Sigla do nome e organizar o repositório na pasta correspondente. Assim, `itau-xp6-consulta-fatura` pertence a XP6 mesmo que uma atividade conduzida por NC2 precise estudá-lo. A regra resolve a atribuição. A organização da área da Plataforma deve respeitar a preservação da aplicação durante o onboarding. |
| **P03.10 · Enriquecimento do material da Sigla** | O resultado de uma nova execução do onboarding deve se refletir no material da Sigla. Esse material se enriquece à medida que se enriquecem os materiais dos seus repositórios. Exemplo sintético: uma reanálise de A acrescenta uma integração. A referência pertinente da Sigla deve refletir o novo conhecimento sobre A. D, que não foi reanalisado, conserva sua revisão conhecida. A regra de enriquecimento está definida mesmo enquanto o conteúdo próprio do Meso é discutido em .4. Detalhes de atualização e publicação têm seus refinamentos próprios. |
| **P03.16 · Primeiro aviso** | O usuário aceitou que o aviso diga explicitamente se o agente pode continuar sozinho ou precisa de decisão humana naquele momento. Se só parte da tarefa depender da decisão, o aviso pode distinguir a parte afetada do trabalho independente. |
| **P03.21 · Fluxo excepcional incluído na v1** | O usuário confirmou que o Motor inicial deve oferecer o fluxo excepcional de execução local da aplicação estudada. Aplicam-se as condições de HUM-03. Precisa restar uma dúvida material intransponível após as investigações autorizadas. O Engenheiro pode responder diretamente. Para solicitar a execução, o agente deve expor tentativas, finalidade, ambiente, dados, pré-requisitos, comandos e efeitos previstos e obter permissão específica do Engenheiro para aquela ocorrência. O aceite nesta conversa define escopo de produto. [HUM-03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-03) |

### P03.1 e P03.2 · Duas perguntas diferentes

**P03.1 · Até onde seguir uma única resposta recebida?** Os campos do contrato HTTP já foram especificados. Considere um repositório A que recebe `200/PENDENTE`. Para proposta ativa, A grava o estado `AGUARDANDO` e publica uma mensagem para revisão. Para proposta cancelada, registra o motivo e encerra, sem publicação. A decisão é se a ficha dessa integração, ou as referências que ela oferece, precisa permitir ao agente reconstruir **os dois caminhos**, suas condições, efeitos e evidências no próprio A. Recomenda-se que sim. O tratamento posterior por outro consumidor permanece sujeito à evidência do outro lado. JSON, Markdown ou uma combinação seguem em avaliação. A mesma resposta a P03.1 vale para C-P03-01.

**P03.2 · O que cobrir ao estudar o repositório inteiro pela primeira vez?** O Engenheiro entrega um worker e pede seu onboarding, sem indicar uma história. O Motor já localizou a fila, o banco, o Terraform, as variáveis e as bibliotecas. Estudando o código, percebe que o worker grava os pedidos válidos, descarta as mensagens repetidas e encaminha pedidos inválidos para revisão. A decisão é se **todos esses caminhos que mudam o resultado** devem ficar identificados desde o primeiro onboarding, mesmo antes de alguém perguntar especificamente sobre duplicidade ou falha. Recomenda-se um índice inicial dos fluxos e das regras que alteram resultados, com condição, efeito e rota até a evidência. Detalhes internos podem ser recuperados quando a tarefa os exigir. A cobertura efetiva e os caminhos inconclusivos ficam explícitos. A mesma resposta a P03.2 vale para C-P03-03.

### P03.4 · O que compete à Sigla e o que compete à solução?

Para explicar uma jornada, a utilidade principal de reunir relações entre os componentes está na **Arquitetura/Solução**. Uma relação técnica observada no Micro também pode ser localizável por Sigla, caso esse índice economize trabalho. Exemplo sintético: `itau-nc2-api-propostas` publica numa fila, `itau-nc2-worker-validacao` a consome e um serviço de ES7 comunica o resultado. NC2 pode conter ainda um repositório de relatórios sem participação nessa jornada.

| Pergunta do engenheiro | Papel possível |
|---|---|
| “Onde a API publica a mensagem e em qual condição?” | **Micro da API.** Explica o comportamento local e aponta a revisão e o trecho que o sustentam. |
| “Quais repositórios de NC2 foram estudados e onde encontro o material atualizado de cada um?” | **Meso de NC2.** Reúne os repositórios da Sigla, suas referências e o material comum pertinente. Pode também encaminhar ao Micro que explica a fila se essa navegação tiver utilidade. Esse índice de relações continua proposto. |
| “Como uma proposta vai da submissão até a comunicação do resultado?” | **Arquitetura/Solução.** Reúne os componentes relevantes de NC2 e ES7, organiza o fluxo e suas alternativas e registra a fronteira funcional delimitada pelo Analista. O repositório de relatórios só entra se houver participação na solução. |

**Recomendação para discussão.** Manter no Meso os submódulos, a navegação para o material dos Micro nas revisões pertinentes e o conteúdo realmente comum da Sigla. Reutilizar as referências dos Micro para explicar a solução quando ela atravessar repositórios. Resta decidir se a primeira entrega precisa oferecer uma consulta própria por relação na Sigla. O enriquecimento do Meso já foi confirmado em P03.10. A saída arquitetural da v1 continua a depender de PE-08. [Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md) · [Retomada do Motor e da Arquitetura](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md)

### P03.14 · O Motor interpreta uma evidência de ambiente que o Engenheiro traz?

**Caso 1.** O Engenheiro pergunta qual é o tempo máximo de espera de uma chamada em homologação (HOM). No repositório estudado, o padrão é 2 segundos, e a aplicação aceita que a configuração do ambiente substitua esse valor. Só com esse material, a resposta possível é “o padrão nessa revisão é 2 segundos e o valor de HOM continua desconhecido”.

**Caso 2.** O Engenheiro entrega registros autorizados que identificam a versão efetivamente implantada em HOM e comprovam que, nessa implantação, a configuração efetiva é 5 segundos. A pergunta que precisa de resposta é: diante disso, a primeira versão do Motor deve interpretar os registros, vinculá-los à conclusão e responder “nessa implantação de HOM, o limite configurado é 5 segundos”? Recomenda-se que sim, delimitando componente, ambiente, versão e origem. Quando faltar o vínculo necessário, basta indicar precisamente o que falta.

**Caso 3.** Com os mesmos registros, alguém pergunta se o pedido X esperou 5 segundos ou se ocorreu timeout. Eles demonstram o limite configurado. Para responder sobre X, seria preciso uma evidência daquela ocorrência. A decisão de P03.14 pode ser tomada sem incluir busca direta em serviços corporativos.

### Tópico 4 · Oito dúvidas colaterais, em termos concretos

| ID | Situação e pergunta que precisa ser respondida | Encaminhamento sugerido |
|---|---|---|
| **C-P03-01 · Profundidade de uma integração** | O mesmo `200/PENDENTE` leva A a publicar uma mensagem quando a proposta está ativa e a encerrar o processamento quando está cancelada. O agente tem de recuperar condição e efeito de cada caminho dentro de A? | Reutilizar a resposta a P03.1. Invalidar uma interpretação que descreve a publicação como obrigatória se o caminho da proposta cancelada demonstra o contrário. |
| **C-P03-02 · Contrato e explicação sem duplicação** | Suponha que o contrato e as regras estejam em arquivos distintos. O serviço continua devolvendo `PENDENTE`, mas A passa a publicar a mensagem somente para propostas prioritárias. Ao atualizar o conhecimento, em qual registro se edita a condição e a partir de onde outro agente a encontra? | Cada fato deve ter uma referência principal para edição. O contrato pode apontar ao tratamento realizado por A, e a regra pode referenciar o campo do contrato. Avaliar os formatos depois de concordar sobre o que o agente deve recuperar. |
| **C-P03-03 · Quando o onboarding amplo está suficiente** | No worker de P03.2, o agente já explicou o fluxo de sucesso. Há também um caminho que descarta duplicatas e outro que encaminha inválidos. O que já precisa aparecer no material inicial para concluir o onboarding com seus limites declarados? | Reutilizar a resposta a P03.2. Proposta: mapear os caminhos relevantes encontrados, registrar o efeito de cada um ou a lacuna que impediu explicá-lo e permitir aprofundamento sob demanda. |
| **C-P03-04 · Arquivos locais alterados** | O último commit permite três tentativas. A cópia local foi alterada para cinco e tem um arquivo novo ainda sem commit. Ao apontar essa pasta ao Motor, o Engenheiro quer retratar o commit ou a cópia que está no disco? | Se o objetivo é explicar o que está na máquina, analisar a cópia de trabalho como estado local e identificar suas diferenças. Uma conclusão sobre cinco tentativas precisa indicar essa origem. |
| **C-P03-05 · Link remoto e branch** | Um link para a raiz segue a regra já decidida de usar `main`. Se o Engenheiro colar um link que contém explicitamente `/tree/feature-x`, isso conta como pedido para estudar aquela branch? Outro caso: se `main` não puder ser lida, que parte da operação segue? | Explicitar a revisão pretendida quando o próprio link divergir da regra. Na falha de obtenção, aplicar P03.9, indicar o impedimento daquele repositório e prosseguir no restante possível. |
| **C-P03-06 · Padrão do código e valor de ambiente** | O código usa `TIMEOUT_MS` e assume 2000 se não houver substituição. Não há fonte disponível com o valor de HOM. O Micro deve mostrar o padrão, como ele pode ser substituído e que o valor de HOM continua desconhecido? | Proposta: registrar os três. Se a evidência chegar, P03.14 decide como o Motor inicial a utiliza. Este item trata do que escrever sobre um parâmetro configurável. |
| **C-P03-07 · Custo conforme a tarefa** | Duas organizações preservam a mesma regra, suas exceções e as evidências. Com um índice, localizar o timeout exige pouca leitura. Uma pergunta sobre todo o fluxo exige abrir várias referências. Um documento contínuo pode ter o custo inverso. Quais tarefas devem orientar a comparação? | Guardar para P03.20 uma consulta pontual e uma investigação de ponta a ponta. Comparar precisão, esforço de leitura, tempo e consumo disponível por ferramenta. Métodos, executores e limites aguardam o momento definido pelo usuário. |
| **C-P03-08 · Fichas de mensagem e de banco** | Num consumidor de fila, o que o agente deve conseguir explicar sobre mensagem recebida, origem conhecida, tratamento, duplicidade e falha? Para uma consulta ao banco, basta identificar os dados lidos ou é necessário dizer o que a aplicação faz quando a consulta vem vazia? | Adotar campos próprios para cada tipo quando aplicáveis. Na mensageria, recuperar contrato e efeitos observáveis do processamento. No banco, recuperar operação, dados afetados e o comportamento da aplicação diante dos resultados relevantes. Enriquecer o exemplo com exceções realmente encontradas. |

**Retomada.** Começar por P03.1/C-P03-01. A resposta a P03.2 será aproveitada em C-P03-03. C-P03-06 e P03.14 compartilham o exemplo de timeout, mas a primeira pergunta trata do conteúdo do Micro e a segunda da capacidade do Motor inicial de interpretar evidência de implantação. O trabalho de avaliação de C-P03-07 permanece no momento reservado a P03.20. Esta edição atualiza o caderno de trabalho. **NÃO PERSISTIDO no GitHub.**

<a id="saldo-p03-r2"></a>

## P03 · Saldo da primeira rodada de respostas

**Edição de trabalho 2 · 8 de novembro de 2026.** Fonte direta desta rodada: respostas do usuário aos itens P03.1 a P03.22 nesta conversa. A segunda ocorrência de “P03.2”, sobre a exceção futura, foi vinculada editorialmente a P03.21 por assunto e posição. A primeira ocorrência permanece em P03.2. As classificações e as perguntas colaterais são análise do assistente. Exemplos permanecem sintéticos.

| Estado nesta rodada | Itens | Total |
|---|---|---:|
| Resolvido no alcance da pergunta | .3, .5, .6, .9, .11, .12, .15, .17, .18, .19 | 10 |
| Parcialmente resolvido | .1, .2, .7, .13, .22 | 5 |
| Decisão anterior em reconsideração | .4 | 1 |
| Pergunta reformulada | .8, .10, .14, .16, .21 | 5 |
| Adiado por decisão expressa | .20 | 1 |

“Resolvido” qualifica a definição de produto no seu alcance. Testar eficácia e escolher a implementação são trabalhos próprios. Entre os cinco itens reformulados há um exemplo hipotético sem conflito comprovado (.8), uma dependência do Meso (.10) e um ponto em grande parte respondido por outra resposta (.16).

### Registro por resposta

| ID | Definição recebida e avaliação |
|---|---|
| **P03.1 · Parcial** | Para uma chamada HTTP consumida, registrar URL, campos de entrada com tipos e exemplos quando possível, campos de saída, headers, parâmetros de consulta, variáveis de caminho, verbo HTTP, configurações de timeout e status esperados. O usuário distingue o contrato técnico das regras que tratam o resultado. Falta definir o alcance da explicação dessas regras. JSON e Markdown são hipóteses de representação. |
| **P03.2 · Parcial** | O usuário relata predominância de APIs, workers e consumidores de tópicos/filas, com Terraform para AWS na maioria dos repositórios. A base deve responder sobre entradas, saídas, APIs e bases consumidas, mensagens publicadas/consumidas, recursos AWS, variáveis de ambiente, parametrizações, frameworks, bibliotecas e regras próprias. Falta especificar o que permite dizer que as regras particulares foram suficientemente explicadas no onboarding de cada tipo. A definição de formato está aberta em .22. |
| **P03.3 · Resolvido** | Evidência tão específica quanto possível, navegável do geral ao particular, incluindo pasta, documento, classe, método, linha e coluna quando aplicáveis. A referência permanece vinculada à revisão estudada. Para um arquivo Terraform ou contrato, um bloco ou uma cláusula pode ser o localizador pertinente. |
| **P03.4 · Em reconsideração** | O usuário mantém a utilidade do repositório por Sigla com os repositórios como submódulos. Reconhece a utilidade de configuração de acesso ao perfil AWS e questiona a necessidade de conhecimento próprio adicional. A edição Git vigente também prevê cobertura por revisão, informação compartilhada e lacunas do conjunto. A dúvida reabre a função da base sem decidir sua retirada. Ponteiros e configurações respeitam os acessos reais GitHub/AWS. |
| **P03.5 · Resolvido por dispensa** | Dispensa expressa de conhecer ou comprovar o total dos repositórios da Sigla. Permanecem identificáveis os repositórios efetivamente solicitados, obtidos, estudados ou impedidos, conforme .7 e .9. A busca por Sigla pode relatar os resultados autorizados obtidos sem um censo corporativo. |
| **P03.6 · Resolvido** | Para a relação observada por um lado, registrar sentido, contrato/evento, evidência, limite da investigação e fonte que seria necessária do outro lado. O Engenheiro decide a eventual inclusão do repositório na atividade. |
| **P03.7 · Parcial** | Quatro entradas: apontar um ou mais repositórios em diretório local, arrastá-los para a pasta da Plataforma, fornecer links GitHub ou pedir ao agente todos os repositórios de uma Sigla no GitHub. Local usa a branch em que o repositório já está, salvo especificação do Engenheiro. Remoto usa a versão de `main`. Faltam o tratamento das alterações locais sem commit e das referências remotas divergentes ou sem `main` acessível. O gesto de arrastar pode usar o gerenciador de arquivos do sistema. |
| **P03.8 · Reformulada, condicional** | O usuário informa que as Siglas como ES7, XP6, CO8 e NC2 normalmente são únicas. A dúvida é sobre atribuir um repositório a uma Sigla. Nenhum conflito real foi apresentado. A investigação pode usar o caminho normal e tratar uma inconsistência somente quando houver indícios concretos. |
| **P03.9 · Resolvido** | Para cada parte material, informar revisão, conteúdo examinado e faltante, motivo conhecido, consequência e ponto de retomada. Entregar de imediato o que estiver sustentado e isolar a conclusão dependente da ausência. |
| **P03.10 · Reformulada, dependente de .4** | “Rodada” é uma nova execução do onboarding. “Incorporar” é refletir no material da Sigla o resultado dessa execução, quando existir algo a refletir. Falta determinar o comportamento incremental que se aplica à saída Meso que vier a ser escolhida. |
| **P03.11 · Resolvido** | A suficiência depende da ação pretendida. Para cada conclusão importante, explicitar o que a evidência permite fazer agora e qual decisão exige outra fonte. |
| **P03.12 · Resolvido** | Confrontar objeto, revisão e condições de cada fonte. Preservar os trechos divergentes, a interpretação que cada um sustenta e a evidência necessária para decidir. Distinguir um teste localizado de uma execução observada. |
| **P03.13 · Parcial** | O usuário aceita o critério de impedimento quando falta uma explicação indispensável ao objetivo ou não é possível delimitar com segurança o que se compreendeu. Pediu refiná-lo pela comparação de três casos. Um caso já tem aceite histórico e os dois outros exemplos abaixo ainda são propostos. |
| **P03.14 · Reformulada** | O usuário pediu esclarecimento sobre comportamento lido no Git, componente e artefato. A regra vigente exige evidência para atribuir uma revisão a um ambiente. Falta delimitar que evidência basta para cada afirmação e o que cabe ao Motor inicial quando ela não está disponível. |
| **P03.15 · Resolvido** | Pedir a menor intervenção que permita avançar, acompanhada das evidências, tentativas autorizadas, interpretações possíveis e decisão afetada. Separar uma dúvida factual sobre o sistema de uma escolha de produto ainda não feita. |
| **P03.16 · Reformulada, parcialmente coberta por .18** | O momento do aviso está decidido e .18 estabelece afirmação, fonte, limitação e próxima ação. A formulação residual é como comunicar no primeiro aviso que o impacto segue sob investigação e se a pessoa precisa agir naquele momento. |
| **P03.17 · Resolvido** | Reapresentar a cadeia concreta entre a atividade e a lacuna. Se a relação for hipotética, explicitar o que falta para confirmá-la. A regra vale também para dependências indiretas. |
| **P03.18 · Resolvido** | Para esta primeira entrega o usuário descreve um Motor sem interface gráfica construída pela equipe. O agente deve mostrar em linguagem direta a afirmação afetada, fonte, limitação e próxima ação possível e permitir chegar ao detalhe por assunto. A interação deve funcionar pelos canais do agente e pelo conhecimento navegável. |
| **P03.19 · Resolvido** | O agente investiga até considerar o pedido suficientemente respondido segundo sua natureza, escopo, critérios e implicações. Reporta dúvidas, pendências, incertezas e inconclusões e oferece aprofundamento conforme a resposta do Engenheiro. Mantém o aviso precoce de lacunas e o encaminhamento humano da criticidade material que permaneça incerta após a investigação autorizada. |
| **P03.20 · Adiado** | O usuário reservou para momento posterior a definição dos testes, validações e de quem poderá executá-los para verificar segurança, confiabilidade e precisão das bases. Permanece no grupo como decisão de sequência. |
| **P03.21 · Reformulada** | Pelo assunto e posição, esta é a segunda resposta identificada como “P03.2”. A dúvida do usuário é o significado da exceção de HUM-03. Sua presença no Motor inicial continua aberta. |
| **P03.22 · Parcial** | Direção expressa para que qualquer agente de IA possa navegar, ler, compreender, explicar e modificar qualquer informação da base no escopo autorizado, em toda profundidade aplicável e em tarefas de qualquer complexidade, buscando qualidade, rapidez e precisão com o menor custo em ACUs, tokens, contexto e recursos. Estrutura, hierarquia, ordenação, skills, ferramentas e instruções devem servir a isso. A atuação continua sujeita à autorização pertinente. A estrutura concreta, os compromissos entre dimensões e a prova de eficácia seguem em refinamento. A portabilidade desejada convive com o suporte específico, na primeira entrega, a Devin Web/CLI/Desktop e Claude Code. |

### Perguntas que precisavam de uma formulação melhor

**P03.8 · Em que momento duas indicações poderiam divergir?** Somente quando existirem duas indicações sobre o mesmo objeto. Por exemplo, num pedido “estude os repositórios de NC2”, uma lista fornecida para a tarefa inclui `itau-xp6-consulta-fatura`. NC2 e XP6 são distintas. Falta saber se esse item entrou por engano ou se deve ser consultado como dependência externa de NC2. Proposta: se nome e contexto forem coerentes, prosseguir. Se houver divergência material persistente, preservar o vínculo organizacional conhecido e esclarecer a finalidade da inclusão. Não há evidência de um cadastro conflitante no banco.

**P03.10 · O que acontece amanhã com o resultado de ontem?** Ontem o Motor analisou A em Alfa. Hoje o Engenheiro, em outra execução do Motor, pede apenas D, também de Alfa. Para o Micro, o resultado de hoje é de D. Para o Meso, a pergunta é o que a visão da Sigla deve fazer com a referência a A. Proposta: acrescentar D, preservar a revisão antes registrada de A e identificar que somente D foi estudado hoje. Se o Meso for apenas um agregador Git, o problema pode se resumir aos ponteiros dos submódulos e à indicação da revisão coberta nos próprios Micro. A resposta depende de P03.4.

**P03.14 · Como distinguir código, implantação e ocorrência observada?** Componente é a parte do software de que se está falando, como a API de propostas ou o worker de reenvio. Artefato é o pacote que se construiu a partir do código e pode ser implantado, como um JAR ou uma imagem de contêiner. Comportamento identificado no Git é o que as fontes permitem explicar em uma revisão. Exemplo: em A@r2, o código prevê nova tentativa após 503 se uma opção estiver ativa. A afirmação “essa regra está habilitada em HOM” requer evidência autorizada da versão implantada e da configuração pertinente. “O pedido X sofreu uma nova tentativa” requer evidência daquele evento. Pergunta residual: no Motor inicial, basta explicar a revisão e indicar a prova de ambiente que falta, ou ele também deve confrontar uma evidência de implantação que o Engenheiro disponibilizar por via autorizada? A inclusão de busca ativa em sistemas corporativos exigiria definição própria.

**P03.16 · O que dizer antes de conhecer todo o impacto?** Exemplo de primeiro aviso textual: “Em A@r1 encontrei o envio de `codigoSegmento` para C. Ainda não encontrei evidência de como C trata a ausência do campo. A análise de A continua. No momento, você só precisa tomar ciência.” Se o pedido já for retirar o campo, a última frase deve indicar a decisão que depende do contrato de C. O canal e o layout permanecem abertos onde não afetam esse comportamento. Pergunta residual: identificar no texto se o aviso é apenas para ciência ou se requer uma ação humana atende à necessidade inicial?

**P03.21 · Que execução está em discussão?** Trata-se de iniciar **localmente uma aplicação estudada**, em uma situação futura e excepcional. O agente esgotou as investigações autorizadas e restou uma dúvida material para a qual uma observação local específica pode discriminar as hipóteses. Oferece a alternativa de esclarecimento direto pelo Engenheiro. Se for propor a execução, apresenta dúvida, tentativas, finalidade, ambiente, dados, pré-requisitos, comandos e efeitos previstos. A execução exige permissão específica. Iniciar o próprio Motor e ler a documentação de execução são operações distintas. A decisão é se a v1 apenas entrega o esclarecimento pendente ou também prepara esse pedido excepcional. Uma observação local só serve para a condição local examinada. [HUM-03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md#hum-03) · [Consolidação do Motor, §1.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf)

### Regras por repositório e formato de documentação

Um exemplo sintético explicita a diferença entre descrever o contrato e explicar o efeito. A usa `POST /segmentos`. Nas respostas HTTP 200, o campo `situacao` pode valer `PENDENTE`. A regra do consumidor lê esse valor e, se a proposta estiver ativa, publica uma mensagem para revisão. A primeira informação pertence ao contrato de entrada/saída. A segunda explica uma condição em A, um efeito observável e uma relação com outra saída de A. Para afirmar o que faz o consumidor dessa mensagem, seria preciso evidência própria.

JSON admite texto explicativo e regras estruturadas, como condições, ação e evidência. Uma representação combinada também é viável: o contrato técnico pode ficar em um registro estruturado e a explicação de domínio em Markdown, ligados por uma referência estável na revisão pertinente. O problema prático é conseguir localizar e modificar a regra sem manter duas versões independentes do mesmo fato. Os formatos e a divisão física permanecem propostos. Exemplos de prova futura: um agente localiza o tratamento de `PENDENTE`, explica a condição, altera a informação autorizada e identifica o que precisa revalidar. Os testes, executores e métricas serão definidos no momento reservado em P03.20.

**Possível função do Meso em P03.4.** Imagine uma fila declarada no Terraform de um repositório da Sigla, alimentada por uma API e consumida por um worker de outro repositório da mesma Sigla. Um índice curto poderia apontar a quem publica, a quem consome e onde o contrato está documentado, quando houver evidência e o público tiver acesso. Se a mesma consulta já for bem atendida pelos Micro e seus ponteiros Git, é plausível manter somente a agregação e a configuração comum necessária. O exemplo serve para decidir se uma explicação própria da Sigla justifica o custo de manutenção.

### P03.13 · Três casos para conferir o critério

| Caso sintético | Efeito sobre o objetivo |
|---|---|
| **Ressalva controlada · já aceito no caso de A** | A emissão do campo está sustentada. O lado de C permanece desconhecido e a ressalva é definida, localizada, detalhada e referenciada em A. O onboarding de A pode terminar. Retirar o campo exige esclarecer C. |
| **Impedimento · exemplo proposto** | O objetivo declarado é explicar como uma proposta é aprovada ou recusada. A apenas encaminha uma decisão de um serviço cuja regra está inacessível. O Motor entrega o fluxo de encaminhamento. A explicação do critério de aprovação fica impedida. |
| **Criticidade incerta · exemplo proposto** | O objetivo é explicar o fluxo “padrão”. Duas fontes mostram caminhos diferentes e, mesmo após a investigação autorizada, falta saber se a variante pertence ao objetivo do Engenheiro. O agente comunica os dois caminhos e leva ao Engenheiro a dúvida sobre o alcance. O restante do fluxo pode continuar. |

### Dúvidas colaterais derivadas desta rodada

Os IDs C-P03 abaixo identificam desdobramentos desta edição. Eles se relacionam com as 77 perguntas originais e não alteram a contagem histórica.

| ID e dependência | Nova questão, exemplo e encaminhamento sugerido |
|---|---|
| **C-P03-01 · .1, .2, .6** | Até qual efeito deve ser rastreado o tratamento de uma integração em A? Um mesmo 200 pode gerar ações diferentes conforme campos da resposta e estado local. Sugestão: recuperar condição, decisão, efeito observável dentro de A e evidência. Ao cruzar uma fronteira sem evidência, aplicar .6. |
| **C-P03-02 · .1, .12, .22** | Se houver mais de uma representação, onde fica a definição de cada fato e como o agente detecta que uma explicação ficou desatualizada? Sugestão: atribuir uma origem verificável a cada fato, vincular contrato e regras e revalidar as referências no ciclo já previsto. Comparar possíveis formatos depois de aceitar o exemplo. |
| **C-P03-03 · .2, .19** | Quando o Engenheiro pede apenas “faça o onboarding deste repositório”, qual conjunto de perguntas sobre regras serve de objetivo para o agente poder parar? Sugestão: partir dos fluxos que o repositório oferece ou consome e verificar se o Micro explica condição, resultado, exceções e efeitos relevantes, respeitando .9 e .13. |
| **C-P03-04 · .7, .3** | Se a branch local tiver alterações sem commit, inclusive arquivos novos, a análise deve retratar o commit ou também a cópia de trabalho? O commit sozinho não identifica essas diferenças. Sugestão: detectar a condição e tornar explícita a fonte antes de tratar o resultado como reproduzível ou compartilhável. |
| **C-P03-05 · .7, .9** | Qual conduta adotar se o link remoto indicar uma branch específica diferente de `main` ou se `main` não estiver acessível? Sugestão: explicitar a divergência, aplicar .9 e não adotar silenciosamente outra origem. A regra já dada para o remoto continua sendo `main`. |
| **C-P03-06 · .1, .2, .12, .14** | Como apresentar parâmetros cujo valor efetivo é definido fora do repositório? Um timeout padrão pode ser substituído por uma variável no deploy. Sugestão: identificar nome, padrão, fonte da substituição e valor efetivamente evidenciado quando pertinente e autorizado. A existência de um header sensível também pode ser documentada sem copiar seu valor. |
| **C-P03-07 · .19, .20, .22** | Entre duas organizações que preservam toda a informação crítica, como comparar precisão, velocidade e custo para tarefas de complexidades diferentes? Uma alternativa que elimina uma exceção material já viola os axiomas. Falta definir como comparar as opções aceitáveis e aferir custo quando uma métrica é própria de determinada ferramenta. Sugestão: comparar os mesmos pedidos simples e complexos na fase de validação, sem fixar um orçamento universal agora. |
| **C-P03-08 · .1, .2** | Qual é o equivalente do contrato HTTP para uma integração por fila, tópico ou banco? Um worker pode precisar explicar a estrutura da mensagem e a ação após uma falha. Uma consulta ao banco pode depender do significado de resultado vazio. Sugestão: identificar entrada, saída, condição e efeito por tipo de integração e validar a seleção antes de impor campos universais. |

### Sequência sugerida

A próxima definição com maior efeito é **C-P03-01**, a profundidade das regras que tratam o retorno de uma integração. P03.4 é uma decisão de produto independente, anterior a P03.10. P03.8 só exige arbitragem se aparecer evidência de inconsistência. P03.20 permanece reservada para a etapa posterior pedida pelo usuário. Esta rodada registra respostas em conversa e neste caderno de trabalho. **NÃO PERSISTIDO no GitHub.**

[Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md) · [Especificação do Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Evidências e ressalvas de A](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md)

## Base de partida anterior à primeira rodada de respostas

| Ponto que pode parecer contraditório | Leitura que as fontes permitem | Questão que resta |
|---|---|---|
| A pode concluir o onboarding embora C não tenha sido analisado | O aceite vale nos dois casos de A, com todas as lacunas percebidas definidas, localizadas, detalhadas e referenciadas no próprio A. Em um caso, A envia o campo a B e C e há evidência sobre o tratamento de B. No outro, A tem duas regras de segmento e falta saber quando cada uma se aplica. | Caracterizar a suficiência para outros objetivos e mostrar exatamente qual ação depende da resposta. |
| O agente avisa cedo e investiga com autonomia | Ao perceber uma lacuna, já a cataloga e comunica. Pode prosseguir nas investigações autorizadas e reapresenta a ressalva quando o pedido depende dela, direta ou indiretamente, inclusive fora do Workspace. Persistindo incerteza sobre criticidade após a investigação, leva a questão ao Engenheiro. | Especificar o conteúdo do primeiro aviso, o que justifica a reapresentação e como distinguir informação de pedido de intervenção. |
| O Motor deve conhecer profundamente um repositório e consumir pouco contexto | A análise contempla finalidade, responsabilidades, regras, fluxos, código, contratos, integrações, infraestrutura, dependências, versões, testes e execução documentada. A consulta posterior parte do contexto suficiente para a tarefa, com acesso às fontes, exceções e contraevidências pertinentes. | Definir o mínimo demonstrável por tipo de repositório e como verificar a qualidade de uma recuperação econômica. |
| Meso, Macro, raiz de instalação e Workspace aparecem em textos de épocas diferentes | Micro é o repositório individual. Meso é o repositório específico da Sigla/conta com Micro como submódulos. Macro é o workspace Git com Meso como submódulos. O Motor prioritário produz Micro e Meso. O Workspace de atividade tem estado próprio e pode consumir várias Siglas. | Decidir as identidades físicas ainda em aberto e os contratos das saídas. |
| O agente consulta uma fonte, sugere um vínculo ou atua no sistema | Para repositório, o agente sugere, o Engenheiro decide e, quando autorizado, o agente inclui o submódulo. Para vincular Sigla à atividade, o agente sugere e o Analista permite a consulta aos índices. Direitos efetivos continuam por operação. | Definir quem efetiva o vínculo permitido da Sigla e quais informações podem circular entre públicos. |
| A especificação inicial deixava em aberto onde guardar o Workspace | A R06 registra uma branch por Workspace no repositório de Workspaces da Sigla do time/analista executor, informada pelo Engenheiro. A aprovação formal e delimitada do refinamento cabe ao Analista. O time decide o destino da branch quando a atividade termina. | Definir o sinal de término quando necessário, o layout interno, o acesso histórico e a relação física com o Meso. |
| Mudou o contrato, mas uma orientação continua visível | Mudança agêntica exige atualização ou revalidação no mesmo ciclo de commit/PR. Mudança externa detectada exige invalidar o uso como atual, reconciliar e verificar. Sem monitor, a detecção ocorre na próxima leitura ou ciclo. | Especificar o alcance da invalidação, os gatilhos, a concorrência e a prova de retorno à validade. |
| A aplicação usa uma regra e alguém precisa conhecer a política do produto | O Motor pode evidenciar a implementação em uma revisão. A conclusão sobre um ambiente exige prova de implantação. O Analista delimita a solução funcional. A autoridade para confirmar uma política de negócio ainda precisa ser caracterizada. | Decidir a saída arquitetural e qual fonte legítima resolve uma dúvida de negócio. |

A proibição de refatorar no onboarding e a exigência de autorização por operação atravessam todos os itens. Uma aplicação que o Motor conhece como executar continua sujeita às condições da exceção futura de HUM-03. A entrevista usa dados sintéticos. [Registro HUM-01–11](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md) · [Retificações](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md) · [Axiomas AX-01–10](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/fundacao/axiomas-arquiteturais.md) · [Dois aceites de A](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md) · [Workspace R06](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/WORKSPACE-R06.md)

## Dois exemplares propostos na abertura da entrevista

A e B foram indicados e pertencem a Siglas diferentes. C apareceu em uma fonte de A e ficou fora da seleção. Os nomes de arquivos, linhas, revisões curtas e Siglas abaixo são fictícios. Servem para experimentar o conteúdo das bases. Não representam o esquema nem o layout definitivo.

| Exemplar | O que o engenheiro conseguiria ler |
|---|---|
| **Micro de A · revisão analisada a1** | “No fluxo de envio da proposta, A monta a mensagem para C e inclui `codigoSegmento`.” A montagem está em `src/EnvioDeProposta.kt`, linhas 38–52, e a identificação do destino está em `config/destinos.yml`, seção `proposta`, ambos em A@a1. Isso demonstra a emissão do lado de A. A evidência sobre B@b1 sustenta somente o tratamento observado em B. Faltam o contrato ou outra evidência pertinente de C para saber se ele aceita a ausência do campo. A pode terminar seu onboarding com essa ressalva documentada em A. A decisão de retirar o campo continua dependendo de C. |
| **Meso da Sigla Alfa · revisão do índice m1** | “Para esta execução foi analisado A@a1, pertencente a Alfa.” O índice aponta ao Micro de A e à ressalva localizável sobre C. B@b1 pertence à Sigla Beta e aparece como relação entre repositórios na medida permitida pelas fontes e pelos direitos. C tem uma relação observada a partir de A, cobertura do lado de C em aberto e Sigla não evidenciada no exemplo. Se faltar um inventário completo de Alfa, a cobertura total da Sigla permanece desconhecida. |

O leitor deve conseguir chegar do índice à afirmação e da afirmação à fonte, explicar a chamada de A e identificar a decisão que continua sem base. O formato acima é uma proposta para discussão. [Especificação do Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Pergunta de retomada](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/README.md)

## P03 · Perguntas e recomendações originais

As fichas abaixo preservam a abertura da entrevista. O [registro de fechamento](#fechamento-p03) apresenta as definições mais recentes e o [saldo anterior](#saldo-p03-r2) conserva a primeira rodada.

Frentes principais PE-03 e PE-04. Origem em D02-PEN-001/002, com D01-PEN-007/005/010. Os ensaios e contratos D02 oferecem candidatos que ajudam a formular as perguntas. O exemplo A/B/C e a R06 dão a precedência às definições posteriores no seu respectivo escopo. [Agenda P03](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#pendencias) · [Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MOTOR-E-WORKSPACES-DE-ATIVIDADE.md) · [Retomada temática](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md) · [PE-04](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/ESCLARECIMENTOS-ONBOARDING.md) · [Avaliação candidata](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/AVALIACAO.md)

### Saídas do Motor e cobertura da Sigla

<a id="p03-1"></a>

**P03.1 · Ao abrir o Micro de A, o que uma integração precisa mostrar para você conseguir explicá-la e conferir até onde a explicação vale?** · Agenda

Este é o conteúdo mínimo de **uma integração**. No exemplar, ver o campo em uma classe diz pouco sobre quem o envia, em qual fluxo e com qual destino.

*Recomendação.* Adotar como ponto de partida o fluxo e seu gatilho, origem e destino, dado ou contrato relevante, revisão e trecho que sustentam a explicação, lado ainda desconhecido e consequência prática. Ajustar esse mínimo pelo que você faria com a informação.

<a id="p03-2"></a>

**P03.2 · Além das integrações, que perguntas toda base Micro precisa responder para merecer uso como entrada em um repositório desconhecido?** · Agenda

Um serviço de decisão tem regras e contratos de entrada e saída. Um repositório de infraestrutura pode descrever recursos, dependências e efeitos sem expor uma API de negócio. A direção ampla de análise já está definida.

*Recomendação.* Usar um núcleo comum de finalidade, responsabilidades, pontos de entrada, fluxos, regras ou efeitos, dependências, operação documentada e meios de verificação. Indicar, por tema, o que foi demonstrado, o que não se aplica e o que não foi localizado.

<a id="p03-3"></a>

**P03.3 · Que precisão torna uma referência conferível por outra pessoa ou agente?** · Agenda

Uma pasta com quarenta arquivos não localiza a condição que omite um campo. Linhas de uma branch móvel podem passar a mostrar outro código. Um teste escrito prova que um caso foi especificado. Um resultado de execução é outra evidência.

*Recomendação.* Para cada afirmação material, indicar repositório, revisão e menor trecho identificável que sustenta a condição. Usar linhas, símbolo, cláusula de contrato ou seção conforme o material. Associar uma segunda fonte quando a conclusão depender das duas.

<a id="p03-4"></a>

**P03.4 · O que o Meso precisa acrescentar para que o engenheiro entenda a Sigla sem abrir todos os seus Micro?** · Agenda

O índice de Alfa pode listar A@a1. Para explicar o caminho de uma proposta, interessa também saber por que procurar A, qual relação atravessa a Sigla e o que é compartilhado ali, como contexto autorizado de infraestrutura.

*Recomendação.* Incluir o inventário coberto e suas revisões, a responsabilidade de cada Micro, as relações relevantes, o conhecimento realmente comum e os limites coletivos. Manter no Micro o detalhe próprio e apontar para a evidência conforme o público.

<a id="p03-5"></a>

**P03.5 · Como o Meso deve declarar a cobertura quando a seleção de repositórios é conhecida e o universo da Sigla é parcial ou desconhecido?** · Agenda

Se A foi o único repositório de Alfa solicitado e foi lido, a execução cobriu o pedido. Sem inventário autorizado da Sigla, continua impossível concluir que toda Alfa foi estudada. B está em Beta e C pode ter Sigla desconhecida.

*Recomendação.* Nomear o universo de cada contagem. Identificar selecionados, analisados integral ou parcialmente, inacessíveis e apenas referenciados. Só declarar o total da Sigla quando houver inventário adequado com origem e revisão.

<a id="p03-6"></a>

**P03.6 · Até que ponto representar uma relação quando só um dos lados foi estudado?** · Agenda

A publica um evento com destino conhecido. Sem a fonte de C, o Motor pode conhecer a publicação e ignorar qual consumidor lê o evento, as condições de consumo ou o retorno. Uma relação também pode envolver ramos, retornos ou ciclos.

*Recomendação.* Representar direção, contrato ou evento observado, fonte, lado conhecido e ponto onde a evidência termina. Permitir identificar o próximo documento ou repositório relevante. Manter inclusão na atividade e delimitação de solução sob suas autoridades já definidas.

### Entrada, limites da leitura e continuidade da coleta

<a id="p03-7"></a>

**P03.7 · O que o Engenheiro precisa fornecer ou confirmar para iniciar o onboarding de um conjunto de repositórios na revisão correta?** · Agenda

O pedido pode chegar como duas URLs de branch ou como uma lista da Sigla. Uma branch pode avançar enquanto B é obtido. Falta decidir quais ambiguidades exigem intervenção e quais dados o agente resolve sozinho.

*Recomendação.* Aceitar referências que o engenheiro já usa, resolver cada fonte autorizada a uma revisão imutável e devolver o conjunto efetivo. Se o pedido mencionar HOM, registrar também a finalidade e verificar a implantação antes de atribuir efeitos ao ambiente.

<a id="p03-8"></a>

**P03.8 · Qual fonte resolve a Sigla de um repositório quando nome, cadastro ou informação do solicitante divergem?** · Desdobramento

Um nome sugere Alfa, mas um cadastro acessível aponta Beta. Classificar pelo nome pode atribuir conhecimento ou acesso ao grupo errado. A correspondência fina entre Sigla, conta e domínio segue aberta.

*Recomendação.* Registrar a divergência, localizar uma fonte organizacional autorizada e pedir confirmação apenas se o conflito persistir e afetar a agregação. Manter a parcela válida do Micro utilizável enquanto o vínculo em disputa aguarda definição.

<a id="p03-9"></a>

**P03.9 · Qual resultado o Motor deve entregar quando parte do material indicado não pôde ser obtida ou examinada?** · Agenda

A e parte dos contratos foram lidos, mas B falhou por credencial, um arquivo de A está truncado ou faltou a revisão pedida. A ausência de um teste nas fontes lidas tem significado diferente de um diretório de testes inacessível.

*Recomendação.* Dar um resultado por repositório e por área material. Informar a revisão lida, o que faltou, o motivo conhecido, o efeito e o ponto para retomar. Preservar a análise independente de A e adiar a conclusão que exige B.

<a id="p03-10"></a>

**P03.10 · Quando o Motor encontra um Meso já existente, que resultado deve produzir nessa rodada?** · Desdobramento

Alfa já indexa D em uma revisão anterior. O novo pedido abrange somente A. Criar um índice vazio pode apagar da visão um componente legítimo. Reapresentar D como reanalisado também falseia a cobertura.

*Recomendação.* Reutilizar a identidade do Meso quando comprovada. Distinguir a cobertura desta rodada das entradas históricas preservadas. Se não houver Meso, identificar se a criação cabe à operação autorizada e indicar o que pode ser preparado localmente.

### Suficiência, contradições e intervenção humana

<a id="p03-11"></a>

**P03.11 · Que evidência basta para a ação concreta que a pessoa pretende tomar?** · Agenda

As fontes de A podem bastar para explicar que um campo é enviado. Para documentar uma promessa de compatibilidade, planejar a retirada do campo ou atribuir comportamento a C, o alcance exigido muda.

*Recomendação.* Registrar a ação avaliada e os elos indispensáveis à sua conclusão. Usar pelo menos um par de pedidos sobre a mesma evidência, um que possa avançar e outro que dependa de um elo ausente. Explicitar a parcela do planejamento que continua segura.

<a id="p03-12"></a>

**P03.12 · Quando duas fontes sustentam interpretações incompatíveis, que resultado deve aparecer até a divergência ser resolvida?** · Desdobramento

Um contrato marca o campo obrigatório, enquanto um teste documentado trata sua ausência. Podem refletir revisões, consumidores ou condições diferentes. As duas regras de segmento em A ilustram outro caso em que o nome não determina precedência.

*Recomendação.* Comparar objeto, revisão, condição e natureza das fontes. Expor os trechos conflitantes, a leitura que cada um sustenta e qual evidência os distinguiria. Se a contradição afetar uma decisão, restringir a conclusão a seu alcance demonstrado.

<a id="p03-13"></a>

**P03.13 · Fora dos dois casos aceitos de A, qual diferença observável torna uma lacuna impeditiva para concluir o onboarding no objetivo declarado?** · Agenda

Descobrir uma exceção sem impacto no objetivo pode admitir ressalva. Se nem o ponto de entrada do fluxo principal puder ser identificado, certificar que esse fluxo foi compreendido passa a ser inseguro. Mais de uma lacuna pequena pode afetar o mesmo elo.

*Recomendação.* Avaliar impacto sobre uma afirmação indispensável ao objetivo e possibilidade de delimitar o que ainda vale. Comparar um caso aceitável, um impeditivo e um de criticidade incerta. No último, o Engenheiro decide após a investigação cabível.

<a id="p03-14"></a>

**P03.14 · Qual evidência da implantação permite estender uma afirmação de uma revisão Git a um ambiente específico?** · Desdobramento

Um contrato mudou na branch da história, enquanto a informação sobre HOM se refere a outra revisão. Para duas aplicações ou regras ativadas por configuração, uma única versão pode não descrever o fluxo inteiro.

*Recomendação.* Partir de uma evidência autorizada que ligue componente, artefato ou revisão ao ambiente pertinente. Incluir a configuração material quando ela muda o comportamento. Se faltar o vínculo, responder apenas sobre a revisão observada e identificar a verificação faltante.

<a id="p03-15"></a>

**P03.15 · O que deve chegar ao responsável quando o agente já investigou e precisa de intervenção?** · Desdobramento

Ao encontrar duas regras de segmento, avisar o usuário é imediato. A intervenção posterior é diferente se faltar uma cláusula de contrato, se faltarem direitos para consultá-la ou se o time precisar definir uma regra de produto.

*Recomendação.* Levar uma pergunta específica, com objetivo, hipóteses ainda compatíveis, fontes e tentativas autorizadas, ação afetada e menor esclarecimento necessário. Na exceção futura de execução local, preservar todos os requisitos de HUM-03 e a alternativa de resposta direta.

### Comunicação, uso e avaliação

<a id="p03-16"></a>

**P03.16 · Que conteúdo e forma tornam o primeiro aviso compreensível enquanto o impacto ainda está em investigação?** · Agenda

O agente encontra a chamada a C antes de saber quais histórias a utilizam. Uma mensagem genérica como “onboarding parcial” esconde a dúvida. Esperar o fim da varredura violaria o momento já acordado.

*Recomendação.* Apresentar a lacuna concreta, onde surgiu, o que já tem evidência, a consequência conhecida e o que está sendo investigado. Agrupar ocorrências relacionadas com acesso individual a cada uma e distinguir aviso de solicitação de decisão.

<a id="p03-17"></a>

**P03.17 · Como demonstrar ao usuário por que uma pendência antiga afeta o pedido que ele acaba de fazer?** · Agenda

Retirar o campo tem dependência direta. Alterar uma tarifa pode depender indiretamente de qual regra calcula o segmento. Uma simples mudança na descrição visual da tarifa pode ser independente desse cálculo.

*Recomendação.* Mostrar uma cadeia curta da atividade à regra e à lacuna, com o efeito sobre o passo atual. Quando a relação for só hipótese, sinalizá-la como tal. Validar o comportamento dentro do Workspace e em uma consulta isolada, mantendo consultáveis as demais pendências.

<a id="p03-18"></a>

**P03.18 · Como a pessoa deve conseguir localizar uma ressalva, conferir a fonte e saber o que ainda pode fazer, inclusive com necessidades de acessibilidade?** · Agenda

Em uma lista extensa, um ícone colorido ou um percentual isolado pode ocultar que só a decisão sobre C depende de evidência. Na ferramenta em texto, pode faltar a ação equivalente a abrir um detalhe.

*Recomendação.* Propor um resumo em linguagem direta, estados escritos, navegação por assunto e acesso ao trecho e ao histórico. Na interface escolhida, validar o percurso também sem depender de cor e, quando aplicável, por teclado e leitura assistida.

<a id="p03-19"></a>

**P03.19 · Que sinais justificam aprofundar a investigação ou encerrá-la com o limite registrado?** · Agenda

Ler todos os repositórios de duas Siglas para responder sobre uma chamada simples tem custo. Encerrar na primeira correspondência textual pode omitir o caminho de falha, uma exceção ou uma contraevidência.

*Recomendação.* Começar pelo índice e aprofundar quando houver elo material sem suporte, conflito ou risco para a ação. Finalizar a busca quando os elos necessários estiverem sustentados ou o limite autorizado estiver explícito. Comparar custo e qualidade sem impor agora teto de tempo, tokens ou arquivos.

<a id="p03-20"></a>

**P03.20 · Que demonstração permite aceitar a qualidade das duas bases para uso por outro engenheiro ou agente?** · Agenda

Um índice pode conter todas as seções e ainda conduzir ao contrato errado. Uma síntese mais curta pode omitir justamente a ressalva que impede a retirada do campo.

*Recomendação.* Entregar os dois exemplares a um leitor que não os produziu. Verificar se localiza a cláusula na revisão correta, explica o fluxo, identifica uma ressalva e evita a conclusão indevida. Registrar o material consultado e o esforço, preservando a verificabilidade e a independência de ferramenta.

### Limites da primeira versão do Motor

<a id="p03-21"></a>

**P03.21 · O Motor da primeira entrega deve oferecer o fluxo de solicitação de execução local excepcional?** · Agenda

A exceção e a autoridade do Engenheiro já estão delimitadas para a IDE futura. A inclusão desse fluxo no Motor inicial ficou expressamente aberta. Imagine que, depois de esgotar a investigação autorizada, só um esclarecimento do Engenheiro ou uma observação local específica distinguiria dois comportamentos.

*Recomendação.* Tomar uma decisão sobre o alcance da versão. Ela pode entregar a lacuna com pedido de esclarecimento ou também preparar a solicitação excepcional. Neste último caso, especificar tentativas, finalidade, ambiente, dados, pré-requisitos, comandos, efeitos, alternativa de resposta direta e permissão específica. [Consolidação do Motor, §1.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf)

<a id="p03-22"></a>

**P03.22 · De que forma o usuário precisa conseguir abrir e percorrer as bases produzidas localmente?** · Agenda

O Git canônico e o pertencimento de Micro/Meso estão definidos. Ainda precisam de escolha o formato de entrega, a organização local e a entrada por onde pessoas e agentes chegam ao índice, às evidências e às pendências. Por exemplo, ao abrir o repositório fora da interface da Plataforma, o engenheiro ainda precisa reconhecer qual base corresponde à revisão analisada.

*Recomendação.* Validar dois percursos com os mesmos exemplares, um na área local e outro a partir da revisão em Git. Escolher o formato e os diretórios após comprovar nesses exemplos a legibilidade, a portabilidade e o acesso às fontes. [Consolidação do Motor, §8.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf)

## P04 · Fichas da agenda original

O [roteiro da rodada atual](#p04-abertura) incorpora as respostas posteriores dadas em P03.

**Premissas.** A mudança realizada por um agente exige atualizar ou revalidar o conhecimento afetado no mesmo ciclo de commit ou PR, antes do fechamento. Alterações externas seguem a sequência detectar → invalidar → reconciliar → verificar. Na ausência de monitor, a detecção acontece na próxima leitura ou ciclo. Na composição multirrepositório, o fechamento depende da coerência entre revisões e ponteiros. O envio de uma contribuição de trabalho ao remoto não lhe confere aprovação. Direitos de consultar, armazenar, publicar e redistribuir têm escopos próprios.

A agenda atribui a P04 as pendências históricas D02-PEN-003 a 005. As perguntas abaixo detalham o efeito delas sobre Micro e Meso. Visibilidade padrão de repositórios e autenticação também dependem de P01. Os nomes A, B e C e as revisões `a1`, `a2` e `m1` são sintéticos. [Agenda da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#pendencias) · [HUM-05 a HUM-09 e D02-PEN-003 a 005](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/REGISTRO.md) · [D02-RET-002 e 004](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETIFICACOES.md) · [Distribuição e acesso r3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/DISTRIBUICAO-E-ACESSO.md) · [Consolidação do Motor, §§5.3, 7 e 8.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/referencias/CONSOLIDACAO-MOTOR-E-CONHECIMENTO.pdf)

<a id="p04-1"></a>

**P04.1 · Que atualização a primeira entrega deve conseguir fazer quando o engenheiro encontra uma revisão nova de um repositório já analisado?** · Agenda

O alcance muda o tempo até obter uma base utilizável e o trabalho que pode ser reaproveitado.

*Exemplo.* Entre `a1` e `a2`, A muda o campo de uma chamada. A explicação sobre o agendamento permanece sustentada por outra fonte.

*Recomendação.* Validar primeiro uma atualização acionada na consulta ou em um ciclo explícito, com reaproveitamento do que conserva evidência válida. Quando o alcance da mudança for incerto, ampliar a revisão e registrar a cobertura efetivamente reconferida.

<a id="p04-2"></a>

**P04.2 · Ao detectar alteração externa, até onde a conclusão deve perder a condição de atual?** · Desdobramento

A direção de invalidar está decidida. Falta delimitar a unidade atingida e os consumidores a alcançar por dependência direta ou indireta.

*Exemplo.* A muda a emissão de `codigoSegmento`. O Meso reproduz a afirmação antiga e uma tarefa usa essa afirmação para estimar o efeito de uma mudança tarifária.

*Recomendação.* Vincular a invalidação à afirmação e aos usos conhecidos que dependem dela. Se o consumidor estiver inacessível, registrar o alcance da verificação e a reconciliação pendente. Outras partes com evidência independente continuam disponíveis.

<a id="p04-3"></a>

**P04.3 · Que prova permite voltar a usar como atual uma conclusão reconciliada?** · Desdobramento

Esta questão trata da recuperação de conhecimento antes invalidado. Editar o texto e conferir sua correspondência com a nova fonte são atos distintos.

*Exemplo.* O Motor corrige a descrição do campo de A em `a2`. O teste encontrado ainda se refere a `a1`, e a aceitação de campo ausente em C continua desconhecida.

*Recomendação.* Restaurar somente as afirmações conferidas na revisão pertinente. Guardar referência anterior, evidência nova e resultado da verificação. A parte sobre C conserva sua ressalva própria.

<a id="p04-4"></a>

**P04.4 · Qual conjunto de revisões deve estar coerente para encerrar uma atualização que afeta o Micro e seu Meso?** · Agenda

Um ponteiro é a referência Git à revisão exata de um submódulo. O produto precisa permitir conferir a composição publicada, inclusive quando apenas parte das escritas ocorreu.

*Exemplo.* A já contém a correção em `a2`, mas o Meso `m1` ainda aponta a `a1` e descreve o contrato antigo.

*Recomendação.* Identificar a revisão efetiva de cada componente, a relação entre versões e a verificação pendente. A composição histórica pode continuar consultável como histórica. O ciclo da composição pretendida fica aberto até reconciliar e conferir os ponteiros pertinentes.

<a id="p04-5"></a>

**P04.5 · Que divergências entre duas contribuições sobre a mesma base o agente pode reconciliar autonomamente?** · Agenda

Uma diferença textual pode ser compatível, e um conflito de significado pode passar por uma combinação automática de arquivos.

*Exemplo.* Duas pessoas partem de `a1`. Uma descreve o campo como opcional na emissão. A outra o descreve como obrigatório segundo um contrato de outra revisão.

*Recomendação.* Reavaliar as duas origens e revisões. Integrar contribuições independentes após verificação. Se persistirem leituras incompatíveis do mesmo fato, preservar ambas com sua evidência e levar ao responsável a divergência exata.

<a id="p04-6"></a>

**P04.6 · Qual validação permite incorporar um esclarecimento do engenheiro às bases utilizadas por outras atividades?** · Desdobramento

A retroalimentação dos níveis pertinentes e autorizados já está prevista. A questão é quando a afirmação muda de estado e em quais consumidores ela pode entrar.

*Exemplo.* Um engenheiro esclarece em um Workspace que a regra da proposta vale para um canal específico. Outros consumidores consultam o mesmo Micro.

*Recomendação.* Identificar quem esclareceu, para qual canal, período e revisão o esclarecimento vale, que tipo de conclusão ele sustenta e quem tem autoridade sobre ela. Relacionar a correção aos registros pertinentes com direito de recebê-la. Uma observação local pode conservar esse alcance.

<a id="p04-7"></a>

**P04.7 · Que informação o Motor precisa ter para reconhecer quem pode autorizar uma operação sobre uma fonte específica?** · Agenda

Há modalidades pontual ou reutilizável e individual ou coletiva. É preciso definir como verificar que a operação concreta cabe na concessão, inclusive quando o titular ou o serviço muda.

*Exemplo.* A equipe pode consultar A no GitHub durante o inventário. Depois, um agente deseja consultar documentação legada para preencher uma lacuna ou operar em outra conta AWS.

*Recomendação.* Vincular a decisão à pessoa ou grupo competente, operação, objeto, finalidade, público, vigência e direito efetivo no serviço. Para retorno ao legado, preservar o aviso de inconformidade e a permissão pertinente. Para pesquisa externa, informar previamente finalidade, fonte e escopo e obter a autorização correspondente.

<a id="p04-8"></a>

**P04.8 · O que deve acontecer com usos futuros e material já obtido quando a autorização vence ou é revogada?** · Agenda

A mudança pode afetar a consulta da fonte, uma cópia local e consumidores de um derivado em condições diferentes.

*Exemplo.* Um usuário perde acesso a C depois de ler um contrato e gerar uma síntese destinada à equipe.

*Recomendação.* Suspender o uso dependente da concessão vencida e verificar separadamente os direitos de retenção e uso do derivado. Registrar destino, alcance e ações que dependem de responsável autorizado. A exclusão de um original exige aprovação expressa de objeto e revisão.

<a id="p04-9"></a>

**P04.9 · O que um leitor do Meso pode descobrir sobre uma dependência cujo repositório ele não pode ler?** · Agenda

Nome, caminho, origem e revisão podem revelar informação pelo próprio repositório pai, antes de qualquer leitura do destino.

*Exemplo.* Um índice acessível a outra Sigla identifica pelo nome um repositório privado. A credencial do leitor impede abrir o repositório, mas o nome já foi exposto no índice.

*Recomendação.* Definir o público autorizado a conhecer a existência e os identificadores do recurso antes de escolher onde gravá-los. Verificar o que um leitor vê diretamente no Git e tratar a política corporativa como dependência de PE-01.

<a id="p04-10"></a>

**P04.10 · Que conteúdo obtido legitimamente em uma fonte pode ser conservado e compartilhado em outro escopo?** · Agenda

A fonte pode permitir consulta e limitar retenção, cópia, síntese ou público destinatário. O próprio conteúdo derivado pode expor o que a origem restringe.

*Exemplo.* O engenheiro pode ler o contrato de C. O Meso de A tem um público maior. Uma cópia do contrato e uma frase que revele sua regra de exceção são dois objetos a avaliar.

*Recomendação.* Representar separadamente o direito de consultar a origem, conservar o derivado e distribuí-lo ao público pretendido. Usar referência autorizada com o mínimo de metadados permitido quando a reprodução exceder os direitos disponíveis.

<a id="p04-11"></a>

**P04.11 · Qual evento torna uma revisão de conhecimento disponível como referência validada aos demais usuários?** · Agenda

O Git é canônico, e uma contribuição de trabalho pode existir no remoto antes da validação. É preciso definir quem responde pela passagem, para qual destino e em qual escopo a primeira entrega a oferece.

*Exemplo.* Um agente envia em uma branch a correção do Micro de A. A equipe consulta uma revisão anterior no Meso.

*Recomendação.* Identificar a revisão proposta, a verificação exigida e a autoridade aplicável ao destino. Explicitar a revisão que o consumidor pode usar. Se a primeira versão só preparar a alteração localmente, registrar a contribuição e o passo de publicação ainda necessário.

<a id="p04-12"></a>

**P04.12 · O que deve acontecer quando o consumidor encontra uma revisão da base cuja representação ele só compreende parcialmente?** · Desdobramento

D02-PEN-005 mantém schemas, índices, adaptadores e nomes em definição. O comportamento diante de incompatibilidade pode ser especificado antes da escolha técnica.

*Exemplo.* Um produtor passa a distinguir “fonte inacessível” de “fonte fora da seleção”. Um consumidor antigo lê o restante, mas trata ambas como cobertura completa.

*Recomendação.* Exigir que a consulta preserve a distinção ou declare a limitação e recupere uma representação autorizada e inteligível. Avaliar a compatibilidade pelo significado que o usuário ou agente consegue verificar ao final.

## P01 · Distribuição e acesso — PE-01

A raiz é atualizada ao iniciar. As dependências da atividade são carregadas ao abrir o Workspace, com a credencial do usuário, na revisão indicada pelo pai e com indicação do acesso parcial. O acesso GitHub por Sigla e o acesso AWS independente são relatos sobre a empresa. Políticas e mecanismos reais precisam de validação no ambiente autorizado. [Distribuição e acesso, revisão 3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/DISTRIBUICAO-E-ACESSO.md)

<a id="p01-1"></a>

**P01.1 · Qual deve ser a visibilidade padrão do repositório de Workspaces de uma Sigla?** · Agenda

A escolha alcança conteúdo ativo e arquivado.

*Exemplo.* Uma atividade contém requisitos reservados à equipe. Uma branch própria ainda tem o público de leitura do repositório.

*Recomendação.* Usar o menor público compatível com a finalidade. Documentar quando uma exceção é admissível e quem pode autorizá-la segundo as políticas do banco.

<a id="p01-2"></a>

**P01.2 · Quem deve poder descobrir um mapa que referencia componentes de duas Siglas?** · Agenda

Metadados no pai podem revelar existência, origem e revisão.

*Exemplo.* O leitor de um mapa consegue ver que C participa de um fluxo, mesmo sem poder abrir C.

*Recomendação.* Escolher o público pelo que o próprio mapa revela. Aplicar a decisão ao local de publicação depois de P08.1.

<a id="p01-3"></a>

**P01.3 · Qual relação física a instalação deve manter com a raiz Git Macro?** · Agenda

A topologia Macro–Meso–Micro está definida, mas o clone de distribuição e a pasta local têm finalidades próprias.

*Exemplo.* A raiz comum recebe uma atualização mesmo se o usuário não puder baixar uma das Siglas.

*Recomendação.* Demonstrar o percurso desse usuário antes de decidir se o clone comum também pode exercer a função de Macro.

<a id="p01-4"></a>

**P01.4 · Como o engenheiro deve iniciar a Plataforma na primeira entrega?** · Agenda

Falta escolher a interação esperada e o resultado visível da atualização inicial.

*Exemplo.* O usuário abre a Plataforma pela manhã e precisa identificar a revisão comum obtida.

*Recomendação.* Definir uma entrada reconhecível e o que comprova a atualização. A equipe autorizada poderá selecionar o mecanismo compatível com a estação corporativa.

<a id="p01-5"></a>

**P01.5 · Que trabalho pode continuar quando a atualização da raiz falha?** · Agenda

A situação difere de uma dependência privada que falha mais tarde, ao abrir a atividade.

*Exemplo.* A máquina possui uma cópia de ontem e não consegue consultar o remoto.

*Recomendação.* Mostrar a última revisão confirmada e o impedimento. Delimitar o que é seguro consultar nessa condição e o que exige atualização verificada.

<a id="p01-6"></a>

**P01.6 · Quais operações com o remoto a primeira entrega precisa autenticar?** · Agenda

É preciso distinguir obter a raiz, ler dependências e enviar trabalho.

*Exemplo.* Uma credencial permite clonar A, mas não publicar o resultado derivado no Meso.

*Recomendação.* Fazer uma matriz de operação, destino e autoridade requerida. Deixar credenciais e fluxos corporativos para validação interna.

<a id="p01-7"></a>

**P01.7 · Que publicação remota o usuário precisa conseguir iniciar pela Plataforma?** · Agenda

O fechamento local de um estudo e a publicação da revisão são eventos distintos.

*Exemplo.* O Motor conclui um estudo local de A e o engenheiro deseja encaminhá-lo para revisão.

*Recomendação.* Decidir se o produto prepara o material, oferece publicação revisável ou prevê outra entrega. Vincular cada opção ao destino, à autorização e ao recibo correspondente. P04.11 trata de quando o conteúdo se torna referência validada.


## P02 · Ferramentas de IA — PE-02

As modalidades priorizadas são Devin Web, Devin CLI, Devin Desktop e Claude Code. O núcleo e as bases precisam continuar portáveis. O guia corporativo do Devin relata uma experiência específica. A equipe autorizada terá de validar mecanismos de obtenção, recursos e permissões na empresa. [Ferramentas](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/FERRAMENTAS.md) · [Referência corporativa do Devin](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/DEVIN-FERRAMENTAS.md)

<a id="p02-1"></a>

**P02.1 · Quais tarefas definem suporte suficiente em cada modalidade?** · Agenda

Explorar recursos próprios preservando o uso das bases comuns.

*Exemplo.* O mesmo estudo de integração é consultado no Devin Web e no Claude Code.

*Recomendação.* Comparar as modalidades por tarefa e resultado verificável, como localizar no mesmo Micro a evidência da chamada, e documentar diferenças aceitas.

<a id="p02-2"></a>

**P02.2 · Como cada modalidade deve encontrar o conhecimento comum?** · Agenda

Falta estabelecer quais instruções próprias são necessárias para chegar à mesma revisão.

*Exemplo.* Uma instrução de entrada do CLI precisa encaminhar o agente para a mesma base que o Desktop.

*Recomendação.* Manter a definição canônica em uma origem compartilhada. Usar configurações específicas para encaminhar o agente ao conteúdo ou expor capacidades próprias.

<a id="p02-3"></a>

**P02.3 · Em que momento a Plataforma pode preparar configurações específicas no repositório?** · Agenda

Gravar arquivos exige autoridade sobre o destino.

*Exemplo.* O Micro está disponível para leitura, mas acrescentar instruções a uma pasta específica da ferramenta exige escrita.

*Recomendação.* Prever proposta revisável com indicação do arquivo, revisão e finalidade. Validar internamente quem pode autorizar a escrita.

<a id="p02-4"></a>

**P02.4 · Qual evidência de versão efetiva é aceitável em cada modalidade?** · Agenda

A observabilidade do serviço Web pode diferir da de um cliente local.

*Exemplo.* A CLI exibe uma versão. A interface Web, neste exemplo, só permite verificar se um recurso está disponível.

*Recomendação.* Distinguir versão identificada, capacidade demonstrada e versão desconhecida. Testar quais evidências existem de fato no ambiente corporativo.

<a id="p02-5"></a>

**P02.5 · Qual é a continuidade esperada quando a atualização ou sua verificação falha?** · Agenda

O objetivo de trabalhar com a última versão já está definido.

*Exemplo.* Um agente instalado abre o Micro, mas não há comprovação de atualização da função exigida para a próxima ação.

*Recomendação.* Avisar prontamente e mostrar as tarefas cujos pré-requisitos ainda são demonstráveis, explicitando a ação dependente.


## P05 · Workspace de Atividades — PE-05

A R06 resolveu a escolha da Sigla que hospeda a branch. O Engenheiro informa a Sigla executora. Ele também decide sobre incluir repositórios sugeridos. O Analista permite vincular a Sigla para consulta dos índices. Encerramento do refinamento, término da atividade e estado da história são marcos diferentes. [Workspace de Atividades, síntese R06](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/WORKSPACE-R06.md)

<a id="p05-1"></a>

**P05.1 · Qual sinal, se necessário, caracteriza o término da atividade?** · Agenda

Só então o time escolhe o destino da branch ou da pasta.

*Exemplo.* O refinamento foi aprovado, uma história acabou, outra ainda tem tasks em aberto.

*Recomendação.* Começar por uma declaração do time sobre o conjunto. Avaliar se basta registrá-la ou se é preciso algum sinal adicional.

<a id="p05-2"></a>

**P05.2 · Quem efetiva o vínculo da Sigla depois da permissão do Analista?** · Agenda

A responsabilidade pela autorização já está definida.

*Exemplo.* O Analista permite consultar o índice da Sigla B a partir da atividade da Sigla A.

*Recomendação.* Comparar o agente efetivando o vínculo sob autorização e a efetivação por um membro autorizado. Em ambos os casos, registrar o resultado verificável.

<a id="p05-3"></a>

**P05.3 · Em que condições outro Workspace pode consultar um histórico?** · Agenda

A finalidade de recuperar contexto já foi aceita.

*Exemplo.* Uma atividade nova precisa saber por que o time arquivou uma decisão anterior.

*Recomendação.* Manter identificado o Workspace de origem e decidir que material a consulta pode apresentar ao público da nova atividade. Validar os limites de acesso reais.

<a id="p05-4"></a>

**P05.4 · O que alguém precisa encontrar na pasta de uma atividade para retomá-la?** · Agenda

O layout interno continua aberto.

*Exemplo.* Um colega abre uma atividade interrompida e precisa separar o requisito vigente, a hipótese descartada e a decisão que o explica.

*Recomendação.* Testar o layout com essa retomada e com uma consulta histórica. Escolher diretórios e formatos depois de definir o percurso de leitura.

<a id="p05-5"></a>

**P05.5 · O repositório de Workspaces deve acumular a função do repositório Meso?** · Agenda

São responsabilidades distintas que podem ou não compartilhar armazenamento físico.

*Exemplo.* Um Meso destina seus índices a um público mais amplo do que uma atividade com documentos restritos.

*Recomendação.* Confrontar público, finalidade, manutenção e arquivamento dos dois antes da decisão, acompanhando P01.1.

<a id="p05-6"></a>

**P05.6 · Quais informações permitem decidir sobre a inclusão de um repositório sugerido pelo agente?** · Desdobramento

O papel do Engenheiro e a consulta prévia já estão decididos. Falta concretizar a apresentação da sugestão.

*Exemplo.* Uma alteração de tarifa depende de confirmar o tratamento do campo em C. O Engenheiro precisa entender qual lacuna diminuiria ao incluí-lo, a revisão pertinente e que parte continuaria sem resposta.

*Recomendação.* Mostrar a razão da sugestão, a fonte da relação, o ganho esperado, a revisão e os direitos ainda necessários. Registrar a decisão e permitir retomar a parte independente se a inclusão for adiada.


## P06 · Agente, etapas e histórias — PE-06

O agente deve adaptar sua atuação à etapa. A aprovação formal e delimitada do refinamento cabe ao Analista. ServiceNow/IUClick é o destino definido para criar, modificar e alterar o status de histórias. O contrato corporativo e as permissões de cada operação exigem validação interna. [Atuação por etapa](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/ATUACAO-POR-ETAPA.md) · [R06](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/evidencias/WORKSPACE-R06.md)

<a id="p06-1"></a>

**P06.1 · Qual sinal determina a etapa de cada item?** · Agenda

Um Workspace pode conter histórias em etapas distintas.

*Exemplo.* A primeira história já está no planejamento de testes, enquanto outra ainda tem uma regra de negócio em aberto.

*Recomendação.* Identificar a etapa por item a partir do último marco comprovado. Permitir que o usuário corrija um enquadramento incorreto.

<a id="p06-2"></a>

**P06.2 · Que condição permite propor a passagem de uma etapa à seguinte?** · Agenda

A aprovação formal que encerra o refinamento já tem responsável.

*Exemplo.* Uma história tem critérios redigidos, mas a equipe ainda discute uma exceção material.

*Recomendação.* Especificar por transição o resultado exigido e o ato humano aplicável. Mostrar o que falta antes de sugerir avanço.

<a id="p06-3"></a>

**P06.3 · Como tratar uma mensagem que corrige uma etapa anterior?** · Agenda

A correção pode mudar decisões e artefatos derivados.

*Exemplo.* Durante o plano de testes, o Analista redefine o que caracteriza um pedido duplicado.

*Recomendação.* Recuperar a definição anterior e apontar a história, os critérios e os testes atingidos. Mostrar quais partes ainda podem continuar.

<a id="p06-4"></a>

**P06.4 · Que informação o agente precisa recuperar antes de retomar um item interrompido?** · Agenda

O estado do Workspace, a revisão do código e o status corporativo podem ter evoluído.

*Exemplo.* Outra pessoa retoma uma história depois que o contrato de integração mudou.

*Recomendação.* Entregar uma síntese recuperável de etapa, última decisão, referências, ressalvas e próxima ação, conferindo as revisões que sustentam a retomada.

<a id="p06-5"></a>

**P06.5 · O que conta como uma entrega suficiente em cada atividade do agente?** · Agenda

Falta concretizar competências, fontes e resultados por etapa.

*Exemplo.* Na regra contra duplicidade, a história precisa de comportamento observável e o plano de testes precisa incluir o caso de dois pedidos legítimos.

*Recomendação.* Construir um exemplo aceito por etapa sobre a mesma demanda. Usar os exemplos para derivar critérios, entregáveis e responsabilidades.

<a id="p06-6"></a>

**P06.6 · Quais transições de história no ServiceNow/IUClick o produto deve oferecer?** · Agenda

Os verbos gerais estão definidos, mas faltam os estados, gatilhos e atos válidos.

*Exemplo.* Depois do aceite do refinamento, criar uma história e alterar seu status posteriormente representam eventos diferentes.

*Recomendação.* Preparar uma matriz por transição com gatilho, papel autorizado, efeito esperado e evidência de sucesso. O responsável interno valida o contrato real.

<a id="p06-7"></a>

**P06.7 · Onde termina o suporte a tasks, subtasks e bugs na primeira entrega?** · Desdobramento

O detalhamento pelo agente já está previsto. A integração definida expressamente para histórias tem um alcance próprio.

*Exemplo.* O engenheiro quer decompor uma história em subtasks e depois vê-las no sistema corporativo.

*Recomendação.* Definir por tipo se a saída é uma descrição revisável ou se requer operação no sistema. Validar separadamente qualquer operação adicional pretendida.


## P07 · Extensões por escopo — PE-07

A direção para a primeira entrega, depois do onboarding, é que o agente possa incorporar e recuperar skills, instruções, comportamentos, documentação e ferramentas em cada escopo autorizado. O caso do MCP de IBM ODM ilustra a descoberta por dependência. A autorização para ler a documentação e a autorização para operar a ferramenta são verificadas separadamente. [Extensões por escopo](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/EXTENSOES-POR-ESCOPO.md)

<a id="p07-1"></a>

**P07.1 · Que informação mínima torna uma extensão apta a ser incorporada em cada tipo?** · Agenda

Uma instrução de leitura e uma ferramenta executável apresentam exigências diferentes.

*Exemplo.* Uma equipe quer incluir a orientação de uso do ODM e uma integração para consultá-lo.

*Recomendação.* Começar por finalidade, escopo de origem, revisão, tarefa de exemplo e atos permitidos. Definir a verificação apropriada a cada tipo.

<a id="p07-2"></a>

**P07.2 · Como o agente reconhece que uma extensão de outro escopo se aplica à atividade?** · Agenda

A recuperação deve funcionar mesmo que a pessoa desconheça seu nome.

*Exemplo.* Ao analisar uma resposta no consumidor, o agente chega pela dependência à orientação do integrador.

*Recomendação.* Fazer o agente explicar o caminho entre a necessidade e a extensão, incluindo a condição que torna o recurso pertinente.

<a id="p07-3"></a>

**P07.3 · Que regra resolve orientações incompatíveis de escopos diferentes?** · Agenda

Precedência funcional e permissão para executar uma operação são questões distintas.

*Exemplo.* Uma instrução da Sigla e uma do repositório indicam procedimentos divergentes para consultar a mesma decisão.

*Recomendação.* Expor a divergência e suas origens. Definir quem resolve o caso antes de fixar precedência automática. Incluir instruções comuns da raiz e sua aplicabilidade aos executores.

<a id="p07-4"></a>

**P07.4 · Como uma atividade descobre o impacto da atualização ou retirada de uma extensão?** · Agenda

É preciso conseguir localizar os consumidores da orientação afetada.

*Exemplo.* Um MCP é substituído durante o refinamento de uma história que ainda cita a versão antiga.

*Recomendação.* Preservar a referência histórica e testar se o usuário identifica quais orientações ainda são aplicáveis e qual dependência precisa de revisão.

<a id="p07-5"></a>

**P07.5 · O que o agente deve entregar quando encontra a extensão, mas não pode operá-la?** · Desdobramento

A permissão para conhecer o recurso já está dissociada da autoridade operacional.

*Exemplo.* O agente localiza a skill do ODM e o contrato emitido pelo integrador, mas não possui a permissão exigida para consultar a regra.

*Recomendação.* Entregar o que as fontes acessíveis demonstram e especificar qual evidência uma pessoa autorizada poderia obter. Conferir no banco as operações realmente disponíveis.


## P08 · Arquitetura e solução — PE-08

O Motor mapeia relações técnicas. O Analista delimita a solução do ponto de vista funcional. Preservar evidências já pertence à PE-03. A extensão da entrega arquitetural condiciona as perguntas seguintes. [Retomada do Motor e da Arquitetura](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md) · [Escopo da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#pendencias)

<a id="p08-1"></a>

**P08.1 · Qual entrega arquitetural o Analista precisa receber nesta versão?** · Agenda

As opções documentadas são evidências de relações, mapa candidato e base verificável.

*Exemplo.* Uma atividade atravessa duas Siglas e usa um componente que também serve a outra solução.

*Recomendação.* Comparar as três saídas com a mesma pergunta realista. Escolher a menor que permita ao Analista reconhecer e delimitar a solução.

<a id="p08-2"></a>

**P08.2 · Como o Analista expressa a fronteira funcional da solução?** · Agenda

O mecanismo depende da saída escolhida.

*Exemplo.* A regra antifraude participa de abertura de conta e de concessão de crédito, com papéis distintos.

*Recomendação.* Descrever finalidade, entrada, resultado e papel do componente em cada percurso. Registrar a decisão do Analista com seu alcance.

<a id="p08-3"></a>

**P08.3 · Como reconhecer a mesma solução entre revisões ou entre Workspaces?** · Agenda

É preciso decidir se a entrega arquitetural necessita de identidade própria.

*Exemplo.* Duas atividades chamam a mesma jornada por nomes diferentes.

*Recomendação.* Começar por uma referência estável e por quem pode confirmar equivalência, se o recorte escolhido exigir identidade persistente.

<a id="p08-4"></a>

**P08.4 · O que deve constar na revisão de uma solução para o leitor reproduzir sua composição?** · Agenda

Um mapa pode combinar componentes em revisões distintas.

*Exemplo.* Um componente passa para a revisão 2 e outro continua na revisão 1.

*Recomendação.* Preservar as revisões de cada relação técnica e da delimitação funcional que foi validada. Aplicar P04 aos itens afetados.

<a id="p08-5"></a>

**P08.5 · Qual manutenção da representação arquitetural cabe à primeira entrega?** · Agenda

Uma alteração pode afetar uma relação técnica sem mudar a finalidade da solução.

*Exemplo.* Um consumidor migra de chamada direta para evento e o processo de negócio continua com o mesmo objetivo.

*Recomendação.* Definir quando a atualização técnica basta e quando a nova composição volta ao Analista. Condicionar a escolha a P08.1 e o público do resultado a P01.2.

<a id="p08-6"></a>

**P08.6 · Quem responde pelo catálogo arquitetural e pela publicação de uma composição reconhecida, caso existam nesta versão?** · Agenda

A delimitação da solução pelo Analista já tem autoridade definida. Falta decidir a propriedade e o ciclo de publicação da representação.

*Exemplo.* Duas Siglas mantêm componentes de uma solução. Há um mapa candidato e uma composição funcional confirmada que mudam em momentos diferentes.

*Recomendação.* Definir quem mantém a identidade, confirma a passagem de candidato à revisão utilizável e escolhe o destino conforme o público autorizado. Avaliar nomenclatura, armazenamento e catálogo na raiz depois de P08.1.


## P09 · Conhecimento de Negócios — PE-09

Incorporar o significado de negócio que excede a análise técnica faz parte do escopo. A organização transversal ainda é hipótese. O caso sintético do novo canal permite avançar sem material interno. [Conhecimento de Negócios](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/notas/NEGOCIOS.md)

<a id="p09-1"></a>

**P09.1 · Qual pergunta de negócio deve orientar o primeiro exemplo?** · Agenda

Escolher uma cuja resposta altere um requisito.

*Exemplo.* O canal anterior exige análise manual. O novo canal deve encaminhar o mesmo caso?

*Recomendação.* Usar o exemplo do canal, ou outro sintético que o usuário reconheça, deixando explícito o que já se conhece pela implementação.

<a id="p09-2"></a>

**P09.2 · Que fonte pode demonstrar a regra de negócio aplicável ao caso escolhido?** · Agenda

Documentação técnica e evidência de execução sustentam o comportamento observado.

*Exemplo.* O código encaminha a proposta, mas só uma política ou orientação legítima esclarece se ambos os canais estão abrangidos.

*Recomendação.* Distinguir políticas, relatos e evidências operacionais. Validar com a área competente a abrangência da fonte e o acesso permitido.

<a id="p09-3"></a>

**P09.3 · Quem pode validar o significado da regra para a atividade?** · Agenda

A autoria de uma implementação não determina a autoridade sobre o produto.

*Exemplo.* O responsável pelo serviço conhece o encaminhamento atual, mas a área do produto pode ter autoridade para decidir sobre o novo canal.

*Recomendação.* Registrar o papel responsável, o alcance de sua manifestação e como solicitar o esclarecimento. Confirmar o responsável real apenas no contexto autorizado.

<a id="p09-4"></a>

**P09.4 · Qual unidade organiza o conhecimento para que as pessoas consigam encontrá-lo?** · Agenda

Produto, domínio, processo e jornada são candidatos.

*Exemplo.* A mesma política aparece em dois canais e atravessa várias soluções.

*Recomendação.* Testar a recuperação partindo da história e da regra, antes de decidir a unidade, sua transversalidade ou a estrutura física.

<a id="p09-5"></a>

**P09.5 · Qual é a menor resposta de negócio útil ao engenheiro e ao agente?** · Agenda

A saída precisa mudar concretamente o refinamento.

*Exemplo.* Ao escrever a história do novo canal, o analista precisa saber se o encaminhamento é obrigatório e que parte permanece indefinida.

*Recomendação.* Testar um registro com significado, alcance, fonte, responsável, vigência e consequência para a história. Manter a lacuna visível quando faltar confirmação.

<a id="p09-6"></a>

**P09.6 · Como saber qual orientação de negócio estava vigente no momento relevante?** · Agenda

A data de uma decisão de produto pode diferir da revisão do código.

*Exemplo.* Uma regra de análise manual termina no próximo mês, enquanto o código ainda conserva o fluxo anterior.

*Recomendação.* Registrar vigência, histórico e confirmação da área responsável. Vincular o efeito prático à história e aplicar P04 para revalidar os derivados autorizados.

<a id="p09-7"></a>

**P09.7 · Que público precisa ver a regra de negócio, sua justificativa e as eventuais exceções?** · Agenda

Uma política pode ser consultável por uma equipe e ter restrições de cópia.

*Exemplo.* O agente de outra Sigla encontra a referência à política, mas o Workspace tem público mais amplo que a fonte.

*Recomendação.* Definir com a área responsável quais referências ou resumos podem ser usados no destino. Aplicar as autorizações de P04 sem inferir direito de redistribuição.

## Como as decisões se encadeiam

| Quando surgirem estes casos | Usar estes itens juntos | Critério para a rodada |
|---|---|---|
| C03 · A contém duas regras de segmento e uma chamada a C. O caso do campo enviado a B e C permite examinar o limite de cada evidência. | P03.1, P03.3–6, P03.11–13, P03.16–18 | Um leitor localiza a evidência de A, reconhece o limite sobre C e entende a consequência para uma ação. |
| C08 · O contrato em que a resposta se baseava mudou. | P03.14, P04.1–6 | O leitor reconhece qual afirmação perdeu validade, quais usos são atingidos e que evidência permite retomá-los. |
| C01 e C04 · A raiz carrega, mas uma atividade entre Siglas só é parcialmente acessível. | P01.1–7, P03.5, P03.9, P04.7–10, P05.2–3 e P05.6 | A pessoa consegue explicar o que carregou, em qual revisão, quem pode ver o quê e qual parte pode continuar. |
| C02 e variação por modalidade · A ferramenta local está desatualizada. Na variação Web, a versão pode não ser observável. | P02.1–5, P03.20 e P04.12 | A verificação indica o que cada modalidade conseguiu demonstrar com a mesma base. |
| C05 · Uma correção de negócio chega durante o planejamento. | P04.6, P05.4, P06.1–6, P09.2–6 | Outro engenheiro consegue recuperar a mudança e localizar histórias, decisões e testes afetados. |
| C06 e variação posterior · O consumidor permite descobrir o MCP do ODM via dependência do integrador. Em outra rodada, o MCP é substituído. | P07.1–5, P04.2–4 e P04.7 | A orientação do consumidor aponta para a versão pertinente e o usuário distingue leitura, operação e autorização. |
| C07 · A aplicação encaminha o caso para análise manual e um novo canal entra na jornada. | P08.1–6, P09.1–7 | O Analista consegue delimitar a solução e identificar quem pode responder se o comportamento vale para o novo canal. |

Estes são critérios para revisar a futura especificação. Os cenários não foram executados como testes de produto. [Cenários C01–C08](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/ESCOPO.md#cenarios) · [Roteiro de revisão](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/roteiro/REFINAMENTO-E-REVISAO.md)

### Escolhas que podem esperar

- **Encaminhamento de engenharia.** A forma do Motor (programa, script ou conjunto de ferramentas), o que usa análise determinística ou assistida, os formatos, os nomes de arquivos, os adaptadores e os indicadores quantitativos devem ser avaliados contra os exemplos aceitos. Para esse confronto, a engenharia pode produzir alternativas e evidências sem exigir que o usuário desenhe a implementação. P03.19, P03.20, P03.22 e P04.12 definem o que elas terão de preservar.
- **Validação no banco.** O modelo de acesso por Sigla e serviço e as estruturas corporativas para atualização de ferramentas são relatos do usuário. As políticas, operações, autenticação, meios de obtenção, revisões observáveis e contratos internos de Git, AWS, ServiceNow/IUClick, Devin, Claude Code e ODM precisam de fontes e profissionais autorizados. Uma resposta de produto pode fixar o resultado desejado enquanto a viabilidade operacional permanece a verificar.
- **Decisões condicionais.** P08.1 determina quanta materialização arquitetural fará parte desta versão. Se a escolha for apenas preservar evidências de relações, os itens sobre catálogo, identidade, manutenção ou publicação de uma base própria podem ser adiados com a razão registrada. Em P06.7 ainda cabe decidir sobre operações corporativas adicionais. A segunda rodada confirmou a inclusão do fluxo excepcional de P03.21, com as condições de HUM-03.
- **Base e continuidade.** D02-PEN-006 trata da manutenção das cópias. D01-PEN-001/A está materialmente reconciliada no escopo R2. A parcela B dessa pendência registra que a transcrição original integral permanece sem recuperação. Isso não invalida as decisões reproduzidas. Os gates documentais do piloto e os 49 critérios operacionais não são pré-requisitos desta entrevista.

### Registro de continuidade na abertura de P04

| Campo | Situação na abertura de P04 |
|---|---|
| Questão inicial | P04.1 · Alcance da atualização incremental e critério de reaproveitamento. |
| Resposta e alcance | O [fechamento do P03](#fechamento-p03) registra a autorização entre Siglas e o uso imediato de atribuição declarada com origem e revisão. |
| Próxima revisão | Avaliar as respostas à [rodada de P04](#p04-abertura) por ID; P04.6 já tem uma resposta aplicável. P03.22 e P03.20/C-P03-07 continuam nos refinamentos reservados. |
| Persistência oficial | **NÃO PERSISTIDO no GitHub.** A base versionada é o HEAD citado no início. Este caderno é material de trabalho para a entrevista. |

**Verificação documental.** As instruções do Projeto foram recebidas automaticamente. O HEAD da branch da primeira entrega foi resolvido no GitHub e as leituras foram fixadas nesse commit. O manifesto da primeira entrega identifica a revisão funcional 1. O manifesto D02 da fundação identifica D02-doc-2, e a branch de consolidação foi confirmada em `8bbd93151640865995fa8a8dfe3d2d5db15da6ec`. Os tamanhos e SHA-256 das cinco cópias 00–04 disponíveis na conversa coincidem com o recibo versionado dessas Fontes. Isso permite identificar os documentos consultados. A aplicação de alterações futuras no Projeto e a publicação de decisões no Git exigem evidências próprias. [Manifesto da primeira entrega](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/primeira-entrega/MANIFESTO.json) · [Manifesto D02](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/docs/01-discovery/discovery-02/MANIFESTO.json) · [Recibo das cinco Fontes](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/5f1d502a0b75fa24eb7616f930c2cf0415485ec8/auditorias/prontidao-discovery-02/FONTES-NATIVAS-APLICADAS.json)
