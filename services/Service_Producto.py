from tkinter import messagebox
from services.Conexion import conectar, cerrar_conexion
import sqlite3



def agregar_producto(producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO productos VALUES (?,?,?,?)"
        cursor.execute(sql,(None,producto.get_nombre(),producto.get_stock(),producto.get_precio()))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("PRODUCTO","PRODUCTO CREADO")
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN CREAR AL Producto", e)