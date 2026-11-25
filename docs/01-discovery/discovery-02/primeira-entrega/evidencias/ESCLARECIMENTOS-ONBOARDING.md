# Onboarding com ressalvas e comunicação de lacunas

Este registro reúne os esclarecimentos dados pelo usuário durante o Discovery da primeira entrega. Os dois casos abaixo são sintéticos. O aceite registrado se refere ao comportamento desejado do produto nesses casos. Os exemplos não correspondem a um teste executado, a uma observação de aplicação do banco ou a uma autorização de mudança. [Escopo da primeira entrega](../ESCOPO.md) · [Índice do pacote](../README.md)

## O que o usuário aceitou

**Nos dois casos, A pode concluir seu onboarding com ressalva**, desde que todas as dúvidas, lacunas, pendências e insuficiências percebidas fiquem bem definidas, localizadas, detalhadas e referenciadas no próprio repositório A. O usuário deu o aceite durante a discussão dos cenários. Cabe ao agente preservar o objeto, o alcance e as condições desse aceite ao reutilizar a decisão.

| Cenário sintético | O que as fontes sustentam | O que continua em aberto e que ação depende da resposta |
|---|---|---|
| A envia `codigoSegmento` para B e C | Há evidências da emissão do campo por A e do tratamento observado em B. A relação com C é visível do lado de A. | Falta evidência de que C aceite a ausência do campo. Registrar a ressalva em A permite concluir seu onboarding. Retirar o campo exige investigar o contrato ou o comportamento pertinente de C. O que se observou em B, isoladamente, não confirma o que C faz. |
| Duas regras em A calculam o segmento | Foram encontradas uma regra a partir do cadastro e outra a partir da proposta. É possível registrar ambas, com as referências em A. | Continua incerto quando se aplica cada regra. Inferir a precedência a partir de seus nomes faria uma hipótese parecer uma regra comprovada. O aceite de A com ressalva conserva essa dúvida. Alterar a seleção entre as regras depende de evidência própria. |

O agente separa o comportamento **observado** na revisão examinada, a **inferência** que ainda carece de confirmação e a **ação** cuja segurança depende da resposta. A conclusão do onboarding de A pode coexistir com um impedimento para uma ação posterior específica. O aceite não se estende por analogia a qualquer repositório, pendência ou alteração.

## Quando comunicar e quando reapresentar

Ao perceber uma dúvida, lacuna, pendência, insuficiência ou incoerência, o agente a cataloga e a apresenta ao usuário **o mais brevemente possível**. Indica onde encontrou o problema, que parte está sustentada pelas fontes e o que ainda precisa ser esclarecido. A investigação autorizada pode prosseguir enquanto o impacto é precisado. O primeiro aviso não depende de já se conhecer a lista completa de atividades afetadas.

Quando o agente percebe que uma história depende da lacuna, sinaliza o vínculo no Workspace. Ao refinar essa história, responder a uma pergunta ou trabalhar em outra atividade, deve voltar a apresentar a ressalva quando houver **dependência direta ou indireta**, inclusive fora do Workspace. Um exemplo de dependência direta é o pedido para retirar `codigoSegmento`. Um exemplo de dependência indireta é a modificação de uma tarifa cujo valor varia conforme o segmento calculado. A cada reapresentação, a ressalva deve explicar a consequência concreta para o pedido atual.

## Relação com decisões anteriores do Discovery

`D01-DEC-002` permite concluir o onboarding com pendências não críticas catalogadas. `D01-DEC-003` requer que a classificação automática se apoie em critérios rigorosos, objetivos e verificáveis. Quando a criticidade permanece incerta após investigação, o agente leva a questão ao Engenheiro. `D01-DEC-016/017` e `HUM-08/09` sustentam a manutenção das pendências e a revalidação do conhecimento com novos esclarecimentos. Os exemplos concretizam parte de `D02-PEN-001/002`, sobre a suficiência da evidência para uma ação e sua apresentação. Critérios para outros casos, formas de apresentação e mecanismos de recuperação permanecem para refinamento.
