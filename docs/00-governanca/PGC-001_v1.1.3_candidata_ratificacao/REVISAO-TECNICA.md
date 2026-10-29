# Revisão técnica v1.1.2 → v1.1.3

**PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO / NÃO TESTADO OPERACIONALMENTE.**

O usuário autorizou a revisão técnica dos três pontos auditados. Essa autorização não ratifica o pacote. A v1.1.2 e seu ZIP permanecem intactos. Esta candidata mantém nove documentos e os 49 IDs CA, todos NOT_RUN. PGC passa a v1.1.3 e os oito contratos a v1.0.3 para identificar o conjunto compatível; nos CT-003..007 a mudança se limita aos metadados de versão/referência. O esquema JSON do catálogo permanece 1.0.2 porque o formato não mudou.

## EM-007 — Decisão por associação

As diferenças foram avaliadas como vínculos de cobertura direta ou parcial, não provas de satisfação integral de cada obrigação. Nenhum vínculo anterior foi retirado. A tabela informa os acréscimos em cada visão; IDs, estímulos e oráculos CA não são renumerados nem enfraquecidos. `contract_owners` é recalculado com os mesmos donos principais da matriz.

| Norma | Acrescentado à matriz | Acrescentado ao catálogo | Justificativa de pertinência (escopo parcial quando aplicável) |
|---|---|---|---|
| N-002 | CA-44 | CA-02, CA-03, CA-04, CA-05, CA-06 | CA-02..06 exercitam a distinção entre intenção, proposta, fonte e aprovação; CA-44 aplica essa classificação aos detalhes derivados. |
| N-006 | CA-43 | CA-05 | CA-05 conserva a revisão vigente diante de decisão nova; CA-43 exige autoridade e escopo na primeira ratificação. |
| N-007 | CA-43, CA-49 | — | CA-43 vincula a ratificação ao digest; CA-49 limita a aprovação à revisão/escopo A. |
| N-009 | — | CA-32 | CA-32 distingue revisão/digest aprovado do resultado de rebase. |
| N-010 | — | CA-07, CA-12, CA-46 | CA-07 verifica concorrência na publicação; CA-12 bloqueia conteúdo com digest alterado; CA-46 exige o portão de ativação. |
| N-012 | — | CA-35 | CA-35 preserva a verdade de publicação com falha posterior, sem apresentar estado parcial como completo. |
| N-013 | — | CA-28 | CA-28 depende da identificação da revisão de origem do artefato derivado. |
| N-014 | CA-28 | — | CA-28 exige revalidação ou invalidação do dependente da revisão antiga. |
| N-015 | CA-03, CA-24 | — | CA-03 trata aprovação em documento como dado; CA-24 considera versão e autoridade da fonte. |
| N-016 | CA-43 | — | CA-43 exige ratificação por autoridade e não permite reutilização do bootstrap. |
| N-022 | — | CA-46, CA-47 | CA-46 exige recibo da ativação; CA-47 conserva evidência da falha e impede alegação de vigência. |
| N-023 | CA-47 | — | CA-47 preserva o manifesto anterior após falha posterior à publicação. |
| N-025 | — | CA-35 | CA-35 distingue commit efetuado e pós-verificação falha. |

## EM-008 — Data da aprovação

Adota-se `issued_at`, já especificado por CT-002, com semântica comum em CT-001. A data de criação de rascunho não concede aprovação. Não há migração silenciosa de dados nem aprovação real: apenas a fixture CA-49 recebe um instante sintético com fuso para verificar o formato documental.

## EM-009 — Bytes reproduzíveis

Gerador e auditor escrevem bytes UTF-8/LF, sem BOM, com ordem e caminhos estáveis; a opção --check não regrava nem em caso de falha. O relatório não contém timestamps de execução nem caminhos absolutos. O ZIP de distribuição usa entradas ordenadas, timestamps e atributos fixos, sem compressão dependente de versão de biblioteca. O inventário exclui a si próprio e é recalculado após o relatório. Hash de inventário não é assinatura nem manifesto de ativação.

## Limites

As regressões documentais não implementam nem testam o harness. A execução nativa foi feita em Windows; testes de portabilidade exercitam o contrato de bytes e a independência da ordem de enumeração, sem alegar execução em Linux/macOS. Proteções, autenticação normativa, CAS, captura automática, runner dos CA e ratificação permanecem pendentes. Aprovação desta revisão ou do PR não ativa a política.
