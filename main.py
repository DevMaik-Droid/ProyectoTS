from services.Service_Usuario import agregar_empleado
from models.Usuario import Usuario

def crear_empleado():
    
    user = Usuario()
    user.set_nombre("Pedro Perez")
    user.set_edad(18)
    user.set_ci(111111)
    user.set_usuario("dev1")
    user.set_password("dev1")
    
    print(user.get_nombre())
    agregar_empleado(user)


crear_empleado()    