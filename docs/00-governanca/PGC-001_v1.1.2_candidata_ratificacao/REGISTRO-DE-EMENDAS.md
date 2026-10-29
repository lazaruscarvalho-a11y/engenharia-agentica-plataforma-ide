# Registro de emendas e decisões corretivas — PGC-001 v1.1.2

**Estado:** proposta preparada, não ratificada. **Origem:** parecer de revisão final da v1.1.1. **Natureza:** mapa de alterações, não fonte normativa paralela.

## EM-001 — Ratificação inicial de uso único

**Problema:** ausência de política P0 na primeira adoção cria círculo de autoautorização. **Decisão corretiva proposta:** ratificação humana explícita sobre pacote/digest, com comprovação de que não há norma anterior vigente e marcação de bootstrap não repetível. **Alterações:** PGC §2.1 e §7; CT-002 §4.1; CT-003 §3.1; CT-005 §4.1. **Validação prevista:** CA-43, CA-31/40.

## EM-002 — Aprovação de intenção ≠ aprovação de requisitos derivados

**Problema:** uma manifestação geral poderia legitimar detalhes que apenas o agente acrescentou. **Decisão corretiva proposta:** separar `INTENCAO_PRODUTO` de `REVISAO_NORMATIVA`, exigir digest e revisão específicos para a última. **Alterações:** PGC N-006; CT-001 §§6,6.1,7; CT-002 §4; CT-005 §4.2. **Validação prevista:** CA-04, CA-44, CA-49.

## EM-003 — Ordem estável de ChangeSets

**Problema:** v1.1.1 posicionava aprovação antes de finalizar snapshot/pré-testes apesar da máquina `PREPARED → VALIDATED → AUTHORIZED`. **Decisão corretiva proposta:** preparar candidato integral, executar pré-testes, obter aprovação sobre digest validado, rechecagem JIT, publicar. **Alterações:** PGC §5; CT-003 §§2,3,3.2,4. **Validação prevista:** CA-45 e CA-32.

## EM-004 — Publicação, verificação e vigência independentes

**Problema:** commit publicado com pós-teste falho poderia ser tratado como definição vigente. **Decisão corretiva proposta:** `EffectiveManifest` separado de `publication_state`; verificação crítica pré-ativação, atualização condicional do manifesto e bloqueio para revisões não ativadas. **Alterações:** PGC N-005/N-007/N-018 e §5.1; CT-002 §4.1; CT-003 §5.1; CT-004 §5.1; CT-005 §4.3; CT-006 §7.1; CT-007 §6. **Validação prevista:** CA-46/47 e CA-34/35.

## EM-005 — Modo inicial de captura e limite real das ferramentas

**Problema:** capture semântica foi confundida com persistência entre sessões. **Decisão corretiva proposta:** padrão `CAPTURA_ASSISTIDA_NA_SESSAO`, modo automático conectado somente com integração/política/autorização; C0/C1 sempre exploratórios. **Alterações:** PGC N-003 e §6.1; CT-001 §3.1; CT-002 §8.1; CT-006 §1.1; CT-007 §7.1. **Validação prevista:** CA-36 e CA-48.

## EM-006 — CA-04 semântico / CA-49 formal

**Problema:** CA-04 esperava `approval_state=VALIDA` sem identidade ou digest do texto normativo. **Decisão corretiva proposta:** CA-04 verifica apenas interpretação de intenção parcial; CA-49 exige fixture autenticada e revisão/digest/escopo completos. **Alterações:** CT-008 §§5,7.1; catálogo JSON e gerador. **Validação prevista:** execução futura de CA-04 e CA-49.

## Mudanças preservadas

Permanecem **PGC-N-001..025**, **CT-001..008**, **CA-01..42** (CA-04 aperfeiçoado sem renumerar) e **AC-01..20**. Novos casos CA-43..49 complementam a bateria. Os scripts de verificação e a matriz foram atualizados para a nova versão.

## Limites

Não há ratificação, instalação, integração com o Projeto no ChatGPT, autenticação efetiva, publicação real no repositório do usuário nem execução operacional dos cenários. Este registro documenta as modificações propostas à norma e aos contratos, não uma autorização de adoção.
