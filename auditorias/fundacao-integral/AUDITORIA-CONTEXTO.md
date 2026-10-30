# Auditoria independente de contexto e pacote ChatGPT

## Identificação e alcance

- Auditor: subagente novo, sem histórico da conversa de produto; recebeu somente caminho do repositório, revisão congelada, escopo e restrições da auditoria.
- Revisão local auditada: `5f3a168849a9fc18a70e2dca9a20becb9ff39eb3`.
- Branch observada: `proposta/fundacao-integral-pm-fund-001-003`.
- Árvore inicial: `git status --short` vazio.
- Natureza: ensaio técnico independente de recuperação por arquivos; não é nova conversa real iniciada por usuário, não demonstra memória nativa e não configura Projeto ChatGPT.
- Único arquivo autorizado a criar/alterar no repositório: este relatório. Artefatos de execução serão temporários fora do repositório. Nenhuma publicação remota está autorizada ou será alegada.

## Registro inicial cego — antes de aprofundar a auditoria

Registro feito após ler somente `README.md`, `AGENTS.md` e suas entradas de recuperação: `ESTADO-ATUAL.md`, `docs/fundacao/visao-produto.md`, `metodologia-fases.md`, `roteamento-contexto.md`, `protocolo-sessoes.md`, `docs/01-discovery/INICIO-DISCOVERY.md` e `harness/governanca_assistida/OPERACAO.md`. `docs/chatgpt/*`, scripts de empacotamento/verificação e relatório final ainda não haviam sido lidos.

| Pergunta recuperada | Resposta independente | Fontes lidas |
|---|---|---|
| Qual é o produto? | Uma Plataforma/IDE corporativa de engenharia de software agêntica para coordenar conhecimento, discovery, repositórios, requisitos, execução, agentes, testes e supervisão humana. O harness documental é auxiliar; frontend/backend/IDE final ainda não foram implementados. | `README.md` abertura; `ESTADO-ATUAL.md` §Produto e fase; `docs/fundacao/visao-produto.md` §Problema e resultado pretendido e §Fronteiras |
| Em que fase está? | Fundação documental e harness inicial na fase 00, em branch de proposta para revisão/auditoria. Fase 01 preparada para começar; fases 02–09 ainda não executadas. Stack, requisitos detalhados, UX, métricas e primeira fatia de valor aguardam discovery/aprovação. | `ESTADO-ATUAL.md` §Produto e fase; `docs/fundacao/metodologia-fases.md` §Fases 00–09; `docs/fundacao/visao-produto.md` §Riscos |
| Qual é o método? | Sete etapas: discovery; especificação aprofundada; revisões profundas; plano de implementação/testes/validações; prompts-mestres especializados; prompt final de execução; contexto e paralelismo útil transversal. Há mapa proposto de fases 00–09 e gates; não é autorização para antecipar implementação. | `docs/fundacao/metodologia-fases.md` §Sete etapas, §Fases 00–09 e §Gates |
| Qual é a governança vigente? | PGC-001 v1.1.3 e CT-001..008 v1.0.3 são candidatos não ratificados; v1.1.2 e acervo histórico devem ser preservados. Branch/PR não equivalem a ratificação. Não há autorização de merge, C2/C3, produção, aceite humano fictício ou mudança administrativa. GOV-REG-0001 tem aceite histórico específico que não aprova a fundação. | `AGENTS.md`; `ESTADO-ATUAL.md` §Governança e harness; `README.md` §Governança preservada |
| Que estado e persistência são demonstrados? | O repositório versionado é o ponto de continuidade; snapshots em Fontes possuem revisão própria e não sincronizam automaticamente. Persistência exige recibo e releitura do destino por commit. Projeto ChatGPT está explicitamente NÃO CONFIGURADO nesta missão. Não há captura contínua de conversas; histórico original recuperado é parcial. | `ESTADO-ATUAL.md` §Conhecimento e continuidade e §ChatGPT; `docs/fundacao/protocolo-sessoes.md` §Persistência assistida e §Ao encerrar |
| O que é o harness? | Piloto C1 histórico de preparação/validação/diário/Gateway assistido/recibos, apenas sintético e com aceite de registro específico. Extensão declarada de captura C0 e adaptador SQLite local/sintético. Não são IDE, autenticação humana ou integração remota. Os 49 CA operacionais PGC permanecem NOT_RUN. | `harness/governanca_assistida/OPERACAO.md` §Componentes, §Evidência humana e §Falhas e limites; `ESTADO-ATUAL.md` §Governança e harness e §Verificação e riscos |
| Qual é a próxima ação? | Iniciar discovery exploratório C0/C1 com um caso concreto de demanda, dores, atores, jornada atual e resultado desejado. É possível prosseguir sem ratificar normas. Configuração nativa requer sessão autenticada/interface autorizada; merge da cadeia de PRs e ratificação são decisões humanas separadas. | `ESTADO-ATUAL.md` §Próxima ação e decisões humanas; `docs/01-discovery/INICIO-DISCOVERY.md` §Sequência recomendada |

