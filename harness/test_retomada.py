import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from verificar_retomada import verify


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.record = {'record_id': 'CONT-REG-0001', 'revision': 1,
                       'normative_effect': 'AUSENTE', 'product_approval': 'NAO_CONCEDIDA',
                       'source_kind': 'USER_DIRECT', 'source_ref': 'thread:test;message:test',
                       'request': 'Conteúdo de teste sintético para recuperação.'}
        self.manifest = {'schema_version': 'continuidade-1', 'repository': 'lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide',
                         'normative_effect': 'AUSENTE', 'record_path': 'registro.json',
                         'record_id': 'CONT-REG-0001', 'revision': 1, 'files': []}
        self.update()

    def update(self):
        data = json.dumps(self.record).encode()
        (self.root/'registro.json').write_bytes(data)
        self.manifest['files'] = [{'path': 'registro.json', 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}]
        self.save()

    def save(self):
        (self.root/'manifesto.json').write_text(json.dumps(self.manifest))

    def run_verify(self):
        return verify(self.root, self.root/'manifesto.json')

    def test_snapshot_valido_recupera_sem_aprovar(self):
        result = self.run_verify()
        self.assertEqual(result['record_id'], 'CONT-REG-0001')
        self.assertEqual(result['product_approval'], 'NAO_CONCEDIDA')

    def test_bytes_alterados_detectados(self):
        (self.root/'registro.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'INTEGRIDADE'): self.run_verify()

    def test_arquivo_ausente_nao_e_sucesso(self):
        (self.root/'registro.json').unlink()
        with self.assertRaises(FileNotFoundError): self.run_verify()

    def test_manifesto_de_outro_repositorio(self):
        self.manifest['repository'] = 'outro/repo'; self.save()
        with self.assertRaisesRegex(ValueError, 'REPOSITORIO'): self.run_verify()

    def test_caminho_fora_da_raiz(self):
        self.manifest['files'][0]['path'] = '../fora.json'; self.save()
        with self.assertRaisesRegex(ValueError, 'CAMINHO'): self.run_verify()

    def test_caminho_duplicado(self):
        self.manifest['files'] *= 2; self.save()
        with self.assertRaisesRegex(ValueError, 'DUPLICADO'): self.run_verify()

    def test_id_revisao_do_payload_devem_corresponder(self):
        self.record['revision'] = 2; self.update()
        with self.assertRaisesRegex(ValueError, 'IDENTIDADE'): self.run_verify()

    def test_efeito_normativo_recusado_mesmo_com_hash_valido(self):
        self.record['product_approval'] = 'APROVADO'; self.update()
        with self.assertRaisesRegex(ValueError, 'EFEITO'): self.run_verify()

    def test_origem_ausente_recusada(self):
        self.record['source_ref'] = ''; self.update()
        with self.assertRaisesRegex(ValueError, 'ORIGEM'): self.run_verify()


if __name__ == '__main__': unittest.main(verbosity=2)
