
class Usuario:
    
    def __init__(self, nombre, edad, ci, usuario, password):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
        self.usuario = usuario
        self.password = password
    
    def __init__(self):
        pass
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad
        
    def get_ci(self):
        return self.ci
    
    def set_ci(self, ci):
        self.ci = ci
    
    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password