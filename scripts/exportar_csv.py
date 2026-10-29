import sqlite3
import pandas as pd

# Conectarnos a nuestra base de datos
conexion = sqlite3.connect('marketplace.db')

# Lista de nuestras tablas
tablas = ['clientes', 'vendedores', 'productos', 'ordenes']

# Exportar cada tabla a un archivo CSV limpio
for tabla in tablas:
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)
    df.to_csv(f"{tabla}.csv", index=False, encoding='utf-8')
    print(f"Tabla '{tabla}' exportada a {tabla}.csv con éxito.")

conexion.close()