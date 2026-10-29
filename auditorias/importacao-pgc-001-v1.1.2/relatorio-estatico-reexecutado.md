# Relatório de verificação estática — PGC-001 v1.1.2

**Escopo:** estrutura e conteúdo formal de nove documentos, índices, emendas e catálogo. **Não** testa sistemas de IA, escrita, autorização, CAS ou ativação real.

**Estado do pacote:** PROPOSTO — NÃO RATIFICADO — NÃO IMPLEMENTADO.

**Casos CA-01..CA-49:** `NOT_RUN`.

**Resultado dos checks estáticos:** 65/65 PASS.

| Check | Resultado | Observação |
|---|---|---|
| Nove documentos normativos/contratuais | PASS |  |
| Contratos CT-001..008 sem lacuna | PASS |  |
| PGC v1.1.2 proposto | PASS |  |
| CT-001 v1.0.2 proposto | PASS |  |
| CT-002 v1.0.2 proposto | PASS |  |
| CT-003 v1.0.2 proposto | PASS |  |
| CT-004 v1.0.2 proposto | PASS |  |
| CT-005 v1.0.2 proposto | PASS |  |
| CT-006 v1.0.2 proposto | PASS |  |
| CT-007 v1.0.2 proposto | PASS |  |
| CT-008 v1.0.2 proposto | PASS |  |
| 25 normas distintas no PGC | PASS |  |
| 25 normas na matriz | PASS |  |
| 20 achados AC na matriz | PASS |  |
| Emendas EM-001..006 no registro | PASS |  |
| Emendas EM-001..006 na matriz | PASS |  |
| Emendas EM-001..006 no README | PASS |  |
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
| `contratos\CT-001-classificacao-aprovacao.md` | 12076 | `f686be94623a8722e5907d8925d553369dbbd7bf9e8b5e96c99b9c71b6562357` |
| `contratos\CT-002-modelo-proveniencia.md` | 11827 | `fae426f2946fdcc22993289e7743d9523306d841fd92dc2f1f5aa2b0297bdf00` |
| `contratos\CT-003-publicacao-concorrencia.md` | 13544 | `adcc71348a9a3516f0ee07324de684cf28508cdaf3b55ccecd8543b2fee726b5` |
| `contratos\CT-004-rastreabilidade-impactos.md` | 7238 | `13a27b93470cfc0ca0b7ddf54f90596dde10d2c3967c2dd5679d603456844745` |
| `contratos\CT-005-seguranca-autorizacao.md` | 10294 | `a121f946fc9348449e1e6842c223d62257b390dcceb56e6bcbe5ffc6446287cc` |
| `contratos\CT-006-continuidade-recuperacao.md` | 7850 | `0e1521e44b8c7e55dd4d781644a4dfe060538cdfb1215e76df03d029880c3574` |
| `contratos\CT-007-organizacao-contexto.md` | 7081 | `c2c42d33255ffa1ca1e8b591afb63c867592d47b810834bfba1b7ba5e55c34ad` |
| `contratos\CT-008-verificacao-adversarial.md` | 14370 | `6579e12d2e22b581d6cd6df47b157248baa4d9059982f00853e5a8c1eaa13ea8` |
| `MATRIZ-DE-RASTREABILIDADE.md` | 7704 | `a53116c6aa5708d6e400343beed13054894090e29e04b4be5a9e76019115ffc7` |
| `PGC-001.md` | 16758 | `dd4b8850314013945fdf71ca675f936bf00096398b0b4dd5c6d9dadb814164c8` |
| `RATIFICACAO-INICIAL-MODELO.md` | 1756 | `bb587176c53d8dd4917dad073eab3a9118984583cf2cd960b6a79eaa7831db43` |
| `README.md` | 5671 | `8c3ede1272d30e9422e164b5bafc74c75188563b31eec0d46461a071e871aff5` |
| `REGISTRO-DE-EMENDAS.md` | 3587 | `e44178b1213ca280eb22f9944e8c708ea333a9499bb797205cb0d2db1cea172a` |
| `verificacoes\auditar_pacote.py` | 8991 | `72ed6612f692bff761f7ce8d623eadeb292e8a1ace83f45709ac367c267ab9b8` |
| `verificacoes\casos-adversariais.json` | 100677 | `1ce1146310bd8edf605f226034a29e528add1d06c6ea18b33c0e783c9a229d7a` |
| `verificacoes\gerar_catalogo.py` | 16874 | `889758b729315748249ee256fdc2ae0aaeb021cfc12e281336c2a208a8fd2483` |

**Nenhuma falha detectada pelos checks estáticos executados.** Isso não demonstra aprovação normativa ou operacional.
