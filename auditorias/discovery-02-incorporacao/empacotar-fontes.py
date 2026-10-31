"""Empacota documentos remotos verificados; nao executa fontes nem aplica configuracao."""
import sys,json,hashlib,zipfile,re,posixpath,stat
from pathlib import Path
from urllib.parse import quote,unquote
cache=Path(sys.argv[1]).absolute()
out=Path(sys.argv[2]).absolute()
def safe_read(base,relative):
    assert relative and not relative.startswith('/') and ':' not in relative and '\\' not in relative and '..' not in relative.split('/')
    target=base/relative
    for ancestor in [*reversed(target.parents),target]:
        info=ancestor.lstat()
        assert not stat.S_ISLNK(info.st_mode) and not getattr(info,'st_reparse_tag',0),str(ancestor)
    assert stat.S_ISREG(target.lstat().st_mode)
    return target.read_bytes()
proof=json.loads(safe_read(cache,'ORIGEM-REMOTA.json'))
assert proof['repository']=='lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide'
assert re.fullmatch(r'[0-9a-f]{40}',proof['content_commit'])
out.mkdir(parents=True,exist_ok=False)
payload=out/'conteudo'
payload.mkdir()
files={}
source_data={}
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,b):
    f=payload/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b);files[p]={'path':p,'bytes':len(b),'sha256':sha(b)}
entries={e['path']:e for e in proof['entries']}
selected=proof['selected_paths']
assert selected==sorted(selected) and len(selected)==len(set(p.lower() for p in selected))
assert len(entries)==len(proof['entries'])
for p in selected:
    assert not p.startswith('/') and '..' not in p.split('/') and ':' not in p and '\\' not in p
    e=entries[p]
    assert e['mode']=='100644',p
    b=safe_read(cache,p)
    source_data[p]=b
    actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert actual==e['sha'] and len(b)==e['size'],p
    write('originais/'+p,b)
commit=proof['content_commit']
prefix='https://github.com/'+proof['repository']+'/blob/'+commit+'/'
mapping=[]
groups={i:[] for i in range(5)}
def group(p):
    if p.endswith('/FONTES.md') or p.endswith('/PROVENIENCIA-RECUPERADA.md') or p.startswith('docs/continuidade/') or p.startswith('auditorias/discovery-02-incorporacao/'):return 4
    if p.startswith('docs/01-discovery/discovery-02/') or p in ('ARCHITECTURE_BLUEPRINT.MD','docs/fundacao/axiomas-arquiteturais.md'):return 1
    if p.startswith('docs/01-discovery/discovery-01/') or p.startswith('auditorias/discovery-01'):return 2
    if p.startswith('docs/fundacao/') or p.startswith('docs/00-governanca/') or p.startswith('docs/06-execucao/'):return 3
    if '/' not in p or p.startswith('docs/chatgpt/') or p=='docs/01-discovery/INICIO-DISCOVERY.md':return 0
    return 4
names=['00-ENTRADA-E-CONFIGURACAO.md','01-DISCOVERY-02.md','02-DISCOVERY-01-HISTORICO.md','03-FUNDACAO-E-CANDIDATOS.md','04-PROVENIENCIA-E-PROVAS.md']
def native_source(p):
    if '/historico/' in p:return False
    if p.startswith('auditorias/'):
        return p in ('auditorias/discovery-02-incorporacao/BLUEPRINT-ORIGEM.md','auditorias/discovery-02-incorporacao/IDENTIDADE-ENTRADAS.json')
    if p.startswith('docs/chatgpt/') and p!='docs/chatgpt/MANIFESTO-FONTES.md':return False
    if p.startswith('docs/01-discovery/discovery-02/') and Path(p).name in ('REVISAO.md','MATRIZ.md'):return False
    if p.endswith('.json'):return p in ('docs/continuidade/CONT-REG-0002.json','docs/continuidade/MANIFESTO.json','docs/01-discovery/discovery-02/MANIFESTO.json')
    return p.lower().endswith('.md')
