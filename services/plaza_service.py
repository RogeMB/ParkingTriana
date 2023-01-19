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
                    p = Plaza(TipoVehiculo.TURISMO).generar_id_plaza()
                    PlazasService.plazas.append(p)
                    break
                elif 21 <= i < 28:
                    p2 = Plaza(TipoVehiculo.MOTOCICLETA).generar_id_plaza()
                    PlazasService.plazas.append(p2)
                    break

                else:
                    p3 = Plaza(TipoVehiculo.MOVILIDADREDUCIDA).generar_id_plaza()
                    PlazasService.plazas.append(p3)

        return PlazasService.plazas

    @staticmethod
    def cargar_plazas():
        try:
            if os.path.lexists("db/plazas.pckl"):
                with open("db/plazas.pckl", "ab+") as fichero:
                    PlazasService.plazas = pickle.load(fichero)
                    fichero.seek(0)
        except os.path.lexists("db/plazas.pckl") is False:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
