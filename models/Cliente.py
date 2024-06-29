class Cliente:
    
    
    
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci
        self.id = None
    
    def __init__(self):
        pass
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_ci(self):
        return self.ci
    
    def set_ci(self, ci):
        self.ci = ci
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id