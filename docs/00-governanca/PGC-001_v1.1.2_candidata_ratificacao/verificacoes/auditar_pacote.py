#!/usr/bin/env python3
"""Auditoria estática e documental do pacote PGC-001 v1.1.2.

NÃO testa funcionamento do harness, autenticação, segurança efetiva ou IA.
"""
from pathlib import Path
import hashlib
import json
import re
from collections import Counter

root = Path(__file__).resolve().parents[1]
contracts = sorted((root / 'contratos').glob('CT-*.md'))
primary = [root / 'PGC-001.md', *contracts]
checks = []
errors = []

def check(name, condition, detail=''):
    result = bool(condition)
    checks.append((name, result, str(detail)))
    if not result:
        errors.append((name, str(detail)))

pgc = (root / 'PGC-001.md').read_text(encoding='utf-8')
mat = (root / 'MATRIZ-DE-RASTREABILIDADE.md').read_text(encoding='utf-8')
readme = (root / 'README.md').read_text(encoding='utf-8')
registry = (root / 'REGISTRO-DE-EMENDAS.md').read_text(encoding='utf-8')
ct = {int(re.search(r'CT-(\d+)', p.name).group(1)): p.read_text(encoding='utf-8') for p in contracts}
data = json.loads((root / 'verificacoes/casos-adversariais.json').read_text(encoding='utf-8'))
cases = data['cases']
fixtures = data['fixtures']

check('Nove documentos normativos/contratuais', len(primary)==9 and all(x.is_file() for x in primary))
check('Contratos CT-001..008 sem lacuna', sorted(ct)==list(range(1,9)))
check('PGC v1.1.2 proposto', 'Versão | **1.1.2**' in pgc and 'PROPOSTO' in pgc)
for i in range(1,9):
    check(f'CT-{i:03d} v1.0.2 proposto', '**Versão:** 1.0.2' in ct[i] and 'PGC-001 v1.1.2' in ct[i] and '**Estado:** PROPOSTO' in ct[i])
check('25 normas distintas no PGC', sorted({int(x) for x in re.findall(r'PGC-N-(\d{3})',pgc)})==list(range(1,26)))
check('25 normas na matriz', sorted({int(x) for x in re.findall(r'^\| N-(\d{3})',mat,re.M)})==list(range(1,26)))
check('20 achados AC na matriz', sorted({int(x) for x in re.findall(r'^\| AC-(\d{2})',mat,re.M)})==list(range(1,21)))
check('Emendas EM-001..006 no registro', sorted({int(x) for x in re.findall(r'^## EM-(\d{3})',registry,re.M)})==list(range(1,7)))
check('Emendas EM-001..006 na matriz', sorted({int(x) for x in re.findall(r'^\| EM-(\d{3})',mat,re.M)})==list(range(1,7)))
check('Emendas EM-001..006 no README', sorted({int(x) for x in re.findall(r'^\| EM-(\d{3})',readme,re.M)})==list(range(1,7)))

actual_ids=[x['case_id'] for x in cases]
expected_ids=[f'CA-{i:02d}' for i in range(1,50)]
check('49 cenários únicos no JSON', len(actual_ids)==49 and sorted(actual_ids)==expected_ids)
ct8_ids=sorted(set(re.findall(r'^\| CA-(\d{2})\s*\|',ct[8],re.M)))
check('49 cenários CA no CT-008', ct8_ids==[f'{i:02d}' for i in range(1,50)])
check('Casos testados NÃO executados', data.get('status')=='TEST_SPEC_ONLY_NOT_EXECUTED' and all(c.get('status')=='NOT_RUN' and c.get('tested_version') is None for c in cases))
check('Fixtures completas', len(fixtures)>=17 and all(c.get('fixture_id') in fixtures for c in cases))
check('Metadados dos cenários', all(c.get('requirements') and c.get('contract_owners') and c.get('steps') and c.get('oracle_assertions') and c.get('forbidden_assertions') and c.get('evidence_fields') for c in cases))
check('Normas referenciadas por casos existentes', all(all(re.fullmatch(r'PGC-N-0(?:0[1-9]|1\d|2[0-5])',n) for n in c['requirements']) for c in cases))
check('Contratos referenciados por casos existentes', all(all(re.fullmatch(r'CT-00[1-8]',n) for n in c['contract_owners']) for c in cases))
check('Oráculos apenas em categorias conhecidas', all(c.get('oracle_kind') in ('semantic','mixed','deterministic') for c in cases))

by_case={c['case_id']:c for c in cases}
ca4=by_case['CA-04']; ca49=by_case['CA-49']
check('CA-04 é semântico e não presume aprovação normativa', ca4['oracle_kind']=='semantic' and 'no_formal_normative_approval_without_evidence' in ca4['expected_assertions'] and 'normative_approval_valid_without_required_evidence'==ca4['forbidden_observation'])
check('CA-04 fixture não tem identidade/digest', fixtures['F-PARCIAL'].get('actor_identity_verified') is False and fixtures['F-PARCIAL'].get('normative_digest_present') is False)
formal=fixtures['F-PARCIAL-FORMAL']['approval']
check('CA-49 inclui identidade, política, revisão, digest e escopo', ca49['fixture_id']=='F-PARCIAL-FORMAL' and formal.get('actor_identity_ref') and formal.get('content_digest') and formal.get('object_revision') and formal.get('scope')==['A'] and fixtures['F-PARCIAL-FORMAL'].get('policy_rev'))

