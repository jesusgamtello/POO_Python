from Cliente_Vip import Vip


class Concesionario(object):

    def __init__(self,vehiculos,clientes):
        self.vehiculos=vehiculos
        self.clientes=clientes
    
    #nos devuelve el cliente asociado a su dni
    def devolver_cliente(self,dni):
        k=0
        for i in self.clientes:
            k+=1
            if i.get_NIF()==dni:
                return i
    
    def consultar_vehiculos(self):
        for i in self.vehiculos:
            print(i.get_modelo())
    
    
    #nos dice si nuestro cliente esta en la base de datos o no devolviendo true si existe o false en caso contrario
    def comprobar_cliente(self,dni):
        k=0
        for i in self.clientes:
            k+=1
            if i.get_NIF()==dni:
                return True
            elif k==len(self.clientes):
                return False 

    def consultar_vip(self,dni):
        cliente=self.devolver_cliente(dni)
        return isinstance(cliente,Vip)
    
    def consultar_reservas(self,dni):
        cliente=self.devolver_cliente(dni)
        

    

        
        
        
            
                
    
    
            

            
            

   
        
                


            



                
