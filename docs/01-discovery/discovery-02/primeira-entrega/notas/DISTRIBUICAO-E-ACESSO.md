# Distribuição da raiz da Plataforma e acesso aos contextos de trabalho

**Revisão 3 · Fluxo aceito em Discovery.** A primeira entrega distribui a raiz comum pelo GitHub. Ao iniciar, o usuário atualiza essa raiz. Ao abrir um Workspace, a Plataforma busca os repositórios pertinentes com a credencial do usuário e informa quais foram carregados, em que revisão e onde faltou acesso. O modelo de extensões locais abrange skills, instruções, comportamentos, documentação e MCPs acrescentados depois do onboarding. [Extensões por escopo](EXTENSOES-POR-ESCOPO.md)

**Origem e alcance do aceite.** A revisão 2 preservava a distribuição como proposta. Após discutir submódulos aninhados `internal` e `private` e a separação entre atualizar a raiz e abrir uma atividade, o usuário declarou nesta conversa: “Tudo isso é aceitável para mim. Estou de acordo”. O aceite abrange o fluxo funcional e os efeitos de visibilidade descritos. A visibilidade padrão dos repositórios de Workspaces continua em aberto.

## Modelo de acesso relatado pelo usuário

A Sigla é a unidade de concessão de acesso em cada serviço. Quem recebe o acesso GitHub de uma Sigla tem acesso a todos os repositórios dela. Segundo o usuário, um repositório `internal` pode ser visto por toda a empresa, inclusive por pessoas de outras Siglas. O acesso AWS também é concedido por Sigla, como acesso próprio desse serviço. A visibilidade de um repositório informa quem pode lê-lo. As operações de escrita no GitHub e as ações permitidas na AWS dependem dos acessos efetivos nos respectivos serviços.

**Retificação da revisão 1.** No exemplo anterior, um engenheiro podia ter o acesso GitHub da Sigla e, ainda assim, ler apenas alguns de seus repositórios Micro. O esclarecimento substitui essa hipótese pelo acesso ao conjunto completo de repositórios da Sigla. Um colaborador de outra Sigla pode, por sua vez, ler os repositórios `internal` sem receber o acesso GitHub da Sigla proprietária.

## Fluxo de distribuição aceito

1. Na primeira utilização, o engenheiro obtém uma cópia local do repositório comum com `git clone`.
2. Os mantenedores publicam uma revisão na `main` pelo fluxo de contribuição autorizado. Cada instalação recebe as mudanças quando atualiza sua cópia, por exemplo com `git pull`. A publicação no remoto e a atualização de cada máquina são eventos distintos.
3. Ao iniciar, o usuário atualiza a raiz comum independentemente da disponibilidade de um repositório privado de outra atividade. O conteúdo comum pode incluir configurações como `.claude/`, `.devin/` e `.skills/`, instruções, documentação e os componentes de instalação e atualização das ferramentas. Devin e Claude Code têm escopo de suporte já definido. RTK, Caveman e Context-Mode foram citados como exemplos. O download e a atualização das ferramentas constituem uma operação própria. O mecanismo de inicialização e atualização segue em refinamento.
4. Ao abrir a atividade, a Plataforma identifica as dependências pertinentes e busca a revisão referenciada de cada repositório autorizado. Se uma dependência estiver inacessível, informa a lacuna e a cobertura obtida. O trabalho que independe dessa lacuna pode prosseguir. Uma tentativa recursiva de Git pode terminar com erro após baixar apenas parte da árvore. O resultado apresentado ao usuário precisa distinguir os repositórios carregados, suas revisões e os acessos ausentes.

[GitHub — clonar um repositório](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) · [GitHub — obter mudanças do remoto](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository) · [Escopo de ferramentas](FERRAMENTAS.md)

## Proposta de organização e leitura

