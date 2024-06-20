-- Practica 2: Archivo sql con las mismas intrucciones del EjercicioUno
-- Alumn@: Gabriela Lopez Diego
-- Curso: Ingenieria de Software 2024-1
-- Fecha: 16/sep/23

-- Crear la tabla 'clientes'
CREATE TABLE CLIENTES (
    Id_cliente int NOT NULL primary key,
    Nombre VARCHAR(50) NOT NULL,
    Domicilio VARCHAR(60) NOT NULL,
    Ciudad VARCHAR(20) NOT NULL,
    Estado VARCHAR(20) NOT NULL,
    CodigoPostal INT NOT NULL,
    Email VARCHAR(30)
);

-- Crear la tabla 'productos'
CREATE TABLE PRODUCTOS (
    Id_producto int NOT NULL primary key NOT NULL,
    Descripcion VARCHAR(80) NOT NULL,
    Precio INT NOT NULL,
    Marca VARCHAR(20) NOT NULL,
    Existencia INT NOT NULL
);

-- Crear la tabla 'proveedores'
CREATE TABLE PROVEEDORES (
    Empresa VARCHAR(20) NOT NULL,
    NombreContacto VARCHAR(50) primary key NOT NULL,
    Direccion VARCHAR(100) NOT NULL,
    Ciudad VARCHAR(50) NOT NULL,
    Estado VARCHAR(30) NOT NULL,
    CodigoPostal INT NOT NULL,
    Email VARCHAR(50) NOT NULL
);

-- Crear la tabla 'pedidos'
CREATE TABLE PEDIDOS(
    Num_Pedido int NOT NULL primary key,
    fechaPedido DATE NOT NULL,
    Vendedor VARCHAR(50) NOT NULL,
    Id_producto INT NOT NULL,
    Id_cliente INT NOT NULL,
    Cantidad INT NOT NULL,
    Precio INT NOT NULL,
    Total INT NOT NULL
);

-- CREATE. Agregamos 15 datos a cada una de las tablas
-- Tabla 'clientes'
INSERT INTO CLIENTES (Id_cliente, Nombre, Domicilio, Ciudad, Estado, CodigoPostal, Email)
VALUES
(1, 'Jose Lopez', 'Calle Girasol', 'La Paz', 'Baja California Sur', 48292, 'cliente1@gmail.com'),
(2, 'Ana Maria', 'Calle Zapata Col. Centro', 'Tuxtla Gutierrez', 'Chiapas', 29000, 'cliente2@gmail.com'),
(3, 'Rodrigo', 'Cale Primavera Col. Libertad', 'Toluca', 'Estado De Mexico', 63799, 'cliente3@gmail.com'),
(4, 'Alicia', 'Calle del bosque Col. Santa Cruz', 'Guadalupe Victoria', 'Durango', 59371, 'cliente4@gmail.com'),
(5, 'Jesus', 'Calle Rosa Col. Santa lucia', 'Durango', 'Durango', 77835, 'cliente5@gmail.com'),
(6, 'Avril', 'Calle 20 Col. Los Robles', 'Xalapa', 'Veracruz', 23548, 'cliente6@gmail.com'),
(7, 'Paola', 'Calle Victoria Col. Las lomas', 'Hermosillo', 'Sonora', 75964, 'cliente7@gmail.com'),
(8, 'Jazmin', 'Calle Estrella Col. Alamos', 'Nogales', 'Sonora', 23458, 'cliente8@gmail.com'),
(9, 'Sara', 'Calle Rubi, Col. las lomas', 'Tapachula', 'Chiapas', 45894, 'cliente9@gmail.com'),
(10, 'Pablo', 'Calle Francisco Vila, Col. Santa Fe', 'Cancun', 'Quintana Roo', 41456, 'cliente10@gmail.com'),
(11, 'Kevin', 'Calle Rio Grande Col. La magdalena', 'Cordoba', 'Veracruz', 27894, 'cliente11@gmail.com'),
(12, 'Maria', 'Calle San Vicente Col. San Agustin', 'Merida', 'Yucatan', 88934, 'cliente12@gmail.com'),
(13, 'Jessica', 'Calle Trigo, Col. Jardines', 'Ciudad Lerdo', 'Durango', 75847, 'cliente13@gmail.com'),
(14, 'Joselyn', 'Calle Montiel, Col. Santa Fe', 'Villa Hermosa', 'Tabasco', 34916, 'cliente14@gmail.com'),
(15, 'Michel', 'Calle Luis Moya, Col. Estrella', 'Chetumal', 'Quintana Roo', 11479, 'cliente15@gmail.com');

