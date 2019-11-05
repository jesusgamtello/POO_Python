import os
from Concesionario import Concesionario
from leer_ficheros import Leer_ficheros


p=Leer_ficheros()
clientes=p.crear_objeto_clientes()
coches=p.crear_objeto_vehiculo()
concesionario=Concesionario(coches,clientes)

def menu():

    os.system('cls') #seria clear en caso de ejecutar en linux
    print('Bienvenido al menú de nuestra aplicacion\n')
    print('-------------------------------------------\n')
    print('Seleccione una opcion:\n')
    print('1.Consultar todos los vehiculos disponibles en el sistema\n')
    print('2.Alquilar un vehiculo\n')
    print('3.Consultar reservas de un cliente\n')
    print('4.Mostrar contrato de un cliente\n')
    print('5.Saber si un cliente es VIP\n')
    print('6.Consultar descuentos de un cliente\n')
    print('7.Salir\n')


while True:
    menu()
    opcion=int(input("La opcion del menu elegida es >>"))

    if opcion==1:
        print("leyendo vehiculos disponibles...\n")
        if clientes != None:
            concesionario.consultar_vehiculos()

        input('\nTodos los clientes mostrados\nPulse una tecla para continuar')
    elif opcion==2:
        print("")
        input('alquilar un vehiculo\nPulse una tecla para continuar')
    elif opcion==3:
        DNI=str(input("Introduzca el DNI >>\n"))
        if concesionario.comprobar_cliente(DNI):
            concesionario.consultar_reservas(DNI)
        else:
            print("el cliente no se encuentra en la base de datos")
        input('consultar reservas\nPulse una tecla para continuar')
    elif opcion==4:
        print("")
        input('mostrar contrato\nPulse una tecla para continuar')
    elif opcion==5:
        DNI=str(input("Introduzca el DNI >>\n"))
        if concesionario.comprobar_cliente(DNI):
            if concesionario.consultar_vip(DNI):
                print("el cliente es VIP")
            else:
                print("El cliente NO es VIP")
        else:
            print("el cliente no existe en la base de datos")
        input('\nPulse una tecla para continuar')
    elif opcion==6:
        DNI=str(input("Introduzca el DNI >>\n"))
        if concesionario.comprobar_cliente(DNI):
            print("El descuento del cliente es de ", concesionario.devolver_cliente(DNI).get_descuento())
        else:
            print("el cliente no existe en la base de datos")
        input('\nPulse una tecla para continuar')
    elif opcion==7:
        print("")
        print('Cerrando aplicacion.....')
        break
    else:
        print("")
        input('No se ha introducido ninguna opcion correcta...\nPulsa una tecla para continuar')

