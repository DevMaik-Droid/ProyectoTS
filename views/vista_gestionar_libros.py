import tkinter as tk
from  tkinter import ttk

from services.Service_Producto import listar_productos

class V_GestionLibro:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Libro")
        self.ventana.geometry("400x300")
        self.ventana.configure(bg="#FFECB3")  # Fondo naranja claro
        self.init_components()
        
    def init_components(self):
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.ventana, text="Nombre: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_nombre.grid(row=1, column=0)
        self.entrada_nombre = tk.Entry(self.ventana)
        self.entrada_nombre.grid(row=2, column=0)
        
        self.lb_stock = tk.Label(self.ventana, text="Stock: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_stock.grid(row=1, column=1)
        self.entrada_stock = tk.Entry(self.ventana)
        self.entrada_stock.grid(row=2, column=1)
    
        self.lb_precio = tk.Label(self.ventana, text="Precio: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_precio.grid(row=3, column=0)
        self.entrada_precio = tk.Entry(self.ventana)
        self.entrada_precio.grid(row=4, column=0)
        
        # Botón
        self.btn_modificar = tk.Button(self.ventana, text="Modificar", bg="#D35400", fg="white", font=("Arial", 12, "bold"))
        self.btn_modificar.grid(row=5, column=0)
        
        self.btn_eliminar = tk.Button(self.ventana, text="Eliminar", bg="#D35400", fg="white", font=("Arial", 12, "bold"))
        self.btn_eliminar.grid(row=5, column=1)
        
        self.crear_tabla_productos()
        
        
    def crear_tabla_productos(self):
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
        self.tabla_productos.grid(row=6, column=0, columnspan=2)

        list_productos = listar_productos()
        
        for producto in list_productos:
            self.tabla_productos.insert("", tk.END, values=producto)
    
        self.tabla_productos.bind('<ButtonRelease-1>', self.evento_tabla) 
    
    def evento_tabla(self, event):
        self.tabla_productos = event.widget
        item = self.tabla_productos.identify('item', event.x, event.y)
        
        item_values = self.tabla_productos.item(item, "values")
        
        self.id_libro = item_values[0]
        print("id_libro: ", self.id_libro)

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(0, item_values[1])
        
        self.entrada_stock.delete(0, tk.END)
        self.entrada_stock.insert(0, item_values[2])
        
        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(0, item_values[3])