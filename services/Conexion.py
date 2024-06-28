import sqlite3

db_name = 'tienda.db'

def conectar():
    conexion = sqlite3.connect(db_name)
    cursor = conexion.cursor()
    cursor.execute(tablaCliente())
    
    return conexion

def tablaCliente():
    return """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        ci TEXT,
        usuario TEXT,
        password TEXT
    )
    """

def cerrar_conexion(conexion):
    conexion.close()
