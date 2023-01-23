import copy
import os.path
import pickle
from io import open
import datetime
from entities.abonado import Abonado


class AbonadoService:
    abonados = []
    lista_facturacion = []

    @staticmethod
    def crear_abonado(matricula, tipo_vehiculo, dni, nombre, apellidos, email, num_tarjeta, fecha_alta, fecha_baja,
                      tipo_abono, facturacion, pin, plaza_asignada):
        if os.path.lexists("db/abonados.pckl") is False and os.path.lexists("db/facturacion.pckl"):
            AbonadoService.cargar_abonados()
        else:
            abonado = Abonado(matricula, tipo_vehiculo, dni, nombre, apellidos, email, num_tarjeta, fecha_alta, fecha_baja,
                              tipo_abono, facturacion, pin, plaza_asignada)
            AbonadoService.abonados.append(abonado)
        return AbonadoService.abonados

    @staticmethod
    def cargar_abonados():
        try:
            with open("db/abonados.pckl", "ab+") as fichero:
                AbonadoService.abonados = pickle.load(fichero)
                fichero.seek(0)
            with open("db/facturacion.pckl", "ab+") as fichero:
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

    @staticmethod
    def comprobar_caducidad_mes(mes):
        # Comprueba que el mes sea correcto y que sea igual o mayor al mes del año actual.
        # También que la lista no esté vacía
        dt = datetime.datetime.now()
        if 1 <= mes <= 12 and dt.month <= mes:
            if len(AbonadoService.abonados) > 0:
                lista_proxima_caducidad_mes = list(
                    filter(lambda abonado: abonado.fecha_baja.month == mes and abonado.fecha_baja.year == dt.year,
                           AbonadoService.abonados))
                return print(cad for cad in lista_proxima_caducidad_mes)
            else:
                return print("*** No hay ningún abonado que caduque en esa fecha *** \n ")
        else:
            return print("ERROR --> Fecha inválida")

    @staticmethod
    def comprobar_caducidad_dias():
        # Comprueba qeu la lista no esté vacía y luego filtra para que la fecha de
        # caducidad esté entre los próximos 10 días.
        dt = datetime.datetime.now()
        if len(AbonadoService.abonados) > 0:
            lista_proxima_caducidad_dias = list(
                filter(lambda abonado: dt.now() < abonado.fecha_baja < dt.now() + datetime.timedelta(days=10),
                       AbonadoService.abonados))
            return print(cad for cad in lista_proxima_caducidad_dias)
        else:
            return print("No hay ningún abonado que caduque en los próximos 10 días")

    @staticmethod
    def buscar_dni(dni):
        for abonado in AbonadoService.abonados:
            if abonado.dni == dni:
                return abonado
            else:
                return None

    @staticmethod
    def buscar_matricula(matricula):
        for abonado in AbonadoService.abonados:
            if abonado.matricula == matricula:
                return abonado
            else:
                return None

    @staticmethod
    def annadir_facturacion(abon):
        nuevo = copy.copy(abon)
        AbonadoService.lista_facturacion.append(nuevo)
        AbonadoService.guardar_facturacion()

    @staticmethod
    def guardar_facturacion():
        fichero = open('db/facturacion.pckl', 'wb')
        pickle.dump(AbonadoService.abonados, fichero)
        fichero.close()

    @staticmethod
    def mostrar_facturacion():
        if len(AbonadoService.lista_facturacion) == 0:
            print("No hay ningún registro en la base de datos.")
            return
        suma_de_pagos = []
        for abonado in AbonadoService.lista_facturacion:
            suma_de_pagos.append(abonado.pago)
            print(f'{abonado}\n')
        total = sum(suma_de_pagos)
        total = round(total, 2)
        print(f'SUMA TOTAL DE PAGOS: {total}€')

    @staticmethod
    def borrar(dni):
        for indice, abonado in enumerate(AbonadoService.abonados):
            if abonado.dni == dni and abonado.fecha_baja > datetime.datetime.now():
                abonado = AbonadoService.abonados.pop(indice)
                AbonadoService.guardar()
                return abonado
            else:
                print("El abonado ya está dado de baja.")


