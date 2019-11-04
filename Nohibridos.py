from Vehiculo import Vehiculo

class Nohibridos(Vehiculo):

    def __init__(self,matricula,kilometraje,precio_dia,modelo,aire_acondicionado):
        Vehiculo.__init__(self,matricula,kilometraje,precio_dia,modelo)
        self.aire_acondicionado=aire_acondicionado