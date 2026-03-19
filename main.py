from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from models import EncuestaCompleta
import logging
from datetime import datetime
from functools import wraps




# --------------------------------------------------
# ✅ CREAR APP (SIEMPRE PRIMERO)
# --------------------------------------------------
app = FastAPI(title="API Encuestas Poblacionales")


def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Endpoint llamado: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper






# --------------------------------------------------
# ✅ CONFIGURAR LOGS
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------
# ✅ DECORADOR PERSONALIZADO
# --------------------------------------------------
def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Endpoint llamado: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# --------------------------------------------------
# ✅ MANEJO PERSONALIZADO DE ERRORES 422
# --------------------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = []

    for err in exc.errors():
        errores.append({
            "campo": err["loc"],
            "mensaje": err["msg"]
        })

    logging.error(f"Error de validación en {request.url}: {errores}")

    return JSONResponse(
        status_code=422,
        content={
            "error": "Datos inválidos",
            "detalle": errores
        }
    )

# --------------------------------------------------
# 📦 "BASE DE DATOS" EN MEMORIA
# --------------------------------------------------
encuestas_db = []
contador_id = 1

# --------------------------------------------------
# 🏠 ENDPOINT BASE
# --------------------------------------------------
@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

# --------------------------------------------------
# ➕ POST (CREAR ENCUESTA)
# --------------------------------------------------
@app.post("/encuestas/", status_code=201)
@log_request
def crear_encuesta(encuesta: EncuestaCompleta):
    global contador_id

    nueva_encuesta = encuesta.dict()
    nueva_encuesta["id"] = contador_id

    encuestas_db.append(nueva_encuesta)
    contador_id += 1

    return nueva_encuesta

# --------------------------------------------------
# 📋 GET (LISTAR TODAS)
# --------------------------------------------------
@app.get("/encuestas/")
def listar_encuestas():
    return encuestas_db

# --------------------------------------------------
# 🔍 GET POR ID
# --------------------------------------------------
@app.get("/encuestas/{id}")
def obtener_encuesta(id: int):
    for encuesta in encuestas_db:
        if encuesta["id"] == id:
            return encuesta
    raise HTTPException(status_code=404, detail="Encuesta no encontrada")

# --------------------------------------------------
# ✏️ PUT (ACTUALIZAR)
# --------------------------------------------------
@app.put("/encuestas/{id}")
def actualizar_encuesta(id: int, encuesta_actualizada: EncuestaCompleta):
    for index, encuesta in enumerate(encuestas_db):
        if encuesta["id"] == id:
            nueva_encuesta = encuesta_actualizada.dict()
            nueva_encuesta["id"] = id
            encuestas_db[index] = nueva_encuesta
            return nueva_encuesta

    raise HTTPException(status_code=404, detail="Encuesta no encontrada")

# --------------------------------------------------
# ❌ DELETE (ELIMINAR)
# --------------------------------------------------
@app.delete("/encuestas/{id}", status_code=204)
def eliminar_encuesta(id: int):
    for index, encuesta in enumerate(encuestas_db):
        if encuesta["id"] == id:
            encuestas_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="Encuesta no encontrada")

# --------------------------------------------------
# 📊 ESTADÍSTICAS
# --------------------------------------------------
@app.get("/encuestas/estadisticas/")
def obtener_estadisticas():
    if len(encuestas_db) == 0:
        return {
            "total_encuestas": 0,
            "promedio_edad": 0,
            "distribucion_estrato": {}
        }

    total = len(encuestas_db)

    suma_edades = sum(e["encuestado"]["edad"] for e in encuestas_db)
    promedio_edad = suma_edades / total

    distribucion = {}
    for e in encuestas_db:
        estrato = e["encuestado"]["estrato"]
        distribucion[estrato] = distribucion.get(estrato, 0) + 1

    return {
        "total_encuestas": total,
        "promedio_edad": promedio_edad,
        "distribucion_estrato": distribucion
    }