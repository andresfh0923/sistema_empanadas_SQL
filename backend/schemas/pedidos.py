from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .clientes import Cliente
from .productos import Producto


class PedidoBase(BaseModel):
    estado:str="Pendiente"
    cantidad:int
    id_cliente_fk:int
    id_producto_fk:int


class PedidoCreate(PedidoBase):
    pass


class Pedido(PedidoBase):
    id_pedido:int
    fecha_de_pedido:datetime
    fecha_de_entrega:Optional[datetime]=None
    cliente:Cliente
    producto:Producto
    model_config={"from_attributes":True}