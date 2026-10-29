"""Verifica os bytes desta importação; não escreve nem executa scripts do pacote."""
from pathlib import Path, PurePosixPath
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PACKAGE_NAME = 'PGC-001_v1.1.2_candidata_ratificacao'
PACKAGE = ROOT / 'docs' / '00-governanca' / PACKAGE_NAME
ZIP = ROOT / 'acervo' / (PACKAGE_NAME + '.zip')

def check_manifest(manifest, base):
    listed = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, rel = line.split('  ', 1)
        rel = rel.removeprefix('./')
        p = PurePosixPath(rel)
        assert not p.is_absolute() and '..' not in p.parts and ':' not in rel and '\\' not in rel
        assert rel not in listed
        listed.add(rel)
        assert hashlib.sha256(base.joinpath(*p.parts).read_bytes()).hexdigest() == digest, rel
    return listed

all_files = check_manifest(HERE / 'SHA256-IMPORTACAO.txt', ROOT)
original_files = check_manifest(PACKAGE / 'SHA256SUMS.txt', PACKAGE)
actual = {p.relative_to(PACKAGE).as_posix() for p in PACKAGE.rglob('*') if p.is_file()}
assert actual == original_files | {'SHA256SUMS.txt'}
assert hashlib.sha256(ZIP.read_bytes()).hexdigest() == '8e2ae296829e5dfcdd313d9c088470c23aa825d72b8c518442ff1a3e338c42fd'
with zipfile.ZipFile(ZIP) as z:
    assert z.testzip() is None
    entries = {e.filename for e in z.infolist() if not e.is_dir()}
    assert entries == {f'{PACKAGE_NAME}/{rel}' for rel in actual}
    for rel in actual:
        assert z.read(f'{PACKAGE_NAME}/{rel}') == (PACKAGE / rel).read_bytes(), rel
print(f'PASS: {len(all_files)} hashes da importação; {len(original_files)} hashes originais; {len(actual)} arquivos idênticos ao ZIP; CRC íntegro.')
print('Escopo: integridade documental. PROPOSTO / NÃO RATIFICADO / NÃO IMPLEMENTADO. Nenhum teste operacional executado.')
