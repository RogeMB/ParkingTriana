import uuid
from entities.cliente import Cliente


class Abonado(Cliente):
    def __init__(self, matricula, tipo_vehiculo, dni, nombre, apellidos, email, num_tarjeta, fecha_alta, fecha_baja,
                 tipo_abono, pago, plaza_asignada):
        super().__init__(matricula=matricula, tipo_vehiculo=tipo_vehiculo)

        self.__id = uuid.uuid4()
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__num_tarjeta = num_tarjeta
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja
        self.__tipo_abono = tipo_abono
        self.__pago = pago
        self.__plaza_asignada = plaza_asignada

    def __del__(self):
        return f'Se ha eliminado el abonado {self.__dni} correctamente.'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, fecha_alta):
        self.__fecha_alta = fecha_alta

    @property
    def fecha_baja(self):
        return self.__fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, fecha_baja):
        self.__fecha_baja = fecha_baja


    @property
    def tipo_abono(self):
        return self.tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, tipo_abono):
        self.__tipo_abono = tipo_abono

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, pago):
        self.__pago = pago

    @property
    def plaza_asignada(self):
        return self.__plaza_asignada

    @plaza_asignada.setter
    def plaza_asignada(self, plaza_asignada):
        self.__plaza_asignada = plaza_asignada
