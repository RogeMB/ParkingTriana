import uuid


class Parking:
    def __init__(self, nombre=None, plazas=None):
        self.__id = uuid.uuid4()
        self.__nombre = nombre
        self.__plazas = plazas

    def __str__(self):
        return f'El parking {self.__nombre} tiene {self.__plazas} plazas y su id es {self.__id}'

    def __del__(self):
        print(f'El parking {self.__nombre} se ha borrado correctamente')

    @property  # getter
    def id(self):
        return self.__id

    @id.setter  # setter
    def id(self, id):
        self.__id = id

    @property  # getter
    def nombre(self):
        return self.__nombre.capitalize()

    @nombre.setter  # setter
    def nombre(self, nombre):
        self.__nombre = nombre.capitalize()

    @property  # getter
    def plazas(self):
        return self.__plazas

    @plazas.setter  # setter
    def plazas(self, plazas):
        self.__plazas = plazas


# Prueba:

p = Parking("Prueba", 100)
p.nombre = "Triana"
p.plazas = 100


print(str(p))
print(p)
del p
