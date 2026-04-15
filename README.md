# 📊 API de Gestión de Encuestas Poblacionales Colombia

<img width="300" height="300" alt="Logo USTA" src="https://github.com/user-attachments/assets/6b48f2b0-160b-4935-a7d3-37574f7a0d23" />

---

## 📌 Descripción del Proyecto

Esta API REST fue desarrollada con **FastAPI** y tiene como objetivo simular un sistema de recolección, validación y análisis de datos provenientes de encuestas poblacionales en Colombia.

El sistema funciona como una **“aduana inteligente de datos”**, garantizando que la información ingresada sea válida, coherente y estructuralmente correcta antes de ser almacenada y analizada.

---

## 🎯 Objetivos del Proyecto

- Construir una API REST moderna con FastAPI  
- Implementar validación avanzada con Pydantic  
- Simular almacenamiento en memoria (sin base de datos)  
- Desarrollar operaciones CRUD completas  
- Generar estadísticas descriptivas automáticas  
- Manejar errores HTTP de forma estructurada  
- Aplicar arquitectura modular (models, services, store, loaders)  

---

## 🧱 Estructura del Proyecto

```bash
encuesta-api/
│
├── main.py              # Punto de entrada de la API (FastAPI)
├── models.py            # Modelos Pydantic y validaciones de datos
├── validators.py       # Reglas del dominio colombiano
├── services.py         # Lógica de negocio (CRUD + estadísticas)
├── store.py            # Base de datos en memoria
├── loaders.py          # Carga de datos desde archivos, URLs y APIs
│
├── tests/              # Pruebas unitarias e integración
│   ├── test_models.py
│   └── test_endpoints.py
│
├── logs/               # Archivos de logs del sistema
│   ├── encuesta_api.log
│   └── frontend_errores.log
│
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación principal
└── .gitignore          # Archivos ignorados por Git
