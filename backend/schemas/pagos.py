from pydantic import BaseModel
from decimal import Decimal
from .movimientos import MovimientoCaja
from .clientes import Cliente


class PagoBase(BaseModel):
    monto:Decimal
    id_movimiento_fk:int
    id_cliente_fk:int


class PagoCreate(PagoBase):
    pass


class Pago(PagoBase):
    id_pago:int
    movimiento:MovimientoCaja
    cliente:Cliente
    model_config={"from_attributes":True}
