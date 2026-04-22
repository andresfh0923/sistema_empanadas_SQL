from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from .usuarios import Usuario
from typing import Literal


class MovimientoCajaBase(BaseModel):
    tipo:Literal['pago','retiro']
    monto:Decimal
    id_usuario_fk:int

class MovimientoCajaCreate(MovimientoCajaBase):
    pass


class MovimientoCaja(MovimientoCajaBase):
    id_movimiento:int
    saldo_total:Decimal
    fecha_movimiento:datetime
    usuario:Usuario
    model_config={"from_attributes":True}