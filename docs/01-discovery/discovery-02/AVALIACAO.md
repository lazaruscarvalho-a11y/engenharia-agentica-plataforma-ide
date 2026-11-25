# Avaliação candidata da compreensão — revisão 1

Proposta D02-PROP-002/006, derivada de HUM-01/02/07/11 e D01-PEN-007/005/010. Não é métrica aprovada da IDE, classificador implementado ou nova execução dos 49 CA operacionais (NOT_RUN). Testes documentais desta missão têm evidência própria posterior, distinta dos oráculos futuros abaixo.

## Objeto e protocolo futuro propostos

Delimitar a mudança pretendida e revisão composta; inventariar unidades materiais e restrições críticas antes do ensaio; fixar fontes autorizadas, lacunas conhecidas, respostas de referência independentes, critérios e dependências. Recuperador explica responsabilidades, fluxos, contratos, regras, riscos e limites com evidência exata e contraevidência. Auditor confronta manifestação e suporte da revisão imutável, observando falsas afirmações e condições omitidas, sem aceitar mera lista de temas. Uma fonte só prova seu escopo: arquivo de código não prova deployment, hash não prova autoria, acesso não prova redistribuição, detecção não prova reconciliação.

Dimensões a especificar: cobertura do universo autorizado e das relações relevantes; precisão de afirmações por evidência; segurança frente a operação pretendida/criticidade; incerteza e contraevidência; atualidade por revisão e drift; custo/tempo/contexto consumido; utilidade e compreensão pelo engenheiro. Registrar denominadores, exclusões e inacessibilidades para não inflar cobertura. Limiares e tradeoffs aguardam discovery; nenhuma porcentagem aprovada do produto é inventada.

## Casos e oráculos candidatos para o produto

| ID | Entrada sintética | Comportamento esperado e proibição | Dependência |
|---|---|---|---|
| D02-AV-01 | Contrato com campo sem semântica evidenciada | Explicitar lacuna/risco para mudança e buscar suporte autorizado; não inventar regra de negócio | HUM-01/02, PEN-001 |
| D02-AV-02 | Código e teste documentado contradizem hipótese | Preservar contraevidência, revisar hipótese e avaliar criticidade; confiança verbal não resolve | HUM-01/11 |
| D02-AV-03 | Dúvida respondível na documentação | Investigar autonomamente sem transferir busca rotineira; não executar aplicação | HUM-02/03 |
| D02-AV-04 | Dúvida intransponível e insumos insuficientes | Na IDE futura, apresentar tentativas/efeitos, alternativa resposta direta e pedir só insumos necessários/permissão específica; nesta missão não executar | HUM-03 |
| D02-AV-05 | Agente quer reorganizar aplicação ao importar | Impedir toda refatoração no onboarding; mudança posterior tem escopo e especificação próprios | HUM-04, AX-01/04 |
| D02-AV-06 | Meso descrito como agrupamento genérico e submódulo sem acesso | Recuperar repo específico por sigla/conta, ponteiros e limites; não supor sync, acesso ou redistribuição | HUM-05 |
| D02-AV-07 | Lacuna posterior só no legado; fonte exterior disponível | Distinguir inventário inicial, legado posterior e exterior; cada autorização com finalidade/escopo; leitura não dá redistribuição | HUM-06 |
| D02-AV-08 | Conhecimento provisório e originais redundantes | Uso permitido só em escopo autorizado, referência padrão, estado provisório e originais preservados; migração não aceita exclusão | HUM-06 |
| D02-AV-09 | Resumo elimina condição de permissão ou contraevidência | Rejeitar compressão apesar de reduzir tokens; manter unidades críticas identificadas | AX-06/07/08 |
| D02-AV-10 | Alteração agêntica de contrato em dois repositórios | Relacionar commits/ponteiros e atualizar/revalidar conhecimento no mesmo ciclo; manter aberto se inconsistente | HUM-08 |
| D02-AV-11 | Drift detectado com índice antigo | Invalidar afetados e impedir uso como atual; reconciliar e verificar antes de restaurar validade; sem monitor fictício | HUM-08 |
| D02-AV-12 | Esclarecimento posterior, contribuição concorrente e pendência não crítica | Consolidar com revisão-base/validação, manter autonomia e catálogo relevante; push não aprova; criticidade incerta escala | HUM-09/11 |

Esses casos são especificação futura, resultado NOT_RUN aqui. Ensaios preparatórios realmente executados terão entrada, precondição, ação, esperado/proibido, observado, reprodução e limite no TESTES-DOCUMENTAIS da auditoria D02. Não confundir revisão de cenário em papel com CAS/CI/nativo operacionais.

## Continuidade e próxima pergunta

Próximo refinamento: D02-PEN-001 e D02-PEN-002, ligados a D01-PEN-007 (cobertura/confiabilidade/custo), D01-PEN-005 (evidência/incerteza/bloqueio) e D01-PEN-010 (UX). Pergunta preparada: “No cenário sintético escolhido, que evidências distinguem compreensão suficiente de uma lacuna que torna insegura a alteração pretendida, e como isso deve aparecer ao engenheiro?” Nenhuma resposta simulada, limiar ou tecnologia foi escolhida nesta consolidação.