A área local pode apresentar recursos de vários repositórios sob a mesma raiz. O repositório de distribuição deve conter apenas material apropriado a todos os seus leitores. As permissões remotas devem ser verificáveis mesmo quando a pessoa acessa o GitHub diretamente. A composição física da raiz local, do clone comum e do Macro Git continua em aberto.

| Escopo | Tratamento proposto para distribuição e acesso |
|---|---|
| Distribuição | Manter componentes e configurações comuns. Um `pull` desse repositório atualiza esses arquivos. Cada contexto de trabalho conserva sua origem. |
| Workspace | A R06 prevê uma branch por Workspace no repositório da Sigla executora destinado aos Workspaces. Se esse repositório for `private`, todos os usuários com acesso GitHub à Sigla podem ler as atividades ali versionadas. Se for `internal`, o público de leitura alcança toda a empresa. Em cada caso, o mesmo público pode ler o material arquivado em `workspaces/` na `main` desse repositório. |
| Sigla e aplicação | Preservar a topologia Macro → Meso → Micro com submódulos. O acesso GitHub da Sigla abrange seus repositórios Meso e Micro. Ao referenciar outra Sigla, considerar o acesso GitHub a ela e a visibilidade `private` ou `internal` do repositório referenciado. |
| Arquitetura | Um mapa que descreve várias Siglas fica visível aos leitores do repositório onde for publicado. Uma referência a uma aplicação privada de outra Sigla permite encontrar a referência, mas a leitura do código exige acesso ao repositório de destino. |
| Extensões do repositório | O MCP do IBM ODM e as instruções sobre seu uso continuam associados ao repositório integrador. Um Workspace autorizado pode localizar essas orientações pela dependência da atividade. O uso efetivo do MCP depende também das permissões para a operação no ODM. |

As branches isolam o contexto de trabalho e podem ter proteções para alteração e integração. A leitura acompanha o público do repositório. Se viesse a existir uma exigência de leitura exclusiva pelos participantes de uma atividade, criar outro repositório sujeito à mesma concessão geral da Sigla manteria o mesmo público. O usuário descreveu o acesso por Sigla e por serviço. Nenhuma exceção para participantes de um Workspace foi definida. [GitHub — papéis por repositório](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization) · [GitHub — proteção de branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

O repositório pai de um submódulo registra caminho, origem e revisão. Mesmo quando o destino é privado, esses metadados podem ser lidos no pai. Isso também vale para o conteúdo copiado para um índice ou documentação de arquitetura. A escolha do que publicar em cada camada deve considerar quem poderá descobrir a existência do recurso, ler seus detalhes e consultar o conteúdo de origem. [Git — submódulos](https://git-scm.com/docs/gitsubmodules)

Por exemplo, o leitor de um Workspace `internal` pode ler os requisitos ali versionados e a referência a uma aplicação `private`. Para baixar a aplicação, precisa de acesso a ela. No sentido inverso, se o Workspace for `private` e inacessível ao usuário, a busca por esse caminho para no Workspace. Uma aplicação `internal` apontada por ele ainda pode ser consultada diretamente por quem conhece sua origem e tem acesso. A revisão usada por aquele Workspace só pode ser conhecida a partir de uma fonte autorizada que a identifique.

## Decisão de produto pendente

**Qual visibilidade adotar para o repositório de Workspaces da Sigla executora?** O efeito de cada escolha sobre a leitura já está esclarecido. A classificação padrão (`private` ou `internal`) e os critérios para eventuais exceções permanecem para decisão de produto conforme as políticas corporativas. O mesmo cuidado vale para escolher onde publicar o mapa de uma arquitetura entre Siglas. A finalidade já definida de consultar outro Workspace para histórico ou entendimento continua sujeita às permissões efetivas.

A R06 trata da localização e do ciclo de vida dos Workspaces. A retomada D02 distingue o contexto comum da raiz, o Macro e a base de arquitetura. [Síntese do acervo R06](../evidencias/WORKSPACE-R06.md) · [Retomada do Motor e da Arquitetura](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md)
