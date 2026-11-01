# Relatório de limitações e verificação do PM-D02 R5

31/10/2026 · America/Sao_Paulo · Escopo: corrigir AUD-01/AUD-02, atualizar a matriz e entregar revisão local. Nenhuma incorporação foi executada.

## Entrega e correções

O [Prompt-Master R5](PROMPT-MASTER-DISCOVERY-02-R5.md) preserva o corpo operacional do R4 e corrige as duas ressalvas da [auditoria anterior](C:/Users/Carvalhos/.codex/visualizations/2026/10/31/01a19331-8f27-72d3-8e4d-652d916348b0/auditoria-pm-d02/AUDITORIA.md). A [matriz atualizada](MATRIZ-CORRECOES-74.md) conserva DEF-001..DEF-074 e suas severidades: 7 críticos, 46 altos e 21 médios. Cláusulas R4-NNN e âncoras r4-NNN são IDs estáveis herdados, enquanto a identidade do arquivo agora é R5. Não houve renumeração histórica.

| Achado | Correção e regressão conferida | Estado nesta revisão |
|---|---|---|
| AUD-01 | R4-010 estabelece duas tentativas totais, inicial e uma alternativa fundamentada; veda terceira e reset por troca de agente/tarefa; preserva consulta após timeout. R4-039 propaga o teto ao contrato delegado. | CORRIGIDO-DOC |
| AUD-02 | §4 discrimina HUM-06 como síntese D01; §4.6 informa commit, caminho, revisão 2, seis grupos de registros/âncoras/linhas e separa controles técnicos propostos das escolhas humanas. | CORRIGIDO-DOC |

As disposições DEF-005/006/010/022 foram rechecadas no delta. DEF-013/014 também foram precisadas para refletir as fontes e a distinção entre modalidade escolhida e mecanismo proposto. As demais linhas conservam conteúdo, com ajustes apenas de identidade da revisão e links. Não foi identificada ressalva remanescente desses dois achados no escopo documental corrigido; isso não é garantia absoluta de ausência de defeitos.

## Fontes e preservação

O PR #6 foi reconsultado somente em leitura antes da edição: aberto, em rascunho, sem merge, HEAD D01 `e37af725a162c577cfa9ffde286d0fcf69294429`, base fundação `f8d7c60955a1250ae4d94a428386787f4aaa24b0`. Foram obtidos por esse SHA o registro D01, seu manifesto e a metodologia. Conteúdos e blobs estão em [FONTES-CONSULTADAS-R5.json](evidencias/FONTES-CONSULTADAS-R5.json). A linha 61 da metodologia estabelece duas tentativas por falha; o registro revisão 2 sustenta os seis grupos de HUM-06. A seleção é limitada às dependências destas correções, sem nova auditoria de toda a fundação.

O R4 original, sua matriz, relatório e quatro arquivos de evidência foram preservados no diretório original. A comparação de caminhos, tamanhos e SHA-256 antes/depois está em [PRESERVACAO-R4-ANTES.json](evidencias/PRESERVACAO-R4-ANTES.json) e no [recibo final](evidencias/VERIFICACAO-R5.json). Nenhum gerador/verificador que escreva nesses originais foi executado. Os diffs [do prompt](evidencias/DELTA-PROMPT-R4-R5.diff) e [da matriz](evidencias/DELTA-MATRIZ-R4-R5.diff) tornam a alteração revisável.

## Verificação final e seu alcance

O [verificador da revisão](evidencias/verificar-r5.py) só lê os documentos entregues e as fontes fixadas; grava seu resultado no recibo externo. Confere identidade R5, preservação dos sete arquivos R4, 74 IDs/severidades, âncoras/alvos, seções 0–20, links locais, suporte das referências HUM-06 e integridade dos blobs consultados. Compara cláusulas e linhas da matriz para detectar alterações fora do escopo e verifica que os critérios de autorização, gates e recuperação permanecem preservados. Os casos específicos de tentativas e proveniência são revisões documentais de entradas/esperados contra as cláusulas; não são execuções de agentes, CAS, CI ou Projeto.

O recibo registra resultados efetivamente observados. A [rodada inicial](evidencias/VERIFICACAO-R5-RODADA-INICIAL.json) apontou duas falhas do verificador: inventários iguais ordenados com critérios distintos e checagem do link do próprio recibo antes de sua gravação. Corrigiram-se a ordenação canônica e a sequência da checagem, sem dispensar comparações nem alterar os arquivos R4. O resultado da rodada final está no recibo externo. As 29 verificações e as 625 combinações relatadas pelo R4 permanecem evidências históricas do R4, não foram transplantadas como testes desta revisão. A verificação R5 e sua segunda leitura são revisão própria do delta; auditoria independente do novo conteúdo de incorporação permanece requisito da missão futura.

## Identidade dos arquivos

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| PROMPT-MASTER-DISCOVERY-02-R5.md | 75442 | ada7257fabb483c921ab3ead2eb6fe7db2d1ccb742502da28dfa9c33b7431da6 |
| MATRIZ-CORRECOES-74.md | 34636 | 8a46579e766b20e7ac8a8a95e78787b00ff811a44134fc32834b03f7d91f88e1 |

O hash deste relatório é externo, em VERIFICACAO-R5.json. O recibo final tem identidade externa na entrega, sem autorreferência. Tamanhos e hashes identificam bytes UTF-8/LF, não commit Git ou assinatura humana.

## Limitações preservadas e prontidão

O R3 literal, seu digest e o blueprint histórico integral continuam inacessíveis no escopo herdado. R5 é revisão corretiva do substituto R4, não certificação linha a linha do R3. As reproduções humanas de execução local e nenhuma refatoração pertencem ao pedido de reconstrução R4, não a uma nova recuperação das falas originais. A correção HUM-06 não reabre a reconciliação material D01-PEN-001/A nem concede acesso ao legado.

O R5 está preparado para ser usado em missão posterior expressamente autorizada, com suas verificações e gates. Essa missão ainda deverá produzir e congelar seu próprio candidato D02, obter auditor distinto dos autores, revalidar fontes/permissões e comprovar Git, pacote, Fontes/Instruções e recuperação separadamente. Esta entrega não atribui PASS a A/G/F/PS/PI/RG/RF/RN/Z da incorporação. Nova conversa real continua indispensável à integralidade; os 49 CA operacionais permanecem NOT_RUN e PGC/CT não ratificados.

GitHub, Projeto ChatGPT, snapshot do repositório e entrega original R4 não foram alterados. A saída é um conjunto novo de arquivos locais R5, acompanhado de evidências de verificação e preservação.
