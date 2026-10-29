# Plataforma/IDE de Engenharia de Software Agêntica

**PGC-001: PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO / NÃO TESTADO OPERACIONALMENTE.**

Este repositório privado recebe a proposta documental inicial de governança do projeto. A publicação em branch ou a aprovação de um PR não constituem ratificação ou ativação normativa.

## Fontes e navegação

- [README original do pacote](docs/00-governanca/PGC-001_v1.1.2_candidata_ratificacao/README.md): índice dos nove documentos, contratos e recursos auxiliares.
- [PGC-001 v1.1.2](docs/00-governanca/PGC-001_v1.1.2_candidata_ratificacao/PGC-001.md): proposta da norma central; contratos CT-001 a CT-008 v1.0.2 estão no índice original.
- [Estado atual e pendências](ESTADO-ATUAL.md).
- [Orientações para agentes](AGENTS.md).
- [Auditoria desta importação](auditorias/importacao-pgc-001-v1.1.2/RELATORIO.md): integridade, versões, referências e ressalvas.
- [ZIP original preservado](acervo/PGC-001_v1.1.2_candidata_ratificacao.zip) e [hash do acervo](acervo/SHA256SUMS.txt).

Os 18 arquivos extraídos foram mantidos byte a byte, com seus caminhos internos preservados. O diretório do pacote e o ZIP de acervo representam o mesmo conjunto: o ZIP é a evidência de origem, não uma segunda fonte normativa. Os índices desta raiz apontam às fontes sem reproduzir suas normas.

## Verificação e adoção

Os 17 hashes do inventário original conferem; o hash do próprio inventário e do ZIP constam na auditoria. Os 65 checks estáticos foram reproduzidos em cópia isolada. Os 49 cenários adversariais permanecem `NOT_RUN`: não existe evidência de execução operacional do harness.

Há ressalvas de rastreabilidade e nomenclatura registradas na auditoria. A candidata foi importada fielmente para revisão; essas ressalvas não foram corrigidas nos originais. Ratificação futura exige consentimento explícito sobre o conjunto exato, versões e hashes, além dos demais critérios aplicáveis. Nenhum manifesto de ratificação ou ativação foi criado.

Para conferir a cópia local: `python auditorias/importacao-pgc-001-v1.1.2/verificar_importacao.py`. O verificador só lê os arquivos. Os scripts originais regravam artefatos e devem ser executados apenas em cópia isolada.
