# Inicialização do Projeto no ChatGPT

Versão 0.1.0 — preparação PM-FUND-003. **Estado da configuração real: NÃO CONFIGURADO.** Preparação documental não é configuração nativa.

## Evidência de acesso nesta missão

O inventário de Projetos acessível pelo aplicativo retornou apenas um projeto não relacionado, “Ateliê Personagens”. Não há ferramenta habilitada para criar/editar as Instruções e Fontes de um Projeto ChatGPT. O navegador aberto em `https://chatgpt.com/` exibiu “Entrar”/“Cadastre-se”, sem autenticação disponível. A UI nativa do ChatGPT desktop não foi automatizada. Não foi criado Projeto substituto em Pages/Space, pois isso não comprovaria a configuração solicitada.

Portanto: Instruções PREPARADAS, Fontes PREPARADAS, upload NÃO EXECUTADO, releitura no Projeto NÃO EXECUTADA. Nenhum recibo de configuração foi preenchido como sucesso.

O pacote de entrega contém três Fontes consolidadas, Instruções separadas e manifesto com hashes por arquivo e commit. Sua geração exige `harness/empacotar_chatgpt.py --commit SHA --snapshot-remoto MANIFESTO --saida PASTA_NOVA`. A coordenação obtém o manifesto por consulta remota ao commit imutável; a ferramenta offline compara todos os bytes ao manifesto e usa exclusivamente os bytes conferidos. Ela não autentica a origem do manifesto nem concede autoridade. Faltas ou divergências impedem a geração; os oito contratos são obrigatórios.

## Passos mínimos quando houver acesso autenticado

1. Abrir ou criar o Projeto destinado à Plataforma/IDE no ChatGPT; sugestão de nome: “Plataforma/IDE de Engenharia Agêntica”. Confirmar o destino antes de adicionar arquivos. Não precisa iniciar novas missões de implementação.
2. No campo Instruções do Projeto, colar integralmente o conteúdo de [INSTRUCOES-PERMANENTES.md](INSTRUCOES-PERMANENTES.md).
3. Em Fontes, carregar o pacote curado correspondente ao commit/recibo de entrega, conforme [MANIFESTO-FONTES.md](MANIFESTO-FONTES.md). Se houver integração autorizada ao GitHub, conferir sua disponibilidade e versão; link isolado não comprova conteúdo recuperável.
4. Abrir a primeira conversa dentro do Projeto e usar a abertura em [PRIMEIRA-SESSAO.md](PRIMEIRA-SESSAO.md). O discovery exploratório já pode começar na conversa atual, com os artefatos efetivamente acessíveis, sem supor a configuração concluída.

Essa intervenção é de acesso/configuração nativa. Merge em main e ratificação do PGC são decisões separadas e não são pré-requisitos para conversar sobre discovery C0/C1 sem efeito normativo.

## Verificação após configuração

Sem antecipar respostas, pedir à nova conversa que identifique, consultando as Fontes: produto/fase atual; distinção entre relato corporativo e requisito desejado; metodologia e próximos passos; status do PGC e limites de escrita; versão/commit das fontes. Solicitar referências aos documentos, não concordância com resumo fornecido.

Registrar Projeto alvo, instruções aplicadas, nomes/versões das Fontes, commit/hash do pacote, acesso real e resultado. Se houver fonte obsoleta, ausente ou não recuperável, corrigir e repetir apenas a verificação afetada. Recuperação em processo isolado ou agente novo é prova técnica separada, não prova de configuração nativa nem de memória entre chats.
