from .database import Base
from sqlalchemy import Column,Integer,String,Enum,Text,TIMESTAMP,func,DECIMAL,ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__='usuarios'
    id_usuario=Column(Integer,primary_key=True)
    rol=Column(Enum('admin','empleado'),nullable=False,default='empleado')
    nombre=Column(String(100),nullable=False)
    contrasena=Column(String(255),nullable=False)


class Cliente(Base):
    __tablename__='clientes'
    id_cliente=Column(Integer,primary_key=True)
    nombre_cliente=Column(String(100),nullable=False)
    nombre_negocio=Column(String(100))
    telefono=Column(String(15))
    direccion=Column(Text)
    fecha_creacion=Column(TIMESTAMP,server_default=func.now())


class Producto(Base):
    __tablename__='producto'
    id_producto=Column(Integer,primary_key=True)
    nombre_producto=Column(String(50),nullable=False)
    valor_de_produccion=Column(DECIMAL(10,2),nullable=False)
    valor_de_venta=Column(DECIMAL(10,2),nullable=False)


class Pedido(Base):
    __tablename__='pedidos'
    id_pedido=Column(Integer,primary_key=True)
    estado=Column(String(20),default='Pendiente')
    cantidad=Column(Integer,nullable=False)
    fecha_de_pedido=Column(TIMESTAMP,server_default=func.now())
    fecha_de_entrega=Column(TIMESTAMP,default=None)
    id_cliente_fk=Column(Integer,ForeignKey("clientes.id_cliente"))
    id_producto_fk=Column(Integer,ForeignKey("producto.id_producto")) 
    cliente=relationship("Cliente")
    producto=relationship("Producto")


class MovimientoCaja(Base):
    __tablename__='movimientos_caja'
    id_movimiento=Column(Integer,primary_key=True)
    tipo=Column(Enum('pago','retiro'),nullable=False)
    monto=Column(DECIMAL(10,2),nullable=False)
    saldo_total=Column(DECIMAL(10,2),nullable=False)
    fecha_movimiento=Column(TIMESTAMP,server_default=func.now(),nullable=False)
    id_usuario_fk=Column(Integer,ForeignKey("usuarios.id_usuario"))
    usuario=relationship("Usuario")


class Pago(Base):
    __tablename__='pagos'
    id_pago=Column(Integer,primary_key=True)
    monto=Column(DECIMAL(10,2),nullable=False)
    id_movimiento_fk=Column(Integer,ForeignKey("movimientos_caja.id_movimiento"))
    id_cliente_fk=Column(Integer,ForeignKey("clientes.id_cliente"))
    movimiento=relationship("MovimientoCaja")
    cliente=relationship("Cliente")


class Retiro(Base):
    __tablename__='retiros'
    id_retiro=Column(Integer,primary_key=True)
    motivo=Column(Enum('retiro admin','compras'),nullable=False)
    monto=Column(DECIMAL(10,2),nullable=False)
    id_movimiento_fk=Column(Integer,ForeignKey("movimientos_caja.id_movimiento"))
    movimiento=relationship("MovimientoCaja")


class Historial(Base):
    __tablename__='historial'
    id_historial=Column(Integer,primary_key=True)
    monto=Column(DECIMAL(10,2),nullable=False)
    tipo=Column(Enum('pago','retiro'),nullable=False)
    fecha_registro=Column(TIMESTAMP,server_default=func.now())
    id_cliente_fk=Column(Integer,ForeignKey("clientes.id_cliente"))
    id_movimiento_fk=Column(Integer,ForeignKey("movimientos_caja.id_movimiento"))
    id_retiro_fk=Column(Integer,ForeignKey("retiros.id_retiro")) 
    id_usuario_fk=Column(Integer,ForeignKey("usuarios.id_usuario"))
    id_pedido_fk=Column(Integer,ForeignKey("pedidos.id_pedido"))
    cliente=relationship("Cliente")
    movimiento=relationship("MovimientoCaja")
    retiro=relationship("Retiro")
    usuario=relationship("Usuario")
    pedido=relationship("Pedido")
