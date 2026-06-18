````markdown
# Modelo de Negocio del Sistema

## Introducción

El proyecto está inspirado en el funcionamiento de empresas de casilleros internacionales como GBOX Honduras.

Estas empresas permiten que los clientes realicen compras en tiendas internacionales y reciban sus paquetes en Honduras mediante un servicio de intermediación logística.

El sistema busca simular este proceso para administrar clientes, paquetes, envíos, aduanas y entregas.

---

## Funcionamiento General

El proceso inicia cuando un cliente se registra en el sistema y obtiene un casillero internacional.

Posteriormente, el cliente utiliza dicho casillero como dirección de recepción para sus compras en el extranjero.

Los paquetes son recibidos inicialmente en una bodega ubicada en Miami, Estados Unidos, desde donde se preparan para ser enviados a Honduras.

Una vez que los paquetes llegan al país, pasan por procesos aduaneros antes de ser entregados al cliente final.

---

## Flujo General del Negocio

```text
Cliente
   │
   ▼
Registro en el sistema
   │
   ▼
Asignación de casillero
   │
   ▼
Compra en tienda internacional
   │
   ▼
Recepción en bodega de Miami
   │
   ▼
Registro del paquete
   │
   ▼
Consolidación de paquetes (opcional)
   │
   ▼
Envío internacional
   │
   ▼
Proceso aduanero
   │
   ▼
Facturación
   │
   ▼
Entrega al cliente
````

---

## Actores Principales

### Cliente

Persona que utiliza el servicio para recibir paquetes desde el extranjero.

Funciones:

* Registrarse en el sistema.
* Consultar información de sus paquetes.
* Realizar pagos.
* Recibir envíos.

---

### Personal Administrativo

Usuarios encargados de gestionar las operaciones del sistema.

Funciones:

* Registrar paquetes.
* Actualizar estados.
* Gestionar envíos.
* Administrar información de clientes.
* Supervisar procesos de entrega.

---

### Aduana

Representa el proceso de revisión y cálculo de cargos asociados a los envíos internacionales.

Funciones:

* Validar mercancías.
* Calcular impuestos.
* Autorizar liberación de paquetes.

---

## Procesos Principales del Sistema

### Gestión de Clientes

Permite registrar y administrar la información de los clientes.

### Gestión de Casilleros

Asigna una dirección única para identificar los paquetes de cada cliente.

### Gestión de Paquetes

Permite registrar y rastrear paquetes desde su recepción hasta su entrega.

### Consolidación

Permite agrupar varios paquetes en un solo envío cuando sea necesario.

### Envíos Internacionales

Gestiona el transporte de paquetes desde Miami hacia Honduras.

### Aduana

Administra el cálculo de impuestos y cargos asociados al proceso de importación.

### Facturación y Pagos

Genera los cobros correspondientes por los servicios prestados.

### Entregas

Controla la entrega final de los paquetes a los clientes.

---

## Alcance del Proyecto

El sistema se enfocará en simular el proceso operativo de una empresa de casilleros internacionales dentro del contexto académico de la asignatura.

No se pretende replicar todos los procesos reales de una empresa logística, sino implementar las funcionalidades necesarias para demostrar el uso adecuado de bases de datos, reglas de negocio y desarrollo de aplicaciones web.

```
```
