# Modelo funcional candidato do onboarding

Este documento organiza as definições de [REGISTRO.md](REGISTRO.md). **As sequências e estruturas abaixo são propostas de consolidação**, salvo o comportamento explicitamente coberto por D01-DEC-001..004. Não há funcionalidade implementada por esta documentação.

## Necessidade e fronteira

O onboarding deve preparar conhecimento recuperável para que agentes compreendam repositórios e trabalhem sob supervisão. Precisa preservar conhecimento existente, explicitar lacunas e evitar que importação de instruções se transforme em autorização para executá-las. A fundação já descreve JOR-001 e CAP-001/002/003/008; a conversa aprofunda a migração, mas sua abertura e a definição inicial do problema não foram recuperadas. Não se inventam métricas de valor, atores adicionais ou prioridade global de MVP.

O engenheiro é o ator explicitamente citado para autorizar consultas e resolver classificações incertas. Outros papéis e direitos corporativos precisam ser refinados. A Plataforma interpreta e propõe; o executor não recebe autoridade humana por ser capaz de agir.

## Conhecimento Agent-First e camadas

| Tema | Preservado do histórico acessível | Detalhamento ainda candidato/pendente |
|---|---|---|
| Agnosticismo | REL-002 cita independência de Devin/Claude/Copilot | HIP-001 sugere núcleo e projeções; contratos, precedência e fidelidade pendentes |
| Micro/Meso/Macro | REL-003 cita três níveis Git hierárquicos | Qual nível corresponde a plataforma, conta/sigla, aplicação ou repositório; como tratar monorepos e múltiplas contas |
| Git Submodules | REL-004 cita o mecanismo | Topologia, quem fixa/atualiza ponteiros, acesso e caminhos; ausência de transação global entre repositórios |
| Compartilhamento | REL-005 cita segurança e reconciliação automática | Origem/destino permitidos, classificação, gatilhos, escopo de proposta vs publicação automática e divergências |
| Incrementalidade | REL-001 cita compreensão incremental | Detecção de mudança, revisão-base, invalidação transitiva, custo e cobertura no Discovery 02 |

Não se fixa a equivalência “Micro=repositório, Meso=conta, Macro=plataforma” como decisão recuperada. Pode ser uma pergunta de reconciliação, apoiada na proposta de camadas da fundação. Também não se assume que usar Submodules sincronize conteúdo automaticamente, conceda acesso ao repositório referenciado ou garanta atomicidade global.

## Jornada candidata

| Passo | Entrada e resultado esperado | Exceções e vínculo |
|---|---|---|
| 1. Delimitar escopo | Repositórios e revisões autorizados, fontes permitidas e finalidade; registrar o que não pode ser lido | Permissão ausente não é suprida por README; CAP-001, CT-005 candidato |
| 2. Inventariar | Catalogar código, documentação e instruções legadas, com origem e revisão | Não executar hooks; distinguir conteúdo inacessível, excluído e ainda não analisado; REL-006, HIP-003 |
| 3. Compreender | Produzir achados com evidência, relações e limitações | Algoritmos, agentes e profundidade são o escopo do Discovery 02; REL-001 |
| 4. Preparar estrutura | Propor conhecimento agnóstico, níveis e vínculos origem→destino | Camadas/Submodules dependem de reconciliação; REL-002..005 |
| 5. Reconciliar migração | Comparar conteúdo preservado, conflitos, lacunas e impacto | Não resolver contradição por mera preferência do modelo; PROP-003/007 e HIP-003 |
| 6. Usar provisoriamente | Disponibilizar conhecimento com limitações visíveis e operações autorizadas | REL-007 não dispensa autorização de código; lacuna que depende do legado segue DEC-001 |
| 7. Classificar e decidir | Classificação fundamentada e recurso humano se incerta | DEC-003; taxonomia PROP-006; não converter “indeterminada” em não crítica |
| 8. Concluir ou manter bloqueio | Permitir conclusão com pendências não críticas controladas | DEC-002; estados PROP-005; pendências e operações afetadas continuam identificáveis |
| 9. Consolidar e evoluir | Incorporar correções verificadas, histórico e referências; atualizar por revisão autorizada | Leitura não aprova escrita; exclusão do original exige aprovação expressa relatada em REL-008 |

