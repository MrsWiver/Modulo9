"""Punto de entrada del módulo 9. Las capacidades nuevas se construyen en el taller.

No conecta automáticamente notas a un modelo ni fabrica datos operacionales.
"""
from flask import Blueprint, abort, jsonify, render_template, send_file
from .db import ROOT

BASE_COMMIT = '096d8fe37259a4c5d363c6eb666dc2976e6d0bc9'
ETAPAS = [
    ('0', 'Comprobar la base', 'Abrir la aplicación, consultar datos y ejecutar las pruebas.', 'disponible'),
    ('1', 'Cuentas e identidad', 'Construir registro, acceso, cierre de sesión y permisos por cliente.', 'pendiente'),
    ('2', 'Conocimiento en Obsidian', 'Recuperar fragmentos del vault y responder con fuentes.', 'pendiente'),
    ('3', 'Disponibilidad', 'Consultar existencias, fechas y datos desconocidos sin reservar.', 'pendiente'),
    ('4', 'Cotizaciones', 'Calcular y emitir un documento completo con aceptación de versión.', 'pendiente'),
    ('5', 'Pedidos', 'Transformar una aceptación en una orden única y revisable.', 'pendiente'),
    ('6', 'Confirmar por soporte', 'Relacionar el pedido con la revisión y operación heredada.', 'pendiente'),
    ('7', 'Entregas', 'Registrar preparación, despacho, recogida y novedades.', 'pendiente'),
    ('8', 'Historial y recompra', 'Consultar compras propias y preparar una cotización nueva.', 'pendiente'),
    ('9', 'Reclamaciones y devoluciones', 'Guardar evidencias y decisiones sobre cantidades.', 'pendiente'),
    ('10', 'Reembolso administrativo', 'Evaluar el expediente y reservar saldo sin mover dinero.', 'pendiente'),
    ('11', 'Atención humana', 'Asignar y retomar el mismo caso con su contexto.', 'pendiente'),
    ('12', 'Trazas y métricas', 'Reconstruir el recorrido y medir resultados y consumo disponible.', 'pendiente'),
    ('13', 'Recuperación', 'Provocar fallas aisladas y continuar sin efectos duplicados.', 'pendiente'),
    ('14', 'Preparar la entrega', 'Documentar y demostrar recorridos, pruebas y pendientes.', 'pendiente'),
]

# Son puntos de extensión, no contratos implementados ni una API de clientes segura.
RUTAS_PENDIENTES = [
    ('/api/cliente/registro', 'POST', 1, 'registro'),
    ('/api/cliente/sesion', 'POST', 1, 'inicio_sesion'),
    ('/api/cliente/salir', 'POST', 1, 'cierre_sesion'),
    ('/api/cliente/chat', 'POST', 2, 'chat_con_fuentes'),
    ('/api/cliente/disponibilidad/<codigo>', 'GET', 3, 'disponibilidad'),
    ('/api/cliente/cotizaciones', 'POST', 4, 'cotizacion'),
    ('/api/cliente/pedidos', 'POST', 5, 'pedido'),
    ('/api/cliente/pedidos/<ident>/soporte', 'POST', 6, 'soporte_del_pedido'),
    ('/api/cliente/pedidos/<ident>/envio', 'GET', 7, 'seguimiento'),
    ('/api/cliente/historial', 'GET', 8, 'historial_propio'),
    ('/api/cliente/recompras', 'POST', 8, 'recompra'),
    ('/api/cliente/reclamaciones', 'POST', 9, 'reclamacion'),
    ('/api/cliente/devoluciones', 'POST', 9, 'devolucion'),
    ('/api/cliente/reembolsos', 'POST', 10, 'solicitud_reembolso'),
    ('/api/cliente/escalamientos', 'POST', 11, 'atencion_humana'),
    ('/api/operador/casos', 'GET', 11, 'bandeja_humana'),
    ('/api/operador/trazas/<ident>', 'GET', 12, 'trazabilidad'),
]


def registrar_modulo9(app, token):
    bp = Blueprint('modulo9', __name__)

    @bp.get('/construccion')
    def construccion():
        return render_template('construccion.html', etapas=ETAPAS, csrf_token=token)

    @bp.get('/materiales/<nombre>')
    def material(nombre):
        permitidos = {
            'taller': 'modulo-9-taller.md',
            'politicas': 'modulo-9-politicas-y-datos.md',
            'casos': 'modulo-9-casos-y-evidencias.md',
        }
        if nombre not in permitidos:
            abort(404, description='No existe ese material.')
        return send_file(ROOT/'docs/modulo-9'/permitidos[nombre],
                         as_attachment=True, download_name=permitidos[nombre],
                         mimetype='text/markdown; charset=utf-8')

    @bp.get('/api/modulo-9/estado')
    def estado():
        return jsonify(
            nombre='Módulo 9', tipo='base_de_construccion', base_commit=BASE_COMMIT,
            autenticacion_clientes=False, chat_cliente_con_vault=False,
            almacenamiento='SQLite y archivos locales',
            etapas=[dict(numero=n, nombre=t, descripcion=d, estado=e) for n,t,d,e in ETAPAS],
        )

    def pendiente(etapa, capacidad):
        def responder(**_):
            return jsonify(error='Esta capacidad se construye durante el taller.',
                           codigo='capacidad_pendiente', capacidad=capacidad,
                           etapa=etapa, implementado=False), 501
        return responder

    for ruta, metodo, etapa, capacidad in RUTAS_PENDIENTES:
        bp.add_url_rule(ruta, endpoint='pendiente_'+capacidad,
                        view_func=pendiente(etapa, capacidad), methods=[metodo])
    app.register_blueprint(bp)
