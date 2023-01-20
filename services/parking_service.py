
import os.path
import pickle
from io import open
from entities.parking import Parking


class ParkingService:

    parkings = []

    @staticmethod
    def crear_parking(nombre, plazas):
        if os.path.lexists("../db/parkings.pckl") is False:
            ParkingService.cargar_parking()
        else:
            park = Parking(nombre, plazas)
            ParkingService.parkings.append(park)
        return ParkingService.parkings

    @staticmethod
    def cargar_parking():
        try:
            with open("../db/parkings.pckl", "ab+") as fichero:
                ParkingService.parkings = pickle.load(fichero)
                fichero.seek(0)
        except:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
            del fichero

    @staticmethod
    def mostrar():
        if len(ParkingService.parkings) == 0:
            print("No hay ningún parking.")
            return
        for pl in ParkingService.parkings:
            print(pl.__str__)

    @staticmethod
    def agregar(pl):
        ParkingService.parkings.append(pl)
        ParkingService.guardar()

    @staticmethod
    def guardar():
        fichero = open('../db/parkings.pckl', 'wb')
        pickle.dump(ParkingService.parkings, fichero)
        fichero.close()
