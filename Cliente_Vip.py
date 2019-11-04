from Cliente import Cliente

class Vip(Cliente):

    def __init__(self,NIF,nombre,num_tarjeta,año_permiso,id_vip,descuento=0):
        self.NIF=NIF
        self.nombre=nombre
        self.num_tarjeta=num_tarjeta
        self.año_permiso=año_permiso

        if  int(año_permiso)>10:
            self.descuento=25
        else:
            self.descuento=20

     
    def get_descuento(self):
        return self.descuento
    
    def get_nombre(self):
        return self.nombre
    
    def get_NIF(self):
        return self.NIF
    
    def get_numtarjeta(self):
        return self.num_tarjeta