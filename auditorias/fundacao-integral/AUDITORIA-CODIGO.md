# Auditoria independente de código e segurança — fundação assistida

Data: 30/10/2026. Snapshot auditado: `5f3a168849a9fc18a70e2dca9a20becb9ff39eb3`. Ambiente: Windows, Python 3.11.9, biblioteca padrão, SQLite local e entradas exclusivamente sintéticas. Este relatório registra o snapshot congelado; correções posteriores exigem delta e reexecução próprios.

**Resultado: nenhum P0/P1 encontrado neste escopo; três P2 reproduzidos.** As suítes existentes passam, mas os ensaios adicionais revelam duas lacunas de integridade/recuperação C0 e um campo de origem C1 fora do filtro conhecido. Não houve alteração de implementação nesta auditoria. Não se declara homologação, autenticação humana, integração remota, aceite operacional ou aprovação dos 49 CA do PGC.

**Atualização após correção pela coordenação:** os três P2 foram corrigidos na extensão e revalidados independentemente: **46/46 testes locais PASS** (14 piloto + 16 extensão + 16 adversariais). A evidência original abaixo é preservada; a seção final identifica o delta auditado e seus limites.

## Escopo e evidência executada

Foram lidos `AGENTS.md`, `ESTADO-ATUAL.md`, visão/roteamento, `fluxo.py`, `fundacao.py`, ambos os arquivos `test_*` do harness e `OPERACAO.md`/`OPERACAO-FUNDACAO.md`. Foram comparadas as alegações de operação à implementação e exercitados armazenamento real, transações SQLite, duas conexões concorrentes, subprocesso Python novo e fluxos de falha. Código de teste novo: [test_adversarial.py](test_adversarial.py). Asserções expressam a proteção esperada; falhas não são mascaradas com `expectedFailure`.

Comandos executados na raiz do repositório:

| Comando | Resultado observado |
|---|---|
| `git rev-parse HEAD` | `5f3a168849a9fc18a70e2dca9a20becb9ff39eb3` |
| `python --version` | `Python 3.11.9` |
| `python -B harness/governanca_assistida/test_fluxo.py` | `Ran 14 tests in 0.130s` / `OK` |
| `python -B harness/governanca_assistida/test_fundacao.py` | `Ran 16 tests in 1.888s` / `OK` |
| `python -B auditorias/fundacao-integral/test_adversarial.py` | 16 casos: 13 PASS, 3 FAIL; processo retorna 1 |
| `git diff --exit-code -- harness/governanca_assistida/fluxo.py harness/governanca_assistida/fundacao.py harness/governanca_assistida/test_fluxo.py harness/governanca_assistida/test_fundacao.py` | Sem diff operacional no momento da auditoria |

As três falhas foram reproduzidas em rodadas independentes antes do fechamento. Saída da última rodada, após delimitar A07 à nova borda SQLite sem exigir alteração do piloto histórico: `Ran 16 tests in 2.096s` / `FAILED (failures=3)`. Rodadas anteriores reproduziram as mesmas duas falhas C0 e a lacuna C1, incluindo verificação direta de `prepare`. Não houve troca de oráculo para declarar sucesso.

## Achados reproduzidos

### COD-01 — P2: repetição C0 retorna recibo sem verificar a existência dos bytes

Local: `fundacao.py:173–177`; teste `A04`.

Reprodução: capturar `FUND-IDEA-0001` com `FUND-OP-0001`, apagar somente a linha em `drafts`, manter `draft_operations` e repetir exatamente a captura. O retorno antecipado devolve o recibo antigo com `publication=LOCAL_SINTETICA`; a releitura de `188–190` não ocorre. `recover_draft` dessa mesma ideia então falharia por ausência. Saída adversarial: `AssertionError: (<class 'fluxo.Blocked'>, <class 'FileNotFoundError'>) not raised`.

Impacto: o chamador não pode interpretar toda resposta bem-sucedida de `capture` como confirmação atual de persistência. A repetição significa apenas reconhecimento histórico enquanto a integridade do armazenamento não é revalidada. A reprodução exige perda/adulteração de armazenamento após uma gravação válida; não decorre de disputa CAS normal nem demonstra escalada de permissão. A limitação administrativa documentada continua válida.

Correção recomendada: no ramo idempotente, conferir novamente a linha exata de ID/revisão, seu hash e o recibo antes de retorná-lo; falhar explicitamente se o efeito anterior estiver ausente ou divergente. Não refazer a escrita automaticamente.

### COD-02 — P2: recuperação C0 não vincula o conteúdo à chave solicitada

Local: `fundacao.py:193–211`; teste `A05`.

Reprodução: capturar duas ideias diferentes e válidas, ID1 e ID2; substituir somente `drafts.data` da linha ID1 pelos bytes já existentes da linha ID2. Não alterar nenhum recibo. `recover_draft(ID1)` desserializa ID2, procura o recibo de ID2 e o aceita porque o hash coincide. A resposta contém ID2 quando o pedido foi ID1. Saída: `AssertionError: Blocked not raised`.

