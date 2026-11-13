# Catálogo de pendências e resoluções P01–P09

Revisão documental de 13/11/2026. Base remota imutável: `0cc6456fbd7613b9a4369d60684d0fe1170a2ed2`, branch `proposta/d02-primeira-entrega-refinamentos`, PR #9. Universo original: **77 IDs**, com **43 fichas completas fora P03/P04** e **34 entradas referenciais P03/P04**. IDs editoriais preservados; contagem de perguntas não mede cobertura de todas as conversas.

As perguntas, contextos e exemplos das 43 fichas são transcritos da fonte curada CADERNO-ED11. As recomendações nela contidas continuam **propostas do assistente**. Dependências e critérios de resolução abaixo são **propostas editoriais desta consolidação**, sem aceite atribuído. Exemplos são sintéticos. Uma decisão funcional preservada não é reaberta por faltar mecanismo, formato, teste operacional ou mensagem histórica original.

**Regra de localizadores:** neste catálogo, `C-P04-*` sem rodada significa **C1-U3**, a manifestação humana final `518d8f93-6536-4b3b-a49d-86faf5033896`, conforme [P04-CONSOLIDADO](P04-CONSOLIDADO.md). Em particular, U3/C-P04-04 significa descoberta gradual de contexto. O rótulo A1/C-P04-04, usado antes para adoção entre branches, deve sempre ser qualificado como A1 e remete a P04.11.

As fontes abaixo permitem rastreio nos dois sentidos: cada ficha mantém o ID e aponta à âncora original; cada âncora P01/P02/P05–P09 tem aqui ficha do mesmo ID; cada linha P03/P04 remete ao registro temático e/ou ficha original. O quadro D02 ao final mantém os seis IDs transversais, sem confundi-los com as 77 perguntas.

## Fichas completas dos sete grupos restantes

## P01 — Distribuição e acesso

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p01-1"></a>

### P01.1

**P01.1 · Qual deve ser a visibilidade padrão do repositório de Workspaces de uma Sigla?** · Agenda

A escolha alcança conteúdo ativo e arquivado.

*Exemplo.* Uma atividade contém requisitos reservados à equipe. Uma branch própria ainda tem o público de leitura do repositório.

*Recomendação da fonte — proposta, sem aceite presumido.* Usar o menor público compatível com a finalidade. Documentar quando uma exceção é admissível e quem pode autorizá-la segundo as políticas do banco.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P05.5; P04.9–10: publicidade corporativa não escolhe classificação padrão dos Workspaces.

**Critério observável de resolução — proposta editorial:** Uma decisão identifica público padrão do conteúdo ativo/arquivado e quem trata exceções, com exemplo de atividade reservada.

**Fonte e destino:** [CADERNO-ED11, P01.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-1); destino nesta consolidação: ficha P01.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-2"></a>

### P01.2

**P01.2 · Quem deve poder descobrir um mapa que referencia componentes de duas Siglas?** · Agenda

Metadados no pai podem revelar existência, origem e revisão.

*Exemplo.* O leitor de um mapa consegue ver que C participa de um fluxo, mesmo sem poder abrir C.

*Recomendação da fonte — proposta, sem aceite presumido.* Escolher o público pelo que o próprio mapa revela. Aplicar a decisão ao local de publicação depois de P08.1.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1 e P08.6; P04.9–10.

**Critério observável de resolução — proposta editorial:** Uma escolha explicita quem vê mapa e seus metadados para a saída arquitetural selecionada.

**Fonte e destino:** [CADERNO-ED11, P01.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-2); destino nesta consolidação: ficha P01.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-3"></a>

### P01.3

**P01.3 · Qual relação física a instalação deve manter com a raiz Git Macro?** · Agenda

A topologia Macro–Meso–Micro está definida, mas o clone de distribuição e a pasta local têm finalidades próprias.

*Exemplo.* A raiz comum recebe uma atualização mesmo se o usuário não puder baixar uma das Siglas.

*Recomendação da fonte — proposta, sem aceite presumido.* Demonstrar o percurso desse usuário antes de decidir se o clone comum também pode exercer a função de Macro.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** HUM-05; P05.5; fluxo de atualização da raiz já aceito.

**Critério observável de resolução — proposta editorial:** Um percurso demonstra relação entre instalação, clone comum e Macro, inclusive Sigla inacessível.

**Fonte e destino:** [CADERNO-ED11, P01.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-3); destino nesta consolidação: ficha P01.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-4"></a>

### P01.4

**P01.4 · Como o engenheiro deve iniciar a Plataforma na primeira entrega?** · Agenda

Falta escolher a interação esperada e o resultado visível da atualização inicial.

*Exemplo.* O usuário abre a Plataforma pela manhã e precisa identificar a revisão comum obtida.

*Recomendação da fonte — proposta, sem aceite presumido.* Definir uma entrada reconhecível e o que comprova a atualização. A equipe autorizada poderá selecionar o mecanismo compatível com a estação corporativa.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.3; P02.2; fluxo CLI posteriormente esclarecido, atualização verificável ainda a detalhar.

**Critério observável de resolução — proposta editorial:** Um percurso de entrada mostra revisão comum obtida, resultado da atualização e inicialização do agente por modalidade pertinente.

**Fonte e destino:** [CADERNO-ED11, P01.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-4); destino nesta consolidação: ficha P01.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-5"></a>

### P01.5

**P01.5 · Que trabalho pode continuar quando a atualização da raiz falha?** · Agenda

A situação difere de uma dependência privada que falha mais tarde, ao abrir a atividade.

*Exemplo.* A máquina possui uma cópia de ontem e não consegue consultar o remoto.

*Recomendação da fonte — proposta, sem aceite presumido.* Mostrar a última revisão confirmada e o impedimento. Delimitar o que é seguro consultar nessa condição e o que exige atualização verificada.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.4; P04.1–4; preservar conhecimento independente.

**Critério observável de resolução — proposta editorial:** Um caso de falha explicita revisão confirmada, aviso e tarefas permitidas/dependentes.

**Fonte e destino:** [CADERNO-ED11, P01.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-5); destino nesta consolidação: ficha P01.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-6"></a>

### P01.6

**P01.6 · Quais operações com o remoto a primeira entrega precisa autenticar?** · Agenda

É preciso distinguir obter a raiz, ler dependências e enviar trabalho.

*Exemplo.* Uma credencial permite clonar A, mas não publicar o resultado derivado no Meso.

*Recomendação da fonte — proposta, sem aceite presumido.* Fazer uma matriz de operação, destino e autoridade requerida. Deixar credenciais e fluxos corporativos para validação interna.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** HUM-06; P04.7–10; operações distintas e direitos reais.

**Critério observável de resolução — proposta editorial:** Uma matriz nomeia operações, destinos, autoridade e evidência de sucesso; contratos reais ficam para validação interna.

**Fonte e destino:** [CADERNO-ED11, P01.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-6); destino nesta consolidação: ficha P01.6. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p01-7"></a>

### P01.7

**P01.7 · Que publicação remota o usuário precisa conseguir iniciar pela Plataforma?** · Agenda

O fechamento local de um estudo e a publicação da revisão são eventos distintos.

*Exemplo.* O Motor conclui um estudo local de A e o engenheiro deseja encaminhá-lo para revisão.

*Recomendação da fonte — proposta, sem aceite presumido.* Decidir se o produto prepara o material, oferece publicação revisável ou prevê outra entrega. Vincular cada opção ao destino, à autorização e ao recibo correspondente. P04.11 trata de quando o conteúdo se torna referência validada.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.6; P04.11; S2 de P03.

**Critério observável de resolução — proposta editorial:** Uma decisão mostra preparação/publicação prevista, destino, autorização, revisão e recibo esperado.

**Fonte e destino:** [CADERNO-ED11, P01.7](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p01-7); destino nesta consolidação: ficha P01.7. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P02 — Ferramentas de IA

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p02-1"></a>

### P02.1

**P02.1 · Quais tarefas definem suporte suficiente em cada modalidade?** · Agenda

Explorar recursos próprios preservando o uso das bases comuns.

*Exemplo.* O mesmo estudo de integração é consultado no Devin Web e no Claude Code.

