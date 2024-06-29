import tkinter as tk
from tkinter import ttk

# Supongamos que tenemos una función para listar productos
# Aquí se define una función de ejemplo
def listar_productos():
    return [
        (1, "Libro 1", 10, 50.0),
        (2, "Libro 2", 15, 45.0),
        (3, "Libro 3", 20, 55.0),
        (4, "Libro 4", 8, 60.0),
        (5, "Libro 5", 12, 40.0)
    ]

class V_Ventas:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Venta")
        self.ventana.geometry("728x450")  # Se ha aumentado el ancho de la ventana
        self.ventana.configure(bg="#E5E8E8")  # Fondo gris claro
        self.init_components()

    def init_components(self):
        self.lb_titulo = tk.Label(self.ventana, text="Registro de Venta", bg="#E5E8E8", fg="#2C3E50", font=("Arial", 20, "bold"))
        self.lb_titulo.grid(row=0, column=1, columnspan=6, pady=(20, 10))

        self.lb_nombre_cliente = tk.Label(self.ventana, text="Cliente:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_nombre_cliente.grid(row=1, column=1,padx=10)
        self.entrada_nombre_cliente = tk.Entry(self.ventana)
        self.entrada_nombre_cliente.grid(row=1, column=2, padx=10)
        
        self.lb_ci_cliente = tk.Label(self.ventana, text="Cédula:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_ci_cliente.grid(row=1, column=3, padx=10)
        self.entrada_ci_cliente = tk.Entry(self.ventana)        
        self.entrada_ci_cliente.grid(row=1, column=4, padx=10)
        
        self.lb_nombre_producto = tk.Label(self.ventana, text="Producto:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_nombre_producto.grid(row=2, column=1, padx=10, pady=(10,0))
        self.entrada_nombre_producto = tk.Entry(self.ventana)
        self.entrada_nombre_producto.grid(row=2, column=2, padx=10, pady=(10,0))
        
        self.lb_precio = tk.Label(self.ventana, text="Precio:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_precio.grid(row=2, column=3, padx=10, pady=(10,0))
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.grid(row=2, column=4, padx=10, pady=(10,0))
        
        self.lb_cantidad = tk.Label(self.ventana, text="Cantidad:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_cantidad.grid(row=1, column=5, padx=10, pady=(10,0), sticky='e')  # Alineado a la derecha con respecto a la cédula
        self.entrada_cantidad = tk.Entry(self.ventana, width=10)  # Se reduce el ancho del campo de cantidad
        self.entrada_cantidad.grid(row=1, column=6, padx=10, pady=(10,0))
        
        self.lb_total = tk.Label(self.ventana, text="Total:", bg="#E5E8E8", fg="#2C3E50")
        self.lb_total.grid(row=2, column=5, padx=10, pady=(10,0), sticky='e')  # Alineado a la derecha con respecto al precio
        self.entrada_total = tk.Entry(self.ventana,width=10)
        self.entrada_total.grid(row=2, column=6, padx=10, pady=(10,0))
        
        self.btn_vender = tk.Button(self.ventana, text="Vender", bg="#2C3E50", fg="white", font=("Arial", 12, "bold"))
        self.btn_vender.grid(row=3, column=6, columnspan=2, pady=10, padx=10)

        self.generar_tabla()
        
    def generar_tabla(self):
        columnas = ("ID Libro", "Libro", "Stock", "Precio")
        self.tabla_productos = ttk.Treeview(self.ventana, columns=columnas, show='headings')
        self.tabla_productos.column("ID Libro", width=80)
        self.tabla_productos.column("Libro", width=200)
        self.tabla_productos.column("Stock", width=80)
        self.tabla_productos.column("Precio", width=80)
        
        self.tabla_productos.heading("ID Libro", text="ID Libro")
        self.tabla_productos.heading("Libro", text="Libro")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.grid(row=4, column=1, columnspan=6, sticky='nsew', pady=(10, 20), padx=10)  # Ajuste de la tabla más arriba y un poco más abajo

        list_productos = listar_productos()
        
        for producto in list_productos:
            self.tabla_productos.insert("", tk.END, values=producto)
            
        self.tabla_productos.bind('<ButtonRelease-1>', self.evento_tabla) # Da evento a la tabla productos
            
    def evento_tabla(self, event):
        self.tabla_productos = event.widget
        item = self.tabla_productos.identify('item', event.x, event.y)
        
        item_values = self.tabla_productos.item(item, "values")
        
        self.entrada_nombre_producto.delete(0, tk.END)
        self.entrada_nombre_producto.insert(0, item_values[1])
        
        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(0, item_values[3])
        
        # Supongamos que calculamos el total como precio * cantidad
        if self.entrada_cantidad.get():
            total = float(self.entrada_precio.get()) * float(self.entrada_cantidad.get())
            self.entrada_total.delete(0, tk.END)
            self.entrada_total.insert(0, total)
        else:
            self.entrada_total.delete(0, tk.END)
