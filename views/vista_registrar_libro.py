import tkinter as tk
from PIL import Image, ImageTk
class V_RegistrarLibro:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Libro")
        self.ventana.geometry("250x300")
        self.crear_fondo()
        self.init_components()

    def crear_fondo(self):
        self.background_image = Image.open("images/registrarL.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self.ventana, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def init_components(self):
  
        # Frame para centrar el contenido
        self.frame = tk.Frame(self.ventana, bg="#141923")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.frame, text="Nombre: ", bg="#141923", fg="#9d6342", font=("Arial", 12, "bold"))
        self.lb_nombre.pack(pady=5)
        self.entrada_nombre = tk.Entry(self.frame)
        self.entrada_nombre.pack(pady=5)
        
        self.lb_stock = tk.Label(self.frame, text="Stock: ", bg="#141923", fg="#9d6342", font=("Arial", 12, "bold"))
        self.lb_stock.pack(pady=5)
        self.entrada_stock = tk.Entry(self.frame)
        self.entrada_stock.pack(pady=5)
    
        self.lb_precio = tk.Label(self.frame, text="Precio: ", bg="#141923", fg="#9d6342", font=("Arial", 12, "bold"))
        self.lb_precio.pack(pady=5)
        self.entrada_precio = tk.Entry(self.frame)
        self.entrada_precio.pack(pady=5)
        
        # Botón
        self.btn_registrar = tk.Button(self.frame, text="Registrar", bg="#D35400", fg="white", font=("Arial", 12, "bold"))
        self.btn_registrar.pack(pady=20)
        