Impacto: a validação detecta alteração de bytes sem recibo, mas não detecta esse transplante de conteúdo já íntegro entre chaves. A alegação de recuperação por ID/revisão precisa dessa amarração adicional. O cenário exercita inconsistência do banco; não presume autenticação nem acesso privilegiado contido por assinaturas. A reprodução não altera recibo e payload em conjunto, ameaça explicitamente excluída da fixture.

Correção recomendada: conferir `value.record_id == record_id` e a revisão do payload contra a revisão efetivamente selecionada da linha; validar também a revisão explícita quando fornecida. Recuperação sem revisão deve selecionar e conferir a chave da última linha, em vez de confiar só no conteúdo desserializado.

### COD-03 — P2: marcador sensível conhecido em `Record.source_ref` chega ao SQLite C1

Local de origem: `fluxo.py:73–74` filtra título, conteúdo e detalhes; `fluxo.py:78` também persiste a origem. A extensão `fundacao.py:119–160` valida formato do changeset, sem filtro de conteúdo. Testes `A06` e `A07`.

Reprodução: usar a origem `synthetic://CHAVE_FICTICIA_SINTETICA_TESTE` em um `Record` C1, mantendo título e corpo sintéticos comuns, e executar `publish_assisted` com decisão **simulada**. A preparação original aceita o pacote e a extensão o persiste. A07 esperava ausência da operação e recebeu o snapshot local `094727b1d4b6ead0b3e9392f73945c52d525fc61`. O mesmo marcador na origem C0 é bloqueado (A06).

Impacto: um padrão que a fixture afirma reconhecer atravessa a barreira por estar em outro campo persistido. Trata-se de marcador fictício; nenhum segredo real foi criado, usado ou exposto. Não se afirma que os filtros possam reconhecer todo segredo ou instrução maliciosa. A revisão humana assistida continua necessária.

Correção recomendada: preservar `fluxo.py` histórico. Acrescentar validação dos campos textuais e bytes pertinentes à nova borda SQLite e/ou preparação própria da extensão, documentando o limite do piloto original. Se o bloqueio ocorrer em `publish`, o alto nível pode devolver `NAO_PUBLICADO_SEM_NOVA_TENTATIVA`; o oráculo A07 exige ausência do efeito no destino, sem presumir exceção no alto nível.

## Proteções efetivamente observadas

| Área | Evidência e limite |
|---|---|
| CAS e concorrência C0 | Teste original FUND-004 usa duas conexões; A01 disputa o mesmo operation ID com payloads/IDs diferentes e confirma um registro e um recibo. A02 confirma rollback do ID após conflito e uso posterior válido. |
| CAS e idempotência C1 | FUND-013/015 e A16 bloqueiam base antiga/payload divergente; paths exatos/quantidade do changeset são exigidos. Não é CAS GitHub. |
| Revisões/histórico | Sucessão C0 e C1 e leitura da revisão anterior passam nas suítes originais. A10 recusa aprovação vinculada aos bytes anteriores. Não há descoberta de validade humana por idade do timestamp. |
| Aprovação parcial/ambígua/indireta/antiga/revogada | Originais e A09/A10 recusam scope incompleto, decisão ambígua, outra revisão/destino, fonte documental e flag de revogação. Isso valida campos fornecidos pelo operador; não consulta canal humano nem revogação atual. |
| Timeouts | A03 confirma que lock C0 falha sem linhas parciais; a exceção é `sqlite3.OperationalError`, ao contrário da tradução `Unknown` de publish C1. A13 reconcilia timeout pós-commit sem chamar publish; A14 não repete timeout anterior mesmo com HEAD alterado. |
| Fontes e injeção | Marcadores conhecidos em corpo e C0 origem são recusados. A08 deixa passar frase alternativa como dado e confirma branch delimitada/efeito normativo AUSENTE. Ausência de detector universal é limite documentado, não sucesso de DLP geral. |
| Recuperação fora do processo | FUND-007 confirma C0. A12 apaga o diário e inicia processo Python novo para recuperar C1 recebendo somente localização do harness e banco; bytes/commit/hash coincidem, origem humana fica NÃO REVALIDADA. Não é nova conversa real de usuário. |
| Escopo de escrita | A15 impede terceiro arquivo, arquivo de ativação e changeset auxiliar disfarçado sob o prefixo permitido. A biblioteca não oferece comandos de merge/ratificação/C2/C3. A API de baixo nível aceita bytes para fixture e não substitui o fluxo assistido. |

## Fronteira de aprovação e limites da conclusão

