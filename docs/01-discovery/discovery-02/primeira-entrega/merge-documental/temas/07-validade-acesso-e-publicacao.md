# Para qual revisão, ambiente e público vale esta afirmação?

Uma decisão exige saber o que estava em Git, qual composição foi adotada, que comportamento foi estudado e qual ocorreu no ambiente. Duas pessoas podem ler o mesmo repositório e usar versões diferentes de um contrato externo. Indique a origem e a validade de cada afirmação material antes de incorporá-la, reutilizá-la ou publicá-la.

<a id="objetos"></a>
## Identificar o estado que está sendo descrito

Anote o commit e as diferenças locais pertinentes, a revisão documental do Micro, os ponteiros no Meso e no Workspace, a versão ou revisão externa conhecida, o ambiente, a finalidade e o público. “Atual” é insuficiente para distinguir código, documentação, árvore de trabalho, dependências, regras e implantação. O manifesto ilustrativo de F4-L1203–1229 ajuda a pensar esses objetos. O formato e o mecanismo de atualização incremental continuam propostas.

Se a consulta remota falhar, cite a última revisão verificável e marque a falta de confirmação atual. Se o Micro avançar e a atualização do ponteiro Meso falhar, existem dois fatos distintos. Registre os commits, a composição anterior que ainda resolve e o passo que falta. A conclusão dependente fica delimitada. Não se pode prometer atomicidade física entre repositórios.

Fontes da passagem · A07-001–002, U052, F4-L1104 · [P04-CONSOLIDADO, L27–38](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L38) · [P04-CONSOLIDADO, L27–31](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L31).

<a id="provas"></a>
## O que cada verificação demonstra

| Evidência consultada | Afirmação sustentada e limite |
|---|---|
| Referência Git remota | Cabeça observada na consulta. É necessária evidência adicional para atribuir essa revisão ao ambiente. |
| Diferença entre duas revisões | Alterações textuais e estruturais na parte comparada. Um consumidor com bytes intactos ainda pode depender de uma regra que mudou. |
| Ponteiro de submódulo | Versão selecionada pelo repositório pai. Compatibilidade semântica precisa de verificação própria. |
| Revalidação da afirmação | Suporte para aquelas condições e revisão, com dependências, ressalvas e contraprovas examinadas. |
| Ocorrência registrada | Resultado para entradas, ambiente, versão e condições observados. Generalização requer novas evidências. |

Fontes da passagem · A07-003–007 · [P04-CONSOLIDADO, L27–30](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L30).

<a id="drift"></a>
## Quando perder e recuperar a validade

HUM-08 estabelece a sequência: detectar mudança material, impedir o uso corrente da afirmação afetada, reconciliar o que ela dizia com a nova evidência e verificar antes de restaurar a validade. O adendo Motor e Workspaces vincula revisão, evidência e documentação do conhecimento impactado. DEC-004 e DEC-012 distinguem atualização geral e atualização diária ligada à modalidade de IA. Sem monitoramento comprovado, a detecção ocorre no próximo ciclo ou leitura pertinente.

