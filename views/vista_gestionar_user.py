import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from services.Service_Usuario import listar_usuarios

class V_GestionUsuarios:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Usuario")
        self.ventana.geometry("750x565")
        self.crear_fondo()
        self.init_components()

    def crear_fondo(self):
        self.background_image = Image.open("images/Regis_Us.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.ventana, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def init_components(self):

        # Configurar el grid para que ocupe toda la ventana
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)

        # Título centrado
        self.lb_titulo = tk.Label(self.ventana, text="Gestion de Usuario", fg="#225e68", bg="#e6e6e6", font=("Arial", 20, "bold"))
        self.lb_titulo.grid(row=0, column=1, pady=(20, 10), columnspan=3, sticky="w",padx=(200,0))

        # Frame para centrar el contenido
        self.frame = tk.Frame(self.ventana, bg="#e6e6e6")
        self.frame.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
        
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.frame, text="Nombre: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_nombre.grid(row=1,column=0)
        self.entrada_nombre = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_nombre.grid(row=2,column=0,columnspan=2,sticky="nesw",padx=(20,20))
        
        self.lb_stock = tk.Label(self.frame, text="Edad: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_stock.grid(row=3,column=0)
        self.entrada_stock = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_stock.grid(row=4,column=0,padx=(20,20))
    
        self.lb_ci = tk.Label(self.frame, text="CI: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_ci.grid(row=3,column=1)
        self.entrada_ci = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_ci.grid(row=4,column=1,padx=(0,20))
        
        self.lb_usuario = tk.Label(self.frame, text="Usuario: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_usuario.grid(row=5, column=0)
        self.entrada_usuario = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_usuario.grid(row=6, column=0,padx=(20,20))
        
        self.lb_password = tk.Label(self.frame, text="Password: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_password.grid(row=5,column=1)
        self.entrada_password = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_password.grid(row=6,column=1,padx=(0,20))
        
        self.lb_confirmar = tk.Label(self.frame, text="Confirmar: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 10, "bold"))
        self.lb_confirmar.grid(row=7,column=1)
        self.entrada_confirmar = tk.Entry(self.frame,font=("Arial", 10, "bold"))
        self.entrada_confirmar.grid(row=8,column=1,padx=(0,20))
        
        # Botón
        self.btn_actualizar = tk.Button(self.frame, text="Actualizar", bg="#225e68", fg="white", font=("Arial", 10, "bold"))
        self.btn_actualizar.grid(row=9,column=0,pady=(20,5))
        
        self.btn_eliminar = tk.Button(self.frame, text="Eliminar", bg="#c60a2e", fg="white", font=("Arial", 10, "bold"))
        self.btn_eliminar.grid(row=9,column=1,pady=(20,5))
        self.generar_tabla()

    def generar_tabla(self):
        columnas = ("ID", "Nombre", "Edad", "CI")
        self.tabla_usuarios = ttk.Treeview(self.frame, columns=columnas, show='headings')
        self.tabla_usuarios.column("ID", width=80)
        self.tabla_usuarios.column("Nombre", width=200)
        self.tabla_usuarios.column("Edad", width=80)
        self.tabla_usuarios.column("CI", width=80)
        
        self.tabla_usuarios.heading("ID", text="ID")
        self.tabla_usuarios.heading("Nombre", text="Nombres")
        self.tabla_usuarios.heading("Edad", text="Edad")
        self.tabla_usuarios.heading("CI", text="CI")
        self.tabla_usuarios.grid(row=10, column=0, columnspan=2, sticky='nsew', pady=(10, 20), padx=10)  

        list_usuarios = listar_usuarios()
        
        for producto in list_usuarios:
            self.tabla_usuarios.insert("", tk.END, values=producto)
            
        self.tabla_usuarios.bind('<ButtonRelease-1>', self.evento_tabla) 