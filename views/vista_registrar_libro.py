import tkinter as tk

class V_RegistrarLibro:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Libro")
        self.ventana.geometry("400x300")
        self.ventana.configure(bg="#FFECB3")  # Fondo naranja claro
        self.init_components()
        
    def init_components(self):
        # Frame para centrar el contenido
        self.frame = tk.Frame(self.ventana, bg="#FFECB3")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.frame, text="Nombre: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_nombre.pack(pady=5)
        self.entrada_nombre = tk.Entry(self.frame)
        self.entrada_nombre.pack(pady=5)
        
        self.lb_stock = tk.Label(self.frame, text="Stock: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_stock.pack(pady=5)
        self.entrada_stock = tk.Entry(self.frame)
        self.entrada_stock.pack(pady=5)
    
        self.lb_precio = tk.Label(self.frame, text="Precio: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_precio.pack(pady=5)
        self.entrada_precio = tk.Entry(self.frame)
        self.entrada_precio.pack(pady=5)
        
        # Botón
        self.btn_registrar = tk.Button(self.frame, text="Registrar", bg="#D35400", fg="white", font=("Arial", 12, "bold"))
        self.btn_registrar.pack(pady=20)
        
