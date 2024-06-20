#Practica 2: Biblioteca mysql.connector de python para conectarse a una base de datos de MySQL
#Objetivo: Realizar operaciones CRUD en la base de datos 'ejercicioUno' de MySQL
#Alumn@: Gabriela Lopez Diego
#Curso: Ingenieria de software 2024-1
#Fecha: 16/sep/23
import mysql.connector

def mostrar_menu():
    print("Hola, bienvenido al sistema de ventas")
    print("¿Que desea hacer?")
    print("1. CREATE")
    print("2. READ")
    print("3. UPDATE")
    print("4. DELETE")
    print("5. Salir")

#Funcion que genera 15 registros en cada tabla de la base de datos
def crearRegistros():
    # Crear un cursor
    cursorInsert = conexion.cursor()    
# Consulta SQL para insertar un registro en las tablas correspondientes
    consulta = "INSERT INTO CLIENTES (Id_cliente, Nombre, Domicilio, Ciudad, Estado, CodigoPostal, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    consulta_productos = "INSERT INTO PRODUCTOS (Id_producto, Descripcion, Precio, Marca, Existencia) VALUES (%s, %s, %s, %s, %s)"
    consulta_proveedores = "INSERT INTO PROVEEDORES (Empresa, NombreContacto, Direccion,  Ciudad, Estado, CodigoPostal, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    consulta_pedidos = "INSERT INTO PEDIDOS (Num_pedido, fechaPedido, Vendedor, Id_producto, Id_cliente, Cantidad, Precio, Total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    # Lista de valores de los registros a insertar (15 registros)
    valores_clientes = [
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
        (15, 'Michel', 'Calle Luis Moya, Col. Estrella', 'Chetumal', 'Quintana Roo', 11479, 'cliente15@gmail.com')
    ]
    valores_productos = [
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
    ]

    valores_proveedores = [
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
    ]


    valores_pedidos = [
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
    ]


    # Iterar a través de la lista de valores y ejecutar la consulta para cada registro
    for cliente in valores_clientes:
        cursorInsert.execute(consulta, cliente)
    
    for producto in valores_productos:
        cursorInsert.execute(consulta_productos, producto)
    
    for proveedor in valores_proveedores:
        cursorInsert.execute(consulta_proveedores, proveedor)

    for pedido in valores_pedidos:
        cursorInsert.execute(consulta_pedidos, pedido)
    
    # Hacer commit de los cambios en la base de datos
    conexion.commit()
    # Cerrar el cursor y la conexión
    cursorInsert.close()
    
def leerRegistros():
    #Realizaremos la siguientes consultas
    #1. Obtener todos los clientes que vivan en el estado de Durango
    #2. Obtener todos los proveedores que su correo contenga @gmail.com
    #3. Obtener los productos que tengan un precio mayor a 100
    #4. Obtener los productos que tengan un precio entre 15 y 50
    #5. Obtener los pedidos que su total sea mayor a 200 y su cantidad igual o mayor a 10
    #6. Obtener los proveedores que su ciudad sea Coyoacan

    #Le mostramos al usuario otro menu con las opciones de consulta 1-4
    print("¿Que consulta desea realizar?")
    print("1. Obtener todos los clientes que vivan en el estado de Durango")
    print("2. Obtener todos los proveedores que su correo contenga @gmail.com")
    print("3. Obtener los productos que tengan un precio mayor a 100")
    print("4. Obtener los productos que tengan un precio entre 15 y 50")
    print("5. Obtener los pedidos que su total sea mayor a 200 y su cantidad igual o mayor a 10")
    print("6. Obtener los proveedores que su ciudad sea Coyoacan")
    opcion2 = input("Ingrese una opcion:")
    
    while True:
        if opcion2 == '1':
        #Consulta 1
            cursorSelect1 = conexion.cursor()
            consulta = "SELECT * FROM CLIENTES WHERE Estado = 'Durango'"
            cursorSelect1.execute(consulta)
            resultados1 = cursorSelect1.fetchall()
            print("Clientes que viven en Durango")
    
            for clienteD in resultados1:
                print(clienteD)
            cursorSelect1.close()
            break
        elif opcion2 == '2':
        #Consulta 2
            cursorSelect2 = conexion.cursor()
            consulta = "SELECT * FROM PROVEEDORES WHERE Email LIKE '%@gmail.com'"
            cursorSelect2.execute(consulta)
            resultados2 = cursorSelect2.fetchall()
            print()
            print("Proveedores con correo @gmail.com")
    
            for proveedor in resultados2:
                print(proveedor)
            cursorSelect2.close()
            break
    
        elif opcion2 == '3':
        #Consulta 3
            cursorSelect3 = conexion.cursor()
            consulta = "SELECT * FROM PRODUCTOS WHERE Precio > 100"
            cursorSelect3.execute(consulta)
            resultados3 = cursorSelect3.fetchall()
            print()
            print("Productos con precio mayor a 100")
    
            for producto in resultados3:
                print(producto)
            cursorSelect3.close()
            break
    
        elif opcion2 == '4':
            #Consulta 4
            consultaSelect4 = conexion.cursor()
            consulta = "SELECT * FROM PRODUCTOS WHERE Precio BETWEEN 15 AND 50"
            consultaSelect4.execute(consulta)
            resultados4 = consultaSelect4.fetchall()
            print()
            print("Productos con precio entre 15 y 50")
    
            for producto in resultados4:
                print(producto)
            consultaSelect4.close()
            break
        elif opcion2 == '5':
        #Consulta 5
            consultaSelect5 = conexion.cursor()
            consulta = "SELECT * FROM PEDIDOS WHERE Total > 200 AND Cantidad >= 10" 
            consultaSelect5.execute(consulta)
            resultados5 = consultaSelect5.fetchall()
            print()
            print("Pedidos con total mayor a 200 y cantidad mayor o igual a 10")
    
            for pedido in resultados5:
                print(pedido)
            consultaSelect5.close()
            break
        elif opcion2 == '6':
        #Consulta 6
            consultaSelect6 = conexion.cursor()
            consulta = "SELECT * FROM PROVEEDORES WHERE Ciudad = 'Coyoacan'"
            consultaSelect6.execute(consulta)
            resultados6 = consultaSelect6.fetchall()
            print()
            print("Proveedores que viven en Coyoacan")

            for proveedor in resultados6:
                print(proveedor)
            consultaSelect6.close()
            print()
            break
        else:
            print("Opcion no valida. Intente de nuevo")
            break
        
def actualizarRegistros():
    #Actualizaremos 4 datos. Uno por cada tabla
    #1. Actualizar el codigo postal del cliente con id 1
    #2. Actualizar el precio del producto con id 1
    #3. Actualizar ciudad y estado del proveedor con id = 'Selena Gomez'
    #4. Actualizar la cantidad del pedido con id 1
    
    #Consulta 1
    print()
    print("--->ACTUALIZACION 1. Se actualiza el codigo postal del cliente con id 1")
    #Mostramos el registro antes de ser actualizado
    cursorSelect1 = conexion.cursor()
    consulta_actual = "SELECT * FROM CLIENTES WHERE Id_cliente = 1"
    cursorSelect1.execute(consulta_actual)
    registro_actual = cursorSelect1.fetchone()
    print("Registro ANTES de ser ACTUALIZADO")
    print(registro_actual)    

    #Actualizamos el registro
    cursorUpdate = conexion.cursor()
    consulta = "UPDATE CLIENTES SET CodigoPostal = 22222 WHERE Id_cliente = 1"
    cursorUpdate.execute(consulta)
    
    #Mostramos en pantalla el registro actualizado
    cursorSelect2 = conexion.cursor()
    consulta_modificada = "SELECT * FROM CLIENTES WHERE Id_cliente = 1"
    cursorSelect2.execute(consulta_modificada)
    registro_modificado = cursorSelect2.fetchone()
    print("Registro DESPUES de ser ACTUALIZADO")
    print(registro_modificado)
    
    conexion.commit()
    cursorUpdate.close()
    
    #Consulta 2
    print()
    print("--->ACTUALIZACION 2. Se actualiza el precio del producto con id 1")
    #Mostramos el registro antes de ser actualizado
    cursorSelect3 = conexion.cursor()
    cursorSelect3.execute("SELECT * FROM PRODUCTOS WHERE Id_producto = 1")
    registro_actual = cursorSelect3.fetchone()
    print("Registro ANTES de ser ACTUALIZADO")
    print(registro_actual)
    
    #Actualizamos el registro
    cursorUpdate2 = conexion.cursor()
    consulta = "UPDATE PRODUCTOS SET Precio = 7500 WHERE Id_producto = 1"
    cursorUpdate2.execute(consulta)
    
    #Mostramos en pantalla el registro actualizado
    cursorSelect4 = conexion.cursor()
    cursorSelect4.execute("SELECT * FROM PRODUCTOS WHERE Id_producto = 1")
    registro_modificado = cursorSelect4.fetchone()
    print("Registro DESPUES de ser ACTUALIZADO")
    print(registro_modificado)
        
    conexion.commit()    
    cursorUpdate2.close()
    
    #Actualizacion 3. Se actualiza la ciudad y el estado del proveedor con id = 'Selena Gomez'
    print()
    print("--->ACTUALIZACION 3. Se actualiza la ciudad y el estado del proveedor con id = 'Selena Gomez'")
    cursorSelect5 = conexion.cursor()
    cursorSelect5.execute("SELECT * FROM PROVEEDORES WHERE NombreContacto = 'Selena Gomez'")
    registro_actual = cursorSelect5.fetchone()
    print("Registro ANTES de ser ACTUALIZADO")
    print(registro_actual)
    
    #Actualizamos el registro
    cursorUpdate3 = conexion.cursor()
    consulta = "UPDATE PROVEEDORES SET Ciudad = 'VillaHermosa', Estado = 'Tabasco' WHERE NombreContacto = 'Selena Gomez'"
    cursorUpdate3.execute(consulta)
    
    #Mostramos en pantalla el registro actualizado
    cursorSelect6 = conexion.cursor()
    cursorSelect6.execute("SELECT * FROM PROVEEDORES WHERE NombreContacto = 'Selena Gomez'")
    registro_modificado = cursorSelect6.fetchone()
    print("Registro DESPUES de ser ACTUALIZADO")
    print(registro_modificado)
    
    conexion.commit()
    cursorUpdate3.close()
    
    #Actualizacion 4. Se actualiza la cantidad del pedido con id 1
    print()
    print("--->ACTUALIZACION 4. Se actualiza la cantidad del pedido con Num_pedido 1")
    cursorSelect7 = conexion.cursor()
    cursorSelect7.execute("SELECT * FROM PEDIDOS WHERE Num_Pedido = 1")
    registro_actual = cursorSelect7.fetchone()
    print("Registro ANTES de ser ACTUALIZADO")
    print(registro_actual)
    
    #Actualizamos el registro
    cursorUpdate4 = conexion.cursor()
    consulta = "UPDATE PEDIDOS SET Cantidad = 6 WHERE Num_pedido = 1"
    cursorUpdate4.execute(consulta)

# Mostramos en pantalla el registro actualizado
    cursorSelect8 = conexion.cursor()
    cursorSelect8.execute("SELECT * FROM PEDIDOS WHERE Num_pedido = 1")
    registro_modificado = cursorSelect8.fetchone()
    print("Registro DESPUES de ser ACTUALIZADO")
    print(registro_modificado)

    conexion.commit()
    cursorUpdate4.close()

   # print()
    
#Eliminamos 5 datos de cada tabla 
def eliminarRegistros():
    #Eliminamos el registro con id 1 de cada tabla
    #1. Eliminar un pedido con id 1 
    #2. Eliminar un cliente con id 2
    #3. Eliminar un producto con id 3
    #4. Eliminar un proveedor con id 4
    #5. Eliminar un pedido con id 5
    
    #Mostramos la tabla antes de eliminar los 5 pedidos
    print()
    print("--->ELIMINACION. Se eliminaran 5 pedidos de la tabla PEDIDOS")
    
    cursorSelect1 = conexion.cursor()
    cursorSelect1.execute("SELECT * FROM PEDIDOS")
    registros = cursorSelect1.fetchall()
    print("Tabla ANTES de eliminar los 5 pedidos")
    for registro in registros:
        print(registro)
    
    #Eliminamos los 5 pedidos
    cursorDelete1 = conexion.cursor()
    consulta = "DELETE FROM PEDIDOS WHERE Num_pedido = 1"
    cursorDelete1.execute(consulta)
    consulta = "DELETE FROM PEDIDOS WHERE Num_pedido = 2"
    cursorDelete1.execute(consulta)
    consulta = "DELETE FROM PEDIDOS WHERE Num_pedido = 3"
    cursorDelete1.execute(consulta)
    consulta = "DELETE FROM PEDIDOS WHERE Num_pedido = 4"
    cursorDelete1.execute(consulta)
    consulta = "DELETE FROM PEDIDOS WHERE Num_pedido = 5"
    cursorDelete1.execute(consulta)
    
    #Mostramos la tabla despues de eliminar los 5 pedidos
    cursorSelect2 = conexion.cursor()
    cursorSelect2.execute("SELECT * FROM PEDIDOS")
    registros = cursorSelect2.fetchall()
    print("Tabla DESPUES de eliminar los 5 pedidos")
    for registro in registros:
        print(registro)
    
    conexion.commit()
    cursorDelete1.close()


########################
# Conexión a la base de datos de MySQL
conexion = mysql.connector.connect(
         host='localhost',
         user='root',
         password='123456',
         database='ejercicioUno',
         port = '3306'
)
while True:
    mostrar_menu()
    opcion = input ("Ingrese una oppcion: ")
    if opcion == '1':
        crearRegistros()
        print("Listo, hemos agregado 15 registros a cada tabla (Clientes, Productos, Proveedores, Pedidos))")
    elif opcion == '2':
        leerRegistros()
    elif opcion == '3':
        actualizarRegistros()
    elif opcion == '4':
        eliminarRegistros()
    elif opcion == '5':
        break
    else:
        print("Opcion no valida. Intente de nuevo")
        
# Cerrar la conexión
conexion.close()
