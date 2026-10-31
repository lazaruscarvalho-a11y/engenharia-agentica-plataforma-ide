# Revisão e pendências — D01-R2, revisão 2

Esta revisão distingue fidelidade histórica, refinamento e prova de publicação. O [relatório de auditoria](../../../auditorias/discovery-01-r2/RELATORIO.md) registra a revisão congelada, achados, correções e testes; o [recibo R2](../../../auditorias/discovery-01-r2/RECIBO-PUBLICACAO.json) sustenta a persistência. Não se declara ausência absoluta de defeitos.

## D01-PEN-001 — dois eixos independentes

**A — Reconciliação material:** E01..E36 e P-A..P-L têm disposição na [matriz](MATRIZ.md), fonte e definição canônica, com retificações de R1. Pode ser concluída no escopo acessível depois de auditoria e publicação verificadas. O relatório/recibo determina se essa condição foi cumprida, não a contagem isolada de linhas.

**B — Recuperação técnica do histórico integral:** **NÃO COMPROVADA**. A nova consulta retornou cinco turnos finais atuais, incluindo respostas truncadas de elaboração do prompt. As declarações reproduzidas pelo usuário em D01-S05 suprem a reconciliação material sem fabricar recuperação das mensagens originais. Não há omissão material conhecida no escopo declarado do dossiê; a possibilidade de contribuições ausentes além dele permanece um limite de certeza.

Na R1, D01-PEN-001 era uma pendência única. A R2 preserva seu ID, desdobra os eixos e retifica as classificações nos [registros de mudanças](RETIFICACOES.md). A falta de tecnologia escolhida não mantém uma decisão conceitual como relato não confirmado.

## Pendências preservadas e reclassificadas

Categorias: **A** consolidação histórica; **B** interpretação; **C** especificação funcional/UX; **D** técnica/arquitetural; **E** operacional/corporativa. A responsabilidade humana indicada é papel a confirmar, sem inventar identidade ou prazo. O assistente prepara investigação/documentação ordinária; só a decisão efetiva e o acesso legítimo dependem da pessoa.

| ID estável | Categoria / estado R2 | Escopo remanescente e registros afetados | Encaminhamento e bloqueio real |
|---|---|---|---|
| D01-PEN-001 | A, eixo A condicionado à verificação; eixo B limitado | Todas E01..E36; classificações REL retificadas | Aferir fonte/matriz/auditoria/recibo. B não impede continuidade material demonstrada; não alegar transcrição integral |
| D01-PEN-002 | B/D, refinamento | E06/E09/E10: correspondência Micro/Meso/Macro e topologia já declaradas; falta relação exata sigla/projeto/domínio/conta, herança, atualização/ponteiros/acesso | Refinar contratos sem pedir nova confirmação da topologia; bloqueia implementação definitiva, não fechamento histórico |
| D01-PEN-003 | C/D/E, refinamento | E11..E15/E35: compartilhamento, consolidação automática controlada, revisão-base, concorrência, publicação, revogação, recuperação, gatilhos duráveis | Especificar e ensaiar controles; motor local de validação continua proposta; não protege pushes por fora nem autoriza novas Actions |
| D01-PEN-004 | C/E, refinamento | E03/E22..E25/E27..E31: execução local, consulta exterior/legado, modalidades pontual/reusável/individual/coletiva, escrita e exclusão | Especificar escopo, identidade, validade, revogação e objeto/revisão. Escolhas de modalidades e exclusão aprovada não estão em aberto; decisões não concedem acesso real |
| D01-PEN-005 | C/D, refinamento | E13/E32/E33/E34: evidência mínima, criticidade, incerteza, bloqueio proporcional, revalidação e transições | Formalizar critérios rigorosos verificáveis; taxonomia/limiares candidatos. Bloqueia classificador operacional, não registro da escolha humana |
| D01-PEN-006 | C/D, refinamento | E04/E05/E07/E08/E21/E26: formato, navegação, adaptação por ferramenta, catálogo federado, preservação/transformação semântica | Manter canônico em Git e agnosticidade; árvore, esquema, projeções, caches e índices específicos continuam propostos |
| D01-PEN-007 | C/D, próxima investigação | E01/E02/E17..E20/E34/E35: motor, profundidade/cobertura/confiabilidade/custo e contexto heterogêneo | Discovery 02, com evidências e metas candidatas; sem seleção antecipada de stack/algoritmo |
| D01-PEN-008 | E, dependência interna | E15/E16/E19..E25: direitos, classificação, retenção, integrações e implantação real | Confirmar controles e contratos com autoridades internas, quando essa fase ocorrer; não acessar dados corporativos nesta missão |
| D01-PEN-009 | C/E, continuidade/distribuição | E36: nova sessão real e distribuição nativa | Preparar/testar recuperação disponível com escopo explícito. Fontes/Instruções nativas NÃO ATUALIZADAS; nova conversa real de usuário é distinta de agente isolado |
| D01-PEN-010 | C, UX | E05/E23/E26/E30..E35: avisos, autorização, estados, evidências, pendências por ciclo e esclarecimentos | Refinar UX/acessibilidade sem converter exemplos e taxonomias em layout/máquina de estados aprovados |

