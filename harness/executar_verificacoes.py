"""Executa verificações do escopo exploratório; nunca converte CA NOT_RUN em PASS."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PGC = 'docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/verificacoes/'
COMMANDS = {
    'piloto': ['harness/governanca_assistida/test_fluxo.py'],
    'extensao': ['harness/governanca_assistida/test_fundacao.py'],
    'adversariais': ['auditorias/fundacao-integral/test_adversarial.py'],
    'regressao-pgc': [PGC+'testar_revisao.py'],
    'retomada': ['harness/test_retomada.py'],
    'fundacao-estatica': ['harness/verificar_fundacao.py'],
    'pgc-estatico': [PGC+'auditar_pacote.py', '--check'],
    'catalogo-estatico': [PGC+'gerar_catalogo.py', '--check'],
    'snapshot-retomada': ['harness/verificar_retomada.py', '--manifesto', 'docs/continuidade/MANIFESTO.json'],
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', required=True)
    args = parser.parse_args()
    out = Path(args.saida).resolve()
    out.mkdir(parents=True, exist_ok=False)
    results = []
    for name, command in COMMANDS.items():
        proc = subprocess.run([sys.executable, '-B', *command], cwd=ROOT, capture_output=True, timeout=180)
        (out/(name+'.stdout.txt')).write_bytes(proc.stdout)
        (out/(name+'.stderr.txt')).write_bytes(proc.stderr)
        results.append({'name': name, 'command': [sys.executable, '-B', *command], 'exit_code': proc.returncode})
    catalog = json.loads((ROOT/PGC/'casos-adversariais.json').read_bytes())
    statuses = {c['case_id']: c['status'] for c in catalog['cases']}
    summary = {'scope': 'EXPLORATORIO_LOCAL_NAO_CONFORMIDADE_PGC',
               'results': results, 'ca_operacionais': statuses,
               'success': all(r['exit_code'] == 0 for r in results) and len(statuses) == 49 and set(statuses.values()) == {'NOT_RUN'}}
    (out/'resultado.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary['success'] else 1

if __name__ == '__main__': sys.exit(main())
