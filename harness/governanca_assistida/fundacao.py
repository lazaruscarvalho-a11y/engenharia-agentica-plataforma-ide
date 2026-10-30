"""Fundação assistida local: C0 exploratório e Gateway SQLite para o piloto C1.

Não conecta ao GitHub, não autentica pessoas e não ativa normas. Commits locais
são identificadores de snapshots sintéticos; não são commits Git remotos.
"""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sqlite3

from fluxo import (Blocked, BRANCH, Conflict, Context, PREFIX, REPO, Unknown,
                   digest, json_bytes, prepare, Record, require, safe_path)

ZERO = '0' * 40
SOURCE_KINDS = {'SYNTHETIC_INPUT', 'SYNTHETIC_DOCUMENT'}


@dataclass(frozen=True)
class Draft:
    """Proposta C0 sem aceite de conteúdo nem efeito normativo."""
    record_id: str
    revision: int
    kind: str
    title: str
    body: str
    source_ref: str
    source_kind: str = 'SYNTHETIC_INPUT'
    classification: str = 'SINTETICO'
    nature: str = 'C0'
    maturity: str = 'PROPOSTO'


def validate_draft(value: Draft):
    require(type(value) is Draft, 'ESQUEMA_INVALIDO')
    require(isinstance(value.record_id, str) and
            re.fullmatch(r'FUND-(?:IDEA|HYP|PEND|DEC)-\d{4}', value.record_id), 'ID_INVALIDO')
    require(type(value.revision) is int and value.revision >= 1, 'REVISAO_INVALIDA')
    require(value.kind in {'IDEIA', 'HIPOTESE', 'PENDENCIA', 'DECISAO_PROPOSTA'}, 'TIPO_INVALIDO')
    expected = {'IDEIA': 'IDEA', 'HIPOTESE': 'HYP', 'PENDENCIA': 'PEND', 'DECISAO_PROPOSTA': 'DEC'}
    require(value.record_id.split('-')[1] == expected[value.kind], 'ID_TIPO_DIVERGENTE')
    require(value.classification == 'SINTETICO' and value.nature == 'C0' and
            value.maturity == 'PROPOSTO', 'CLASSIFICACAO_OU_EFEITO_PROIBIDO')
    require(value.source_kind in SOURCE_KINDS and isinstance(value.source_ref, str) and
            value.source_ref.startswith('synthetic://') and '\n' not in value.source_ref and
            '\r' not in value.source_ref, 'PROVENIENCIA_INVALIDA')
    require(all(isinstance(x, str) and x.strip() for x in (value.title, value.body)), 'CONTEUDO_AUSENTE')
    require(len(value.title) <= 300 and len(value.body) <= 100_000 and
            len(value.source_ref) <= 1000, 'LIMITE_EXCEDIDO')
    # Barreiras de fixture, não detector universal de DLP ou prompt injection.
    text = '\n'.join((value.title, value.body, value.source_ref))
    require(not re.search(r'CHAVE_FICTICIA_SINTETICA_TESTE|-----BEGIN .*PRIVATE KEY|'
                          r'gh[pousr]_[A-Za-z0-9]{20,}|(?i:ignore (?:o protocolo|as regras)|'
                          r'ignore previous instructions|INSTRUÇÃO PRIORITÁRIA)', text),
            'QUARENTENA_REQUER_REVISAO')


