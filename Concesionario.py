from Cliente_Vip import Vip
from Cliente import Cliente
from Contrato import Contrato
from leer_ficheros import Leer_ficheros
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

    def devolver_vehiculo(self,matricula):
        k=0
        for i in self.vehiculos:
            k+=1
            if i.get_matricula()==matricula:
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

    def comprobar_matricula(self,matricula):
        k=0
        for i in self.vehiculos:
            k+=1
            if i.get_matricula()==matricula:
                return True
            elif k==len(self.vehiculos):
                return False

    def consultar_vip(self,dni):
        cliente=self.devolver_cliente(dni)
        return isinstance(cliente,Vip)
    
    def consultar_reservas(self,dni):
        cliente=self.devolver_cliente(dni)

    def realizar_reservas(self,dni):

        if not self.comprobar_cliente(dni):
            nombre=str(input("Introduzca el nombre del nuevo cliente >>\n"))
            DNI=str(input("Introduzca el DNI >>\n"))
            numero=input("Inserte numero de tarjeta >>\n")
            años_carnet=int(input("Introduzca los años que lleva con el permiso de conducir >>\n"))
            cliente=Cliente(nombre, DNI, numero, años_carnet)
            print("Cliente nuevo creado con éxito")
        else:
            cliente=self.devolver_cliente(dni)

        matricula=str(input("introduzca la matricula del vehiculo que desea alquilar >> \n"))
        while not self.comprobar_matricula(matricula):
            matricula=str(input("Matricula introducida incorrecta, introduzca de nuevo otra matricula >>\n"))
        while not self.devolver_vehiculo(matricula).get_disponible():
            matricula=str(input("El vehiculo ya esta alquilado, introduzca otra matricula >>\n"))
        coche=self.devolver_vehiculo(matricula)
        num_dias=str(input("Introduzca el numero de días que desea alquilar el vehiculo >>\n"))
        if coche.get_disponible():

            cliente.set_contratos(Contrato(cliente,coche,num_dias))
            coche.set_disponible(False)
            print("Coche alquilado correctamente")

        '''else:
            print("El coche ya esta alquilado")'''
