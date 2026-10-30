# Método de engenharia e fases do produto

Versão: 0.1.0 — fundação proposta, sem vigência normativa. Fontes: SRC-001 (pedido desta missão) e SRC-002 (trechos recuperados da conversa de origem). As sete etapas foram relatadas como método do usuário; a distribuição em dez fases é uma organização proposta e explicitamente solicitada nesta missão. Isso não aprova funcionalidades nem tecnologia da IDE.

## Sete etapas do método

| Etapa | Trabalho concreto | Saída e critério de passagem |
|---|---|---|
| M-01 Discovery, discussões e refinamento | Investigar problema, atores, contexto, alternativas, dúvidas e pendências; consultar fontes antes de perguntar | Necessidades com origem e problemas reconhecidos; incertezas relevantes visíveis |
| M-02 Especificação aprofundada | Descrever regras, dados, estados, exceções, permissões, interfaces, UX, dependências e critérios de aceite | Requisito verificável, com ID e fonte; detalhes acrescentados por agentes continuam propostos |
| M-03 Revisões profundas | Revisão de negócio, UX, engenharia, segurança e testes por pessoas/agentes distintos dos autores | Achados classificados; contradições resolvidas ou aceitas pelo responsável legítimo; nenhuma aprovação fictícia |
| M-04 Plano de implementação, testes e validações | Dividir entregas, contratos, dependências, ambientes, oráculos, execução e recuperação | Plano executável vinculado a requisitos revisados, com gates e limites de autorização |
| M-05 Prompts-mestres especializados | Preparar tarefas por especialidade e responsabilidade | Cada tarefa tem objetivo, fontes, arquivos, interfaces, permissões, dependências, entregas e oráculos |
| M-06 Prompt final de execução | Consolidar ordem, coordenação, auditoria e remediação | Ordem de execução vinculada a versões exatas dos requisitos e plano; execução somente após autorização aplicável |
| M-07 Contexto e paralelismo útil | Aplicar contexto mínimo suficiente, roteamento, agentes e subagentes durante todas as anteriores | Cada agente recebe contexto necessário; resultados têm evidência e revisão; ausência de colisões e trabalho duplicado |

M-07 é transversal. Não significa esperar seis etapas para pensar em agentes. Revisões podem devolver trabalho à descoberta, sem apagar versões anteriores. Profundidade reduz omissões; não garante ausência absoluta de defeitos.

## Fases 00–09

| Fase | Objetivo e artefatos úteis | Gate de saída e retorno |
|---|---|---|
| 00 Fundação e governança | Visão integral, fontes, estado, método, continuidade, harness assistido e auditoria | Cobertura e limites evidenciados; branch/PR revisáveis; pendências humanas explícitas. Ratificação do PGC é gate separado, sem impedir brainstorm exploratório |
| 01 Estudo investigativo e discovery | Problemas, perfis, jornadas atuais/desejadas, hipóteses, riscos e perguntas priorizadas | Problemas e oportunidades compreendidos suficientemente para formular requisitos; incógnitas restantes com responsável e impacto |
| 02 Requisitos de negócio e produto | Objetivos, resultados, fronteiras, regras de negócio, perfis, prioridades e métricas propostas | Responsável do produto valida escopo e critérios relevantes; mudanças materiais retornam à fase 01 |
| 03 Requisitos funcionais, UX e experiência visual da IDE | Fluxos, telas, navegação, workspaces, estados, ações, permissões, acessibilidade e exceções | Requisitos e cenários de UX revisados; decisões visuais aprovadas no escopo exato; nenhuma tela inventada vira aceite |
| 04 Requisitos não funcionais e restrições | Segurança, privacidade, desempenho, disponibilidade, observabilidade, acessibilidade, custo e operação | Metas mensuráveis e método de medição acordados; conflitos custo/risco resolvidos ou registrados |
| 05 Arquitetura e contratos | Frontend/backend, dados, orquestrador, agentes, adaptadores, persistência e contratos; ADRs | Contratos testáveis e alternativas justificadas; riscos técnicos reduzidos por provas isoladas quando úteis |
| 06 Qualidade, testes e validações | Estratégia por requisito; testes independentes, falhas, segurança, regressão, integração e recuperação | Oráculos objetivos, dados sintéticos, ambientes e evidências definidos; cobertura insuficiente devolve às fases 02–05 |
| 07 Plano-mestre de implementação | Entregas, dependências, arquivos/interfaces, capacidade, agentes, prompts e critérios de pronta revisão | Plano e autorização delimitam versões e escopo; tarefas independentes podem avançar em paralelo |
| 08 Implementação e verificação | Plataforma real externa com frontend, backend, persistência, motor, agentes, conectores desacoplados, mocks, testes, documentação e pacote | Execução e testes comprovam capacidades; auditoria independente; P0/P1 corrigidos; limitações declaradas; sem substituição por interface vazia |
| 09 Internalização e homologação | Importação controlada; troca de mocks por adaptadores internos; identidade, redes, dados e operação do banco | Equipes autorizadas validam segurança, integrações e homologação. Produção depende de controles corporativos, GMUD, janela e aprovação explícita |

