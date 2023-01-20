from entities.enums import tipo_vehiculo as tv


class Plaza:
    __set_usados = set()

    def __init__(self, tipo_vehiculo, cliente=None, disponible=True):

        self.__id = self.generar_id_plaza()
        self.__tipo_vehiculo = tipo_vehiculo
        self.__cliente = cliente
        self.__disponible = disponible

    def __str__(self):
        return f'La plaza {self.__id} para vehículos {self.know_tipo_vehiculo()} está {self.know_disponibilidad()} ' \
               f'y su cliente es {self.__cliente}'

    def __del__(self):
        print(f'La plaza {self.__id} se ha borrado correctamente')

    def know_disponibilidad(self):
        if self.__disponible:
            return "disponible"
        else:
            return "ocupada"

    def know_tipo_vehiculo(self):
        if self.__tipo_vehiculo == tv.TipoVehiculo.TURISMO:
            return "TURISMO"
        elif self.__tipo_vehiculo == tv.TipoVehiculo.MOTOCICLETA:
            return "MOTO"
        else:
            return "MOVILIDAD REDUCIDA"

    @staticmethod
    def generar_id_plaza():
        key = None
        lista_keys = (','.join(["A%d" % i for i in range(1, 301)])).split(",")
        for i in range(0, len(lista_keys) + 1):
            key = lista_keys[i]
            if key not in Plaza.__set_usados:
                Plaza.__set_usados.add(key)
                return key

    @property  # getter
    def id(self):
        return self.__id

    @id.setter  # setter
    def id(self, id):
        self.__id = id

    @property
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo

    @property  # getter
    def cliente(self):
        return self.__cliente

    @cliente.setter  # setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property  # getter
    def disponible(self):
        return self.__disponible

    @disponible.setter  # setter
    def disponible(self, disponible):
        self.__disponible = disponible
