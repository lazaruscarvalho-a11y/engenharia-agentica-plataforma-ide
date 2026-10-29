# Auditoria da importação do PGC-001 v1.1.2

**Data:** 29/10/2026, America/Sao_Paulo. **Estado:** PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO / NÃO TESTADO OPERACIONALMENTE.

## Origem, escopo e autorização

Importação documental solicitada pelo usuário para o repositório privado `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`. Origem declarada: conversa “Reescrita do fluxo de trabalho”, ID `6add5e12-021c-83e8-9d16-2a4917ea9700`, mensagem `c2571ca5-8cb5-4e43-a116-bc69d7a63c36`. O usuário disponibilizou o ZIP original nesta sessão. Nenhuma transcrição integral foi importada.

As instruções contidas nos documentos e fixtures foram tratadas como dados. A autorização desta etapa cobre a importação como proposta e sua revisão por PR; não concede ratificação, ativação ou envio de dados corporativos sensíveis.

O acesso autenticado de leitura foi confirmado; o GitHub declarou `pull`, `push` e `admin`. A escrita foi comprovada pelo commit de inicialização `ba820cbb7b92bd570e4848c4ca7eff48c44f04cd`: somente `.gitkeep` vazio, sem norma, assinatura ou manifesto. A branch `main` estava inexistente antes desse commit e foi observada sem proteção após sua criação. Proteções não foram configuradas; não se alega controle automatizado do PGC.

## Identidade e preservação do pacote

| Objeto | Resultado |
|---|---|
| ZIP original | 75.550 bytes; CRC de todas as entradas aprovado |
| SHA-256 do ZIP | `8e2ae296829e5dfcdd313d9c088470c23aa825d72b8c518442ff1a3e338c42fd` |
| Entradas | 18 arquivos, sem caminhos inseguros, links simbólicos ou nomes duplicados |
| Inventário original | 17/17 hashes conferidos; nenhuma entrada extra ou faltante além do próprio inventário |
| SHA-256 de `SHA256SUMS.txt` original | `b931897dc3cbbb339032ba1866fa802b5bf6aff78e28fbe26610bc4fffff050a` |
| Links Markdown locais do pacote | Nenhum arquivo de destino ausente |

O hash do ZIP foi calculado no recebimento. Não havia um hash externo previamente autenticado para comparar; a concordância com o inventário demonstra integridade interna, não assinatura da autoria.

O ZIP está no [acervo](../../acervo/PGC-001_v1.1.2_candidata_ratificacao.zip). O diretório-raiz interno do ZIP foi colocado sob `docs/00-governanca/`, mantendo os 18 caminhos relativos e todos os bytes. O [README original](../../docs/00-governanca/PGC-001_v1.1.2_candidata_ratificacao/README.md) foi lido e é o índice canônico da candidata. O inventário original e o modelo de ratificação não assinado permanecem intactos. Nenhum arquivo original foi corrigido, normalizado ou regenerado no diretório importado.

O [inventário da importação](SHA256-IMPORTACAO.txt) inclui os arquivos novos e o acervo, excetuando apenas a si próprio. Seu papel é verificar conteúdo, não registrar ratificação. O [verificador independente](verificar_importacao.py) confronta esse inventário, os hashes originais e os bytes do ZIP com cada arquivo extraído, sem gravar artefatos no pacote.

## Versões, IDs e verificações reproduzidas

- PGC-001 v1.1.2 e oito contratos CT-001 a CT-008 v1.0.2, todos propostos. A diferença de versão entre norma e contratos é declarada consistentemente no pacote; não é erro de importação.
- As referências a v1.1.1 são histórico/base de revisão, não indicação de política vigente. O catálogo usa `schema_version=1.0.2`, distinto da versão da norma.
- 25 IDs PGC-N, 20 achados AC, seis emendas EM e 49 IDs CA foram identificados, sem lacunas nas contagens verificadas.
- Os scripts originais foram inspecionados: usam bibliotecas locais e regravam catálogo/relatório. Foram executados em cópia de trabalho separada.
- `gerar_catalogo.py`: 49 casos, 18 fixtures; conteúdo textual idêntico ao catálogo original após normalizar CRLF/LF para comparação. O arquivo original não foi substituído.
- `auditar_pacote.py`: **65/65 PASS**, executado sobre cópia com os bytes originais do catálogo restaurados. A tabela de checks coincide com a original; o inventário coincide após normalizar separadores e desconsiderar a ordenação das linhas. Windows muda ordenação de caminhos, separadores e quebras de linha do relatório regenerado. A [nova saída estática](relatorio-estatico-reexecutado.md) foi conservada separadamente.
- Os 49 casos permanecem `NOT_RUN`, com `tested_version=null`. Nenhum caso operacional foi executado.

