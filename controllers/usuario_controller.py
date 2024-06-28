from services.Service_Usuario import agregar_empleado, login
from models.Usuario import Usuario
from views.vista_login import Vista_Login
from tkinter import messagebox
class usuario_controller(Vista_Login):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.btn_ingresar.config(command=self.iniciar_sesion)


    def crear_empleado(self):
        
        
        user = Usuario()
        user.set_nombre("Pedro Perez")
        user.set_edad(18)
        user.set_ci(111111)
        user.set_usuario("dev1")
        user.set_password("dev1")
        
        print(user.get_nombre())
        agregar_empleado(user)
        
    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        password = self.entrada_password.get()
        
        if login(usuario, password):
            messagebox.showinfo("FFF", "inicio correcto")
        else:
            messagebox.showwarning("Iniciar sesion", "Datos incorrectos")
            
        
        
        
        
