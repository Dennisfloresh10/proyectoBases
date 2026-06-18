````markdown
# Sistema de Casilleros  - Proyecto Académico

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión de casilleros internacionales inspirado en el funcionamiento de empresas como GBOX Honduras.

El objetivo principal es administrar el proceso completo de recepción, consolidación, transporte y entrega de paquetes, permitiendo controlar la información de clientes, casilleros, envíos, aduanas, facturación y entregas desde una plataforma centralizada.

El proyecto está siendo desarrollado como parte de la asignatura de Bases de Datos, aplicando conceptos de modelado de datos, normalización, integridad referencial, transacciones y desarrollo de aplicaciones web.

---

## Tecnologías Utilizadas

### Backend
- FastAPI
- Python

### Base de Datos
- PostgreSQL

### Frontend
- HTML
- Bootstrap
- JavaScript

### Control de Versiones
- Git
- GitHub

---

## Arquitectura General

El sistema sigue una arquitectura de tres capas:

```text
Frontend (HTML + Bootstrap)

↓

Backend (FastAPI)

↓

Base de Datos (PostgreSQL)
````

FastAPI se encarga de la lógica de negocio y PostgreSQL de la persistencia e integridad de los datos.

---

## Estructura del Proyecto

```text
project/
│
├── app/
├── database/
├── frontend/
├── docs/
├── requirements.txt
├── .env
└── README.md
```

### app/

Contiene la lógica principal del backend desarrollada con FastAPI.

### database/

Contiene scripts SQL, diagramas y documentación relacionada con PostgreSQL.

### frontend/

Contiene las páginas y recursos visuales del sistema.

### docs/

Contiene la documentación técnica y funcional del proyecto.

HACK TRICK DE MESSI
---

