class Vehiculo(object):
    #matrícula, kilometraje, precio por día,modelo
    disponible=True
    def __init__(self,matricula,kilometraje,precio_dia,modelo):
        self.matricula=matricula
        self.kilometraje=kilometraje
        self.precio_dia=precio_dia
        self.modelo=modelo
    

    def get_matricula(self):
        return self.matricula
    
    def get_kilometraje(self):
        return self.kilometraje

    def get_precio_dia(self):
        return self.precio_dia
    
    def get_modelo(self):
        return self.modelo
    def get_disponible(self):
        return self.disponible


    def set_disponible(self,valor):
        self.disponible=valor
    def set_matricula(self,valor):
        self.matricula=valor

    def set_kilometraje(self,valor):
        self.kilometraje=valor
    def set_precio_dia(self,valor):
        self.precio_dia=valor

