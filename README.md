# Módulo 9

Base inicial de Comercial La Esquina para construir integración multisistema y operación confiable. Trae portada con catálogo real, mesa de comprobantes de la clase 8, vault comercial y puntos de extensión. El canal de clientes se construye durante el taller.

## Disponible en esta base

- Catálogo con búsqueda y paginación: 1.250 productos, precios en COP.
- Mesa operativa heredada con ocho ventas ficticias, doce soportes autorizados, carga, revisión, propuestas, aprobación por versión y ejecución comercial.
- OCR y agente administrativo opcionales al configurar una clave propia. No se invocan al abrir la portada ni al instalar.
- Referencias de inventario en lectura: 827 filas y 75 proveedores sin contactos.
- Vault completo con 2.191 notas: 1.250 fichas de producto, cinco índices de categoría, ocho políticas, guías, 32 preguntas frecuentes y referencias internas de 75 proveedores y 827 registros de inventario.
- Ruta de construcción, taller completo, contratos, fixtures de diseño y matriz de casos.
- Pruebas y empaquetador que entrega una práctica limpia e independiente.

## Por construir

Registro, acceso y cierre de sesión; chat del cliente con fuentes; disponibilidad; cotización versionada; pedido y vínculo con soporte; seguimiento; historial y recompra; reclamaciones y devoluciones; reembolso administrativo; escalamiento humano; trazas, métricas y recuperación.

Las nuevas rutas devuelven 501 capacidad_pendiente. No generan datos, cuentas o respuestas falsas. La mesa y las API heredadas siguen siendo para un operador local, sin autenticación multiusuario. Una ruta separada no es una frontera de permisos. La etapa 1 debe protegerlas antes de habilitar historial privado. No desplegar ni usar datos personales.

## Obtener el proyecto

```bash
git clone https://github.com/MrsWiver/Modulo9.git
cd Modulo9
```

El repositorio contiene la app, el vault y los materiales. En materiales/ puedes abrir modulo-9-clase.html o modulo-9-presentacion.html y consultar el guion del docente en PDF o Word. Las páginas son archivos locales; crear el repositorio no despliega un sitio.

## Preparar e iniciar

Requiere Python 3.11+ y uv. Abre esta carpeta con el asistente de programación y pide que ejecute los comandos. Son iguales en Windows y macOS:

```bash
uv sync --locked
uv run python -m scripts.iniciar_datos
uv run python -m scripts.verificar_base
uv run python -m src.app
```

Abre http://127.0.0.1:8009. Detén con Ctrl+C. El inicio conserva la práctica existente y aplica las migraciones; no sustituye datos.

- /: portada y catálogo.
- /mesa: interfaz operativa heredada.
- /construccion: etapas y materiales descargables.
- /api/modulo-9/estado: capacidades explícitas y procedencia.

Si el puerto está ocupado:

```bash
uv run flask --app src.app:crear_app run --host 127.0.0.1 --port 8010
```

## IA heredada

Sin clave puedes explorar catálogo, ventas y soportes y ejecutar pruebas. Para usar OCR o agente de la mesa, copia backend/.env.example a backend/.env con tu editor o explorador y configura allí:

```dotenv
OPENAI_API_KEY=valor_privado_en_backend
OPENAI_OCR_MODEL=gpt-5.6-luna
OPENAI_CHAT_MODEL=gpt-5.6-luna
```

La app lee backend/.env, no el .env de raíz. No pegues secretos en el chat ni exijas listar modelos para probar acceso. La cuenta del asistente de programación no configura la app. Esta base no incluye credencial ni saldo. La configuración del modelo se conserva por decisión del curso, sin fallback automático.

El agente de la mesa es administrativo y usa el historial global heredado. No lo conectes directamente con clientes. La primera etapa separa sesiones, historial, permisos y herramientas antes del nuevo chat.

## Vault de Obsidian

Abre conocimiento/la-esquina/ como bóveda. Empieza por Inicio.md. Catalogo/ contiene fichas públicas de productos e índices; las políticas de raíz definen las reglas ficticias; Atencion/ y Guias/ ayudan a responder; Interno/ contiene costos, proveedores, inventario y procedimientos exclusivos del operador. El manifiesto registra audiencias, corte y hashes.

Los precios del vault son referencias de la semilla y las existencias son históricas, con registros antiguos y vencidos. No se presentan como disponibilidad actual. Cotizaciones y estados comerciales consultan SQLite con permisos. No se exportan ventas, compradores, conversaciones ni claves al vault.

El bot todavía no recupera estas notas. La etapa 2 implementa lectura acotada y filtrado por audiencia en cada fragmento y enlace. No basta con permitir toda la carpeta: las notas internas y esta portada no deben llegar al cliente. El bot no publica sus propias políticas.

scripts.generar_vault permite reproducir el catálogo documental sin cambiar la semilla. Conserva las políticas manuales y se detiene antes de reemplazar una nota generada que tenga cambios. No hay sincronización automática con la base de trabajo.

## Construcción

Lee AGENTS.md y docs/TALLER.md. Los tres materiales completos están en docs/modulo-9/. Si recibiste esta carpeta o ZIP, úsala como punto de partida: no clones encima la clase 8. La etapa 0 verifica esta base y BASE.json. Construye una etapa, comprueba y continúa. fixtures/ describe clientes ficticios, pero no importa cuentas ni contraseñas. No asignes ventas a cuentas nuevas por coincidencia de nombre o correo.

## Pruebas y distribución

```bash
uv run pytest -q
uv run python -m scripts.empaquetar
```

El paquete modulo-9-inicial.zip aparece junto a esta carpeta y contiene raíz modulo-9/. Incluye vault, materiales, fixtures, una SQLite nueva migrada y los doce soportes autorizados. No incluye claves, historial personal, respaldos, entornos ni cachés. Las pruebas nuevas validan la base y su paquete, no las capacidades pendientes.

## Respaldo y recuperación

Con el servidor detenido, copia completa datos/practica/ a una ubicación privada. Restaura esa carpeta completa para recuperar, incluidas imágenes. No uses scripts.reiniciar para diagnosticar: ese comando pide REINICIAR y crea respaldo antes de reiniciar. Tras una respuesta incierta consulta la propuesta por ID antes de repetir escritura.

## Procedencia

Base publicada de la clase 8, commit 096d8fe37259a4c5d363c6eb666dc2976e6d0bc9. No incorpora cambios sin commit de otras carpetas. BASE.json registra la referencia. docs/VALIDACION.md documenta esta preparación; docs/heredado-modulo-8/ conserva antecedentes históricos sin acreditar las nuevas funciones.

No hay banco, transportadora, factura fiscal, reserva de inventario ni movimiento de reembolsos en esta base. Las operaciones permanecen sin verificación bancaria.
