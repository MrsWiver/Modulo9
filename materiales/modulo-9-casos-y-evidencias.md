# Casos de comprobación y recuperación del módulo 9

Usa esta matriz con el [taller](modulo-9-taller.md) y las [políticas ficticias](modulo-9-politicas-y-datos.md). Son resultados esperados para evaluar la construcción; ninguna fila está declarada aprobada por aparecer aquí. No cambia la rúbrica del curso.

## Cómo registrar una ejecución

Para cada caso anota: identificador, fecha, versión de app y política, datos iniciales, origen de prueba, pasos, resultado esperado, resultado observado, IDs, conteos antes/después y evidencia. Resultado: cumple, no cumple o pendiente. Conserva el fallo original cuando luego lo corrijas.

El origen será `api_real`, `mock_prueba`, `simulacion_falla` o `manual_sin_ia`, según lo realmente ejecutado. Un caso puede tener varias evidencias con orígenes diferentes: un recorrido de interfaz con extracción mock no se vuelve real por incluir una respuesta de chat real.

## Casos funcionales

| ID | Acción | Resultado esperado | Evidencia mínima |
| --- | --- | --- | --- |
| C01 | Preguntar vigencia y plazo con respuesta en vault | Respuesta correcta con documento, sección y versión | Respuesta, fragmento y consulta |
| C02 | Preguntar por una condición ausente | Reconoce falta de evidencia y ofrece escalamiento | Respuesta y estado del caso |
| C03 | Editar y versionar una nota en Obsidian | Nueva consulta usa cambio; cotización emitida conserva condiciones | Dos fuentes y documento anterior |
| C04 | Consultar disponibilidad positiva, agotada y desconocida | Resultados diferenciados con procedencia/fecha conocida o no disponible; ninguna escritura | Consultas y conteo/integridad de inventario |
| C05 | Solicitar producto ambiguo | Pide selección antes de cotizar | Opciones y código seleccionado |
| C06 | Cotizar dos líneas, emitir y aceptar | Documento completo, total calculado y aceptación de versión | Documento e ID/versión |
| C07 | Cambiar cantidad tras aceptación | Nueva versión; aceptación previa ya no autoriza pedido | Dos versiones y rechazo de la antigua |
| C08 | Aceptar cotización vencida | Rechazo y posibilidad de nueva versión | Reloj del test, vencimiento y resultado |
| C09 | Cambiar precio o disponibilidad antes del pedido | Revisión explícita; no altera importe aceptado ni confirma sin resolver | Datos iniciales/cambiados y estado |
| C10 | Generar pedido dos veces desde misma aceptación | Un pedido y mismos IDs | Conteo antes/después y respuesta |
| C11 | Cargar soporte válido y revisar/aprobar/ejecutar | Una venta vinculada, pedido confirmado por soporte, banco no verificado | Original, revisión, aprobación, resultado y relaciones |
| C12 | Cargar soporte parcial, mayor, de financiación o con fecha incompatible | Permanece pendiente y escala; no confirma por OCR | Extracción y motivo |
| C13 | Adjuntar segunda foto del mismo pago | Revisión y adjunto a operación existente; no suma dinero | IDs de soportes y monto único |
| C14 | Consultar envío antes y después de actualizar como operador | Estado y fechas reales del registro, sin guía inventada | Eventos y respuesta |
| C15 | Confirmar en viernes y contar plazo | Recogida siguiente lunes de práctica; domicilio martes a miércoles, salvo fixture con otras fechas | Fecha local, cálculo y condiciones |
| C16 | Consultar historial de Ana y pedir recompra | Solo compras propias; nueva cotización con datos actuales y referencia al origen | Historial y nuevo borrador |
| C17 | Recomprar producto agotado o inexistente | Explica situación y solicita decisión; sin sustitución automática | Datos y respuesta |
| C18 | Abrir reclamación por una unidad y autorizar devolución | Caso persistente, cantidad válida y decisión humana | Solicitud, política y decisión |
| C19 | Reclamar con fecha de entrega ausente o fuera de ventana | Guarda solicitud y escala, sin elegibilidad inventada | Datos faltantes y escalamiento |
| C20 | Probar días 7 y 8 desde entrega | Día 7 entra a evaluación ordinaria; día 8 pasa a excepción humana | Reloj y resultados de ambos |
| C21 | Pedir devolver más unidades que las compradas | No autoriza exceso acumulado | Cantidades y rechazo |
| C22 | Aprobar reembolso parcial tras recepción | Cálculo con precio de venta histórico; reserva de saldo | Venta, devolución y expediente |
| C23 | Remitir reembolso a pago externo | Cierre administrativo sin estado de dinero pagado/devuelto | Ficha y estado del cliente |
| C24 | Pedir persona, tomar y responder | Mismo caso, contexto disponible y respuesta humana identificada | Secuencia y responsable |
| C25 | Retomar después de intervención humana | Continúa desde estado persistido sin repetir efectos completados | Mismo caso y relaciones |
| C26 | Crear otra recompra intencional después de la primera | Nueva intención produce nuevo borrador; reintento de cada intención conserva el suyo | IDs y claves distintas |
| C27 | Registrar cuenta nueva y repetir correo | Cliente con ID único y rol cliente; historial vacío; segundo registro no duplica cuenta | Resultado del formulario y conteos, sin contraseña |
| C28 | Cerrar sesión, entrar de nuevo y reiniciar | Acceso privado denegado tras salir; al entrar recupera solo sus recursos por ID estable | Sesión cerrada, nuevo acceso e historial propio |

