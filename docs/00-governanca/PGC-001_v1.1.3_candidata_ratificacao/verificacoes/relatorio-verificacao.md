# Relatório de verificação estática — PGC-001 v1.1.3

**Escopo:** estrutura e conteúdo formal de nove documentos, índices, emendas e catálogo. **Não** testa sistemas de IA, escrita, autorização, CAS ou ativação real.

**Estado do pacote:** PROPOSTO — NÃO RATIFICADO — NÃO IMPLEMENTADO.

**Casos CA-01..CA-49:** `NOT_RUN`.

**Resultado dos checks estáticos:** 76/76 PASS.

| Check | Resultado | Observação |
|---|---|---|
| Nove documentos normativos/contratuais | PASS |  |
| Contratos CT-001..008 sem lacuna | PASS |  |
| PGC v1.1.3 proposto | PASS |  |
| CT-001 v1.0.3 proposto | PASS |  |
| CT-002 v1.0.3 proposto | PASS |  |
| CT-003 v1.0.3 proposto | PASS |  |
| CT-004 v1.0.3 proposto | PASS |  |
| CT-005 v1.0.3 proposto | PASS |  |
| CT-006 v1.0.3 proposto | PASS |  |
| CT-007 v1.0.3 proposto | PASS |  |
| CT-008 v1.0.3 proposto | PASS |  |
| 25 normas distintas no PGC | PASS |  |
| 25 normas na matriz | PASS |  |
| 20 achados AC na matriz | PASS |  |
| Emendas EM-001..009 no registro | PASS |  |
| Emendas EM-001..009 na matriz | PASS |  |
| Emendas EM-001..009 no README | PASS |  |
| 49 cenários únicos no JSON | PASS |  |
| 49 cenários CA no CT-008 | PASS |  |
| Casos testados NÃO executados | PASS |  |
| Fixtures completas | PASS |  |
| Metadados dos cenários | PASS |  |
| Normas referenciadas por casos existentes | PASS |  |
| Contratos referenciados por casos existentes | PASS |  |
| Oráculos apenas em categorias conhecidas | PASS |  |
| CA-04 é semântico e não presume aprovação normativa | PASS |  |
| CA-04 fixture não tem identidade/digest | PASS |  |
| CA-49 inclui identidade, política, revisão, digest e escopo | PASS |  |
| Bootstrap EM-001 com ratificação inicial | PASS |  |
| Separação intenção/norma EM-002 | PASS |  |
| Ordem canônica no CT-003 | PASS |  |
| Pré-testes antecedem aprovação e publicação | PASS |  |
| Vigência só por manifesto ativado | PASS |  |
| Publicado não implica vigente | PASS |  |
| Falha pós-publicação mantém norma anterior | PASS |  |
| Captura assistida como padrão | PASS |  |
| Captura automática não presumida | PASS |  |
| Ratificação é modelo não executado | PASS |  |
| Matriz sem normas repetidas | PASS |  |
| Matriz e catálogo: vínculos bidirecionais idênticos | PASS | matriz_sem_catalogo=[]; catalogo_sem_matriz=[] |
| Requisitos por caso sem duplicação | PASS |  |
| Todos os 25 IDs têm casos associados | PASS |  |
| Catálogo em UTF-8 sem BOM e LF | PASS |  |
| CT-001 Approval usa issued_at | PASS |  |
| CT-002 Approval usa issued_at | PASS |  |
| Data de emissão distinta de rascunho | PASS |  |
| CA-49 tem data de emissão sintética com fuso | PASS |  |
| Link relativo README.md: PGC-001.md | PASS |  |
| Link relativo README.md: contratos/CT-001-classificacao-aprovacao.md | PASS |  |
| Link relativo README.md: contratos/CT-002-modelo-proveniencia.md | PASS |  |
| Link relativo README.md: contratos/CT-003-publicacao-concorrencia.md | PASS |  |
| Link relativo README.md: contratos/CT-004-rastreabilidade-impactos.md | PASS |  |
| Link relativo README.md: contratos/CT-005-seguranca-autorizacao.md | PASS |  |
| Link relativo README.md: contratos/CT-006-continuidade-recuperacao.md | PASS |  |
| Link relativo README.md: contratos/CT-007-organizacao-contexto.md | PASS |  |
| Link relativo README.md: contratos/CT-008-verificacao-adversarial.md | PASS |  |
| Link relativo README.md: MATRIZ-DE-RASTREABILIDADE.md | PASS |  |
| Link relativo README.md: REGISTRO-DE-EMENDAS.md | PASS |  |
| Link relativo README.md: RATIFICACAO-INICIAL-MODELO.md | PASS |  |
| Link relativo README.md: verificacoes/casos-adversariais.json | PASS |  |
| Link relativo README.md: verificacoes/gerar_catalogo.py | PASS |  |
| Link relativo README.md: verificacoes/auditar_pacote.py | PASS |  |
| Link relativo README.md: verificacoes/relatorio-verificacao.md | PASS |  |
| Link relativo README.md: REVISAO-TECNICA.md | PASS |  |
| Link relativo README.md: verificacoes/testar_revisao.py | PASS |  |
| Arquivo PGC-001.md não truncado | PASS |  |
| Arquivo CT-001-classificacao-aprovacao.md não truncado | PASS |  |
| Arquivo CT-002-modelo-proveniencia.md não truncado | PASS |  |
| Arquivo CT-003-publicacao-concorrencia.md não truncado | PASS |  |
| Arquivo CT-004-rastreabilidade-impactos.md não truncado | PASS |  |
| Arquivo CT-005-seguranca-autorizacao.md não truncado | PASS |  |
| Arquivo CT-006-continuidade-recuperacao.md não truncado | PASS |  |
| Arquivo CT-007-organizacao-contexto.md não truncado | PASS |  |
| Arquivo CT-008-verificacao-adversarial.md não truncado | PASS |  |
| README deixa clara ausência de implementação | PASS |  |
| Catálogo é test spec e não test execution | PASS |  |

