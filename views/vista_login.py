import tkinter as tk

class Vista_Login:
    
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("500x300")
        self.ventana.title("Login")
        self.iniciar_componentes()
        
    def iniciar_componentes(self):
        lb_usuario = tk.Label(self.ventana, text="Usuario: ")
        lb_usuario.pack()
        entrada_usuario = tk.Entry(self.ventana)
        entrada_usuario.pack()
        lb_password = tk.Label(self.ventana, text="Contraseña:")
        lb_password.pack()
        entrada_password = tk.Entry(self.ventana)
        entrada_password.pack()
        btn_ingresar = tk.Button(self.ventana, text="Ingresar")
        btn_ingresar.config(bg="#00ff00")
        btn_ingresar.pack()

def main():
    ventana = tk.Tk()
    ventana_p = Vista_Login(ventana)
    ventana.mainloop()

main()


