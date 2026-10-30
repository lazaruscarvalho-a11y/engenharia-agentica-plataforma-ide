"""Leitor de exportação de commits. Não consulta rede nem simula nova conversa."""
import argparse
from pathlib import Path
import sys
from fluxo import *

class SnapshotReader:
    def __init__(self,folder,head): self.folder=folder.resolve();self.head=head
    def context(self): return Context(REPO,BRANCH,self.head,True,True,False,False)
    def read(self,commit,path):
        require(sha(commit),'COMMIT_INVALIDO');safe_path(path)
        target=(self.folder/commit/path).resolve()
        require(target.is_relative_to(self.folder),'CAMINHO_FORA_DO_SNAPSHOT')
        return target.read_bytes()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Retomada somente de leitura em exportação explícita de commits.')
    parser.add_argument('--snapshot',required=True);parser.add_argument('--head',required=True)
    args=parser.parse_args()
    try:
        result=recover(SnapshotReader(Path(args.snapshot),args.head))
        result['evidence_scope']='EXPORTACAO_DE_COMMITS_NAO_CONVERSA_NOVA_REAL'
        sys.stdout.buffer.write(json_bytes(result))
    except (Blocked,FileNotFoundError,KeyError,ValueError) as exc:
        print('RETOMADA_NAO_CONFIRMADA: '+type(exc).__name__,file=sys.stderr);raise SystemExit(1)
