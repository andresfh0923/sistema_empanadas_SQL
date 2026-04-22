from pydantic import BaseModel
from decimal import Decimal

class ProductoBase(BaseModel):
    nombre_producto:str
    valor_de_produccion:Decimal
    valor_de_venta:Decimal

    
class CreateProducto(ProductoBase):
    pass


class Producto(ProductoBase):
    id_producto:int
    model_config={"from_attributes":True}