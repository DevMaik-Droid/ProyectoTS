import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from services.Service_Producto import listar_productos

class V_Ventas:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Venta")
        self.ventana.geometry("750x500") 
        self.crear_fondo()
        self.init_components()

    def crear_fondo(self):
        self.background_image = Image.open("images/fondo_ventas.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.ventana, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def init_components(self):
        self.lb_titulo = tk.Label(self.ventana, text="Registro de Venta", fg="white",bg = "#0f0700", font=("Arial", 20, "bold"))
        self.lb_titulo.grid(row=0, column=1, pady=(20, 10))

        self.lb_nombre_cliente = tk.Label(self.ventana, text="Cliente:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_nombre_cliente.grid(row=1, column=0,padx=(10,0))
        self.entrada_nombre_cliente = tk.Entry(self.ventana)
        self.entrada_nombre_cliente.grid(row=2, column=0, padx=(10,0))
        
        self.lb_ci_cliente = tk.Label(self.ventana, text="Cédula:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_ci_cliente.grid(row=1, column=1, padx=10)
        self.entrada_ci_cliente = tk.Entry(self.ventana)        
        self.entrada_ci_cliente.grid(row=2, column=1, padx=10)
        
        self.lb_nombre_producto = tk.Label(self.ventana, text="Producto:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_nombre_producto.grid(row=3, column=0, padx=(10,0), pady=(10,0))
        self.entrada_nombre_producto = tk.Entry(self.ventana)
        self.entrada_nombre_producto.grid(row=4, column=0, padx=(10,0), pady=(10,0))
        
        self.lb_precio = tk.Label(self.ventana, text="Precio:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_precio.grid(row=3, column=1, padx=10, pady=(10,0))
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.grid(row=4, column=1, padx=10, pady=(10,0))
        
        self.lb_total = tk.Label(self.ventana, text="Total:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_total.grid(row=3, column=2, padx=10, pady=(10,0))  
        self.entrada_total = tk.Entry(self.ventana)
        self.entrada_total.grid(row=4, column=2, padx=10, pady=(10,0))
        
        self.lb_cantidad = tk.Label(self.ventana, text="Cantidad:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_cantidad.grid(row=1, column=2, padx=10, pady=(10,0))  
        self.entrada_cantidad = tk.Entry(self.ventana) 
        self.entrada_cantidad.grid(row=2, column=2, padx=10, pady=(10,0))

        self.btn_vender = tk.Button(self.ventana, text="Vender", fg="white",bg = "#74512D",font=("Arial", 12, "bold"))
        self.btn_vender.grid(row=5, column=1, pady=10, padx=10)

        self.lb_clientes = tk.Label(self.ventana, text="Clientes:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_clientes.grid(row=6, column=0)
        
        self.lb_productos = tk.Label(self.ventana, text="Productos:", fg="white",bg = "#0f0700",font=("Arial", 12, "bold"))
        self.lb_productos.grid(row=6, column=1, sticky='w', padx=10)
        
        self.generar_tabla()
        self.generar_tabla_cliente()
        
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
        self.tabla_productos.grid(row=7, column=1, columnspan=2, sticky='nsew', pady=(10, 20), padx=10)  

        list_productos = listar_productos()
        
        for producto in list_productos:
            self.tabla_productos.insert("", tk.END, values=producto)
            
        self.tabla_productos.bind('<ButtonRelease-1>', self.evento_tabla) 
    
    def generar_tabla_cliente(self):
        columnas = ("ID Cliente", "Cliente", "CI")
        self.tabla_cliente = ttk.Treeview(self.ventana, columns=columnas, show='headings')
        self.tabla_cliente.column("ID Cliente", width=30)
        self.tabla_cliente.column("Cliente", width=100)
        self.tabla_cliente.column("CI", width=60)
        
        self.tabla_cliente.heading("ID Cliente", text="ID Cliente")
        self.tabla_cliente.heading("Cliente", text="Cliente")
        self.tabla_cliente.heading("CI", text="CI")
        self.tabla_cliente.grid(row=7, column=0, columnspan=1, sticky='nsew', pady=(10, 20), padx=10) 
    

    def evento_tabla(self, event):
        self.tabla_productos = event.widget
        item = self.tabla_productos.identify('item', event.x, event.y)
        
        item_values = self.tabla_productos.item(item, "values")
        self.id_producto = item_values[0]
        
        self.entrada_nombre_producto.delete(0, tk.END)
        self.entrada_nombre_producto.insert(0, item_values[1])
        
        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(0, item_values[3])
        
        """
        # Supongamos que calculamos el total como precio * cantidad
        if self.entrada_cantidad.get():
            total = float(self.entrada_precio.get()) * float(self.entrada_cantidad.get())
            self.entrada_total.delete(0, tk.END)
            self.entrada_total.insert(0, total)
        else:
            self.entrada_total.delete(0, tk.END)"""
