"""Verifica o snapshot e ambos os pacotes, sem escrever ou ativar política."""
import hashlib
from pathlib import Path, PurePosixPath
import zipfile

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent

def manifest(path,base):
    seen=set()
    for line in path.read_text(encoding='utf-8').splitlines():
        digest,rel=line.split('  ',1)
        rel=rel.removeprefix('./'); p=PurePosixPath(rel)
        if p.is_absolute() or '..' in p.parts or ':' in rel or '\\' in rel or rel in seen:
            raise ValueError('Caminho ou entrada inválida: '+rel)
        seen.add(rel)
        if hashlib.sha256(base.joinpath(*p.parts).read_bytes()).hexdigest()!=digest:
            raise ValueError('Hash diferente: '+rel)
    return seen

files=manifest(HERE/'SHA256-REVISAO.txt',ROOT)
for ver,count in [('1.1.2',18),('1.1.3',20)]:
    name=f'PGC-001_v{ver}_candidata_ratificacao'
    pkg=ROOT/'docs/00-governanca'/name
    listed=manifest(pkg/'SHA256SUMS.txt',pkg)
    actual={p.relative_to(pkg).as_posix() for p in pkg.rglob('*') if p.is_file()}
    if len(actual)!=count or actual!=listed|{'SHA256SUMS.txt'}:
        raise ValueError('Inventário incompleto: '+name)
    with zipfile.ZipFile(ROOT/'acervo'/(name+'.zip')) as z:
        if z.testzip() is not None: raise ValueError('CRC inválido')
        if len(z.infolist())!=count or {x.filename for x in z.infolist()}!={name+'/'+rel for rel in actual}:
            raise ValueError('ZIP divergente: '+name)
        for rel in actual:
            if z.read(name+'/'+rel)!=(pkg/rel).read_bytes(): raise ValueError('Bytes divergentes: '+rel)
if hashlib.sha256((ROOT/'acervo/PGC-001_v1.1.2_candidata_ratificacao.zip').read_bytes()).hexdigest()!='8e2ae296829e5dfcdd313d9c088470c23aa825d72b8c518442ff1a3e338c42fd':
    raise ValueError('O ZIP original v1.1.2 foi alterado')
print(f'PASS: {len(files)} hashes do snapshot; v1.1.2 (18 arquivos) e v1.1.3 (20 arquivos) idênticos aos respectivos ZIPs; CRCs íntegros.')
print('PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO. Zero casos CA executados.')