*Recomendação da fonte — proposta, sem aceite presumido.* Comparar as modalidades por tarefa e resultado verificável, como localizar no mesmo Micro a evidência da chamada, e documentar diferenças aceitas.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P03.22; C-P04-09/10; comportamento comum, obtenção própria por modalidade.

**Critério observável de resolução — proposta editorial:** O mesmo caso gera resultados comparáveis nas modalidades escolhidas e diferenças aceitas ficam registradas.

**Fonte e destino:** [CADERNO-ED11, P02.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p02-1); destino nesta consolidação: ficha P02.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p02-2"></a>

### P02.2

**P02.2 · Como cada modalidade deve encontrar o conhecimento comum?** · Agenda

Falta estabelecer quais instruções próprias são necessárias para chegar à mesma revisão.

*Exemplo.* Uma instrução de entrada do CLI precisa encaminhar o agente para a mesma base que o Desktop.

*Recomendação da fonte — proposta, sem aceite presumido.* Manter a definição canônica em uma origem compartilhada. Usar configurações específicas para encaminhar o agente ao conteúdo ou expor capacidades próprias.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.3–4; P03.22; C-P04-04/09.

**Critério observável de resolução — proposta editorial:** Um agente por modalidade alcança a revisão correta por instrução demonstrável e descoberta gradual.

**Fonte e destino:** [CADERNO-ED11, P02.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p02-2); destino nesta consolidação: ficha P02.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p02-3"></a>

### P02.3

**P02.3 · Em que momento a Plataforma pode preparar configurações específicas no repositório?** · Agenda

Gravar arquivos exige autoridade sobre o destino.

*Exemplo.* O Micro está disponível para leitura, mas acrescentar instruções a uma pasta específica da ferramenta exige escrita.

*Recomendação da fonte — proposta, sem aceite presumido.* Prever proposta revisável com indicação do arquivo, revisão e finalidade. Validar internamente quem pode autorizar a escrita.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P02.2; HUM-04/06; escrita exige escopo próprio.

**Critério observável de resolução — proposta editorial:** Uma proposta nomeia arquivos, revisão, finalidade, momento e autoridade para escrita de configuração.

**Fonte e destino:** [CADERNO-ED11, P02.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p02-3); destino nesta consolidação: ficha P02.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p02-4"></a>

### P02.4

**P02.4 · Qual evidência de versão efetiva é aceitável em cada modalidade?** · Agenda

A observabilidade do serviço Web pode diferir da de um cliente local.

*Exemplo.* A CLI exibe uma versão. A interface Web, neste exemplo, só permite verificar se um recurso está disponível.

*Recomendação da fonte — proposta, sem aceite presumido.* Distinguir versão identificada, capacidade demonstrada e versão desconhecida. Testar quais evidências existem de fato no ambiente corporativo.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P02.1; evidência real no ambiente autorizado.

**Critério observável de resolução — proposta editorial:** Uma matriz distingue versão identificada, capacidade demonstrada e desconhecimento com evidência por modalidade.

**Fonte e destino:** [CADERNO-ED11, P02.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p02-4); destino nesta consolidação: ficha P02.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p02-5"></a>

### P02.5

**P02.5 · Qual é a continuidade esperada quando a atualização ou sua verificação falha?** · Agenda

O objetivo de trabalhar com a última versão já está definido.

*Exemplo.* Um agente instalado abre o Micro, mas não há comprovação de atualização da função exigida para a próxima ação.

*Recomendação da fonte — proposta, sem aceite presumido.* Avisar prontamente e mostrar as tarefas cujos pré-requisitos ainda são demonstráveis, explicitando a ação dependente.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P02.4; P04.12; continuidade independente.

**Critério observável de resolução — proposta editorial:** Um caso de falha mostra aviso, continuidade possível e ação dependente suspensa.

**Fonte e destino:** [CADERNO-ED11, P02.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p02-5); destino nesta consolidação: ficha P02.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P05 — Workspace de Atividades

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p05-1"></a>

### P05.1

**P05.1 · Qual sinal, se necessário, caracteriza o término da atividade?** · Agenda

Só então o time escolhe o destino da branch ou da pasta.

*Exemplo.* O refinamento foi aprovado, uma história acabou, outra ainda tem tasks em aberto.

*Recomendação da fonte — proposta, sem aceite presumido.* Começar por uma declaração do time sobre o conjunto. Avaliar se basta registrá-la ou se é preciso algum sinal adicional.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** R06; P06.1–2; término de refinamento não é término da atividade.

**Critério observável de resolução — proposta editorial:** Um exemplo com múltiplas histórias mostra sinal de término escolhido e destino de branch/pasta, preservando marcos distintos.

**Fonte e destino:** [CADERNO-ED11, P05.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-1); destino nesta consolidação: ficha P05.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p05-2"></a>

### P05.2

**P05.2 · Quem efetiva o vínculo da Sigla depois da permissão do Analista?** · Agenda

A responsabilidade pela autorização já está definida.

*Exemplo.* O Analista permite consultar o índice da Sigla B a partir da atividade da Sigla A.

*Recomendação da fonte — proposta, sem aceite presumido.* Comparar o agente efetivando o vínculo sob autorização e a efetivação por um membro autorizado. Em ambos os casos, registrar o resultado verificável.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** R06; P01.6; autorização do Analista preservada.

**Critério observável de resolução — proposta editorial:** Uma decisão nomeia quem efetiva o vínculo autorizado e como seu resultado é demonstrado.

**Fonte e destino:** [CADERNO-ED11, P05.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-2); destino nesta consolidação: ficha P05.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p05-3"></a>

### P05.3

**P05.3 · Em que condições outro Workspace pode consultar um histórico?** · Agenda

A finalidade de recuperar contexto já foi aceita.

*Exemplo.* Uma atividade nova precisa saber por que o time arquivou uma decisão anterior.

*Recomendação da fonte — proposta, sem aceite presumido.* Manter identificado o Workspace de origem e decidir que material a consulta pode apresentar ao público da nova atividade. Validar os limites de acesso reais.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.1; P04.9–10; origem e público do histórico.

**Critério observável de resolução — proposta editorial:** Um caso de consulta histórica especifica origem, material exibido e público autorizado do destino.

**Fonte e destino:** [CADERNO-ED11, P05.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-3); destino nesta consolidação: ficha P05.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p05-4"></a>

### P05.4

**P05.4 · O que alguém precisa encontrar na pasta de uma atividade para retomá-la?** · Agenda

O layout interno continua aberto.

*Exemplo.* Um colega abre uma atividade interrompida e precisa separar o requisito vigente, a hipótese descartada e a decisão que o explica.

*Recomendação da fonte — proposta, sem aceite presumido.* Testar o layout com essa retomada e com uma consulta histórica. Escolher diretórios e formatos depois de definir o percurso de leitura.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P06.4; P03.22; distinguir decisão, hipótese e revisão.

**Critério observável de resolução — proposta editorial:** Uma retomada localiza requisito vigente, hipótese descartada, decisão, revisão e próxima ação sem memória implícita.

**Fonte e destino:** [CADERNO-ED11, P05.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-4); destino nesta consolidação: ficha P05.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p05-5"></a>

### P05.5

**P05.5 · O repositório de Workspaces deve acumular a função do repositório Meso?** · Agenda

São responsabilidades distintas que podem ou não compartilhar armazenamento físico.

*Exemplo.* Um Meso destina seus índices a um público mais amplo do que uma atividade com documentos restritos.

*Recomendação da fonte — proposta, sem aceite presumido.* Confrontar público, finalidade, manutenção e arquivamento dos dois antes da decisão, acompanhando P01.1.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.1/3; HUM-05; função não equivale a identidade física.

**Critério observável de resolução — proposta editorial:** Uma decisão compara finalidade, público, manutenção e arquivamento e delimita eventual coabitação física.

**Fonte e destino:** [CADERNO-ED11, P05.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-5); destino nesta consolidação: ficha P05.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p05-6"></a>

### P05.6

**P05.6 · Quais informações permitem decidir sobre a inclusão de um repositório sugerido pelo agente?** · Desdobramento

O papel do Engenheiro e a consulta prévia já estão decididos. Falta concretizar a apresentação da sugestão.

