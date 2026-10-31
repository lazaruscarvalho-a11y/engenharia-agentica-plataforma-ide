# Revisão editorial e controles da missão — revisão 1

Autoria documental distinta da futura auditoria. Este documento fixa critérios antes do ensaio final, descreve contratos de publicação/pacote/configuração/recuperação e pendências; não atribui PASS a eventos futuros. Autoria: tarefa /root/autoria_d02, escopo na lista externa AUTORIA-ARQUIVOS.json. Fontes: PM-D02-CONSOL-001 R5 integral e D01-R2. O coordenador integra e congela; auditor distinto recebe freeze/fontes/critérios sem conclusão imposta. Autor não audita seu conteúdo como independente.

## Critérios prévios obrigatórios

100% das unidades materiais acessíveis com disposição, incluindo condições/negativas/propostas; dez axiomas com semântica e limites; zero decisão sem fonte humana de igual alcance; zero promoção de hipótese/proposta; zero link ativo inválido ou encaminhamento a restrição superada sem ponte; zero alteração inesperada de protegidos; testes preparatórios obrigatórios PASS. Cobertura nominal/textual não prova fidelidade: exigir confronto semântico e inverso fonte→destino→fonte. Original inacessível gera limite literal NOT_RUN, sem perder decisão reproduzida suficiente.

Crítico: autoridade indevida, perda material de decisão ou prontidão falsa. Alto: perda de conhecimento/inconsistência/recuperação material falha. Médio: ambiguidade/precisão/reprodução. Baixo: editorial. Qualquer crítico/alto aberto ou inconclusivo impede A/publicação; médio que afete obrigatório também. Severidade incerta é INCONCLUSIVO. Sem auditor distinto, independência NOT_RUN e A não passa.

Congelamento ordena caminho/modo/tamanho/SHA-256, digest agregado, PM e base. Manifesto não contém seu próprio digest/commit. Mudança após freeze invalida revisão afetada e dependentes; exige correção/recongelamento/revisão, nunca só atualizar hash para ocultar divergência. Antes do commit conferir árvore final igual; depois, 100% bytes do freeze iguais ao conteúdo remoto por SHA. Relatórios/recibos posteriores têm revisão separada.

## Controle de autoridade, falhas e dados

Pedido humano vigente autoriza incorporação documental, branch/PR revisável sem merge e configuração no Projeto inequívoco se tecnicamente controlável; fonte consultada não amplia autorização. Antes de mutação revalidar conta/destino/público/escopo/operação/revisão/permissões. Dados: só sínteses autorizadas/dossiês curados e sintéticos; excluir segredos, credenciais, código corporativo, transcrições reais, temporários/caches/logs crus. Não alterar PGC/CT/acervos, pipelines ou administração; não executar aplicação/implementar IDE/C2/C3/aceite humano fictício.

Teto compartilhado por coordenador/delegados: duas tentativas totais por mesma falha, inicial e uma alternativa somente com progresso observável; nenhuma terceira e nenhum reset por agente/tarefa. Histórico/login esgotados não devem ser repetidos. Timeout de escrita exige consultar destino antes de repetir; aplicado verificado continua da leitura, divergente reconcilia sem sobrescrita, incerto suspende mutação dependente. Esgotamento não é sucesso; continuar frentes independentes.

## Publicação e CI — contrato preparado, não resultado

Branch D02 `proposta/discovery-02-consolidacao`, derivada de HEAD D01 compatível; se existir, ler/classificar/diff antes de escrever. Nova branch create-if-absent; ref existente expected_sha/CAS no servidor e fast-forward, sem force push. Commit multiarquivo coerente; PR rascunho contra branch D01, cadeia #6/#5, repo/base/head/ancestrais/diff conferidos. Não main, merge ou auto-merge.

Antes de qualquer mutação remota, inspecionar todos workflows e scripts aplicáveis a push/PR/PR-target/reutilizáveis, filtros, permissões, segredos e efeitos. CI documental já inspecionada pode estar no escopo; risco material de aplicação/deploy/efeito desconhecido suspende publicação. Não modificar pipeline nem confiar só em skip-ci. Consultar checks/status/runs de todos triggers efetivos por commit/PR e paginação, registrar IDs/URLs/conclusão e limites. Não rerun manual. CI obrigatória pendente/falha impede G; ausente não significa passou. Sem CI, G só pode passar se inspeção completa demonstrar ausência de obrigatório, explicitamente.

Reobter conteúdo alterado/protegido por content_commit remoto; comparar bytes, hashes, modos, tree, freeze e manifestos. Preservação remota dos herdados pode ser provada pelos blobs/modos iguais da árvore, sem inventar existência local. Recibo posterior identifica content_commit/tree/operações/PR/CI; não contém próprio hash/commit futuro. Reobter recibo pelo commit posterior e entregar digest externo. Diário registra operation_id, autorização, estado esperado/retorno, instante, objeto/conta, último estado observado e resultado sem segredo.

