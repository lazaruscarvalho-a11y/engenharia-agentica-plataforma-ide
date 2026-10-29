# Revisão técnica do PGC-001 v1.1.3

**29/10/2026 — PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO / NÃO TESTADO OPERACIONALMENTE.**

O usuário autorizou a revisão dos três achados, sem ratificação. Base: commit `4f0450ac996505639d2d34ff79519e00dd8d1aa8`, PR #1, branch de importação da candidata v1.1.2. A nova branch é `proposta/revisao-pgc-001-v1.1.3`, com PR dependente da branch anterior; nenhum merge é necessário para revisar esta diferença.

## Mudanças e preservação

A [candidata v1.1.3](../../docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/README.md) mantém nove documentos; os oito contratos são v1.0.3. A [revisão técnica](../../docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/REVISAO-TECNICA.md) justifica os vínculos por obrigação e registra EM-007..009. As seis emendas anteriores, 25 obrigações, 20 achados e 49 IDs CA foram mantidos. O [diff das fontes](comparacao-fontes.diff) permite comparar versões.

Os 18 arquivos v1.1.2 e seu ZIP continuam byte a byte idênticos. Os 49 casos preservam estímulos, passos e oráculos: mudam apenas relações `requirements`/`contract_owners`; a fixture sintética de aprovação recebe `issued_at`. A data de emissão fica padronizada em CT-001/002. Nenhuma aprovação real foi criada. A nova candidata tem 20 arquivos, incluindo notas de revisão e regressões documentais, com 19 hashes no inventário.

## Verificações

- Checks: 76/76 PASS; os checks anteriores foram mantidos, com controles novos de relação bidirecional e metadados. O novo total não representa execução de mais casos CA.
- 99 pares norma/caso conferidos nas duas direções e contra a união das duas fontes antigas: zero associações perdidas, zero diferenças. Donos principais recalculados conferem com a matriz.
- 10/10 regressões documentais aprovadas: repetição, seeds diferentes, enumeração invertida, --check sem escrita e falhas injetadas de vínculos, data, versão e CRLF. [Saída integral](testes-documentais.txt).
- Catálogo e relatório conferem por --check; os arquivos gerados usam UTF-8/LF, sem BOM, caminhos relativos POSIX e ordenação explícita. A distribuição ZIP usa entradas ordenadas, data fixa e ZIP_STORED; duas gerações produziram os mesmos bytes.
- ZIP da candidata: 279050 bytes; SHA-256 `40829bb2ddfaa8b739c2d7b19918a703845dd6bc7d97c205f8b1ad5528db4b43`. [Acervo](../../acervo/PGC-001_v1.1.3_candidata_ratificacao.zip).

Resultados estruturados: [resultados.json](resultados.json). Conferência do snapshot completo e de ambos os pacotes: [verificar_revisao.py](verificar_revisao.py), somente leitura. O inventário antigo da importação descreve o commit antigo e deve ser executado naquele checkout; não é inventário dos índices atualizados nesta revisão.

## Limites e revisão

Execução nativa: Windows. Não foi executada uma segunda plataforma; as garantias exercitadas são de serialização e ordenação explícitas. Nenhum cenário operacional CA foi executado e todos permanecem NOT_RUN. Não há harness, IAM, CAS, sincronização ou proteções novos. A revisão dos vínculos admite cobertura parcial, não prova cobertura semântica completa.

Os hashes são inventários de integridade, não manifestos de ativação ou assinatura. Os modelos de ratificação seguem não assinados. O conteúdo é uma proposta para revisão por PR; não houve merge, ratificação ou ativação. O recibo de entrega separado identificará a publicação efetivamente verificada.
