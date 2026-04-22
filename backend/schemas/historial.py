from pydantic import BaseModel
from decimal import Decimal
from typing import Literal,Optional
from datetime import datetime
from .clientes import Cliente
from .movimientos import MovimientoCaja
from .retiros import Retiro
from .usuarios import Usuario
from .pedidos import Pedido


class Historial(BaseModel):
    id_historial:int
    monto:Decimal
    tipo:Literal['pago','retiro']
    fecha_registro:datetime
    id_cliente_fk:Optional[int]=None
    id_movimiento_fk:Optional[int]=None
    id_retiro_fk:Optional[int]=None
    id_usuario_fk:int
    id_pedido_fk:Optional[int]=None
    cliente:Optional[Cliente]=None
    movimiento:Optional[MovimientoCaja]=None
    retiro:Optional[Retiro]=None
    usuario:Usuario
    pedido:Optional[Pedido]=None
    model_config={"from_attributes":True}