# PGC-001 v1.1.2 — Candidata à ratificação normativa

**Data:** 29/10/2026  
**Estado:** **PROPOSTO — NÃO RATIFICADO — NÃO IMPLEMENTADO — NÃO TESTADO OPERACIONALMENTE**  
**Norma:** `PGC-001.md` v1.1.2  
**Contratos:** oito documentos CT-001 a CT-008 v1.0.2  
**Base de revisão:** v1.1.1 e parecer final com seis emendas EM-001..EM-006.

## Escopo e composição

Preservam-se **integralmente os nove documentos normativos e contratuais** da arquitetura modular. Foram aplicadas correções localizadas e consistentes; a norma central continua regulando obrigações, e os oito contratos continuam proprietários dos mecanismos especializados.

| Arquivo | Papel |
|---|---|
| [`PGC-001.md`](PGC-001.md) | Norma central, 25 obrigações, hierarquia e ratificação inicial |
| [`contratos/CT-001-classificacao-aprovacao.md`](contratos/CT-001-classificacao-aprovacao.md) | Captura, significado de decisões e escopo de aprovação |
| [`contratos/CT-002-modelo-proveniencia.md`](contratos/CT-002-modelo-proveniencia.md) | Identidades, estados, versões, manifesto e fontes |
| [`contratos/CT-003-publicacao-concorrencia.md`](contratos/CT-003-publicacao-concorrencia.md) | Publicação, concorrência, pré/pós-checks e ativação |
| [`contratos/CT-004-rastreabilidade-impactos.md`](contratos/CT-004-rastreabilidade-impactos.md) | Dependências e invalidações no snapshot efetivo |
| [`contratos/CT-005-seguranca-autorizacao.md`](contratos/CT-005-seguranca-autorizacao.md) | Política vigente, ratificação, identidade e permissões |
| [`contratos/CT-006-continuidade-recuperacao.md`](contratos/CT-006-continuidade-recuperacao.md) | Sessões, modos de captura, pendências e recuperação |
| [`contratos/CT-007-organizacao-contexto.md`](contratos/CT-007-organizacao-contexto.md) | Organização física e navegação pela versão vigente |
| [`contratos/CT-008-verificacao-adversarial.md`](contratos/CT-008-verificacao-adversarial.md) | Estratégia de avaliação, CA-01..CA-49 e oráculos |

**Arquivos de suporte:**

- [`MATRIZ-DE-RASTREABILIDADE.md`](MATRIZ-DE-RASTREABILIDADE.md): cobertura PGC-N→contratos→CA, AC-01..20 e EM-001..006.
- [`REGISTRO-DE-EMENDAS.md`](REGISTRO-DE-EMENDAS.md): diferenças da revisão e razões técnicas.
- [`RATIFICACAO-INICIAL-MODELO.md`](RATIFICACAO-INICIAL-MODELO.md): modelo **não assinado** para ratificação fundacional futura.
- [`verificacoes/casos-adversariais.json`](verificacoes/casos-adversariais.json): 49 especificações de testes, **NOT_RUN**.
- [`verificacoes/gerar_catalogo.py`](verificacoes/gerar_catalogo.py): reproduz o catálogo JSON, sem executar o harness.
- [`verificacoes/auditar_pacote.py`](verificacoes/auditar_pacote.py): verificação estática do pacote.
- [`verificacoes/relatorio-verificacao.md`](verificacoes/relatorio-verificacao.md): execução da auditoria estática e inventário de artefatos.

## As seis emendas incorporadas

| Emenda | Diretriz | Resultado esperado |
|---|---|---|
| EM-001 | Ratificação inicial manual, autenticada e de uso único | Primeira política entra em vigor sem autoaprovação e sem exceção reutilizável |
| EM-002 | Separar decisão de intenção e aprovação da revisão normativa | Requisitos derivados pelo agente não recebem aprovação implícita |
| EM-003 | Preparar → pré-validar → aprovar → revalidar → publicar | O conteúdo aprovado corresponde ao snapshot efetivo |
| EM-004 | Publicado ≠ verificado ≠ vigente | Só manifesto ativado define a norma vigente |
| EM-005 | Captura assistida inicialmente; automática apenas com integração autorizada | Ideias não são perdidas por promessa de sincronização inexistente |
| EM-006 | CA-04 é teste semântico; CA-49 valida aprovação formal | Diferenciar compreensão da intenção e autorização técnica |

## Condições para adoção

1. Os nove documentos permanecem **propostas** até ratificação expressa, válida e registrada pelo responsável legitimado.
2. Ratificação inicial deve referenciar conjunto documental exato, versões, identidade/autorização e digest do pacote, com registro verificável e comprovação de ausência de política anterior vigente.
3. O processo de bootstrap é de **uso único**. Revisões posteriores utilizam a versão da política vigente anterior à mudança.
4. A publicação de código/documentação em repositório não significa ativação normativa. O manifesto efetivo deve ser protegido e atualizado condicionalmente.
5. A aprovação da especificação **não** equivale a implementação operacional, nem comprova os casos adversariais.

## Limites de capacidade

A criação deste pacote não altera o futuro Projeto do ChatGPT nem configura uma integração com Git, autenticação, captura entre conversas ou publicação automática. Nenhum teste CA-01..CA-49 foi executado contra um harness. Todos exigem fixture/runner, ambiente controlado e evidências para aprovação operacional.

## Escolhas de arquitetura ainda abertas

Continuam abertas: repositório oficial e proteções, esquema concreto, forma de autenticar autorizações, mecanismo real de ativação/manifesto, sincronização entre ChatGPT/Work/Codex e arquivos, retenção/classificação corporativa, fila durável, CAS multi-repositórios, outbox/eventos, limites de retries, métricas semânticas e runner de testes. Essas escolhas devem respeitar as invariantes, não substituí-las.

**Próxima etapa:** revisão humana da candidata v1.1.2, ratificação fundacional registrada e, depois, implementação dos controles em ambiente isolado. A ratificação não deve ser presumida pelo pedido de elaborar este pacote.
