from services.Conexion import conectar, cerrar_conexion
from tkinter import messagebox 
import sqlite3



def agregar_usuario(usuario):
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
        
        id_usuario = resultado[0]
        
        cerrar_conexion(conexion)

        return resultado is not None, id_usuario
    
    except sqlite3.Error as e: 
        print("Error en iniciar sesion: " + e)
    
    return False

def listar_usuarios():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        cerrar_conexion(conexion)
        return usuarios
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN CREAR AL USUARIO", e)
        

def actualizar_usuario(usuario):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET nombre=?, edad=?, ci=?, usuario=?, password=? WHERE id=?"
        cursor.execute(sql,(usuario.get_nombre(),usuario.get_edad(),usuario.get_ci(),usuario.get_usuario(),usuario.get_password(),usuario.get_id()))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("USUARIOS","USUARIO ACTUALIZADO")
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN ACTUALIZAR AL USUARIO", e)
        
def eliminar_usuario(id_usuario):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id=?"
        cursor.execute(sql,(id_usuario))
        conexion.commit()
        cerrar_conexion(conexion)
        messagebox.showinfo("USUARIOS","USUARIO ELIMINADO")
    except sqlite3.Error as e:
        messagebox.showerror("Error","ERROR EN ELIMINAR AL USUARIO", e)