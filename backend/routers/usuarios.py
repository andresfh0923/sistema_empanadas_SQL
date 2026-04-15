from fastapi import APIRouter
from schemas.usuarios import UsuarioCreate

router=APIRouter()
 

@router.post('/usuarios/')
def crear_usuario(usuario: UsuarioCreate):
    return {"mensaje":f"usuario recibido {usuario.nombre} listo para hashear y guardar"}