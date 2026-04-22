from pydantic import BaseModel,EmailStr

class UsuarioBase(BaseModel):
    nombre:str
    telefono:str
    rol:str="usuario"
    email:EmailStr


class UsuarioCreate(UsuarioBase):
    contrasena:str


class Usuario(UsuarioBase):
    id_usuario:int
    model_config={"from_attributes":True}