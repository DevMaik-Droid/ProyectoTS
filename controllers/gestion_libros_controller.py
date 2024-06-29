from models.Producto import Producto
from models.Usuario import Usuario
from views.vista_gestionar_libros import V_GestionLibro
from services.Service_Producto import modificar_producto, eliminar_producto

class ControllerGestionLibros(V_GestionLibro):
    
    
    def __init__(self, ventana):
        super().__init__(ventana)
        self.btn_modificar.config(command=self.actualizar_libro)
        self.btn_eliminar.config(command=self.eliminar_libro)

    def actualizar_libro(self):
        producto = Producto()
        producto.set_nombre(self.entrada_nombre.get())
        producto.set_precio(float(self.entrada_precio.get()))
        producto.set_stock(int(self.entrada_stock.get()))
        producto.set_id(self.id_libro)
        
        modificar_producto(producto)
        self.ventana.destroy()
    
    def eliminar_libro(self):
        eliminar_producto(self.id_libro)
        self.ventana.destroy()