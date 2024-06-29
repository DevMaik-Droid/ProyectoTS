from tkinter import messagebox
from services.Conexion import conectar, cerrar_conexion
import sqlite3



def agregar_venta(venta):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO ventas VALUES (?,?,?,?,?)"
        cursor.execute(sql,(None,venta.get_id_producto(),venta.get_id_usuario(),venta.get_id_cliente(),venta.get_precio_real()))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("CLIENTE","Venta CREADa")
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