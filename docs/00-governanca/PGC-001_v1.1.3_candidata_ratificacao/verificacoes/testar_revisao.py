"""Regressões da revisão documental; NÃO executa nenhum cenário CA do harness."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE=Path(__file__).resolve().parents[1]

def snapshot(root):
    return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}

class DocumentRevisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='pgc-regressao-')
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'copia com espacos'
        shutil.copytree(SOURCE,self.root)

    def run_script(self,name,*args,seed='11',reverse=False):
        path=self.root/'verificacoes'/name
        env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONHASHSEED=seed)
        if reverse:
            shim="from pathlib import Path; import runpy,sys; old=Path.rglob; Path.rglob=lambda self,*a,**k:iter(reversed(list(old(self,*a,**k)))); script=sys.argv[1]; sys.argv=sys.argv[1:]; runpy.run_path(script,run_name='__main__')"
            cmd=[sys.executable,'-c',shim,str(path),*args]
        else:
            cmd=[sys.executable,str(path),*args]
        return subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env)

    def require_ok(self,result):
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

    def test_repeticao_e_seeds(self):
        before=snapshot(self.root)
        for seed in ('11','97'):
            self.require_ok(self.run_script('gerar_catalogo.py',seed=seed))
            self.require_ok(self.run_script('auditar_pacote.py',seed=seed))
            self.assertEqual(snapshot(self.root),before)

    def test_ordem_de_enumeracao_invertida(self):
        before=snapshot(self.root)
        self.require_ok(self.run_script('auditar_pacote.py',reverse=True))
        self.assertEqual(snapshot(self.root),before)

    def test_conferencia_sucesso_nao_escreve(self):
        before=snapshot(self.root)
        self.require_ok(self.run_script('gerar_catalogo.py','--check'))
        self.require_ok(self.run_script('auditar_pacote.py','--check'))
        self.assertEqual(snapshot(self.root),before)

    def test_catalogo_crlf_rejeitado_sem_escrita(self):
        file=self.root/'verificacoes/casos-adversariais.json'
        file.write_bytes(file.read_bytes().replace(b'\n',b'\r\n'))
        before=snapshot(self.root)
        result=self.run_script('gerar_catalogo.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(snapshot(self.root),before)

    def test_relatorio_crlf_rejeitado_sem_escrita(self):
        file=self.root/'verificacoes/relatorio-verificacao.md'
        file.write_bytes(file.read_bytes().replace(b'\n',b'\r\n'))
        before=snapshot(self.root)
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(snapshot(self.root),before)

    def test_vinculo_removido_do_json_detectado(self):
        file=self.root/'verificacoes/casos-adversariais.json'
        data=json.loads(file.read_bytes())
        data['cases'][0]['requirements'].remove('PGC-N-001')
        file.write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('FAIL Matriz e catálogo: vínculos bidirecionais idênticos',result.stdout)

    def test_vinculo_indevido_na_matriz_detectado(self):
        file=self.root/'MATRIZ-DE-RASTREABILIDADE.md'
        text=file.read_text(encoding='utf-8').replace('| CA-01, CA-36 |','| CA-01, CA-36, CA-49 |',1)
        file.write_bytes(text.encode())
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('FAIL Matriz e catálogo: vínculos bidirecionais idênticos',result.stdout)

    def test_created_at_nao_substitui_emissao(self):
        file=self.root/'contratos/CT-001-classificacao-aprovacao.md'
        file.write_bytes(file.read_text(encoding='utf-8').replace('`issued_at`, `approval_state`','`created_at`, `approval_state`').encode())
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('FAIL CT-001 Approval usa issued_at',result.stdout)

    def test_data_sem_fuso_rejeitada(self):
        file=self.root/'verificacoes/casos-adversariais.json'
        data=json.loads(file.read_bytes())
        data['fixtures']['F-PARCIAL-FORMAL']['approval']['issued_at']='2026-10-29T00:00:00'
        file.write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode())
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('FAIL CA-49 tem data de emissão sintética com fuso',result.stdout)

    def test_versao_contratual_antiga_rejeitada(self):
        file=self.root/'contratos/CT-003-publicacao-concorrencia.md'
        file.write_bytes(file.read_text(encoding='utf-8').replace('**Versão:** 1.0.3','**Versão:** 1.0.2').encode())
        result=self.run_script('auditar_pacote.py','--check')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('FAIL CT-003 v1.0.3 proposto',result.stdout)

if __name__=='__main__':
    unittest.main(verbosity=2)
