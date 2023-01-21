import os.path
import pickle
from entities.plaza import Plaza
from entities.enums.tipo_vehiculo import TipoVehiculo
from io import open


class PlazasService:
    plazas = []

    @staticmethod
    def crear_plazas():
        if os.path.lexists("db/plazas.pckl") is False:
            PlazasService.cargar_plazas()

        else:
            for i in range(1, 31):
                if 1 <= i < 21:
                    p = Plaza(TipoVehiculo.TURISMO)
                    PlazasService.plazas.append(p)
                elif 21 <= i < 28:
                    p = Plaza(TipoVehiculo.MOTOCICLETA)
                    PlazasService.plazas.append(p)
                else:
                    p = Plaza(TipoVehiculo.MOVILIDADREDUCIDA)
                    PlazasService.plazas.append(p)

        return PlazasService.plazas

    @staticmethod
    def cargar_plazas():
        try:
            with open("db/plazas.pckl", "ab+") as fichero:
                PlazasService.plazas = pickle.load(fichero)
                fichero.seek(0)
        except:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()

    @staticmethod
    def mostrar():
        if len(PlazasService.plazas) == 0:
            print("El parking está vacío.")
            return
        for pl in PlazasService.plazas:
            print(pl)

    @staticmethod
    def agregar(pl):
        PlazasService.plazas.append(pl)
        PlazasService.guardar()

    @staticmethod
    def guardar():
        fichero = open('db/plazas.pckl', 'wb')
        pickle.dump(PlazasService.plazas, fichero)
        fichero.close()