Limite desta recuperação: os fatos acima são o que os documentos afirmam; a leitura inicial ainda não comprova os executáveis, a configuração externa nem a precisão histórica do relato. Não recebi respostas esperadas antes de produzir esta tabela. A existência de um stub pendente de relatório final, se encontrada depois, não será classificada por si como defeito.

## Auditoria aprofundada — conclusão no snapshot congelado

Recuperação documental inicial: **SUFICIENTE NO ENSAIO TÉCNICO** para identificar produto, fase, método, governança, estado, harness e próxima ação. Configuração nativa e nova conversa real de usuário: **NÃO TESTADAS / NÃO DEMONSTRADAS**. Nenhum teste local recebeu valor de ratificação ou dos 49 CA operacionais.

Achados no commit auditado: **0 P0, 1 P1, 1 P2**. O empacotador desse snapshot precisa corrigir a prova de revisão antes de um pacote ser descrito como snapshot remoto verificado. **Os dois achados foram depois corrigidos pela coordenação e rechecados no delta, com resultado registrado ao fim deste relatório.** A presença do stub `RELATORIO-FINAL.md`, explicitamente pendente de auditoria, **não é achado**.

### CTX-001 — P1 — O SHA informado não vincula os bytes exportados à revisão

- Local: `harness/empacotar_chatgpt.py:13–17,39–50` no commit congelado. `--commit` passa apenas por regex; `read_bytes()` lê a árvore atual de `ROOT`. O SHA informado é copiado no cabeçalho e no recibo sem verificar objeto Git, existência remota, árvore ou equivalência de bytes.
- Contrato documental: `docs/chatgpt/MANIFESTO-FONTES.md:7,34–35` exige commit imutável e hashes exatos; `INSTRUCOES-PERMANENTES.md:5,13` pede confirmação de revisão e releitura imutável. Hashes de arquivos corretos não provam, sozinhos, que esses arquivos pertencem ao SHA declarado.
- Reprodução negativa A: com `--commit aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`, o comando retorna **0**, gera 28 fontes e sete arquivos, e rotula todos como snapshot desse SHA. A consulta `git cat-file -e <SHA>:ESTADO-ATUAL.md` falha. Os metadados das 28 fontes são **idênticos** aos do pacote com SHA verdadeiro.
- Reprodução negativa B: com o SHA Git local existente `20f1c689cb53967964d55574136d7ed78f84cc6b`, também retorna **0** com os mesmos metadados atuais. A comparação independente de `git show <SHA>:<path>` detecta **17 das 28 fontes divergentes ou ausentes** nessa revisão. Exemplo: `ESTADO-ATUAL.md` naquele SHA tem SHA-256 `1de5b84b55e9eefe30c15e178d19d4cf814cf334611d5bd1dda065644681d81d`, enquanto o arquivo exportado como se fosse daquele SHA tem `c5dcf4b766ad1b5d24e598ba08815397348aaaf18294ee9c393976c27e63c3bc`.
- Efeito: um operador pode produzir recibo internamente consistente e ZIP íntegro, porém com proveniência de revisão falsa. A nova conversa não consegue determinar o estado exato pelo SHA do recibo e pode retomar documentos diferentes dos publicados. Isto também permite empacotar alterações ainda não registradas como se fossem publicadas.
- Correção requerida: obter bytes da revisão imutável, ou exigir prova da árvore dessa revisão e comparar **todos** os arquivos exportados, inclusive os três auxiliares. Rejeitar SHA sem prova, caminho fora da árvore, bytes divergentes e atualização concorrente da fonte. Um SHA local deve ser marcado como ensaio, sem alegação de publicação remota. Adicionar testes negativos para SHA inexistente, revisão antiga e bytes locais modificados.
- Evidências: `work/acx5/resultados.json` e `evidencias-aprofundadas.json`, fora do repositório. ZIPs negativos A/B: `2f476c8208a429e61245cb470146372ff78cbeea75fa554bfa87e9db51057bcf` e `014f1cb63db64e75a09eff8c99e94adbac034bf23cf6613c124302e070fb5888`.