-- Tabla 'productos'
INSERT INTO PRODUCTOS (Id_cliente, Descripcion, Precio, Marca, Existencia)
VALUES
(1, 'Pantalla', 5000, 'Samsung', 17),
(2, 'Celular', 5000, 'Huawei', 10),
(3, 'Servilletas', 45, 'Suavel', 100),
(4, 'Rubor', 790, 'Rare Beauty', 200),
(5, 'Laptop', 14000, 'DELL', 50),
(6, 'Plumones', 55, 'Touch', 100),
(7, 'Gloss Magico', 150, 'Loreal', 100),
(8, 'Tintas para labios', 200, 'Rare Beauty', 500),
(9, 'Polvo de hadas', 150, 'Rare Beauty', 400),
(10, 'Espejos de mano', 35, 'Rare Beauty', 50),
(11, 'Serum', 300, 'Rare Beauty', 100),
(12, 'Delineador', 150, 'Rare Beauty', 100),
(13, 'Mascara', 200, 'Rare Beauty', 100),
(14, 'Pegatinas', 150, 'Rare Beauty', 100),
(15, 'Crema', 150, 'Rare Beauty', 100)

-- Tabla 'proveedores'
INSERT INTO PROVEEDORES (Empresa, NombreContacto, Direccion, Ciudad, Estado, CodigoPostal, Email)
VALUES
        ('Samsung', 'Juan Hernandez', 'Calle 20 Col. Los Robles', 'Xalapa', 'Veracruz', 13974, 'juanP@gmail.com'),
        ('Huawei', 'Pedro Lopez', 'Calle Girasol Col. Tor', 'Tlalpan', 'CDMX', 23548, 'Pedro@gmail.com'),
        ('Suavel', 'Maria Cantu', 'Calle Hidalgo Col. San Esteban', 'Alvaro Obregon', 'CDMX', 30249, 'cantu@gmail.com'),
        ('Rare Beauty', 'Selena Gomez', 'Calle 300 Col. Lomas', 'Coyoacan', 'Ciudad de Mexico', 55542, 'sel@gmail.com'),
        ('DELL', 'Carlos Gutierrez', 'Calle Sol, Col. Miramontes', 'Coyoacan', 'Ciudad de Mexico', 24963, 'carlos@gmail.com'),
        ('Touch', 'Susana Perez', 'Calle 6, Col. San Agustin', 'Coyoacan', 'Ciudad de Mexico', 34967, 'sus@hotmail.com'),
        ('Loreal', 'Cristina Hernandez', 'Calle Rojo, Col. Hank', 'Tlahuac', 'Ciudad de Mexico', 29348, 'lol@hotmail.com'),
        ('VestidosCriss', 'Cristian Espinoza', 'Calle Verde, Col. Santa Fe', 'Coyoacan', 'Ciudad de Mexico', 88564, 'criss@yahoo.com'),
        ('kittyCute', 'Maria', 'Calle fe, Col. los pinos', 'Cuautemoc', 'ciudad de Mexico', 11289, 'mar@yahoo.com'),
        ('MaquillajeAnn', 'Ana Berta', 'Calle 1, Col dos', 'Cuautemoc', 'Ciudad de Mexico', 28744, 'ann@gmail.com'),
        ('Aplle', 'Olivia trigo', 'Calle 2, Col. tres', 'Cuautemoc', 'Ciudad de Mexico', 96697, 'trigo@gmail.com'),
        ('LG', 'Laura Gomez', 'Calle 15, Col. Los Pinos', 'Monterrey', 'Nuevo León', 65321, 'laura@gmail.com'),
        ('Sony', 'Carlos Sanchez', 'Calle Estrella, Col. San Rafael', 'Guadalajara', 'Jalisco', 42110, 'carlos@yahoo.com'),
        ('Panasonic', 'Ana Rodriguez', 'Calle Sol, Col. Miraflores', 'Puebla', 'Puebla', 72530, 'ana@gmail.com'),
        ('Toshiba', 'Miguel Torres', 'Avenida del Bosque, Col. Los Alamos', 'Querétaro', 'Querétaro', 34987, 'miguel@gmail.com')

