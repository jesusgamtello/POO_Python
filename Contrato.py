class Contrato(object):
    
    def __init__(self,cliente,vehiculo,num_dias):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.num_dias=num_dias

    def get_cliente(self):
        return self.cliente

    def get_vehiculo(self):
        return self.vehiculo
    
    def get_num_dias(self):
        return self.num_dias