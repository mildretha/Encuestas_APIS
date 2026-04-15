#  API de Gestión de Encuestas Poblacionales Colombia

<img width="300" height="300" alt="Logo USTA" src="https://github.com/user-attachments/assets/6b48f2b0-160b-4935-a7d3-37574f7a0d23" />

---

##  Descripción del Proyecto

Esta API REST fue desarrollada con **FastAPI** y tiene como objetivo simular un sistema de recolección, validación y análisis de datos provenientes de encuestas poblacionales en Colombia.

El sistema funciona como una **“aduana inteligente de datos”**, garantizando que la información ingresada sea válida, coherente y estructuralmente correcta antes de ser almacenada y analizada.

---

## ✔️ Objetivos del Proyecto

- Construir una API REST moderna con FastAPI  
- Implementar validación avanzada con Pydantic  
- Simular almacenamiento en memoria (sin base de datos)  
- Desarrollar operaciones CRUD completas  
- Generar estadísticas descriptivas automáticas  
- Manejar errores HTTP de forma estructurada  
- Aplicar arquitectura modular (models, services, store, loaders)  

---

## ✔️ Estructura del Proyecto

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
```


## ✔️ Instalación y Ejecución

### ✔️ Clonar el repositorio

```bash
git clone https://github.com/mildretha/Encuestas_APIS
cd Encuestas_APIS
```

## ✔️ Crear entorno virtual

```bash
python -m venv venv
```


## ✔️ Activar entorno virtual

### 🪟 Windows
```bash
venv\Scripts\activate
```

## ✔️ Instalar dependencias

```bash
pip install -r requirements.txt
```


## ✔️ Ejecutar la API

```bash
uvicorn main:app --reload
```

## ✔️ Acceso a la API

Una vez ejecutado el servidor, puedes acceder a la documentación interactiva:

- 📘 Swagger UI: http://127.0.0.1:8000/docs  
- 📕 ReDoc: http://127.0.0.1:8000/redoc


## ✔️ Modelos de Datos

La API trabaja con tres modelos principales:

### 👤 Encuestado
Representa la información demográfica del participante:
- Nombre  
- Edad (0 a 120 años)  
- Estrato socioeconómico (1 a 6)  
- Departamento de Colombia  
- Municipio  
- Género  
- Nivel educativo  
- Ingresos mensuales  
- Personas en el hogar  
- Tipo de vivienda  
- Situación laboral  

---

### ✔️ RespuestaEncuesta
Representa cada respuesta dentro de la encuesta:
- ID de la pregunta  
- Texto de la pregunta  
- Tipo de pregunta (likert, porcentaje, texto, número)  
- Respuesta validada según el tipo  
- Observación opcional  

---

### ✔️ EncuestaCompleta
Modelo principal que agrupa toda la información:
- Datos del encuestado  
- Lista de respuestas  
- Fecha de diligenciamiento  
- Versión de la encuesta


## ✔️ Endpoints de la API

La API expone los siguientes endpoints para gestionar las encuestas:

| Método | Endpoint                     | Descripción               |
|--------|-----------------------------|---------------------------|
| GET    | `/`                         | Estado de la API          |
| POST   | `/encuestas/`              | Crear una encuesta        |
| GET    | `/encuestas/`              | Listar todas las encuestas|
| GET    | `/encuestas/{id}`          | Obtener una encuesta      |
| PUT    | `/encuestas/{id}`          | Actualizar una encuesta   |
| DELETE | `/encuestas/{id}`          | Eliminar una encuesta     |
| GET    | `/encuestas/estadisticas/` | Ver estadísticas globales |


## ✔️ Ejemplos para Probar los Endpoints

A continuación se muestran ejemplos de cómo consumir la API utilizando JSON en los principales endpoints.

---

### ✔️ 1. Crear una encuesta (POST /encuestas/)

```json
{
  "encuestado": {
    "nombre": "Laura Martínez",
    "edad": 29,
    "genero": "femenino",
    "estrato": 3,
    "departamento": "ANTIOQUIA",
    "municipio": "Medellín",
    "nivel_educativo": "universitario",
    "ingresos_mensuales": 3200000,
    "personas_hogar": 3,
    "vivienda": "propia",
    "situacion_laboral": "Empleado"
  },
  "respuestas": [
    {
      "pregunta_id": "P001",
      "pregunta_texto": "¿Qué tan satisfecho está con los servicios públicos?",
      "tipo_pregunta": "likert",
      "respuesta": 4
    },
    {
      "pregunta_id": "P002",
      "pregunta_texto": "¿Porcentaje de ingreso destinado a vivienda?",
      "tipo_pregunta": "porcentaje",
      "respuesta": 30.5
    }
  ],
  "fecha_diligenciamiento": "2026-03-20",
  "encuesta_version": "1.0"
}
```




## ✔️ Validaciones Implementadas

La API incluye validaciones robustas para garantizar la calidad de los datos:

- Edad entre **0 y 120 años**
- Estrato socioeconómico entre **1 y 6**
- Departamentos válidos de Colombia
- Género validado contra lista permitida
- Escala Likert de **1 a 5**
- Porcentajes entre **0 y 100**
- Tipos de pregunta controlados (likert, porcentaje, texto, número)
- Normalización de texto (mayúsculas/minúsculas)
- Validación de campos obligatorios
- Prevención de respuestas duplicadas por pregunta_id


## ✔️ Estadísticas del Sistema

La API genera automáticamente estadísticas a partir de las encuestas almacenadas:

- Total de encuestas registradas  
- Promedio de edad de los encuestados  
- Mediana de edad  
- Distribución por estrato socioeconómico  
- Distribución por departamento  
- Distribución por género  
- Promedio de respuestas por encuesta  
- Satisfacción con el gobierno por departamento

## ✔️ Arquitectura del Sistema

El proyecto está organizado bajo una arquitectura modular que separa responsabilidades para mejorar la mantenibilidad y escalabilidad:

### ✔️ main.py
Es el punto de entrada de la API con FastAPI. Aquí se definen todos los endpoints y se conectan con la lógica de negocio.

### ✔️ models.py
Contiene los modelos de datos basados en Pydantic. Aquí se realizan todas las validaciones de estructura, tipos y reglas del negocio.

### ✔️ validators.py
Define reglas del dominio colombiano como:
- Departamentos válidos
- Escala Likert
- Opciones de género, vivienda y situación laboral

### ✔️ services.py
Contiene la lógica de negocio:
- CRUD de encuestas
- Cálculo de estadísticas
- Procesamiento de datos

### ✔️ store.py
Simula una base de datos en memoria usando un diccionario Python.

### ✔️ loaders.py
Permite la carga de datos desde:
- Archivos locales (CSV, JSON, Excel, etc.)
- URLs externas
- APIs REST

### ✔️ tests/
Contiene pruebas unitarias e integración para validar:
- Modelos
- Endpoints
- Reglas del sistema

---

## ✔️ Autor

Este proyecto fue desarrollado por:

**Alejandra Díaz**  
Estudiante de **Estadística**  
Universidad Santo Tomás (USTA)

---

## ✔️ Repositorio del Proyecto

El código fuente completo de esta API está disponible en GitHub:

✔️ https://github.com/mildretha/Encuestas_APIS

---

## ✔️ Contexto Académico

Este proyecto fue desarrollado como parte de la formación en la carrera de Estadística, con el objetivo de aplicar conocimientos en:

- Programación con Python
- Desarrollo de APIs con FastAPI
- Modelado de datos con Pydantic
- Validación estadística de información
- Construcción de sistemas de análisis de datos
- Buenas prácticas de ingeniería de software

---




