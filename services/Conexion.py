import sqlite3

db_name = 'tienda.db'

def conectar():
    conexion = sqlite3.connect(db_name)
    cursor = conexion.cursor()
    
    # Ejecutar cada tabla de creación individualmente
    for sql in crear_tablas():
        cursor.execute(sql)
    
    cursor.close()

    return conexion

def crear_tablas():
    return [
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            ci TEXT,
            usuario TEXT,
            password TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS productos (
            idp INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            stock INTEGER,
            precio REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS clientes (
            idc INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ci TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ventas (
            idv INTEGER PRIMARY KEY AUTOINCREMENT,
            id_producto INTEGER,
            id_usuario INTEGER,
            id_cliente INTEGER,
            precio_real REAL,
            FOREIGN KEY (id_producto) REFERENCES productos(idp),
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
            FOREIGN KEY (id_cliente) REFERENCES clientes(idc)
        );
        """
    ]

def cerrar_conexion(conexion):
    conexion.close()
