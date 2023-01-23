import math
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

    @staticmethod
    def calcular_ingresos(fecha_inicial, fecha_final):
        # Calcula los ingresos de las facturas siempre que no sean None y que estén entre las fechas indicadas.
        # Se ha comprobado previamente que las fechas sean válidas.
        # Se filtra y se guarda to en una lista a la que se suma todos sus elementos y se redondea el resultado a 2 dec.
        lista_ingresos = list(
            filter(lambda factura: factura.precio_total is not None and fecha_inicial <= factura.fecha_entrada <= fecha_final, FacturaService.facturas))
        result = math.fsum(lista_ingresos)
        result = round(result, 2)
        return result

    @staticmethod
    def buscar_factura(plaza_salida, matricula_salida, pin_salida):
        factura_salida = list(filter(lambda factura: factura.plaza.id == plaza_salida
                              and factura.matricula == matricula_salida
                              and factura.pin == pin_salida, FacturaService.facturas))
        if len(factura_salida) > 0:
            return factura_salida[0]
        else:
            return None
