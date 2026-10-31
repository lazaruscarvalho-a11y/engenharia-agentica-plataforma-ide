# D01-R2 — relatório de reconciliação e verificação

Revisão 2 documental. Escopo: correção exploratória do Discovery 01, PR #6 existente. Base consultada `d9e48c3d36598d40f9d2e38caf836bccb5fac97f`; fundação `f8d7c60955a1250ae4d94a428386787f4aaa24b0`. Sem merge, ratificação, ativação normativa ou mudança administrativa.

## Resultado e alcance

A [matriz](../../docs/01-discovery/discovery-01/MATRIZ.md) dispõe E01..E36 e P-A..P-L; o [registro único](../../docs/01-discovery/discovery-01/REGISTRO.md) preserva intenções, escolhas, restrições, relatos, propostas e hipóteses. Os 27 IDs da R1 permanecem; REL-001..008 têm classe retificada com fonte reproduzida e REL-009 é agrupador histórico/desdobrado. [Retificações](../../docs/01-discovery/discovery-01/RETIFICACOES.md) explicam as mudanças.

A evidência nova é declaração reproduzida no pedido atual, arquivada em [DOSSIE-REPRODUZIDO](DOSSIE-REPRODUZIDO.md), não recuperação técnica das mensagens originais. O recorte é literal, normalizado UTF-8/LF, acrescido somente de âncoras HTML e cabeçalho de proveniência; sua comparação com o trecho fornecido conferiu. SHA-256 do pedido original: `e611884b12ddcbfc2378674e124de5543ffc78eb8dff2a3700675bb379805a35`, 50.831 bytes.

## Auditoria semântica independente

O [parecer independente](AUDITORIA-INDEPENDENTE.md) confrontou cada uma das 36 âncoras e doze grupos, além das restrições e cobertura inversa. O auditor é distinto dos autores e recebeu fonte, arquivos congelados e critérios, sem gabarito de conclusões.

| Achado do freeze 1 | Correção | Rechecagem |
|---|---|---|
| Pergunta antecedente E12 continha alternativa não fornecida em D01-S05 | Removidos pergunta/alternativas/resposta literal reconstruídas; preservada escolha declarada e ausência do literal | Freeze 2: registro e índice corrigidos |
| Relações inversas de pendências não cobriam todo o escopo declarado na revisão | União de vínculos válidos; registro, índice e matriz alinhados aos escopos | Auditor conferiu 92 relações exigidas, presentes nos três destinos |

[Candidato congelado 2](CANDIDATO-CONGELADO.json): 15 arquivos, digest `b344b88e90f9d755e976ab7a0f645744e47c731ba4cdc8acd79599bfa376f95a`. Auditor confirmou 15/15 tamanhos e SHA-256. Nenhum achado material aberto identificado nesse recorte; não é garantia absoluta de inexistência de omissões. Saídas posteriores de empacotamento/relatório/recibo têm conferência separada e não são apresentadas como parte dos 15 arquivos auditados.

## Verificações documentais

- `node auditorias/discovery-01-r2/verificar_r2.mjs . --write`: **8 checks estruturais/de regressão e 13 casos negativos**, todos aprovados. [Resultado detalhado](TESTES-DOCUMENTAIS.json), [verificador](verificar_r2.mjs).
- A fonte arquivada fornece as 36 âncoras independentemente do índice. IDs históricos, referências canônicas e propostas são verificados; duas regressões cobrem os achados reais.
- Os contraexemplos estruturados exercitam omissão, resposta mal associada, promoção de proposta, leitura→escrita, migração→exclusão, main→PROD, submódulo→sync, acessível→compartilhável, relato→política, pendência oculta, fonte falsa/ausente, D02 incompatível e execução local pelo agente.
- Esse verificador é limitado a invariantes documentais e fixtures sintéticas; não é analisador semântico geral nem motor de autorização da IDE. A cobertura semântica é sustentada pelo confronto independente com as fontes.
- O [manifesto R2](../../docs/01-discovery/discovery-01/MANIFESTO.json) inventaria o pacote; `node auditorias/discovery-01-r2/verificar_integridade.mjs . --write` confere arquivos, hashes, links e âncoras. [Resultado](INTEGRIDADE-LOCAL.json) e [verificador](verificar_integridade.mjs). Evidências declaradas como posteriores são resolvidas/conferidas no commit separado.
- Manifesto R1: 11/11 arquivos conferidos no snapshot-base. Recibo R1 preservado sem reescrita; não é usado como prova de conteúdo R2.

## Persistência e continuidade

O [recibo R2 separado](RECIBO-PUBLICACAO.json) informa o commit efetivo de conteúdo, hashes e comparações remotas. Ele só declara fechamento material após o candidato ter sido publicado e reobtido pelo SHA. O próprio recibo é reobtido em commit posterior e sua prova/digest é comunicada fora dele, evitando autorreferência circular. Sem confirmação da atualização da branch e da comparação, o estado é preparado ou não verificado.

A [entrada D02 revisão 2](../../docs/01-discovery/discovery-02/RETOMADA.md) recupera escolhas e propostas sem executar o Discovery 02. A [prova de agente isolado](CONTINUIDADE-SUBAGENTE.md), produzida separadamente se disponível, registra referências iniciais e resultado observado. É evidência técnica de subagente sem histórico, distinta de nova conversa real iniciada pelo usuário. Nova conversa real e atualização/releitura nativa de Fontes/Instruções **NÃO EXECUTADAS** nesta missão.

## Fechamento de D01-PEN-001

**Eixo A:** materialmente coberto no escopo acessível E01..E36 e grupos relevantes; a conclusão verificada está condicionada ao estado real informado pelo recibo de publicação. A auditoria não apontou omissão material conhecida no freeze 2.

**Eixo B:** transcrição original integral **NÃO RECUPERADA**. D01-S06 retornou cinco turnos recentes, com respostas extensas truncadas; o dossiê do pedido permite reconciliar conteúdo sem alegar recuperação original.

Pendências de interpretação, especificação funcional, arquitetura e operação estão separadas na [revisão](../../docs/01-discovery/discovery-01/REVISAO.md); não bloqueiam indevidamente o fechamento histórico A ou exigem nova confirmação das escolhas declaradas.

## Limitações e critérios finais

Conferidos: identidade/revisão remota inicial; manifesto e estado; 36 âncoras; proveniência; respostas curtas; IDs e retificações; modelo/registro/matriz; pendências por categoria; guardrails; auditor distinto; congelamento; testes documentais; entrada D02. Publicação, hashes remotos, herdados, PR e continuidade têm resultado efetivo no recibo e prova posterior, não são inferidos deste checklist.

Não foram executados oráculos futuros D01-V* ou D01-R2-V*, funcionalidades da IDE, integrações corporativas, aplicações, pipelines novas, GMUD/hotfix, produção ou os 49 CA operacionais do PGC. Não há identidade/assinatura corporativa demonstrada por hashes. Dados novos sintéticos; sem transcrições empresariais ou segredos. Fontes/Instruções nativas não atualizadas, sem sincronização presumida. Decisões humanas declaradas não aprovam detalhes técnicos derivados.
