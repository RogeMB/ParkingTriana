import uuid
from datetime import datetime


class Factura:

    def __init__(self, matricula, plaza, pin_salida, fecha_entrada=datetime.now(), fecha_salida=None,
                 precio_total=None):

        self.__id = uuid.uuid4()
        self.__matricula = matricula
        self.__plaza = plaza
        self.__pin_salida = pin_salida
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__precio_total = precio_total

    def __str__(self):
        return f"==============TICKET DE SALIDA===============\n" \
               f"MATRICULA: \t {self.__matricula}\n" \
               f"FECHA ENTRADA: \t {self.__fecha_entrada}\n" \
               f"PLAZA: \t {self.__plaza.id}\n" \
               f"PIN SALIDA: \t {self.__pin_salida}\n" \
               f"FECHA SALIDA: \t {self.__fecha_salida}\n" \
               f"PRECIO TOTAL: \t {self.__precio_total}\n" \
               f"=============================================\n" \


    def __del__(self):
        return f'La factura {self.__id} se ha borrado correctamente.'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def plaza(self):
        return self.plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def pin_salida(self):
        return self.pin_salida

    @pin_salida.setter
    def pin_salida(self, pin_salida):
        self.__pin_salida = pin_salida

    @property
    def precio_total(self):
        return self.__precio_total

    @precio_total.setter
    def precio_total(self, precio_total):
        self.__precio_total = precio_total

