from backend.database import engine,Base #importación para la conexión a la bese de datos.
import backend.models as models
 
#funcion para la creación de las tablas en la base de datos, siguiendo models.py.
def init():
    print('Conectando a la base de datos....')
    Base.metadata.create_all(bind=engine)
    print('proceso terminado, creación de tablas exitoso')


if __name__=='__main__':
    init()