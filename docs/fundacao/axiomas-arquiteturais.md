# Axiomas arquiteturais — revisão 1

**Direções de produto reproduzidas e interpretações operacionais candidatas. Sem efeito normativo corporativo. PGC-001 v1.1.3 e CT-001..CT-008 v1.0.3 NÃO RATIFICADOS.** Publicar em fundação/Git, aprovar redação ou testar documentos não ratifica normas nem aprova implementação.

Dono temático AX-01..AX-10. Fonte de direção: PM-D02-CONSOL-001 R5 §4.7 e cláusulas indicadas; HUM-07 do [ledger D02](../01-discovery/discovery-02/REGISTRO.md#hum-07) possui identidade/proveniência/maturidade. A semântica restaurada é interpretação do dossiê/catálogo, não citação literal recuperada do R3. Projeções devem citar ID/revisão deste arquivo.

<a id="ax-01"></a>

## AX-01 — Agent-Centric

Fonte: HUM-04/07; R4-021; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Priorizar leitura, compreensão e modificação por agentes desde a importação para trabalho posterior autorizado. No onboarding, nenhuma refatoração. Limitar a diretriz ao escopo efetivo da mudança; não reestruturar todo arquivo, repositório ou dependência por oportunismo.

Interpretação operacional proposta: Relacionar intenção, evidências e escopo de cada mudança; conservar fonte e interfaces que não precisem mudar.

Tecnologias exemplificativas e dependências abertas: Convenções de arquivos e índices são exemplos candidatos; desenho Agent-First ainda a especificar.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-02"></a>

## AX-02 — Agent-Oriented

Fonte: HUM-07; R4-017; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Componentes e interfaces devem ser utilizáveis por agentes mediante contratos de execução, entradas/saídas, precondições, efeitos, permissões, falhas, metadados e evidências observáveis. README/comentários sozinhos são insuficientes.

Interpretação operacional proposta: Contratos candidatos D02-CT documentam essas fronteiras sem executar componentes.

Tecnologias exemplificativas e dependências abertas: Protocolos, schemas, transportes e ferramentas permanecem candidatos.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-03"></a>

## AX-03 — AI-Intent

Fonte: HUM-07; R4-016; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Explicitar intenção, porquê, objetivos, semântica, invariantes, restrições e critérios de aceite de modo legível por máquina, vinculado à fonte humana. Concisão narrativa sozinha não satisfaz a direção.

Interpretação operacional proposta: Representação candidata relaciona cada intenção à fonte, revisão, invariante e oráculo; inclui evidência contrária e pendências.

Tecnologias exemplificativas e dependências abertas: Linguagem, schema e tecnologia de representação ainda não escolhidos.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-04"></a>

## AX-04 — SDD

Fonte: HUM-07; R4-015; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Proibir código produtivo antes de especificação validada e aprovações aplicáveis. Guiado por especificações não suaviza essa precondição.

Interpretação operacional proposta: Ensaios sintéticos descartáveis exigem escopo explícito e não podem virar produto disfarçado; nesta missão somente documentos e verificações documentais.

Tecnologias exemplificativas e dependências abertas: Método de validação/aceite e ferramentas futuras continuam a especificar.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-05"></a>

## AX-05 — Harness Engineering

Fonte: HUM-07 §4.7; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Contexto, contratos de tarefa, permissões, ferramentas, oráculos, observabilidade, revisão e recuperação são partes do sistema de engenharia.

Interpretação operacional proposta: Delegação indica objetivo, arquivos, fontes, dependências, permissões, entregável e oráculo; autoria/auditoria distintas e teto de duas tentativas por falha são controles desta missão.

Tecnologias exemplificativas e dependências abertas: Harness assistido documental não é IDE final nem prova dos 49 CA; orquestrador/observabilidade futuros são candidatos.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-06"></a>

## AX-06 — Contexto Mínimo Necessário

Fonte: HUM-07; R4-020; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Selecionar o menor contexto suficiente à tarefa sem perder restrições, decisões, contratos, contradições, evidências e pendências que alterem o resultado.

Interpretação operacional proposta: Inventariar unidades críticas antes de resumir/remover e confrontar retenção; expandir dependências necessárias.

Tecnologias exemplificativas e dependências abertas: Orçamento de contexto não justifica amputação; limiares e seleção automatizada são propostas.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-07"></a>

## AX-07 — Roteamento de Contexto

Fonte: HUM-07; R4-020; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Recuperar por tema, evidência e dependência; índices orientam navegação e não substituem fonte indispensável.

Interpretação operacional proposta: Rotas atuais remetem ao ledger, axiomas temáticos, retificações e evidências da revisão; contradição expande leitura.

Tecnologias exemplificativas e dependências abertas: Schemas/índices/adaptadores específicos e mecanismo de busca não escolhidos.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-08"></a>

## AX-08 — Contexto-Ótimo

Fonte: HUM-07; R4-020; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Otimizar recuperação/custo preservando toda informação crítica identificada, com cobertura e incerteza visíveis.

Interpretação operacional proposta: Comparar conjunto crítico antes/depois da transformação e rejeitar compressão que perca condição negativa, fonte ou autoridade.

Tecnologias exemplificativas e dependências abertas: Métrica, algoritmo, limite e garantia de ótimo não aprovados; otimização é sujeita a evidência.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-09"></a>

## AX-09 — AI-Based Architecture

Fonte: HUM-07; R4-018; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Loops cognitivos de investigar, planejar, agir, verificar e reconciliar ocupam posição central na arquitetura pretendida, com fronteiras de autoridade, dados, execução e intervenção humana explícitas.

Interpretação operacional proposta: Modelo descreve estados/efeitos e contratos candidatos por etapa; agir só dentro das permissões e do escopo.

Tecnologias exemplificativas e dependências abertas: Nenhum framework escolhido, autonomia implementada comprovada ou autorização irrestrita criada.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.

<a id="ax-10"></a>

## AX-10 — Agnosticidade de modelo/agente/ferramenta

Fonte: HUM-07; R4-019; D01-REL-002; revisão da direção conforme PM R5; definição temática revisão 1.

Direção preservada: Preservar portabilidade, padrões abertos e adaptações explícitas nas fronteiras. Exemplos Devin, Claude e Copilot não criam exclusividade ou conector existente.

Interpretação operacional proposta: Registrar capacidades necessárias, versão e limitações de cada adaptação; não prometer equivalência sem teste.

Tecnologias exemplificativas e dependências abertas: Formatos/adaptadores ainda candidatos. Disponibilidade e equivalência exigem provas próprias.

Evidência de capacidade: esta missão produz definição documental candidata; nenhuma funcionalidade da IDE, adaptador ou eficácia operacional é demonstrada por este axioma.
