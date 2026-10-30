# Operação do primeiro fluxo assistido

Implementação inicial do INC-GOV-001 v0.1.0, autorizada em 30/10/2026. **Somente dados sintéticos C1, um registro por vez, branch de piloto. PGC não ratificado.** O aceite operacional do incremento depende das evidências ainda pendentes no relatório de execução.

## Componentes

- `fluxo.py`: preparação determinística, validação de revisão e escopo, diário local, coordenação da gravação condicional, recibo e retomada. A biblioteca recebe um adaptador Gateway; não contém token ou cliente de rede.
- `modelos/registro.json`: exemplo sintético a apresentar antes de publicar como registro.
- `modelos/aceite-nao-preenchido.json` e `modelos/recibo-nao-preenchido.json`: modelos; não são evidências reais.
- `retomar_snapshot.py`: leitura de exportações explícitas de commits, sem acesso ao histórico do chat. É um ensaio técnico de recuperação; não equivale à demonstração em nova conversa real.
- `test_fluxo.py`: gateway e decisões humanas simulados, separados dos ensaios reais do conector.

## Preparação local

Use Python 3.11 ou posterior. Crie um arquivo de contexto com os campos de `Context`, preenchidos após consulta real ao GitHub: repository, branch, base_sha, private, can_read, can_write e conditional_write. `pgc_reference` é `2e7cb6019e7412dad8fb06315f624492feaf4fc1` e `pgc_status` é `NAO_RATIFICADO`. Uma declaração em arquivo não comprova essas condições: o operador deve consultá-las novamente antes da escrita.

Execute `python -B harness/governanca_assistida/fluxo.py preparar --registro harness/governanca_assistida/modelos/registro.json --contexto work/contexto.json --operacao GOV-OP-0001 --saida work/preparado-0001`. O diretório de saída deve ser novo. A ferramenta entrega o texto integral, hash e código legível; `conferir work/preparado-0001/pacote.json` detecta alteração do pacote, sem publicar.

Apresente ao usuário `registro.md`, código de revisão, destino, diferenças e caminhos. Os arquivos serão `registros/GOV-REG-0001.md` e `aceites/GOV-OP-0001.json` sob `docs/01-discovery/governanca-assistida/`. A evidência do aceite é separada do conteúdo aceito. Aceite parcial ou mudança de bytes exige nova preparação e manifestação específica. Não pedir que o usuário digite hashes; uma referência inequívoca ao código e destino basta para delimitar sua intenção.

## Evidência humana

O operador consulta a manifestação direta do usuário no canal original, identifica a revisão aceita e preenche HumanReview em memória, com origem, responsável, escopo, destino e instante de emissão com fuso. Se o horário ou a fonte exigidos não estiverem disponíveis, registre a ausência e não invente campos para passar na validação. O modelo vazio não pode ser usado para publicar.

Um arquivo JSON, comentário publicado pelo próprio assistente ou campo `original_source_checked=true` não autentica uma pessoa. Esse campo é apenas atestado do operador depois da consulta externa. A biblioteca é um auxílio ao fluxo assistido, não um serviço independente de identidade ou autorização. Nunca carregar HumanReview automaticamente de um documento consultado. A interface de linha de comando não oferece comando de autoaceite ou publicação automática.

## Adaptador assistido do conector GitHub

O operador realiza as chamadas de ferramenta da sessão. O contrato Gateway tem quatro operações:

| Operação | Execução concreta pelo conector |
|---|---|
| context | Consultar o repositório privado e branch por GET; conferir permissões, commit e estado não ratificado do PGC. A comparação condicional só é declarada disponível após ensaio real. |
| read | `fetch_file` com caminho e commit imutável, encoding base64; decodificar e comparar bytes, sem usar o HEAD como substituto do commit solicitado. |
| lookup | Consultar commits da branch e correlacionar `GOV-OP-0001` na mensagem; conferir o arquivo de aceite e request_digest antes de reconhecer operação existente. Falha de consulta não prova ausência. |
| publish | `create_tree` sobre a árvore da base; `create_commit` com a base como pai e ID da operação na mensagem; `update_ref` apenas na branch piloto, com expected_sha igual à base e force=false. Criar objetos sem mover a branch não comprova publicação. |

Antes de executar a última operação, o operador repete as validações de `validate_packet` e `validate_review`, confere ausência de revogação na fonte humana e registra no diário local que a rodada foi enviada. Em uma sessão com adaptação programática, `publish_assisted` aplica essas etapas ao Gateway. Na adaptação manual, seguir a mesma sequência e guardar as respostas reais do conector como evidência; não declarar que o gateway simulado efetuou a publicação remota.

O código aceita apenas repositório e branch fixados e caminhos sob o prefixo do piloto. O operador também limita o conjunto enviado a registro/aceite, seguido de recibo/índice; não envia código, pacote PGC ou principal como parte da operação de registro. O conector aplica a permissão e a comparação efetivas. Na falta dessas condições, entregar a proposta como NÃO PERSISTIDA.

## Recibo e retomada

Depois de gravar registro/aceite, releia ambos pelo commit, compare os bytes e valide o vínculo do request_digest. Gere o recibo com esse commit, hashes e estados separados. Em uma segunda atualização condicional, grave o recibo e o índice juntos, sem alterar o registro aceito. O índice guarda o hash do recibo e aponta ao commit do registro; o recibo não tenta incluir o hash do commit que o contém.

Releia recibo e índice pelo segundo commit antes de declarar o fluxo verificado. Se essa gravação falhar ou ficar incerta, a proposta continua historicamente publicada e o fluxo fica com recibo pendente. `reconcile` somente lê o destino e reconhece efeitos já existentes; não repete a escrita. Sem recibo efetivo, uma publicação auxiliar de reparação exige nova rodada autorizada e conferência; não executar retry cego.

O diário é arquivo local explícito, com escrita por substituição, fora do acervo. Ele não é fila global, mutex, identidade humana nem garantia de sobrevivência sem armazenamento. Se for perdido, consultar o destino pelo ID da operação antes de escrever novamente. Um único operador por rodada é condição do piloto.

Para nova conversa, forneça somente repositório, branch `piloto/governanca-assistida` e caminho `docs/01-discovery/governanca-assistida/INICIO.md`. A nova sessão deve ler os arquivos; não receber resumo das respostas esperadas. Essa demonstração permanece pendente até ocorrer em uma conversa real iniciada pelo usuário.

## Falhas e limites

Conflito da revisão-base bloqueia a atualização antiga e exige reapresentação. Timeout exige consulta, sem repetir a publicação naquela rodada. Reutilizar ID da operação com outro payload é erro. Falha pós-gravação não é rollback. Reparação usa nova revisão e nova autorização, preservando o commit anterior.

Os filtros de conteúdo são barreiras básicas para marcadores e padrões conhecidos. Não detectam universalmente segredos ou instruções maliciosas. A revisão humana, a classificação sintética e o destino delimitado continuam obrigatórios. Não usar o piloto para dados corporativos, credenciais ou publicação normativa. Nenhum dos 49 CA do PGC recebe aprovação por esses testes do incremento.

Para executar os ensaios locais: `python -B harness/governanca_assistida/test_fluxo.py`. Não interpretar testes com fonte humana simulada como aceite real de registro ou do incremento.