### CTX-002 — P2 — Contratos selecionados ausentes são omitidos silenciosamente

- Local: `harness/empacotar_chatgpt.py:27–29`. A coleção CT-001..CT-008 é descoberta por `glob('*.md')`, em vez de validar a lista esperada. Um caminho ausente desaparece da seleção antes da leitura e não aciona erro.
- Contrato documental: `docs/chatgpt/MANIFESTO-FONTES.md:27` seleciona CT-001..CT-008 e `:35` determina interromper se algum caminho faltar.
- Reprodução A, somente em cópia descartável: retirar `CT-001-classificacao-aprovacao.md` e executar com o SHA congelado. Resultado **0**, ZIP íntegro, apenas **27 fontes**.
- Reprodução B, na mesma cópia descartável: retirar todos os oito contratos. Resultado **0**, ZIP íntegro, apenas **20 fontes**; continua existindo `FONTES-02-GOVERNANCA-CANDIDATA.md` e o mesmo cabeçalho de candidata.
- Efeito: uma cópia parcial do repositório aparenta ter produzido o conjunto curado completo. O recibo enumera a omissão, mas o processo não apresenta o erro exigido e a continuidade por contrato pode falhar depois do upload.
- Correção requerida: declarar os oito caminhos obrigatórios, validar existência e integridade antes de criar o destino e testar ausência individual e total. Conferir uma árvore só dos arquivos descobertos por `glob` não corrige esta lacuna.
- ZIPs negativos A/B: `808e781b355f11f167ae4adbcfc77a611b8b8bd8e56b736443b72966417c8046` e `144d50a415db072bf31b0ef6889bb8f6a50a0d5dcf46c52e1c10f37b4d59af92`.

## Alegações conferidas sem achado

| Tema | Conclusão e provas |
|---|---|
| Configuração real | `CONFIGURACAO.md:3,7–9` e `ESTADO-ATUAL.md` mantêm NÃO CONFIGURADO, upload/releitura não executados. O código só exporta arquivos, não contém cliente do ChatGPT e fixa no recibo `configuration=NAO_CONFIGURADO` / `upload=NAO_EXECUTADO`. A narrativa de acesso anterior não foi reexecutada por este auditor e permanece relato documental, sem promoção a prova independente de conta/sessão. |
| Instruções e Fontes | O documento de Instruções é separado dos três bundles. Sua exportação e os dois auxiliares foram comparados byte a byte ao commit local congelado, com êxito. O uso prescrito distingue campo Instruções de Fontes (`MANIFESTO-FONTES.md:9`; empacotador `:48–57`). |
| Limites do produto | O manifesto `:30` manda confirmar quantidade/tamanho na interface e não estabelece limite universal. Tamanho real do ensaio: Fontes-01 85.476 bytes, Fontes-02 111.952 bytes, Fontes-03 25.456 bytes; isso não demonstra aceitação pela conta/UI. O orçamento de contexto é declarado heurística operacional. |
| Sincronização e continuidade | `INSTRUCOES-PERMANENTES.md:5,13,19`, manifesto `:36–40` e configuração `:22–24` separam upload, aplicação de instruções, recuperação, persistência e vigência. Não prometem atualização automática, memória entre chats nem atividade contínua. A recuperação cega deste relatório só demonstra leitura de arquivos por processo novo. |
| Segurança e autoridade | `INSTRUCOES-PERMANENTES.md:7,15,17` preserva proposta versus aprovação, candidata não ratificada, limites de escrita, dados sintéticos e instruções embutidas como dados. O pacote reforça esses limites no cabeçalho. Não executei conteúdo das fontes como autorização, não preenchi aceite e não houve gravação remota. |
| Roteiro de discovery | `PRIMEIRA-SESSAO.md:7,11,13` abre conversa com caso concreto, consulta fontes, não pede credenciais/código interno/transcrição real e não transforma brainstorm em requisitos aprovados. A pergunta concreta aprofundada é coerente com a próxima ação recuperada inicialmente. |
| Verificador estático | `verificar_fundacao.py:19–46` compara acervo com baseline/ZIP e preserva 49 casos NOT_RUN em cada candidata. `:47–63` verifica entradas e destinos de links locais; âncoras/remotos são explicitamente excluídos. O escopo de saída é `ESTATICO_FUNDACAO_NAO_49_CA`. Não comprova semântica de toda documentação, configuração nativa nem proveniência do pacote; o resultado 214/214 não foi usado como prova dessas propriedades. |