*Exemplo.* Uma alteração de tarifa depende de confirmar o tratamento do campo em C. O Engenheiro precisa entender qual lacuna diminuiria ao incluí-lo, a revisão pertinente e que parte continuaria sem resposta.

*Recomendação da fonte — proposta, sem aceite presumido.* Mostrar a razão da sugestão, a fonte da relação, o ganho esperado, a revisão e os direitos ainda necessários. Registrar a decisão e permitir retomar a parte independente se a inclusão for adiada.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P03.6/9; decisão de inclusão cabe ao Engenheiro.

**Critério observável de resolução — proposta editorial:** Uma sugestão apresenta lacuna, evidência, ganho, revisão e direitos; registra decisão e continuidade independente.

**Fonte e destino:** [CADERNO-ED11, P05.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p05-6); destino nesta consolidação: ficha P05.6. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P06 — Agente, etapas e histórias

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p06-1"></a>

### P06.1

**P06.1 · Qual sinal determina a etapa de cada item?** · Agenda

Um Workspace pode conter histórias em etapas distintas.

*Exemplo.* A primeira história já está no planejamento de testes, enquanto outra ainda tem uma regra de negócio em aberto.

*Recomendação da fonte — proposta, sem aceite presumido.* Identificar a etapa por item a partir do último marco comprovado. Permitir que o usuário corrija um enquadramento incorreto.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** R01-P007; R06; P05.1.

**Critério observável de resolução — proposta editorial:** Um Workspace com histórias em etapas diferentes permite localizar último marco comprovado e corrigir enquadramento.

**Fonte e destino:** [CADERNO-ED11, P06.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-1); destino nesta consolidação: ficha P06.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-2"></a>

### P06.2

**P06.2 · Que condição permite propor a passagem de uma etapa à seguinte?** · Agenda

A aprovação formal que encerra o refinamento já tem responsável.

*Exemplo.* Uma história tem critérios redigidos, mas a equipe ainda discute uma exceção material.

*Recomendação da fonte — proposta, sem aceite presumido.* Especificar por transição o resultado exigido e o ato humano aplicável. Mostrar o que falta antes de sugerir avanço.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P06.1; aprovação formal do Analista; HUM-09.

**Critério observável de resolução — proposta editorial:** Cada transição selecionada identifica resultado exigido, pendência material e ato humano aplicável.

**Fonte e destino:** [CADERNO-ED11, P06.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-2); destino nesta consolidação: ficha P06.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-3"></a>

### P06.3

**P06.3 · Como tratar uma mensagem que corrige uma etapa anterior?** · Agenda

A correção pode mudar decisões e artefatos derivados.

*Exemplo.* Durante o plano de testes, o Analista redefine o que caracteriza um pedido duplicado.

*Recomendação da fonte — proposta, sem aceite presumido.* Recuperar a definição anterior e apontar a história, os critérios e os testes atingidos. Mostrar quais partes ainda podem continuar.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P04.1–4; S3 de P03; P06.1.

**Critério observável de resolução — proposta editorial:** Uma correção tardia identifica artefatos atingidos, revisões e partes que ainda podem continuar.

**Fonte e destino:** [CADERNO-ED11, P06.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-3); destino nesta consolidação: ficha P06.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-4"></a>

### P06.4

**P06.4 · Que informação o agente precisa recuperar antes de retomar um item interrompido?** · Agenda

O estado do Workspace, a revisão do código e o status corporativo podem ter evoluído.

*Exemplo.* Outra pessoa retoma uma história depois que o contrato de integração mudou.

*Recomendação da fonte — proposta, sem aceite presumido.* Entregar uma síntese recuperável de etapa, última decisão, referências, ressalvas e próxima ação, conferindo as revisões que sustentam a retomada.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P05.4; P04.5/11; revisões e status podem divergir.

**Critério observável de resolução — proposta editorial:** Uma retomada confere etapa, última decisão, referências, ressalvas e revisão antes da próxima ação.

**Fonte e destino:** [CADERNO-ED11, P06.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-4); destino nesta consolidação: ficha P06.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-5"></a>

### P06.5

**P06.5 · O que conta como uma entrega suficiente em cada atividade do agente?** · Agenda

Falta concretizar competências, fontes e resultados por etapa.

*Exemplo.* Na regra contra duplicidade, a história precisa de comportamento observável e o plano de testes precisa incluir o caso de dois pedidos legítimos.

*Recomendação da fonte — proposta, sem aceite presumido.* Construir um exemplo aceito por etapa sobre a mesma demanda. Usar os exemplos para derivar critérios, entregáveis e responsabilidades.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P06.1–4; P03.19; critérios por natureza da tarefa.

**Critério observável de resolução — proposta editorial:** Exemplos aceitos por etapa vinculam competências, fontes, resultados e critérios observáveis.

**Fonte e destino:** [CADERNO-ED11, P06.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-5); destino nesta consolidação: ficha P06.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-6"></a>

### P06.6

**P06.6 · Quais transições de história no ServiceNow/IUClick o produto deve oferecer?** · Agenda

Os verbos gerais estão definidos, mas faltam os estados, gatilhos e atos válidos.

*Exemplo.* Depois do aceite do refinamento, criar uma história e alterar seu status posteriormente representam eventos diferentes.

*Recomendação da fonte — proposta, sem aceite presumido.* Preparar uma matriz por transição com gatilho, papel autorizado, efeito esperado e evidência de sucesso. O responsável interno valida o contrato real.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.6; P06.2; contrato corporativo autorizado.

**Critério observável de resolução — proposta editorial:** Uma matriz por transição identifica gatilho, papel, efeito e evidência; contrato real é validado no ambiente autorizado.

**Fonte e destino:** [CADERNO-ED11, P06.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-6); destino nesta consolidação: ficha P06.6. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p06-7"></a>

### P06.7

**P06.7 · Onde termina o suporte a tasks, subtasks e bugs na primeira entrega?** · Desdobramento

O detalhamento pelo agente já está previsto. A integração definida expressamente para histórias tem um alcance próprio.

*Exemplo.* O engenheiro quer decompor uma história em subtasks e depois vê-las no sistema corporativo.

*Recomendação da fonte — proposta, sem aceite presumido.* Definir por tipo se a saída é uma descrição revisável ou se requer operação no sistema. Validar separadamente qualquer operação adicional pretendida.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P06.6; escopo de integração expressa para histórias.

**Critério observável de resolução — proposta editorial:** Uma decisão por tipo delimita descrição revisável versus operação corporativa e sua autorização.

**Fonte e destino:** [CADERNO-ED11, P06.7](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p06-7); destino nesta consolidação: ficha P06.7. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P07 — Extensões por escopo

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p07-1"></a>

### P07.1

**P07.1 · Que informação mínima torna uma extensão apta a ser incorporada em cada tipo?** · Agenda

Uma instrução de leitura e uma ferramenta executável apresentam exigências diferentes.

*Exemplo.* Uma equipe quer incluir a orientação de uso do ODM e uma integração para consultá-lo.

*Recomendação da fonte — proposta, sem aceite presumido.* Começar por finalidade, escopo de origem, revisão, tarefa de exemplo e atos permitidos. Definir a verificação apropriada a cada tipo.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P02.3; HUM-06; P07.5.

**Critério observável de resolução — proposta editorial:** Um exemplar por tipo registra finalidade, origem, revisão, tarefa, atos e verificação proporcional.

**Fonte e destino:** [CADERNO-ED11, P07.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p07-1); destino nesta consolidação: ficha P07.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p07-2"></a>

### P07.2

**P07.2 · Como o agente reconhece que uma extensão de outro escopo se aplica à atividade?** · Agenda

A recuperação deve funcionar mesmo que a pessoa desconheça seu nome.

*Exemplo.* Ao analisar uma resposta no consumidor, o agente chega pela dependência à orientação do integrador.

*Recomendação da fonte — proposta, sem aceite presumido.* Fazer o agente explicar o caminho entre a necessidade e a extensão, incluindo a condição que torna o recurso pertinente.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P03.4/6; P04.1–4; C-P04-04.

**Critério observável de resolução — proposta editorial:** Um caso demonstra caminho da necessidade à extensão e condição de aplicabilidade sem depender do nome conhecido.

