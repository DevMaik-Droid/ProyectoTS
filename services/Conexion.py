import sqlite3

db_name = 'tienda.db'

def conectar():
    conexion = sqlite3.connect(db_name)
    cursor = conexion.cursor()
    cursor.execute(tablaUsuario())
    cursor.execute(tablaProducto())
    cursor.execute()
    return conexion

def tablaUsuario():
    return """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        ci TEXT,
        usuario TEXT,
        password TEXT
    );
    """
    
def tablaProducto():
    return """
    CREATE TABLE IF NOT EXISTS productos (
        idp INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        stock INTEGER,
        precio REAL
    );
    """
    
def tablaCliente():
    return """
    CREATE TABLE IF NOT EXISTS productos (
        idc INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        ci TEXT
    );
    """
def tablaVenta():
    return """
    CREATE TABLE IF NOT EXISTS venta (
        idv INTEGER PRIMARY KEY AUTOINCREMENT,
        idproducto INTEGER,
        idusuario INTEGER,
        idventa 
        ci TEXT
    );
    """

def cerrar_conexion(conexion):
    conexion.close()
