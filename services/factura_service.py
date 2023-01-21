import os.path
import pickle
from io import open

from entities.factura import Factura


class FacturaService:

    facturas = []

    @staticmethod
    def crear_factura(matricula, plaza, pin_salida):
        if os.path.lexists("db/facturas.pckl") is False:
            FacturaService.cargar_facturas()
        else:
            factura = Factura(matricula, plaza, pin_salida)
            FacturaService.facturas.append(factura)

        return FacturaService.facturas

    @staticmethod
    def cargar_facturas():
        try:
            with open("db/facturas.pckl", "ab+") as fichero:
                FacturaService.facturas = pickle.load(fichero)
                fichero.seek(0)
        except:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
            del fichero

    @staticmethod
    def mostrar():
        if len(FacturaService.facturas) == 0:
            print("No hay ninguna factura en la base de datos.")
            return
        for fac in FacturaService.facturas:
            print(fac)

    @staticmethod
    def agregar(fa):
        FacturaService.facturas.append(fa)
        FacturaService.guardar()

    @staticmethod
    def guardar():
        fichero = open('db/facturas.pckl', 'wb')
        pickle.dump(FacturaService.facturas, fichero)
        fichero.close()
