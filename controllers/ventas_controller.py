from models.Cliente import Cliente
from models.Venta import Venta
from services.Service_Venta import agregar_venta
from views.vista_ventas import V_Ventas
from services.Service_Cliente import agregar_cliente, listar_clientes

class Ventas_Controller(V_Ventas):
    
    def __init__(self, ventana, id_usuario):
        super().__init__(ventana)
        self.id_usuario = id_usuario
        self.btn_vender.config(command=self.registrar_venta)
        
    
    def registrar_venta(self):
        cliente = Cliente()
        cliente.set_nombre(self.entrada_nombre_cliente.get())
        cliente.set_ci(self.entrada_ci_cliente.get())
        agregar_cliente(cliente)
        
        lista_cliente = listar_clientes()
        id_cliente = 0
        for datos in lista_cliente:
            if datos[2] == self.entrada_ci_cliente.get():
                id_cliente = datos[0]
                break
            
        if id_cliente > 0: 
            venta = Venta()
            venta.set_id_producto(int(self.id_producto))
            venta.set_id_cliente(int(id_cliente))
            venta.set_id_usuario(int(self.id_usuario))
            venta.set_precio_real(float(self.entrada_total.get()))
            agregar_venta(venta)
        
        
        
        