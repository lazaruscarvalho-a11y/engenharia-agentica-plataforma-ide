# CT-007 — Organização documental, fonte canônica e roteamento de contexto

**Versão:** 1.0.2 · **Estado:** PROPOSTO · **Norma:** PGC-001 v1.1.2  
**Dono exclusivo:** estrutura física, navegação, índices e recuperação contextual. **Não** redefine identidade lógica de CT-002 nem publica alterações fora de CT-003.

## 1. Objetivo

Criar uma base documental legível, modular, fácil de alterar e recuperável por agentes, com fonte normativa única para cada definição e referências entre documentos. Arquivos são **contêineres** de registros, não identidades imutáveis: mover/renomear documento não cria outro requisito.

## 2. Estrutura física inicial

```text
README.md
AGENTS.md
ESTADO-ATUAL.md
docs/
  00-governanca/
    PGC-001.md
    contratos/CT-001-...md ... CT-008-...md
    registros/{decisoes,pendencias,alteracoes}.md
  01-discovery/
  02-produto/{visao,ux}/
  03-requisitos/{indice,negocio,funcionais,nao-funcionais,integracoes}/
  04-arquitetura/
  05-qualidade/
  06-execucao/
harness/{protocolos,agentes,skills}/
```

Subdiretórios só serão materializados quando houver conteúdo real. Esta estrutura é proposta, não comando para criar arquivos vazios em massa. Arquivos canônicos têm nomes estáveis e descritivos; a revisão é mantida em sistema de versões, não em cópias `final_v7_revisado.md`.

## 3. Responsabilidade dos documentos principais

- `README.md`: apresentação do produto e entrada humana.
- `AGENTS.md`: índice **enxuto** de rotas, restrições gerais e contratos; não duplicar toda a norma.
- `ESTADO-ATUAL.md`: fase, versão consultada, marcos, decisões recentes, pendências, trabalhos bloqueados e próximas ações; **não** é lock nem prova de commit.
- `docs/00-governanca/`: norma, contratos e registros oficiais de decisão/alteração.
- `docs/01-discovery/`: fontes, hipóteses, brainstorms, estudos com seus estados.
- `docs/02-produto/`: visão, atores/jornadas, capacidades, UX e navegação.
- `docs/03-requisitos/`: registros normativos por domínio com índice e IDs.
- `docs/04-arquitetura/`: desenhos, componentes, contratos de software e ADRs.
- `docs/05-qualidade/`: planos, avaliações e evidências.
- `docs/06-execucao/`: marcos, progresso, planos e critérios de implementação.

## 4. Fonte canônica e aliases

CT-002 determina `record_id` e o registro `record_id -> canonical_ref`. CT-007 define onde esse registro reside e mantém os índices físicos. Uma definição normativa não pode possuir **duas fontes canônicas ativas**, ainda que seja citada em vários arquivos. Identificadores em links Markdown podem ser aliases; a resolução precisa detectar alias ambíguo, ausente ou circular.

Ao mover arquivos: alterar mapeamento e referências pertinentes no mesmo ChangeSet (CT-003), verificar links e evitar mudança de `record_id`. Sinopses auxiliares devem referenciar a revisão vigente, e não ser tratadas como autoridade normativa paralela.

## 5. Granularidade e política de divisão

Manter **um documento por responsabilidade coesa**; vários requisitos relacionados podem ocupar o mesmo arquivo com âncoras/IDs. Dividir quando: responsabilidades independentes, revisões frequentes em partes distintas, leitura/recuperação demasiado custosa, alto índice de conflitos de edição, ou mudança de escopo. Unir quando: arquivos pequenos redundantes ou impossíveis de compreender isoladamente. A decisão deverá justificar ganho de clareza/recuperação, não apenas contagem de linhas.

Não existe regra universal de tamanho máximo fixada neste contrato. Limiares instrumentais podem ser definidos após medidas de uso e avaliados em teste.

## 6. Roteamento de contexto

Para atividade `A`:
1. Identificar intenção, domínios e escopo.
2. Ler instruções da **versão ativada** e verificar revisão do EffectiveManifest/estado; não confundir último commit com norma vigente.
3. Consultar índices e recuperar registros canônicos do domínio.
4. Expandir para dependências críticas e revisões referenciadas.
5. Avaliar atualidade por CT-004 e acessibilidade da fonte por CT-002.
6. Se faltar informação material, ampliar consulta ou produzir pendência; não completar com hipótese não sinalizada.
7. Registrar no resultado referências efetivamente consultadas.

Roteamento mínimo não significa menos informação a qualquer custo: não eliminar políticas, decisões vigentes ou restrições essenciais. Dados sensíveis só podem entrar no contexto conforme CT-005.

## 7. Sincronização entre conversas e repositório

O Projeto do ChatGPT organiza conversas e fontes, mas isso não impõe, por si só, captura automática de todas as mensagens nem atualização de repositório. No modo inicial `CAPTURA_ASSISTIDA_NA_SESSAO`, o ChatGPT pode interpretar e propor alterações apenas para interações acessíveis. Quando houver escrita autorizada, o adaptador aplica CT-003 para persistência C0/C1; com somente leitura produz proposta; sem acesso declara limitações. A modalidade `CAPTURA_AUTOMATICA_CONECTADA` exige integração explícita e confirmada. Qualquer integração futura que ingestione conversas de múltiplas sessões precisa ser explicitamente implementada, autorizada, idempotente e avaliada por CT-008.

### 7.1. Separação entre acervo exploratório e revisão normativa vigente — EM-005

Índices e documentos auxiliares devem distinguir registro exploratório **persistido** de definição **vigente**. Salvar C0/C1 em arquivo navegável não os torna requisitos aprovados. O índice normativo deve resolver o `EffectiveManifest`/mapeamento canônico de CT-002/003; documentos candidatos ficam em espaço ou estado não normativo, com referências explícitas aos objetos que poderão alterar no futuro. A falta de conector entre chats e arquivos deve constar como limitação, não como sincronização presumida.
## 8. Manutenção e arquivamento

Verificações de rotina, quando acionadas, devem localizar: índices quebrados, registros sem fonte canônica, aliases duplicados, documentos `STALE`, requisitos aprovados sem critérios necessários ao seu escopo, referências a decisões substituídas como vigentes, arquivos não indexados, redundâncias e páginas extensas de responsabilidade confusa. O resultado pode recomendar arquivar, dividir, unir ou corrigir; não excluir silenciosamente históricos relevantes.

Arquivar não equivale a apagar; retenção e exclusão definitiva seguem CT-005. Material de baixo valor pode ser resumido ou descartado conforme classe e política, mantendo justificativas de decisões importantes.

## 9. Saída e aceite

Entregas incluem árvore documental, mapeamento canônico, índices, relatórios de links e plano de roteamento. Falhas: link inexistente → sinalizar; dois IDs reivindicando mesma âncora → conflito; resumo desatualizado → marcar como derivado; fonte ausente → não inventar; documento contendo segredo → bloquear sua ingestão/publicação inadequada.

**Aceite:** CA-16, CA-25 a CA-28, CA-30, CA-36, CA-42, CA-46 e CA-48.
