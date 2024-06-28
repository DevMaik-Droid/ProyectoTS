from services.Conexion import conectar, cerrar_conexion
from tkinter import messagebox 
import sqlite3



def agregar_empleado(usuario):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios VALUES (?,?,?,?,?,?)"
        cursor.execute(sql,(None,usuario.get_nombre(),usuario.get_edad(),usuario.get_ci(),usuario.get_usuario(),usuario.get_password()))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("USUARIOS","USUARIO CREADO")
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN CREAR AL USUARIO", e)
        
        
def login(usuario, password):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "SELECT * FROM usuarios WHERE usuario=? AND password=?"
        cursor.execute(sql,(usuario, password))
        resultado = cursor.fetchone()
        
        cerrar_conexion(conexion)

        return resultado is not None
    
    except sqlite3.Error as e: 
        print("Error en iniciar sesion: " + e)
    
    return False