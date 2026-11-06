"""Checks de la base. No acreditan las funciones pendientes del taller."""
import hashlib
import json
import re
import sqlite3
import zipfile
import pytest
from src.app import crear_app
from src.db import ROOT, conectar
from src.modulo9 import RUTAS_PENDIENTES


@pytest.fixture
def app(tmp_path):
    app=crear_app(tmp_path/'practica')
    app.config['TESTING']=True
    return app


def test_portada_mesa_materiales_y_estado_sin_ia(app, monkeypatch):
    monkeypatch.setattr('src.ia.respuesta_api', lambda *a,**k: pytest.fail('No debe invocar IA'))
    c=app.test_client()
    for ruta in ('/','/mesa','/construccion'):
        assert c.get(ruta).status_code==200
    assert 'Módulo 9' in c.get('/').text
    assert c.get('/api/modulo-9/estado').json['autenticacion_clientes'] is False
    assert c.get('/api/modulo-9/estado').json['chat_cliente_con_vault'] is False
    assert c.get('/api/productos?q=FER-0001').json['resultados'][0]['precio_venta']==121300
    for nombre in ('taller','politicas','casos'):
        r=c.get('/materiales/'+nombre)
        assert r.status_code==200 and 'attachment' in r.headers['Content-Disposition']
    assert c.get('/materiales/secreto').status_code==404
    assert c.get('/backend/.env').status_code==404


def test_stubs_rechazan_sin_efectos_y_sin_api(app, monkeypatch):
    monkeypatch.setattr('src.ia.respuesta_api', lambda *a,**k: pytest.fail('Un stub no invoca IA'))
    c=app.test_client()
    token=re.search(r'name="practica-token" content="([^"]+)"',c.get('/').text)[1]
    with conectar(app.config['DB_PATH']) as db:
        inicial={t:db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0]
                 for t in ('ventas','mensajes_chat','archivos_ingresados','propuestas','operaciones')}
    for ruta,metodo,etapa,capacidad in RUTAS_PENDIENTES:
        ruta=ruta.replace('<codigo>','FER-0001').replace('<ident>','DEMO')
        r=c.open(ruta,method=metodo,json={} if metodo=='POST' else None,
                 headers={'X-Practica-Token':token})
        assert r.status_code==501
        assert r.json['etapa']==etapa and r.json['implementado'] is False
    with conectar(app.config['DB_PATH']) as db:
        assert inicial=={t:db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in inicial}


def test_vault_y_prompt_original_conservados():
    vault=ROOT/'conocimiento/la-esquina'
    manifest=json.loads((vault/'manifest.json').read_text())
    assert manifest['productos']==1250 and manifest['notas']==len(list(vault.rglob('*.md')))
    assert len(list((vault/'Catalogo/Productos').glob('*.md')))==1250
    for nota in vault.glob('*.md'):
        if nota.name!='Inicio.md':
            assert 'origen: escenario_ficticio' in nota.read_text()
            assert 'version: "1.0"' in nota.read_text()
    assert hashlib.sha256((ROOT/'prompts/extractor-v1.txt').read_bytes()).hexdigest()==(
        '9559d1c8ff92a5f293a0e0dea5509db4165a1b40fb638e7aca9cd16dcab2e170')


def test_zip_es_independiente_y_trae_vault_y_materiales(tmp_path):
    from scripts.empaquetar import empaquetar
    result=empaquetar(tmp_path/'modulo9.zip')
    with zipfile.ZipFile(result) as z:
        assert z.testzip() is None
        names=z.namelist()
        assert all(n.startswith('modulo-9/') for n in names)
        manifest=json.loads(z.read('modulo-9/conocimiento/la-esquina/manifest.json'))
        assert len([n for n in names if '/conocimiento/' in n and n.endswith('.md')])==manifest['notas']
        assert 'modulo-9/docs/modulo-9/modulo-9-taller.md' in names
        assert 'modulo-9/fixtures/clientes-de-ejemplo.json' in names
        assert 'modulo-9/BASE.json' in names
        assert not any(n.endswith('/.env') or '/.git/' in n or '/.venv/' in n for n in names)
        z.extractall(tmp_path/'extraido')
    extracted=tmp_path/'extraido/modulo-9'
    with sqlite3.connect(extracted/'datos/practica/negocio.sqlite3') as db:
        assert db.execute('SELECT COUNT(*) FROM ventas').fetchone()[0]==8
        assert db.execute('SELECT COUNT(*) FROM mensajes_chat').fetchone()[0]==0
    import subprocess, sys
    r=subprocess.run([sys.executable,'-c',
        "from src.app import crear_app; a=crear_app(); c=a.test_client(); "
        "assert c.get('/').status_code==200; "
        "assert c.get('/api/productos').json['total']==1250; "
        "assert c.get('/construccion').status_code==200"],
        cwd=extracted,capture_output=True,text=True,timeout=30)
    assert r.returncode==0,r.stderr
