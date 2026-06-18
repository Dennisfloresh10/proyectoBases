````markdown
# Flujo del Sistema

## Introducción

Este documento describe los principales módulos que compondrán el sistema y cómo interactúan entre sí durante el proceso de gestión de casilleros internacionales.

El objetivo es proporcionar una visión general de las funcionalidades que serán implementadas y la relación existente entre los diferentes procesos del negocio.

---

## Vista General

El sistema permitirá administrar el ciclo completo de un paquete desde que un cliente se registra hasta que recibe su envío en Honduras.

```text
Usuarios
   │
   ▼
Clientes
   │
   ▼
Casilleros
   │
   ▼
Paquetes
   │
   ▼
Consolidación
   │
   ▼
Envíos Internacionales
   │
   ▼
Aduana
   │
   ▼
Facturación
   │
   ▼
Pagos
   │
   ▼
Entrega Final
````

---

## Módulo de Usuarios

Permite administrar las cuentas que tendrán acceso al sistema.

Funciones principales:

* Inicio de sesión.
* Gestión de roles.
* Administración de permisos.
* Control de acceso.

---

## Módulo de Clientes

Permite registrar y administrar la información de los clientes.

Funciones principales:

* Registro de clientes.
* Actualización de información personal.
* Consulta de historial de envíos.
* Administración de direcciones.

---

## Módulo de Casilleros

Cada cliente tendrá asignado un casillero único.

Funciones principales:

* Generación de casillero.
* Asociación con cliente.
* Consulta de información del casillero.

---

## Módulo de Paquetes

Gestiona los paquetes recibidos en la bodega de Miami.

Funciones principales:

* Registro de paquetes.
* Actualización de estados.
* Control de peso y dimensiones.
* Asociación con clientes.

---

## Módulo de Consolidación

Permite agrupar varios paquetes en un solo envío.

Funciones principales:

* Agrupar paquetes.
* Calcular peso total.
* Generar consolidaciones.

---

## Módulo de Envíos Internacionales

Administra el transporte de paquetes hacia Honduras.

Funciones principales:

* Registro de envíos.
* Seguimiento del transporte.
* Control de estados logísticos.

---

## Módulo de Aduana

Gestiona el proceso de importación de paquetes.

Funciones principales:

* Registro de liquidaciones.
* Cálculo de impuestos.
* Control de liberación de paquetes.

---

## Módulo de Facturación

Permite generar los cobros asociados a los servicios prestados.

Funciones principales:

* Emisión de facturas.
* Registro de cargos.
* Control de pagos pendientes.

---

## Módulo de Pagos

Administra los pagos realizados por los clientes.

Funciones principales:

* Registro de pagos.
* Confirmación de transacciones.
* Actualización de saldos.

---

## Módulo de Entregas

Gestiona la entrega final de los paquetes.

Funciones principales:

* Asignación de rutas.
* Registro de entregas.
* Confirmación de recepción.

---

## Módulo de Reclamos

Permite registrar incidencias relacionadas con paquetes o entregas.

Funciones principales:

* Creación de reclamos.
* Seguimiento de casos.
* Resolución de incidencias.

---

## Módulo de Auditoría

Registra eventos importantes dentro del sistema.

Funciones principales:

* Registro de cambios.
* Seguimiento de acciones de usuarios.
* Historial de operaciones.

---

## Objetivo del Flujo

La integración de estos módulos permitirá representar de forma ordenada el funcionamiento de una empresa de casilleros internacionales, manteniendo la trazabilidad de cada paquete desde su recepción hasta la entrega final al cliente.

```
```
