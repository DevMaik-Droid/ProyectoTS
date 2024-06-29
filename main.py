from controllers.usuario_controller import usuario_controller
import tkinter as tk


def main():

    ventana = tk.Tk()
    ventana_main = usuario_controller(ventana)
    ventana.mainloop()
    
main()