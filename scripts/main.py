import sqlite3
import sqlite3
import random
from datetime import datetime, timedelta

# 1. Conectar a la base de datos (si no existe, SQLite la crea automáticamente)
conexion = sqlite3.connect('marketplace.db')

# 2. Crear el cursor (es la herramienta que ejecutará los comandos SQL)
cursor = conexion.cursor()

# 3. Crear la tabla 'clientes' usando SQL dentro de Python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY,
        nombre TEXT,
        email TEXT,
        pais TEXT,
        fecha_registro TEXT
    )
''')

# 4. Guardar (commit) los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("¡Base de datos y tabla 'clientes' creadas con éxito!")

# 1. Conectarnos de nuevo a nuestra base de datos
conexion = sqlite3.connect('marketplace.db')
cursor = conexion.cursor()

# 2. Definir datos de ejemplo para simular variedad
paises = ['España', 'México', 'Colombia', 'Argentina', 'Chile']
nombres = ['Ana', 'Carlos', 'Sofía', 'David', 'Lucía', 'Mateo', 'Elena', 'Alejandro', 'Valentina', 'Lucas']
apellidos = ['García', 'Martínez', 'López', 'Rodríguez', 'Pérez', 'González', 'Sánchez', 'Ramírez', 'Torres', 'Flores']

# 3. Generar una lista con 50 clientes simulados
clientes_nuevos = []
fecha_inicio = datetime(2023, 1, 1)

for i in range(1, 51): # Vamos a crear 50 clientes
    nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
    email = f"usuario_{i}@email.com"
    pais = random.choice(paises)
    # Generar una fecha aleatoria en los últimos 700 días
    dias_offset = random.randint(0, 700)
    fecha_reg = (fecha_inicio + timedelta(days=dias_offset)).strftime('%Y-%m-%d')
    
    clientes_nuevos.append((i, nombre_completo, email, pais, fecha_reg))

# 4. Insertar los datos en la tabla 'clientes'
# Usamos OR IGNORE por si volvemos a correr el script, para que no dé error de ID duplicado
cursor.executemany('''
    INSERT OR IGNORE INTO clientes (id_cliente, nombre, email, pais, fecha_registro)
    VALUES (?, ?, ?, ?, ?)
''', clientes_nuevos)

# 5. Guardar cambios y cerrar
conexion.commit()
conexion.close()

print("¡50 clientes insertados con éxito en la base de datos!")

# Conectarnos a la base de datos
conexion = sqlite3.connect('marketplace.db')
cursor = conexion.cursor()

# 1. Crear la tabla 'vendedores'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendedores (
        id_vendedor INTEGER PRIMARY KEY,
        nombre_tienda TEXT,
        ciudad TEXT
    )
''')

# 2. Datos de ejemplo para los vendedores
ciudades_tiendas = ['Madrid', 'CDMX', 'Bogotá', 'Buenos Aires', 'Santiago']
nombres_tiendas_base = ['Tech', 'Hogar', 'Moda', 'Express', 'Global', 'Shop', 'Market', 'Store', 'Direct', 'Outlet']

vendedores_nuevos = []
for i in range(1, 11): # Crearemos 10 vendedores
    nombre_tienda = f"Tienda {random.choice(nombres_tiendas_base)} {i}"
    ciudad = random.choice(ciudades_tiendas)
    vendedores_nuevos.append((i, nombre_tienda, ciudad))

# 3. Insertar los vendedores en la tabla
cursor.executemany('''
    INSERT OR IGNORE INTO vendedores (id_vendedor, nombre_tienda, ciudad)
    VALUES (?, ?, ?)
''', vendedores_nuevos)

# Guardar y cerrar
conexion.commit()
conexion.close()

print("¡Tabla 'vendedores' creada y 10 tiendas insertadas con éxito!")

# Conectarnos a la base de datos
conexion = sqlite3.connect('marketplace.db')
cursor = conexion.cursor()

# 1. Crear la tabla 'productos' con llave foránea
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY,
        nombre_producto TEXT,
        id_vendedor INTEGER,
        categoria TEXT,
        precio REAL,
        FOREIGN KEY (id_vendedor) REFERENCES vendedores (id_vendedor)
    )
''')

# 2. Datos de ejemplo para los productos
categorias = ['Electrónica', 'Hogar', 'Moda', 'Deportes', 'Belleza']
nombres_base = ['Smartphone', 'Cafetera', 'Camisa', 'Mat de Yoga', 'Secador', 'Auriculares', 'Aspiradora', 'Pantalón', 'Mancuernas', 'Perfume']

productos_nuevos = []
for i in range(1, 31): # Crearemos 30 productos
    nombre_prod = f"{random.choice(nombres_base)} {i}"
    id_vendedor = random.randint(1, 10) # Asignado a uno de nuestros 10 vendedores
    categoria = random.choice(categorias)
    precio = round(random.uniform(10.0, 300.0), 2) # Precio aleatorio entre 10 y 300
    
    productos_nuevos.append((i, nombre_prod, id_vendedor, categoria, precio))

# 3. Insertar los productos en la tabla
cursor.executemany('''
    INSERT OR IGNORE INTO productos (id_producto, nombre_producto, id_vendedor, categoria, precio)
    VALUES (?, ?, ?, ?, ?)
''', productos_nuevos)

# Guardar y cerrar
conexion.commit()
conexion.close()

print("¡Tabla 'productos' creada y 30 productos insertados con éxito!")

# Conectarnos a la base de datos
conexion = sqlite3.connect('marketplace.db')
cursor = conexion.cursor()

# 1. Crear la tabla 'ordenes' con llaves foráneas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ordenes (
        id_orden INTEGER PRIMARY KEY,
        id_cliente INTEGER,
        id_producto INTEGER,
        cantidad INTEGER,
        fecha_orden TEXT,
        estado TEXT,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
    )
''')

# 2. Datos de ejemplo para las órdenes
estados = ['Completada', 'Enviada', 'Pendiente', 'Cancelada']
from datetime import datetime, timedelta
fecha_inicio_ordenes = datetime(2024, 1, 1)

ordenes_nuevas = []
for i in range(1, 201): # Crearemos 200 órdenes de compra
    id_cliente = random.randint(1, 50)  # Un cliente entre los 50 que creamos
    id_producto = random.randint(1, 30) # Un producto entre los 30 que creamos
    cantidad = random.choices([1, 2, 3, 4], weights=[70, 20, 7, 3], k=1)[0]
    
    # Fecha aleatoria en el año 2024
    dias_offset = random.randint(0, 360)
    fecha_ord = (fecha_inicio_ordenes + timedelta(days=dias_offset)).strftime('%Y-%m-%d')
    
    estado = random.choices(estados, weights=[75, 15, 5, 5], k=1)[0]
    
    ordenes_nuevas.append((i, id_cliente, id_producto, cantidad, fecha_ord, estado))

# 3. Insertar las órdenes en la tabla
cursor.executemany('''
    INSERT OR IGNORE INTO ordenes (id_orden, id_cliente, id_producto, cantidad, fecha_orden, estado)
    VALUES (?, ?, ?, ?, ?, ?)
''', ordenes_nuevas)

# Guardar cambios y cerrar definitivamente
conexion.commit()
conexion.close()

print("¡Tabla 'ordenes' creada y 200 transacciones insertadas con éxito! Base de datos completa.")