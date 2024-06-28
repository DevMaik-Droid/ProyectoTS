import tkinter as tk
from PIL import Image, ImageTk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self["bg"] = parent["bg"]

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=65, **kwargs):
        points = [
            x1 + radius, y1,
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1,
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

class Vista_Login:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("700x500")
        self.ventana.title("Login - Venta de libros")
        
        # Cargar la imagen de fondo
        try:
            self.imagen_fondo = Image.open("images/login.jpg")
            self.imagen_fondo = self.imagen_fondo.resize((700, 500), Image.LANCZOS)
            self.imagen_fondo_tk = ImageTk.PhotoImage(self.imagen_fondo)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.imagen_fondo_tk = None
        
        # Crear el Canvas para el marco redondeado
        self.frame_transparente = RoundedFrame(self.ventana, bg="#2C2C2C")
        self.frame_transparente.place(relx=0.5, rely=0.5, anchor="center", width=700, height=500)
        
        # Colocar la imagen en el marco redondeado si se cargó correctamente
        if self.imagen_fondo_tk:
            self.frame_transparente.create_image(0, 0, image=self.imagen_fondo_tk, anchor="nw")
        
        self.iniciar_componentes()
        
    def iniciar_componentes(self):
        # Crear el rectángulo redondeado
        self.frame_transparente.create_rounded_rectangle(200,100, 500, 400, radius=20, fill="#2C2C2C", outline="")
        
        # Título "Inicio de Sesión"
        titulo = tk.Label(self.frame_transparente, text="Inicio de Sesión", font=("Helvetica", 16), bg="#2C2C2C", fg="#E0E0E0")
        self.frame_transparente.create_window(350, 130, window=titulo, anchor="center")
        
        # Etiqueta de usuario
        lb_usuario = tk.Label(self.frame_transparente, text="Usuario: ", font=("Helvetica", 14),bg="#2C2C2C", fg="#E0E0E0")
        self.frame_transparente.create_window(350, 180, window=lb_usuario, anchor="center")
        
        # Entrada de usuario
        entrada_usuario = tk.Entry(self.frame_transparente, bg="#FFFFFF",font=("Helvetica", 14), fg="#000000")
        self.frame_transparente.create_window(350, 220, window=entrada_usuario, anchor="center")
        
        # Etiqueta de contraseña
        lb_password = tk.Label(self.frame_transparente, text="Contraseña:", font=("Helvetica", 14),bg="#2C2C2C", fg="#E0E0E0")
        self.frame_transparente.create_window(350, 260, window=lb_password, anchor="center")
        
        # Entrada de contraseña
        entrada_password = tk.Entry(self.frame_transparente, show="*", font=("Helvetica", 14),bg="#FFFFFF", fg="#000000")
        self.frame_transparente.create_window(350, 300, window=entrada_password, anchor="center")
        
        # Botón de ingresar
        btn_ingresar = tk.Button(self.frame_transparente, text="Ingresar", font=("Helvetica", 14),bg="#4A4A4A", fg="#FFFFFF", activebackground="#6A6A6A", activeforeground="#FFFFFF")
        self.frame_transparente.create_window(350, 360, window=btn_ingresar, anchor="center")

def main():
    ventana = tk.Tk()
    ventana_p = Vista_Login(ventana)
    ventana.mainloop()

main()