## Limites metodológicos

- Verificações de tokens/estrutura e correspondência de referências não são prova de consistência semântica completa.
- Testes CA-01..49 não foram executados; não há runner nem integrações reais.
- Aprovação de usuário, ratificação inicial e ativação normativa são pendentes.
- Escolhas tecnológicas de IAM, CAS, manifesto, filas e persistência permanecem em aberto.

## Inventário SHA-256 do conteúdo (excluindo este relatório e SHA256SUMS.txt)

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| `MATRIZ-DE-RASTREABILIDADE.md` | 8753 | `a62626c4c942d73dbc74ceebe424a0a581669e334dbd153ac815994449534218` |
| `PGC-001.md` | 16818 | `99a6586b230f426a6b2f8a23179f5fd6047c472c5713abb239e3a0680fad961b` |
| `RATIFICACAO-INICIAL-MODELO.md` | 1756 | `2e64fa721d7e940026e4f90424519ba8cfcd93981f64ce15af0791b10543ed64` |
| `README.md` | 6958 | `daf62ebdb18f7982e3f1ab4044e040fc0e859661a416f4e1fb92e174742eda54` |
| `REGISTRO-DE-EMENDAS.md` | 5416 | `eac3add951e677e6142a87f7bf98d4bf62f5a43db3969a3d8b9e9bc498ccb2ab` |
| `REVISAO-TECNICA.md` | 4064 | `390b1f06a458a5f40a99c843e99ef51b98bb7013b86222d3b7c197b385d47d09` |
| `contratos/CT-001-classificacao-aprovacao.md` | 12481 | `4f9e94dab864868de60b57ec4d4859d66640b3eb4721455ecde0a19357cb2428` |
| `contratos/CT-002-modelo-proveniencia.md` | 12216 | `1002e1988e8a264e00eed5f097ad7d5bb4bac94bc84c67df7a31450af88cb9a4` |
| `contratos/CT-003-publicacao-concorrencia.md` | 13544 | `95f42a4e4be4b5a2f44bb313019abf5fccc7890183dad4e56f464e337b542458` |
| `contratos/CT-004-rastreabilidade-impactos.md` | 7238 | `c048b0679bdb5cd24da7ee58ecc986d4986c8843d045920966996b563f18ce0e` |
| `contratos/CT-005-seguranca-autorizacao.md` | 10294 | `d41f85e689d871a2fd9ed0f02e0c53c38e422367a917afe8277e4a8c4ff057a7` |
| `contratos/CT-006-continuidade-recuperacao.md` | 7850 | `ff560118fd1939732187626e1c2e3ad370d45901920a24cf5ac242f7853f8738` |
| `contratos/CT-007-organizacao-contexto.md` | 7081 | `c0dd230f58453d43011a2c8fd15e4a788ae507493274239cf586b273af15c7dd` |
| `contratos/CT-008-verificacao-adversarial.md` | 15367 | `230869fcc1e1f8d7f515b7b0424a489c84179710e75595c8df76fbaafca2d0f0` |
| `verificacoes/auditar_pacote.py` | 11322 | `d79e0dbe731787b6a7c52c84fece82c8d3d52db44eada394011fa54a5a3ccc95` |
| `verificacoes/casos-adversariais.json` | 101145 | `1abd8fb0ca3553e10ebc0d2011b7dc859a60458c9ab803d294bec244101323e0` |
| `verificacoes/gerar_catalogo.py` | 17532 | `6f3db4d134b10f8408b9157e51981cb919050c071f666848584e8ad759d49f50` |
| `verificacoes/testar_revisao.py` | 5493 | `3baebb69590ebe72e13fb58f71feb80a13344cab43c13c97a6461bb73cc85db0` |

**Nenhuma falha detectada pelos checks estáticos executados.** Isso não demonstra aprovação normativa ou operacional.
