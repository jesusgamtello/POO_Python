class Cliente(object):
    #atos  personales  (NIFy nombre),  número  de  tarjeta  de  crédito, 
    # identificador  del  vehículoa  alquilar,
    # el  tiempo por el que se alquilayaño en el que se sacó el permiso de conducir
    contratos=[]
    def __init__(self,NIF,nombre,num_tarjeta,año_permiso,descuento=0):
        self.NIF=NIF
        self.nombre=nombre
        self.num_tarjeta=num_tarjeta
        self.año_permiso=año_permiso
        if int(año_permiso)>10:
            self.descuento=5

    
    def get_descuento(self):
        return self.descuento
    
    def get_nombre(self):
        return self.nombre
    
    def get_NIF(self):
        return self.NIF
    
    def get_numtarjeta(self):
        return self.num_tarjeta

    def get_contratos(self):
        return self.contratos
    def set_contratos(self,valor):
        self.contratos.append(valor)