for p in sorted(selected):
    if not native_source(p):continue
    b=source_data[p]
    if p.lower().endswith('.md'):
        text=b.decode('utf8')
        def link(m):
            dest=m.group(2)
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',dest):return m.group(0)
            local,sep,anchor=dest.partition('#')
            target=posixpath.normpath(posixpath.join(posixpath.dirname(p),unquote(local))) if local else p
            if target in entries:
                url=prefix+quote(target,safe='/')+('#'+anchor if sep else '')
                mapping.append({'source':p,'original':dest,'destination':url,'disposition':'IMMUTABLE_GIT_REFERENCE'})
                return '['+m.group(1)+']('+url+')'
            mapping.append({'source':p,'original':dest,'destination':None,'disposition':'HISTORICAL_REFERENCE_UNAVAILABLE_OR_POSTERIOR_PENDING'})
            return m.group(1)+' [referencia historica indisponivel ou evidencia posterior ainda nao incluida; ver mapa]'
        # Transform only links outside fenced code; archived source bytes remain exact above.
        parts=re.split(r'(^\x60\x60\x60[^\n]*\n[\s\S]*?^\x60\x60\x60[^\n]*$)',text,flags=re.M)
        for i in range(0,len(parts),2):parts[i]=re.sub(r'\[([^\]]*)\]\(([^)\n]+)\)',link,parts[i])
        body=''.join(parts)
    elif p.endswith('.json'):
        body='\x60\x60\x60json\n'+b.decode('utf8')+'\n\x60\x60\x60'
    else:continue
    origin=prefix+quote(p,safe='/')
    header='\n\n---\n\n# '+p+'\n\nOrigem: ['+p+']('+origin+'#L1-L'+str(len(b.splitlines()))+'). Commit '+commit+'. Blob SHA-1 '+entries[p]['sha']+'. SHA-256 dos bytes originais '+sha(b)+'.\n\n'
    groups[group(p)].append(header+body)
for i,name in enumerate(names):
    title='# Fontes D02 — conjunto '+str(i)+' — revisao documental 1\n\nSnapshot '+commit+'; proposta, sem ratificacao. Cada trecho tem origem e identidade; links relativos foram mapeados a URLs imutaveis. Arquivos originais preservados separadamente. Nenhum upload ou campo nativo aplicado e comprovado por este pacote.\n'
    write('upload/'+name,(title+''.join(groups[i])+'\n').encode('utf8'))
