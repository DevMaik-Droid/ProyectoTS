from views.vista_registrar_libro import V_RegistrarLibro
from services.Service_Producto import agregar_producto
from models.Producto import Producto

class Producto_Controller(V_RegistrarLibro):
    
    def __init__(self, ventana):
        super().__init__(ventana)
        self.btn_registrar.config(command=self.registrar_producto)
        
    def registrar_producto(self):
        producto = Producto()
        producto.set_nombre(self.entrada_nombre.get())
        producto.set_precio(float(self.entrada_precio.get()))
        producto.set_stock(int(self.entrada_stock.get()))
        agregar_producto(producto)
        self.ventana.destroy()
        
        