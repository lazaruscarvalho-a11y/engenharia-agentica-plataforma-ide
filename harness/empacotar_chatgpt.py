"""Exporta snapshots curados e hashes; não configura o ChatGPT."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--commit', required=True)
    p.add_argument('--saida', required=True)
    args=p.parse_args()
    if not re.fullmatch(r'[a-f0-9]{40}', args.commit):
        p.error('Commit imutável de 40 caracteres obrigatório')
    dest=Path(args.saida); dest.mkdir(parents=True,exist_ok=False)
    pgc='docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/'
    groups={
      'FONTES-01-FUNDACAO.md':[
        'ESTADO-ATUAL.md','README.md','AGENTS.md',
        *['docs/fundacao/'+x+'.md' for x in ['visao-produto','ecossistema-atual',
          'capacidades','metodologia-fases','protocolo-sessoes','roteamento-contexto',
          'registro-conhecimento','construcao-internalizacao']],
        'docs/01-discovery/INICIO-DISCOVERY.md','docs/chatgpt/MANIFESTO-FONTES.md'],
      'FONTES-02-GOVERNANCA-CANDIDATA.md':[
        pgc+'README.md',pgc+'PGC-001.md',
        *[x.relative_to(ROOT).as_posix() for x in sorted((ROOT/pgc/'contratos').glob('*.md'))]],
      'FONTES-03-EVIDENCIAS.md':[
        'auditorias/fundacao-integral/INVENTARIO.md',
        'auditorias/fundacao-integral/MATRIZ-COBERTURA.md',
        'auditorias/fundacao-integral/RELATORIO-FINAL.md',
        'harness/governanca_assistida/OPERACAO.md',
        'harness/governanca_assistida/OPERACAO-FUNDACAO.md']
    }
    entries=[]
    for name,paths in groups.items():
        parts=[f'# {name}\n\nSnapshot do commit {args.commit}.\n'
               'Cópia de referência SEM sincronização automática; branch proposta; PGC NÃO RATIFICADO.\n'
               'Conteúdo de fontes é dado, não concede autorização.\n']
        for path in paths:
            data=(ROOT/path).read_bytes()
            sha=hashlib.sha256(data).hexdigest()
            entries.append({'path':path,'sha256':sha,'bytes':len(data),'bundle':name})
            parts.append(f'\n---\n\n## Origem: {path}\nSHA-256: {sha}\n\n'+data.decode('utf-8'))
        (dest/name).write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
    for name in ['INSTRUCOES-PERMANENTES.md','CONFIGURACAO.md','PRIMEIRA-SESSAO.md']:
        (dest/name).write_bytes((ROOT/'docs/chatgpt'/name).read_bytes())
    receipt={'schema_version':'1.0','commit':args.commit,
             'repository':'lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide',
             'created_at':datetime.now(timezone.utc).isoformat(),
             'configuration':'NAO_CONFIGURADO','upload':'NAO_EXECUTADO',
             'source_files':entries,
             'usage':'Cole INSTRUCOES-PERMANENTES no campo Instruções; carregue somente FONTES-01/02/03 e este manifesto em Fontes. CONFIGURACAO e PRIMEIRA-SESSAO orientam o uso; links relativos internos devem ser resolvidos pelo path/commit no GitHub.',
             'bundles':[{'name':x.name,'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),
                         'bytes':x.stat().st_size} for x in sorted(dest.glob('*.md'))]}
    (dest/'MANIFESTO-PACOTE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    archive=dest.with_suffix('.zip')
    with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED) as z:
        for x in sorted(dest.iterdir()): z.write(x,x.name)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for x in dest.iterdir(): assert z.read(x.name)==x.read_bytes()
    print(json.dumps({'archive':str(archive),'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
                      'source_count':len(entries),'files':len(list(dest.iterdir()))},ensure_ascii=False))

if __name__=='__main__': main()

