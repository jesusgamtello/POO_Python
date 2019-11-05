import os
from Cliente import Cliente
from Cliente_Vip import Vip
from Hibrido import Hibridos
from Nohibridos import Nohibridos
class Leer_ficheros():
    def leer_clientes_fichero(self):
        try:
            clientes=[]
            with open('Clientes.txt','r') as c:
                for linea in c:
                    clientes.append(linea.split())
            return clientes
        except:
            print("el fichero clientes no existe")
    
   

    def leer_coches_fichero(self):
        try:
            vehiculos=[]
            with open ('Vehiculos.txt','r') as v:
                for linea in v:
                    vehiculos.append(linea.split())
            return vehiculos
        except:
            print("el fichero vehiculos no existe")

    def crear_objeto_clientes(self):
        c=self.leer_clientes_fichero()
        id_vip=0
        clientes=[]
        for i in c:
            if i[4]=='false':
                cliente=Cliente(i[1],i[0],i[2],i[3])
                clientes.append(cliente)
                
            else:
                cliente=Vip(i[1],i[0],i[2],i[3],id_vip)
                id_vip+=1
                clientes.append(cliente)
        return clientes
            
    
    def crear_objeto_vehiculo(self):
        v=self.leer_coches_fichero()
        vehiculos=[]
        for i in v:
            if i[0]=='h':
                vehiculo=Hibridos(i[1],i[2],i[3],i[4],i[5],i[6])
                vehiculos.append(vehiculo)
            else:
                vehiculo=Nohibridos(i[1],i[2],i[3],i[4],i[5])
                vehiculos.append(vehiculo)
        return vehiculos
