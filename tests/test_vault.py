"""Aceptación documental: fuentes correctas, enlaces y audiencias del vault."""
import hashlib
import json
import re
import pytest
from src.db import ROOT
from scripts.generar_vault import generar

VAULT=ROOT/'conocimiento/la-esquina'


def test_fichas_completas_y_sin_costos_en_fuentes_de_cliente():
    semilla=json.loads((ROOT/'datos/semilla/catalogo.json').read_text())
    manifest=json.loads((VAULT/'manifest.json').read_text())
    assert manifest['fuente_catalogo_sha256']==hashlib.sha256((ROOT/'datos/semilla/catalogo.json').read_bytes()).hexdigest()
    assert manifest['sincronizacion_operacional'] is False
    assert len(list((VAULT/'Catalogo/Productos').glob('*.md')))==len(semilla['productos'])==1250
    for p in semilla['productos']:
        text=(VAULT/'Catalogo/Productos'/(p['codigo']+'.md')).read_text()
        assert p['nombre'] in text
        assert f'{p["precio_venta"]:,}'.replace(',','.')+' COP' in text
        assert 'audiencia: "cliente"' in text
        assert 'precio_costo' not in text and 'Costo de referencia' not in text
        assert 'requiere_consulta_operacional: true' in text
    assert len(list((VAULT/'Interno/Proveedores').glob('*.md')))==75
    assert len(list((VAULT/'Interno/Inventario').glob('*.md')))==827


def test_enlaces_integridad_y_separacion_de_audiencia():
    manifest=json.loads((VAULT/'manifest.json').read_text())
    docs={d['ruta']:d for d in manifest['documentos']}
    assert len(docs)==len(list(VAULT.rglob('*.md')))
    ids=set()
    for path,d in docs.items():
        text=(VAULT/path).read_text()
        assert hashlib.sha256((VAULT/path).read_bytes()).hexdigest()==d['sha256']
        ident=re.search(r'^id:\s*(.+)$',text,re.M).group(1)
        assert ident not in ids
        ids.add(ident)
        if path.startswith('Interno/') or path=='Inicio.md':
            assert d['audiencia']=='interno'
        for raw in re.findall(r'\[\[([^\]]+)\]\]',text):
            target=raw.replace('\\|','|').split('|',1)[0].split('#',1)[0]
            if not target:continue
            if not target.endswith('.md'):target+='.md'
            assert target in docs,(path,target)
            if d['audiencia']=='cliente':
                assert docs[target]['audiencia']=='cliente',(path,target)
    # Un estado antiguo VIGENTE no autoriza ofrecer un lote vencido a la fecha de corte.
    inventory=(VAULT/'Catalogo/Disponibilidad y vigencia.md').read_text()
    assert 'No se presentan como disponibilidad comercial actual' in inventory


def test_regeneracion_conserva_edicion_humana_y_no_toca_base(tmp_path):
    for p in VAULT.glob('*.md'):
        if p.name!='Inicio.md':(tmp_path/p.name).write_text(p.read_text())
    target=tmp_path/'Catalogo/Productos/ABA-0001.md'
    target.parent.mkdir(parents=True)
    target.write_text('Nota editada por una persona, conservar.')
    source_hash=hashlib.sha256((ROOT/'datos/semilla/catalogo.json').read_bytes()).hexdigest()
    with pytest.raises(RuntimeError,match='cambió'):
        generar(tmp_path)
    assert target.read_text()=='Nota editada por una persona, conservar.'
    assert len(list(tmp_path.rglob('*.md')))==9
    assert hashlib.sha256((ROOT/'datos/semilla/catalogo.json').read_bytes()).hexdigest()==source_hash
