# Matrizes de rastreabilidade — PGC-001 v1.1.2

**Estado:** revisão documental proposta. Referências indicam **regras escritas**, não mecanismos implementados ou testes executados.

## A. Obrigações PGC-N → dono principal, interfaces e testes

| Norma | Dono operacional principal | Contratos auxiliares | Testes centrais |
|---|---|---|---|
| N-001 Interação natural | CT-001 | CT-006/007 | CA-01, CA-36 |
| N-002 Classificação | CT-001 | CT-002/008 | CA-01 a CA-06 |
| N-003 Captura proporcional | CT-001 | CT-006/007 | CA-01, CA-25, CA-36, CA-48 |
| N-004 Formalização progressiva | CT-001 | CT-002 | CA-01, CA-04, CA-05 |
| N-005 Estados ortogonais | CT-002 | CT-001/003/004/008 | CA-33, CA-46 |
| N-006 Aprovação verificável | CT-001 | CT-002/005/003 | CA-02 a CA-06, CA-32, CA-44, CA-49 |
| N-007 Integridade da aprovação | CT-001 | CT-003/005 | CA-12, CA-32, CA-37, CA-44, CA-46 |
| N-008 Fonte canônica | CT-002 | CT-007/003 | CA-30, CA-42 |
| N-009 Versionamento | CT-002 | CT-003/005 | CA-11, CA-17, CA-32 |
| N-010 Publicação controlada | CT-003 | CT-001/005/008 | CA-07, CA-12, CA-31, CA-43, CA-45, CA-46 |
| N-011 Concorrência segura | CT-003 | CT-006 | CA-07, CA-08, CA-17, CA-40 |
| N-012 Consistência documental | CT-003 | CT-004 | CA-15, CA-34, CA-35 |
| N-013 Rastreabilidade | CT-002 | CT-004 | CA-27, CA-28 |
| N-014 Propagação de impacto | CT-004 | CT-003/002 | CA-09, CA-10, CA-34 |
| N-015 Fronteiras de confiança | CT-005 | CT-008 | CA-19, CA-20, CA-22, CA-41 |
| N-016 Menor privilégio | CT-005 | CT-003 | CA-06, CA-23, CA-31 |
| N-017 Proteção de informações | CT-005 | CT-002 | CA-21, CA-38 |
| N-018 Persistência verificável | CT-003 | CT-006/008 | CA-14, CA-18, CA-35, CA-46, CA-47 |
| N-019 Continuidade | CT-006 | CT-007 | CA-13, CA-16, CA-36, CA-48 |
| N-020 Contexto mínimo suficiente | CT-007 | CT-006/004 | CA-16, CA-28 |
| N-021 Revisão crítica | CT-008 | CT-001/004 | CA-05, CA-26, CA-32 |
| N-022 Evidências de conclusão | CT-008 | CT-002/003 | CA-18, CA-35, CA-46, CA-47 |
| N-023 Recuperação controlada | CT-003 | CT-006 | CA-14, CA-15, CA-35, CA-39 |
| N-024 Limites de automação | CT-006 | CT-008 | CA-29 |
| N-025 Transparência | CT-006 | CT-003/007 | CA-13, CA-18, CA-35, CA-36, CA-48 |

## B. Achados da auditoria cruzada AC-01..AC-20 → local de correção

| Achado | Correção normativa implementada **no texto** | Status documental |
|---|---|---|
| AC-01 Estados misturados | CT-001 §4; CT-002 §2; CT-003 §2; CT-004 §3 | Especificado, não codificado |
| AC-02 Aprovação textual vs identidade | CT-001 §6; CT-005 §§2–3; CT-003 §4 | Especificado |
| AC-03 Autoalteração das regras | PGC §2/§8; CT-005 §4; CT-003 §4 | Especificado |
| AC-04 Publicação sem invalidação | CT-004 §5; CT-003 §§3/4 | Especificado |
| AC-05 Atomicidade ambígua | CT-003 §§1/5 e limitações multi-repositório | Especificado com limite explicitado |
| AC-06 Aprovação inválida após reconciliação | CT-001 §7; CT-003 §§4/5 | Especificado |
| AC-07 Publicado vs verificado | CT-003 §§2/7/8 | Especificado |
| AC-08 Captura automática indefinida | CT-001 §3; CT-006 §§1/4; CT-007 §7 | Especificado com limite de ferramentas |
| AC-09 Testes não executáveis | CT-008 e catálogo JSON; runner pendente | Especificação verificável; execução pendente |
| AC-10 Esquema de dados | CT-002 §§1–2/9 | Modelo normativo; JSON Schema concreto pendente |
| AC-11 Versões confundidas | CT-002 §3 | Especificado |
| AC-12 Fonte canônica duplicada | CT-002 §5; CT-007 §4 | Especificado |
| AC-13 Confiança/proveniência | CT-002 §6; CT-005 §5 | Especificado |
| AC-14 Impacto vs autorização | CT-001 §9; CT-005 §8 | Especificado |
| AC-15 Revogação e dependentes | CT-001 §8; CT-004 §7 | Especificado |
| AC-16 Fonte removida | CT-002 §6; CT-004 §8 | Especificado |
| AC-17 Retenção de sensíveis | CT-005 §6 | Política concreta pendente |
| AC-18 Tentativas e escalonamento | CT-006 §6 | Parâmetros operacionais pendentes |
| AC-19 Isolamento da revisão | CT-008 §§2/10; CT-005 §5 | Método definido; ambiente pendente |
| AC-20 Deterioração documental | CT-007 §8 | Inspeção definida; limites quantitativos pendentes |