A11 constrói integralmente um `HumanReview` fictício em memória e obtém `VERIFICADO` na fixture. Isso confirma o contrato declarado: **a API local não autentica humanos**. `source_kind=USER_DIRECT`, `actor_ref`, timestamp e `original_source_checked=True` são atestados do operador; JSON, documento ou objeto Python não comprovam identidade nem manifestação no canal original. O estado retornado pela fixture nunca deve ser exibido como aceite humano real sem a verificação externa autorizada. Recuperação marca `NAO_REVALIDADA_NESTA_SESSAO` e exige nova consulta antes de escrita.

O Gateway SQLite tem permissões fixas de teste e snapshots locais; não comprova permissões, CAS, persistência ou autorização remotos. Não foram usados tokens, rede, material corporativo, transcrições reais ou credenciais. Nenhuma escrita desta auditoria alterou implementação, acervos, PGC, normas, branches remotas, merge ou configuração administrativa. Os únicos arquivos criados pelo auditor são este relatório e a suíte adversarial.

Os cenários de corrupção usam cópias temporárias sintéticas. Não demonstram proteção contra administrador que edite banco, recibos e hashes; essa proteção é explicitamente inexistente. Testes de falha são determinísticos e não cobrem queda de energia, corrupção física, volume, todos os agendamentos possíveis de concorrência ou ambientes corporativos. Não houve benchmark ou prova formal.

**Contagem correta:** 30 testes originais PASS e 13 de 16 testes independentes PASS no snapshot auditado, com três falhas mantidas visíveis. Nenhum dos 49 CA operacionais do PGC foi executado ou aprovado por estes ensaios; continuam NOT_RUN. PGC permanece NÃO RATIFICADO. Correção e reexecução posteriores podem encerrar os achados sem apagar esta evidência do snapshot original.

## Identidade dos arquivos operacionais lidos

SHA-256 no congelamento, antes de qualquer correção:

| Arquivo | SHA-256 |
|---|---|
| `harness/governanca_assistida/fluxo.py` | `2f37ef7e114ceffd5820eee0dc3ea9162209de5607abfe349358b5ad92943a20` |
| `harness/governanca_assistida/fundacao.py` | `fdb16b88c1ba74cfeb5660b0bb0348e1ca48ac5cc0feea6ae3ba50cdc68e4e87` |
| `harness/governanca_assistida/test_fluxo.py` | `c82756154d13dd45be49c2a8966fa05e75e769772a31b545a44e50fed3406d02` |
| `harness/governanca_assistida/test_fundacao.py` | `3c515694e4de6eba552eaa052729bc5a18ad87bdcb7a02c75c02cca97a094b51` |

## Revalidação independente do delta corrigido

A coordenação, não o auditor, alterou `fundacao.py` após receber os achados. O auditor releu o diff e executou novamente as três suítes. Esta revalidação refere-se ao arquivo corrigido na árvore de trabalho, SHA-256 `a4d30fab1a3b07928d9150da166444ac54ee303f3ca0212aeb29f904c77665d9`; não se atribui esse conteúdo ao commit congelado original.

| Achado | Delta inspecionado | Resultado independente |
|---|---|---|
| COD-01 | Ramo idempotente chama `recover_draft` e compara o hash aos bytes esperados antes de devolver recibo | A04 PASS: ausência do registro provoca falha, sem nova escrita |
| COD-02 | Consulta seleciona ID/revisão/data; compara chave selecionada, ID solicitado e identidade/revisão do payload | A05 PASS: transplante de bytes entre IDs provoca bloqueio |
| COD-03 | Nova borda `SQLiteGateway.publish` filtra os blobs UTF-8 persistidos, incluindo `source_ref` e metadados serializados | A07 PASS: o marcador conhecido não gera operação no destino local |

Saídas reais desta revalidação:

| Comando | Saída | Código |
|---|---|---|
| `python -B harness/governanca_assistida/test_fluxo.py` | `Ran 14 tests in 0.171s` / `OK` | 0 |
| `python -B harness/governanca_assistida/test_fundacao.py` | `Ran 16 tests in 2.753s` / `OK` | 0 |
| `python -B auditorias/fundacao-integral/test_adversarial.py` | `Ran 16 tests in 2.868s` / `OK` | 0 |

Os três antigos casos de falha passaram sem marcar falhas como esperadas nem remover seus oráculos. O diff de implementação relevante está restrito à extensão `fundacao.py`. `fluxo.py` histórico mantém SHA-256 `2f37ef7e114ceffd5820eee0dc3ea9162209de5607abfe349358b5ad92943a20` e nenhum diff. Os achados COD-01/COD-02/COD-03 ficam **encerrados para esse delta e esses cenários**.

Persistem os limites anteriores: o piloto original não ganha filtro universal de conteúdo nem autenticação humana; a correção C1 atua na nova borda de persistência SQLite, não transforma `prepare` histórico em DLP. Nenhum teste local passa a representar GitHub real, nova conversa nativa, aceite humano ou qualquer um dos 49 CA operacionais, que continuam NOT_RUN. Não houve merge, ratificação ou ativação C2/C3 por esta revalidação.
