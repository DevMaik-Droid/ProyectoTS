import tkinter as tk

class V_RegistrarLibro:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Libro")
        self.ventana.geometry("400x300")
        self.init_components()
        
    
    def init_components(self):
        self.lb_nombre = tk.Label(self.ventana, text="Nombre: ")
        self.lb_nombre.pack()
        self.entrada_nombre = tk.Entry(self.ventana)
        self.entrada_nombre.pack()
        
        self.lb_stock = tk.Label(self.ventana, text="Stock: ")
        self.lb_stock.pack()
        self.entrada_stock = tk.Entry(self.ventana)
        self.entrada_stock.pack()
    
        self.lb_precio = tk.Label(self.ventana, text="Precio: ")
        self.lb_precio.pack()
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.pack()
        
        self.btn_registrar = tk.Button(self.ventana, text="Registrar")
        self.btn_registrar.pack()