A autorização inicial de inventário/migração e a permissão para voltar ao legado diante de lacuna são momentos distintos. DEC-001 não foi reinterpretada como necessidade de um diálogo por cada arquivo do inventário; granularidade e reutilização de permissão continuam em D01-PEN-004.

## Lacuna durante uso provisório

Fluxo proposto PROP-001..004: registrar conhecimento ausente/incompleto/contraditório; identificar operações afetadas; informar ao engenheiro qual artefato legado pode ajudar e por quê; solicitar autorização antes da consulta para suprir a lacuna. Se negada, manter a pendência e seguir somente em atividades independentes. Se autorizada, ler como fonte de dados, verificar e propor correção. A pendência só se resolve após incorporação e verificação adequadas. Publicação e eliminação do original não decorrem da permissão de consulta.

Exemplo inteiramente sintético: o repositório `servico-exemplo` foi migrado; o conhecimento provisório não explica recuperação de mensagens. O inventário aponta `docs/operacao/recovery.md`. A IDE candidata informa lacuna, impacto e motivo da consulta e apresenta ações de autorizar/negar. Esse caminho é ilustrativo; não foi acessado um documento empresarial nem implementada uma tela.

## Inconformidades e conclusão

| Situação candidata | Efeito proposto | Origem/estado |
|---|---|---|
| Nenhuma pendência conhecida impeditiva | Concluída | PROP-005; não prova compreensão perfeita |
| Pendência não crítica rastreável | Concluída com ressalvas, com limitações e acompanhamento | DEC-002 permite; nomes/UX são PROP-005/009 |
| Falha crítica | Bloquear conclusão segura e operações afetadas, resolver e revalidar | PROP-006; critérios detalhados pendentes |
| Criticidade indeterminada | Investigar ou encaminhar ao engenheiro antes de liberar dependentes | DEC-003 exige recurso humano se incerto; estado operacional é PROP-006 |

Perda de instrução de segurança e referência documental quebrada são exemplos do assistente para investigar criticidade, não regras universais aprovadas. Uma referência quebrada pode ser material dependendo do contexto. Quantidade de pendências e confiança verbal do modelo não bastam para justificar liberação. Conclusão com ressalvas não autoriza consulta silenciosa ao legado, exclusão, produção ou alterações de código fora do escopo concedido.

## Segurança, concorrência e consolidação

São preservadas as fronteiras da fundação e os temas REL-005/009. Controles novos permanecem propostas: registrar revisão-base e fontes, classificar dados antes de compartilhar, verificar acesso no destino, separar leitura/interpretação/preparação/publicação/exclusão e não executar instruções embutidas. Usar sínteses sintéticas externamente e não transportar segredos entre níveis de conhecimento.

Para alterações concorrentes, proposta de engenharia: comparar revisão esperada, recusar atualização incompatível, reler e reconciliar; se o conteúdo mudou materialmente, reavaliar a autorização aplicável. Timeout de escrita exige consulta ao destino antes de repetir. Commit por repositório não demonstra transação distribuída. Essa compatibilidade com CT-003/005 candidatos não certifica conformidade normativa nem recupera decisões técnicas ausentes do histórico.

Uma reconciliação “automática” pode preparar diagnóstico/diff sem publicar nem excluir. O alcance exato de automação anterior não está recuperado; D01-PEN-003 impede tratá-lo como aprovação irrestrita. A consolidação deve distinguir achado, proposta, decisão humana, arquivo publicado e verificação do conteúdo exato.

## Registro mínimo candidato

Para cada item migrado/inconformidade: ID; origem e revisão; destino e revisão; natureza (informação/instrução); status de migração; evidência de preservação ou lacuna; operações afetadas; criticidade e justificativa; incerteza; permissão de consulta com escopo e referência quando existir; correção proposta; resultado de verificação e pendências. Esse esquema é novo detalhamento de engenharia, sem campos obrigatórios aprovados ou contrato de software definido.
