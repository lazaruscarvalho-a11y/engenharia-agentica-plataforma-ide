# Extensão de fundação assistida — v0.1.0

Estado: implementação de ensaio local, sintética, sem efeito normativo. PGC-001 v1.1.3 continua não ratificado. Os 49 CA do PGC não são executados nem aprovados por esta extensão.

`fundacao.py` importa as funções e contratos do piloto `fluxo.py`; o piloto e seus testes originais permanecem intactos. A extensão acrescenta captura exploratória C0 e um Gateway SQLite persistente para ensaiar o fluxo C1 já existente. O banco SQLite é uma fixture local: flags `private/can_write/conditional_write` expressam o ambiente de teste e não permissões reais do GitHub. IDs de snapshots com 40 caracteres são identificadores locais, nunca commits Git remotos.

## Contratos implementados

| Objeto | Contrato efetivo |
|---|---|
| C0 | `Draft`: ID estável FUND-IDEA/HYP/PEND/DEC-nnnn, revisão sequencial, tipo, título, corpo, fonte sintética e classificação. Maturidade sempre PROPOSTO; DEC significa DECISAO_PROPOSTA. |
| Proveniência | `synthetic://`, tipo de fonte, dados tratados como UNTRUSTED_DATA; sem execução do corpo ou extração de instruções. |
| Revisões | Captura exige revisão anterior exata dentro de `BEGIN IMMEDIATE`; histórico anterior não é alterado. |
| Idempotência | ID de operação + digest de payload e revisão esperada; repetição idêntica retorna recibo anterior, mudança é bloqueada. |
| Persistência | Captura C0 e recibo no mesmo commit SQLite; releitura por nova conexão compara hash. Recuperação compara recibo e bytes persistidos. |
| C1 | Preparação e publicação assistida usam `prepare`, `HumanReview`, `publish_assisted`, `recover` originais. Um aceite genérico ou arquivo de fonte não autentica a pessoa. |
| Changeset C1 | Exatamente registro + evidência do aceite, depois recibo + índice, sob os caminhos do piloto. HEAD esperado é comparado dentro da transação local. |
| Falhas | Timeout antes/depois exercitável; reconciliação consulta o destino. Não existe retry automático nem publicação normativa. |

O Gateway é uma camada de armazenamento de baixo nível, não uma autoridade de aprovação. Não chamar `publish` diretamente como substituto de `publish_assisted`. Fixtures dos testes chamam essa camada diretamente apenas para verificar CAS, escopo de caminhos e idempotência. Qualquer adaptação remota deve verificar autorização real e seguir o contrato descrito em [OPERACAO.md](OPERACAO.md), sem copiar as flags da fixture.

## Uso executável

Python 3.11+, biblioteca padrão. Executar da raiz do repositório. Criar banco e entradas em `work/`, fora do acervo. O diretório deve existir; nenhum comando envia dados à rede.

Exemplo de entrada C0 sintética (`work/ideia.json`):

```json
{
  "record_id": "FUND-IDEA-0001",
  "revision": 1,
  "kind": "IDEIA",
  "title": "Painel sintético de agentes",
  "body": "Explorar a visibilidade de tarefas antes de especificar a interface.",
  "source_ref": "synthetic://discovery/exemplo"
}
```

```text
python -B harness/governanca_assistida/fundacao.py --database work/fundacao.sqlite capturar-c0 --entrada work/ideia.json --operacao FUND-OP-0001 --revisao-esperada 0
python -B harness/governanca_assistida/fundacao.py --database work/fundacao.sqlite retomar-c0 --id FUND-IDEA-0001
python -B harness/governanca_assistida/fundacao.py --database work/fundacao.sqlite preparar-c1 --registro harness/governanca_assistida/modelos/registro.json --operacao GOV-OP-0001 --saida work/pacote-c1.json
```

O último comando prepara um pacote para a fixture local e não o publica. Arquivo de saída deve ser novo. A CLI não possui comando de autoaceite ou publicação C1; o operador consulta a manifestação humana original antes de construir `HumanReview`. Decisões nos testes são explicitamente simuladas, nunca evidência de aceite humano real. Autorização para registrar exploração C0 não aprova requisitos de produto e não amplia o contrato do piloto C1.

## Verificação e recuperação

```text
python -B harness/governanca_assistida/test_fluxo.py
python -B harness/governanca_assistida/test_fundacao.py
```

`test_fundacao.py` exercita persistência, releitura, recibo, payload alterado, revisão antiga, histórico, duas conexões concorrentes, lock timeout SQLite, aprovação parcial/ambígua/antiga, timeout antes/depois, fontes injetadas, marcadores sensíveis sintéticos, caminhos fora do escopo, perda de contexto e subprocesso novo. O processo novo recebe somente caminho do banco e ID, recuperando bytes/fonte/hash sem histórico do chat. Isso comprova recuperação técnica entre processos, não uma nova sessão nativa do ChatGPT nem configuração das Fontes.

## Limitações e segurança

Somente dados sintéticos: a extensão não ingere transcrições ou código interno. Os filtros reconhecem padrões de fixture conhecidos e não detectam universalmente segredos ou ataques. Os hashes detectam divergências acidentais entre registros e recibos; um administrador que modifica ambos no SQLite não é contido por assinatura criptográfica. O arquivo deve ficar em armazenamento local autorizado, com permissões do sistema operacional. Não há autenticação corporativa, RBAC, criptografia adicional, serviço de monitoramento, conector de banco ou sincronização de conversas.

Não há publicação C2/C3, ratificação, manifesto efetivo, merge, alteração em permissões ou implantação produtiva. A implementação final da IDE depende de discovery e aprovação de requisitos. C1 remoto permanece assistido e sua comprovação depende de chamadas reais ao conector; testes locais não substituem essas evidências.
