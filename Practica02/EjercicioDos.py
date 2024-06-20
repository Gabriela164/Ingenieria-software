#Practica 2: Biblioteca SQLAlchemy de python para poder acceder a una base de datos en MySQL
#Objetivo: Crear una base de datos con 4 tablas (Clientes, Productos, Proveedores, Pedidos) 
#y realizar operaciones de CRUD (Create, Read, Update, Delete). 
#Alumn@: Gabriela Lopez Diego
#Curso: Ingenieria de software 2024-1
#Fecha: 16/sep/23

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#Creamos las tablas CLIENTES, PRODUCTOS, PROVEEDORES, PEDIDOS
class Cliente(Base):
    __tablename__ = 'CLIENTES'
    Id_cliente = Column(Integer, primary_key=True)
    Nombre = Column(String(50), nullable=False)
    Domicilio = Column(String(60), nullable=False)
    Ciudad = Column(String(20), nullable=False)
    Estado = Column(String(20), nullable=False)
    CodigoPostal = Column(Integer, nullable=False)
    Email = Column(String(30))

class Producto(Base):
    __tablename__ = 'PRODUCTOS'
    Id_producto = Column(Integer, primary_key=True)
    Descripcion = Column(String(80), nullable=False)
    Precio = Column(Integer, nullable=False)
    Marca = Column(String(20))
    Existencia = Column(Integer, nullable=False)
    
class Proveedor(Base):
    __tablename__ = 'PROVEEDORES'
    Empresa = Column(String(20), nullable=False)
    NombreContacto = Column(String(50), primary_key=True)
    Direccion = Column(String(100), nullable=False)
    Ciudad = Column(String(50), nullable=False)
    Estado = Column(String(30), nullable=False)
    CodigoPostal = Column(Integer, nullable=False)
    Email = Column(String(50), nullable=False)