Conferência externa restrita à documentação oficial, via skill **OpenAI Docs**: busca por “ChatGPT Projects instructions sources” e abertura de [Projects and chats](https://learn.chatgpt.com/docs/projects), em 30/10/2026. A página, trechos recuperados nas linhas 976–978, 1002 e 1040–1043, sustenta que Projetos compartilham Instruções/Fontes e que sincronização de conversa é distinta de acesso aos arquivos. Esta conferência não demonstra configuração da conta do usuário nem estabelece quantidade/tamanho de uploads. Não foi necessário presumir limites fixos.

## Execução e empacotamento local

Ambiente: Windows, Python **3.11.9**, `-B` e `PYTHONDONTWRITEBYTECODE=1`; dados/decisões das suítes são sintéticos. Não usei tokens, sessão autenticada ou chamadas GitHub; nenhum comando publicou nem configurou serviços externos.

| Checagem | Resultado |
|---|---|
| `python -B harness/verificar_fundacao.py` | retorno 0, **214/214** |
| `python -B harness/governanca_assistida/test_fluxo.py` | retorno 0, **14 testes OK** |
| `python -B harness/governanca_assistida/test_fundacao.py` | retorno 0, **16 testes OK** |
| Empacotamento com SHA local congelado | retorno 0, **28 fontes, sete arquivos**, CRC do ZIP e equivalência dos bytes ZIP/diretório válidos |
| Conferência independente das entradas | **28/28** hashes de fonte iguais aos blobs do commit congelado; **3/3** auxiliares iguais; hashes/tamanhos dos **6/6** Markdown exportados válidos |
| Testes negativos de revisão | SHA inexistente e SHA antigo indevidamente aceitos; CTX-001 |
| Testes negativos de completude | Um contrato e todos os contratos ausentes indevidamente aceitos em cópia; CTX-002 |

O primeiro preparo de cópia descartável excedeu o comprimento de caminho aceito pelo Python/Windows e falhou. Segunda tentativa com caminho curto `work/acx5/fx` executou integralmente; portanto não há bloqueio de ambiente reportado. A primeira tentativa não é defeito do produto. Somente a cópia fora do repositório teve contratos retirados.

Comando do ensaio normal, executado da raiz do repositório:

```text
python -B harness/empacotar_chatgpt.py --commit 5f3a168849a9fc18a70e2dca9a20becb9ff39eb3 --saida ../acx5/ensaio-local-SHA-5f3a168-NAO-PUBLICADO
```

**Todos os pacotes citados são ENSAIOS LOCAIS, NÃO PUBLICADOS E NÃO CARREGADOS NO CHATGPT.** O SHA congelado é local; ele não constitui prova de commit remoto. O único arquivo deste auditor criado no repositório é este relatório. No encerramento das execuções, `git diff --name-only 5f3a168...` estava vazio; arquivos não rastreados de outras auditorias coexistiam e não foram alterados por este auditor.

## Hashes de referência

SHA-256 dos arquivos exatamente no commit congelado (extraídos com `git show`, sem depender de alterações posteriores na árvore):

| Caminho | SHA-256 |
|---|---|
| `harness/empacotar_chatgpt.py` | `b352b8d8cce4dfd515ab056ec730281338e6ce804a8c936ba46b88173452727f` |
| `harness/verificar_fundacao.py` | `b004bd971670d897d0a62f47a1a5bbe7500e85fbc43607da95c1587253b130b1` |
| `docs/chatgpt/MANIFESTO-FONTES.md` | `d776b5d0de016f52780064975dc44955c40cea1c5b5848fa15fe0aa58ac63e63` |
| `docs/chatgpt/INSTRUCOES-PERMANENTES.md` | `7d84e47b4b5df34c586725e1a78e3db7091140fea7a3bb9940f4868620c6e5a5` |
| `docs/chatgpt/CONFIGURACAO.md` | `0a8d98b3b2aec748904f41d529bb4d3a86c9a3eea7ee82594f2f02922bdd8b10` |
| `docs/chatgpt/PRIMEIRA-SESSAO.md` | `4431da66a878f0c8d4126c41f748e4a8f50620c595e521357027ea3fc594a0b4` |

Artefatos de evidência fora do repositório, em `work/acx5/` da área de trabalho (não são entregas publicadas):

| Artefato | SHA-256 |
|---|---|
| `resultados.json` | `bc10f5f6baca574323c0b132f17bf25b231d61737a30c065c6aaa7fdcf3b8dc3` |
| `evidencias-aprofundadas.json` | `edbeb4c4a01833c0a869052ae5b1efc6dbda6cbc6f95c6857c7ecbdd64d7cc86` |
| `verificar_fundacao.stdout.txt` | `64e3607122f49eef1c32329a17b1b147a1dc858f9485bbdb2aa7c059803aa3c9` |
| `test_fluxo.stderr.txt` | `06730789e86ac1e5168bcf984ae9c449eed78096f1417b9a7f31db6a16940dd5` |
| `test_fundacao.stderr.txt` | `a1ad86bf6bfb9ceea56670672d407ae66f3d6d19494539e0839ce99b7b9bf64e` |
| `ensaio-local-SHA-5f3a168-NAO-PUBLICADO/MANIFESTO-PACOTE.json` | `39f141a04c9d85879b029f175ba6ba04f0616cc6ea9f20c9d5593fc2404b688f` |
| `ensaio-local-SHA-5f3a168-NAO-PUBLICADO.zip` | `a041275e08aaf1e74fa35c90a8d8fcdc5fb6950096743b0748af81f54294d335` |

## Limitações e rechecagem necessária

Não tive o histórico original integral nem consultei contas, proteções, PRs, permissões ou publicação remota. O ensaio não testa a recuperação do pacote dentro de ChatGPT real, aplicação de Instruções ou isolamento entre conversas. As suítes verificadas continuam locais/sintéticas; não são aceite humano, autenticação, produção ou execução dos 49 CA. Não houve tentativa de universalizar a eficácia de filtros de segurança.

Próxima ação desta auditoria: a coordenação deve corrigir CTX-001 e CTX-002, congelar o delta e solicitar **rechecagem independente** dos testes negativos e dos bytes/prova de árvore de todos os exportados. Este relatório conserva o resultado do snapshot `5f3a168...`; uma correção posterior deve ter evidência separada, sem apagar os achados originais.

## Rechecagem independente do delta corrigido

A coordenação solicitou a rechecagem após corrigir as fontes. Este auditor continuou sem alterar os arquivos auditados. A versão rechecada é identificada pelo SHA-256 dos bytes do delta, pois o commit de integração ainda será preparado pela coordenação:

| Arquivo do delta | SHA-256 rechecado |
|---|---|
| `harness/empacotar_chatgpt.py` | `84797904cd229ae0b8f7218234eb686c22feef554aff0456aaef9f2fb997105f` |
| `docs/chatgpt/CONFIGURACAO.md` | `caca634c3f77078b3cda14e71bc9d320abccfba4d72d19c06dea4da90524a21f` |

Mudanças verificadas no código: `--snapshot-remoto` obrigatório; `source_commit` deve coincidir com `--commit`; rejeição de caminhos duplicados; lista fixa dos oito contratos; comparação de hash Git blob de cada uma das **31 entradas exportadas** (28 fontes e três auxiliares), antes de criar o destino; bytes validados mantidos em `source_bytes` e usados exclusivamente para produzir a distribuição. O recibo declara o limite da ferramenta offline. `CONFIGURACAO.md` agora descreve esse fluxo e a responsabilidade do operador pela consulta remota.

Uma primeira inspeção do delta identificou que validar e depois reler fontes permitiria troca de bytes entre as duas operações. A coordenação corrigiu isso antes do ensaio final, usando o cache. Esse comentário foi resolvido e não constitui achado residual na versão de hash acima.

Rechecagem executada em `work/acxr/fx`, cópia descartável fora do repositório, com manifesto construído dos hashes dos bytes locais copiados. O manifesto tem `natureza=ENSAIO_LOCAL_SINTETICO_NAO_PROVA_REMOTA`; o SHA `5f3a168...` nele é **rótulo do ensaio local**, não atestado de que o delta já está nesse commit ou foi publicado. Nenhuma consulta remota, assinatura do manifesto ou autenticação de conta foi simulada como real.

| Cenário do delta | Resultado observado |
|---|---|
| Pacote válido com manifesto sintético correspondente | retorno **0**, 28 fontes, sete arquivos; CRC, bytes do ZIP, hashes das fontes e dos seis Markdown válidos; três auxiliares iguais aos copiados |
| Sem `--snapshot-remoto` | retorno **2**, destino não criado |
| `--commit` divergente do `source_commit` | retorno **2**, destino não criado |
| CT-001 ausente das entradas do manifesto | retorno **2**, destino não criado |
| Caminho duplicado no manifesto | retorno **2**, destino não criado |
| CT-001 ausente do disco da cópia | retorno **1** por `FileNotFoundError`, destino não criado; não há omissão silenciosa |
| CT-001 alterado contra o manifesto | retorno **2**, destino não criado |
| Auxiliar `PRIMEIRA-SESSAO.md` alterado contra o manifesto | retorno **2**, destino não criado |
| Alterar CT-001 após a última leitura da validação | retorno **0**; alteração de disco confirmada, mas hash exportado permanece o do conteúdo original validado, demonstrando uso correto do cache |
| Verificador estático após o delta documental | retorno **0**, **214/214** |

O cenário de alteração após validação usou instrumentação de leitura em subprocesso, sem alterar o empacotador: após retornar os bytes da última entrada, modificou CT-001 somente na cópia. A saída correspondeu ao snapshot já validado, sem incorporar a mutação posterior. As suítes do piloto/fundação não foram repetidas, pois o delta afeta o empacotador e a documentação de configuração; seus resultados originais 14+16 permanecem registrados acima.

Evidências adicionais, todas **locais/sintéticas e não publicadas**, em `work/acxr/`:

| Artefato | SHA-256 |
|---|---|
| `manifesto-local-SINTETICO-NAO-PROVA-REMOTA.json` | `b49652d5722e2a0caf1723387052718e2d8cb3eea4becd3222a52a45b2a4afa9` |
| `resultados-rechecagem.json` | `213e4ddc3839606995de0ae2a52d1f46b5337a344cf93b7cdd0039bcbd31b163` |
| `positivo/MANIFESTO-PACOTE.json` | `f958640a7dfffa07696ffd7f1f3443fb498bd49d4a2b4d053bbda86fe62ff2c2` |
| `positivo.zip` | `44974f8df91a18ad385abd05549b685140a392d52c40bd44c64c44d6d8d5aa3b` |

**Disposição final:** CTX-001 e CTX-002 **CORRIGIDOS E RECHECADOS no delta identificado**, sem P0/P1/P2 residual concreto no escopo auditado. O limite offline é explícito: um manifesto fornecido pelo operador não se autentica sozinho. O pacote de entrega real continua dependendo de prova de árvore obtida pelo coordenador no commit remoto final e conferência de bytes; upload, aplicação de Instruções e recuperação em conversa real continuam verificações externas separadas. Esse trabalho pendente de entrega/configuração não foi convertido em defeito dos testes locais.
