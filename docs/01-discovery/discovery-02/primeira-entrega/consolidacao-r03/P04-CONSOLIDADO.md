# P04 — fechamento funcional e proveniência

Revisão R03, 13/11/2026. Base remota: `0cc6456fbd7613b9a4369d60684d0fe1170a2ed2`, PR #9. Esta revisão sobrepõe o estado de abertura da R02, preservada no histórico. Decisões funcionais não comprovam implementação nem autoridade corporativa.

## Fontes e alcance do fechamento

Fonte C1: conversa [Refinar PE03 questionar definition](chatgpt-conversation://6aefea59-1198-83ea-ade8-26c2c77da871). Localizadores estáveis são os IDs de mensagens abaixo; o acesso por outra conta não é garantido. As sínteses neste pacote permitem continuidade sem depender da conversa.

| Fonte | Autoria e conteúdo | Uso nesta revisão |
|---|---|---|
| C1-U1 `d51dfbcc-8bf9-47a7-8f6a-64d92fec52d1` | Usuário: respostas P04.7–12 | Histórico das autorizações abrangentes/permanentes, publicidade, estado Git e CLI |
| C1-A1 `ced5e8a2-47e0-4f64-a978-446f04ae3dac` | Assistente: avaliação das seis respostas; preserva aceites anteriores P04.1–6 | Proveniência indireta desses aceites, sem inventar suas mensagens humanas |
| C1-U2 `48789bb7-3e69-4a27-9186-770bf616ef99` | Usuário: descartar sistema de autorizações, publicidade corporativa, P04.11 seguir recomendação | Retificação intermediária, posteriormente delimitada por U3 |
| C1-A2 `b92f29c1-a41b-4086-81e2-824e09208195` | Assistente: análise intermediária | Perguntas residuais e recomendações, sem aprovação implícita |
| C1-A3 `d16a54a3-8da2-440c-ae39-ae07bed78dc1` | Assistente: inventário das pendências; recuperação limitada a 20.000 caracteres | Síntese explícita dos aceites P04.1–6 e P04.11; trecho final inacessível |
| C1-U3 `518d8f93-6536-4b3b-a49d-86faf5033896` | Usuário: dez colaterais C-P04-01..10 e P04.12 | Fonte humana direta das onze manifestações finais |
| C1-A4 `77c13e72-9c9d-452e-ba23-4df24bb815a5` | Assistente: avaliação final e encerramento P04 | Parecer de Discovery e propostas de cenários; não aceite humano separado |

O serviço retornou cinco turnos e `hasMore=false`, sem cursor para mensagens anteriores. P04.1–5 têm aceites anteriores expressamente relatados pelo assistente, mas suas respostas humanas originais não estão nesta recuperação. Isso é uma lacuna de proveniência, não justificativa para reabrir as decisões. P04.6 tem ainda suporte no P03/S2. O parecer de 12/12 funcionalmente respondidas é preservado com essa qualificação. Não é alegado confronto literal integral da entrevista.

## Saldo das doze perguntas

As perguntas, os contextos e exemplos originais permanecem nas [fichas R02](https://github.com/lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide/blob/0cc6456fbd7613b9a4369d60684d0fe1170a2ed2/docs/01-discovery/discovery-02/primeira-entrega/refinamentos/P04-ATUALIDADE.md). Cada linha abaixo aponta ao ID de origem e a seu resultado; a matriz inversa está em [RASTREABILIDADE](RASTREABILIDADE.md).

| ID | Definição consolidada e condições | Evidência e maturidade |
|---|---|---|
| P04.1 | Reaproveitar conhecimento cuja validade permaneça demonstrável para a nova revisão; investigar alterações e dependências afetadas. Economia de trabalho não permite presumir validade porque um arquivo ficou igual. Alcance incremental e métodos ainda precisam de demonstração. | C1-A3, aceite anterior relatado; HUM-08; engenharia posterior |
| P04.2 | Ao detectar mudança, impedir o uso como atual das afirmações afetadas e das conclusões dependentes; preservar informação independente. Registrar impacto indireto incerto e destino inacessível, sem alegar atualização nele. | C1-A3, aceite anterior relatado; HUM-08 |
| P04.3 | Restabelecer a validade somente por evidências pertinentes à afirmação e ao estado estudado. Código pode sustentar comportamento previsto; ocorrência executada exige sua evidência. Parte inconclusiva conserva ressalva. | C1-A3, aceite anterior relatado; HUM-08 |
| P04.4 | Distinguir atualização individual Micro de composição Micro/Meso/raiz. Identificar revisões e ponteiros, manter composição anterior identificada, registrar falha e retomar a etapa incompleta. Corrigir raiz se significado ou referência forem afetados. Não prometer atomicidade física. | C1-A3, aceite anterior relatado; D02-RET-004; U3/C-P04-05 reforça correspondência |
| P04.5 | Quando a base mudar, reexaminar o significado das contribuições antes de incorporar. Reler revisão vigente, aproveitar partes independentes verificadas, preservar divergências que a evidência não resolve. Ausência de conflito textual não prova compatibilidade semântica. | C1-A3, aceite anterior relatado; P03/S1/S3 |
| P04.6 | Esclarecimento reutilizável preserva fonte, natureza, revisão, condição e público. Para novo entendimento, pedido único ao Analista com entendimento, origem, destino e efeito; silêncio gera pendência, negativa descarta aquele destino. Correção inequívoca segue S1. | P03/S2, C1-A1/A3/A4; U3/C-P04-01 mantém aprovações específicas |
| P04.7 | Eliminar consentimento genérico adicional para ler fontes internas já legitimamente acessíveis. Manter aceites específicos de decisões humanas, operações sensíveis e alterações já expressamente definidas. Não derivar direitos de uma cópia disponível. | U3/C-P04-01, decisão direta; substitui leitura absoluta de U2 |
| P04.8 | Dispensar controle próprio de expiração; reconhecer restrições reais encontradas. Conhecimento pode permanecer quando conservação e distribuição continuam legítimas; perda de fundamento impede uso da cópia. Ausência de expiração não é irrevogabilidade. | U3/C-P04-02, decisão direta; delimita U1/U2 |
| P04.9 | Aceitar publicidade corporativa da existência e identidade dos repositórios; leitura do índice não cria acesso ao destino. Classificação padrão de Workspaces/mapas permanece em P01. | U2/P04.9 e U3/C-P04-03; decisão direta |
| P04.10 | Circulação legítima entre camadas como padrão, sem aprovações repetitivas; origem principal por fato, preferir referências suficientes e autorizadas, proteger segredos/dados/direitos de terceiros, conservar origem/revisão/alcance/restrições conhecidas. | U3/C-P04-03/07, decisão direta; delimita 'sem limitações' de U2 |
| P04.11 | Conhecimento reflete estado efetivamente usado: branch, commit-base e alterações locais pertinentes. Cada atividade mantém revisão/composição escolhida, sem promoção silenciosa de outra branch. Preservar ponteiros pretendidos dos submódulos. | U1/P04.11, U2/P04.11 aceita recomendação; A3 e U3/C-P04-05/08 |
| P04.12 | Usar informações independentes suficientemente compreendidas. Nunca usar como premissa informação de significado material não recuperado; buscar outra evidência autorizada ou apresentar limitação e suspender conclusão dependente. | U3/P04.12, decisão direta; não confundir Git atualizado e compreensão |

## Onze manifestações finais e destinos

IDs abaixo são qualificados por **U3**. Isso evita colisão com a avaliação A1, na qual **C-P04-04** nomeava adoção entre branches; em U3, o mesmo rótulo nomeia descoberta de contexto. São assuntos diferentes. Adoção de revisão mantém seu destino P04.11. Nenhum ID histórico foi apagado ou renumerado silenciosamente.

| Unidade | Decisão, condição e encaminhamento | Destinos e dependências |
|---|---|---|
| U3/C-P04-01 | A frase intermediária 'descartar sistema de autorizações' é delimitada: remover apenas consentimento genérico para leitura interna acessível. Preservar aprovações específicas existentes. | P04.7, P03/S1/S2, HUM-06/09, PE-01/06 |
| U3/C-P04-02 | Sem gerenciador próprio de expiração. Reconhecer perda efetiva de acesso e legitimidade de retenção/distribuição. Não continuar usando apenas porque existe cópia. | P04.8, D02-PEN-004, PE-01 |
| U3/C-P04-03 | Compartilhar legitimamente entre camadas sem repetição de aprovação; origem principal, referência preferida quando suficiente/autorizada, respeito a dados e direitos, proveniência preservada. Tecnologia de classificação não escolhida agora. | P04.9/10, C-P03-02, P01/P03.22 |
| U3/P04.12 | Timeout compreendido pode sustentar resposta independente; contrato incompreendido não pode ser declarado conferido. Obter evidência autorizada alternativa ou explicitar limitação. | P04.12, P03.11/13/19, PE-02/04 |
| U3/C-P04-04 | Ao iniciar agente na pasta da Plataforma, não ler automaticamente bases de todos os repositórios, Siglas, Macro, Workspaces, arquitetura e negócio. Refinar depois descoberta gradual, dirigida e otimizada para evitar contexto excessivo, custo e imprecisão. | P03.22, PE-02, P01.4, PE-07/08/09 |
| U3/C-P04-05 | Engenharia deve demonstrar correspondência entre estado usado, commit-base, diferenças locais e conhecimento; atualização de submódulos preserva ponteiros/composição e não muda branch silenciosamente. | P04.4/11, P03.7, D02-PEN-003, PE-01/04 |
| U3/C-P04-06 | Distinguir falta de acesso direto, falta de onboarding, referência indireta e conhecimento histórico legítimo. Não baixar C não significa inexistir informação sobre C. | P03.6/9, P04.7/12, HUM-06 |
| U3/C-P04-07 | Manter uma origem principal por fato e referências ou derivados verificáveis. Mudança de significado exige revalidar consumidores afetados conforme P04.1–4. | C-P03-02, P04.1–4/10, HUM-08 |
| U3/C-P04-08 | Relato humano: modificações chegam à main após pipeline que efetivamente faz deploy em PROD; processo correspondente nas releases/HOM. Adotar convenção no universo relatado, mantendo commit exato. | P03.14/P04.11; natureza RELATO, inspeção corporativa posterior |
| U3/C-P04-09 | CLI local é referência concreta; Web/Desktop não presumem mesma cópia nem contexto automático. Comportamento funcional comum e máxima agnosticidade/flexibilidade, com particularidades de cada ferramenta. | PE-02/P02, P03.22, D02-PEN-005 |
| U3/C-P04-10 | Reservar cenário para qualidade: resultados esperados, recuperação de evidência, lacunas e custo por modalidade. Mecanismos de cumprimento de restrições/princípios/instruções por todos os agentes serão definidos posteriormente. | P03.20/C-P03-07, PE-02/04/07, avaliação futura |

## Evolução e conflitos resolvidos

U1 pretendia autorização para três usos e permanência; U2 propôs eliminar o sistema por considerar as fontes já acessíveis; U3 esclarece que se trata da consulta genérica e conserva os aceites específicos. Não apagar U1/U2, nem interpretar U3 como permissão operacional ampla. O pedido S2 para incorporar novo entendimento não foi abolido.

U2 aceitava publicidade e dizia não haver limitações naquele momento; U3 define o alcance legítimo, protege dados e terceiros e preserva origem. Isso resolve a aparente contradição de compartilhamento irrestrito. Autorizar leitura, conservar derivado, redistribuir e escrever continuam objetos distinguíveis, sem consentimentos genéricos repetidos.

U1 explicava estado local por Git; U3/P04.12 distingue compreensão semântica e atualização. U3/C-P04-05 liga o conhecimento à composição efetivamente usada, sem troca de branch silenciosa. U3/C-P04-08 esclarece a convenção branch/ambiente; não prova pipeline examinada, artefato implantado, configuração externa ou ocorrência específica. Por exemplo, timeout definido no código pode ser substituído por variável de ambiente: afirmar seu valor efetivo requer a fonte pertinente. Esse exemplo é ilustração editorial, não fato adicional do banco.

Não há conflito funcional novo demonstrado que exija repetir a entrevista. Permanecem a lacuna de fonte original de P04.1–5, o trecho truncado A3 e os mecanismos explicitamente futuros. Fechar funcionalmente P04 não fecha P01/P02/P03.20/P03.22/PE-04 nem os outros grupos por analogia.

## Critérios candidatos para avaliação futura

Estes são oráculos editoriais, não novos aceites nem testes executados: consulta interna ordinária sem consentimento genérico; incorporação S2 com objeto/destino/efeito aceitos; inicialização sem carga indiscriminada; contrato incompreendido sem afirmação positiva de conferência; resposta independente sobre timeout sustentada; Micro atualizado com composição ainda antiga devidamente identificada; revalidação semântica após contribuição concorrente; acesso direto ausente com referência indireta legítima reconhecida; referência main/PROD e release/HOM atribuída ao relato com commit exato. Métodos, limiares, responsáveis e custo continuam postergados em P03.20/C-P03-07 e C-P04-10.

Rota de manutenção: registrar nova manifestação com ID e autoria; qualificar rótulos reutilizados; atualizar unidade, saldo da pergunta, dependências e matriz inversa; conservar formulação anterior; auditar candidato congelado; publicar por revisão verificável e emitir recibo. Não adotar recomendação porque outro agente a repetiu.
