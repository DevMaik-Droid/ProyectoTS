from tkinter import messagebox
from services.Conexion import conectar, cerrar_conexion
import sqlite3



def agregar_cliente(cliente):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes VALUES (?,?,?)"
        cursor.execute(sql,(None,cliente.get_nombre(),cliente.get_ci()))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("CLIENTE","CLIENTE CREADO")
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN CREAR AL cliente", e)
        
def listar_clientes():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        productos = cursor.fetchall()
        cerrar_conexion(conexion)
        return productos
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN LISTAR CLIENTES", e)