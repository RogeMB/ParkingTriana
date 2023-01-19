from entities.parking import Parking
import os.path
from services.plaza_service import PlazasService, pickle
from io import open


class ParkingService:

    parkings = []

    @staticmethod
    def crear_parking(nombre):
        if os.path.lexists("db/parking.pckl") is False:
            ParkingService.cargar_parking()
        else:
            park = Parking(nombre, PlazasService.plazas)
            ParkingService.parkings.append(park)

        return ParkingService.parkings

    @staticmethod
    def cargar_parking():
        try:
            if os.path.lexists("db/parking.pckl"):
                with open("db/parking.pckl", "ab+") as fichero:
                    ParkingService.parkings = pickle.load(fichero)
                    fichero.seek(0)
        except os.path.lexists("db/parking.pckl") is False:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