Não se exige resolver B/C/D/E para fechar A, salvo ambiguidade que impeça registrar o significado material declarado. Nenhuma pendência de implementação é transferida ao usuário como tarefa de reconstituir o histórico.

## Guardrails da reconciliação

- Natureza “decisão” e qualidade “declaração reproduzida” são campos distintos; não há prova de mensagem original por mero aceite do dossiê.
- Respostas curtas têm pergunta antecedente no registro; “Sim” não aprova detalhes surgidos depois.
- Decisão sobre produto é distinta de permissão operacional. Executar aplicações localmente cabe ao engenheiro; não instalar/subir aplicação por iniciativa do agente.
- Consulta exterior, consulta posterior ao legado, escrita/publicação e exclusão são autorizações distintas. Aprovação da migração não exclui originais; fonte acessível não implica redistribuição.
- Main e commit de submódulo não provam implantação, sincronização nem acesso. Contextos mistos não são uniformizados silenciosamente.
- Fluxo corporativo é relato contextual; scheduled/GMUD e hotfix não viram política universal ou ação autorizada.
- Pendência não crítica continua rastreável após conclusão com ressalvas; E34 e E35 são requisitos de direção individuais, sem supor carregamento integral ou processamento assíncrono existente.
- P-A..P-L, PROP e HIP preservados; referências a contratos candidatos não ativam PGC/CT.

## Validação e condições de conclusão

A matriz contém disposição por âncora, evidência, natureza, revisão, maturidade, capacidade, destino, cobertura, justificativa e pendência; há navegação inversa por registro, documento, capacidade, derivação, pendência e critério futuro. A revisão semântica confronta conteúdo e fonte, além de testes estruturais e negativos.

O auditor distinto dos autores recebe candidato congelado e critérios, sem gabarito de conclusões. Achados materiais exigem correção e novo congelamento. A evidência real, inclusive eventual limitação de continuidade, está no relatório. Todos os testes desta missão são **documentais**; não são testes funcionais da IDE nem os 49 CA operacionais PGC.

Publicação usa revisão-base conferida e atualização condicional sem force push no PR #6. Arquivos reobtidos por commit imutável, bytes/SHA-256/hash Git comparados; herdados fora do escopo preservados; recibo novo publicado e reobtido separadamente. Recibo R1 permanece intacto. PGC/CT não ratificados, main e permissões sem alterações desta missão.

[Revisão R1 histórica](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/ceedbc1f0fcb4133ce8109ec889676dca966193d/docs/01-discovery/discovery-01/REVISAO.md).
