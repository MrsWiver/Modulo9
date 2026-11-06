# Contratos de extensión del módulo 9

## Estado inicial

src/modulo9.py registra la ruta de construcción, materiales y estado. Las rutas nuevas son puntos de extensión. Devuelven HTTP 501, codigo=capacidad_pendiente, etapa y capacidad. No escriben cuentas, pedidos ni conversaciones, no recuperan notas ni invocan modelos.

Las escrituras conservan la protección heredada X-Practica-Token. Sin token, un POST devuelve 403 antes del stub. El token local no es una sesión de cliente.

## Disponible

- GET /: portada con catálogo real.
- GET /mesa: interfaz de operador heredada.
- GET /construccion: etapas y materiales.
- GET /api/modulo-9/estado: capacidades y procedencia.
- Los materiales docentes se distribuyen por separado. No existen rutas de descarga /materiales/ en la app pública.

CONTRATOS.md conserva la API de la base. Todavía no tiene aislamiento por cliente. La etapa 1 protege también esas rutas, archivos, listados y herramientas.

## Ampliaciones

Define para cada capacidad propósito, entradas, resultados, errores, estados, permisos e idempotencia antes de sustituir su stub. Las rutas propuestas están en RUTAS_PENDIENTES. No uses una respuesta de éxito si no existe el registro.

El servidor determina identidad y propiedad. El vault aporta políticas; catálogo e inventario datos comerciales; SQLite operaciones. El modelo prepara y recomienda. El operador decide. Conserva revisión, versiones, transacciones e inventario en lectura. El reembolso no mueve dinero y el banco permanece no_verificado.

Las entidades nuevas necesitan IDs, versión, propietario y fechas. Relaciona caso, cotización, pedido, propuesta, venta y posventa. Implementa controles de cantidad, saldo, autorización y reintento antes de habilitar efectos.

## Vault completo y audiencias

conocimiento/la-esquina/ incluye 2.191 notas. Catalogo/ tiene 1.250 productos y cinco índices de categoría. Las políticas manuales de raíz, Atencion/ y Guias/ describen el escenario. Interno/ contiene referencias de proveedores, costos, lotes y ubicaciones; su audiencia es interno. Inicio.md también es interno porque enlaza esos materiales.

El manifiesto identifica ruta, audiencia y hash. Los metadatos sirven para filtrar, pero no sustituyen permisos en servidor. Una búsqueda del cliente no devuelve notas internas ni sigue un enlace sin revalidar audiencia. Los importes y cantidades documentales no sustituyen una consulta operacional vigente. No hay sincronización automática del vault ni exportación de historiales privados.
