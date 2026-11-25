# Integrações e harness por cliente e modalidade

A base comum da primeira entrega precisa permitir que o engenheiro trabalhe pelo cliente que usa. A R04 aceita adaptações explícitas e descoberta progressiva. O catálogo do motor (F1) detalha como testar, por operação, se uma adaptação preservou resultado, significado e possibilidade de retomada. Os novos contratos, estados de compatibilidade e implementações descritos a seguir são propostas. [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-011](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-011) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035).

<a id="abertura"></a>

<a id="a04-001"></a>

A primeira entrega contempla Devin Web, Devin CLI, Devin Desktop e Claude Code. GitHub Copilot é uma possibilidade futura. A direção humana é aproveitar especializações e preservar performance, eficiência, qualidade, profundidade e precisão, com a maior independência possível de fornecedores e tecnologias. Para especificar o que deve ser preservado, F1 propõe seis dimensões de agnosticidade: cliente, modelo, ferramenta de análise, tecnologia do repositório, Sigla ou domínio e ambiente de execução. Continua aberta a evidência suficiente para demonstrar a preservação em cada condição. Não há margem de perda aprovada nem comprovação universal de efeito nulo. [Origem A04-001](#origem-a04-001).

<a id="entrada"></a>
## Como o engenheiro inicia o cliente e este descobre os recursos da plataforma

<a id="a04-002"></a>

Na jornada de referência, o engenheiro obtém a raiz autorizada em Git, abre um terminal na área de trabalho e inicia `devin` ou `claude` conforme a modalidade e a permissão. Pede um onboarding, abre uma atividade ou formula uma pergunta. O cliente lê as instruções que suporta e pode descobrir CLIs, servidores MCP e motores da plataforma. Evidências e marcos de decisão vão aos destinos autorizados. Outra sessão pode ler o estado versionado sem depender da transferência do histórico privado. A decisão R04-DEC-003 reúne raiz comum, instalação local e estrutura Macro na mesma distribuição Git. O exemplo de pastas `.claude/`, `.devin/`, `contracts/`, `adapters/` e `workspaces/` ilustra a organização local possível. A distribuição comum não exige reunir todos os repositórios no mesmo remoto e deixa em aberto a disposição física exata das pastas. A identidade física entre o repositório de Workspaces e o Meso também continua em aberto. A instalação da raiz Git, o papel do Meso e a composição de uma atividade têm consequências diferentes para acesso e retomada. [Camadas e workspaces](02-camadas-e-workspaces.md). [Origem A04-002](#origem-a04-002).

<a id="a04-003"></a>

O agente interpreta a tarefa e usa ferramentas no próprio ambiente de execução. A plataforma responde pelos contratos, conhecimento, operações e controles que efetivamente implementar. O adaptador expõe essas capacidades segundo as convenções do cliente e da modalidade. Git, AWS e serviços corporativos conservam seus controles de acesso. Uma pasta reconhecida por um cliente ou um servidor MCP configurado não garante que toda ação passará por aquela interface. A síntese autorizada da experiência corporativa situa a investigação por operação. Aferir hoje o acesso exige os profissionais e o ambiente correspondentes. [Referência funcional de Devin](../../evidencias/DEVIN-FERRAMENTAS.md). [Origem A04-003](#origem-a04-003).

<a id="contrato"></a>
## Três perguntas para integrar uma capacidade

<a id="a04-004"></a>

1. **É possível executar a operação correta?** Conferir identidade, parâmetros, revisão, ambiente, pré-requisitos, acesso, efeitos e estado. Um job aceito não é um índice pronto. [Origem A04-004](#origem-a04-004).
<a id="a04-005"></a>

2. **O que o resultado significa?** Identificar tipo, unidade, filtro, transformação, convenção de posição e omissões. Uma resposta vazia de análise concluída, um retorno truncado, uma operação sem suporte e uma falha de parser exigem tratamentos diferentes. [Origem A04-005](#origem-a04-005).
<a id="a04-006"></a>

3. **Que conclusão ele sustenta?** Conservar fonte, revisão, cobertura, condições de uso e acesso ao material especializado. Um caminho válido no servidor pode não estar acessível pelo cliente; uma chamada de transporte bem-sucedida não resolve esse problema. Se o agente só obtiver metadados, o relatório se limita a identificar o artefato. A afirmação de que ele contém uma evidência permanece pendente até o leitor autorizado abrir a versão correta. [Origem A04-006](#origem-a04-006).

<a id="a04-007"></a>

O modelo proposto separa núcleo do motor, adaptadores de ferramentas, adaptadores de clientes, registro de capacidades, gestão de artefatos e avaliação/observabilidade. A separação é lógica. O adaptador traduz parâmetros, respostas, falhas e artefatos de cada especialista; o de cliente traduz operações para instruções, skills, hooks e permissões que aquele cliente efetivamente possui. O registro orienta a seleção e a avaliação identifica o que foi demonstrado. Extensões especializadas continuam possíveis quando seu significado e seus efeitos são explícitos. [Origem A04-007](#origem-a04-007).

<a id="a04-008"></a>

O contrato candidato cobre identidade e revisão, aplicabilidade, entradas, pré-requisitos, autoridade e efeitos, saídas, transformações, ciclo de vida, falhas, verificação e evolução. Precisa explicar, por exemplo, quem poderá ler um arquivo gerado remotamente, até quando e com quais direitos. Formatos de intercâmbio, campos obrigatórios e nomes de operações permanecem abertos. Para trocar de cliente, preservar intenção, evidência, efeito e resultado. Arquivos de configuração podem ser diferentes quando cumprem a mesma obrigação nas condições verificadas. [Origem A04-008](#origem-a04-008).

<a id="mecanismos"></a>
## O alcance de instruções, skills, scripts e hooks

| Mecanismo | Para que serve e qual limite precisa aparecer |
|---|---|
| <a id="a04-009"></a> Instruções e roteamento | `AGENTS.md`, `CLAUDE.md` e equivalentes podem apontar contratos e orientar o trabalho. `AGENTES.MD` e `PENDENCIAS.MD` são nomes futuros propostos. O roteamento candidato considera autoridade, papel, etapa, contexto Micro/Meso e do Workspace, recursos efetivos, versões e conflitos. A precedência formal entre orientações permanece aberta; instruções locais não podem ampliar autoridade. F1 descreve suporte do Claude a `AGENTS.md` condicionado a versão, configuração e precedência; a convenção precisa ser verificada na modalidade usada. [Origem A04-009](#origem-a04-009). |
| <a id="a04-010"></a> Skills | Agrupam procedimentos e referências, com carregamento progressivo. O campo experimental `allowed-tools` depende do cliente. No Devin estudado, a lista pré-aprova as ferramentas indicadas e não proíbe automaticamente as demais. A skill pode orientar a preservação da aplicação no onboarding. Uma barreira à escrita depende do controle real disponível no ambiente. [Origem A04-010](#origem-a04-010). |
| <a id="a04-011"></a> API, CLI, MCP e scripts | Expõem operações, consultam índices e transformam artefatos. Verificar revisões, extensões, efeitos, erros e permissões. No estudo visual, editar, validar e gerar pela CLI é o percurso inicial proposto. O MCP pode acrescentar consulta ao modelo quando houver benefício. Devin documenta transportes STDIO, SSE e HTTP; validar acesso às entradas e saídas no ambiente escolhido. [Origem A04-011](#origem-a04-011). |
| <a id="a04-012"></a> Hooks | Conferir momento, evento, cobertura, parâmetros e comportamento no erro. Em `PreToolUse`, `updatedInput` no Claude substitui o objeto completo; Devin documenta mesclagem. O adaptador precisa preservar os campos que deveriam permanecer. No Claude Code, em `PostToolUse`, mudar a saída vista pelo modelo não reverte o efeito já executado. Devin documenta diferenças por modalidade e a ausência de `SessionEnd` em cloud. [Origem A04-012](#origem-a04-012). |
| <a id="a04-013"></a> Política e validação | O motor de autorização controla os percursos que passam por ele; o validador examina integridade e entregas observáveis. Um prompt pode orientar uma ação sem impedi-la tecnicamente, e um hook posterior não comprova prevenção. O subagente precisa de contrato próprio e de um subconjunto autorizado; herança de histórico, permissões, MCPs, hooks e skills exige comprovação. [Origem A04-013](#origem-a04-013). |

<a id="artefatos"></a>
## Exemplo de integração com arquivos e modos de execução

<a id="a04-014"></a>

No projeto **FSoft-AI4Code/CodeWiki** estudado, `codewiki generate` trabalha no diretório corrente na CLI, com opções de provedor, modelo, filtros, foco e destino. No modo MCP, o cliente fornece o raciocínio e o servidor oferece análise, leitura, organização de módulos e escrita. Resultados extensos vão para `.codewiki/sessions` e retornam por caminho; fechar a sessão remove a área temporária. É preciso verificar visibilidade no cliente e acesso autorizado antes da limpeza. A unidade de atualização incremental muda de componente na CLI para módulo no MCP. A demonstração a preparar identifica a instalação, o modo e o consumidor do artefato. O breve uso relatado em F1 não teve identificação suficiente para vincular a instalação ao projeto aberto. [Origem A04-014](#origem-a04-014).

<a id="a04-015"></a>

Entre os produtos documentados estão `overview.md`, páginas de módulos, `module_tree.json`, `first_module_tree.json`, `metadata.json`, `update_record.json`, índice de artefatos, grafos e visualização opcional conforme o modo e as opções. Uma interface comum deve conservar o detalhe nativo útil ou uma referência legitimamente acessível, indicando transformação, cobertura e expiração. O relato de uso do CodeWiki e o interesse no resultado não instituem ferramenta obrigatória. O estudo de documentação visual tem um uso próprio para esses insumos; a documentação pode sustentar uma visão mesmo sem uma nova execução completa. [Origem A04-015](#origem-a04-015).

<a id="compatibilidade"></a>
## Como reconhecer uma combinação utilizável

<a id="a04-016"></a>

A unidade de comparação proposta especifica cliente, modalidade, modelo quando observável, versões, ferramenta, adaptador, operação, configuração, ambiente, recorte de repositório e evidência. A matriz deve examinar carregamento, regras por diretório, subagentes, concorrência, permissões, isolamento, acesso ao sistema de arquivos e rede, custo, observabilidade e retomada. Devin Web e Desktop não herdam automaticamente a raiz, o shell ou os hooks de CLI; subagentes de Claude e Agent Teams têm condições próprias. Uma identidade interna que o fornecedor não expõe permanece desconhecida. [Origem A04-016](#origem-a04-016).

<a id="a04-017"></a>

Os estados candidatos são **documentado, adaptado, demonstrado no recorte, limitado, não avaliado e incompatível no recorte**. Um recurso pode estar documentado e limitado, ou demonstrado para uma operação e não avaliado para outra. A conformidade entre clientes pode ser examinada com o mesmo pedido, base e permissões, comparando efeitos, autoridade, interpretação de conflitos e qualidade do resultado. A sequência de ferramentas e a redação da resposta podem diferir. A habilitação de uma operação com restrição obrigatória depende de uma forma efetiva de atendê-la. **ONB-PEN-05..09** e **Q09** mantêm em aberto contrato, compatibilidade por modalidade, composição mínima, conservação de artefatos e conciliação do harness. Como teste de portabilidade, F1-P156 propõe que outro agente autorizado recupere a etapa, a revisão da fonte e o resultado pela informação compartilhada. Abrir um segundo cliente com as mesmas instruções testa a inicialização. A retomada exige que ele reconstrua o trabalho sem depender exclusivamente do histórico privado do fornecedor. [Memória e evidências](05-evidencias-e-memoria.md) · [Critérios de avaliação](12-avaliacao-riscos-e-provas.md#a12-013). [Origem A04-017](#origem-a04-017).

<a id="falha"></a>
## Falhas, recuperação e evolução do harness

<a id="a04-018"></a>

Após um timeout com possível escrita, consultar o destino antes de repetir. Se a incerteza permanecer, suspender a parte dependente. Uma retomada identifica o que permanece válido e o que precisa ser refeito, considera idempotência, expiração e concorrência, e distingue repositórios e revisões para impedir colisões. Na falha de uma otimização opcional, cabe um percurso alternativo autorizado, com indicação da cobertura efetiva. Na falha de controle necessário ou de evidência indispensável, preservar a parcela independente e suspender a dependente. Alternativas não ampliam autoridade. [Origem A04-018](#origem-a04-018).

<a id="a04-019"></a>

Scripts, adaptadores, filtros, parâmetros, instruções e skills precisam ser identificáveis por revisão para que uma mudança material permita reexaminar os resultados atingidos. Registrar percurso observável, escopo, configuração, resultado, transformação e fonte; preservar restrições sobre dados derivados, destinos e exclusão de originais. A avaliação proposta compara o agente com uma referência nativa competente e observa efeitos do conjunto habilitado: um hook pode não injetar tokens e ainda consumir tempo; skills podem duplicar orientação; uma integração permanentemente carregada pode afetar outra atividade. **ONB-PEN-02/11..14 e Q13** deixam em refinamento margens de não regressão, custos, falhas e retomada, revalidação, versões e licenças, inclusive como ligar a prova anterior a cada push ao candidato exato. [Origem A04-019](#origem-a04-019).

## Como reencontrar as evidências

As notas numeradas estão no ZIP corrigido v0, em `rastreabilidade/temas/04.md`. Cada nota identifica as unidades usadas no bloco e seu índice de origem. A [consulta de origens](../consulta-origens.md) identifica as edições e permite partir de uma unidade. Os localizadores em tabelas incluem a linha do cabeçalho. A ligação a um bloco registra uso daquela passagem no texto.

<details>
<summary>Notas e antecedentes por passagem</summary>

| Passagem | Nota no ZIP v0 | Antecedente ou limite da comparação |
|---|---|---|
| <a id="origem-a04-001"></a> [A04-001](#a04-001) | `n1` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a04-002"></a> [A04-002](#a04-002) | `n2` | [R04-DEC-003](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-003) · [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-011](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-011) · [R04-DEC-024](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-024) |
| <a id="origem-a04-003"></a> [A04-003](#a04-003) | `n3` | [R04-DEC-006](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-006) · [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a04-004"></a> [A04-004](#a04-004) | `n4` | [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a04-005"></a> [A04-005](#a04-005) | `n5` | [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-039](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-039) |
| <a id="origem-a04-006"></a> [A04-006](#a04-006) | `n6` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-039](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-039) |
| <a id="origem-a04-007"></a> [A04-007](#a04-007) | `n7` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-011](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-011) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) |
| <a id="origem-a04-008"></a> [A04-008](#a04-008) | `n8` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) |
| <a id="origem-a04-009"></a> [A04-009](#a04-009) | `n9` | [R04-DEC-011](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-011) · [R04-DEC-036](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-036) · [R04-DEC-037](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-037) |
| <a id="origem-a04-010"></a> [A04-010](#a04-010) | `n10` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-036](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-036) |
| <a id="origem-a04-011"></a> [A04-011](#a04-011) | `n11` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-036](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-036) |
| <a id="origem-a04-012"></a> [A04-012](#a04-012) | `n12` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-039](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-039) |
| <a id="origem-a04-013"></a> [A04-013](#a04-013) | `n13` | [R04-DEC-006](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-006) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-037](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-037) |
| <a id="origem-a04-014"></a> [A04-014](#a04-014) | `n14` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a04-015"></a> [A04-015](#a04-015) | `n15` | [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) |
| <a id="origem-a04-016"></a> [A04-016](#a04-016) | `n16` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-012](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-012) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a04-017"></a> [A04-017](#a04-017) | `n17` | [R04-DEC-009](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-009) · [R04-DEC-010](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-010) · [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) |
| <a id="origem-a04-018"></a> [A04-018](#a04-018) | `n18` | [R04-DEC-005](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-005) · [R04-DEC-013](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-013) · [R04-DEC-039](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-039) |
| <a id="origem-a04-019"></a> [A04-019](#a04-019) | `n19` | [R04-DEC-015](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-015) · [R04-DEC-035](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-035) · [R04-DEC-038](../../consolidacao-r04/REGISTRO-DECISOES.md#r04-dec-038) |

</details>

<details>
<summary>Localizar as seções, tabelas e exemplos nos originais</summary>

Cada linha identifica o recorte titular. Os IDs das extremidades permitem abrir a composição exata da faixa no Repasse 2, em `indices-origem/faixas.csv` e `matriz.jsonl`. As linhas intermediárias seguem a seleção daquela ficha. Títulos delimitam a seção e casos, tabelas e registros preservam sua natureza original.

| Faixa | Da primeira à última unidade da ficha | O que procurar |
|---|---|---|
| <a id="faixa-u026-01"></a> U026-01 | `F1-P066` | Abre as direções de F1. A intenção de uma pessoa e a forma de prová-la têm autoridades diferentes. |
| <a id="faixa-u026-02"></a> U026-02 | `F1-P067` | Cabeçalho “Direções registradas”. A tabela de direções vem na parcela seguinte. |
| <a id="faixa-u026-03"></a> U026-03 | `F1-T05R01 … F1-P070` | O engenheiro deve conseguir usar o cliente pretendido e os benefícios das ferramentas de análise disponíveis no recorte permitido. |
| <a id="faixa-u026-04"></a> U026-04 | `F1-P071 … F1-P074` | A intenção de preservar a qualidade exige ensaio comparável. Margem, classe crítica e perda admissível continuam para refinamento. |
| <a id="faixa-u026-05"></a> U026-05 | `F1-T06R01 … F1-P076` | Cliente, modelo, analisador, tecnologia, domínio e ambiente variam independentemente. Registre qual variação a afirmação cobre. |
| <a id="faixa-u027-01"></a> U027-01 | `F1-P077` | Introduz o modelo funcional como proposta de organização do motor. |
| <a id="faixa-u027-02"></a> U027-02 | `F1-P078` | Cabeçalho das responsabilidades de integração do modelo proposto. |
| <a id="faixa-u027-03"></a> U027-03 | `F1-P079 … F1-P082` | Distribuir responsabilidades lógicas entre núcleo, adaptadores, catálogo, artefatos e avaliação permite identificar onde se perde significado. |
| <a id="faixa-u027-04"></a> U027-04 | `F1-P083 … F1-P087` | A chamada, a semântica do retorno e a possibilidade de sustentar uma conclusão pedem evidências próprias. |
| <a id="faixa-u027-05"></a> U027-05 | `F1-P088 … F1-P098` | O fluxo vai da pergunta à descoberta, produção, verificação e registro que outro cliente possa consultar. |
| <a id="faixa-u027-06"></a> U027-06 | `F1-P099 … F1-P101` | O contrato candidato explica entrada, efeito, transformação, acesso ao resultado e comportamento de recuperação. |
| <a id="faixa-u028-01"></a> U028-01 | `F1-P153` | Situa a parte de F1 que deriva requisitos para agentes e mecanismos. |
| <a id="faixa-u028-02"></a> U028-02 | `F1-P154` | Cabeçalho de RF15, sobre obrigações comuns e adaptações explícitas. Seu corpo e seu teste de retomada estão na parcela seguinte. |
| <a id="faixa-u028-03"></a> U028-03 | `F1-P155 … F1-P158` | RF15 pede conservar intenção, escopo, evidência, efeito e resultado entre clientes. F1-P156 propõe que outro agente autorizado retome o trabalho pelo registro comum, independentemente do histórico privado. A última unidade abre RF16. |
| <a id="faixa-u028-04"></a> U028-04 | `F1-P159 … F1-P161` | RF16 admite uso das especializações nativas e exige lidar com capacidades indisponíveis em outra modalidade. A última unidade abre RF17. |
| <a id="faixa-u028-05"></a> U028-05 | `F1-P162 … F1-P164` | RF17 pede conciliar instruções e skills aplicáveis e revelar incompatibilidades de escopo, precedência ou versão. |
| <a id="faixa-u028-06"></a> U028-06 | `F1-P165 … F1-P167` | RF18 pede testar entrada, momento e efeito de cada hook na modalidade e revisão em questão. |
| <a id="faixa-u028-07"></a> U028-07 | `F1-P168 … F1-P170` | RF19 pede explicitar ao engenheiro o que funciona, o que falta e o que pode prosseguir naquela combinação. |
| <a id="faixa-u029-01"></a> U029-01 | `F1-P171` | Localiza os requisitos derivados de estado, falha e evolução. |
| <a id="faixa-u029-02"></a> U029-02 | `F1-P172` | Cabeçalho de RF20, sobre o estado real das operações. A parcela seguinte contém o requisito e o exemplo do job. |
| <a id="faixa-u029-03"></a> U029-03 | `F1-P173 … F1-P175` | RF20 acompanha a operação depois da aceitação do pedido até uma saída verificável ou um estado de falha. |
| <a id="faixa-u029-04"></a> U029-04 | `F1-P176 … F1-P178` | RF21 verifica os efeitos já realizados antes de retomar a partir de um marco. |
| <a id="faixa-u029-05"></a> U029-05 | `F1-P179 … F1-P181` | RF22 mantém a parte independente e distingue a falta de uma otimização da ausência de um controle obrigatório. |
| <a id="faixa-u029-06"></a> U029-06 | `F1-P182 … F1-P184` | RF23 localiza quais resultados consumiram a configuração, filtro, adaptador ou versão alterados. |
| <a id="faixa-u029-07"></a> U029-07 | `F1-P185 … F1-P186` | RF24 obriga a examinar derivados, seus consumidores e as restrições de publicação quando muda uma premissa. |
| <a id="faixa-u030-01"></a> U030-01 | `F1-P187` | F1-P187 é a remissão do grupo de falhas e evolução às direções ONB-DIR-03/05/07, ao catálogo M07–M10/M13 e CA03–07/14/16/17/19 e a R04-DEC-017/038. O corpo de RF24 está na faixa anterior. |
| <a id="faixa-u031-01"></a> U031-01 | `F1-P188` | Delimita o capítulo de segurança, observabilidade e avaliação de F1. |
| <a id="faixa-u032-01"></a> U032-01 | `F1-P193` | Cabeçalho de RF26, que introduz o registro do percurso observável. |
| <a id="faixa-u032-02"></a> U032-02 | `F1-P194 … F1-P195` | RF26 conserva origem, revisão, operação, transformação e resultado observável, respeitando o acesso ao registro. |
| <a id="faixa-u033-01"></a> U033-01 | `F1-P102` | Introduz a seção de requisitos derivados. Um identificador de requisito marca proposta até que se estabeleçam natureza e aceite. |
| <a id="faixa-u033-02"></a> U033-02 | `F1-P103` | Localiza os requisitos no catálogo do motor para recuperar o contexto que acompanha suas cláusulas. |
| <a id="faixa-u034-01"></a> U034-01 | `F1-P221` | Abre o estudo de ferramentas, mecanismos e compatibilidade de F1. |
| <a id="faixa-u034-02"></a> U034-02 | `F1-P222` | Cabeçalho sobre os papéis dos mecanismos de integração. |
| <a id="faixa-u034-03"></a> U034-03 | `F1-P223 … F1-P226` | Separa arquivos de orientação, rotinas executáveis, interfaces e verificadores de conformidade. |
| <a id="faixa-u034-04"></a> U034-04 | `F1-P227 … F1-P231` | Contrasta diferenças documentadas em arquivo de instruções, carregamento, pré-aprovação e operação de hooks. |
| <a id="faixa-u034-05"></a> U034-05 | `F1-P232 … F1-P235` | Um padrão comum de transporte admite capacidades e permissões diferentes nos dois lados. |
| <a id="faixa-u034-06"></a> U034-06 | `F1-P236 … F1-P240` | A identidade do projeto CodeWiki, a granularidade de atualização e a duração dos arquivos variam segundo instalação e modo. |
| <a id="faixa-u034-07"></a> U034-07 | `F1-T10R01 … F1-P244` | Busca textual, navegação de símbolos, grafo e documentação oferecem evidências diferentes para a mesma investigação. |
| <a id="faixa-u034-08"></a> U034-08 | `F1-P245 … F1-P247` | A matriz proposta conserva operação, recorte e estado de compatibilidade da combinação testada. |
| <a id="faixa-u035-01"></a> U035-01 | `F4-L1539` | Introduz o estudo do harness no dossiê F4. |
| <a id="faixa-u035-02"></a> U035-02 | `F4-L1541 … F4-L1546` | Situa fontes de orientação e aplicação segundo contexto e autoridade. |
| <a id="faixa-u035-03"></a> U035-03 | `F4-L1548 … F4-L1562` | Distingue instruções aplicáveis, skills, ferramentas, políticas e validadores pelo efeito que podem produzir. |
| <a id="faixa-u035-04"></a> U035-04 | `F4-L1564 … F4-L1572` | A mesma intenção pode exigir adaptadores específicos e testes que verifiquem efeitos equivalentes. |
| <a id="faixa-u035-05"></a> U035-05 | `F4-L1574 … F4-L1591` | A composição deve resolver pertinência, versões e conflitos entre orientações antes de entregá-las ao agente. |
| <a id="faixa-u035-06"></a> U035-06 | `F4-L1593 … F4-L1599` | A tarefa delegada explicita as ferramentas, o contexto e as permissões efetivamente disponíveis ao subagente. |
| <a id="faixa-u035-07"></a> U035-07 | `F4-L1601 … F4-L1606` | Comparar clientes pela obrigação cumprida, evidência, efeito e limite conservados no mesmo recorte. |

</details>
