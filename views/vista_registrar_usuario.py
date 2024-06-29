import tkinter as tk

class V_RegistrarUsuario:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registrar Usuario")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="#FFECB3")  # Fondo naranja claro
        self.init_components()
        
    def init_components(self):
        # Frame para centrar el contenido
        self.frame = tk.Frame(self.ventana, bg="#FFECB3")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Etiquetas y widgets de entrada
        self.lb_nombre = tk.Label(self.frame, text="Nombre: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_nombre.grid(row=1,column=0)
        self.entrada_nombre = tk.Entry(self.frame)
        self.entrada_nombre.grid(row=2,column=0)
        
        self.lb_stock = tk.Label(self.frame, text="Edad: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_stock.grid(row=1,column=1)
        self.entrada_stock = tk.Entry(self.frame)
        self.entrada_stock.grid(row=2,column=1)
    
        self.lb_ci = tk.Label(self.frame, text="CI: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_ci.grid(row=1,column=2)
        self.entrada_ci = tk.Entry(self.frame)
        self.entrada_ci.grid(row=2,column=2)
        
        self.lb_usuario = tk.Label(self.frame, text="Usuario: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_usuario.grid(row=3, column=0)
        self.entrada_usuario = tk.Entry(self.frame)
        self.entrada_usuario.grid(row=4, column=0)
        
        self.lb_password = tk.Label(self.frame, text="Password: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_password.grid(row=3,column=1)
        self.entrada_password = tk.Entry(self.frame)
        self.entrada_password.grid(row=4,column=1)
        
        self.lb_confirmar = tk.Label(self.frame, text="Confirmar: ", bg="#FFECB3", fg="#D35400", font=("Arial", 12, "bold"))
        self.lb_confirmar.grid(row=3,column=2)
        self.entrada_confirmar = tk.Entry(self.frame)
        self.entrada_confirmar.grid(row=4,column=2)
        
        # Botón
        self.btn_registrar = tk.Button(self.frame, text="Registrar", bg="#D35400", fg="white", font=("Arial", 12, "bold"))
        self.btn_registrar.grid(row=5,column=1)
        
        
ven = tk.Tk()
vv = V_RegistrarUsuario(ven)
ven.mainloop()