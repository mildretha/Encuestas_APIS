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
```


## Instalación y Ejecución

### 1. Clonar repositorio

```bash
git clone <TU_REPO_URL>
cd encuesta-api
```
### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
uvicorn main:app --reload
```

### 5. Acceder a la documentación

- **Swagger UI:** http://127.0.0.1:8000/docs  
- **Redoc:** http://127.0.0.1:8000/redoc


### 6. Modelos de Datos

##### Encuestado

Contiene información demográfica:

- **nombre**  
- **edad** *(0-120)*  
- **estrato** *(1-6)*  
- **departamento** *(validado contra lista oficial)*  

##### RespuestaEncuesta

- **pregunta_id**  
- **respuesta** *(int, float o string)*  
- **comentario** *(opcional)*  

##### EncuestaCompleta

- **encuestado**  
- **respuestas** *(lista de respuestas)*

### 7. Validaciones Implementadas

- Edad entre **0 y 120**  
- Estrato entre **1 y 6**  
- Departamento válido en Colombia  
- Escala Likert (**1-5**)  
- Porcentajes (**0-100**)  

Se utilizan validadores de tipo:

```python
@field_validator(mode="before")
@field_validator(mode="after")
  
```

### 8. Endpoints

| Método | Ruta                       | Descripción         |
|--------|----------------------------|---------------------|
| GET    | `/`                        | Estado de la API    |
| POST   | `/encuestas/`              | Crear encuesta      |
| GET    | `/encuestas/`              | Listar encuestas    |
| GET    | `/encuestas/{id}`          | Obtener por ID      |
| PUT    | `/encuestas/{id}`          | Actualizar encuesta |
| DELETE | `/encuestas/{id}`          | Eliminar encuesta   |
| GET    | `/encuestas/estadisticas/` | Estadísticas        |



### 9. Estadísticas

El endpoint `/encuestas/estadisticas/` calcula:

- Total de encuestas  
- Promedio de edad  
- Distribución por estrato  
