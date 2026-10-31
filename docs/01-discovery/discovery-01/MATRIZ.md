# Matriz de rastreabilidade D01

Registro canônico: [REGISTRO.md](REGISTRO.md). Fontes: [FONTES.md](FONTES.md). Pendências: [REVISAO.md](REVISAO.md). CAP-* remetem ao [catálogo herdado](../../fundacao/capacidades.md); vínculos são análise desta consolidação, não aprovação de novos requisitos. Todos os oráculos abaixo são **planejados / NÃO EXECUTADOS** para a futura Plataforma. Conferência documental desta entrega é distinta.

| Definição | Fonte localizável | Classe | Capacidades | Oráculo futuro / evidência esperada | Pendência |
|---|---|---|---|---|---|
| D01-DEC-001 | S02-A humano | Decisão explícita | CAP-008/013/016 | D01-V01: lacuna sintética gera aviso e pedido; nenhuma consulta ao legado antes da permissão | D01-PEN-004 |
| D01-DEC-002 | S02-B humano, pergunta A | Decisão explícita | CAP-008/013/015 | D01-V02: permite conclusão com pendência não crítica visível e preservada; não apaga evidência | D01-PEN-005 |
| D01-DEC-003 | S02-C humano, pergunta B | Decisão explícita | CAP-002/008/013/015 | D01-V03: classifica por evidência verificável; ambiguidade encaminha ao engenheiro | D01-PEN-005 |
| D01-DEC-004 | S02-D/E e S01 | Decisão de continuidade | CAP-008/016 | D01-V04: nova sessão localiza base, fontes, estados e pendências pelo recibo | D01-PEN-001/009 |
| D01-REL-001 | S02-C/D assistente | Relato anterior | CAP-002/006 | D01-V05: achados em revisões incrementais têm fonte e cobertura conhecida | D01-PEN-001/007 |
| D01-REL-002 | S02-C/D assistente | Relato anterior | CAP-003/019/020 | D01-V06: mudança de executor preserva conhecimento e semântica | D01-PEN-001/006 |
| D01-REL-003 | S02-C/D assistente | Relato anterior | CAP-001/003/008 | D01-V07: contexto recupera nível correto e detecta conflito de herança | D01-PEN-001/002 |
| D01-REL-004 | S02-D assistente | Relato anterior | CAP-001/003/012 | D01-V08: ponteiro fixado, alteração divergente e acesso negado são distinguíveis | D01-PEN-001/002 |
| D01-REL-005 | S02-C/D assistente | Relato anterior | CAP-008/013/016 | D01-V09: não compartilha dado sem acesso; conflito não vira sobrescrita silenciosa | D01-PEN-001/003 |
| D01-REL-006 | S02-C/D assistente | Relato anterior | CAP-002/003/008 | D01-V10: perda/contradição injetada é detectada no mapa origem→destino | D01-PEN-001/006 |
| D01-REL-007 | S02-A/C assistente | Relato anterior | CAP-012/013 | D01-V11: uso provisório sinaliza lacunas; mudança de código exige escopo concedido | D01-PEN-001/004 |
| D01-REL-008 | S02-B/C assistente | Restrição relatada | CAP-008/013 | D01-V12: original permanece sem aprovação expressa específica de exclusão | D01-PEN-001/004 |
| D01-REL-009 | S02-D assistente | Temas relatados | CAP-008/013/016 | D01-V13: revisão concorrente/resultado incerto preservam histórico e impedem falso sucesso | D01-PEN-001/003 |
| D01-PROP-001 | S02-A assistente | Proposta | CAP-008/013/016 | D01-V01: rastrear etapas e autorização contextual sem acesso prematuro | D01-PEN-004 |
| D01-PROP-002 | S02-A assistente | Proposta | CAP-003/012/013 | D01-V14: instrução/hook malicioso sintético é dado; permissão de leitura não permite executar/publicar/excluir | D01-PEN-004/008 |
| D01-PROP-003 | S02-A assistente | Proposta | CAP-008/015/016 | D01-V15: consulta isolada não encerra pendência; negação preserva bloqueios dependentes | D01-PEN-004/005 |
| D01-PROP-004 | S02-A assistente | Proposta | CAP-010/013 | D01-V16: bloqueio localizado não paralisa trabalho independente nem libera dependente crítico | D01-PEN-005 |
| D01-PROP-005 | S02-B assistente | Proposta | CAP-008/014 | D01-V17: transições distinguem concluída/ressalvas/bloqueada sem perda de pendências | D01-PEN-005/010 |
| D01-PROP-006 | S02-C assistente | Proposta | CAP-008/015 | D01-V03: casos crítica/não crítica/indeterminada têm justificativa e efeitos diferentes | D01-PEN-005 |
| D01-PROP-007 | S02-C assistente | Proposta | CAP-002/015 | D01-V18: evidência contradizendo confiança do modelo impede classificação sem fundamento | D01-PEN-005/007 |
| D01-PROP-008 | S02-C assistente | Proposta | CAP-013/014/016 | D01-V19: classificação exibe artefatos/evidências/medidas e revisão humana preserva controles | D01-PEN-005/010 |
| D01-PROP-009 | S02-B assistente | Proposta | CAP-003/008/016 | D01-V02: agentes recebem limitações relevantes após conclusão com ressalvas | D01-PEN-005/006 |
| D01-PROP-010 | S02-A assistente | Exemplo proposto | CAP-013/014 | D01-V20: engenheiro entende lacuna, impacto, objeto e efeito de autorizar/negar | D01-PEN-010 |
| D01-PROP-011 | S02-D assistente | Roteiro proposto | CAP-002/003/006/010/015 | D01-V21: Discovery 02 produz achados e métricas candidatas com fontes | D01-PEN-007 |
| D01-HIP-001 | Consolidação atual | Hipótese nova | CAP-003/019 | D01-V06: comparar núcleo/projeções sem perda de restrições relevantes | D01-PEN-006 |
| D01-HIP-002 | Consolidação atual | Hipótese nova | CAP-003/008/016 | D01-V07/08/09: revisão e permissões divergentes impedem uso indevido/obsoleto | D01-PEN-002/003 |
| D01-HIP-003 | Consolidação atual | Hipótese nova | CAP-002/008/015 | D01-V10: medir detecção de perda, duplicação, contradição e referência quebrada | D01-PEN-006/007 |

