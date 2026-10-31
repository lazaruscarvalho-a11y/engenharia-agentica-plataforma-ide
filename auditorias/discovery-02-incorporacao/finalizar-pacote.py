"""Corrige apenas projecao de links do manual em novo pacote; preserva emissao anterior."""
import sys,json,hashlib,shutil,re,posixpath,zipfile
from pathlib import Path
from urllib.parse import quote
root=Path(sys.argv[1]).resolve()
src=(root/'entrega-fontes-D02-v1').resolve()
dest=(root/'entrega-fontes-D02-v2').resolve()
assert src.parent==root and dest.parent==root and not dest.exists()
shutil.copytree(src,dest)
payload=dest/'conteudo'
cache=root/'remote-content-991e56a9'
proof=json.loads((cache/'ORIGEM-REMOTA.json').read_bytes())
entries={e['path']:e for e in proof['entries']}
prefix='https://github.com/'+proof['repository']+'/blob/'+proof['content_commit']+'/'
source='docs/chatgpt/CONFIGURACAO.md'
text=(cache/source).read_text(encoding='utf8')
mapping=json.loads((payload/'MAPA-LINKS.json').read_bytes())
def link(m):
    relative=m.group(2)
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',relative):return m.group(0)
    local,sep,anchor=relative.partition('#')
    target=posixpath.normpath(posixpath.join(posixpath.dirname(source),local)) if local else source
    assert target in entries,target
    url=prefix+quote(target,safe='/')+('#'+anchor if sep else '')
    mapping.append({'source':source,'projection':'APLICACAO-E-RECUPERACAO.md','original':relative,'destination':url,'disposition':'IMMUTABLE_GIT_REFERENCE'})
    return '['+m.group(1)+']('+url+')'
projected=re.sub(r'\[([^\]]*)\]\(([^)\n]+)\)',link,text)
(payload/'APLICACAO-E-RECUPERACAO.md').write_text(projected,encoding='utf8',newline='\n')
(payload/'MAPA-LINKS.json').write_text(json.dumps(mapping,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8',newline='\n')
shutil.copyfile(cache/'ORIGEM-REMOTA.json',payload/'ORIGEM-REMOTA.json')
def sha(b):return hashlib.sha256(b).hexdigest()
def inventory():
    return [{'path':p.relative_to(payload).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in sorted(payload.rglob('*')) if p.is_file() and p.name!='MANIFESTO-PACOTE.json']
manifest=json.loads((payload/'MANIFESTO-PACOTE.json').read_bytes())
manifest['package_revision']=2
manifest['transformation_delta']='Standalone operator manual links resolved to immutable Git URLs; raw source originals unchanged; remote source proof included'
manifest['files']=inventory()
manifest['logical_digest']=sha(json.dumps(manifest['files'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8'))
(payload/'MANIFESTO-PACOTE.json').write_text(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8',newline='\n')
allfiles=[p for p in sorted(payload.rglob('*')) if p.is_file()]
for name in ('FONTES-D02.zip','FONTES-D02-repeticao.zip'):
    with zipfile.ZipFile(dest/name,'w',compression=zipfile.ZIP_STORED) as z:
        for p in allfiles:
            info=zipfile.ZipInfo(p.relative_to(payload).as_posix(),date_time=(1980,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_STORED
            z.writestr(info,p.read_bytes())
a=(dest/'FONTES-D02.zip').read_bytes()
assert a==(dest/'FONTES-D02-repeticao.zip').read_bytes()
with zipfile.ZipFile(dest/'FONTES-D02.zip') as z:
    assert z.testzip() is None
    for e in manifest['files']:assert sha(z.read(e['path']))==e['sha256'] and len(z.read(e['path']))==e['bytes']
    assert z.read('MANIFESTO-PACOTE.json')==(payload/'MANIFESTO-PACOTE.json').read_bytes()
for p in proof['selected_paths']:
    assert (payload/'originais'/p).read_bytes()==(cache/p).read_bytes()
critical=['docs/01-discovery/discovery-02/REGISTRO.md','docs/fundacao/axiomas-arquiteturais.md','ARCHITECTURE_BLUEPRINT.MD','docs/01-discovery/discovery-02/RETIFICACOES.md','docs/01-discovery/discovery-01/REGISTRO.md','docs/01-discovery/discovery-01/REVISAO.md','docs/01-discovery/discovery-02/MODELO-FUNCIONAL.md','docs/01-discovery/discovery-02/CONTRATOS-CANDIDATOS.md','docs/01-discovery/discovery-02/AVALIACAO.md']
assert all(p in manifest['native_source_paths']for p in critical)
assert not any(re.search(r'CENARIOS|ORACULOS|CONFIGURACAO|AUDITORIA|entradas/',p)for p in manifest['native_source_paths'])
for active in [payload/'APLICACAO-E-RECUPERACAO.md',*[payload/p for p in manifest['upload_files']]]:
    text=active.read_text(encoding='utf8')
    text=re.sub(r'^\x60\x60\x60[^\n]*\n[\s\S]*?^\x60\x60\x60\s*$','',text,flags=re.M)
    for m in re.finditer(r'\[[^\]]*\]\(([^)\n]+)\)',text):
        d=m.group(1)
        assert re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',d) or d.startswith('#') or (active.parent/d.split('#')[0]).is_file(),(active,d)
receipt={'schema_version':'d02-package-receipt-2','scope':'REMOTE_VERIFIED_DOCUMENT_PACKAGE_NOT_NATIVE_CONFIGURATION','package_revision':2,'content_commit':proof['content_commit'],'content_tree':proof['content_tree'],'selected_originals':len(proof['selected_paths']),'files':len(allfiles),'native_source_paths':len(manifest['native_source_paths']),'upload_files':manifest['upload_files'],'all_original_bytes_equal_remote_cache':True,'critical_owners_all_in_upload':True,'evaluator_rubrics_excluded_from_upload':True,'active_links_validated':True,'mapped_links':len(mapping),'zip_bytes':len(a),'zip_sha256':sha(a),'zip_repeat_identical':True,'zip_metadata':'sorted files, timestamp1980, Unix100644, ZIP_STORED','logical_digest':manifest['logical_digest'],'manifest_sha256':sha((payload/'MANIFESTO-PACOTE.json').read_bytes()),'payload_reopened_and_verified':True,'prior_emission':'entrega-fontes-D02-v1 retained; first package verification found two unadapted manual relative links; revision2 corrected projection only'}
(dest/'RECIBO-PACOTE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps(receipt,ensure_ascii=False))
