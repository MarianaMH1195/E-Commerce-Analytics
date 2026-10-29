import sqlite3

# Conectarnos a nuestra base de datos existente
conexion = sqlite3.connect('marketplace.db')
cursor = conexion.cursor()

# Consulta SQL: Unir órdenes, clientes y productos
consulta = '''
    SELECT 
        o.id_orden,
        c.nombre AS cliente,
        p.nombre_producto,
        o.cantidad,
        p.precio,
        (o.cantidad * p.precio) AS total_venta,
        o.fecha_orden,
        o.estado
    FROM ordenes o
    JOIN clientes c ON o.id_cliente = c.id_cliente
    JOIN productos p ON o.id_producto = p.id_producto
    LIMIT 5;
'''

cursor.execute(consulta)
resultados = cursor.fetchall()

print("--- LAS PRIMERAS 5 VENTAS DE TU MARKETPLACE ---")
for fila in resultados:
    print(fila)

conexion.close()