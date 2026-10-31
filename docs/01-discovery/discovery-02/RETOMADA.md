# Discovery 02 — Motor de Compreensão Profunda de Repositórios

Entrada **revisão 2**, D01-R2 v2.0. Discovery 02 preparado, ainda não executado. Não se escolhem tecnologias nem se inicia implementação integral por este documento.

## Localizar a versão

Repositório: `lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide`.
Branch: `proposta/discovery-01-onboarding-agent-first`; PR #6, base PR #5.
Caminho: `docs/01-discovery/discovery-02/RETOMADA.md`.

Recebendo um commit imutável, leia todos os arquivos nesse commit. Para o pacote final, o [recibo R2](../../../auditorias/discovery-01-r2/RECIBO-PUBLICACAO.json) identifica `content_commit`, hashes e escopo. O recibo é posterior ao conteúdo: se não existir no commit fornecido, a referência é de candidato/conteúdo, sem presumir recibo final. O manifesto descreve sua própria revisão, não a R1. Não substituir por `main`, cujo estado observado é apenas inicial.

Leia [índice D01](../discovery-01/README.md), [FONTES](../discovery-01/FONTES.md), [REGISTRO](../discovery-01/REGISTRO.md), [MATRIZ](../discovery-01/MATRIZ.md), [REVISÃO](../discovery-01/REVISAO.md) e [MANIFESTO](../discovery-01/MANIFESTO.json). Expanda para [visão](../../fundacao/visao-produto.md) e [CAP-001..020](../../fundacao/capacidades.md). [RETIFICAÇÕES](../discovery-01/RETIFICACOES.md) preservam IDs e mudanças desde R1.

## Base que não precisa ser rediscutida

| Tema | Definição recuperável no registro canônico |
|---|---|
| Objetivo e estrutura | E01..E05: compreensão ampla/profunda viável, incremental, conhecimento concreto/conciso/hierarquizado para agentes, contexto mínimo suficiente com evidências. Execução local da aplicação cabe exclusivamente ao engenheiro (E03). |
| Camadas e Git | E06..E10: Micro=repositório; Meso=domínio/contexto de sigla/projeto/agrupamento de contas; Macro=workspace/ecossistema. Git canônico, Meso incorpora Micro como Submodules e Macro incorpora Meso como Submodules. Sem sync ou acesso implícito. |
| Ferramentas e colaboração | E08/E11..E15: agnóstico a Devin/Claude/Copilot; compartilhar entre autorizados; consolidação predominantemente automática com controles e escalonamento; pushes de trabalho separados da publicação. Restrição relatada de criar Actions corporativas não aprova motor local nem protege pushes externos. |
| Ambientes | E16..E19: CI/CD e scheduled/GMUD são relatos; main não prova PROD. Composições heterogêneas entre feature branches/HOM/PROD, reprodução controlada e integrações reais somente autorizadas. |
| Fontes externas | E20..E25: compreender interfaces mesmo sem implementação; fontes indiretas, referências preservadas e só derivado legitimamente armazenável/compartilhável. Busca exterior informada e autorizada previamente; modalidades pontual/reutilizável e individual/coletiva, sem ampliar direitos reais. |
| Migração | E26..E33: inventário cuidadoso, transformação e comunicação; exclusão de originais sempre aprovada expressamente; provisório permitido, padrão e utilizável para consultas/código em escopo autorizado. Consulta posterior ao legado para lacuna pede permissão e comunica inconformidade; não confundir com inventário inicial autorizado. Ressalvas permitidas para pendências não críticas; classificação rigorosa com escalonamento se incerta; taxonomia e limiares continuam candidatos. |
| Conhecimento contínuo | E34/E35: pendências estruturadas/rastreáveis disponíveis aos agentes e engenheiros, relevantes a cada leitura/ciclo; esclarecimentos posteriores retroalimentam Micro/Meso/Macro com controles. Sem carregar tudo no contexto ou supor execução em segundo plano. |
| Continuidade e limites | E36: preservar D01 e aprofundar motor em outra sessão. D01-PEN-001 separa reconciliação material das fontes E01..E36 (A) de transcrição original integral não recuperada (B). P-A..P-L e HIP permanecem propostas/hipóteses. |

A fonte adicional é **declaração reproduzida no pedido atual D01-S05**, não recuperação das mensagens originais. O relatório/recibo sustentam o estado final do eixo A; B permanece limitado. Refinamentos técnicos e funcionais não reabrem automaticamente decisões conceituais.

## Investigação proposta

Como explorar um repositório desconhecido, identificar tecnologias e responsabilidades, reconstruir fluxos/regras/contratos/dependências, combinar múltiplos repositórios, selecionar contexto, coordenar agentes especializados, reconhecer lacunas, validar fatos/inferências, estruturar achados, atualizar incrementalmente e medir cobertura/confiabilidade/custo?

Primeira pergunta: **“Ao abrir um sistema desconhecido, o que o engenheiro precisa que a Plataforma consiga explicar e demonstrar com evidências antes de confiar numa alteração?”**

Pode-se usar um serviço e consumidor fictícios, com regra de negócio, evento, dependência e documentação obsoleta. O exemplo é sintético; não há aplicação a executar. Produzir requisitos/experimentos candidatos, riscos e perguntas, sem antecipar parser, modelo, banco, mecanismo vetorial ou framework.

## Autoridade e continuidade

PGC/CT NÃO RATIFICADOS; 49 CA operacionais NOT_RUN. Sem merge, produção, GMUD, hotfix, execução de aplicações, acessos internos, novas pipelines ou mudança de permissões. Decisão de produto não concede autorização operacional. Fontes/Instruções nativas não atualizadas; não presumir memória ou sincronização.

Preserve proveniência, revisão e natureza de cada novo achado. Pendências A históricas, B interpretativas, C funcionais, D técnicas e E corporativas constam da revisão; não exigir todas antes de investigar. Prova por subagente isolado, se executada, é evidência técnica distinta de nova conversa real de usuário. O [relatório R2](../../../auditorias/discovery-01-r2/RELATORIO.md) informa o alcance observado.