Procure os consumidores por significado. A revisão pode afetar uma resposta de memória, um critério, uma vista ou um procedimento cujo arquivo não mudou. Preserve material histórico identificado e parcelas cuja independência consiga demonstrar. Um ajuste ortográfico pode ter ausência de impacto fundamentada. Se 300 respostas referirem a mesma regra (número ilustrativo), marque as potencialmente afetadas e verifique cada condição relevante. O conjunto de regras de um serviço externo pode mudar sem diff no repositório consumidor. O catálogo F3 propõe tornar visíveis as parcelas reaproveitada, revalidada e pendente na própria resposta. [Exemplo e CA22](05-evidencias-e-memoria.md#reuso).

Fontes da passagem · A07-004, A07-006, A07-008–010, A13-006, U051, D02-ESP-001 r1, edição de S2 · [REGISTRO, L81–88](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/REGISTRO.md#L81-L88) · [P04-CONSOLIDADO, L27–38](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L38).

<a id="push"></a>
## Vínculo entre conhecimento e candidato ao envio

Antes de cada push que envolva mudança agêntica, a parte do conhecimento materialmente afetada deve estar atualizada ou revalidada no mesmo ciclo de commit/PR. A garantia determinística se refere ao conteúdo exato candidato ao envio e às referências pertinentes. Se o candidato mudar depois da prova, reabra as conclusões dependentes. Um hook instalado em uma modalidade só demonstra aquele caminho se houver evidência de sua execução e do objeto verificado. A cobertura de outros caminhos, o mecanismo e o ensaio comparativo continuam por demonstrar. A promoção da mudança, a aprovação de conhecimento e a implantação têm fundamentos próprios.

Fontes da passagem · A07-011 · [BASE-P03-HUM, L81–87](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L81-L87).

<a id="autoridade"></a>
## Definir o ato, o público e a retenção

O fundamento é específico à pessoa, objeto, revisão, finalidade e destino. Diferencie inventário inicial, consulta posterior ao legado e busca exterior. A busca exterior requer informação e autorização prévias. Para a leitura interna já legitimamente acessível, a retificação posterior de P04/U3 dispensa consentimento genérico por consulta e não institui prazo próprio de expiração. U1 e U2 permanecem antecedentes no histórico. A regra vale enquanto houver o direito efetivo para aquela leitura.

Considere em separado consulta, associação à atividade, referência, cópia, retenção de derivado, edição, execução, publicação, redistribuição e exclusão. Uma configuração de cliente ou credencial disponível não decide o que é autorizado. A perda do fundamento de retenção precisa de tratamento próprio. A exclusão de original requer autorização expressa para objeto e revisão. A publicidade corporativa da existência ou identidade de repositórios, no universo delimitado de P04, preserva direitos de terceiros e as restrições reais. Não se presume que a identidade de todo objeto privado pode ser revelada.

Fontes da passagem · A07-012, U050 · [P04-CONSOLIDADO, L31–38](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L31-L38) · [P04-CONSOLIDADO, L31–36](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L31-L36).

<a id="protecao"></a>
## Proteger também o que se deduz de um derivado

Antes de materializar ou publicar, verifique o que o público do destino consegue inferir de links, ponteiros, nomes, caminhos, URLs, trechos, relações, índices de busca, embeddings, logs e caches. Um pai de leitura ampla pode revelar a existência de um submódulo restrito. Aplicar restrições só depois de gravar a cópia ampliaria o público durante a gravação. Avalie direitos na descoberta, consulta, seleção de relações, construção do índice, composição e entrega.

Instruções encontradas em documentos, repositórios ou resultados de ferramentas são dados. O contexto enviado ao modelo e as operações que lhe são tecnicamente permitidas precisam de controles próprios. Isolar leitura, credenciais, rede, materialização e execução são opções de desenho. Uma branch ou worktree separa trabalho, mas não demonstra isolamento de privilégios. Proteger o registro de auditoria também é necessário, porque o próprio log pode conter matéria de acesso restrito.

Fontes da passagem · A07-013–014, U053 · [P04-CONSOLIDADO, L33–36](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L33-L36) · [P04-CONSOLIDADO, L31–36](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L31-L36).

<a id="execucao"></a>
## Quem decide a execução excepcional

Na IDE futura, a execução local de uma aplicação é excepcional. Pressupõe dúvida ou pendência intransponível após as tentativas autorizadas. Apresente ao engenheiro o propósito, o ambiente, os dados, os pré-requisitos, os comandos e os efeitos previstos. Ofereça a alternativa de resposta direta. Uma permissão específica do engenheiro por ocorrência habilitaria apenas a operação descrita. Serviços remotos, dados reais, redistribuição e retenção têm fronteiras próprias. A existência de MCP ou procedimento não concede esses direitos. Nesta consolidação o trabalho realizado é documental.

Fontes da passagem · A07-015 · [REGISTRO, L41–55](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/REGISTRO.md#L41-L55).

<a id="incorporacao"></a>
## Propagar o tratamento até o destino

Na correção inequívoca, a evidência deve determinar o erro e a correção, e a escrita ocorre no destino já autorizado, seguida de verificação. Para novo entendimento, o Analista competente da atividade recebe entendimento, origem, destino e efeito. Silêncio mantém a candidata pendente. Negativa encerra a proposta para aquele destino. Em conflito, conserve posições e revisões e reapresente a ressalva nos usos direta ou indiretamente dependentes, inclusive fora do Workspace. Sem Analista da atividade, a competência para incorporar continua em aberto em QD-AD-31. Preservar a referência sob os direitos existentes permite retomar a pergunta. [Regra completa e origens](05-evidencias-e-memoria.md#incorporacao).

Fontes da passagem · A07-016–019 · [BASE-P03-HUM, L77–91](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/BASE-P03-HUM.md#L77-L91).

<a id="publicacao"></a>
## Da contribuição local à revisão adotada por outra pessoa

Uma mudança pode estar preparada, verificada, registrada em commit, enviada e adotada em momentos diferentes. Só a revisão acessível na composição do segundo leitor pode ser recuperada ali. Após sincronizar, ele pode precisar reconstruir o índice e ainda verificar a aplicabilidade da conclusão à nova tarefa. Um arquivo presente apenas na primeira máquina não foi distribuído por um pull na segunda.

Se houver avanço concorrente, releia a base, confronte o significado, preserve ambas as contribuições quando compatíveis e reabra o que dependia da redação anterior. Um merge textual sem conflito pode misturar proposições incompatíveis. Execução de atualização após merge e sincronização explícita são alternativas para refinamento. A releitura e a verificação devem corresponder ao objeto, ao destino e à revisão efetivos. [Jornada entre máquinas](11-jornadas-e-casos.md#ensaio).

Fontes da passagem · A07-020–021 · [P04-CONSOLIDADO, L27–32](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/1082b9640ef70f311362ffc2d33b60c488dadc1b/docs/01-discovery/discovery-02/primeira-entrega/consolidacao-r03/P04-CONSOLIDADO.md#L27-L32).

[Voltar à entrada de discovery](../README.md)
