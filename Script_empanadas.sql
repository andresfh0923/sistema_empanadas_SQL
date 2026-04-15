-- Script principal del sistema de empanadas.
-- Creado por: Andres Felipe Hernandez Rendon.

CREATE DATABASE sistema_empanadas;
USE sistema_empanadas;
	
-- tabla de usuarios con los roles definidos.
create table usuarios (     
id_usuario int auto_increment primary key,
rol enum ('admin','empleado')not null default 'empleado',
nombre varchar (100) not null,
contrasena varchar(255) not null
) ;

-- tabla de clientes con datos minimos.
create table clientes (
id_cliente int auto_increment primary key,
nombre_cliente varchar (100) not null,
nombre_negocio varchar (100),
telefono varchar (15),
direccion text,
fecha_creacion timestamp default current_timestamp
);

-- tabla de productos con los campos para hacer operaciones del negocio.
create table producto (
id_producto int auto_increment primary key,
nombre_producto varchar(50),
valor_de_produccion decimal(10,2),
valor_de_venta decimal(10,2)
);

-- tabla de pedidos con llaves para conectar con clientes y productos.
create table pedidos(
id_pedido int auto_increment primary key,
estado varchar (20) default "Pendiente",
cantidad int not null,
fecha_de_pedido timestamp default now(),
fecha_de_entrega timestamp null default null,
id_cliente_fk int,
id_producto_fk int,

foreign key(id_cliente_fk) references clientes(id_cliente),
foreign key(id_producto_fk) references producto(id_producto)
);

-- el corazon financiero.
create table movimientos_caja(
id_movimiento int auto_increment primary key,
tipo enum ('pago','retiro') not null,
monto decimal (10,2) not null,
saldo_total decimal (10,2) not null,
fecha_movimiento timestamp default current_timestamp,
id_usuario_fk int,

foreign key(id_usuario_fk) references usuarios(id_usuario)
);

-- para registrar los pagos asociados a un cliente y plasmado en los movimientos.
create table pagos(
id_pago int auto_increment primary key,
monto decimal (10,2) not null,
id_movimiento_fk int,
id_cliente_fk int,

foreign key(id_movimiento_fk) references movimientos_caja(id_movimiento),
foreign key(id_cliente_fk) references clientes(id_cliente)
);

-- para egresos de la empresa y compra de materia prima, se refleja en movimientos.
create table retiros(
id_retiro int auto_increment primary key,
motivo enum ('retiro admin','compras') not null,
monto decimal (10,2) not null,
id_movimiento_fk int,

foreign key(id_movimiento_fk) references movimientos_caja(id_movimiento)
);

-- para consultas financieras (solo admin).
create table historial(
id_historial int auto_increment primary key,
monto decimal (10,2) not null,
tipo enum ('pago','retiro') not null,
fecha_registro timestamp default current_timestamp,
id_cliente_fk int,
id_movimiento_fk int,
id_retiro_fk int,
id_usuario_fk int,
id_pedido_fk int,

foreign key(id_cliente_fk) references clientes(id_cliente),
foreign key(id_movimiento_fk) references movimientos_caja(id_movimiento),
foreign key(id_retiro_fk) references retiros(id_retiro),
foreign key(id_usuario_fk) references usuarios(id_usuario),
foreign key(id_pedido_fk) references pedidos(id_pedido)
);

-- todas las llaves foraneas y funciones de cada linea, son especificadas en la documentacion.
