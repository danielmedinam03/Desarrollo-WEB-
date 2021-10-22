CREATE SCHEMA VideoJuegos; 
USE VideoJuegos;
CREATE TABLE genero(
	cod_Genero VARCHAR(10) NOT NULL PRIMARY KEY,
    des_Genero VARCHAR(15) NOT NULL
);
CREATE TABLE estado_civil(
	cod_EstadoCivil VARCHAR(10) NOT NULL PRIMARY KEY,
    des_EstadoCivil VARCHAR(15) NOT NULL
);
CREATE TABLE estrato(
	cod_Estrato VARCHAR(10) NOT NULL PRIMARY KEY,
    des_Estrato VARCHAR(15) NOT NULL
);
CREATE TABLE forma_pago(
	cod_FormaPago VARCHAR(10) NOT NULL PRIMARY KEY,
    des_FormaPago VARCHAR(15) NOT NULL
);
CREATE TABLE tipo_id(
	cod_TipoID VARCHAR(10) NOT NULL PRIMARY KEY,
    des_TipoID VARCHAR(15) NOT NULL
);
CREATE TABLE productos(
	cod_Producto VARCHAR(10) PRIMARY KEY,
    nombre_Producto VARCHAR(15) NOT NULL,
    valor_unitario INTEGER,
	KEY precio (valor_unitario),
    descuento INTEGER 
);
CREATE TABLE persona(
	numero_ID INTEGER NOT NULL PRIMARY KEY,
    cod_TipoID VARCHAR(15) NOT NULL,
    nombre_1 VARCHAR(50) NOT NULL,
    nombre_2 VARCHAR(50),
    apellido_1 VARCHAR(50) NOT NULL,
    apellido_2 VARCHAR(50),
    fecha_Nacimiento DATE,
    celular INTEGER,
    cod_Genero VARCHAR(50),
    telefono INTEGER,
    correo VARCHAR(100),
    direccion VARCHAR(50),
    cod_Estrato VARCHAR(15),
    cod_EstadoCivil VARCHAR(15),
    FOREIGN KEY (cod_TipoID) REFERENCES tipo_id(cod_TipoID),
	FOREIGN KEY (cod_Genero) REFERENCES genero(cod_Genero),
    FOREIGN KEY (cod_Estrato) REFERENCES estrato(cod_Estrato),
    FOREIGN KEY (cod_EstadoCivil) REFERENCES estado_civil(cod_EstadoCivil)
);

CREATE TABLE movimiento_encabezado(
	cod_Movimiento VARCHAR(15),
    numero_movimiento INTEGER,
	fecha_movimiento DATE,
    numero_ID INTEGER,
    cod_FormaPago VARCHAR(15),
    observaciones VARCHAR(100),
    PRIMARY KEY (cod_Movimiento, numero_movimiento),
    FOREIGN KEY (numero_ID) REFERENCES persona(numero_ID),
    FOREIGN KEY (cod_FormaPago) REFERENCES forma_pago(cod_FormaPago)
);

CREATE TABLE movimiento_detalle(
	cod_Movimiento VARCHAR(15),
    numero_movimiento INTEGER,
    item INTEGER AUTO_INCREMENT UNIQUE,
    cod_Producto VARCHAR(15),
    valor_unitario INTEGER,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (cod_Movimiento, numero_movimiento),
	FOREIGN KEY (cod_Movimiento,numero_movimiento) REFERENCES movimiento_encabezado(cod_Movimiento, numero_movimiento),
	FOREIGN KEY (cod_Producto) REFERENCES productos(cod_Producto),
    FOREIGN KEY (valor_unitario) REFERENCES productos(valor_unitario)
);