import tkinter as tk
from PIL import Image, ImageTk
class V_RegistrarUsuario:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Usuario")
        self.ventana.geometry("600x400")
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
        self.lb_titulo = tk.Label(self.ventana, text="Registro de Usuario", fg="#225e68", bg="#e6e6e6", font=("Arial", 20, "bold"))
        self.lb_titulo.grid(row=0, column=1, pady=(20, 10), columnspan=3, sticky="w",padx=(200,0))

        # Frame para centrar el contenido
        self.frame = tk.Frame(self.ventana, bg="#e6e6e6")
        self.frame.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
        
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.frame, text="Nombre: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_nombre.grid(row=1,column=0)
        self.entrada_nombre = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_nombre.grid(row=2,column=0,columnspan=2,sticky="nesw",padx=(20,20))
        
        self.lb_stock = tk.Label(self.frame, text="Edad: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_stock.grid(row=3,column=0)
        self.entrada_stock = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_stock.grid(row=4,column=0,padx=(20,20))
    
        self.lb_ci = tk.Label(self.frame, text="CI: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_ci.grid(row=3,column=1)
        self.entrada_ci = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_ci.grid(row=4,column=1,padx=(0,20))
        
        self.lb_usuario = tk.Label(self.frame, text="Usuario: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_usuario.grid(row=5, column=0)
        self.entrada_usuario = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_usuario.grid(row=6, column=0,padx=(20,20))
        
        self.lb_password = tk.Label(self.frame, text="Password: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_password.grid(row=5,column=1)
        self.entrada_password = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_password.grid(row=6,column=1,padx=(0,20))
        
        self.lb_confirmar = tk.Label(self.frame, text="Confirmar: ", bg="#e6e6e6", fg="#225e68", font=("Arial", 12, "bold"))
        self.lb_confirmar.grid(row=7,column=1)
        self.entrada_confirmar = tk.Entry(self.frame,font=("Arial", 12, "bold"))
        self.entrada_confirmar.grid(row=8,column=1,padx=(0,20))
        
        # Botón
        self.btn_registrar = tk.Button(self.frame, text="Registrar", bg="#225e68", fg="white", font=("Arial", 12, "bold"))
        self.btn_registrar.grid(row=9,column=1,pady=(20,5))
        
        
ven = tk.Tk()
vv = V_RegistrarUsuario(ven)
ven.mainloop()