## Cobertura inversa e lacunas

| Capacidade herdada | Definições D01 relacionadas | Alcance |
|---|---|---|
| CAP-001 | REL-003/004, HIP-002 | Organização do workspace; topologia pendente |
| CAP-002 | DEC-003, REL-001/006, PROP-007/011, HIP-003 | Compreensão/classificação; algoritmo não definido |
| CAP-003 | REL-002/003/004/006, PROP-002/009, HIP-001/002 | Conhecimento e contexto; sem formato/precedência aprovados |
| CAP-006 | REL-001, PROP-011 | Arquitetura e dependências para Discovery 02 |
| CAP-008 | DEC-001..004, REL-003/005/006/008/009, PROP-001/003/005/006/009, HIP-002/003 | Migração, histórico e pendências; não implementação da gestão integral |
| CAP-010 | PROP-004/011 | Dependências e agentes; não autorização de execução paralela nesta missão |
| CAP-012 | REL-004/007, PROP-002 | Código autorizado, Git e fonte não executável |
| CAP-013 | DEC-001..003, REL-005/007/008/009, PROP-001/002/004/008/010 | Supervisão e fronteiras de autorização |
| CAP-014 | PROP-005/008/010 | Estados e interação candidatos; sem layout aprovado |
| CAP-015 | DEC-002/003, PROP-003/006/007/011, HIP-003 | Verificação e criticidade; oráculos somente planejados |
| CAP-016 | DEC-001/004, REL-005/009, PROP-001/003/008/009, HIP-002 | Proveniência e continuidade |
| CAP-019/020 | REL-002, HIP-001 | Agnosticismo/portabilidade; nenhuma integração demonstrada |

CAP-004/005/007/009/011/017/018 e demais jornadas permanecem no catálogo da fundação. Não são descartadas nem declaradas refinadas integralmente pelo D01. A matriz cobre 27 definições deste registro; não equivale a cobertura dos turnos anteriores ausentes, dos requisitos da IDE ou dos CA do PGC.
