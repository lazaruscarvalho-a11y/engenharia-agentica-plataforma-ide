# Composição candidata das Fontes D02 — revisão 1

Missão PM-D02-CONSOL-001 R5, 31/10/2026. Projeto ID g-p-6ae4fdf0eb688191bb6536420421ef69. Preparação documental; nenhuma Fonte/Instrução nativa foi inspecionada/atualizada nesta missão. PS/PI são provas independentes do Git e do pacote. Limites atuais da conta/interface desconhecidos por login; não fixar quantidade/tamanho por memória. [Configuração e fallback](CONFIGURACAO.md).

## Conjunto integral e cobertura

A projeção planejada para upload contém cinco Fontes: `00-ENTRADA-E-CONFIGURACAO.md` (entradas e índice), `01-DISCOVERY-02.md` (D02/axiomas/blueprint), `02-DISCOVERY-01-HISTORICO.md` (fontes canônicas D01 históricas), `03-FUNDACAO-E-CANDIDATOS.md` (fundação/PGC/CT) e `04-PROVENIENCIA-E-PROVAS.md` (fontes, proveniência e identidades; sem rubrica de recuperação). São projeções, não arquivos nativos já aplicados. Cada trecho preserva origem por caminho/commit/blob/SHA-256/linhas; JSON pertinente é incluído integralmente. Links relativos são mapeados a URLs imutáveis e conferidos no mapa do pacote; o conteúdo indispensável deve estar no conjunto, sem exigir Git durante RF. O ZIP durável também preserva originais documentais byte a byte e fornece manifesto, hashes, mapa de links, instruções integrais e configuração separadas. Não aplicar se o conjunto completo exceder o limite real sem nova segmentação fiel verificada; quantidade planejada não prova capacidade da conta.

O pacote final F deve ser gerado somente a partir do content_commit remoto G verificado, por GET autenticado/base64 ou objetos Git, comparando todos os bytes/blobs selecionados. Não basta manifesto local arbitrário ou árvore da autoria. Preservar arquivos/caminhos separados; se segmentar/concatenar por limite real, fornecer índice de origem repo/commit/caminho/âncora e mapa testado de links/âncoras, mantendo originais autorizados no pacote durável. Timestamps reais de emissão ficam em recibo externo. ZIP idêntico só é alegado se metadados fixos e duas gerações comparadas; caso contrário apenas composição lógica determinística.

A tabela abaixo é a composição integral do ZIP para o operador. As exclusões do upload do recuperador estão explicitadas ao final e no manifesto do pacote, preservando proprietários canônicos de todo conhecimento material.

| Prioridade | Conteúdo necessário no ZIP integral | Cobertura e motivo |
|---|---|---|
| P0 | ESTADO-ATUAL, RETOMADA raiz, AGENTS e RETOMADA D02 | Uma rota vigente, base/estado/limites e ponto de continuidade; histórico subordinado às retificações |
| P0 | D02 REGISTRO, RETIFICACOES, FONTES, MATRIZ e manifesto D02 | HUM-01..11, restrições/proveniência, decisões/propostas/pendências, inversa e revisão |
| P0 | docs/fundacao/axiomas-arquiteturais.md e ARCHITECTURE_BLUEPRINT.MD | Dez axiomas completos com cinco classes e integração rastreável; síntese substituta explícita |
| P1 | D02 MODELO-FUNCIONAL, CONTRATOS-CANDIDATOS, AVALIACAO, REVISAO, README | Fluxos/estados/UX/interfaces/métricas candidatas e controles da missão; nenhuma implementação/aprovação técnica |
| P1 | D01 README, FONTES, REGISTRO, RETIFICACOES, MODELO-FUNCIONAL, MATRIZ, REVISAO, MANIFESTO e auditoria/recibo R2 pertinentes | E01..36/P-A..L e fontes herdadas, suporte HUM-06/09; conteúdo histórico não reescrito, D02 tem ponte vigente |
| P1 | Visão/roteamento/metodologia/sessões/capacidades/registro de conhecimento/proveniência recuperada da fundação e dependências materiais | Produto completo, maturidade/método e contexto mínimo suficiente; expandir só dependências que alterem interpretação/autoridade |
| P1 | PM R5, matriz 74 e relatório R5, BLUEPRINT-ORIGEM e provas D02 existentes da fase de conteúdo | Dossiês curados autorizados e limitação histórica; testes antigos não novos |
| P1 | docs/chatgpt/INSTRUCOES-PERMANENTES.md, CONFIGURACAO.md e este inventário | Texto integral para campo separado, aplicação/verificação/recuperação, inventário/cobertura |
| P2 | Governança candidata/contratos e auditorias antigas quando dependência pertinente | Preservados no Git; sem ratificação por upload; rota imutável e motivo de exclusão/impacto no manifesto do pacote |

Seleção exige fechamento de dependências transitivas e prova de que nenhuma decisão/restrição crítica disponível ficou só em arquivo excluído/link indisponível. O manifesto do pacote contém caminhos normalizados, modos, bytes, SHA-256, blobs conhecidos, content_commit/tree e exclusões por categoria/motivo/impacto/rota alternativa. Zero perda silenciosa. Pacote integral durável e fontes prontas para upload têm tamanho/hash/releitura após cópia; recibos de eventos posteriores seguem em suplemento separado.

## Manter, substituir logicamente e excluir

Manter originais, Fontes anteriores e regras nativas não revogadas até inspeção/backup; não remover fisicamente por esta instrução. Substituição lógica: rota atual D02 e retificações D02-RET-001..004; fonte antiga fica histórica identificada, nunca instrução concorrente silenciosa. Se coexistência causar recuperação material incorreta, suspenda ativação e diagnostique. Excluídos da redistribuição nova: credenciais/segredos, dados/código corporativos, transcrições reais, caches/temporários/logs crus. R3/blueprint original inexistentes no escopo não são fingidos como anexos recuperados. Acervos normativos não são reescritos nem gerados de novo.

Instruções são texto separado da Fonte, aplicadas só após conteúdo/cobertura/ensaio de conflito PS; não assumir que carregar este inventário aplica o campo nativo. Histórico Git anterior de instruções/configuração/inventário está em `historico/pre-d02/*.md.snapshot`, sem uso ativo e sem substituir backup nativo. Fontes são snapshots; nova mudança autorizada requer pacote/conferência/aplicação/verificação/recibo novos, sem sync automático.

## Separação entre operador e recuperador

O ZIP integral preserva documentos e provas; RF não recebe esse ZIP. As cinco Fontes de upload contêm proprietários canônicos de conhecimento de produto/autoridade e proveniência, sem o PM completo, fixtures, pareceres, respostas de recuperação, CONFIGURACAO, REVISAO e matriz de controles D02 reservados ao avaliador. Esses originais permanecem disponíveis ao operador no pacote durável. O manifesto do pacote enumera native_source_paths/operator_only_paths e comprova que todo elemento material HUM/AX/D01 continua nas Fontes; exclusão de rubrica não exclui decisão ou restrição. No upload, 04 reúne FONTES/proveniência/identidades, não respostas esperadas; 00 é entrada/índice. Registre o campo de Instruções e memória como canais automáticos; regras canônicas de produto não são prova de leitura das Fontes por si. Se outro canal puder explicar a resposta e faltar atribuição suficiente, RF é INCONCLUSIVO.
