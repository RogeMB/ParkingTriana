import time
import pickle
from services.parking_service import ParkingService
from services.plaza_service import PlazasService
from services.cliente_service import ClienteService
from threading import Thread


plaza_serv = PlazasService()
plaza_serv.cargar_plazas()

parking_serv = ParkingService()
parking_serv.crear_parking("Triana", plaza_serv.plazas)
parking1 = parking_serv.parkings[0]

cliente_serv = ClienteService()
cliente_serv.cargar_clientes()


lista_parkings = parking_serv.parkings
lista_plazas = plaza_serv.plazas
lista_clientes = cliente_serv.clientes


def almacenar():
    while True:
        if mainThread.is_alive():
            time.sleep(300)
        else:
            almacenarThread.join()
            break

    with open("db/plazas.pckl", "wb") as fichero:
        fichero.seek(0)
        pickle.dump(lista_plazas, fichero)
        del fichero
    with open("db/parkings.pckl", "wb") as fichero:
        pickle.dump(lista_parkings, fichero)
        fichero.close()
        del fichero
    with open("db/clientes.pckl", "wb") as fichero:
        pickle.dump(lista_clientes, fichero)
        fichero.close()
        del fichero


almacenarThread = Thread(target=almacenar())
almacenarThread.start()


def iniciar():
    print("aquí iría el programa")

    # Falta armar el main empezando a llamar todos los métodos ya construidos


mainThread = Thread(target=iniciar())
mainThread.start()






