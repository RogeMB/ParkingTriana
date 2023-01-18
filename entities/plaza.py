import uuid


class Plaza:
    contador = 0
    seccion = ord("a")

    def __init__(self, disponible=True, cliente=None):
        self.__id = self.generar_id_plaza()
        self.__disponible = disponible
        self.__cliente = cliente

    def __str__(self):
        return f'La plaza {self.__id} está {self.know_disponibilidad()} plazas y su cliente es {self.__cliente}'

    def __del__(self):
        print(f'La plaza {self.__id} se ha borrado correctamente')

    def know_disponibilidad(self):
        result = self.__disponible if "disponible" else "ocupada"
        return result

    def generar_id_plaza(self):
        value = 0
        key = "A"

        for i in range(self.contador, 10000):
            value = i
            break

        for i in range(self.seccion, ord('z') + 1):
            if self.contador <= 100:
                key = i
                break
            else:
                self.seccion = self.seccion + 1
                key = self.seccion

        self.contador += 1
        return str(key+value).upper()

    @property  # getter
    def id(self):
        return self.__id

    @id.setter  # setter
    def id(self, id):
        self.__id = id

    @property  # getter
    def disponible(self):
        return self.__disponible

    @disponible.setter  # setter
    def disponible(self, nombre):
        self.__disponible = nombre.capitalize()

    @property  # getter
    def cliente(self):
        return self.__cliente

    @cliente.setter  # setter
    def cliente(self, cliente):
        self.__cliente = cliente
