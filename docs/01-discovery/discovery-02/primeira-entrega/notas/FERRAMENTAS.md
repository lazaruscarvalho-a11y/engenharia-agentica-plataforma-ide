# Devin e Claude Code na primeira entrega do Motor

**Revisão 1 · Decisão de escopo em Discovery.** As ferramentas de IA da primeira entrega do Motor de Onboarding serão **Devin**, nas modalidades **Web, CLI e Desktop**, e **Claude Code**. Segundo o usuário, são as duas ferramentas utilizadas com mais frequência e consistência na empresa. O panorama anterior incluía também o GitHub Copilot. A decisão atual retira o suporte específico ao Copilot da primeira entrega e deixa sua eventual inclusão para outro momento.

## Agnosticidade e configurações específicas

Tudo o que for construído deve permanecer agnóstico e independente de ferramenta ou plataforma. As bases de conhecimento Micro e Meso, por exemplo, devem continuar utilizáveis se a equipe mudar de ferramenta. Ao mesmo tempo, a plataforma deve aproveitar ao máximo as capacidades próprias de Devin e Claude Code. O usuário citou as pastas `.devin` e `.claude` na raiz dos repositórios como exemplos de configurações que podem melhorar o uso de cada ferramenta.

O recorte define quais ferramentas receberão suporte. A escolha dos recursos de cada modalidade, o conteúdo das configurações e as operações autorizadas para criá-las ou atualizá-las nos repositórios ficam para especificação. A primeira entrega do Motor continua voltada à obtenção e análise dos repositórios indicados pelo engenheiro e à produção das bases Micro e Meso.

## Comportamento ao iniciar a plataforma

A cada inicialização na máquina de trabalho, a plataforma deve providenciar o download ou a atualização de Devin e Claude Code, conforme necessário para utilizar a última versão de cada ferramenta. O usuário relata que o ambiente corporativo já possui estruturas para cuidar da obtenção dessas ferramentas. A forma de iniciar a plataforma, as origens dos downloads e o procedimento de distribuição ficam para outro momento.

## Pontos para o próximo Discovery deste tema

- Identificar, separadamente para Devin Web, CLI, Desktop e Claude Code, os recursos que a primeira entrega deverá aproveitar e como verificar que funcionam com as bases do Motor.
- Especificar como cada ferramenta encontra o conhecimento comum e quais configurações próprias são úteis. Definir quando e sob quais permissões preparar essas configurações na raiz dos repositórios.
- Definir como reconhecer a versão efetivamente em uso em cada modalidade, inclusive no acesso via Devin Web, e o comportamento quando a atualização ou a verificação de versão não for possível. Quando um impedimento for percebido, aplica-se a direção de catalogá-lo e apresentá-lo ao usuário o mais brevemente possível.

## Origem e continuidade

A fonte desta decisão é a manifestação direta do usuário iniciada por “Quero diminuir o escopo da primeira entrega”. O histórico das ferramentas e de suas particularidades está em `02_ferramentas_de_ia.md`, na revisão R06 do acervo. [Síntese do acervo R06](../evidencias/WORKSPACE-R06.md)

A direção de portabilidade está em AX-10. A delimitação anterior da primeira entrega do Motor está na continuidade de D02. [AX-10 — Agnosticidade](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/8bbd93151640865995fa8a8dfe3d2d5db15da6ec/docs/fundacao/axiomas-arquiteturais.md#ax-10) · [Retomada do Motor](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/766f3323997e1cc4ae1fff7fc2bf31ce3ccd1455/docs/01-discovery/discovery-02/RETOMADA-MOTOR-E-ARQUITETURA.md)
