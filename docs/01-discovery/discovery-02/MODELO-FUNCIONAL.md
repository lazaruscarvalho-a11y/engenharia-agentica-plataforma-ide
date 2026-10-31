# Modelo funcional candidato D02 — revisão 1

Projeção de HUM-01..HUM-11 e AX-01..AX-10, definidos no [ledger](REGISTRO.md) e nos [axiomas](../../fundacao/axiomas-arquiteturais.md). Sequência, nomes de estados, schemas, UX e algoritmos abaixo são D02-PROP-001..007, ainda propostas. Sem IDE implementada, aplicação executada ou norma ratificada.

## Jornada candidata de compreensão

| Etapa candidata | Entrada/precondição | Ação pretendida e saída | Falha/limite e intervenção |
|---|---|---|---|
| 1. Delimitar | Objetivo/mudança sintética, fontes permitidas, revisão e direitos | Identificar Micro/Meso/Macro, branches/commits e finalidade; catálogo de escopo lido/não lido | Identidade/permissão ausente bloqueia só fonte/efeito dependente; não presume acesso a submódulo |
| 2. Inventariar | Material autorizado de onboarding | Mapear código/documentação/configurações/contratos/testes/regras/dependências; preservar originais | Nenhuma refatoração; ausência/truncamento explícitos, sem reconstruir como fato |
| 3. Investigar | Catálogo, evidências e perguntas | Ampliar cobertura e aprofundar dirigido; responsabilidades, fluxos, contratos, regras, riscos e contraevidência | Busca exterior exige finalidade/fonte/escopo e autorização; consulta posterior ao legado exige permissão/aviso |
| 4. Estruturar | Unidades e suporte localizável | Distinguir fato verificado, relato, intenção, decisão reproduzida, proposta, hipótese e pergunta; registrar seis eixos de proveniência | Hipótese não vira fato; resposta curta sem pergunta não aprova derivação |
| 5. Avaliar | Mudança pretendida e unidades críticas | Confrontar suficiência, cobertura, precisão, incerteza e impacto; emitir lacunas e dependências | Criticidade incerta escala; conclusão com ressalvas somente não críticas e catalogadas; limiares pendentes |
| 6. Consolidar | Contribuição candidata, revisão-base, direitos e oráculos | Deduplicar/reconciliar de forma rastreável; verificar antes de publicação autorizada | Push de trabalho não publica conhecimento aprovado; concorrência rejeita sobrescrita e exige reconciliação |
| 7. Usar | Conhecimento vigente/provisório identificado e escopo de tarefa | Consultar/explicar e, em trabalho posterior autorizado, planejar/modificar/validar | Uso provisório não é verificação definitiva nem permissão genérica de código/execução |
| 8. Revalidar | Mudança agêntica ou alteração externa observada | Atualizar/revalidar conhecimento afetado no mesmo commit/PR; drift detectado é invalidado, reconciliado e verificado | Sem prova de consistência, manter ciclo dependente aberto; ausência de monitor não implica detecção contínua |

## Estados candidatos e validade

Uma unidade pode estar proposta, em investigação, verificada no escopo, provisória, contradita, invalidada ou superada; são nomes candidatos, separados da natureza de conteúdo e de resultado de teste. Verificada exige revisão e suporte do escopo; não significa certeza universal. Provisória identifica o limite, mantém originais e permite somente operações autorizadas. Contradita/invalidada não pode ser usada como atual sem ressalva e bloqueio das decisões dependentes.

| Drift — direção HUM-08 | Entrada | Saída e prova |
|---|---|---|
| Detectar | Alteração externa observada por leitura/ciclo | Diferença e revisão de origem identificadas; ainda não corrigida |
| Invalidar | Relação de impacto candidata | Unidades afetadas marcadas, uso como atual impedido; impacto/incerteza visíveis |
| Reconciliar | Fontes novas, contraevidência e autorização | Revisão candidata de conteúdo e relações; autoria/retificações preservadas |
| Verificar | Candidato e oráculos aplicáveis | Evidência da nova revisão contra fontes; só então restabelecer validade delimitada |

Em múltiplos repositórios, a revisão composta lista cada commit e ponteiro Micro/Meso/Macro e suas dependências. Fonte main não comprova implantação; versões DEV/HOM/PROD e branches podem diferir, inclusive dentro da mesma funcionalidade (D01-DEC-008/009, INT-004). Simulações e integrações reais são modos distintos; suportar ambos não autoriza acesso real.

## Permissões e exceções

HUM-06 separa inventário/leitura, exterior, legado posterior, execução, escrita/publicação, armazenamento, redistribuição e exclusão. Permissão pontual/reutilizável e individual/coletiva respeita autoridade e direitos efetivos; validade, revogação e fiscalização técnica continuam candidatas. Inventário inicial autorizado não é bloqueado pela regra de consulta posterior. Fonte acessível pode não ser armazenável/compartilhável; conservar referência e só derivado legítimo. Exclusão de originais exige aprovação expressa de objeto/revisão.

HUM-03 permite pedir execução local na IDE futura somente por dúvida/pendência/esclarecimento intransponível após investigação autorizada; apresentar propósito, ambiente/dados, comandos e efeitos, oferecer resposta direta e obter permissão específica. Insumos faltantes são pedidos só se necessários. **Nesta consolidação é proibido executar aplicações ou usar essa exceção.** HUM-04 proíbe absolutamente refatoração no onboarding; AX-01 só orienta modificações futuras autorizadas em seu escopo.

## UX candidata e supervisão

Mostrar escopo e revisão; origem/estado de cada afirmação; evidência navegável e contraevidência; áreas não lidas/inacessíveis; dúvidas, impactos, bloqueios e ações possíveis. Engenheiro pode corrigir interpretação e oferecer esclarecimento depois do onboarding; contribuição pertinente retorna aos níveis autorizados com validação e publicação controlada. Não exigir repetir histórico acessível ou carregar todas as pendências em todo ciclo.

Tratar estados vazio, carregando, parcial, obsoleto, conflito, bloqueado, falha e recuperação; permitir entender motivo e dependência afetada. Acionamento de permissão precisa indicar objeto/escopo e alternativa de resposta direta quando pertinente. Layout, acessibilidade detalhada, notificações, limiares e máquina de estados serão refinados em D02-PEN-001/002/004, sem tela aprovada nesta missão.

## Cenário sintético para próximo discovery

Aplicação fictícia Micro-A fornece contrato HTTP usado por Micro-B. Meso-SIG contém ambos como submodules; Macro-WS contém Meso-SIG. Mudança pretendida altera um campo do contrato. Código Micro-A usa feature branch; comportamento esperado de dependência se refere a revisão HOM diferente. Evidência do significado de um campo está ausente e teste documentado é inconclusivo. O cenário é proposta, sem resposta humana nem execução. [AVALIACAO](AVALIACAO.md) organiza o confronto entre evidência suficiente e lacuna insegura; não atribui valor numérico de aceite.
