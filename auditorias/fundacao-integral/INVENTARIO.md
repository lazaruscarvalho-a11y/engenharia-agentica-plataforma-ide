# Inventário e estratégia — PM-FUND-001
Data: 30/10/2026. Natureza: proposta de fundação, sem ratificação.

## Leitura remota inicial
Repositório privado lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide. main = ba820cbb7b92bd570e4848c4ca7eff48c44f04cd; só .gitkeep. Cinco branches, quatro PRs abertos.
|PR|Head (SHA)|Base|
|---|---|---|
|1|proposta/importacao-pgc-001-v1.1.2 (4f0450ac996505639d2d34ff79519e00dd8d1aa8)|main|
|2|proposta/revisao-pgc-001-v1.1.3 (2e7cb6019e7412dad8fb06315f624492feaf4fc1)|branch #1|
|3|proposta/incremento-governanca-assistida-001 (50a37b409370bae058b6514dd2d5ba99726c416f)|branch #2|
|4|piloto/governanca-assistida (f2189bf9481a48fb6281844326d35501952ebd0e)|branch #3|

GET árvore recursiva #4: 101 entradas, 77 blobs, truncated=false. Cache local foi comparado ao hash Git de cada blob. ZIPs recuperados em base64 e README da candidata em UTF-8 para corrigir cache, antes da implementação. Manifesto em baseline-remoto.json permite repetir a comparação. SHA local de reconstrução não representa commit publicado: os commits remotos desta missão terão como pai f2189bf… via API.

Permissões declaradas pelo GET: pull/push/triage/maintain/admin=true; isso não substitui autorização. GET proteção main: 403 Resource not accessible by integration. Lista branches informa protected=false. GET rulesets: 403 solicitando plano GitHub Pro. Controles administrativos completos NÃO INSPECIONÁVEIS. Nenhuma proteção/permissão alterada.

## Proveniência e limites
SRC-001: pedido atual do usuário, 30/10/2026, dossiê detalhado e autorização de execução; fonte primária desta missão.
SRC-002: read_thread 6add5e12-021c-83e8-9d16-2a4917ea9700, turnLimit=10, retornou cinco turnos, hasMore=false, nextCursor=null. Mensagem ecf720a8-dc21-4bdf-82e5-9bb590be4f7d limitada a 20000 caracteres pelo serviço. Mensagens 6739f6d0…, 6d528f60… e 2469f322… descrevem lacuna/dinâmica. Não foi recuperada a transcrição original longa anterior a esses turnos; nenhuma recuperação exaustiva alegada.
SRC-003: repositório e objetos remotos nos SHAs acima, comprovados por árvore/hashes, não pelo texto de relatórios anteriores.
SRC-004: documentação oficial https://learn.chatgpt.com/docs/projects consultada e aberta em 30/10/2026. Instruções, Fontes e acesso a arquivos são recursos distintos; sem suposição de sincronização.

## Branch e ordem
Uma branch integrada proposta/fundacao-integral-pm-fund-001-003 parte de #4, preservando a cadeia. PR contra piloto/governanca-assistida exibe só a fundação. Não duplicar importação em PR contra main. Nada será mesclado/ratificado.
1. Inventário e matriz inicial: lacunas em visão/método/discovery/ChatGPT, piloto C1 existente.
2. Produto: cinco arquivos exclusivos docs/fundacao.
3. Método/ChatGPT: três arquivos exclusivos docs/fundacao, docs/chatgpt e INICIO-DISCOVERY.
4. Harness: novos arquivos sob harness/governanca_assistida; preservar protocolo anterior.
5. Coordenador: entradas raiz, matriz, verificadores e publicação.
6. Congelar versão; auditores independentes só então leem, com permissão exclusiva para relatórios/testes adversariais.
7. Corrigir P0/P1, revalidar; preparar pacote e configurar apenas se houver controle permitido.

## Protocolo de tarefas usado
Cada delegação recebeu objetivo, arquivos exclusivos, fontes SRC-001/002/003, limites de autorização, entregáveis, oráculo e limite de duas tentativas antes de alternativa segura/escalonamento. Dependências de escrita foram sequenciadas; nenhum agente publica remoto. Coordenador integra e é único escritor de ref/PR. Auditoria não reutiliza agentes autores para auditar seus próprios arquivos. Trabalho independente continua em caso de falha. Sem processos de execução prometidos após fim desta sessão.

