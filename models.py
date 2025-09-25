from dataclasses import dataclass
from datetime import datetime

@dataclass
class Movimiento:
    tipo: str
    monto: float
    categoria: str
    descripcion: str
    fecha: datetime
