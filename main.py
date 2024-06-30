from controllers.usuario_controller import usuario_controller
import tkinter as tk
from services.Conexion import conectar

def main():

    conectar()

    ventana = tk.Tk()
    ventana_main = usuario_controller(ventana)
    ventana.mainloop()
    
main()