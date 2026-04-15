from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashear_contrasena(contrasena: str):
    return pwd_context.hash(contrasena)


def verificar_contrasena(plain_contrasena, hashed_contrasena):
    return pwd_context.verify(plain_contrasena, hashed_contrasena)