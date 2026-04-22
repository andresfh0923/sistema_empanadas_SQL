from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nombre_cliente:str
    nombre_negocio:str
    telefono:str
    direccion:Optional[str]=None


class CreateCliente(ClienteBase):
    pass

class Cliente(ClienteBase):
    id_cliente:int
    fecha_creacion:datetime
    model_config={"from_attributes":True}
