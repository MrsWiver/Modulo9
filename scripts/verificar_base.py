"""Comprueba integridad y procedencia sin leer claves ni invocar IA."""
import hashlib
import json
from src.app import crear_app
from src.db import ROOT, conectar


def verificar():
    app = crear_app()
    with conectar(app.config['DB_PATH']) as db:
        assert db.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
        assert not db.execute('PRAGMA foreign_key_check').fetchall()
        conteos = {t: db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0]
                   for t in ('productos','proveedores','inventario','ventas')}
    manifest = json.loads((ROOT/'soportes/manifest.json').read_text())
    assert len(manifest) == 12
    for item in manifest:
        assert hashlib.sha256((ROOT/'soportes'/item['archivo']).read_bytes()).hexdigest() == item['sha256']
    with app.test_client() as cliente:
        for ruta in ('/','/mesa','/construccion','/api/productos','/api/modulo-9/estado'):
            assert cliente.get(ruta).status_code == 200, ruta
        assert cliente.get('/api/cliente/historial').status_code == 501
    print('Módulo 9: integridad correcta, datos conservados y rutas disponibles.')
    print(json.dumps(conteos, ensure_ascii=False))
    print('Doce soportes autorizados verificados. Sin llamadas a IA.')
    print('Cuentas, chat del cliente y procesos nuevos: por construir.')


if __name__ == '__main__':
    verificar()
