from pydantic import BaseModel
from typing import Literal
from decimal import Decimal
from .movimientos import MovimientoCaja


class RetiroBase(BaseModel):
    motivo:Literal['retiro admin','compras']
    monto:Decimal
    id_movimiento_fk:int


class RetiroCreate(RetiroBase):
    pass


class Retiro(RetiroBase):
    id_retiro:int
    movimiento:MovimientoCaja
    model_config={"from_attributes":True}