check('Bootstrap EM-001 com ratificação inicial', all('bootstrap' in txt.lower() or 'ratifica' in txt.lower() for txt in (pgc,ct[2],ct[3],ct[5])))
check('Separação intenção/norma EM-002', all('INTENCAO_PRODUTO' in txt or 'intenção' in txt for txt in (ct[1],ct[2],ct[5])))
check('Ordem canônica no CT-003', all(fragment in ct[3] for fragment in ('`DRAFT → PREPARED`','`PREPARED → VALIDATED`','`VALIDATED → AUTHORIZED`','`AUTHORIZED → PUBLISHING`','`PUBLISHING → PUBLISHED`','`PUBLISHED → VERIFIED`')))
steps=ct[3].split('## 3. Protocolo de preparação')[1].split('### 3.1.')[0]
check('Pré-testes antecedem aprovação e publicação', steps.index('6. Executar os **pré-testes**') < steps.index('7. Obter ou conferir aprovação') < steps.index('9. Publicar **consistentemente**'))
check('Vigência só por manifesto ativado', all('EffectiveManifest' in txt for txt in (ct[2],ct[3],ct[4],ct[5],ct[6],ct[7])))
check('Publicado não implica vigente', 'não vigência' in ct[3] and 'VERIFIED' in ct[3] and 'VIGENTE' in ct[3])
check('Falha pós-publicação mantém norma anterior', 'versão anterior continua ativa' in ct[3] and 'P1_not_effective' in by_case['CA-47']['expected_assertions'])
check('Captura assistida como padrão', all('CAPTURA_ASSISTIDA_NA_SESSAO' in txt for txt in (pgc,ct[1],ct[2],ct[6],ct[7])))
check('Captura automática não presumida', 'não se deve presumir' in ct[6] and 'NAO_PERSISTIDO' in ct[6])
check('Ratificação é modelo não executado', 'NÃO ASSINADO / NÃO EXECUTADO' in (root/'RATIFICACAO-INICIAL-MODELO.md').read_text(encoding='utf-8'))

# Links relative references in normative docs and supporting README.
for p in [*primary,root/'README.md',root/'MATRIZ-DE-RASTREABILIDADE.md',root/'REGISTRO-DE-EMENDAS.md']:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if target.startswith(('https:','http:','#','mailto:','sandbox:')): continue
        path=p.parent/target.split('#')[0]
        check(f'Link relativo {p.name}: {target}',path.is_file())

for p in primary:
    check(f'Arquivo {p.name} não truncado', len(p.read_bytes())>5000)

# No unsupported claims of operational verification in status and report header.
check('README deixa clara ausência de implementação', 'NÃO IMPLEMENTADO' in readme and 'NOT_RUN' in readme)
check('Catálogo é test spec e não test execution', 'TEST_SPEC_ONLY_NOT_EXECUTED' in data['status'])

# Derive manifest (excluding self/report) and render report every time.
manifest=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name in {'relatorio-verificacao.md','SHA256SUMS.txt'}: continue
    rel=str(p.relative_to(root))
    manifest.append((rel,len(p.read_bytes()),hashlib.sha256(p.read_bytes()).hexdigest()))
lines=[
'# Relatório de verificação estática — PGC-001 v1.1.2','',
'**Escopo:** estrutura e conteúdo formal de nove documentos, índices, emendas e catálogo. **Não** testa sistemas de IA, escrita, autorização, CAS ou ativação real.','',
'**Estado do pacote:** PROPOSTO — NÃO RATIFICADO — NÃO IMPLEMENTADO.','',
'**Casos CA-01..CA-49:** `NOT_RUN`.','',
'**Resultado dos checks estáticos:** '+str(sum(ok for _,ok,_ in checks))+'/'+str(len(checks))+' PASS.','',
'| Check | Resultado | Observação |','|---|---|---|'
]
for label,ok,detail in checks:
    lines.append(f'| {label.replace("|","/")} | {"PASS" if ok else "FAIL"} | {detail.replace("|","/")} |')
lines.extend(['','## Limites metodológicos','','- Verificações de tokens/estrutura e correspondência de referências não são prova de consistência semântica completa.','- Testes CA-01..49 não foram executados; não há runner nem integrações reais.','- Aprovação de usuário, ratificação inicial e ativação normativa são pendentes.','- Escolhas tecnológicas de IAM, CAS, manifesto, filas e persistência permanecem em aberto.','','## Inventário SHA-256 do conteúdo (excluindo este relatório e SHA256SUMS.txt)','', '| Arquivo | Bytes | SHA-256 |','|---|---:|---|'])
for name,size,dig in manifest:
    lines.append(f'| `{name}` | {size} | `{dig}` |')
if errors:
    lines+=['','## Falhas detectadas','']+[f'- {name}: {detail}' for name,detail in errors]
else:
    lines+=['','**Nenhuma falha detectada pelos checks estáticos executados.** Isso não demonstra aprovação normativa ou operacional.']
(root/'verificacoes/relatorio-verificacao.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'Checks: {sum(ok for _,ok,_ in checks)}/{len(checks)} PASS')
for n,d in errors: print('FAIL',n,d)
raise SystemExit(1 if errors else 0)