-- Tabla 'pedidos'
INSERT INTO PEDIDOS (Num_Pedido, fechaPedido, Vendedor, Id_producto, Id_cliente, Cantidad, Precio, Total)
VALUES  
        (1, '2021-01-01', 'Juan Hernandez', 1, 1, 2, 5000, 10000),
        (2, '2023-02-02', 'Pedro Lopez', 2, 2, 1, 5000, 5000),
        (3, '2023-02-02', 'Selena Gomez', 8, 10, 50, 200, 10000),
        (4, '2023-02-02', 'Selena Gomez', 8, 1, 20, 200, 4000),
        (5, '2023-02-02', 'Selena Gomez', 8, 6, 10, 200, 2000),
        (6, '2023-02-02', 'Selena Gomez', 8, 13, 12, 200, 2400),
        (7, '2023-02-02', 'Juan Hernandez', 1, 1, 2, 5000, 10000),
        (8, '2023-02-02', 'Pedro Lopez', 2, 8, 1, 5000, 5000),
        (9, '2023-02-02', 'Carlos Gutierrez', 5, 10, 1, 14000, 14000),
        (10, '2023-02-02', 'Carlos Gutierrez', 5, 2, 1, 14000, 14000),
        (11, '2023-02-02', 'Carlos Gutierrez', 5, 3, 1, 14000, 14000),
        (12, '2023-02-02', 'Carlos Gutierrez', 5, 9, 1, 14000, 14000),
        (13, '2023-02-02', 'Carlos Gutierrez', 5, 15, 1, 14000, 14000),
        (14, '2023-02-02', 'Carlos Gutierrez', 5, 6, 1, 14000, 14000),
        (15, '2023-02-02', 'Carlos Gutierrez', 5, 5, 1, 14000, 14000)

-- READ. Realizar las siguientes 6 consultas
-- 1. Obtener los clientes que vivan en Durango
SELECT * FROM CLIENTES WHERE Estado = 'Durango';
-- 2. Obtener los proveedores de que su correo contenga @gmail.com
SELECT * FROM PROVEEDORES WHERE Email LIKE '%@gmail.com';
-- 3. Obtener los productos que su precio sea mayor a 100
SELECT * FROM PRODUCTOS WHERE Precio > 100;
-- 4. Obtener los pedidos que su precio este entre 15 y 50
SELECT * FROM PEDIDOS WHERE Precio BETWEEN 15 AND 50;
-- 5. Obtener los pedidos que su total sea mayor a 200 y su cantidad mayor o igual a 10
SELECT * FROM PEDIDOS WHERE Total > 200 AND Cantidad >= 10;
-- 6. Obtener los proveedores que vivan en la ciudad de Coyoacan y su codigo postal sea mayor a 10000
SELECT * FROM PROVEEDORES WHERE Ciudad = 'Coyoacan';

-- UPDATE. 
--#Actualizaremos 4 datos. Uno por cada tabla
  --  #1. Actualizar el codigo postal del cliente con id 1
  --  #2. Actualizar el precio del producto con id 1
  --  #3. Actualizar ciudad y estado del proveedor con id = 'Selena Gomez'
  --  #4. Actualizar la cantidad del pedido con id 1
UPDATE CLIENTES SET CodigoPostal = 22222 WHERE Id_cliente = 1;
UPDATE PRODUCTOS SET Precio = 7500 WHERE Id_cliente = 1;
UPDATE PROVEEDORES SET Ciudad = 'Villahermosa', Estado = 'Tabasco' WHERE NombreContacto = 'Selena Gomez';
UPDATE PEDIDOS SET Cantidad = 6 WHERE Num_Pedido = 1;

-- DELETE.
--#Eliminaremos los primeros 5 datos de la tabla clientes
DELETE FROM CLIENTES WHERE Id_cliente <= 5;
