````markdown
# Base de Datos

## Introducción

La base de datos constituye el núcleo del sistema de casilleros internacionales.

Su función principal es almacenar y administrar toda la información relacionada con clientes, casilleros, paquetes, envíos, procesos aduaneros, facturación y entregas.

Para este proyecto se utilizará PostgreSQL debido a su estabilidad, soporte para integridad referencial y amplio conjunto de herramientas para la administración de datos.

---

## Objetivos de la Base de Datos

- Garantizar la integridad de la información.
- Evitar redundancia innecesaria de datos.
- Mantener consistencia entre módulos.
- Facilitar consultas y reportes.
- Aplicar conceptos de normalización estudiados en clase.

---

## Modelo General

La base de datos fue diseñada tomando como referencia el flujo operativo de una empresa de casilleros internacionales.

Las entidades principales son:

```text
Usuarios
Clientes
Direcciones
Casilleros
Paquetes
Consolidaciones
Envíos
Aduana
Facturas
Pagos
Entregas
Reclamos
Auditoría
````

Estas entidades estarán relacionadas mediante claves primarias y claves foráneas para garantizar la integridad referencial.

---

## Normalización

Durante el diseño se aplicarán las técnicas de normalización estudiadas en la asignatura.

Objetivos:

* Eliminar redundancia de información.
* Reducir anomalías de inserción.
* Reducir anomalías de actualización.
* Reducir anomalías de eliminación.

El modelo se desarrollará respetando al menos la Tercera Forma Normal (3FN), y cuando sea posible se evaluarán niveles superiores de normalización.

---

## Integridad Referencial

La base de datos implementará restricciones para asegurar la consistencia de los datos.

Ejemplos:

* Un paquete debe pertenecer a un cliente existente.
* Un envío debe estar asociado a una consolidación válida.
* Una factura debe estar asociada a un cliente registrado.
* Un pago debe corresponder a una factura existente.

---

## Índices

Se implementarán índices en columnas utilizadas frecuentemente para búsquedas y relaciones.

Objetivos:

* Mejorar el rendimiento de consultas.
* Optimizar búsquedas por identificadores.
* Reducir tiempos de respuesta.

La definición específica de índices se realizará durante la fase de implementación.

---

## Vistas

Se crearán vistas para simplificar consultas frecuentes y apoyar la generación de reportes.

Posibles ejemplos:

* Estado actual de paquetes.
* Historial de envíos por cliente.
* Facturas pendientes de pago.
* Resumen de entregas realizadas.

---

## Transacciones

El sistema utilizará transacciones para garantizar la consistencia de operaciones críticas.

Ejemplos:

* Registro de pagos.
* Generación de facturas.
* Procesos de consolidación.
* Actualización de estados logísticos.

En caso de error, las operaciones podrán revertirse mediante mecanismos de rollback.

---

## Procedimientos y Funciones

PostgreSQL permitirá implementar lógica complementaria directamente en la base de datos.

Posibles aplicaciones:

* Cálculo automático de impuestos.
* Generación de identificadores.
* Validaciones de negocio.
* Automatización de procesos repetitivos.

---


