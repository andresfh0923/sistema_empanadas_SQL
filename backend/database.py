from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#conexion con base de datos, parametros para cada sesión y declaración de modelo. 
DATABASE_URL='mysql+pymysql://root@localhost:3306/sistema_empanadas'
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(autocommit=False,bind=engine,autoflush=False)
Base=declarative_base()

#funcion para asegurar que cada sesión se cierre.
def get_db():
    db=SessionLocal()
    try:
       yield db
    finally:
        db.close()