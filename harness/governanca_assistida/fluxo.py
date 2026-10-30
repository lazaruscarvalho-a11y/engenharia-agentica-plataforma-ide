"""INC-GOV-001: preparação e publicação ASSISTIDA C1, sem ativação normativa.

Não autentica pessoas. HumanReview só pode ser fornecido pelo operador depois
de consultar a manifestação humana no canal original. JSON de arquivo não é
essa confirmação. O adaptador de ferramentas impõe acesso e CAS reais.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Protocol

REPO='lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide'
BRANCH='piloto/governanca-assistida'
PREFIX='docs/01-discovery/governanca-assistida/'
PGC='2e7cb6019e7412dad8fb06315f624492feaf4fc1'

class Blocked(ValueError): pass
class Conflict(RuntimeError): pass
class Unknown(RuntimeError): pass

def require(ok,code):
    if not ok: raise Blocked(code)

def digest(data:bytes): return hashlib.sha256(data).hexdigest()
def json_bytes(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode('utf-8')
def now(): return datetime.now(timezone.utc).isoformat()
def timestamp(value):
    try: return datetime.fromisoformat(value.replace('Z','+00:00')).utcoffset() is not None
    except (ValueError,TypeError,AttributeError): return False
def sha(value): return isinstance(value,str) and re.fullmatch(r'[a-f0-9]{40}',value) is not None
def safe_path(path):
    require(isinstance(path,str) and path.startswith(PREFIX) and '\\' not in path and ':' not in path and all(p not in ('','..','.') for p in path.split('/')),'DESTINO_FORA_DO_ESCOPO')

@dataclass(frozen=True)
class Context:
    repository:str
    branch:str
    base_sha:str
    private:bool
    can_read:bool
    can_write:bool
    conditional_write:bool
    pgc_reference:str=PGC
    pgc_status:str='NAO_RATIFICADO'

@dataclass(frozen=True)
class Record:
    record_id:str
    revision:int
    title:str
    user_content:str
    proposed_details:list[str]
    source_ref:str
    source_kind:str='SYNTHETIC_INPUT'
    data_classification:str='SINTETICO'
    nature:str='C1'
    previous_revision:int|None=None

def validate_record(r:Record):
    require(re.fullmatch(r'GOV-REG-\d{4}',r.record_id) is not None,'ID_INVALIDO')
    require(type(r.revision) is int and r.revision>=1,'REVISAO_INVALIDA')
    require(r.previous_revision is None and r.revision==1 or type(r.previous_revision) is int and r.revision==r.previous_revision+1,'SUCESSAO_INVALIDA')
    require(r.nature=='C1' and r.data_classification=='SINTETICO','DADOS_OU_NATUREZA_FORA_DO_PILOTO')
    require(r.source_kind in ('USER_DIRECT','SYNTHETIC_INPUT') and bool(r.source_ref.strip()) and '\n' not in r.source_ref and '\r' not in r.source_ref,'ORIGEM_AUSENTE_OU_NAO_CONFIAVEL')
    require(bool(r.title.strip()) and '\n' not in r.title and bool(r.user_content.strip()),'CONTEUDO_INCOMPLETO')
    require(isinstance(r.proposed_details,list) and all(isinstance(x,str) for x in r.proposed_details),'INFERENCIAS_INVALIDAS')
    text='\n'.join([r.title,r.user_content,*r.proposed_details])
    require(not re.search(r'CHAVE_FICTICIA_SINTETICA_TESTE|-----BEGIN .*PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{20,}|(?i:ignore (?:o protocolo|as regras)|INSTRUÇÃO PRIORITÁRIA)',text),'CONTEUDO_REQUER_AVALIACAO_HUMANA')

def render(r:Record):
    validate_record(r)
    text=f'# {r.title}\n\nID: {r.record_id}\nRevisão: {r.revision}\nNatureza: C1\nMaturidade: PROPOSTO\nEfeito normativo: AUSENTE\nClassificação: SINTETICO\nOrigem: {r.source_ref}\nTipo de origem: {r.source_kind}\n\n## Conteúdo declarado\n\n{r.user_content}\n\n## Detalhes propostos pelo assistente\n\n'
    text+=('\n'.join('- '+x for x in r.proposed_details) if r.proposed_details else 'Nenhum detalhe adicional.')+'\n'
    return text.encode('utf-8')

def prepare(record:Record,context:Context,operation_id:str):
    require(re.fullmatch(r'GOV-OP-\d{4}',operation_id) is not None,'OPERACAO_INVALIDA')
    require(context.repository==REPO and context.branch==BRANCH and sha(context.base_sha),'DESTINO_OU_BASE_INVALIDO')
    require(context.private and context.can_read,'FONTE_PRIVADA_INACESSIVEL')
    require(context.pgc_reference==PGC and context.pgc_status=='NAO_RATIFICADO','REFERENCIA_PGC_DIVERGENTE')
    content=render(record)
    packet={'schema_version':'1.0','operation_id':operation_id,'record':asdict(record),'context':asdict(context),
            'path':PREFIX+'registros/'+record.record_id+'.md','content':content.decode(),
            'content_sha256':digest(content),'status':'PREPARADO_NAO_ACEITO','effect':'EXPLORATORIO_SEM_VIGENCIA'}
    packet['request_digest']=digest(json_bytes(packet))
    packet['review_code']=operation_id+'-R'+str(record.revision)+'-'+packet['request_digest'][:12]
    return packet

def validate_packet(packet):
    expected=prepare(Record(**packet['record']),Context(**packet['context']),packet['operation_id'])
    require(packet==expected,'PACOTE_ALTERADO_APOS_PREPARACAO')
    return expected

@dataclass(frozen=True)
class HumanReview:
    """Atestado manual do operador, não prova criptográfica de identidade."""
    review_code:str
    request_digest:str
    source_ref:str
    actor_ref:str
    issued_at:str
    decision:str
    scope:list[str]
    destination_repository:str
    destination_branch:str
    original_source_checked:bool
    source_kind:str='USER_DIRECT'
    revoked:bool=False

def validate_review(packet,review:HumanReview):
    require(type(review) is HumanReview,'CONFIRMACAO_OPERADOR_AUSENTE')
    require(review.source_kind=='USER_DIRECT' and review.original_source_checked,'FONTE_HUMANA_NAO_CONFERIDA')
    require(bool(review.source_ref.strip()) and bool(review.actor_ref.strip()) and timestamp(review.issued_at),'EVIDENCIA_HUMANA_INCOMPLETA')
    require(review.decision=='ACEITO_PARA_REGISTRO' and not review.revoked,'ACEITE_AUSENTE_AMBIGUO_OU_REVOGADO')
    require(review.review_code==packet['review_code'] and review.request_digest==packet['request_digest'],'ACEITE_DE_OUTRA_REVISAO')
    require(review.scope==[packet['path']],'ACEITE_PARCIAL_EXIGE_NOVA_PREPARACAO')
    require(review.destination_repository==REPO and review.destination_branch==BRANCH,'ACEITE_DE_OUTRO_DESTINO')

class Gateway(Protocol):
    def context(self)->Context: ...
    def read(self,commit:str,path:str)->bytes: ...
    def lookup(self,operation_id:str)->str|None: ...
    def publish(self,base_sha:str,files:dict[str,bytes],operation_id:str)->str: ...

class Journal:
    """Diário local explícito; não é fila nem prova de aprovação humana."""
    def __init__(self,path:Path): self.path=path
    def load(self):
        return json.loads(self.path.read_bytes()) if self.path.exists() else {}
    def save(self,operation_id,value):
        records=self.load();records[operation_id]=value
        self.path.parent.mkdir(parents=True,exist_ok=True)
        tmp=self.path.with_suffix('.tmp')
        tmp.write_bytes(json_bytes(records));tmp.replace(self.path)

def verify_commit(packet,commit,gateway):
    require(sha(commit),'COMMIT_INVALIDO')
    data=gateway.read(commit,packet['path'])
    require(data==packet['content'].encode() and digest(data)==packet['content_sha256'],'DIVERGENCIA_NA_RELEITURA')
    evidence=json.loads(gateway.read(commit,PREFIX+'aceites/'+packet['operation_id']+'.json'))
    require(evidence.get('request_digest')==packet['request_digest'] and evidence.get('kind')=='ACEITE_DE_REGISTRO_NAO_NORMATIVO','OPERACAO_EXISTENTE_COM_OUTRO_PAYLOAD')

def _receipt(packet,record_commit,review):
    return {'schema_version':'1.0','operation_id':packet['operation_id'],'record_id':packet['record']['record_id'],
            'revision':packet['record']['revision'],'path':packet['path'],'repository':REPO,'branch':BRANCH,
            'record_commit':record_commit,'sha256':packet['content_sha256'],'request_digest':packet['request_digest'],
            'content_acceptance':'ACEITO_PARA_REGISTRO_EXPLORATORIO','acceptance_source':review.source_ref,
            'issued_at':review.issued_at,'publication':'PUBLICADO','verification':'BYTES_CONFERIDOS',
            'normative_effect':'AUSENTE','pgc_status':'NAO_RATIFICADO','verified_at':now(),
            'next_action':'Retomar por INDICE.json em outra conversa; revalidar a origem antes de nova escrita.'}

def publish_assisted(packet,review:HumanReview,gateway:Gateway,journal:Journal):
    """Uma rodada de registro; recibo em commit separado, sem retry cego."""
    validate_packet(packet);validate_review(packet,review)
    ctx=gateway.context()
    require(ctx.repository==REPO and ctx.branch==BRANCH and ctx.private and ctx.can_read,'DESTINO_NAO_CONFIRMADO')
    require(ctx.can_write and ctx.conditional_write,'NAO_PERSISTIDO_SEM_ESCRITA_CONDICIONAL')
    require(ctx.pgc_reference==PGC and ctx.pgc_status=='NAO_RATIFICADO','PGC_MUDOU')
    op=packet['operation_id']; stored=journal.load().get(op)
    if stored:
        require(stored['request_digest']==packet['request_digest'],'OPERACAO_REUSADA_COM_OUTRO_PAYLOAD')
        if stored['state']=='VERIFICADO':
            verify_commit(packet,stored['record_commit'],gateway)
            receipt_data=gateway.read(stored['receipt_commit'],stored['receipt_path'])
            require(digest(receipt_data)==stored['receipt_sha256'],'RECIBO_DIVERGENTE')
            return stored
        # Ainda que o processo anterior tenha caído, não enviar de novo.
        try: found=gateway.lookup(op)
        except Exception:
            return {**stored,'state':'INDETERMINADO_SEM_NOVA_TENTATIVA'}
        return {**stored,'state':'PUBLICADO_PENDENTE_RECONCILIACAO' if found else 'NAO_PUBLICADO_SEM_NOVA_TENTATIVA','record_commit':found}
    # Reconhecer operação já existente mesmo sem diário local (nova sessão).
    try: found=gateway.lookup(op)
    except Exception: raise Blocked('CONSULTA_DA_OPERACAO_INDISPONIVEL')
    if found:
        verify_commit(packet,found,gateway)
        return {'state':'PUBLICADO_PENDENTE_RECONCILIACAO','record_commit':found,'operation_id':op,'request_digest':packet['request_digest']}
    require(ctx.base_sha==packet['context']['base_sha'],'BASE_MUDOU_REAPRESENTAR')
    # ID estável: inexistente na revisão 1; sucessora deve corresponder à anterior.
    try: previous=gateway.read(ctx.base_sha,packet['path'])
    except FileNotFoundError: previous=None
    r=packet['record']
    if previous is not None:
        header=previous.decode('utf-8').split('## Conteúdo declarado',1)[0]
        previous_ok=re.search(r'^ID: '+re.escape(r['record_id'])+r'$',header,re.M) is not None and re.search(r'^Revisão: '+str(r['previous_revision'])+r'$',header,re.M) is not None
    else:
        previous_ok=False
    require(previous is None if r['revision']==1 else previous_ok,'IDENTIDADE_OU_REVISAO_CONFLITANTE')
    state={'operation_id':op,'request_digest':packet['request_digest'],'state':'PUBLICACAO_ENVIADA','attempts':1}
    journal.save(op,state)
    files={packet['path']:packet['content'].encode(),PREFIX+'aceites/'+op+'.json':json_bytes({'kind':'ACEITE_DE_REGISTRO_NAO_NORMATIVO','human_review':asdict(review),'request_digest':packet['request_digest']})}
    try:
        commit=gateway.publish(ctx.base_sha,files,op)
    except Conflict:
        state.update(state='CONFLITO_NAO_PUBLICADO');journal.save(op,state);return state
    except Exception:
        try: commit=gateway.lookup(op)
        except Exception: commit=None;state.update(state='INDETERMINADO_SEM_NOVA_TENTATIVA')
        if not commit:
            if state['state']!='INDETERMINADO_SEM_NOVA_TENTATIVA': state['state']='NAO_PUBLICADO_SEM_NOVA_TENTATIVA'
            journal.save(op,state);return state
    state.update(record_commit=commit,state='PUBLICADO_VERIFICACAO_PENDENTE');journal.save(op,state)
    try:
        verify_commit(packet,commit,gateway)
    except Exception:
        state['state']='PUBLICADO_VERIFICACAO_FALHOU';journal.save(op,state);return state
    receipt=_receipt(packet,commit,review)
    receipt_path=PREFIX+'recibos/'+op+'.json'; receipt_data=json_bytes(receipt)
    entry={'schema_version':'1.0','repository':REPO,'branch':BRANCH,'pgc_status':'NAO_RATIFICADO','record_id':r['record_id'],'revision':r['revision'],
           'path':packet['path'],'record_commit':commit,'record_sha256':packet['content_sha256'],'receipt_path':receipt_path,'receipt_sha256':digest(receipt_data)}
    try:
        rc=gateway.publish(commit,{receipt_path:receipt_data,PREFIX+'INDICE.json':json_bytes(entry)},op+'-RECIBO')
        require(gateway.read(rc,receipt_path)==receipt_data and gateway.read(rc,PREFIX+'INDICE.json')==json_bytes(entry),'RECIBO_NAO_CONFIRMADO')
    except Exception:
        state['state']='PUBLICADO_RECIBO_PENDENTE';journal.save(op,state);return state
    state.update(state='VERIFICADO',receipt_commit=rc,receipt_path=receipt_path,receipt_sha256=digest(receipt_data),normative_effect='AUSENTE')
    journal.save(op,state);return state

def reconcile(packet,gateway:Gateway,journal:Journal):
    """Somente leitura remota; reconhece efeitos sem repetir publicação."""
    validate_packet(packet)
    ctx=gateway.context()
    require(ctx.repository==REPO and ctx.branch==BRANCH and ctx.private and ctx.can_read,'FONTE_INACESSIVEL')
    stored=journal.load().get(packet['operation_id'])
    require(stored is not None and stored['request_digest']==packet['request_digest'],'OPERACAO_LOCAL_AUSENTE_OU_DIVERGENTE')
    try:
        commit=gateway.lookup(packet['operation_id'])
        if not commit: return {**stored,'state':'NAO_PUBLICADO_SEM_NOVA_TENTATIVA'}
        verify_commit(packet,commit,gateway)
        rc=gateway.lookup(packet['operation_id']+'-RECIBO')
        if not rc: return {**stored,'state':'PUBLICADO_RECIBO_PENDENTE','record_commit':commit}
        receipt_path=PREFIX+'recibos/'+packet['operation_id']+'.json'
        data=gateway.read(rc,receipt_path); receipt=json.loads(data)
        entry=json.loads(gateway.read(rc,PREFIX+'INDICE.json'))
        require(receipt['record_commit']==commit and receipt['sha256']==packet['content_sha256'] and receipt['request_digest']==packet['request_digest'] and entry['receipt_sha256']==digest(data) and entry['record_commit']==commit and entry['path']==packet['path'],'RECIBO_INCONSISTENTE')
        state={**stored,'state':'VERIFICADO','record_commit':commit,'receipt_commit':rc,'receipt_path':receipt_path,'receipt_sha256':digest(data),'normative_effect':'AUSENTE'}
        journal.save(packet['operation_id'],state);return state
    except Exception:
        return {**stored,'state':'INDETERMINADO_SEM_NOVA_TENTATIVA'}

def recover(gateway:Gateway):
    """Leitura pelo índice; não aceita referências externas como instruções."""
    ctx=gateway.context()
    require(ctx.repository==REPO and ctx.branch==BRANCH and ctx.private and ctx.can_read,'FONTE_INACESSIVEL')
    entry=json.loads(gateway.read(ctx.base_sha,PREFIX+'INDICE.json'))
    require(entry['repository']==REPO and entry['branch']==BRANCH and entry['pgc_status']=='NAO_RATIFICADO','INDICE_INVALIDO')
    require(sha(entry['record_commit']) and re.fullmatch(r'GOV-REG-\d{4}',entry['record_id']) is not None and type(entry['revision']) is int and entry['revision']>=1,'IDENTIDADE_DA_RETOMADA_INVALIDA')
    safe_path(entry['path']);safe_path(entry['receipt_path'])
    content=gateway.read(entry['record_commit'],entry['path'])
    receipt_data=gateway.read(ctx.base_sha,entry['receipt_path'])
    require(digest(content)==entry['record_sha256'] and digest(receipt_data)==entry['receipt_sha256'],'INTEGRIDADE_DA_RETOMADA_FALHOU')
    receipt=json.loads(receipt_data)
    require(receipt['repository']==REPO and receipt['branch']==BRANCH and receipt['record_commit']==entry['record_commit'] and receipt['sha256']==entry['record_sha256'] and receipt['path']==entry['path'] and receipt['record_id']==entry['record_id'] and receipt['revision']==entry['revision'] and receipt['normative_effect']=='AUSENTE' and receipt['pgc_status']=='NAO_RATIFICADO','RECIBO_INCONSISTENTE')
    return {'record_id':entry['record_id'],'revision':entry['revision'],'content':content.decode('utf-8'),'record_commit':entry['record_commit'],
            'receipt':receipt,'acceptance_origin_status':'NAO_REVALIDADA_NESTA_SESSAO','normative_effect':'AUSENTE',
            'next_action':'Consultar a origem humana antes de qualquer nova escrita; sem acesso, não reutilizar o aceite.'}

def main():
    parser=argparse.ArgumentParser(description='Preparação local C1; publicação exige operador e gateway autorizado.')
    subs=parser.add_subparsers(dest='command',required=True)
    p=subs.add_parser('preparar');p.add_argument('--registro',required=True);p.add_argument('--contexto',required=True);p.add_argument('--operacao',required=True);p.add_argument('--saida',required=True)
    p=subs.add_parser('conferir');p.add_argument('pacote')
    args=parser.parse_args()
    if args.command=='preparar':
        packet=prepare(Record(**json.loads(Path(args.registro).read_bytes())),Context(**json.loads(Path(args.contexto).read_bytes())),args.operacao)
        out=Path(args.saida);out.mkdir(parents=True,exist_ok=False)
        (out/'pacote.json').write_bytes(json_bytes(packet));(out/'registro.md').write_bytes(packet['content'].encode())
        print(json.dumps({'review_code':packet['review_code'],'request_digest':packet['request_digest'],'path':packet['path'],'status':'PREPARADO_NAO_ACEITO'},ensure_ascii=False))
    else:
        packet=json.loads(Path(args.pacote).read_bytes());validate_packet(packet)
        print('PASS: conteúdo preparado íntegro; NÃO comprova aceite humano ou publicação.')

if __name__=='__main__': main()
