# Fontes e proveniência — revisão 2

Missão D01-R2 v2.0. A evidência agora permite reconciliar materialmente E01..E36 sem alegar recuperação técnica da transcrição original completa.

## Fontes e hierarquia

| ID | Fonte e localização | Qualidade e uso | Limite |
|---|---|---|---|
| D01-S01 | Pedido inicial de consolidação desta sessão | Autorização direta de documentação e publicação em branch/PR | Sem merge, ratificação ou permissão corporativa |
| D01-S02 | Conversa “Iniciar discovery funcional”, `REF-RESTRITA-a81df44a5fbe`; cinco turnos finais recuperados na R1 | Mensagens diretas A..E abaixo; decisões DEC-001..004 | Recorte, sem transcrição completa |
| D01-S03 | GitHub privado, snapshot anterior `d9e48c3d36598d40f9d2e38caf836bccb5fac97f`; base da fundação `f8d7c60955a1250ae4d94a428386787f4aaa24b0` | Documentos/manifestos e recibos observados; branch de proposta | Publicação não é vigência nem implantação |
| D01-S04 | Tentativa de navegador na R1 | Observação histórica de redirecionamento para login | Não houve nova inspeção nativa nesta R2 |
| D01-S05 | Arquivo “Texto colado.txt”, Prompt-Master D01-R2 v2.0, fornecido pelo usuário nesta sessão | **DECLARAÇÃO REPRODUZIDA NO PEDIDO ATUAL**; E01..E36 sustentam reconciliação material e retificação das decisões declaradas | Não é prova de que as mensagens humanas originais anteriores foram tecnicamente recuperadas |
| D01-S06 | Nova leitura da conversa por read_thread na R2, turnLimit=10, 20.000 caracteres/item | Cinco turnos finais atuais; página sem cursor e sem mais páginas; contém E36 original e pedidos de revisão | Respostas extensas truncadas; não recuperou início do discovery nem amplia a prova de decisões a partir de textos do assistente |

O arquivo original D01-S05 tem **50.831 bytes** e SHA-256 `e611884b12ddcbfc2378674e124de5543ffc78eb8dff2a3700675bb379805a35`. O [recorte arquivado](../../../auditorias/discovery-01-r2/DOSSIE-REPRODUZIDO.md) preserva o conteúdo literal de E01..E36 e P-A..P-L em UTF-8/LF, com âncoras de navegação acrescentadas, com metadados. Esse acervo é evidência reproduzida, não um segundo registro canônico. E01 etc. são âncoras do pedido, nunca IDs de mensagens.

Classes de evidência: direta recuperada; declaração reproduzida; relato documental anterior; proposta/recomendação; hipótese/inferência. A classe da evidência difere da natureza do conteúdo: uma decisão declarada no dossiê tem natureza DECISÃO, com proveniência REPRODUZIDA; não precisa continuar “mero relato” porque o mecanismo técnico não recuperou a mensagem original. Detalhes acrescentados depois da concordância permanecem propostas.

## Mensagens diretas já disponíveis na R1

| Referência | Mensagem/turno humano | Resposta do assistente | Alcance |
|---|---|---|---|
| D01-S02-A | `REF-RESTRITA-12ba0dca3eaa` | `REF-RESTRITA-c608dfe3ed96` | Permissão e comunicação de inconformidade na consulta posterior ao legado; E31 |
| D01-S02-B | `REF-RESTRITA-18066fc64e8b` | `REF-RESTRITA-dae7a0b51427` | “Permitir”, à pergunta em A sobre conclusão com pendências não críticas; E32 |
| D01-S02-C | `REF-RESTRITA-ae0800f9d64f` | `REF-RESTRITA-32b70c7394e6` | “Sim”, à pergunta em B sobre classificação objetiva com recurso ao engenheiro se incerta; E33 |
| D01-S02-D | `REF-RESTRITA-f337fbd03299` | `REF-RESTRITA-37892cb1c25d` | Concordância com direção e pergunta sobre nova sessão; E36 |
| D01-S02-E | `REF-RESTRITA-adfede88d695` | `REF-RESTRITA-073cf1482125` | Pedido de consolidação; encaminhamento do assistente não é prova de persistência |

[Conversa](chatgpt-conversation://REF-RESTRITA-a81df44a5fbe). D01-S06 retornou exatamente os turnos `REF-RESTRITA-8d5dc4d64b9f`, `REF-RESTRITA-0bdbdf2b55f1`, `REF-RESTRITA-1005957b30da`, `REF-RESTRITA-6f97bbec116a` e `REF-RESTRITA-adfede88d695`. As respostas extensas de elaboração dos prompts estão truncadas. Conteúdo do assistente, mesmo quando diz ter visto o histórico, não é manifestação humana original. O arquivo bruto de consulta permanece local; o dossiê autorizado fornece a fonte reproduzida completa desta revisão.

## Snapshot consultado e integridade

Foram relidos pelo SHA anterior: AGENTS, ESTADO-ATUAL, RETOMADA, manifesto de Fontes, INICIO-DISCOVERY, os sete documentos D01, entrada D02, recibo R1, visão, CAP-001..020, metodologia, protocolo, roteamento e proveniência. A análise de segurança/publicação/contexto usa CT-003/005/007 candidatos da fundação; PGC v1.1.3 e CT v1.0.3 NÃO RATIFICADOS. Manifestos e recibos anteriores são preservados e conferidos em seus commits, não reescritos.

PR #6 confirmado aberto/draft, base `proposta/fundacao-integral-pm-fund-001-003`, HEAD inicial R2 `d9e48c3d36598d40f9d2e38caf836bccb5fac97f`, sem alterações posteriores nessa observação. Main `ba820cbb7b92bd570e4848c4ca7eff48c44f04cd`, somente marcador inicial. A revisão publicada e hashes desta R2 ficam no recibo novo, separado do recibo R1.

## Eixos de D01-PEN-001

**A — Reconciliação material:** verificar individualmente todas as âncoras acessíveis, classificações, propostas, retificações e consistência; concluir somente após publicação e verificação.

**B — Recuperação histórica integral:** continua não comprovada. O dossiê pode encerrar A no escopo E01..E36 sem encerrar B. Ausência de algoritmo, formato ou refinamento futuro não constitui lacuna histórica.

Não se inventam IDs, horários de aprovação, identidade corporativa, acesso ou assinatura. As Fontes e Instruções do Projeto não foram atualizadas. A referência versionada é GitHub por commit; memória entre chats e sincronização automática não são presumidas.

[Histórico FONTES R1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/ceedbc1f0fcb4133ce8109ec889676dca966193d/docs/01-discovery/discovery-01/FONTES.md).