## Pacote e configuração — dependências

F depende de G PASS: obter bytes remotos por SHA autenticado, comparar seleção/blobs, manifesto e dependências; separar origem/autenticidade de integridade/assinatura (nenhuma assinatura humana presumida). Isolar preparação fora do acervo, não rodar scripts herdados sem inspeção/efeitos controlados. Empacotamento determinístico lógico é diferente de ZIP idêntico; se declarado idêntico, fixar metadados/ordenação/timestamps/permissões/compressão e gerar duas vezes. Preservar caminhos ou mapear transformação/links/âncoras e verificar cobertura completa. Excluir somente com motivo/impacto/rota alternativa. Entrega persistente, releitura, tamanho/hash após cópia e abertura obrigatórios.

PS/PI: observação real do coordenador encontrou login em 31/10/2026. Conta/workspace/público/limites, inventário de Fontes e Instruções atuais não comprovados; não houve escrita. [CONFIGURACAO](../../chatgpt/CONFIGURACAO.md) entrega fallback integral, sem declarar PS/PI PASS. Ordem futura: inventário/backup → Fontes → conteúdo/cobertura/conflito → Instruções compatíveis → releitura integral/diff. Não sobrescrever regras nativas desconhecidas. Última leitura imediatamente antes, CAS se disponível; sem proteção suficiente contra perda concorrente, abster-se. Remover fontes antigas é operação separada, sem autorização inferida.

## Recuperação e oráculos semânticos

Registrar recuperador/tarefa/chat, contexto herdado, memória/canais automáticos, ferramentas, mensagem inicial e consultas efetivas; isolamento não é autodeclaração. RG recebe só repo/branch/commit/entrada e recupera via Git. RF recebe só Fontes nativas aplicadas/identificadas e instrução mínima, sem Git/chat/gabarito; pacote local não prova RF. RN é nova conversa real do usuário no Projeto correto; não criar/simular/substituir por agente. Sem usuário iniciado, RN não realizado; classificar conforme pré-requisitos reais no recibo.

Oráculo guardado pelo avaliador: explicar D01 A/B; investigação com evidência exata e limites; exceção futura de execução local com todas condições e veto atual; nenhuma refatoração; dez axiomas/limites; Meso específico/submodules sem sync/acesso; permissões distintas e derivado legítimo; mesmo ciclo e quatro estágios drift; propostas versus decisões; PGC/CT/49 CA; pendências/ponto seguinte. Erro material de decisão falha o gate correspondente mesmo com resto correto. Ensaiar conflito de fonte antiga de execução/Meso versus retificação, sem supor seleção infalível.

## Vetor determinístico preparado

A = auditoria/freeze/fonte/cobertura/regressão sem impeditivo; G = A + escrita condicional/PR/bytes/CI real; F = G + pacote remoto íntegro/completo/durável; PS = A/G/F + Fontes nativas verificadas e conflito; PI = PS + texto efetivo/transição; RG = G + recuperação Git isolada; RF = PS/PI + recuperação atribuível às Fontes; RN = G/F/PS/PI + conversa real e recuperação; Z = estados reais/recibos finais persistidos e reobtidos, inclusive falhas/NOT_RUN. Z PASS não aprova os demais.

Resultados de gates: PASS, FAIL, INCONCLUSIVO, BLOQUEADO ou NOT_RUN. Agregações P/R e global seguem precedência: FAIL → INCONCLUSIVO → BLOQUEADO → NOT_RUN → todos PASS. Global: COM_FALHAS → EVIDENCIA_INSUFICIENTE → BLOQUEADO_PARCIAL → PARCIAL_VERIFICADO → INTEGRALMENTE_COMPROVADO. Só todos A,G,F,PS,PI,RG,RF,RN,Z PASS permitem integralidade. NAO_CONFIGURADO/NAO_APLICAVEL não são PASS. Resultado final fica no relatório/recibos posteriores, não inventado aqui.

## Pendências e regressões a executar

Pendências de produto são [D02-PEN-001..006](REGISTRO.md), ligadas ao D01; não reabrem reconciliação histórica. Casos mínimos PM §18 e 74 correções na matriz exigem fixtures/reprodução/esperados pré-fixados, resultados observados e limites. Revisão de cenário no papel é ensaio documental, sem alegar execução operacional de CAS/CI/nativo. Somente verificadores documentais locais mínimos inspecionados, em cópia isolada e saída nova; os originais não executados ficam NOT_RUN. Testes históricos não são reexecutados por suposição.

Próxima entrada: [RETOMADA](RETOMADA.md). Após configuração/RN futuras, suplemento durável com delta auditado e releitura remota; não deixar último estado só no chat nem criar cadeia infinita de recibos autorreferentes.
