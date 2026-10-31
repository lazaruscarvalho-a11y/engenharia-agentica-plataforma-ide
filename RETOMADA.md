# Entrada vigente — Discovery 02, consolidação R5

Consulte o HEAD remoto de `proposta/discovery-02-consolidacao` e leia por SHA imutável. Base conhecida `e37af725a162c577cfa9ffde286d0fcf69294429`; candidato preparatório sem publicação comprovada neste texto. [Estado vigente](ESTADO-ATUAL.md) → [RETOMADA D02](docs/01-discovery/discovery-02/RETOMADA.md) → [retificações](docs/01-discovery/discovery-02/RETIFICACOES.md). Manifesto D02 no caminho `docs/01-discovery/discovery-02/MANIFESTO.json`; recibos posteriores em `auditorias/discovery-02-incorporacao/`. Conteúdo e prova posterior são revisões distintas; não retomar de main ou da rota histórica abaixo.

Leia HUM-01..11 e AX-01..10, estados e limites. Meso é repo específico por sigla/conta com Micro submodules; Macro workspace Git contém Meso submodules; sem sync/acesso/redistribuição implícitos. Execução local é exceção futura condicionada, proibida nesta missão; nenhuma refatoração no onboarding. Mesmo ciclo commit/PR e drift detectar→invalidar→reconciliar→verificar. PGC/CT NÃO RATIFICADOS; 49 CA NOT_RUN. RN não é ensaio de subagente.

## HISTÓRICO preservado — retomada da fundação, não entrada atual

O restante identifica o snapshot anterior. Aplicar a rota D02 acima e suas retificações antes de expandir fontes herdadas; seus hashes antigos não provam o conteúdo D02.

# Retomada do discovery

Entrada operacional da proposta `proposta/fundacao-integral-pm-fund-001-003`. Consulte o HEAD pelo GitHub e leia os arquivos pelo SHA retornado. `main` contém apenas a base mínima; não usá-la para recuperar a fundação. Merge e ratificação não são necessários para discovery exploratório.

1. Leia [ESTADO-ATUAL](ESTADO-ATUAL.md), [manifesto de continuidade](docs/continuidade/MANIFESTO.json) e o registro indicado nele. Confira IDs, revisões, fontes e hashes. Manifesto não concede autorização.
2. Leia [visão](docs/fundacao/visao-produto.md), [capacidades](docs/fundacao/capacidades.md), [fontes recuperadas](docs/fundacao/PROVENIENCIA-RECUPERADA.md) e [roteiro](docs/01-discovery/INICIO-DISCOVERY.md) conforme a tarefa.
3. Para retomar o discovery, pergunte sobre o ponto de maior espera/retrabalho em uma demanda fictícia/anonimizada. A entrevista anterior só chegou à primeira pergunta; não invente respostas ou requisitos.
4. Ao obter conhecimento relevante, prepare registro com fonte, ID, revisão e natureza. Sugestões permanecem propostas. Escrita autorizada em branch deve ser reobtida por commit imutável; então publique recibo separado. O piloto C1 histórico conserva aceite específico e não é automaticamente aplicável a novos registros.

## Estado e limites

PGC-001 v1.1.3/CT v1.0.3 NÃO RATIFICADOS; 49 CA operacionais NOT_RUN. Harness local/sintético e CI exploratória não são a IDE final, a conformidade integral do PGC ou uma autorização produtiva. As Fontes nativas são snapshots; a revisão atual do GitHub prevalece como referência de versão da proposta.

O Projeto alvo identificado é `g-p-6ae4fdf0eb688191bb6536420421ef69`, “Plataforma/IDE — Engenharia Agêntica.”. Sua existência e a conversa de discovery foram recuperadas; o campo nativo de Instruções e bytes de Fontes não foram inspecionados. O navegador disponível pede login. A recuperação direta pelo GitHub é a rota operacional verificável enquanto esse acesso não estiver disponível.

## Verificação reproduzível

`python -B harness/verificar_retomada.py --manifesto docs/continuidade/MANIFESTO.json`

`python -B harness/executar_verificacoes.py --saida PASTA_NOVA`

O primeiro comando verifica bytes e identidade localmente. O operador deve conferir o commit remoto consultado. O segundo executa testes/checks exploratórios e mantém os CA NOT_RUN separados.