instructions='docs/chatgpt/INSTRUCOES-PERMANENTES.md'
write('INSTRUCOES-PERMANENTES.md',source_data[instructions])
config='docs/chatgpt/CONFIGURACAO.md'
write('APLICACAO-E-RECUPERACAO.md',source_data[config])
write('MAPA-LINKS.json',(json.dumps(mapping,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode('utf8'))
readme=('# Entrega D02\n\nConteudo obtido pelo conector GitHub autenticado no commit '+commit+'.\n\n'
'1. Confira MANIFESTO-PACOTE.json e os hashes dos originais.\n'
'2. Em sessao autenticada no Projeto g-p-6ae4fdf0eb688191bb6536420421ef69, confira conta/workspace/visibilidade e guarde backup integral das Fontes/Instrucoes existentes.\n'
'3. Carregue os cinco arquivos upload/*.md como conjunto e confira inventario, conteudo integral e conflitos de versao conforme APLICACAO-E-RECUPERACAO.md. Se limites efetivos impedirem, mantenha a rota Git; nao fragmente sem novo mapa de cobertura.\n'
'4. So apos PS verificado, compare/mescle regras nativas legitimas desconhecidas e aplique o texto integral candidato INSTRUCOES-PERMANENTES.md. Releia campo completo e registre diff/modalidade.\n'
'5. Mantenha Fontes antigas identificadas como historicas; exclusao exige autorizacao separada. Sem controle de concorrencia seguro, pare a escrita dependente.\n'
'6. Execute os ensaios de conflito execucao local/Meso e as provas separadas; RF requer Fontes nativas efetivas. RN e uma nova conversa real iniciada pelo usuario.\n\n'
'Nao ha sincronizacao automatica. Mudanca canonica exige novo pacote/revisao, aplicacao, verificacao e recibo.\n'
'originais/ e arquivo de fontes byte a byte; links historicos desses originais sao preservados, nao sao rotas ativas. upload/ e a projecao navegavel, com mapa das transformacoes. Referencias historicas nao recebidas e recibos posteriores sao explicitados no mapa, sem fabricar arquivos.\n'
'Arquivos reservados ao operador: CONFIGURACAO, REVISAO/matriz de controles D02, PM completo, fixtures, pareceres e respostas de recuperacao ficam nos originais do ZIP e fora das Fontes de upload para preservar o oraculo do avaliador. Todo HUM/AX/D01 material e suas restricoes permanecem nas definicoes canonicas de upload; RF nao recebe o ZIP integral.\n'
'Exclusoes: codigo/harness e scripts herdados (sem execucao), logs crus historicos, ZIPs de acervo e arquivos nao documentais; nenhuma definicao critica D01/D02/axiomas/autoridade depende exclusivamente dessas exclusoes. Codigo e acervos continuam no Git imutavel, como dados; capacidades e limites historicos constam dos relatorios incluidos. Provas posteriores sao suplemento separado.\n')
write('LEIA-ME.md',readme.encode('utf8'))
manifest={'schema_version':'d02-package-1','repository':proof['repository'],'content_commit':commit,'content_tree':proof['content_tree'],'origin_channel':'GitHub connector fetch_file(ref=immutable commit, encoding=base64)','signature':'NOT_VERIFIED; SHA equality is not human authorship','selected_paths':selected,'files':[files[k] for k in sorted(files)],'upload_files':['upload/'+n for n in names],'native_source_paths':[p for p in selected if native_source(p)],'operator_only_paths':[p for p in selected if not native_source(p)],'rf_isolation':'Evaluator rubrics, PM control dossier, mission REVISAO/MATRIZ, fixtures, audits and recovery outputs excluded from upload; canonical product decisions retained. Native instructions/memory still require channel attribution.','coverage':'All accessible canonical D01/D02, ten axioms, retifications, matrices, provenance and candidate instructions; raw source originals plus transformed upload projections','exclusions':'See LEIA-ME.md','logical_digest':sha(json.dumps([files[k]for k in sorted(files)],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')),'posterior_evidence':'Separate supplement; not part of this content snapshot'}
write('MANIFESTO-PACOTE.json',(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode('utf8'))
for name in ('FONTES-D02.zip','FONTES-D02-repeticao.zip'):
    with zipfile.ZipFile(out/name,'x',compression=zipfile.ZIP_STORED)as z:
        for p in sorted(files):
            info=zipfile.ZipInfo(p,date_time=(1980,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_STORED
            z.writestr(info,(payload/p).read_bytes())
a=(out/'FONTES-D02.zip').read_bytes();b=(out/'FONTES-D02-repeticao.zip').read_bytes()
assert a==b
with zipfile.ZipFile(out/'FONTES-D02.zip')as z:
    assert z.testzip()is None
    for p,e in files.items():
        data=z.read(p);assert len(data)==e['bytes']and sha(data)==e['sha256']
receipt={'scope':'PACKAGE_NOT_NATIVE_CONFIGURATION','content_commit':commit,'content_tree':proof['content_tree'],'files':len(files),'selected_originals':len(selected),'zip_bytes':len(a),'zip_sha256':sha(a),'zip_repeat_identical':True,'zip_metadata':'ordered paths, fixed 1980 timestamp, Unix 100644, ZIP_STORED','python':sys.version,'logical_digest':manifest['logical_digest'],'manifest_sha256':files['MANIFESTO-PACOTE.json']['sha256'],'payload_reopened_and_verified':True}
(out/'RECIBO-PACOTE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,ensure_ascii=False))
