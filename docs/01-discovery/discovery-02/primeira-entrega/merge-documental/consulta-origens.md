# Como localizar a origem de uma afirmação

[Entrada da edição](README.md) · [Edições e autoridades](proveniencia.md) · [Mapa de A e B](correspondencia-ab.md)

<a id="chaves"></a>
## Escolher o ponto de partida

O ZIP corrigido v0 contém 291 membros. O Repasse 2 possui os índices de consulta e o inventário de S1, com os complementos de S2. Se a busca começa por uma pergunta de continuidade, abra consulta/pendencias.md no ZIP e localize a família e a linha. ONB-PEN designa o motor, VIS identifica oito linhas do piloto visual, Q pertence ao catálogo de memória, DISC-EA e QD-AD identificam as agendas de A e de B, e ED-LAC identifica as oito tensões editoriais. Confronte o objeto com [sucessões](sucessoes.md) e [decisões e continuidade](temas/13-decisoes-e-continuidade.md).

Para recuperar os dois arquivos na conta autorizada, use os nomes e os SHA-256 da tabela. A entrada da edição encaminha também ao comprovante por destino. As localizações internas abaixo se referem à raiz do respectivo ZIP.

| Arquivo | SHA-256 | Primeira leitura |
| --- | --- | --- |
| Plataforma_Engenharia_Agentica_Consolidada_Corrigida.zip | `11f3e256e6cd3f6c59ed8cc6bc22b3dc771aeb1be8ed727741bf058a7f3d062b` | `LEIA-ME.md` |
| Repasse-2-Merge-EA-r1.zip | `79c62cd6449a6ff6018f5b7f785b0d1a76b118671c51af82db24333c08a2317e` | `LEIA-PRIMEIRO.md` |

No Repasse 2, índices-origem é grafado `indices-origem/`. O inventário de membros auxiliares identifica por caminho, resumo criptográfico e disposição os 108 objetos atribuídos à conferência IDX. Ele distingue guias e atalhos da origem que sustenta a afirmação.


<a id="volta"></a>
## Da redação ao original e do original ao destino

1. No ZIP corrigido, abra o capítulo temático e procure o bloco Axx-yyy. Em rastreabilidade/temas/xx.md, siga a nota com os IDs na ordem original. O ID temático nomeia a síntese; cada ID F1–F4 identifica uma passagem.
2. No Repasse 2, procure o ID inteiro em indices-origem/unidades.jsonl. Os campos caderno, linha_ancora e passagem_no_caderno_registro_do_zip apontam para o detalhe do ZIP. O campo coordenada_original leva ao parágrafo, linha de tabela ou intervalo físico no original correspondente. As linhas de tabela precisam do cabeçalho que rege a célula.
3. Para o percurso inverso, procure a chave origem em indice-reverso.jsonl e cada ID resultante em matriz.jsonl. Leia contribuições, ressalvas, consumidores e pendências. Converta o destino proposto em arquivo efetivo com plano/arquivos.json. O pacote de provas da edição final acrescenta a seção e a identidade congelada do destino; parta da [entrada](README.md).
4. Para uma passagem sem bloco direto, mantenha o detalhe próprio, procure a unidade em indices-origem/concordancia-sem-bloco.jsonl e abra a ficha do tema titular. A ausência de um pareamento textual naquela pesquisa não resolve novidade, contradição ou ausência semântica.

São 4.285 IDs distribuídos em 144 faixas e 121 cadernos. Os 279 blocos dos temas 01–13 ligam-se a 1.178 IDs por 1.630 pares distintos. Os outros 3.107 IDs mantêm origem e detalhe próprios. Há ainda 223 relações de outra natureza. A função de um bloco, de um apoio e de uma comparação interessa mais que o total bruto de referências.

