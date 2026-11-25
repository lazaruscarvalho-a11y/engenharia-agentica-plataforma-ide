# Até onde investigar uma pergunta ou uma alteração?

Uma pergunta sobre a declaração de um método pode terminar no símbolo e na revisão correta. Uma alteração de contrato pode exigir os consumidores, as condições de negócio, as configurações e o tratamento das exceções. A direção adotada é recuperar o mínimo suficiente e ampliar se uma dependência puder mudar a interpretação, a autorização ou a resposta.

<a id="tarefa"></a>
## Definir a tarefa e a composição antes da busca

Identifique a intenção, a etapa e o papel de quem pergunta. Determine repositório, estado local e revisão, Sigla, Solução, Workspace se existir, cliente, capacidade efetiva e acesso. Uma ocorrência em homologação exige evidência adicional da versão implantada e da entrada observada. Uma investigação recuperada pode poupar leituras se seus fundamentos continuarem aplicáveis. Para declarar executada uma mudança, validado seu impacto ou aprovado um teste, são necessários os atos e evidências do candidato atual. F3-P106 estende a política de investigação às atividades, além das perguntas.

Assim, a resposta pode indicar que parte do histórico foi aproveitada, qual contrato foi conferido no estado atual e que ramo ficou pendente. Faça essa distinção no ponto de decisão, antes de recomendar uma mudança. [Exemplo de F3-CA22](05-evidencias-e-memoria.md#reuso).

Fontes da passagem · A06-001–002, F3-P106 · [roteamento-contexto, L5–22](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L5-L22) · [P04-CONSOLIDADO, L27–29](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L29).

<a id="percurso"></a>
## Encontrar, qualificar e compor a evidência

Uma chave, ID ou nome exato permite procurar um alvo sem inferência. Para nomes de símbolos e mensagens de erro, a busca lexical ou estrutural pode ser mais informativa. Para uma paráfrase, a busca semântica propõe candidatos. Metadados, revisão e direitos permitem descartar os que não podem responder à tarefa. Representações numéricas exigem compatibilidade entre modelo de indexação e de consulta. Uma pontuação elevada ainda precisa de confronto com as fontes.

Recupere a passagem e também o parágrafo vizinho que contém a negação ou a condição. Confira o sentido e o tipo de cada aresta, a composição examinada e a origem principal. O recuperador encontra. O compositor escolhe granularidade, ordem, motivo da inclusão, referência que permite aprofundar, lacunas, cobertura e contradições. Uma proposta de pacote contextual em F4 reúne as afirmações e relações qualificadas e registra material inacessível. O exemplo de um pacote para investigar uma dependência externa distingue consulta autorizada de execução, troca de regras ou publicação. Receber o trecho dá contexto para a análise dentro dos direitos existentes.

Fontes da passagem · A06-003–006, U048 · [roteamento-contexto, L9–24](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L9-L24) · [roteamento-contexto, L19–26](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L19-L26).

<a id="alcance"></a>
## Escolher a amplitude segundo a conclusão procurada

| Abrangência ilustrativa de F3 | Pergunta que orienta a expansão |
|---|---|
| Local | Símbolo, função, contrato ou configuração explicam a decisão no repositório ativo? |
| Próxima | Um consumidor, parâmetro ou serviço diretamente relacionado pode inverter a conclusão? |
| Ampliada | Uma política comum, contrato compartilhado ou relação entre componentes da Solução é necessária para explicar a exceção? |
| Transversal | O pedido envolve mais de uma Sigla ou domínio e exige compatibilizar vocabulário, autoridade ou efeitos? |

Uma conclusão transversal pode depender de poucas relações bem sustentadas. Uma conclusão local pode exigir ler a função inteira. A amplitude da investigação, a profundidade de leitura e a granularidade de uma vista de arquitetura respondem a perguntas diferentes. A finalidade e a abrangência da descoberta arquitetural são delimitadas pelo Analista com apoio do agente. A autorização para incluir outro repositório na atividade tem regra própria. [Composição](02-camadas-e-workspaces.md) · [Vistas arquiteturais](09-documentacao-visual.md).

Fontes da passagem · A06-007–011, U047 · [roteamento-contexto, L9–22](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L9-L22) · [roteamento-contexto, L5–24](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L5-L24).

<a id="carregamento"></a>
## Quanto carregar em cada momento

A orientação de não carregar automaticamente documentos das Siglas ao iniciar foi preservada. **L0**, na proposta F4, contém contratos universais mínimos, identidade, segurança e descoberta de capacidades. **L1** situa a atividade, suas revisões, decisões e pendências materiais, inclusive em um pedido avulso. **L2** recupera unidades específicas de Micro, Meso, Solução, Negócios e procedimentos. **L3** permite aprofundar em código, contratos, logs ou documentos completos quando necessários, acessíveis e autorizados. O agente principal conserva uma via de aprofundamento. Uma investigação delegada pode receber só o contexto pertinente à sua pergunta.

Defina tipos de aresta, direção, condições de expansão e retorno. Observar ciclos e ramificação importa mais que prescrever uma quantidade fixa de saltos. Um único nó pode ter centenas de vizinhos. A ilustração de F4-L1333–1344 separa resolução de autorização, recuperação e composição validada. O custo inclui descrições de capacidades e ferramentas, mensagens, resultados e histórico, além dos documentos carregados. No original, F4-L1333–1344 preserva o diagrama integral de autorização, recuperação e composição e F4-L1503–1534 preserva o exemplo de pacote com evidências, lacunas e direitos por operação. Essas coordenadas permitem recuperar ordem, rótulos e limites sem impor o modelo como contrato. Os números ilustrativos de latência local por ID não são prazos para entregar a resposta.

Fontes da passagem · A06-012–016, U049 · [P04-CONSOLIDADO, L49–53](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L49-L53).

<a id="parada"></a>
## Justificar a ampliação ou delimitar o resultado

Por conclusão material, pergunte se a revisão corresponde ao objetivo e se há condições, exceções, dependentes ou contraevidências que possam mudar a resposta. Explique por que a nova fonte é relevante e o que se procuraria nela. A consulta de material já legitimamente acessível, a inclusão de um repositório na atividade e a autorização de execução são atos diferentes. Para a inclusão, o agente sugere e o engenheiro decide no seu alcance.

O orçamento pode considerar fontes, chamadas, custo e tempo do modelo, rede, tokens, profundidade, validações e número de vizinhos. Se ele se esgotar antes da evidência decisiva, mantenha a resposta parcial com a próxima operação que resolveria a dúvida. Distinga *relação investigada e ausente*, *parser sem cobertura* e *acesso indisponível*. No onboarding, uma dúvida persistente sobre a criticidade recebe tratamento próprio. [Estados de conclusão](03-onboarding-e-compreensao.md#conclusao).

Fontes da passagem · A06-017–019 · [REGISTRO-DECISOES, L962–1002](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r04/REGISTRO-DECISOES.md#L962-L1002).

<a id="exemplos"></a>
## Três situações que exigem verificações diferentes

- **Regra de um canal.** A pergunta atual parece uma paráfrase de uma anterior. Verifique o contrato, o canal e o objetivo antes de usar a resposta. Recupere o worker ou a política externa quando puder mudar a conclusão. Se o canal for outro, explicite o limite.
- **Evento condicionado.** No cenário sintético Alfa/Beta, Alfa publica sob certas condições e Beta consulta um serviço externo. É possível explicar a emissão condicionada e a delegação. Decidir a política de elegibilidade exige evidência do outro lado.
- **Relação em uma vista.** A figura orienta a investigação. Confira nomes, revisão, fonte, direção e natureza da ligação. Uma saída local do produtor precisa estar acessível no cliente que a consome. Uma vista legível pode conter uma relação invertida.

Fontes da passagem · A06-020–022 · [BASE-P03-HUM, L66–75](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L66-L75).

<a id="interfaces"></a>
## Que alternativas comparar no piloto

F3 exemplifica as operações de resolver contexto, buscar memória e conhecimento, recuperar e verificar evidência, expandir dependências, conferir validade e propor um registro. F4 exemplifica `knowledge.get_context_pack` com revisão da composição, evidência, lacunas, contradições e rota de aprofundamento. Esses esboços ainda precisam definir precondições, erros, limites de saída, autorização, compatibilidade e custo por cliente e modalidade.

Uma comparação pode partir de Markdown e manifestos com índice lexical SQLite FTS5 e tabela de relações, conforme F4. Para a memória local, F3 propõe testar busca híbrida com sqlite-vec e FastEmbed, tendo LanceDB como alternativa. GraphRAG, LightRAG ou LlamaIndex são hipóteses para comparação com as mesmas perguntas, exceções e evidências esperadas. Meça recuperação, **correção do reúso**, custo inicial de indexação, primeiro resultado útil, tempo total e comportamento em cada modalidade. A escolha de ferramentas continua aberta. [Alternativas e modalidades](10-ferramentas-e-composicoes.md).

Fontes da passagem · A06-023–024 · [roteamento-contexto, L19–26](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/fundacao/roteamento-contexto.md#L19-L26).

[Voltar à entrada de discovery](../README.md)
