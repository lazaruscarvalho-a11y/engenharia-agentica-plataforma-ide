# Consolidação P03/P04 — R03

13/11/2026 · Plataforma/IDE corporativa de Engenharia Agêntica · revisão documental para o PR #9, branch `proposta/d02-primeira-entrega-refinamentos`. Base imutável conferida: `0cc6456fbd7613b9a4369d60684d0fe1170a2ed2`. A publicação é comprovada exclusivamente pelo recibo posterior e releitura do commit, não pela existência deste índice.

## Rota de leitura

1. [CONTINUIDADE](CONTINUIDADE.md): objetivo, estado, mapa e próxima ação.
   Consulte também o [ESCOPO-INTEGRADO](ESCOPO-INTEGRADO.md) para os comportamentos e fronteiras das nove frentes PE-01–09.
2. [BASE-P03-HUM](BASE-P03-HUM.md): decisões e limites preservados, DoD corrigido, topologia, escrita, atualidade e retificações.
3. [P04-CONSOLIDADO](P04-CONSOLIDADO.md): doze perguntas, onze manifestações finais, evolução e origem dos aceites.
4. [PENDENCIAS-P01-P09](PENDENCIAS-P01-P09.md): 77 perguntas originais, com saldo e 43 fichas completas dos demais grupos, mais seis pendências D02.
5. [FONTES](FONTES.md), [RASTREABILIDADE](RASTREABILIDADE.md) e [UNIDADES](UNIDADES.json): fontes, destinos e unidades recuperáveis.
6. [AUDITORIA](AUDITORIA.md), [MANIFESTO-R03](MANIFESTO-R03.json) e recibo posterior: alcance e prova da edição.
7. [PROMPT-NOVA-SESSAO](PROMPT-NOVA-SESSAO.md): instrução reutilizável.

Este conjunto é a sobreposição temática R03. Os documentos D02-doc-2, os manifestos D02/R01/R02 e o CADERNO-ED11 conservam suas identidades históricas; seus hashes não certificam esta nova revisão. A R03 não reescreve seus bytes para fazê-los parecer atuais. Entradas de navegação conduzem à sobreposição, e as referências históricas continuam por SHA.

## Produto e escopo

A missão maior é conceber uma Plataforma/IDE corporativa completa para compreender sistemas, organizar conhecimento e apoiar atividades de engenharia com agentes supervisionados. A primeira entrega concentra o Motor de Onboarding e suas bases Micro/Meso, com agentes de ferramentas existentes e sem interface gráfica própria construída nesta entrega. Escolha de stack, formatos, adaptadores, limiares e avaliação ainda exige refinamento.

O Motor produz conhecimento do repositório e estado estudados; a interação posterior decide suficiência para uma pergunta ou ação concreta. O engenheiro indica entradas e decide incluir repositórios sugeridos. O Analista delimita a solução e aprova o refinamento. Atribuir responsabilidade como declarada não prova corroboração. Conhecimento técnico não confirma sozinho uma regra nova de negócio.

Micro é o repositório; Meso é repositório da Sigla/conta com Micro submodules; Macro é workspace Git com Meso submodules. Raiz de instalação e Macro têm funções distintas; sua identidade física segue aberta. A raiz possui catálogo de Siglas e recursos comuns. Workspace de atividade guarda fontes, hipóteses, requisitos, decisões, pendências e vínculos da demanda, inclusive entre Siglas. Conhecimento de Arquitetura como base materializada na primeira entrega e organização transversal de Negócios continuam em investigação.

Fluxo funcional de referência: selecionar fontes/revisões → obter material acessível → investigar amplamente e aprofundar → registrar conhecimento/evidência/limites → conferir cobertura e coerência → entregar Micro/Meso → recuperar contexto pertinente na atividade → incorporar esclarecimentos autorizados e revalidar mudanças. Essa sequência é síntese documental, não algoritmo ou ordem de implementação aprovados. A descoberta de contexto deve ser gradual; iniciar o agente não implica ler todas as camadas.

## Estados e autoridade

P03 conserva vinte questões resolvidas funcionalmente, P03.20/C-P03-07 adiados e P03.22 com direção aceita/desenho postergado. O parecer de fechamento funcional do P04 é preservado: P04.1–5 têm aceites anteriores relatados, sem as mensagens humanas originais nesta recuperação; P04.6 tem suporte em P03. P04.7–12 e as onze manifestações finais têm fontes humanas recuperadas. Isso não exige repetir perguntas respondidas.

As decisões sobre consulta ordinária e circulação legítima reduzem consentimentos repetidos, preservando aceites específicos de escrita, decisões e operações sensíveis. A relação main/PROD e release/HOM é premissa corporativa relatada; não houve inspeção de pipeline, implantação, configuração ou ocorrência do banco. Não se comprovou capacidade produtiva da IDE.

PGC-001 v1.1.3 e CT v1.0.3 permanecem NÃO RATIFICADOS; 49 CA operacionais NOT_RUN. Sem merge, execução de aplicações, mudança de permissões ou publicação de dados corporativos. A conexão tem permissão de push no repositório público; o conjunto remoto contém sínteses autorizadas e exemplos sintéticos. Capturas locais de conversa e caminhos temporários não compõem a publicação.
