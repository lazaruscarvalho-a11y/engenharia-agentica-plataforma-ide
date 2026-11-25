# Histórico de retificações — D01-R2

Revisão documental 1. Este histórico altera a interpretação corrente de definições sem apagar o que a revisão 1 conseguiu demonstrar. A classificação anterior era prudente para o recorte então acessível. A evidência nova é **D01-S05 — declaração reproduzida no pedido atual**; não é recuperação técnica de todas as mensagens originais.

## Base preservada

A revisão anterior de [REGISTRO.md](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/d9e48c3d36598d40f9d2e38caf836bccb5fac97f/docs/01-discovery/discovery-01/REGISTRO.md), do [manifesto](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/d9e48c3d36598d40f9d2e38caf836bccb5fac97f/docs/01-discovery/discovery-01/MANIFESTO.json) e do [recibo](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/d9e48c3d36598d40f9d2e38caf836bccb5fac97f/auditorias/discovery-01/RECIBO-PUBLICACAO.json) permanece por commit imutável. O recibo antigo não é reescrito para validar R2. O [dossiê reproduzido](../../../auditorias/discovery-01-r2/DOSSIE-REPRODUZIDO.md) localiza a fonte adicional pelas âncoras E01..E36.

## Retificações de classificação e desdobramentos

Todos os registros existentes evoluem da revisão documental 1 para 2, mantendo identidade. A natureza é campo explícito, não deduzida do prefixo do ID.

| ID preservado | Classificação/alcance na revisão 1 | Classificação/alcance corrente e fonte adicional | Justificativa, impactos e pendências restantes |
|---|---|---|---|
| D01-REL-001 | Relato do assistente de compreensão profunda/incremental | Intenção explícita reproduzida, D01-S05/E02 | Acrescenta dimensões materiais, investigação ampla, incremento e limites. Motor/métricas continuam D01-PEN-007 |
| D01-REL-002 | Relato de agnosticidade | Intenção/restrição reproduzida, E08 | Devin/Claude/Copilot e adaptações mínimas necessárias preservados; formato de adaptador é D01-PEN-006, não decisão reaberta |
| D01-REL-003 | Relato de três níveis sem correspondência recuperada | Decisão conceitual reproduzida, E06 | Micro/Meso/Macro têm correspondência definida. Relação organizacional exata e herança continuam D01-PEN-002 |
| D01-REL-004 | Menção indireta a Git Submodules | Decisão de topologia Meso reproduzida, E09 | Repositório Meso e Micro como submódulos deixam de ser hipótese. Macro desdobrado em D01-DEC-006/E10; atualização/permissões continuam D01-PEN-002/003 |
| D01-REL-005 | Relato de compartilhamento/reconciliação automática | Decisão de intenção reproduzida de consolidação predominantemente automática, E12 | Necessidade compartilhada desdobrada em D01-NEC-001/E11; controles e publicação em RST-002/DEC-007. Protocolos não aprovados; D01-PEN-003 |
| D01-REL-006 | Relato de migração cuidadosa | Intenção determinada reproduzida, E26 | Preserva tipos de artefatos, reconciliação/adaptação e relatório ao engenheiro. Substituir redundância não autoriza exclusão; mecanismos D01-PEN-006 |
| D01-REL-007 | Relato composto: uso provisório e código autorizado | Decisão reproduzida de uso provisório preservando originais, E28 | Código desdobrado em D01-DEC-014/E29 e referência padrão em DEC-015/E30. Relação anterior preservada; autorização específica D01-PEN-004 |
| D01-REL-008 | Restrição de exclusão relatada | Decisão restritiva reproduzida, E27 | 'Sempre exija' vinculado à pergunta sobre remoção automática versus aprovação. Objeto/revisão e mudança material preservados; não houve exclusão; D01-PEN-004 |
| D01-REL-009 | Relato agregado de segurança/autorizações/concorrência/inconsistências | HISTÓRICO/DESDOBRADO, sem canônico ativo independente | Encaminha a REL-005, RST-002, DEC-007, DEC-010..013, DEC-016/017. Não duplica definição nem apaga o agrupador histórico |
| D01-DEC-001 | Decisão diretamente recuperada de permissão/aviso para legado | Mesma decisão; contexto reforçado por E31 | Inventário inicial autorizado é distinto de consulta posterior para lacuna. Não cria permissão de escrita/execução/exclusão |
| D01-DEC-002 | Decisão diretamente recuperada de conclusão com pendências não críticas | Mesma decisão; E32 reproduz pergunta/resposta | Catálogo/evidência permanecem; estados/UX técnicos continuam propostas; D01-PEN-005 |
| D01-DEC-003 | Decisão diretamente recuperada de classificação objetiva e recurso ao engenheiro | Mesma decisão; E33 reproduz pergunta/resposta | Taxonomia e limiares posteriores continuam candidatos; D01-PEN-005 |
| D01-DEC-004 | Decisão de consolidação/continuidade | Mesma decisão; E36 e pedido corretivo atual | Abrange revisão corretiva e preservação do contexto; não executa D02 nem aprova sua arquitetura; D01-PEN-001/007/009 |

