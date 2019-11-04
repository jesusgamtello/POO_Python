from Vehiculo import Vehiculo
class Hibridos(Vehiculo):
   # duración  de  la  bateríay  si tienencambio  automático
   def __init__(self,matricula,kilometraje,precio_dia,modelo,duracion_bateria,cambio_auto):
        Vehiculo.__init__(self,matricula,kilometraje,precio_dia,modelo)

        self.duracion_bateria=duracion_bateria
        self.cambio_auto=cambio_auto