**Fonte e destino:** [CADERNO-ED11, P07.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p07-2); destino nesta consolidação: ficha P07.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p07-3"></a>

### P07.3

**P07.3 · Que regra resolve orientações incompatíveis de escopos diferentes?** · Agenda

Precedência funcional e permissão para executar uma operação são questões distintas.

*Exemplo.* Uma instrução da Sigla e uma do repositório indicam procedimentos divergentes para consultar a mesma decisão.

*Recomendação da fonte — proposta, sem aceite presumido.* Expor a divergência e suas origens. Definir quem resolve o caso antes de fixar precedência automática. Incluir instruções comuns da raiz e sua aplicabilidade aos executores.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** HUM-07; P02.2; autoridade operacional não decorre de precedência.

**Critério observável de resolução — proposta editorial:** Um conflito explicita origens, consequência e responsável pela resolução antes de adotar precedência automática.

**Fonte e destino:** [CADERNO-ED11, P07.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p07-3); destino nesta consolidação: ficha P07.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p07-4"></a>

### P07.4

**P07.4 · Como uma atividade descobre o impacto da atualização ou retirada de uma extensão?** · Agenda

É preciso conseguir localizar os consumidores da orientação afetada.

*Exemplo.* Um MCP é substituído durante o refinamento de uma história que ainda cita a versão antiga.

*Recomendação da fonte — proposta, sem aceite presumido.* Preservar a referência histórica e testar se o usuário identifica quais orientações ainda são aplicáveis e qual dependência precisa de revisão.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P04.1–5; P07.2; rastreio de consumidores.

**Critério observável de resolução — proposta editorial:** Uma retirada/substituição preserva histórico e permite localizar consumidores e orientações ainda aplicáveis.

**Fonte e destino:** [CADERNO-ED11, P07.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p07-4); destino nesta consolidação: ficha P07.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p07-5"></a>

### P07.5

**P07.5 · O que o agente deve entregar quando encontra a extensão, mas não pode operá-la?** · Desdobramento

A permissão para conhecer o recurso já está dissociada da autoridade operacional.

*Exemplo.* O agente localiza a skill do ODM e o contrato emitido pelo integrador, mas não possui a permissão exigida para consultar a regra.

*Recomendação da fonte — proposta, sem aceite presumido.* Entregar o que as fontes acessíveis demonstram e especificar qual evidência uma pessoa autorizada poderia obter. Conferir no banco as operações realmente disponíveis.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** HUM-06; P03.9/13; P07.1.

**Critério observável de resolução — proposta editorial:** Um caso entrega conhecimento sustentado e identifica evidência obtível por autorizado sem alegar execução.

**Fonte e destino:** [CADERNO-ED11, P07.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p07-5); destino nesta consolidação: ficha P07.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P08 — Arquitetura e solução

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p08-1"></a>

### P08.1

**P08.1 · Qual entrega arquitetural o Analista precisa receber nesta versão?** · Agenda

As opções documentadas são evidências de relações, mapa candidato e base verificável.

*Exemplo.* Uma atividade atravessa duas Siglas e usa um componente que também serve a outra solução.

*Recomendação da fonte — proposta, sem aceite presumido.* Comparar as três saídas com a mesma pergunta realista. Escolher a menor que permita ao Analista reconhecer e delimitar a solução.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P03.4/6; P09.1; Analista delimita solução.

**Critério observável de resolução — proposta editorial:** Uma decisão compara evidências, mapa candidato e base verificável no mesmo caso e escolhe saída da versão.

**Fonte e destino:** [CADERNO-ED11, P08.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-1); destino nesta consolidação: ficha P08.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p08-2"></a>

### P08.2

**P08.2 · Como o Analista expressa a fronteira funcional da solução?** · Agenda

O mecanismo depende da saída escolhida.

*Exemplo.* A regra antifraude participa de abertura de conta e de concessão de crédito, com papéis distintos.

*Recomendação da fonte — proposta, sem aceite presumido.* Descrever finalidade, entrada, resultado e papel do componente em cada percurso. Registrar a decisão do Analista com seu alcance.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1; P09.3; preservar papel humano.

**Critério observável de resolução — proposta editorial:** Um exemplo registra finalidade, entrada, resultado, papéis de componente e alcance da delimitação pelo Analista.

**Fonte e destino:** [CADERNO-ED11, P08.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-2); destino nesta consolidação: ficha P08.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p08-3"></a>

### P08.3

**P08.3 · Como reconhecer a mesma solução entre revisões ou entre Workspaces?** · Agenda

É preciso decidir se a entrega arquitetural necessita de identidade própria.

*Exemplo.* Duas atividades chamam a mesma jornada por nomes diferentes.

*Recomendação da fonte — proposta, sem aceite presumido.* Começar por uma referência estável e por quem pode confirmar equivalência, se o recorte escolhido exigir identidade persistente.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1/2; P05.3.

**Critério observável de resolução — proposta editorial:** Uma decisão explica identidade/equivalência entre revisões e Workspaces caso a saída exija identidade persistente.

**Fonte e destino:** [CADERNO-ED11, P08.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-3); destino nesta consolidação: ficha P08.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p08-4"></a>

### P08.4

**P08.4 · O que deve constar na revisão de uma solução para o leitor reproduzir sua composição?** · Agenda

Um mapa pode combinar componentes em revisões distintas.

*Exemplo.* Um componente passa para a revisão 2 e outro continua na revisão 1.

*Recomendação da fonte — proposta, sem aceite presumido.* Preservar as revisões de cada relação técnica e da delimitação funcional que foi validada. Aplicar P04 aos itens afetados.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1/3; P04.4/11; commits e relações.

**Critério observável de resolução — proposta editorial:** Um leitor reproduz a composição pelas revisões das relações técnicas e da delimitação funcional.

**Fonte e destino:** [CADERNO-ED11, P08.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-4); destino nesta consolidação: ficha P08.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p08-5"></a>

### P08.5

**P08.5 · Qual manutenção da representação arquitetural cabe à primeira entrega?** · Agenda

Uma alteração pode afetar uma relação técnica sem mudar a finalidade da solução.

*Exemplo.* Um consumidor migra de chamada direta para evento e o processo de negócio continua com o mesmo objetivo.

*Recomendação da fonte — proposta, sem aceite presumido.* Definir quando a atualização técnica basta e quando a nova composição volta ao Analista. Condicionar a escolha a P08.1 e o público do resultado a P01.2.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1/4; P01.2; P04.1–4.

**Critério observável de resolução — proposta editorial:** Um caso diferencia atualização técnica suficiente de nova confirmação pelo Analista e registra público.

**Fonte e destino:** [CADERNO-ED11, P08.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-5); destino nesta consolidação: ficha P08.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p08-6"></a>

### P08.6

**P08.6 · Quem responde pelo catálogo arquitetural e pela publicação de uma composição reconhecida, caso existam nesta versão?** · Agenda

A delimitação da solução pelo Analista já tem autoridade definida. Falta decidir a propriedade e o ciclo de publicação da representação.

*Exemplo.* Duas Siglas mantêm componentes de uma solução. Há um mapa candidato e uma composição funcional confirmada que mudam em momentos diferentes.

*Recomendação da fonte — proposta, sem aceite presumido.* Definir quem mantém a identidade, confirma a passagem de candidato à revisão utilizável e escolhe o destino conforme o público autorizado. Avaliar nomenclatura, armazenamento e catálogo na raiz depois de P08.1.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1/3; P01.2/7; P04.11.

**Critério observável de resolução — proposta editorial:** Uma decisão nomeia mantenedor, confirmação de candidato para utilizável, destino e público quando esse catálogo fizer parte do recorte.

**Fonte e destino:** [CADERNO-ED11, P08.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p08-6); destino nesta consolidação: ficha P08.6. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P09 — Conhecimento de Negócios

Estado: grupo em refinamento; respostas posteriores podem resolver parcelas das fichas. Não se presume fechamento por analogia com P03/P04.

<a id="p09-1"></a>

### P09.1

**P09.1 · Qual pergunta de negócio deve orientar o primeiro exemplo?** · Agenda

Escolher uma cuja resposta altere um requisito.