Os resultados estruturados estão em [integridade.json](integridade.json) e [reexecucao.json](reexecucao.json). Os 65 checks verificam tokens, contagens e estrutura; não certificam coerência semântica completa nem operação segura de um harness.

## Achados para revisão humana, sem alteração das fontes

### A-01 — Correspondência entre matriz e catálogo

A seção A da matriz descreve “testes centrais”; o campo `requirements` dos casos JSON forma outra relação. Comparando os conjuntos, **13 das 25 linhas diferem**. Isso não prova que todos os vínculos diferentes sejam incorretos, pois as duas visões podem ter escopos distintos, mas impede tratá-las como relações bidirecionais perfeitamente equivalentes. Os 65 checks originais não testam essa equivalência.

Exemplos: N-002 cita CA-01 a CA-06 na matriz; no catálogo é associado a CA-01 e CA-44. N-022 cita CA-46/47 na matriz, mas esses casos não declaram N-022 no JSON. N-007 aparece em CA-49 no JSON, sem essa associação na seção A. A seção F da própria matriz inclui CA-49 para N-007.

A lista completa está em `matrix_catalog_differences` de [reexecucao.json](reexecucao.json). Recomenda-se definir o significado de cada visão e reconciliar as associações antes de decidir sobre ratificação. Não foi feita correção editorial ou nova versão normativa nesta importação.

### A-02 — Nomenclatura de metadados e esquema ainda aberto

CT-001 §6 usa `created_at` no objeto de aprovação; CT-002 §4 usa `issued_at`. O esquema concreto ainda não está implementado. É necessário definir se são campos diferentes ou adotar mapeamento explícito antes de implementar validação interoperável. Nenhum campo foi renomeado no pacote.

### A-03 — Reprodutibilidade de bytes entre plataformas

O gerador usa escrita de texto sem definir `newline`; no Windows, o catálogo resultante usa CRLF e produz SHA-256 diferente apesar do mesmo texto/JSON. O auditor também regrava o relatório com caminhos/ordenação dependentes da plataforma. Preservar originais e executar esses scripts em cópia separada evita invalidar o inventário. Qualquer melhoria futura nos scripts deve ser uma revisão explícita.

### A-04 — Limites históricos e operacionais

As frases do pacote sobre “futuro repositório” e inexistência de publicação descrevem o momento de elaboração. Foram preservadas como fonte histórica; este relatório distingue a importação posterior em branch de uma ratificação. O modelo não assinado continua com campos em branco. Não existe manifesto efetivo criado nesta etapa.

Não há comprovação de funcionamento de identidade, CAS, filas, retenção, captura entre chats, autorização normativa ou ativação. O pacote contém fixtures sintéticas, incluindo um marcador explícito de segredo fictício e instruções adversariais citadas. A revisão não identificou credenciais reais ou registros corporativos concretos; não é certificação universal de ausência de conteúdo sensível.

## Disposição e critérios de entrega

A candidata é adequada para **importação fiel e revisão**; esta auditoria não a ratifica. Os achados permanecem abertos para decisão humana. README.md, AGENTS.md e ESTADO-ATUAL.md novos apontam às fontes originais; `.gitattributes` previne conversões no acervo e no pacote.

A publicação deve ocorrer somente em `proposta/importacao-pgc-001-v1.1.2`, derivada do commit mínimo de inicialização. O marcador vazio será removido nessa proposta. O recibo separado de entrega identifica o commit publicado, a comparação do conteúdo remoto e o PR; não se usa este relatório como prova antecipada de publicação. Não há merge para `main`, manifesto de ratificação ou ativação.