| Pergunta | Bloco e nota do ZIP | Origem e leitura a recuperar |
| --- | --- | --- |
| Qual a ampliação da memória? | A05-020 · rastreabilidade/temas/05.md#n20 | F3-T06R03, F3-P094 e F3-T17R03. A regra anterior exige validade por afirmação. F3 acrescenta a apresentação do estado de sustentação ao engenheiro e propõe CA22. |
| O que a exportação de uma vista conserva? | A09-023 · rastreabilidade/temas/09.md#n23 | F2-P061 e F2-P134–136. Em F2-P135 separe os elementos transferidos, as regras que permanecem no gerador e a regeneração que ainda requer prova. |
| Quem define a Solução? | A01-012 · rastreabilidade/temas/01.md#n12 | F4-L380, F3-P044, F2-P005 e F4-L434. Distinga a dúvida antiga, o piloto de vistas e a decisão funcional de P08. Confronte DEC-042, DEC-045, RET-08 e PEN-042. |

Exemplo de volta pelo ZIP: F2-P135 aparece em `rastreabilidade/origens/f2-008.md` L20 e remete a `detalhes/09-documentacao-visual/f2-07.md#f2-p135` L41–43. A unidade também sustenta a comparação r12 em `rastreabilidade/relacoes.md`. Uma ocorrência pode servir a mais de um propósito.


<a id="formatos"></a>
## Ler coordenadas de Word e Markdown

Nos DOCX F1–F3, P conta parágrafos diretamente sob o corpo de word/document.xml, incluindo os vazios. T é o índice da tabela direta e R é a linha, contando o cabeçalho como 1. Leia as células na ordem XML, inclusive mesclagens e quebras internas; um hiperlink distingue texto exibido e alvo. As 65 tabelas têm 579 linhas incluindo cabeçalhos. Os 114 parágrafos fora do índice material estão discriminados com posição e função. O motor preserva os dois fluxos numerados de oito e sete itens. Para reconstituir uma tabela ou relação, abra indices-origem/tabelas-word.csv, relacoes-word.csv, fora-dos-ids.csv e elementos-especiais.jsonl no Repasse 2.

Para F4, L indica a linha física a partir de 1. Um bloco cercado inclui as duas cercas, o texto interno e, quando aplicável, nós, relações e condições da legenda. Um cabeçalho de tabela qualifica inclusive as linhas citadas isoladamente. Reabra as [correspondências A/B](correspondencia-ab.md) para interpretar um endereço herdado.


<a id="onb"></a>
## Séries e vocabulário do motor

Em F1-P330–353, DIR01, RF01, RQ01 e CA01 abreviam ONB-DIR-01, ONB-RF-01, ONB-RQ-01 e ONB-CA-01 quando usadas pelo complemento. Na tabela de vínculos, requisitos de qualidade atravessam mais de uma família. Um cenário pode investigar várias dimensões; a suficiência e execução continuam sujeitas a avaliação específica.

O glossário F1-T28R01–21 diferencia a capacidade oferecida sob condições, o adaptador que traduz contratos e preserva efeitos, o artefato nativo e o derivado. O retorno observado ancora a verificação da operação. O fallback é a alternativa quando a via principal falha ou se mostra insuficiente. Essa distinção impede atribuir ao efeito real um resultado meramente pretendido.


<a id="series"></a>
## Identificadores homônimos e referências externas

Em F2-P186 e seguintes, S01–S30 identificam 30 referências técnicas da edição de 22/11. S01 aponta para CodeWiki; em F3-P355 a mesma grafia pertence ao histórico de necessidades da conversa. Conserve fonte, família e edição na chave. Em F4-L4212–4514, R06 pode identificar risco ou revisão do Workspace. IDs ilustrativos de registro e tarefa ajudam a ler exemplos, e as PoCs A–G são localizadas por título de A.

As 69 entradas ED-URL em F4-L4139–4209 apontam para os usos de cada endereço. A ocorrência e o rótulo são elementos de proveniência. Versão vigente, licença aplicável, desempenho real ou acesso empresarial pedem verificação competente. Antes de abrir uma referência externa, considere o escopo de consulta autorizado. Para links de branch e blobs de arquivo, veja [duas edições do mesmo caminho](proveniencia.md#revisao-git).
