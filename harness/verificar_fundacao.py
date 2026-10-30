"""Verificações de fundação somente leitura; não executa CA operacionais."""
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'auditorias/fundacao-integral'

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def check():
    results = []
    def require(ok, label):
        results.append({'check': label, 'pass': bool(ok)})
    manifest = json.loads((AUDIT/'baseline-remoto.json').read_text(encoding='utf-8'))
    for entry in manifest['entries']:
        if entry['path'] in manifest['allowed_changed']:
            continue
        p = ROOT/entry['path']
        require(p.is_file() and git_blob(p.read_bytes()) == entry['sha'],
                'historico-intacto:'+entry['path'])
    for version in ('1.1.2', '1.1.3'):
        name = f'PGC-001_v{version}_candidata_ratificacao'
        folder = ROOT/'docs/00-governanca'/name
        with zipfile.ZipFile(ROOT/'acervo'/(name+'.zip')) as archive:
            require(archive.testzip() is None, 'zip-crc:'+version)
            for entry in archive.infolist():
                relative = Path(entry.filename).relative_to(name)
                require((folder/relative).read_bytes() == archive.read(entry),
                        'zip-bytes:'+str(relative)+':'+version)
        cases = json.loads((folder/'verificacoes/casos-adversariais.json').read_text(encoding='utf-8'))
        # Busca todos os estados de caso sem pressupor o nome do container.
        def walk(value):
            if isinstance(value, dict):
                if re.fullmatch(r'CA-\d{2}', str(value.get('case_id', ''))):
                    yield value
                for child in value.values(): yield from walk(child)
            elif isinstance(value, list):
                for child in value: yield from walk(child)
        found = list(walk(cases))
        require(len(found) == 49 and all(x['status'] == 'NOT_RUN' for x in found),
                '49-CA-preservados-NOT_RUN:'+version)
    required = ['README.md','AGENTS.md','ESTADO-ATUAL.md',
        'docs/fundacao/visao-produto.md','docs/fundacao/ecossistema-atual.md',
        'docs/fundacao/capacidades.md','docs/fundacao/metodologia-fases.md',
        'docs/fundacao/registro-conhecimento.md','docs/fundacao/construcao-internalizacao.md',
        'docs/fundacao/protocolo-sessoes.md','docs/fundacao/roteamento-contexto.md',
        'docs/chatgpt/INSTRUCOES-PERMANENTES.md','docs/01-discovery/INICIO-DISCOVERY.md']
    for path in required: require((ROOT/path).is_file(), 'entrada:'+path)
    # Caminhos de links são verificados; âncoras Markdown e links remotos não são resolvidos.
    documents = [ROOT/p for p in required] + list((ROOT/'docs/chatgpt').glob('*.md'))
    for path in dict.fromkeys(documents):
        if not path.is_file(): continue
        content = path.read_text(encoding='utf-8')
        for dest in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', dest) or dest.startswith('#'): continue
            target = (path.parent/dest.split('#')[0]).resolve()
            require(target.is_relative_to(ROOT) and target.exists(),
                    'link:'+path.relative_to(ROOT).as_posix()+'->'+dest)
    return results

if __name__ == '__main__':
    checks = check()
    output = {'scope':'ESTATICO_FUNDACAO_NAO_49_CA', 'checks': checks,
              'passed':sum(x['pass'] for x in checks), 'total':len(checks)}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    sys.exit(0 if all(x['pass'] for x in checks) else 1)

