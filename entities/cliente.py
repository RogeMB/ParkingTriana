class Cliente:

    def __init__(self, matricula, tipo_vehiculo, abonado):
        self.__matricula = matricula
        self.__tipo_vehiculo = tipo_vehiculo
        self.__abonado = abonado

    def __str__(self):
        return f'El cliente tiene la matrícula {self.__matricula} con el tipo de vehículo {self.__tipo_vehiculo} ' \
               f'y está {self.know_abonado()} '

    def __del__(self):
        return f'El cliente {self.__matricula} se ha borrado correctamente'

    def know_abonado(self):
        if self.__abonado:
            return "abonado"
        else:
            return "no abonado"

    @property  # getter
    def matricula(self):
        return self.__matricula

    @matricula.setter  # setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property  # getter
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter  # setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo

    @property  # getter
    def abonado(self):
        return self.__abonado

    @abonado.setter  # setter
    def abonado(self, abonado):
        self.__abonado = abonado
