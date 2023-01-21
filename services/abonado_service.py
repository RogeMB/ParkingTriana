import os.path
import pickle
from io import open

from entities.abonado import Abonado


class AbonadoService:

    abonados = []

    @staticmethod
    def crear_abonado(matricula, tipo_vehiculo, dni, nombre, apellidos, email, num_tarjeta, fecha_alta, fecha_baja,
                      tipo_abono, facturacion, plaza_asignada):
        if os.path.lexists("db/abonados.pckl") is False:
            AbonadoService.cargar_abonados()
        else:
            abonado = Abonado(matricula, tipo_vehiculo, dni, nombre, apellidos, email, num_tarjeta, fecha_alta,
                              fecha_baja, tipo_abono, facturacion, plaza_asignada)
            AbonadoService.abonados.append(abonado)

        return AbonadoService.abonados

    @staticmethod
    def cargar_abonados():
        try:
            with open("db/abonados.pckl", "ab+") as fichero:
                AbonadoService.abonados = pickle.load(fichero)
                fichero.seek(0)
        except:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
            del fichero

    @staticmethod
    def mostrar():
        if len(AbonadoService.abonados) == 0:
            print("No hay ningún abonado en la base de datos.")
            return
        for abo in AbonadoService.abonados:
            print(abo)

    @staticmethod
    def agregar(ab):
        AbonadoService.abonados.append(ab)
        AbonadoService.guardar()

    @staticmethod
    def guardar():
        fichero = open('db/abonados.pckl', 'wb')
        pickle.dump(AbonadoService.abonados, fichero)
        fichero.close()
