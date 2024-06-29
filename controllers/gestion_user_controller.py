from models.Usuario import Usuario
from views.vista_gestionar_user import V_GestionUsuarios
from tkinter import messagebox
from services.Service_Usuario import agregar_usuario

class GestionUsuarios(V_GestionUsuarios):
    
    
    def __init__(self, ventana):
        super().__init__(ventana)
        self.btn_registrar.config(command=self.registrar_usuario)
        
    
    def registrar_usuario(self):
        usuario = Usuario()
        usuario.set_nombre(self.entrada_nombre.get())
        usuario.set_edad(self.entrada_stock.get())
        usuario.set_ci(self.entrada_ci.get())
        usuario.set_usuario(self.entrada_usuario.get())
        
        if self.entrada_password.get() == self.entrada_confirmar.get():
            usuario.set_password(self.entrada_password.get())
            agregar_usuario(usuario)
            self.ventana.destroy()
        else:
            messagebox.showwarning("Error", "Las contraseñas no coinciden.")