A classificação **decisão reproduzida** conserva a escolha declarada sem exigir que algoritmos, protocolos ou permissões corporativas já tenham sido definidos. Não há promoção automática de todos os detalhes do dossiê a requisitos normativos.

## Registros novos e origem lógica

| Âncoras | Novos IDs | Motivo de criação |
|---|---|---|
| E01, E04, E05 | D01-INT-001..003 | Objetivo, paradigma e uso do conhecimento não tinham unidades próprias |
| E03, E13 | D01-RST-001..002 | Restrição de execução local e exigência de confiabilidade antes ausentes/agregadas |
| E07, E10, E14 | D01-DEC-005..007 | Git canônico, Macro/Submodules e separação trabalho/publicação são escolhas distintas |
| E11 | D01-NEC-001 | Compartilhamento com concorrência e autonomia é necessidade própria; não escolhe modalidade de workspace |
| E15, E16 | D01-CTX-001..002 | Restrição de Actions e fluxo corporativo são relatos, não políticas universais |
| E17..E19 | D01-DEC-008, D01-INT-004, D01-DEC-009 | Distinguir implantação, comportamentos mistos e suporte a reprodução/integração são definições distintas |
| E20..E25 | D01-INT-005..006, D01-DEC-010..013 | Sistemas inacessíveis, fontes indiretas e quatro modalidades de autorização exigem registro delimitado |
| E29, E30 | D01-DEC-014..015 | Desdobramento do composto provisório/código/padrão evita sobrecarga do REL-007 |
| E34, E35 | D01-DEC-016..017 | Gestão contínua de pendências e retroalimentação posterior passam a ter unidades individuais |

## Propostas e hipóteses preservadas

| ID histórico | Estado na revisão 1 → R2 | Efeito da evidência nova |
|---|---|---|
| D01-PROP-001 | Proposta → proposta | Fluxo completo não é aprovado pela permissão de consulta de DEC-001 |
| D01-PROP-002 | Proposta → proposta | Fronteiras de dados/execução compatíveis com restrições; sem autorização operacional nova |
| D01-PROP-003 | Proposta → proposta | DEC-002/016 dão intenção, mas sequência de resolução permanece candidata |
| D01-PROP-004 | Proposta → proposta | Bloqueio proporcional é recomendação; sem política definitiva |
| D01-PROP-005 | Proposta → proposta | Estados continuam candidatos; 'Permitir' não aprovou a máquina posterior |
| D01-PROP-006 | Proposta → proposta | Taxonomia continua candidata; 'Sim' não escolheu limiares |
| D01-PROP-007 | Proposta → proposta | RST-002 exige rigor; fatores/verificações detalhados não se tornam decisão retroativa |
| D01-PROP-008 | Proposta → proposta | Apresentação/revisão de classificação ainda candidata |
| D01-PROP-009 | Proposta → proposta | DEC-016 individualiza exigência de gestão/comunicação de pendências; implementação/UX não aprovada |
| D01-PROP-010 | Exemplo → exemplo proposto | Não é tela implementada/aprovada |
| D01-PROP-011 | Roteiro → roteiro proposto | Direção D02 aceita; método/arquitetura não antecipados |
| D01-HIP-001 | Hipótese → hipótese | Agnosticidade e Git canônico confirmados por reprodução; núcleo/projeções concretas ainda hipótese |
| D01-HIP-002 | Hipótese → hipótese | Topologia escolhida não aprova protocolo de revisão/obsolescência |
| D01-HIP-003 | Hipótese → hipótese | Migração cuidadosa escolhida não prova eficácia do inventário/verificações propostos |

Novos D01-PROP-012..021 (revisão 1) inventariam contribuições materiais de P-A/B/C/E/F/G/H/I/J/L. P-D referencia HIP-001; P-K referencia PROP-005/006/010. O [registro](REGISTRO.md) mantém a disposição dos doze grupos com justificativa de intenção versus detalhamento.

## Dois eixos de fechamento

A reconciliação material de E01..E36 pode ser conferida independentemente da recuperação integral da transcrição. D01-PEN-001 não deve continuar como bloqueio genérico a decisões agora reproduzidas: seu eixo material é avaliado pela matriz/auditoria e publicação R2; seu eixo de recuperação integral permanece limitação enquanto não demonstrado. Pendências de interpretação, especificação, arquitetura e operação permanecem em [REVISAO.md](REVISAO.md); não rebaixam escolhas históricas conhecidas a meras hipóteses.
