from pydantic import BaseModel
from typing import Any


class Product(BaseModel):
    nombre: str
    id: int
    categorias: Any
    descripcion: str
    precio: float
    link: str
    casos_de_uso: str | None
