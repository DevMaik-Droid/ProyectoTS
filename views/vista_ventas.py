
import tkinter as tk
from tkinter import ttk

from services.Service_Producto import listar_productos

class V_Ventas:
    
    def __init__(self, ventana):

        self.ventana = ventana
        self.ventana.title("Ventas")
        self.ventana.geometry("600x400")
        self.init_components()

    def init_components(self):
        self.lb_titulo = tk.Label(self.ventana, text="Ventas")
        
        
        self.lb_nombre_cliente = tk.Label(self.ventana, text="Cliente")
        self.lb_nombre_cliente.grid(row=0, column=1, pady=(20,0))
        self.entrada_nombre_cliente = tk.Entry(self.ventana)
        self.entrada_nombre_cliente.grid(row=2, column=1)
        
        self.lb_ci_cliente = tk.Label(self.ventana, text="Cedula:")
        self.lb_ci_cliente.grid(row=0,column=2)
        self.entrada_ci_cliente = tk.Entry(self.ventana)        
        self.entrada_ci_cliente.grid(row=2,column=2)
        
        self.lb_nombre_producto = tk.Label(self.ventana, text="Producto")
        self.lb_nombre_producto.grid(row=3, column=1)
        self.entrada_nombre_producto = tk.Entry(self.ventana)
        self.entrada_nombre_producto.grid(row=4, column=1)
        
        self.lb_precio = tk.Label(self.ventana, text="Precio")
        self.lb_precio.grid(row=3, column=2)
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.grid(row=4, column=2)
        
        self.lb_cantidad = tk.Label(self.ventana, text="Cantidad")
        self.lb_cantidad.grid(row=3, column=3)
        self.entrada_cantidad = tk.Entry(self.ventana)
        self.entrada_cantidad.grid(row=4, column=3)
        
        self.lb_total = tk.Label(self.ventana, text="Total")
        self.lb_total.grid(row=3, column=4)
        self.entrada_total = tk.Entry(self.ventana)
        self.entrada_total.grid(row=4, column=4)
        
        
        self.btn_vender = tk.Button(self.ventana, text="Vender")
        self.btn_vender.grid(row=5, column=2)
        self.generar_tabla()
        
    def generar_tabla(self):
        
        columnas = ("ID Libro","Libro", "Stock", "Precio")
        self.tabla_productos = ttk.Treeview(self.ventana, columns=columnas, show='headings')
        self.tabla_productos.column("ID Libro",width=20)
        self.tabla_productos.column("Libro",width=200)
        self.tabla_productos.column("Stock",width=20)
        self.tabla_productos.column("Precio",width=20)
        
        self.tabla_productos.heading("ID Libro", text="ID Libro")
        self.tabla_productos.heading("Libro", text="Libro")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.grid(row=7, column=1, sticky='NSWE')

        list_productos = listar_productos()
        
        for producto in list_productos:
            self.tabla_productos.insert("", tk.END, values=producto)
            
        self.tabla_productos.bind('<ButtonRelease-1>', self.evento_tabla) #Da evento a la tabla productos
            
    def evento_tabla(self, event):
        self.tabla_productos = event.widget
        item = self.tabla_productos.identify('item', event.x, event.y)
        
        item_values = self.tabla_productos.item(item, "values")
        
        self.entrada_nombre_producto.delete(0, tk.END)
        self.entrada_nombre_producto.insert(0, item_values[1])
        
        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(0, item_values[0])
        
        self.id = item_values[0]
