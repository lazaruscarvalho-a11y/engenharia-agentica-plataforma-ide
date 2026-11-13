# Rastreabilidade bidirecional e manutenção R03

## Universo e classes

O inventário de 40 fontes identifica 37 documentos textuais por SHA imutável, dois PDFs locais com identidade Git e um oráculo operacional de continuidade herdado. A conversa tem cinco turnos retornados, quatro mensagens humanas textuais pertinentes e uma mensagem de anexo; a análise A3 está truncada. O pedido atual e o Prompt-Master delimitam a missão. A recuperação não equivale a toda a história do Projeto.

[UNIDADES.json](UNIDADES.json) preserva 77 perguntas originais com trecho e fonte por âncora, 30 saldos P03 (22 perguntas e oito colaterais), 23 registros P04 (doze perguntas e onze manifestações finais) e onze HUM: **141 registros**, sem IDs duplicados. Esses números contam unidades catalogadas, não porcentagem de cobertura do projeto. Os sete critérios DoD, S1/S2/S3, seis RET, contextos e cenários têm definição detalhada em BASE-P03-HUM. As 43 fichas fora P03/P04 preservam pergunta, contexto, exemplo e recomendação; critérios editoriais novos estão rotulados como propostas.

Uma PERGUNTA_HISTORICA não determina sozinha seu saldo atual. Consultar o status e o destino consolidado; as unidades `R03/P03.*`, `R03/P04.*` e `R03/U3/*` guardam o resultado posterior. A ausência das mensagens humanas iniciais do P04 não foi convertida em pendência funcional nova.

## Fonte para destino e destino para fonte

| Fonte/unidades de origem | Destinos principais | Conferência inversa e efeito |
|---|---|---|
| CADERNO-ED11, P01.1–7, P02.1–5, P05.1–6, P06.1–7, P07.1–5, P08.1–6, P09.1–7 | PENDENCIAS-P01-P09, 43 fichas, âncora por ID; UNIDADES | Cada ficha aponta à mesma âncora Git por SHA. Recomendações continuam propostas; não fechar grupos por analogia |
| CADERNO/P03-CONHECIMENTO, P03.1–22, C-P03-01–08 | BASE-P03-HUM, PENDENCIAS, UNIDADES | Tabelas mantêm IDs, origem por edição e condições. Direção P03.22 e adiamento P03.20 não desaparecem sob o rótulo 'encerrado' |
| P03 DoD edição 8, S1/S2/S3 edições 9–10, catálogo da raiz e pré-push | BASE-P03-HUM; CONTINUIDADE; ESCOPO-INTEGRADO | Resultado deve voltar à fonte/edição. Produtor distinto de consumidor; confirmação não extrapola objeto, destino ou efeito |
| P04-ATUALIDADE R02, P04.1–12 | P04-CONSOLIDADO e PENDENCIAS | Origem contém perguntas e propostas de abertura. Saldo posterior vem de mensagens recuperadas e não da recomendação isolada |
| C1-A1/A3/A4, notícia dos aceites P04.1–5 | P04-CONSOLIDADO, saldo PENDENCIAS | Fonte indireta preservada; mensagens humanas originais não recuperadas. P04.6 também tem apoio P03/S2 |
| C1-U1, respostas P04.7–12 | P04-CONSOLIDADO, histórico U1 | Autorizações amplas/permanentes, publicidade, estado Git e cenário CLI; ler retificações U2/U3 |
| C1-U2, P04.7–11 | P04-CONSOLIDADO, histórico U2 | Proposta humana de eliminar sistema posteriormente delimitada; publicidade corporativa; aceite de recomendação P04.11 |
| C1-U3, C-P04-01–03 | P04.7–10; HUM-06 delimitado; P03/S2 preservado | Fonte humana direta elimina consentimento genérico e preserva decisões/ações sensíveis; retenção/distribuição legítimas |
| C1-U3, P04.12 | P04.12; PE-02/04; critérios candidatos | Informação independente compreendida utilizável; nenhuma afirmação de contrato conferido sem significado/evidência |
| C1-U3, C-P04-04 | P03.22, P01.4, P02, contexto gradual | Rótulo foi reutilizado: A1/C-P04-04 era adoção entre branches; conservar qualificação da rodada |
| C1-U3, C-P04-05/07 | P04.1–4/10/11; HUM-08; D02-PEN-003 | Correspondência código/base/ponteiros e revalidação dos consumidores; mecanismos futuros |
| C1-U3, C-P04-06 | P03.6/9, P04.7/12 | Quatro estados: sem acesso direto, sem onboarding, referência indireta, conhecimento histórico legítimo |
| C1-U3, C-P04-08 | P03.14/P04.11; ESCOPO-INTEGRADO | Relato contextual de pipeline e branch/ambiente. Nenhuma comprovação de implantação inferida |
| C1-U3, C-P04-09/10 | P02, P03.20/22, C-P03-07, PE-04/07 | Agnosticidade funcional com particularidades; avaliação e mecanismos postergados |
| C1-A2/A3/A4, análises e cenários | P04-CONSOLIDADO, histórico, limitações e oráculos candidatos | Avaliação não vira manifestação humana; critérios continuam candidatos sem resultado executado |
| REGISTRO D02 HUM-01..11; RET-001..006 | BASE-P03-HUM; CONTINUIDADE | Naturezas distintas preservadas: HUM-06/09 sínteses, HUM-10 proposta, HUM-11 síntese de limites; exceção futura não executável nesta missão |
| ESCOPO PE-01..09 e cenários C01..C08; cinco notas e R06 | ESCOPO-INTEGRADO; PENDENCIAS; CONTINUIDADE | Não confundir necessidade e desenho escolhido. R06 prevalece sobre estado próprio do Workspace antes aberto |
| MODELO-FUNCIONAL, CONTRATOS-CANDIDATOS, AVALIACAO, MATRIZ | ESCOPO-INTEGRADO; BASE-P03-HUM; FONTES | Projeções e contratos propostos preservados por referência; DoD P03 posterior corrige alcance do produtor |
| PDF Motor r1 e diagrama r2 | ESCOPO-INTEGRADO; histórico de precedência | Representações históricas não reabrem P03.21/DoD nem encerram Arquitetura/Negócios |
| ESTADO/RETOMADA/MANIFESTOS D02/R01/R02 e continuidade | FONTES; CONTINUIDADE; MANIFESTO-R03 e recibo posterior | Revisões e provas por snapshot. R03 tem manifesto próprio, sem certificar de novo o acervo |
| Visão, roteamento, axiomas e auditoria da fundação | README; BASE-P03-HUM; ESCOPO-INTEGRADO; FONTES | Visão completa e primeira entrega distintas. Evidência histórica de harness não comprova IDE ou 49 CA |

