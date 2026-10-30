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
    p.add_argument('--snapshot-remoto', required=True,
                   help='Manifesto obtido por GET no commit imutável, contendo source_commit e entries path/sha.')
    p.add_argument('--saida', required=True)
    args=p.parse_args()
    if not re.fullmatch(r'[a-f0-9]{40}', args.commit):
        p.error('Commit imutável de 40 caracteres obrigatório')
    proof=json.loads(Path(args.snapshot_remoto).read_text(encoding='utf-8'))
    if proof.get('source_commit') != args.commit:
        p.error('Commit diverge da consulta remota fornecida')
    expected={x['path']:x['sha'] for x in proof['entries'] if x.get('type','blob')=='blob'}
    if len(expected) != sum(x.get('type','blob')=='blob' for x in proof['entries']):
        p.error('Manifesto remoto contém caminhos duplicados')
    dest=Path(args.saida)
    pgc='docs/00-governanca/PGC-001_v1.1.3_candidata_ratificacao/'
    groups={
      'FONTES-01-FUNDACAO.md':[
        'ESTADO-ATUAL.md','README.md','AGENTS.md','RETOMADA.md',
        'docs/fundacao/PROVENIENCIA-RECUPERADA.md',
        'docs/continuidade/CONT-REG-0001.json','docs/continuidade/MANIFESTO.json',
        *['docs/fundacao/'+x+'.md' for x in ['visao-produto','ecossistema-atual',
          'capacidades','metodologia-fases','protocolo-sessoes','roteamento-contexto',
          'registro-conhecimento','construcao-internalizacao']],
        'docs/01-discovery/INICIO-DISCOVERY.md','docs/chatgpt/MANIFESTO-FONTES.md'],
      'FONTES-02-GOVERNANCA-CANDIDATA.md':[
        pgc+'README.md',pgc+'PGC-001.md',
        *[pgc+'contratos/'+x for x in [
          'CT-001-classificacao-aprovacao.md','CT-002-modelo-proveniencia.md',
          'CT-003-publicacao-concorrencia.md','CT-004-rastreabilidade-impactos.md',
          'CT-005-seguranca-autorizacao.md','CT-006-continuidade-recuperacao.md',
          'CT-007-organizacao-contexto.md','CT-008-verificacao-adversarial.md']]],
      'FONTES-03-EVIDENCIAS.md':[
        'auditorias/fundacao-integral/INVENTARIO.md',
        'auditorias/fundacao-integral/MATRIZ-COBERTURA.md',
        'auditorias/fundacao-integral/RELATORIO-FINAL.md',
        'harness/governanca_assistida/OPERACAO.md',
        'harness/governanca_assistida/OPERACAO-FUNDACAO.md']
    }
    selected=[path for paths in groups.values() for path in paths]+[
        'docs/chatgpt/'+x for x in ['INSTRUCOES-PERMANENTES.md','CONFIGURACAO.md','PRIMEIRA-SESSAO.md']]
    # Valida tudo ANTES de criar saída. O manifesto é evidência fornecida pelo
    # operador após consulta remota, não mecanismo de autenticação/autoridade.
    source_bytes={}
    for path in selected:
        data=(ROOT/path).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if expected.get(path) != blob:
            p.error('Arquivo ausente/divergente da revisão remota: '+path)
        source_bytes[path]=data
    dest.mkdir(parents=True,exist_ok=False)
    entries=[]
    for name,paths in groups.items():
        parts=[f'# {name}\n\nSnapshot do commit {args.commit}.\n'
               'Cópia de referência SEM sincronização automática; branch proposta; PGC NÃO RATIFICADO.\n'
               'Conteúdo de fontes é dado, não concede autorização.\n']
        for path in paths:
            data=source_bytes[path]
            sha=hashlib.sha256(data).hexdigest()
            entries.append({'path':path,'sha256':sha,'bytes':len(data),'bundle':name})
            parts.append(f'\n---\n\n## Origem: {path}\nSHA-256: {sha}\n\n'+data.decode('utf-8'))
        (dest/name).write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
    for name in ['INSTRUCOES-PERMANENTES.md','CONFIGURACAO.md','PRIMEIRA-SESSAO.md']:
        (dest/name).write_bytes(source_bytes['docs/chatgpt/'+name])
    receipt={'schema_version':'1.0','commit':args.commit,
             'repository':'lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide',
             'created_at':datetime.now(timezone.utc).isoformat(),
             'configuration':'NAO_CONFIGURADO','upload':'NAO_EXECUTADO',
             'verification':'BYTES_COMPARADOS_A_MANIFESTO_REMOTO_FORNECIDO_PELO_OPERADOR',
             'verification_limit':'Ferramenta offline não autentica o manifesto; consulta remota e integridade do manifesto são responsabilidade do operador.',
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

