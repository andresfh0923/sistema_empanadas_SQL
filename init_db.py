from backend.database import engine,Base
import backend.models as models
 

def init():
    print('Conectando a la base de datos....')
    Base.metadata.create_all(bind=engine)
    print('proceso terminado, creación de tablas exitoso')


if __name__=='__main__':
    init()