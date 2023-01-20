import os
import time
import pickle

from services.parking_service import ParkingService
from services.plaza_service import PlazasService
from services.cliente_service import ClienteService
from threading import Thread
from views import menus
from helpers import helpers

plaza_serv = PlazasService()
plaza_serv.crear_plazas()

parking_serv = ParkingService()
parking_serv.crear_parking("Triana", plaza_serv.plazas)

cliente_serv = ClienteService()
cliente_serv.cargar_clientes()

lista_parkings = parking_serv.parkings
lista_plazas = plaza_serv.plazas
lista_clientes = cliente_serv.clientes


def almacenar():
    salida = True
    while salida:
        contador = 1
        while contador <= 301:
            if main_thread.is_alive():
                time.sleep(1)
                contador += 1
            else:
                contador = 302
                salida = False

    with open("../db/plazas.pckl", "wb") as fichero:
        pickle.dump(lista_plazas, fichero)
        fichero.close()
        del fichero
    with open("../db/parkings.pckl", "wb") as fichero:
        pickle.dump(lista_parkings, fichero)
        fichero.close()
        del fichero
    with open("../db/clientes.pckl", "wb") as fichero:
        pickle.dump(lista_clientes, fichero)
        fichero.close()
        del fichero


def iniciar():

    salida = True
    while salida:
        user = "admin"

        time.sleep(1)
        helpers.limpiar_pantalla()
        menus.menu_inicio()
        try:
            print("Seleccione una opción: ")
            opcion = int(helpers.leer_texto())
            if opcion == 0:
                print("Saliendo...")
                salida = False
                break

            if opcion == 1:
                helpers.limpiar_pantalla()
                menus.menu_cliente_principal()

            elif opcion == 2:
                print(f"Hola {user}")
                if helpers.comprobar_password():
                    print("RRRRRRRRRRRR")
                else:
                    pass
            else:
                print("ERROR --> Por favor, seleccione una opción válida")
        except:
            print("ERROR --> Seleccione una número entero")


    print("***** GRACIAS, HASTA PRONTO *****")

    # Falta armar el main empezando a llamar todos los métodos ya construidos


main_thread = Thread(target=iniciar())
almacen_thread = Thread(target=almacenar())

main_thread.start()
almacen_thread.start()
