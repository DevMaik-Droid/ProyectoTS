from models.Usuario import Usuario
from views.vista_gestionar_libros import V_GestionLibro
from views.vista_gestionar_user import V_GestionUsuarios
from tkinter import messagebox
from services.Service_Usuario import agregar_usuario

class GestionLibros(V_GestionLibro):
    
    
    def __init__(self, ventana):
        super().__init__(ventana)
        #self.btn_registrar.config(command=self.registrar_usuario)

    def actualizar_libro(self):
        pass