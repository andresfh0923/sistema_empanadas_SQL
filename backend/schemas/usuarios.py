from pydantic import BaseModel,EmailStr

class UsuarioCreate(BaseModel):
    nombre:str
    telefono:str
    rol=str
    contrasena:str
    email:EmailStr