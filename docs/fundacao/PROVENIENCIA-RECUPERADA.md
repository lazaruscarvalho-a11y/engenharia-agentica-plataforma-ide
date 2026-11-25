# Proveniência recuperada e escopo das afirmações

30/10/2026. Documento de reconciliação; não é aprovação de requisitos nem escolha de stack. As fontes abaixo são mensagens reais recuperadas, e não normas corporativas verificadas.

## SRC-REC-001 — pedido original do Work recuperado

Chat Codex “Executar ecossistema PM-FUND”, `REF-RESTRITA-a1c097dc46a6`, mensagem `REF-RESTRITA-a444cbdfb04a`. O pedido contém dossiê explícito e instrui a distinção entre fatos relatados, hipóteses, recomendações e decisões. Ele detalha a fonte histórica SRC-001 e é a origem direta verificável da consolidação do Work; não substitui todas as falas anteriores da concepção. O namespace SRC-REC evita colisão com SRC-004 histórico, que identifica a documentação oficial de Projetos no inventário original.

| Afirmação consolidada | Localização no pedido | Documento resultante |
|---|---|---|
| Ferramentas/processos do banco, atores, ambientes e controles | OBJETIVO E LACUNA CRÍTICA (1) | ecossistema-atual.md, BAN-001..018 |
| Plataforma/IDE, agentes, repositórios, reuniões, requisitos, incidentes e supervisão | Mesmo bloco (2) | visao-produto.md, capacidades.md |
| Construção externa real e integração interna posterior | Mesmo bloco (3) | construcao-internalizacao.md |
| Método de sete etapas | Mesmo bloco (4), METODOLOGIA DO USUÁRIO | metodologia-fases.md |
| Dez fases 00–09 | Mesmo bloco (5) | metodologia-fases.md |
| Conversas naturais, fontes, IDs, revisão e continuidade | Mesmo bloco (6) | protocolo-sessoes.md, registro-conhecimento.md |
| Harness exploratório sem efeito normativo | PM-FUND-001 / IMPLEMENTAÇÃO | harness/governanca_assistida |
| Não confundir testes do piloto com os 49 CA | PM-FUND-002 / AUDITORIA INDEPENDENTE | auditorias/fundacao-integral |
| Sem merge, ratificação ou permissões novas | LIMITES DE AUTORIZAÇÃO | pontos de entrada e relatórios |

## SRC-REC-002 — fonte adicional de produto recuperada

Chat ChatGPT “Plataforma AI Nativa”, `REF-RESTRITA-8e47ed8ae95d`. Cinco turnos disponíveis, sem cursor mais antigo. Somente as falas do usuário abaixo são usadas como relatos/intenções. As recomendações do assistente nesse chat NÃO foram promovidas a decisões.

| ID | Mensagem/turno do usuário | Conteúdo recuperado de forma sanitizada | Estado |
|---|---|---|---|
| REC-001 | REF-RESTRITA-66b662b02320 | Plataforma específica para a empresa; repositórios de aplicação/infraestrutura associados a contas AWS; proposta de harness em camadas plataforma→conta/sigla→repositório | Relato e proposta do usuário; hierarquia, herança e acesso a refinar; nomes internos de exemplo não reproduzidos |
| REC-002 | REF-RESTRITA-3725482ec193 | Intenção de cobrir o ciclo desde a história até a criação de GMUD para produção | Intenção explícita; preparar GMUD não autoriza implantação produtiva |
| REC-003 | REF-RESTRITA-9c9cb6316e34 e REF-RESTRITA-3f8f82393f09 | Pedido de avaliação conjunta de Theia AI, OpenSpec, OpenHands SDK, Serena e Temporal | Alternativas em avaliação; nenhuma stack aprovada |
| REC-004 | REF-RESTRITA-5f2001045791 | Uso relatado de ai-memory, context-mode, caveman e rtk; pedido de avaliar integração | Relato e avaliação pendente; identificadores/produtos exatos e contratos ainda a confirmar |

Impactos para discovery: explorar escopo por conta/repositório e conflitos de herança; incluir preparação de GMUD na jornada; comparar executores e ferramentas sem presumir que OpenHands substituiu Devin CLI ou que uma recomendação arquitetural recebeu aceite. Não instalar ferramentas nem acessar contas internas com base nesses relatos.

## Limite residual

A recuperação melhora a rastreabilidade: o dossiê do Work foi localizado e há falas adicionais de produto. Ainda não foi recuperada a transcrição inicial integral de “Reescrita do fluxo de trabalho”. Não alegar cobertura exaustiva de todas as definições originais. Novas diferenças são pendências de reconciliação; não substituir histórico por síntese silenciosa.
