# Blueprint de arquitetura — síntese substituta rastreável, revisão 1

ORIGINAL_INACESSIVEL: o blueprint histórico integral e o R3 literal não foram recuperados. Esta síntese integra o dossiê curado PM-D02-CONSOL-001 R5 e o D01-R2. Não é original integral certificado. [Origem e lacunas](auditorias/discovery-02-incorporacao/BLUEPRINT-ORIGEM.md).

**Plataforma/IDE pretendida, ainda em discovery.** Nenhuma implementação da IDE ou aplicação foi executada nesta consolidação. PGC/CT candidatos NÃO RATIFICADOS; 49 CA operacionais NOT_RUN. Stack, layout, algoritmo, métricas e normas não aprovados.

## Arquitetura de conhecimento e responsabilidade

O [ledger D02](docs/01-discovery/discovery-02/REGISTRO.md), HUM-01..HUM-11 revisão 1, é dono das unidades, natureza, origem, validade, propostas e pendências. [AX-01..AX-10](docs/fundacao/axiomas-arquiteturais.md) revisão 1 definem a direção temática; este blueprint só integra as referências. [Modelo funcional](docs/01-discovery/discovery-02/MODELO-FUNCIONAL.md), [contratos](docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md) e [avaliação](docs/01-discovery/discovery-02/AVALIACAO.md) detalham propostas D02-PROP-001..007, sem aprovação humana retroativa.

HUM-05: Macro é workspace Git com Meso como submodules; cada Meso é repositório específico por sigla/conta e contém Micro como submodules; Micro é repositório individual. Git é canônico. Não há acesso, redistribuição ou sincronização herdados. Pendências D01-PEN-002/003 e D02-PEN-003 refinam relações, clonagem e ponteiros sem reabrir a topologia escolhida.

## Fluxo cognitivo pretendido

HUM-01/02 e AX-09 orientam investigar, formular hipóteses, planejar, agir somente quando autorizado, verificar e reconciliar. A compreensão precisa explicar responsabilidades, fluxos, contratos, regras e riscos por evidência exata, declarando escopo e contraevidência. As fronteiras de dados, autoridade, execução e intervenção são parte do desenho. Conhecimento insuficiente não é resolvido por confiança verbal do modelo.

HUM-03/04: nenhuma refatoração no onboarding. Execução local é exceção futura restrita a dúvida intransponível, tentativas autorizadas esgotadas e permissão específica, com resposta direta como alternativa; é proibida nesta missão. HUM-06 distingue inventário inicial, legado posterior, exterior, execução, escrita, armazenamento, redistribuição e exclusão. Uso provisório Agent-First mantém originais e controles.

HUM-08 exige atualização/revalidação no mesmo ciclo commit/PR e drift em detectar → invalidar → reconciliar → verificar. Sem monitor implementado, detecção ocorre na próxima leitura/ciclo executado. Multirrepositório tem transação lógica de commits/ponteiros, sem atomicidade física prometida.

## Consolidação, incerteza e continuidade

HUM-09 mantém colaboração entre autorizados e separação de push de trabalho/publicação canônica. Pendências relevantes reaparecem em cada leitura/ciclo por roteamento. P-A..P-L herdadas continuam propostas; o [inventário bidirecional](docs/01-discovery/discovery-02/MATRIZ.md) discrimina donos e projeções. A [retificação D02](docs/01-discovery/discovery-02/RETIFICACOES.md) resolve leitura antiga de execução exclusiva e Meso genérico sem apagar D01.

O produto completo inclui UX, permissões, estados, exceções, segurança, evidências e operação, sujeitos a discovery. Não há seleção antecipada de stack ou MVP. D01-PEN-001/A permanece reconciliado no escopo R2 e B permanece original integral não recuperado. A próxima entrada é [RETOMADA D02](docs/01-discovery/discovery-02/RETOMADA.md), com questão fundada em D01-PEN-007/005/010.
