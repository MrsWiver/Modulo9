# Validación de la base del módulo 9

Preparación: 6 de noviembre de 2026. Origen: commit publicado 096d8fe37259a4c5d363c6eb666dc2976e6d0bc9 de la clase 8. Se creó una copia independiente sin incorporar los cambios de trabajo de otras ramas ni modificar la app anterior.

## Pruebas ejecutadas

macOS, Python 3.14.7 y uv. Instalación con uv sync --locked. scripts.iniciar_datos y scripts.verificar_base ejecutados correctamente. Pytest: 62 pruebas aprobadas, incluidas las 58 regresiones de la base y cuatro pruebas de infraestructura del módulo 9.

Los controles nuevos verifican portada y mesa; descarga de materiales desde lista fija; ausencia de claves expuestas; estado explícito de capacidades pendientes; stubs 501 sin llamadas a IA ni escrituras comerciales; ocho políticas versionadas y prompt original; paquete independiente con vault, fixtures y materiales; extracción y arranque del ZIP en un proceso separado, sin acceder a la clase 8.

Integridad SQLite y claves foráneas correctas. Semilla: 1.250 productos, 75 proveedores sin contactos, 827 filas de inventario y ocho ventas. Hashes de los doce soportes autorizados conservados. Prompt original SHA-256 9559d1c8ff92a5f293a0e0dea5509db4165a1b40fb638e7aca9cd16dcab2e170.

## Alcance de IA

No se configuró ni copió una clave, ni se hicieron llamadas pagadas durante esta preparación. Las regresiones de IA usan mocks identificados y bases temporales. Los informes históricos de OCR y agente del módulo 8 no acreditan el chat de cliente, que todavía no existe. Se conservan aparte en docs/heredado-modulo-8/.

## Pendientes del taller

Autenticación y aislamiento por cliente, chat con recuperación del vault, disponibilidad, cotizaciones, pedidos, seguimiento, historial, recompra, posventa, bandeja humana y trazas integrales siguen pendientes. La operación administrativa heredada sigue local para un operador sin permisos multiusuario. No se ofrece verificación bancaria, reserva de stock ni transferencias de reembolso.

Windows no se ejecutó en esta preparación. La app usa rutas relativas y comandos de Python/uv, pero no se declara una prueba realizada en ese sistema.

## Revisión de interfaz

Portada, búsqueda FER-0001 y precio 121300, navegación a mesa y ruta de construcción observadas en navegador. Sin clave ni invocación real de modelos. Vista móvil de 390 × 844 sin desbordamiento horizontal de página. JavaScript nuevo y heredado comprobado con node --check. No se hizo auditoría completa con lector de pantalla ni prueba física en teléfono.

## Ampliación del vault comercial

El 6 de noviembre se amplió el vault a 2.191 notas: 1.250 productos, cinco categorías, ocho políticas existentes, guías, 32 preguntas frecuentes, 75 proveedores y 827 referencias de inventario internas. Se conservaron las políticas manuales y la semilla. Inicio.md previo se respaldó fuera del vault, bajo datos/respaldos/, excluido de entregas.

Pytest: 65 pruebas aprobadas tras la ampliación. Se comprueban precios y nombres contra cada producto de la semilla; cobertura de proveedores e inventario; integridad de hashes; IDs y enlaces internos válidos; notas públicas sin enlaces a material interno; regeneración que conserva ediciones humanas; y ZIP independiente con todos los documentos. La regeneración se repitió sin cambios correctamente.

Las notas documentan precios de referencia y existencias históricas, sin declarar disponibilidad actual. Se conservaron estados y fechas originales, incluidas alertas de vencimiento. La conexión al bot sigue pendiente; los metadatos no son por sí mismos un control de acceso. No se exportaron compradores, ventas de trabajo, conversaciones, claves o contraseñas. No hubo llamadas a modelos ni escrituras en la base de trabajo.
