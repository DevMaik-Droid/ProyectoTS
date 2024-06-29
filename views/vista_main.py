import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.gestion_user_controller import GestionUsuarios
from controllers.producto_controller import Producto_Controller
from controllers.ventas_controller import Ventas_Controller
from controllers.user_controller import Usuario_Controller
from services.Service_Producto import listar_productos

class VentanaPrincipal:
    def __init__(self, root, id_usuario):
        self.root = root
        self.root.title("Software - Control de Venta de Libros")
        self.root.geometry("800x600")
        self.id_usuario = id_usuario
        self.crear_fondo()
        self.crear_menu()
        self.crear_panel_principal()

    def crear_fondo(self):
        # Cargar la imagen de fondo
        self.background_image = Image.open("images/menu.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Crear una etiqueta para mostrar la imagen de fondo
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def crear_menu(self):
        menu = tk.Menu(self.root)

        # Menú Registrar 
        empleados_menu = tk.Menu(menu, tearoff=0)
        empleados_menu.add_command(label="Registrar Usuario", command=self.abrir_subventana_agregar_usuario)
        empleados_menu.add_command(label="Registrar Libro", command=self.ventana_registrar_libro)
        menu.add_cascade(label="Registrar", menu=empleados_menu)

        # Menú Gestionar
        empleados_menu = tk.Menu(menu, tearoff=0)
        empleados_menu.add_command(label="Gestionar Usuario", command=self.ventana_gestion_usuario)
        empleados_menu.add_command(label="Gestionar Libro")
        menu.add_cascade(label="Gestionar", menu=empleados_menu)

        # Menú Reportes
        reportes_menu = tk.Menu(menu, tearoff=0)
        reportes_menu.add_command(label="Generar Reporte de Usuarios", command=self.generar_reporte_empleados)
        reportes_menu.add_command(label="Generar Reporte de Libros", command=self.generar_reporte_empleados)
        reportes_menu.add_command(label="Generar Reporte de Ventas", command=self.generar_reporte_empleados)
        menu.add_cascade(label="Reportes", menu=reportes_menu)

        # Menú Ventas
        ventas_menu = tk.Menu(menu, tearoff=0)
        ventas_menu.add_command(label="Registrar Venta", command=self.abrir_ventana_ventas)
        menu.add_cascade(label="Ventas", menu=ventas_menu)

        # Menú Ayuda
        ayuda_menu = tk.Menu(menu, tearoff=0)
        ayuda_menu.add_command(label="Acerca de HR Software", command=self.mostrar_acerca_de)
        menu.add_cascade(label="Ayuda", menu=ayuda_menu)

        # Menú Salir
        menu.add_command(label="Salir", command=self.salir)

        self.root.config(menu=menu)

    def crear_panel_principal(self):
        panel_principal = tk.Frame(self.root, bg='white')
        panel_principal.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.8)

        self.crear_paneles_informacion(panel_principal)
        self.crear_tabla_ventas(panel_principal)
        
        

    def crear_paneles_informacion(self, parent):
        panel_informacion = tk.Frame(parent, bg='lightgray')
        panel_informacion.pack(fill=tk.X, pady=10)

        total_usuarios = tk.Label(panel_informacion, text="Total de Usuarios: 500", bg='lightgreen', font=('Arial', 12), width=25)
        total_usuarios.pack(side=tk.LEFT, padx=5, pady=5)

        total_empleados = tk.Label(panel_informacion, text="Total de Empleados: 50", bg='lightcoral', font=('Arial', 12), width=25)
        total_empleados.pack(side=tk.LEFT, padx=5, pady=5)

        total_libros = tk.Label(panel_informacion, text="Total de Libros: 1000", bg='lightblue', font=('Arial', 12), width=25)
        total_libros.pack(side=tk.LEFT, padx=5, pady=5)


    def crear_tabla_ventas(self, parent):
        frame_tabla = tk.Frame(parent)
        frame_tabla.pack(fill=tk.BOTH, expand=True, pady=10)

        columnas = ("ID Libro","Libro", "Stock", "Precio")
        self.tabla_ventas = ttk.Treeview(frame_tabla, columns=columnas, show='headings')
        self.tabla_ventas.column("ID Libro",width=20)
        self.tabla_ventas.column("Libro",width=200)
        self.tabla_ventas.column("Stock",width=20)
        self.tabla_ventas.column("Precio",width=20)
        
        self.tabla_ventas.heading("ID Libro", text="ID Libro")
        self.tabla_ventas.heading("Libro", text="Libro")
        self.tabla_ventas.heading("Stock", text="Stock")
        self.tabla_ventas.heading("Precio", text="Precio")
        self.tabla_ventas.pack(fill=tk.BOTH, expand=True)

        list_productos = listar_productos()
        
        for producto in list_productos:
            self.tabla_ventas.insert("", tk.END, values=producto)

    def abrir_subventana_agregar_usuario(self):
        ventana_usuario = Toplevel(self.root)
        Usuario_Controller(ventana_usuario)
        

    def abrir_ventana_ventas(self):
        v_ventas = Toplevel(self.root)
        Ventas_Controller(v_ventas, self.id_usuario)
        
    def ventana_registrar_libro(self):
        ventana_libros = Toplevel(self.root)
        Producto_Controller(ventana_libros)
    
    def ventana_gestion_usuario(self):
        ventana_empleados = Toplevel(self.root)
        GestionUsuarios(ventana_empleados)
        
    def mostrar_ventana_empleados(self):
        ventana_empleados = Toplevel(self.root)
        
        
        

    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de HR Software", "HR Software - Control de Recursos Humanos\nVersión 1.0\nDesarrollado por HR Soft\nhttps://www.hrsoft.com")

    def generar_reporte_empleados(self):
        pass

    def salir(self):
        self.root.quit()