class Pedido(Base):
    __tablename__ = 'PEDIDOS'
    Num_Pedido = Column(Integer, primary_key=True)
    fechaPedido = Column(Date, nullable=False)
    Vendedor = Column(String(50), nullable=False)
    Id_producto = Column(Integer, nullable=False)
    Id_cliente = Column(Integer, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Precio = Column(Integer, nullable=False)
    Total = Column(Integer, nullable=False)


#Creamos la conexion con la base de datos
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/ejercicioDos')

Base.metadata.create_all(engine)

#Creamos una sesion para poder hacer operaciones con la base de datos
Session = sessionmaker(bind=engine)
session = Session()


#Insertamos 15 registros en cada tabla
def crearRegistros():
    #Agregamos 15 registros a la tabla clientes
    session.add_all([
        Cliente(Id_cliente=1, Nombre='Jose Lopez', Domicilio='Calle Girasol', Ciudad='La Paz', Estado='Baja California Sur', CodigoPostal=48292, Email='cliente1@gmail.com'),
        Cliente(Id_cliente=2, Nombre='Ana Maria', Domicilio='Calle Zapata Col. Centro', Ciudad='Tuxtla Gutierrez', Estado='Chiapas', CodigoPostal=29000, Email='cliente2@gmail.com'),
        Cliente(Id_cliente=3, Nombre='Rodrigo', Domicilio='Calle Primavera Col. Libertad', Ciudad='Toluca', Estado='Estado de Mexico', CodigoPostal=93485, Email= 'cliente3@gmail.com'),
        Cliente(Id_cliente=4, Nombre='Alicia',Domicilio='Calle del bosque Col. Santa Cruz',Ciudad='Guadalupe Victoria',Estado='Durando',CodigoPostal=24531,Email='cliente4@gmail.com'),
        Cliente(Id_cliente=5, Nombre='Esteban',Domicilio='Calle Rosa Col. Santa lucia',Ciudad='Durango',Estado='Durango',CodigoPostal=19648,Email='cliente5@gmail.com'),
        Cliente(Id_cliente=6, Nombre='Avril',Domicilio='Calle 20 Col. Los Robles',Ciudad='Xalapa',Estado='Veracurz',CodigoPostal=86885,Email='cliente6@gmail.com'),
        Cliente(Id_cliente=7, Nombre='Elizabeth',Domicilio='Calle Victoria Col. Las lomas',Ciudad='Hermosillo',Estado='Sonora',CodigoPostal=12964,Email='cliente7@gmail.com'),
        Cliente(Id_cliente=8, Nombre='Jazmin',Domicilio='Calle Estrella Col. Alamos',Ciudad='Nogales',Estado='Sonora',CodigoPostal=33697,Email='cliente8@gmail.com'),
        Cliente(Id_cliente=9, Nombre='Sara',Domicilio='Calle Rubi, Col. las lomas',Ciudad='Tapachula',Estado='Chiapas',CodigoPostal=81994,Email='cliente9@gmail.com'),
        Cliente(Id_cliente=10, Nombre='Pablo',Domicilio='Calle Francisco Vila, Col. Santa Fe',Ciudad='Cancun',Estado='Quintana Roo',CodigoPostal=97684,Email='cliente10@gmail.com'),
        Cliente(Id_cliente=11, Nombre='Kevin',Domicilio='Calle Rio Grande Col. La magdalena',Ciudad='Cordoba',Estado='Veracruz',CodigoPostal=30214,Email='cliente11@gmail.com'),
        Cliente(Id_cliente=12, Nombre='Maria',Domicilio='Calle San Vicente Col. San Agustin',Ciudad='Merida',Estado='Yucatan',CodigoPostal=30305,Email='cliente12@gmail.com'),
        Cliente(Id_cliente=13, Nombre='Eduardo',Domicilio='Calle Trigo, Col. Jardines',Ciudad='Ciudad Lerdo',Estado='Durango',CodigoPostal=68691,Email='cliente13@gmail.com'),
        Cliente(Id_cliente=14, Nombre='Joselyn',Domicilio='Calle Montiel, Col. Santa Fe',Ciudad='Villa Hermosa',Estado='Tabasco',CodigoPostal=29370,Email='cliente14@gmail.com'),
        Cliente(Id_cliente=15, Nombre='Elena',Domicilio='Calle Luis Moya, Col. Estrella',Ciudad='Chetumal',Estado='Quintana Roo',CodigoPostal=50503,Email='cliente15@gmail.com'),
    ])
    
    #Agregar 15 registros a la tabla productos
    session.add_all([
        Producto(Id_producto=1, Descripcion='Laptop', Precio=15000, Marca='HP', Existencia=10),
        Producto(Id_producto=2, Descripcion='Television', Precio=20000, Marca='LG', Existencia=0),
        Producto(Id_producto=3, Descripcion='Celular', Precio=10000, Marca='Samsung', Existencia=20),
        Producto(Id_producto=4, Descripcion='Tablet', Precio=8000, Marca='Lenovo', Existencia=25),
        Producto(Id_producto=5, Descripcion='Audifonos', Precio=2000, Marca='Sony', Existencia=30),
        Producto(Id_producto=6, Descripcion='Mouse', Precio=500, Marca='Logitech', Existencia=35),
        Producto(Id_producto=7, Descripcion='Teclado', Precio=1000, Marca='Genius', Existencia=0),
        Producto(Id_producto=8, Descripcion='Bocinas', Precio=1500, Marca='JBL', Existencia=45),
        Producto(Id_producto=9, Descripcion='Impresora', Precio=3000, Marca='Epson', Existencia=50),
        Producto(Id_producto=10, Descripcion='Laptop', Precio=15000, Marca='Dell', Existencia=0),
        Producto(Id_producto=11, Descripcion='Television', Precio=20000, Marca='LG', Existencia=15),
        Producto(Id_producto=12, Descripcion='Celular', Precio=10000, Marca='Samsung', Existencia=0),
        Producto(Id_producto=13, Descripcion='Tablet', Precio=8000, Marca='Lenovo', Existencia=25),
        Producto(Id_producto=14, Descripcion='Audifonos', Precio=2000, Marca='Sony', Existencia=30),
        Producto(Id_producto=15, Descripcion='Mouse', Precio=500, Marca='Logitech', Existencia=35),
    ])   
    
    #Agregar 15 registros a la tabla proveedores
    session.add_all([
        Proveedor(Empresa='HP', NombreContacto='Juan Perez', Direccion='Calle 20 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=12345, Email = 'proveedor1@correo.com'),
        Proveedor(Empresa='LG', NombreContacto='Maria Lopez', Direccion='Calle 30 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=12345, Email = 'proveedor2@correo.com'),
        Proveedor(Empresa='Samsung', NombreContacto='Pedro Sanchez', Direccion='Calle 40 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=13795, Email = 'proveedor3@correo.com'),
        Proveedor(Empresa='Lenovo', NombreContacto='Ana Maria', Direccion='Calle 50 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=33694, Email = 'proveedor4@gmail.com'),
        Proveedor(Empresa='Sony', NombreContacto='Jose Lopez', Direccion='Calle 60 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=23236, Email = 'proveedor5@gmail.com'),
        Proveedor(Empresa='Logitech', NombreContacto='Ricardo Perez', Direccion='Calle 70 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=12345, Email = 'proveedor6@gmail.com'),
        Proveedor(Empresa='Genius', NombreContacto='Luisa Lopez', Direccion='Calle 80 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=20261, Email = 'proveedor7@gmail.com'),
        Proveedor(Empresa='JBL', NombreContacto='Ricardo Trujillo', Direccion='Calle 90 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=30621, Email = 'proveedor8@gmail.com'),
        Proveedor(Empresa='Epson', NombreContacto='Teresa Martinez', Direccion='Calle 100 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=29786,Email = 'proveedor9@correo.com'),
        Proveedor(Empresa='HP', NombreContacto='Adriana Robles', Direccion='Calle 200 Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=78785, Email = 'proveedor10@gmail.com'),
        Proveedor(Empresa='Suavel', NombreContacto='Cristian Cantu', Direccion='Calle 5 de Mayo Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=31975, Email = 'proveedor11@correo.com'),
        Proveedor(Empresa='Coca Cola', NombreContacto='Karla Mendez', Direccion='Calle Primavera Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=71896, Email = 'proveedor12@gmail.com'),
        Proveedor(Empresa='Pepsi', NombreContacto='Laura Hernandez', Direccion='Calle 20 de Noviembre Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=87896, Email = 'proveedor13@correo.com'),
        Proveedor(Empresa='Sabritas', NombreContacto='Ana Paula', Direccion='Calle 5 de Febrero Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=37868, Email = 'proveedor14@correo.com'),
        Proveedor(Empresa='Dell', NombreContacto='Susana Perez', Direccion='Calle 16 de Septiembre Col. Centro', Ciudad='Mexico', Estado='CDMX', CodigoPostal=56584, Email = 'proveedor5@correo.com'),
    ])
    
    #Agregar 15 registros a la tabla pedidos
    session.add_all([
        Pedido(Num_Pedido=1, fechaPedido='2023-04-23', Vendedor='Juan Perez', Id_producto=1, Id_cliente=1, Cantidad=1, Precio=15000, Total=15000),
        Pedido(Num_Pedido=2, fechaPedido='2023-06-12', Vendedor='Juan Perez', Id_producto=1, Id_cliente=4, Cantidad=1, Precio=15000, Total=15000),
        Pedido(Num_Pedido=3, fechaPedido='2023-06-10', Vendedor='Teresa Martinez', Id_producto=9, Id_cliente=6, Cantidad=1, Precio=3000, Total=3000),
        Pedido(Num_Pedido=4, fechaPedido='2023-03-28', Vendedor='Teresa Martinez', Id_producto=9, Id_cliente=7, Cantidad=1, Precio=3000, Total=3000),
        Pedido(Num_Pedido=5, fechaPedido='2023-01-25', Vendedor='Jose Lopez', Id_producto=5, Id_cliente=13, Cantidad=1, Precio=2000, Total=2000),
        Pedido(Num_Pedido=6, fechaPedido='2023-04-01', Vendedor='Jose Lopez', Id_producto=5, Id_cliente=15, Cantidad=1, Precio=2000, Total=2000),
        Pedido(Num_Pedido=7, fechaPedido='2023-07-01', Vendedor='Ana Maria', Id_producto=4, Id_cliente=14, Cantidad=1, Precio=8000, Total=8000),
        Pedido(Num_Pedido=8, fechaPedido='2023-11-01', Vendedor='Ana Maria', Id_producto=4, Id_cliente=7, Cantidad=1, Precio=8000, Total=8000),
        Pedido(Num_Pedido=9, fechaPedido='2023-03-15', Vendedor='Susana Perez', Id_producto=10, Id_cliente=1, Cantidad=1, Precio=15000, Total=15000),
        Pedido(Num_Pedido=10, fechaPedido='2023-01-01', Vendedor='Susana Perez', Id_producto=10, Id_cliente=4, Cantidad=1, Precio=15000, Total=15000),
        Pedido(Num_Pedido=11, fechaPedido='2023-02-25', Vendedor='Maria Lopez', Id_producto=2, Id_cliente=8, Cantidad=1, Precio=20000, Total=20000),
        Pedido(Num_Pedido=12, fechaPedido='2023-12-20', Vendedor='Maria Lopez', Id_producto=2, Id_cliente=9, Cantidad=1, Precio=20000, Total=20000),
        Pedido(Num_Pedido=13, fechaPedido='2023-11-14', Vendedor='Ricardo Perez', Id_producto=7, Id_cliente=2, Cantidad=1, Precio=1000, Total=1000),
        Pedido(Num_Pedido=14, fechaPedido='2023-03-13', Vendedor='Ricardo Perez', Id_producto=7, Id_cliente=5, Cantidad=3, Precio=1000, Total=3000),
        Pedido(Num_Pedido=15, fechaPedido='2023-12-01', Vendedor='Ricardo Perez', Id_producto=7, Id_cliente=3, Cantidad=1, Precio=1000, Total=1000),
    ])                
    session.commit()
    
def leerRegistros():
    #Creamos un subMenu
    print("¿Que consulta desea realizar?")
    print("1. Buscar a los clientes que empiecen su nombre con la letra E")
    print("2. Buscar los proveedores que su correo contenga al menos una a")
    print("3. Buscar los productos que tenga en existencia(mayor a o igual a 1)")
    print("4. Buscar los productos que la marca empiece con la letra D")
    print("5. Buscar los pedidos donde su fecha sea entre 2023-01-24 al 2023-04-24")
    print("6. Buscar los proveedores que se apelliden Perez")
    opcion2 = input("Ingrese una opcion:")
    
    while True:
        if opcion2 == '1':
            #Buscar a los clientes que empiecen su nombre con la letra E
            print()
            print("Clientes con nombre que empiezan con la letra E")
            clientes_con_E = session.query(Cliente).filter(Cliente.Nombre.startswith('E')).all()
            # Imprime los resultados
            for cliente in clientes_con_E:
                print(f'Id_cliente: {cliente.Id_cliente}, Nombre: {cliente.Nombre}')
            break
        elif opcion2 == '2':
            print()
            print("Proveedores que tienen una al menos una a en su correo")
            proveedores_con_a = session.query(Proveedor).filter(Proveedor.Email.like('%a%')).all()
            # Imprime los resultados
            for proveedor in proveedores_con_a:
                print(f'Id_proveedor: {proveedor.NombreContacto}, Email: {proveedor.Email}')
            break
        elif opcion2 == '3':
            print("")
            print("Productos en existencia")
            productos_en_existencia = session.query(Producto).filter(Producto.Existencia >=1).all()
            # Imprime los resultados
            for producto in productos_en_existencia:
                print(f'Id_producto: {producto.Id_producto}, Descripcion: {producto.Descripcion}, Existencia: {producto.Existencia}')
            break
        elif opcion2 == '4':
            print()
            print("Buscar los productos con marca que empiecen con la letra D")
            productos_D = session.query(Producto).filter(Producto.Marca.startswith('D')).all()
            # Imprime los resultados
            for producto in productos_D:
                print(f'Id_producto: {producto.Id_producto}, Descripcion: {producto.Descripcion}, Marca: {producto.Marca}')
            break
        elif opcion2 == '5':
            print()
            print("Pedidos con fecha 2023-01-24 al 2023-04-24")
            pedidos_fecha = session.query(Pedido).filter(Pedido.fechaPedido.between('2023-01-24','2023-04-24')).all()
            # Imprime los resultados
            for pedido in pedidos_fecha:
                print(f'Num_Pedido: {pedido.Num_Pedido}, fechaPedido: {pedido.fechaPedido}')
            break
        elif opcion2 == '6':
            print()
            print("Proveedores que se apellidan Perez")
            proveedores_perez = session.query(Proveedor).filter(Proveedor.NombreContacto.like('%Perez%')).all()
            # Imprime los resultados
            for proveedor in proveedores_perez:
                print(f'NombreContacto: {proveedor.NombreContacto}, Empresa: {proveedor.Empresa}')
            break
        else:
            print("Opcion no valida. Intente de nuevo")
            break

def actualizarRegistros():
    #Se actualizan 4 datos. 1 dato por cada tabla. 
    #Se muestra en terminal los datos antes y despues de actualizar.
    #1. Actualizamos la ciudad y el estado del cliente con id 2
    #2. Actualizamos la cantidad en existencia del producto con id 5
    #3. Actualizamos la empresa del proveedor con nombre de contacto Juan Perez
    #4. Actualizamos la fecha de pedido del pedido con numero de pedido 8
    
    #1. 
    print()
    print("ACTUALIZACION 1-> Actualizamos la ciudad y el estado del cliente con id 2")
    print("Datos del cliente ANTES de actualizar")
    cliente = session.query(Cliente).filter(Cliente.Id_cliente == 2).first()
    print(f'Id_cliente: {cliente.Id_cliente}, Nombre: {cliente.Nombre}, Ciudad: {cliente.Ciudad}, Estado: {cliente.Estado}')
    #Actualizamos la ciudad y el estado del cliente con id 2
    session.query(Cliente).filter(Cliente.Id_cliente == 2).update({'Ciudad': 'Guadalajara', 'Estado': 'Jalisco'})
    session.commit()
    print("Datos del cliente DESPUES de actualizar")
    cliente = session.query(Cliente).filter(Cliente.Id_cliente == 2).first()
    print(f'Id_cliente: {cliente.Id_cliente}, Nombre: {cliente.Nombre}, Ciudad: {cliente.Ciudad}, Estado: {cliente.Estado}')
    
    #2 
    print()
    print("ACTUALIZACION 2-> Actualizamos la cantidad en existencia del producto con id 5")
    print("Datos del producto ANTES de actualizar")
    producto = session.query(Producto).filter(Producto.Id_producto == 5).first()
    print(f'Id_producto: {producto.Id_producto}, Descripcion: {producto.Descripcion}, Existencia: {producto.Existencia}')
    #Actualizamos la cantidad en existencia del producto con id 5
    session.query(Producto).filter(Producto.Id_producto == 5).update({'Existencia': 210})
    session.commit()
    print("Datos del producto DESPUES de actualizar")
    producto = session.query(Producto).filter(Producto.Id_producto == 5).first()
    print(f'Id_producto: {producto.Id_producto}, Descripcion: {producto.Descripcion}, Existencia: {producto.Existencia}')
        
    #3
    print()
    print("ACTUALIZACION 3-> Actualizamos la empresa del proveedor con nombre de contacto Juan Perez")
    print("Datos del proveedor ANTES de actualizar")
    proveedor = session.query(Proveedor).filter(Proveedor.NombreContacto == 'Juan Perez').first()
    print(f'NombreContacto: {proveedor.NombreContacto}, Empresa: {proveedor.Empresa}')
    #Actualizamos la empresa del proveedor con nombre de contacto Juan Perez
    session.query(Proveedor).filter(Proveedor.NombreContacto == 'Juan Perez').update({'Empresa': 'Apple'})
    session.commit()
    print("Datos del proveedor DESPUES de actualizar")
    proveedor = session.query(Proveedor).filter(Proveedor.NombreContacto == 'Juan Perez').first()
    print(f'NombreContacto: {proveedor.NombreContacto}, Empresa: {proveedor.Empresa}')
    
    #4
    print()
    print("ACTUALIZACION 4-> Actualizamos la fecha de pedido del pedido con numero de pedido 8")
    print("Datos del pedido ANTES de actualizar")
    pedido = session.query(Pedido).filter(Pedido.Num_Pedido == 8).first()
    print(f'Num_Pedido: {pedido.Num_Pedido}, fechaPedido: {pedido.fechaPedido}')
    #Actualizamos la fecha de pedido del pedido con numero de pedido 8
    session.query(Pedido).filter(Pedido.Num_Pedido == 8).update({'fechaPedido': '2023-12-25'})
    session.commit()
    print("Datos del pedido DESPUES de actualizar")
    pedido = session.query(Pedido).filter(Pedido.Num_Pedido == 8).first()
    print(f'Num_Pedido: {pedido.Num_Pedido}, fechaPedido: {pedido.fechaPedido}')
    
    
def eliminarRegistros():
    #Se eliminan los primeros 5 registros de la tabla CLIENTES
    #Mostramos la tabla CLIENTES antes de eliminar los registros
    print()
    print("Tabla CLIENTES ANTES de eliminar los registros")
    clientes = session.query(Cliente).all()
    # Imprime los resultados
    for cliente in clientes:
        print(f'Id_cliente: {cliente.Id_cliente}, Nombre: {cliente.Nombre}')
    
    #Eliminamos los primeros 5 registros de la tabla CLIENTES
    session.query(Cliente).filter(Cliente.Id_cliente <= 5).delete()
    session.commit()
    
    #Mostramos la tabla CLIENTES despues de eliminar los registros
    print()
    print("Tabla CLIENTES DESPUES de eliminar los registros")
    clientes = session.query(Cliente).all()
    # Imprime los resultados    
    for cliente in clientes:
        print(f'Id_cliente: {cliente.Id_cliente}, Nombre:{cliente.Nombre}')
    
def mostrar_menu():
    print()
    print("Hola, bienvenido al sistema de ventas")
    print("¿Que desea hacer?")
    print("1. CREATE")
    print("2. READ")
    print("3. UPDATE")
    print("4. DELETE")
    print("5. Salir")
    
while True:
    mostrar_menu()
    opcion = input ("Ingrese una opcion: ")
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
    
#Cerramos la sesion
session.close()