"""Verifica snapshot de continuidade; não publica, aprova ou autentica pessoas."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath


def verify(root, manifest_path):
    root = Path(root).resolve()
    manifest = json.loads(Path(manifest_path).read_bytes())
    if manifest.get('schema_version') != 'continuidade-1' or manifest.get('normative_effect') != 'AUSENTE':
        raise ValueError('MANIFESTO_INVALIDO')
    if manifest.get('repository') != 'lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide':
        raise ValueError('REPOSITORIO_DIVERGENTE')
    entries = manifest['files']
    if not entries or len({e['path'] for e in entries}) != len(entries):
        raise ValueError('INVENTARIO_VAZIO_OU_DUPLICADO')
    verified = {}
    for entry in entries:
        relative = entry['path']
        parts = PurePosixPath(relative).parts
        if not relative or '\\' in relative or ':' in relative or relative.startswith('/') or '..' in parts:
            raise ValueError('CAMINHO_INVALIDO')
        target = (root / relative).resolve()
        if not target.is_relative_to(root):
            raise ValueError('DESTINO_FORA_DA_RAIZ')
        data = target.read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        if actual != entry['sha256'] or len(data) != entry['bytes']:
            raise ValueError('INTEGRIDADE_DIVERGENTE:' + relative)
        verified[relative] = actual
    record_path = manifest['record_path']
    if record_path not in verified:
        raise ValueError('REGISTRO_NAO_INVENTARIADO')
    record = json.loads((root / record_path).read_bytes())
    if record.get('record_id') != manifest['record_id'] or type(record.get('revision')) is not int or record['revision'] != manifest['revision']:
        raise ValueError('IDENTIDADE_DIVERGENTE')
    if record.get('normative_effect') != 'AUSENTE' or record.get('product_approval') != 'NAO_CONCEDIDA':
        raise ValueError('EFEITO_INDEVIDO')
    if record.get('source_kind') != 'USER_DIRECT' or not record.get('source_ref') or not record.get('request'):
        raise ValueError('ORIGEM_AUSENTE')
    return {'status': 'VERIFICADO_LOCALMENTE', 'record_id': record['record_id'],
            'revision': record['revision'], 'files': verified,
            'normative_effect': 'AUSENTE', 'product_approval': 'NAO_CONCEDIDA',
            'limit': 'Comparação de bytes; origem do manifesto e commit remoto devem ser conferidos pelo operador.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument('--manifesto', required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.manifesto), ensure_ascii=False, indent=2))