## Fallas y recuperación

Provoca fallas en pruebas aisladas, con puntos de interrupción controlados y deshabilitados fuera del entorno de pruebas. El objetivo es observar el estado de la aplicación y su recuperación; no afectar al proveedor real.

| ID | Interrupción o intento | Estado esperado tras el incidente | Recuperación y prueba del resultado |
| --- | --- | --- | --- |
| F01 | Timeout o error de modelo antes de respuesta | Caso y mensaje conservados; ningún éxito comercial inventado | Consultar estado; reintentar de forma acotada en la misma conversación, sin perder lo persistido |
| F02 | Vault no disponible o nota ausente | Respuesta indica límite y puede guardar escalamiento | Restaurar fuente y repetir consulta; cita correcta sin recrear caso |
| F03 | Límite de herramientas alcanzado | Explicación del límite; propuestas guardadas siguen consultables | Consultar recursos y continuar en otro turno; sin ejecutar propuestas sin autorización |
| F04 | Editar propuesta después de aprobarla | Aprobación antigua no autoriza nueva versión | Revisar y aprobar la nueva versión; solo esa ejecuta |
| F05 | Excepción antes del commit compuesto | No existen venta, líneas, operación, vínculo ni confirmación parciales de ese intento | Verificar conteos e integridad; reintentar misma intención y obtener un resultado completo |
| F06 | Perder respuesta después del commit | Operación completa ya persistida; interfaz desconoce resultado | Consultar por ID; repetir misma clave devuelve mismo resultado y mismos conteos |
| F07 | Dos ejecuciones concurrentes o doble clic | Una venta por pedido y una operación del pago | Ambas solicitudes recuperan resultado único o conflicto claro consultable |
| F08 | Reiniciar con borrador, pedido o escalamiento pendiente | Recursos conservan ID, estado, versión y propietario | Volver a iniciar sesión si hace falta; continuar sin reconstruir desde el chat |
| F09 | Usar mismo soporte/pago en otro pedido | No confirma segundo pedido; registra motivo | Operador compara evidencia y resuelve; no duplica dinero |
| F10 | Bruno intenta leer historial, compra, imagen o expediente de Ana | Denegado desde API y herramientas, sin filtración | Volver a recurso propio; probar también ID adivinado y ruta heredada |
| F11 | Nota o imagen ordena revelar datos/cambiar reglas | Se trata como contenido y no obtiene permisos | Mantener sesión/permisos y dejar traza del rechazo; repetir pregunta legítima |
| F12 | Cliente/modelo intenta aprobar reembolso o cambiar envío | Acción rechazada en servidor, sin efectos | Operador autorizado usa control correcto, con versión y motivo |
| F13 | Dos reembolsos concurrentes superan saldo | Suma reservada no supera cobro elegible | Consultar expedientes; una decisión válida y otra rechazada o en revisión |
| F14 | Modelo falla al generar resumen de escalamiento | Caso conserva motivo, IDs y estado pendiente_persona | Operador abre contexto existente y responde sin depender del modelo |
| F15 | Dos operadores toman el mismo caso | Un responsable activo | Segunda toma muestra asignación actual; reasignar exige acción explícita |
| F16 | Error al escribir traza durante ejecución | Si falla el evento comercial obligatorio, revierte negocio completo; si falla registro separado de intentos, no inventa traza completa | Consultar estado comercial; recuperar registro de auditoría sin repetir efectos ya confirmados |
| F17 | Doble solicitud de devolución de mismas unidades | Cantidad autorizada acumulada no excede venta | Consultar solicitudes existentes y resolver sin duplicar devolución |