As fases são uma estrutura de raciocínio, não dez pastas vazias nem autorização de implementação antecipada. Materializar um documento quando houver conteúdo e necessidade de manutenção. O diretório histórico `docs/06-execucao` conserva seu nome e proveniência; ele não redefine a fase 06 deste mapa.

## Entradas, saídas e retorno por fase

| Fase | Entrada mínima | Saída verificável | Retorno quando o gate falhar |
|---|---|---|---|
| 00 | Dossiê e fontes acessíveis, autorização de escopo, snapshot real do repositório | Fundação reconciliada, evidências e limites; configuração comprovada ou pendência honesta | Permanecer em 00 para corrigir cobertura/persistência; discovery exploratório independente pode avançar |
| 01 | Fundação, relatos, intenções e pendências com proveniência | Problemas, perfis, jornadas, hipóteses e prioridades propostas | Retomar investigação em 01; se faltar fonte ou contexto, reconciliar também em 00 |
| 02 | Problemas e oportunidades refinados em 01 | Requisitos de negócio com objetivos, regras e critérios delimitados | Voltar a 01 se problema/valor for incerto; revisar 02 se houver contradição de escopo |
| 03 | Requisitos de negócio e jornadas, perfis e restrições conhecidos | Requisitos funcionais/UX, fluxos, telas e estados testáveis | Voltar a 02 para conflitos de regra; a 01 para necessidade desconhecida; revisar 03 para falha de usabilidade |
| 04 | Requisitos funcionais, riscos e restrições de ambiente | RNFs mensuráveis com orçamento e método de medição | Retomar 02/03 se metas conflitam com escopo; revisar 04 se medição ou limite for inviável |
| 05 | Requisitos revisados e RNFs; contratos disponíveis ou lacunas identificadas | Arquitetura/contratos e decisões técnicas justificadas | Voltar a 03/04 se requisito inviável; revisar 05 e realizar prova isolada se risco técnico persistir |
| 06 | Requisitos, riscos, arquitetura e contratos versionados | Estratégia, dados, oráculos, ambientes e matriz de testes | Voltar a 02–05 quando não houver oráculo/contrato; revisar 06 se houver lacuna de cobertura |
| 07 | Arquitetura, estratégia de testes e requisitos revisados | Plano de entregas e prompts especializados com dependências, arquivos e critérios | Voltar a 05/06 se não for possível decompor/testar; a 02–04 se escopo ainda for ambíguo |
| 08 | Plano autorizado ligado a revisões exatas, ambiente e permissões reais | Plataforma externa executável, testes, auditoria, documentação e pacote | Corrigir implementação em 08; replanejar em 07 ou reabrir 02–06 diante de mudança material |
| 09 | Pacote externo verificado, contratos internos e profissionais autorizados | Evidências de internalização/homologação e operação autorizada | Voltar a 05/08 para incompatibilidade técnica; 04 para restrição interna; manter produção bloqueada até controles reais |

Cada retorno abre revisão rastreável nos documentos afetados e preserva decisões anteriores; não apaga histórico nem autoriza automaticamente a nova versão.

## Gates e decisões

Antes de construir uma funcionalidade da IDE, ligar necessidade → decisão/requisito aprovado → critérios de aceite → plano → tarefa → implementação → testes → evidência. Ausência de aprovação material mantém o item como proposta; não bloquear investigação ou preparação reversível autorizadas.

Provas técnicas isoladas podem reduzir dúvidas durante discovery. Devem ter hipótese, limite de dados/permissões, critério de conclusão e descarte/continuidade explícitos. Seu sucesso não aprova arquitetura nem capacidade produtiva.

## Protocolo de delegação

Uma tarefa contém: identificador, objetivo, fontes e versões, caminhos exclusivos de escrita, interfaces compartilhadas, dependências, permissões, entregáveis, comandos de verificação/oráculos, limite de duas tentativas por falha e condição de escalonamento. O coordenador integra diffs e resolve colisões. Agentes não ampliam autorização por conta própria.

Paralelizar frentes sem dependência de escrita; testes independentes podem ser planejados antes, mas a auditoria final usa versão congelada. Auditor não é o autor daquilo que audita. Se não houver equipe independente disponível, declarar revisão própria e não chamá-la de auditoria independente. Uma frente bloqueada não interrompe as demais.