## C. Fronteiras exclusivas entre contratos

- **CT-001 × CT-005:** CT-001 interpreta objeto/escopo da aprovação; CT-005 **autoriza** identidade/operação na política vigente.
- **CT-003 × CT-006:** CT-003 publica e recupera **efeitos de escrita**; CT-006 recupera **contexto/atividades**, chamando CT-003 para verificar recibos.
- **CT-003 × CT-004:** CT-004 calcula invalidações; CT-003 as publica com consistência e CAS.
- **CT-002 × CT-007:** CT-002 define registro/ID/revisão; CT-007 define caminho/índice físico.
- **CT-008 × todos:** define critérios e evidências de avaliação, sem alterar o objeto testado por conta própria.

## D. Invariantes de maior risco

1. Nenhuma decisão normativa aprovada sem autoridade, escopo e revisão válidos.
2. Política candidata não autoriza a própria ativação.
3. Aprovação não sobrevive automaticamente a mudança material de digest ou revogação.
4. CAS ou equivalente bloqueia sobrescrita silenciosa sob concorrência.
5. O requisito alterado e a invalidação de dependentes conhecidos têm visibilidade oficial consistente.
6. Uma publicação que passou por commit mas falhou na pós-verificação nunca é reclassificada como “não publicada”.
7. Mesma chave de idempotência com conteúdo diferente é erro.
8. Documento externo não se promove a canal de instrução.
9. Sem recibo verificável não existe alegação de persistência comprovada.
10. Aprovado, publicado, atual, implementado e verificado não são sinônimos.

## E. Escopo da auditoria documental posterior

Uma implementação deverá demonstrar os 49 casos CA, com fixtures e runner efetivos, e os portões específicos do ambiente. Antes disso, os resultados permanecem `NOT_RUN`. A matriz afirma **cobertura contratual de 25/25 normas e tratamento textual de 20/20 achados**, não conformidade operacional comprovada.


## F. Emendas EM-001..EM-006 → documentos, normas e testes

| Emenda | Responsabilidade principal | Outras alterações vinculadas | Normas | Testes (não executados) |
|---|---|---|---|---|
| EM-001 — Ratificação inicial | PGC §2.1; CT-005 §4.1 | CT-002 §4.1; CT-003 §3.1 | N-006, N-010, N-016 | CA-31, CA-40, CA-43 |
| EM-002 — Intenção ≠ revisão derivada | CT-001 §6.1 | CT-002 §4; CT-005 §4.2 | N-002, N-006, N-007 | CA-04, CA-44, CA-49 |
| EM-003 — Ordem de preparação/validação/aprovação | CT-003 §§2,3,3.2 | PGC §5 | N-010, N-018 | CA-12, CA-32, CA-45 |
| EM-004 — Publicado, verificado e vigente | CT-003 §5.1 | PGC §5.1; CT-002 §4.1; CT-004 §5.1; CT-005 §4.3; CT-006 §7.1; CT-007 §6 | N-005, N-007, N-010, N-014, N-018 | CA-33, CA-34, CA-35, CA-46, CA-47 |
| EM-005 — Política de captura | CT-001 §3.1; CT-006 §1.1 | PGC §6.1; CT-002 §8.1; CT-007 §7.1 | N-001, N-003, N-019, N-025 | CA-01, CA-13, CA-36, CA-48 |
| EM-006 — CA-04 semântico e CA-49 formal | CT-008 §5 e §7.1 | CT-001 §6.1; JSON `F-PARCIAL`/`F-PARCIAL-FORMAL` | N-004, N-006, N-007 | CA-04, CA-49 |

## G. Regra de contagem e validade

A matriz registra **25/25 normas associadas**, **20/20 achados de auditoria cruzada localizados** e **6/6 emendas rastreadas**. O catálogo contém **49 casos CA**, todos `NOT_RUN`. Essas contagens são propriedades documentais verificáveis, não certificação semântica nem comprovação de comportamento operacional. Nenhum documento foi ratificado pelo simples fato de constar desta matriz.