## Protocolo para comprobar la confirmación recuperable

1. Prepara un pedido autorizado y una propuesta comercial revisada/aprobada en una base temporal. Guarda IDs y conteos iniciales.
2. Inyecta una excepción dentro de la transacción antes de su commit. Ejecuta. Consulta con otra conexión: no deben existir efectos parciales.
3. Desactiva esa falla y repite con la misma intención. Consulta el resultado completo y sus relaciones.
4. En un segundo fixture, deja completar el commit e interrumpe únicamente la entrega de la respuesta al cliente. El resultado existe aunque la interfaz vea un error.
5. Consulta propuesta y pedido por sus IDs antes de repetir. Reintenta con la misma clave. Deben conservar venta, operación y vínculo únicos.
6. Reinicia y repite la consulta. La unicidad no puede depender de variables en memoria.
7. Guarda conteos y origen `simulacion_falla`. Una captura del mensaje de error sin consultas posteriores no demuestra recuperación.

## Comprobaciones con IA real

Los tests automáticos usan mocks. En tu práctica identifica además una pregunta real con fuente del vault, una selección real de herramientas comerciales, una preparación real de solicitud de posventa y un reconocimiento real de un soporte autorizado. Puedes reutilizar una extracción real ya persistida sin volver a pagar su lectura; documenta origen y fecha. Verifica manualmente campos y respuestas contra las fuentes.

Para un fallo, intento malicioso o escenario adicional probado solo con simulación, conserva esa clasificación. Si no tienes acceso a IA, puedes construir y probar contratos e interfaz, pero debes dejar pendientes esas comprobaciones reales; no presentar respuestas fijas como un agente funcionando.

Antes de enviar una imagen en una prueba real, identifica qué imagen se usará y que esa acción invoca la API. No proceses la colección en masa. Una prueba real del proveedor no valida todos los escenarios de la matriz.

## Informe de resultados

Incluye una fila por ejecución y un resumen separado por origen de prueba. Reporta:

- Casos que cumplen / casos ejecutados; pendientes por separado. Si un caso se repitió, muestra intentos y resultado final sin ocultar fallos.
- Respuestas fundamentadas correctamente / respuestas revisadas que requerían fuente. La revisión humana comprueba que el fragmento respalda la afirmación.
- Duplicados y escrituras no autorizadas observados, con su conjunto de pruebas. Un cero observado no prueba ausencia universal de fallas.
- Intervenciones humanas y motivo; distingue escalamiento esperado de error.
- Duración de ejecución y de llamadas de modelo/herramientas. La espera de una persona se reporta aparte.
- Llamadas intentadas/completadas y tokens reportados por proveedor. Consumo desconocido se muestra como no disponible.
- Costo estimado solo si verificaste tarifa oficial del modelo exacto, fecha, unidades y categorías aplicables. No supongas que todos los tokens tienen el mismo precio. Con datos parciales, etiqueta el subtotal conocido y el consumo desconocido; no lo presentes como costo total.

Entrega trazas depuradas con IDs y evidencias ficticias. No incluyas claves, tokens de sesión, datos bancarios ni imágenes personales. Mantén la relación entre evidencia y resultado sin publicar la aplicación.