## Histórico e dependências transversais

| Mudança | Antes | Depois e consumidores |
|---|---|---|
| DoD produtor | Rodadas anteriores/modelo candidato vinculavam objetivo particular ou êxito de consulta | P03 edição 8 fixa cobertura/proveniência/integridade e sete critérios; PE-03/04 e avaliação precisam usar esse alcance |
| Workspace | Adendo anterior deixava estado próprio a especificar | R06 define conteúdo e ciclo de vida; PE-05/06, P01 e retomada devem distinguir fim do refinamento e da atividade |
| Consentimentos | HUM-06 herdado e U1 tratavam autorizações reutilizáveis/permanentes; U2 dizia descartar sistema | U3 dispensa genérico para leitura acessível e conserva aprovações específicas; afeta P01/04, S2, HUM-06/09 |
| Circulação | U2 dizia ausência de limitações | U3 fixa legitimidade, origem principal, referências e direitos; afeta todas as camadas |
| Branch/ambiente | Regra contextual em P03.14, questionamento posterior de suficiência | U3/C-P04-08 explica pipeline relatada; seleção está esclarecida, prova operacional permanece distinta |
| P04.12 | Cenário CLI/Git atualizado era resposta insuficiente à incompreensão | U3 permite uso independente e restringe conclusão de significado não recuperado; P02/P03.20/22/PE-04 |
| Contexto | Inicialização poderia ser lida como carga geral | U3/C-P04-04 rejeita carga indiscriminada; mecanismo gradual posterior, sem reabrir decisão |

Dependências metodológicas, não prioridades de negócio: P08.1 antecede armazenamento/publicação de mapas; P09 precisa de pergunta/fonte/autoridade antes de estrutura; P02, P03.22 e P07 exigem refinamento conjunto de formatos e descoberta; P01/P04 sustentam acesso/composição de P05/P06. S2 e direitos efetivos atravessam as frentes, sem autorização bancária implícita.

## Regra para próximas alterações

Nova resposta deve atualizar: unidade/estado → ficha e decisão principal → consumidores da matriz → histórico de substituição → fontes e manifesto → auditoria do candidato → recibo remoto. Uma referência pode bastar onde o significado já está integralmente disponível e autorizado; duplicação não cria segunda origem principal. Conflito material sem retificação suficiente conserva versões e pendência. Esta regra é processo editorial de manutenção desta base, não um algoritmo implementado na futura IDE.
