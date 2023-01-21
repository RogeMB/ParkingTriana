import os.path
import pickle
from io import open
from entities.cliente import Cliente


class ClienteService:

    clientes = []

    @staticmethod
    def crear_cliente(matricula, tipo_vehiculo, abonado):
        if os.path.lexists("db/clientes.pckl") is False:
            ClienteService.cargar_clientes()
        else:
            cliente = Cliente(matricula, tipo_vehiculo, abonado)
            ClienteService.clientes.append(cliente)

        return ClienteService.clientes

    @staticmethod
    def cargar_clientes():
        try:
            with open("db/clientes.pckl", "ab+") as fichero:
                ClienteService.clientes = pickle.load(fichero)
                fichero.seek(0)
        except:
            print("Fichero no encontrado. Creando fichero...")
        finally:
            fichero.close()
            del fichero

    @staticmethod
    def mostrar():
        if len(ClienteService.clientes) == 0:
            print("No hay ningún cliente en la base de datos.")
            return
        for cl in ClienteService.clientes:
            print(cl)

    @staticmethod
    def agregar(cl):
        ClienteService.clientes.append(cl)
        ClienteService.guardar()

    @staticmethod
    def guardar():
        fichero = open('db/clientes.pckl', 'wb')
        pickle.dump(ClienteService.clientes, fichero)
        fichero.close()
