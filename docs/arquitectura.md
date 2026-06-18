````markdown
# Arquitectura del Sistema

## Introducción

El sistema de casilleros fue diseñado utilizando una arquitectura de tres capas. Esta separación permite mantener una organización clara entre la interfaz de usuario, la lógica de negocio y el almacenamiento de datos.

La arquitectura seleccionada busca ser sencilla de implementar, fácil de mantener y adecuada para los objetivos académicos del proyecto.

---

## Arquitectura General

```text
Frontend (HTML + Bootstrap)
            │
            ▼
      FastAPI (Backend)
            │
            ▼
    PostgreSQL (Base de Datos)
````

---

## Frontend

El frontend es la capa encargada de interactuar con los usuarios del sistema.

Tecnologías utilizadas:

* HTML
* Bootstrap
* JavaScript

Responsabilidades:

* Mostrar información al usuario.
* Capturar datos mediante formularios.
* Consumir los servicios proporcionados por FastAPI.
* Presentar resultados de consultas, registros y operaciones del sistema.

El frontend no contiene lógica de negocio ni acceso directo a la base de datos.

---

## Backend

El backend será desarrollado utilizando FastAPI.

Responsabilidades:

* Procesar solicitudes del frontend.
* Aplicar reglas de negocio.
* Validar información recibida.
* Gestionar autenticación y autorización.
* Comunicarse con PostgreSQL.
* Generar respuestas para el frontend.

La lógica principal del sistema se concentra en esta capa.

---

## Base de Datos

La base de datos será implementada utilizando PostgreSQL.

Responsabilidades:

* Almacenar información de forma permanente.
* Garantizar integridad referencial.
* Mantener consistencia de los datos.
* Gestionar transacciones.
* Implementar restricciones, vistas, índices y demás elementos requeridos por el proyecto.

---

## Estructura del Proyecto

```text
project/
│
├── app/
│   ├── core/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── utils/
│   └── dependencies.py
│
├── database/
│
├── frontend/
│
├── docs/
│
├── requirements.txt
├── .env
└── README.md
```

---

## Descripción de Carpetas

### app/

Contiene todo el código relacionado con FastAPI.

### app/core/

Configuraciones generales del sistema, conexión a base de datos y variables de entorno.

### app/routes/

Define los endpoints o rutas de la API.

### app/services/

Implementa la lógica de negocio del sistema.

### app/schemas/

Modelos utilizados para validación y transferencia de datos.

### app/utils/

Funciones auxiliares reutilizables.

### database/

Contiene scripts SQL, diagramas y documentación relacionada con PostgreSQL.

### frontend/

Contiene la interfaz gráfica del sistema.

### docs/

Contiene la documentación técnica y funcional del proyecto.

---

## Justificación de la Arquitectura

Se eligió esta arquitectura porque permite separar responsabilidades y mantener una organización clara durante el desarrollo.

Además, facilita el trabajo colaborativo del equipo, ya que cada integrante puede trabajar sobre módulos específicos sin afectar directamente otras áreas del sistema.

Esta estructura también es adecuada para demostrar los conceptos de bases de datos y desarrollo web requeridos por la asignatura.

```
```
