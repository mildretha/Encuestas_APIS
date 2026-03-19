
from pydantic import BaseModel, Field, field_validator
from typing import List, Union, Optional
from validators import DEPARTAMENTOS_COLOMBIA



encuestas_db = []
contador_id = 1


# -------------------------
# MODELO 1: Encuestado
# -------------------------
class Encuestado(BaseModel):
    nombre: str = Field(..., example="Juan Pérez")
    edad: int = Field(..., example=30)
    estrato: int = Field(..., example=3)
    departamento: str = Field(..., example="Cundinamarca")

    @field_validator("edad")
    def validar_edad(cls, value):
        if not (0 <= value <= 120):
            raise ValueError("La edad debe estar entre 0 y 120")
        return value

    @field_validator("estrato")
    def validar_estrato(cls, value):
        if value not in range(1, 7):
            raise ValueError("El estrato debe estar entre 1 y 6")
        return value

    @field_validator("departamento", mode="before")
    def validar_departamento(cls, value):
        value = value.strip().title()
        if value not in DEPARTAMENTOS_COLOMBIA:
            raise ValueError("Departamento no válido")
        return value

# -------------------------
# MODELO 2: Respuesta
# -------------------------
class RespuestaEncuesta(BaseModel):
    pregunta_id: int
    respuesta: Union[int, float, str]
    comentario: Optional[str] = None

    @field_validator("respuesta", mode="after")
    def validar_respuesta(cls, value):
        if isinstance(value, int):
            if not (1 <= value <= 5):
                raise ValueError("Likert debe estar entre 1 y 5")
        elif isinstance(value, float):
            if not (0.0 <= value <= 100.0):
                raise ValueError("Porcentaje debe estar entre 0 y 100")
        return value

# -------------------------
# MODELO 3: Encuesta Completa
# -------------------------
class EncuestaCompleta(BaseModel):
    encuestado: Encuestado
    respuestas: List[RespuestaEncuesta]

    model_config = {
        "json_schema_extra": {
            "example": {
                "encuestado": {
                    "nombre": "Ana",
                    "edad": 28,
                    "estrato": 2,
                    "departamento": "Antioquia"
                },
                "respuestas": [
                    {"pregunta_id": 1, "respuesta": 5},
                    {"pregunta_id": 2, "respuesta": 80.5}
                ]
            }
        }
    }