class SQLiteGateway:
    """Gateway transacional SOMENTE LOCAL para ensaiar o contrato do piloto.

    BEGIN IMMEDIATE serializa escritores. O HEAD esperado é conferido dentro da
    transação; operações têm ID único e payload imutável. Nenhum token é aceito.
    """
    def __init__(self, database: Path | str, timeout: float = 2.0):
        self.database = str(database)
        self.timeout = timeout
        self.fault = None  # injeção explícita de falha em ensaio sintético
        with self._connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS snapshots (id TEXT PRIMARY KEY, files BLOB NOT NULL);
                CREATE TABLE IF NOT EXISTS meta (name TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS operations
                  (id TEXT PRIMARY KEY, request_digest TEXT NOT NULL, snapshot TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS drafts
                  (id TEXT NOT NULL, revision INTEGER NOT NULL, data BLOB NOT NULL,
                   PRIMARY KEY(id, revision));
                CREATE TABLE IF NOT EXISTS draft_operations
                  (id TEXT PRIMARY KEY, request_digest TEXT NOT NULL, receipt BLOB NOT NULL);
            ''')
            db.execute('INSERT OR IGNORE INTO snapshots VALUES (?,?)', (ZERO, json_bytes({})))
            db.execute('INSERT OR IGNORE INTO meta VALUES (?,?)', ('head', ZERO))

    @contextmanager
    def _connect(self):
        connection = sqlite3.connect(self.database, timeout=self.timeout)
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def context(self):
        with self._connect() as db:
            head = db.execute("SELECT value FROM meta WHERE name='head'").fetchone()[0]
        # Estas flags identificam SOMENTE a fixture sintética local.
        return Context(REPO, BRANCH, head, True, True, True, True)

    def read(self, commit: str, path: str) -> bytes:
        safe_path(path)
        with self._connect() as db:
            row = db.execute('SELECT files FROM snapshots WHERE id=?', (commit,)).fetchone()
        if row is None:
            raise FileNotFoundError('SNAPSHOT_LOCAL_AUSENTE')
        files = json.loads(row[0])
        if path not in files:
            raise FileNotFoundError(path)
        return base64.b64decode(files[path], validate=True)

    def lookup(self, operation_id: str) -> str | None:
        with self._connect() as db:
            row = db.execute('SELECT snapshot FROM operations WHERE id=?', (operation_id,)).fetchone()
        return row[0] if row else None

    def publish(self, base_sha: str, files: dict[str, bytes], operation_id: str) -> str:
        require(isinstance(operation_id, str) and
                re.fullmatch(r'GOV-OP-\d{4}(?:-RECIBO)?', operation_id), 'OPERACAO_INVALIDA')
        require(isinstance(files, dict) and len(files) == 2 and
                all(type(v) is bytes for v in files.values()), 'CHANGESET_INVALIDO')
        for path in files:
            safe_path(path)
        op = operation_id.removesuffix('-RECIBO')
        if operation_id.endswith('-RECIBO'):
            require(set(files) == {PREFIX+'recibos/'+op+'.json', PREFIX+'INDICE.json'},
                    'CHANGESET_RECIBO_FORA_DO_ESCOPO')
        else:
            records = [p for p in files if re.fullmatch(re.escape(PREFIX)+r'registros/GOV-REG-\d{4}\.md', p)]
            require(len(records) == 1 and set(files) == {records[0], PREFIX+'aceites/'+op+'.json'},
                    'CHANGESET_REGISTRO_FORA_DO_ESCOPO')
        encoded = {p: base64.b64encode(v).decode('ascii') for p, v in files.items()}
        payload_digest = digest(json_bytes({'base': base_sha, 'files': encoded}))
        if self.fault == 'before':
            raise TimeoutError('FALHA_SINTETICA_ANTES_DA_TRANSACAO')
        with self._connect() as db:
            try:
                db.execute('BEGIN IMMEDIATE')
                old = db.execute('SELECT request_digest,snapshot FROM operations WHERE id=?',
                                 (operation_id,)).fetchone()
                if old:
                    require(old[0] == payload_digest, 'OPERACAO_REUSADA_COM_OUTRO_PAYLOAD')
                    return old[1]
                head = db.execute("SELECT value FROM meta WHERE name='head'").fetchone()[0]
                if head != base_sha:
                    raise Conflict('CAS_LOCAL_RECUSOU_BASE_ANTIGA')
                current = json.loads(db.execute('SELECT files FROM snapshots WHERE id=?', (head,)).fetchone()[0])
                current.update(encoded)
                snapshot = digest(json_bytes({'base': head, 'operation': operation_id, 'files': current}))[:40]
                db.execute('INSERT INTO snapshots VALUES (?,?)', (snapshot, json_bytes(current)))
                db.execute('INSERT INTO operations VALUES (?,?,?)', (operation_id, payload_digest, snapshot))
                db.execute("UPDATE meta SET value=? WHERE name='head'", (snapshot,))
                db.commit()
            except sqlite3.OperationalError as exc:
                raise Unknown('SQLITE_LOCAL_INDISPONIVEL_CONSULTAR_ANTES_DE_REPETIR') from exc
        if self.fault == 'after':
            raise TimeoutError('FALHA_SINTETICA_APOS_COMMIT_LOCAL')
        return snapshot

    def capture(self, draft: Draft, operation_id: str, expected_revision: int):
        """Persistência C0 local, sem criar HumanReview ou aceite de produto."""
        validate_draft(draft)
        require(isinstance(operation_id, str) and re.fullmatch(r'FUND-OP-\d{4}', operation_id),
                'OPERACAO_INVALIDA')
        require(type(expected_revision) is int and expected_revision >= 0 and
                draft.revision == expected_revision+1, 'SUCESSAO_INVALIDA')
        data = json_bytes(asdict(draft))
        request_digest = digest(json_bytes({'draft': asdict(draft), 'expected_revision': expected_revision}))
        with self._connect() as db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT request_digest,receipt FROM draft_operations WHERE id=?',
                             (operation_id,)).fetchone()
            if old:
                require(old[0] == request_digest, 'OPERACAO_REUSADA_COM_OUTRO_PAYLOAD')
                return json.loads(old[1])
            current = db.execute('SELECT MAX(revision) FROM drafts WHERE id=?', (draft.record_id,)).fetchone()[0] or 0
            if current != expected_revision:
                raise Conflict('REVISAO_C0_ANTIGA')
            receipt = {'schema_version': 'fundacao-local-1', 'operation_id': operation_id,
                       'record_id': draft.record_id, 'revision': draft.revision,
                       'sha256': digest(data), 'request_digest': request_digest,
                       'publication': 'LOCAL_SINTETICA', 'normative_effect': 'AUSENTE',
                       'content_acceptance': 'NAO_SOLICITADO_C0', 'source_trust': 'UNTRUSTED_DATA'}
            db.execute('INSERT INTO drafts VALUES (?,?,?)', (draft.record_id, draft.revision, data))
            db.execute('INSERT INTO draft_operations VALUES (?,?,?)', (operation_id, request_digest, json_bytes(receipt)))
        # Confirma a escrita por nova conexão, após commit da transação.
        require(self.recover_draft(draft.record_id, draft.revision)['sha256'] == receipt['sha256'],
                'RELEITURA_C0_DIVERGENTE')
        return receipt

    def recover_draft(self, record_id: str, revision: int | None = None):
        require(isinstance(record_id, str) and re.fullmatch(r'FUND-(?:IDEA|HYP|PEND|DEC)-\d{4}', record_id),
                'ID_INVALIDO')
        require(revision is None or type(revision) is int and revision >= 1, 'REVISAO_INVALIDA')
        with self._connect() as db:
            if revision is None:
                row = db.execute('SELECT data FROM drafts WHERE id=? ORDER BY revision DESC LIMIT 1', (record_id,)).fetchone()
            else:
                row = db.execute('SELECT data FROM drafts WHERE id=? AND revision=?', (record_id, revision)).fetchone()
        if row is None:
            raise FileNotFoundError('REGISTRO_C0_AUSENTE')
        value = Draft(**json.loads(row[0]))
        validate_draft(value)
        with self._connect() as db:
            receipts = [json.loads(r[0]) for r in db.execute('SELECT receipt FROM draft_operations')]
        matching = [r for r in receipts if r['record_id'] == value.record_id and
                    r['revision'] == value.revision]
        require(len(matching) == 1 and matching[0]['sha256'] == digest(row[0]),
                'RECIBO_C0_AUSENTE_OU_DIVERGENTE')
        return {'record': asdict(value), 'sha256': digest(row[0]), 'normative_effect': 'AUSENTE',
                'publication': 'LOCAL_SINTETICA', 'source_trust': 'UNTRUSTED_DATA'}


def main():
    parser = argparse.ArgumentParser(description='Fixture LOCAL sintética C0/C1; não publica no GitHub.')
    parser.add_argument('--database', required=True)
    subs = parser.add_subparsers(dest='command', required=True)
    p = subs.add_parser('capturar-c0'); p.add_argument('--entrada', required=True)
    p.add_argument('--operacao', required=True); p.add_argument('--revisao-esperada', type=int, required=True)
    p = subs.add_parser('retomar-c0'); p.add_argument('--id', required=True)
    p = subs.add_parser('preparar-c1'); p.add_argument('--registro', required=True)
    p.add_argument('--operacao', required=True); p.add_argument('--saida', required=True)
    args = parser.parse_args()
    gateway = SQLiteGateway(args.database)
    if args.command == 'capturar-c0':
        result = gateway.capture(Draft(**json.loads(Path(args.entrada).read_bytes())),
                                 args.operacao, args.revisao_esperada)
    elif args.command == 'retomar-c0':
        result = gateway.recover_draft(args.id)
    else:
        packet = prepare(Record(**json.loads(Path(args.registro).read_bytes())), gateway.context(), args.operacao)
        with Path(args.saida).open('xb') as stream:
            stream.write(json_bytes(packet))
        result = {'state': 'PREPARADO_NAO_ACEITO', 'destination': 'FIXTURE_LOCAL_SINTETICA',
                  'request_digest': packet['request_digest']}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
