class Producto:
    
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.id = None
    def __init__(self):
        pass
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id