*Exemplo.* O canal anterior exige análise manual. O novo canal deve encaminhar o mesmo caso?

*Recomendação da fonte — proposta, sem aceite presumido.* Usar o exemplo do canal, ou outro sintético que o usuário reconheça, deixando explícito o que já se conhece pela implementação.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P08.1/2; P03.1; escolha de exemplo ainda necessária.

**Critério observável de resolução — proposta editorial:** Uma pergunta sintética é escolhida e sua resposta altera concretamente um requisito.

**Fonte e destino:** [CADERNO-ED11, P09.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-1); destino nesta consolidação: ficha P09.1. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-2"></a>

### P09.2

**P09.2 · Que fonte pode demonstrar a regra de negócio aplicável ao caso escolhido?** · Agenda

Documentação técnica e evidência de execução sustentam o comportamento observado.

*Exemplo.* O código encaminha a proposta, mas só uma política ou orientação legítima esclarece se ambos os canais estão abrangidos.

*Recomendação da fonte — proposta, sem aceite presumido.* Distinguir políticas, relatos e evidências operacionais. Validar com a área competente a abrangência da fonte e o acesso permitido.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P09.1; HUM-06; P04.9–10.

**Critério observável de resolução — proposta editorial:** Uma fonte identificada sustenta regra e alcance, distinguindo política, relato e comportamento observado.

**Fonte e destino:** [CADERNO-ED11, P09.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-2); destino nesta consolidação: ficha P09.2. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-3"></a>

### P09.3

**P09.3 · Quem pode validar o significado da regra para a atividade?** · Agenda

A autoria de uma implementação não determina a autoridade sobre o produto.

*Exemplo.* O responsável pelo serviço conhece o encaminhamento atual, mas a área do produto pode ter autoridade para decidir sobre o novo canal.

*Recomendação da fonte — proposta, sem aceite presumido.* Registrar o papel responsável, o alcance de sua manifestação e como solicitar o esclarecimento. Confirmar o responsável real apenas no contexto autorizado.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P09.1/2; S2/S3 de P03.

**Critério observável de resolução — proposta editorial:** Um papel competente e alcance da validação são nomeados; pessoa/autoridade real depende de contexto autorizado.

**Fonte e destino:** [CADERNO-ED11, P09.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-3); destino nesta consolidação: ficha P09.3. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-4"></a>

### P09.4

**P09.4 · Qual unidade organiza o conhecimento para que as pessoas consigam encontrá-lo?** · Agenda

Produto, domínio, processo e jornada são candidatos.

*Exemplo.* A mesma política aparece em dois canais e atravessa várias soluções.

*Recomendação da fonte — proposta, sem aceite presumido.* Testar a recuperação partindo da história e da regra, antes de decidir a unidade, sua transversalidade ou a estrutura física.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P09.1/5; P03.22; P08.1.

**Critério observável de resolução — proposta editorial:** Um percurso recupera a mesma regra pela história e pelo assunto, permitindo decidir unidade organizadora.

**Fonte e destino:** [CADERNO-ED11, P09.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-4); destino nesta consolidação: ficha P09.4. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-5"></a>

### P09.5

**P09.5 · Qual é a menor resposta de negócio útil ao engenheiro e ao agente?** · Agenda

A saída precisa mudar concretamente o refinamento.

*Exemplo.* Ao escrever a história do novo canal, o analista precisa saber se o encaminhamento é obrigatório e que parte permanece indefinida.

*Recomendação da fonte — proposta, sem aceite presumido.* Testar um registro com significado, alcance, fonte, responsável, vigência e consequência para a história. Manter a lacuna visível quando faltar confirmação.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P09.1–4; P03.19; saída útil observável.

**Critério observável de resolução — proposta editorial:** Um exemplo de saída muda o refinamento e contém significado, alcance, fonte, responsável, vigência e lacuna.

**Fonte e destino:** [CADERNO-ED11, P09.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-5); destino nesta consolidação: ficha P09.5. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-6"></a>

### P09.6

**P09.6 · Como saber qual orientação de negócio estava vigente no momento relevante?** · Agenda

A data de uma decisão de produto pode diferir da revisão do código.

*Exemplo.* Uma regra de análise manual termina no próximo mês, enquanto o código ainda conserva o fluxo anterior.

*Recomendação da fonte — proposta, sem aceite presumido.* Registrar vigência, histórico e confirmação da área responsável. Vincular o efeito prático à história e aplicar P04 para revalidar os derivados autorizados.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P09.2/3; P04.1–4; vigência distinta de commit.

**Critério observável de resolução — proposta editorial:** Um caso diferencia vigência de orientação e revisão do código e identifica derivados a revalidar.

**Fonte e destino:** [CADERNO-ED11, P09.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-6); destino nesta consolidação: ficha P09.6. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

<a id="p09-7"></a>

### P09.7

**P09.7 · Que público precisa ver a regra de negócio, sua justificativa e as eventuais exceções?** · Agenda

Uma política pode ser consultável por uma equipe e ter restrições de cópia.

*Exemplo.* O agente de outra Sigla encontra a referência à política, mas o Workspace tem público mais amplo que a fonte.

*Recomendação da fonte — proposta, sem aceite presumido.* Definir com a área responsável quais referências ou resumos podem ser usados no destino. Aplicar as autorizações de P04 sem inferir direito de redistribuição.

**Estado:** pendência preservada, com os impactos posteriores das decisões P03/P04 a considerar. **Por que permanece:** não foi localizada nesta recuperação uma decisão humana que encerre integralmente esta ficha.

**Dependências — proposta editorial:** P01.1/2; P04.9–10; direitos sobre conteúdo.

**Critério observável de resolução — proposta editorial:** Uma decisão delimita público e referências/resumos permitidos, sem conceder redistribuição pela leitura.

