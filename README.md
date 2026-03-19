# API de Gestión de Encuestas Poblacionales

## Descripción del Proyecto

Esta API REST fue desarrollada con **FastAPI** y tiene como objetivo simular un sistema de recolección, validación y análisis de datos provenientes de encuestas poblacionales.

El sistema actúa como una **"aduana de datos"**, garantizando que solo información válida, consistente y estructuralmente correcta sea almacenada y utilizada para análisis estadístico.

---

## Objetivos

- Implementar una API REST funcional con FastAPI  
- Aplicar validación robusta de datos con Pydantic  
- Simular almacenamiento en memoria  
- Desarrollar operaciones CRUD completas  
- Generar estadísticas descriptivas básicas  
- Implementar manejo de errores HTTP 422  
- Aplicar decoradores personalizados  

---

## Estructura del Proyecto

```bash
encuesta-api/
│
├── main.py            # API y endpoints
├── models.py          # Modelos Pydantic y validaciones
├── validators.py      # Listas auxiliares (departamentos)
├── requirements.txt   # Dependencias
├── README.md          # Documentación
└── .gitignore