**Fonte e destino:** [CADERNO-ED11, P09.7](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md#p09-7); destino nesta consolidação: ficha P09.7. O contexto, o exemplo e a recomendação conservados acima tornam recuperável o efeito da escolha; a formulação do critério não constitui requisito aprovado.

## P03 — Catálogo referencial das 22 perguntas

Fonte temática canônica consultada: [P03-CONHECIMENTO](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md), revisão temática 1. História das edições 1–11 preservada no [CADERNO-ED11](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/historico/CADERNO-ED11.md). As vinte perguntas resolvidas no alcance funcional não voltam a abertas pela ausência de desenho ou prova operacional. As duas frentes postergadas mantêm seus IDs.

| ID | Estado preservado | Resultado funcional e condições da fonte | Fonte/destino |
|---|---|---|---|
| <a id="p03-1"></a>P03.1 | RESOLVIDO NO ALCANCE FUNCIONAL | Consolidar no onboarding todo conhecimento suficientemente válido identificado. Para uma chamada HTTP consumida, permitir recuperar URL, verbo, campos de entrada com tipos e exemplos quando possível, campos de saída, headers, parâmetros de consulta, variáveis de caminho, configurações de timeout e status esperados. Explicar o tratamento dado pelo próprio repositório às respostas quando ele muda uma conclusão material. A política de explicação, referência e enriquecimento está na seção 2. Origem preservada: Ed. 2, 4, 7 e 8; C-P03-01/02, R1/R2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.1; destino: esta linha P03.1. |
| <a id="p03-2"></a>P03.2 | RESOLVIDO NO ALCANCE FUNCIONAL | A finalidade do onboarding é fixa. O Engenheiro indica o que importar. O Motor examina, conforme aplicável, responsabilidades, fluxos, regras, contratos de entrada e saída, integrações, APIs, workers, tópicos, filas, bancos, configurações, variáveis, bibliotecas, frameworks, recursos de infraestrutura e procedimentos documentados de operação e teste. O uso frequente de AWS e Terraform foi relatado pelo usuário para seu ambiente. O DoD corrigido está na seção 3. Origem preservada: Ed. 2, 4, 7 e 8; C-P03-03/08, R4. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.2; destino: esta linha P03.2. |
| <a id="p03-3"></a>P03.3 | RESOLVIDO NO ALCANCE FUNCIONAL | Relacionar cada afirmação à revisão e à evidência tão específica quanto o material permitir, do geral ao particular. Uma referência pode chegar a arquivo, seção, classe, método, linha, coluna, cláusula contratual ou bloco de infraestrutura. Quando a explicação requer duas fontes, manter ambas. Origem preservada: Ed. 2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.3; destino: esta linha P03.3. |
| <a id="p03-4"></a>P03.4 | RESOLVIDO NO ALCANCE FUNCIONAL | O Meso reúne os repositórios da Sigla como submódulos e indexa suas responsabilidades para conduzir uma dúvida até os Micro pertinentes. O índice identifica o material estudado, suas revisões e os limites conhecidos. O catálogo da raiz encaminha o assunto à Sigla quando ela for inicialmente desconhecida. A delimitação funcional de uma solução, inclusive entre Siglas, compete ao Analista. Origem preservada: Ed. 2–4, 7–10; R6–R8, S3. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.4; destino: esta linha P03.4. |
| <a id="p03-5"></a>P03.5 | RESOLVIDO NO ALCANCE FUNCIONAL | O usuário dispensou conhecer ou provar o total de repositórios da Sigla. Uma busca pode abranger todos os repositórios que o agente consiga encontrar dentro do acesso permitido. O resultado identifica a seleção ou busca efetiva, o que foi obtido e analisado e as falhas conhecidas. Origem preservada: Ed. 2; P03.7 e P03.9. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.5; destino: esta linha P03.5. |
| <a id="p03-6"></a>P03.6 | RESOLVIDO NO ALCANCE FUNCIONAL | Na relação examinada por um lado, registrar sentido, contrato ou evento observado, origem e revisão, limite da conclusão e o que teria de ser consultado no outro lado. O agente pode sugerir a inclusão de um repositório pertinente na atividade; a decisão cabe ao Engenheiro. Origem preservada: Ed. 2 e 4; C-P03-01. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.6; destino: esta linha P03.6. |
| <a id="p03-7"></a>P03.7 | RESOLVIDO NO ALCANCE FUNCIONAL | Quatro entradas: indicação de repositórios em diretório local, repositórios arrastados para a pasta da Plataforma, links GitHub ou busca por Sigla no GitHub. A pasta local usa a branch em que está, salvo indicação do Engenheiro, e retrata a cópia de trabalho autorizada com alterações locais distinguidas do commit-base. O link remoto para a raiz usa `main`; um link de branch específica é escolha explícita. Falha de obtenção segue P03.9. Origem preservada: Ed. 2, 4 e 5; C-P03-04/05. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.7; destino: esta linha P03.7. |
| <a id="p03-8"></a>P03.8 | RESOLVIDO NO ALCANCE FUNCIONAL | Segundo o usuário, o nome do repositório identifica obrigatoriamente sua Sigla no ambiente descrito. O Motor identifica esse pertencimento e organiza a cópia na pasta correspondente. A participação em atividade de outra Sigla preserva o pertencimento original. Origem preservada: Ed. 2 e 3. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.8; destino: esta linha P03.8. |
| <a id="p03-9"></a>P03.9 | RESOLVIDO NO ALCANCE FUNCIONAL | Para cada parte material incompleta, indicar revisão, conteúdo examinado, material faltante, motivo conhecido, consequência e ponto de retomada. Entregar a parte sustentada. Delimitar a conclusão que depende da fonte ausente. Origem preservada: Ed. 2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.9; destino: esta linha P03.9. |
| <a id="p03-10"></a>P03.10 | RESOLVIDO NO ALCANCE FUNCIONAL | Uma nova execução ou um novo entendimento validado sobre um repositório deve refletir-se no material pertinente de sua Sigla. O Meso se enriquece conforme os seus Micro. Preservar a revisão conhecida dos demais repositórios e a cobertura da rodada. Origem preservada: Ed. 2 e 3; S1. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.10; destino: esta linha P03.10. |
| <a id="p03-11"></a>P03.11 | RESOLVIDO NO ALCANCE FUNCIONAL | Na interação posterior, confrontar a evidência com a ação concreta pretendida. O agente explica o que pode afirmar ou fazer com segurança e quais decisões ainda dependem de outra fonte. Origem preservada: Ed. 2; distinção produtor/consumidor da ed. 8. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.11; destino: esta linha P03.11. |
| <a id="p03-12"></a>P03.12 | RESOLVIDO NO ALCANCE FUNCIONAL | Diante de divergência, confrontar objeto, revisão, condições e natureza das fontes. Preservar evidências e interpretações concorrentes e identificar a evidência necessária para distingui-las. Teste documentado e execução observada sustentam afirmações diferentes. Origem preservada: Ed. 2, 8 e 9; S1/S3. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.12; destino: esta linha P03.12. |
| <a id="p03-13"></a>P03.13 | RESOLVIDO NO ALCANCE FUNCIONAL | Durante a produção, a falta de suporte imprescindível à fidelidade da base ou à delimitação de sua cobertura impede a conclusão dependente. Se a criticidade continuar incerta após investigação autorizada, levar a dúvida ao Engenheiro. Na interação, avaliar o impacto sobre a pergunta ou ação quando ela existir. O agente pode entregar o trabalho independente. Origem preservada: Ed. 2 e 7, com a correção da ed. 8; [casos aceitos de A](../evidencias/ESCLARECIMENTOS-ONBOARDING.md). | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.13; destino: esta linha P03.13. |
| <a id="p03-14"></a>P03.14 | RESOLVIDO NO ALCANCE FUNCIONAL | Regra de pipeline **relatada pelo usuário** para os repositórios em questão: a release branch mais recente representa o código de HOM. Registrar o commit efetivamente examinado. A primeira entrega pode interpretar evidência autorizada de implantação ou configuração fornecida pelo Engenheiro, delimitando componente, revisão e ambiente. Atribuir uma ocorrência a uma requisição precisa de evidência daquela ocorrência. Origem preservada: Ed. 2–5; C-P03-06. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.14; destino: esta linha P03.14. |
| <a id="p03-15"></a>P03.15 | RESOLVIDO NO ALCANCE FUNCIONAL | Quando necessária intervenção, levar a menor pergunta útil, as hipóteses ainda compatíveis, as referências, as tentativas autorizadas e a decisão afetada. Diferenciar dúvida factual sobre a revisão de escolha de produto futura. Origem preservada: Ed. 2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.15; destino: esta linha P03.15. |
| <a id="p03-16"></a>P03.16 | RESOLVIDO NO ALCANCE FUNCIONAL | Catalogar e comunicar cada lacuna ou incoerência tão logo percebida, com a informação sustentada, a limitação e a próxima ação. O aviso explicita se o agente pode continuar sozinho ou se uma decisão humana é necessária naquele momento. Origem preservada: Ed. 2 e 3. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.16; destino: esta linha P03.16. |
| <a id="p03-17"></a>P03.17 | RESOLVIDO NO ALCANCE FUNCIONAL | Reapresentar uma ressalva nas perguntas e atividades em que houver dependência direta ou indireta, inclusive fora do Workspace. Mostrar a relação concreta e a consequência para o pedido atual. Se a ligação ainda for hipótese, explicitar o que falta para confirmá-la. Origem preservada: Ed. 2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.17; destino: esta linha P03.17. |
| <a id="p03-18"></a>P03.18 | RESOLVIDO NO ALCANCE FUNCIONAL | A primeira entrega prioriza o Motor sem interface gráfica própria construída pela equipe. O agente apresenta em linguagem direta a afirmação afetada, a fonte, a limitação e a próxima ação. A informação de detalhe deve ser acessível por assunto. Origem preservada: Ed. 2. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.18; destino: esta linha P03.18. |
| <a id="p03-19"></a>P03.19 | RESOLVIDO NO ALCANCE FUNCIONAL | Ao atender a um pedido, investigar até haver resposta suficientemente fundamentada conforme sua natureza, escopo, critérios e implicações. Reportar dúvidas e inconclusões e oferecer aprofundamento conforme a resposta do Engenheiro. Para encerrar o onboarding, usar o DoD do produtor da seção 3. Origem preservada: Ed. 2 e 8. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.19; destino: esta linha P03.19. |
| <a id="p03-20"></a>P03.20 | AVALIAÇÃO ADIADA — P03.20/C-P03-07 | **Avaliação adiada.** O usuário reservou a definição de testes, métodos, resultados esperados, responsáveis e provas de segurança, precisão e confiabilidade das bases. Origem preservada: Ed. 2, 7 e 8; C-P03-07/R10. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.20; destino: esta linha P03.20. |
| <a id="p03-21"></a>P03.21 | RESOLVIDO NO ALCANCE FUNCIONAL | A primeira entrega oferecerá o fluxo de solicitação excepcional de execução local da aplicação estudada nas condições de HUM-03. Após esgotar investigações autorizadas diante de uma dúvida intransponível, oferecer esclarecimento direto pelo Engenheiro. Para propor execução, indicar dúvida, tentativas, finalidade, ambiente, dados, pré-requisitos, comandos e efeitos e obter permissão específica por ocorrência. Origem preservada: Ed. 2 e 3; [HUM-03](../../REGISTRO.md#hum-03). A segunda resposta rotulada “P03.2” na primeira rodada foi vinculada a P03.21 pelo assunto e pela posição. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.21; destino: esta linha P03.21. |
| <a id="p03-22"></a>P03.22 | DIREÇÃO ACEITA — desenho concreto postergado | O conjunto de documentos e referências deve favorecer navegação, leitura, compreensão, explicação e modificação autorizada por qualquer agente, com profundidade, qualidade, rapidez e precisão, buscando menor consumo de ACUs, tokens, contexto e recursos. A direção funcional foi aceita; a estrutura física, a granularidade, os formatos, os índices e as instruções concretas ficam **postergados**. Origem preservada: Ed. 2, 4, 5, 7 e 8; R5. | [Registro temático](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#1-decisões-por-pergunta), linha P03.22; destino: esta linha P03.22. |

**Remanescentes reais.** P03.20/C-P03-07: definir testes, métodos, resultados esperados, responsáveis e provas de segurança, precisão, confiabilidade, tempo, recursos e custo por tarefa/modalidade. Dependências: P02 e C-P04-10. P03.22: escolher estrutura física, granularidade, formatos, índices e instruções concretas, preservando navegação, compreensão, profundidade, rapidez e precisão com uso econômico de recursos. Dependências: P02.2, P05.4, D02-PEN-005 e descoberta gradual de C-P04-04. **Critério editorial proposto:** uma avaliação reproduzível com universo/oráculos identificados para P03.20 e exemplares recuperáveis por modalidade para P03.22; nenhum desses mecanismos foi escolhido nesta ficha.

**Colaterais e transversais.** C-P03-01/02/04/05/06/08 aceitas; C-P03-03 direção aceita com DoD corrigido; C-P03-07 adiada. S1/S2/S3 encerradas funcionalmente, com correção inequívoca, pedido único de incorporação e conservação de conflito. Ver [§§2–7 do canônico](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P03-CONHECIMENTO.md#2-fronteira-e-manutenção-do-conhecimento-micro). Preservar origens e casos A/B/C: encerramento do onboarding com ressalvas não autoriza mudança dependente.

## P04 — Catálogo referencial das 12 perguntas

**Precedência.** O remoto-base ainda registra abertura de P04. A conversa recuperada `6aefea59-1198-83ea-ade8-26c2c77da871`, “Refinar PE03 questionar definition”, contém manifestações posteriores. Para P04.1–6, preservar aceites anteriores relatados na avaliação do assistente, explicitando que suas mensagens humanas originais não foram recuperadas neste recorte; isso é lacuna de proveniência, não declaração de que ficaram não decididos. P04.6 também possui suporte herdado direto do canônico P03. Para P04.7–12 e colaterais, a consolidação principal relaciona mensagens humanas recuperadas e seus IDs. Esta seção remete ao mesmo ID em vez de criar decisões concorrentes.

<a id="p04-1"></a>

### P04.1 — Atualização incremental

**Estado:** ACEITE ANTERIOR RELATADO E PRESERVADO; lacuna de proveniência humana original.

**Resultado, condições e limite:** Reaproveitamento e ampliação da investigação devem manter o alcance aceito anteriormente. A ficha de abertura descreve diferenças/dependências e retorno ao inventário se necessário, mas sua recomendação não substitui a mensagem humana ausente.

**Dependências — relação editorial:** HUM-08; D02-RET-004; P04.2–4.

**Fonte/destino:** [Ficha original P04.1](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-1); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.1. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-2"></a>

### P04.2 — Alcance da invalidação

**Estado:** ACEITE ANTERIOR RELATADO E PRESERVADO; lacuna de proveniência humana original.

**Resultado, condições e limite:** Preservar o aceite anterior sobre parte afetada, dependências e continuidade independente. A formulação literal humana desta rodada não foi recuperada; conservar a ficha como contexto histórico, sem afirmar comprovação de atualização de destino inacessível.

**Dependências — relação editorial:** P04.1/3; P03.9/13; HUM-08.

**Fonte/destino:** [Ficha original P04.2](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-2); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.2. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-3"></a>

### P04.3 — Restabelecimento da validade

**Estado:** ACEITE ANTERIOR RELATADO E PRESERVADO; lacuna de proveniência humana original.

**Resultado, condições e limite:** Manter distinção entre evidência da regra na revisão e prova de execução efetiva, sem reabrir o aceite relatado por faltar teste operacional. A recomendação original continua identificada em sua fonte.

**Dependências — relação editorial:** P04.1–2; HUM-08; P03.12.

**Fonte/destino:** [Ficha original P04.3](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-3); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.3. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-4"></a>

### P04.4 — Fechamento Micro/Meso/raiz

**Estado:** ACEITE ANTERIOR RELATADO E PRESERVADO; lacuna de proveniência humana original.

**Resultado, condições e limite:** Preservar conclusão por componente/composição e revisões explicitadas. Mecanismo futuro não equivale a ausência de decisão; a mensagem humana específica anterior não foi recuperada.

**Dependências — relação editorial:** HUM-05/08; D02-RET-004; P04.11; C-P04-05.

**Fonte/destino:** [Ficha original P04.4](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-4); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.4. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-5"></a>

### P04.5 — Contribuições concorrentes

**Estado:** ACEITE ANTERIOR RELATADO E PRESERVADO; lacuna de proveniência humana original.

**Resultado, condições e limite:** Manter o aceite anterior de releitura/reconciliação perante revisão-base alterada e conflito sem arbitragem infundada. Ausência de conflito textual não demonstra ausência de conflito semântico.

**Dependências — relação editorial:** HUM-09; S1/S3 de P03; D02-PEN-003.

**Fonte/destino:** [Ficha original P04.5](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-5); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.5. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-6"></a>

### P04.6 — Esclarecimento reutilizável

**Estado:** ACEITE HERDADO DE P03 E PRESERVADO; avaliação posterior relata P04.1–6 aceitos.

**Resultado, condições e limite:** Caso central já resolvido no P03: pedido de escrita reúne entendimento, origem, destino e efeito; Analista pode autorizar destino nomeado inclusive entre Siglas se permitido. Silêncio pendente; negativa descarta incorporação no destino negado.

**Dependências — relação editorial:** S2/S3 de P03; HUM-06/09; P04.11.

**Fonte/destino:** [Ficha original P04.6](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-6); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.6. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-7"></a>

### P04.7 — Alcance/reuso da autorização

**Estado:** RESOLVIDO FUNCIONALMENTE pelas manifestações humanas recuperadas; mecanismos específicos posteriores.

**Resultado, condições e limite:** C-P04-01 retifica interpretação anterior: eliminar consentimentos genéricos para leitura de fontes internas acessíveis, preservando aprovações específicas de decisões humanas, operações sensíveis e alterações com aceite expressamente definido. Não interpretar isso como poder operacional novo.

**Dependências — relação editorial:** HUM-06; S2 de P03; P01.6/7.

**Fonte/destino:** [Ficha original P04.7](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-7); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.7. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-8"></a>

### P04.8 — Vencimento/revogação

**Estado:** RESOLVIDO FUNCIONALMENTE pelas manifestações humanas recuperadas.

**Resultado, condições e limite:** C-P04-02 dispensa controle próprio de expiração e conserva reconhecimento de limitações efetivas. Conhecimento pode continuar disponível se conservação/distribuição legítimas; cópia local não justifica uso que perdeu fundamento. Não torna direitos irrevogáveis nem autoriza eliminação indiscriminada.

**Dependências — relação editorial:** HUM-06; P04.7/10; D02-PEN-004.

**Fonte/destino:** [Ficha original P04.8](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-8); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.8. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-9"></a>

### P04.9 — Visibilidade dos identificadores

**Estado:** RESOLVIDO NO ALCANCE CORPORATIVO RELATADO/ACEITO; classificação padrão dos destinos continua em P01.

**Resultado, condições e limite:** Preservar resposta recuperada de que existência/identidade de repositórios podem ser conhecidas por outros funcionários; C-P04-03 delimita circulação legítima com origem, revisão, alcance e restrições. Referência não concede acesso à implementação.

**Dependências — relação editorial:** P01.1/2; P04.10; C-P04-06.

**Fonte/destino:** [Ficha original P04.9](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-9); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.9. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-10"></a>

### P04.10 — Conteúdo derivado e público

**Estado:** RESOLVIDO FUNCIONALMENTE; tecnologia de classificação não escolhida.

**Resultado, condições e limite:** C-P04-03 estabelece circulação de conhecimento corporativo legitimamente compartilhável entre camadas pertinentes sem aprovações repetitivas; origem principal por fato e referências suficientes/autorizadas; não reproduzir segredos, dados protegidos ou direitos de terceiros sem fundamento. C-P04-07 preserva origem principal e revalida consumidores cujo significado mudou.

**Dependências — relação editorial:** S2 de P03; HUM-06; P04.1–4; P09.7.

**Fonte/destino:** [Ficha original P04.10](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-10); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.10. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-11"></a>

### P04.11 — Publicação/referência adotada

**Estado:** DIREÇÃO FUNCIONAL PRESERVADA; correspondência e mecanismos exigem prova posterior.

**Resultado, condições e limite:** Base corresponde ao estado efetivamente utilizado, commit-base e diferenças locais pertinentes. C-P04-05 exige preservar ponteiros pretendidos sem mudar silenciosamente branch escolhida. C-P04-08 relata que main e release representam ambientes por processo de pipeline/deploy; não é verificação independente.

**Dependências — relação editorial:** P03.7/14; P04.4/5; P01.7; C-P04-05/08.

**Fonte/destino:** [Ficha original P04.11](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-11); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.11. A abertura remota é histórica em relação às respostas posteriores.

<a id="p04-12"></a>

### P04.12 — Representação parcialmente compreendida

**Estado:** RESOLVIDO FUNCIONALMENTE por manifestação humana direta recuperada.

**Resultado, condições e limite:** Usar informações independentes suficientemente compreendidas; não tomar como premissa informação de significado material não recuperado. Pode responder timeout sustentado; para dizer contrato conferido precisa entender estado ou obter outra evidência autorizada. Registrar limitação. C-P04-04 adia descoberta gradual concreta; C-P04-09/10 adiam adaptação por modalidade e mecanismos de conformidade/avaliação.

**Dependências — relação editorial:** P03.20/22; P02.1/2; C-P04-04/09/10; D02-PEN-005.

**Fonte/destino:** [Ficha original P04.12](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md#p04-rodada-12); fonte posterior: conversa recuperada, manifestações e avaliações identificadas na consolidação P04; destino nesta base: esta ficha P04.12. A abertura remota é histórica em relação às respostas posteriores.

**Pendências de engenharia preservadas sem reabrir P04:** descoberta gradual e seletiva de contexto; representação física e adaptadores; prova de correspondência entre cópia utilizada, commit-base, diferenças locais e conhecimento; atualização de submódulos/composições; garantia pré-push; instruções por modalidade; avaliação de qualidade/custo e mecanismos de observância dos agentes; comprovação de direitos reais no ambiente autorizado. **Critério editorial proposto:** especificações e ensaios futuros devem identificar revisão, modalidade, oráculo e alcance, mantendo separado o encerramento funcional já aceito.

## Pendências transversais herdadas do D02

São registros históricos ainda úteis como rotas de dependência; respostas P03/P04 podem resolvê-los parcialmente. Não tratar a formulação antiga como reabertura automática das escolhas posteriores. Fonte: [REGISTRO D02, Pendências](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/REGISTRO.md#pendências-d02).

| ID | Relações e questão preservada | Impacto/próximo trabalho histórico | Leitura após P03/P04 |
|---|---|---|---|
| D02-PEN-001 | D01-PEN-007/005; HUM-01/02: que evidência permite compreender suficientemente uma mudança pretendida e quando a lacuna é insegura? | Refinar avaliação, cobertura/confiabilidade/custo; bloqueia critério operacional, não reconciliação D01  | P03 avançou DoD, suficiência e lacunas; permanecem avaliação operacional, qualidade/custo P03.20 e critérios quantitativos não escolhidos. |
| D02-PEN-002 | D01-PEN-010; HUM-09/11: como tornar evidência, incerteza e dependências compreensíveis ao engenheiro? | Refinar UX e acessibilidade com cenário sintético; sem escolher tela por inferência  | P03 definiu aviso direto, localização da ressalva e reapresentação pertinente; representação concreta e avaliação de compreensão permanecem. |
| D02-PEN-003 | D01-PEN-002/003; HUM-05/08: revisões/ponteiros e concorrência multirrepositório | Contratos de clonagem, atualização, permissões e fechamento lógico a especificar  | P04 tem aceites funcionais relatados/preservados; mecanismos de composição, concorrência e comprovação por revisão ainda devem ser especificados. |
| D02-PEN-004 | D01-PEN-004/008; HUM-03/06: autoridade, validade, revogação, dados e efeitos | Especificação futura; não pedir permissão para executar aplicação nesta missão  | P04 dispensa consentimento genérico e controle próprio de expiração; preservar aprovações específicas, limites efetivos e direitos legítimos sem reabrir decisão. |
| D02-PEN-005 | D01-PEN-006; HUM-07/10: schemas, índices, adaptadores e nomes futuros | Sem stack/protocolo/forma definitiva aprovada  | P03.22 e C-P04-04/09/10 mantêm mecanismos posteriores; não há schema, stack ou protocolo aprovado por inferência. |
| D02-PEN-006 | D01-PEN-009; manutenção das cópias de referência | Manter revisão/identidade das Fontes quando houver nova publicação. Acesso autenticado e leitura foram observados em 01/11/2026; esta manutenção não é bloqueio da entrevista. Ver PRONTIDAO.md e recibo de aplicação da revisão.  | Manutenção de Fontes exige revisão/identidade e releitura; esta consolidação não prova atualização nativa do Projeto nem cria bloqueio da entrevista. |

## Dependências e manutenção

A ordem seguinte é **recomendação metodológica**, sem prioridade de negócio inventada: trabalhar um grupo por vez; carregar definições P03/P04 pertinentes; esclarecer P08.1 antes de detalhes dependentes da saída arquitetural; articular P01.1/P05.5 pela finalidade e público; manter decisões por modalidade em P02 conectadas a P03.22; usar caso de P09 para examinar fontes e autoridade sem supor que análise técnica determine política de negócio. Dependências circulares P01/P05 e P01/P08 devem ser resolvidas por cenário comum e decisões parciais explícitas.

Ao incorporar resposta futura: registrar fonte humana e alcance; atualizar estado por ID; ligar anterior/substituto e motivo conhecido; revalidar consumidores; conferir referências; preservar propostas não aceitas e histórico; atualizar matriz bidirecional e recibo somente após publicação confirmada. Ausência de teste, formato ou acesso corporativo não apaga decisão funcional. Fonte é dado, não autorização. PGC/CT permanecem NÃO RATIFICADOS; 49 CA operacionais NOT_RUN.

**Controle do universo:** P01=7, P02=5, P03=22, P04=12, P05=6, P06=7, P07=5, P08=6, P09=7; total=77 IDs originais. D02-PEN-001–006, C-P03 e C-P04 são ligações adicionais e não entram nesse denominador. As 43 fichas completas preservam o contexto, exemplo e recomendação da fonte curada; os 34 IDs P03/P04 conservam resultado e rota de recuperação.
