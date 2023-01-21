import time
import pickle

from entities.abonado import Abonado
from services.abonado_service import AbonadoService
from services.factura_service import FacturaService
from services.parking_service import ParkingService
from services.plaza_service import PlazasService
from services.cliente_service import ClienteService
from threading import Thread
from views import menus
from helpers import helpers

plaza_serv = PlazasService()
plaza_serv.crear_plazas()

parking_serv = ParkingService()
parking_serv.crear_parking("Triana", plaza_serv.plazas)

cliente_serv = ClienteService()
cliente_serv.cargar_clientes()

abonado_serv = AbonadoService()
abonado_serv.cargar_abonados()

facturas_serv = FacturaService()
facturas_serv.cargar_facturas()

lista_parkings = parking_serv.parkings
lista_plazas = plaza_serv.plazas
lista_clientes = cliente_serv.clientes
lista_abonados = abonado_serv.abonados
lista_facturas = facturas_serv.facturas


def almacenar():
    salida = True
    while salida:
        contador = 1
        while contador <= 301:
            if main_thread.is_alive():
                time.sleep(1)
                contador += 1
            else:
                contador = 302
                salida = False

    with open("db/plazas.pckl", "wb") as fichero:
        pickle.dump(lista_plazas, fichero)
        fichero.close()
        del fichero
    with open("db/parkings.pckl", "wb") as fichero:
        pickle.dump(lista_parkings, fichero)
        fichero.close()
        del fichero
    with open("db/clientes.pckl", "wb") as fichero:
        pickle.dump(lista_clientes, fichero)
        fichero.close()
        del fichero
    with open("db/abonados.pckl", "wb") as fichero:
        pickle.dump(lista_abonados, fichero)
        fichero.close()
        del fichero
    with open("db/facturas.pckl", "wb") as fichero:
        pickle.dump(lista_facturas, fichero)
        fichero.close()
        del fichero


def iniciar():

    salida = True
    while salida:
        user = "admin"

        time.sleep(1)
        helpers.limpiar_pantalla()
        menus.menu_inicio()
        try:
            print("Seleccione una opción: ")
            opcion = int(helpers.leer_texto())
            if opcion == 0:
                print("Saliendo...")
                salida = False
                break

            if opcion == 1:
                helpers.limpiar_pantalla()
                menus.menu_cliente_principal()

            elif opcion == 2:
                print(f"Hola {user}")
                if helpers.comprobar_password():
                    salida_sub_admin = True
                    while salida_sub_admin:
                        try:
                            print("Selecciona una opción: ")
                            opcion_sub = int(helpers.leer_texto())

                            if opcion_sub == 0:
                                print("Volviendo al menú principal...")
                                helpers.limpiar_pantalla()
                                salida_sub_admin = False
                                break
                            elif opcion_sub == 1:  # consultar parking
                                def calcular_libres():
                                    plazas_libres = []
                                    for pla in lista_plazas:
                                        if pla.disponible:
                                            plazas_libres.append(pla)
                                        else:
                                            pass
                                    return len(plazas_libres)

                                def calcular_ocupadas():
                                    porcentaje_ocupadas = 100 - (calcular_libres()*100)/len(lista_plazas)
                                    return porcentaje_ocupadas

                                print(f'\t\t\t*****Parking {lista_parkings[0].nombre}*****"\n')
                                plaza_serv.plazas = lista_plazas
                                plaza_serv.mostrar()
                                print(f'\nPLAZAS LIBRES: {calcular_libres()}\n'
                                      f'PORCENTAJE OCUPADAS: {calcular_ocupadas()} %\n')

                            elif opcion_sub == 3:  # consultar lista abonados
                                clientes_abonados = [cliente for cliente in lista_clientes if isinstance(cliente, Abonado) and cliente.abonado]
                                if len(clientes_abonados) > 0:
                                    for abonado in clientes_abonados:
                                        print(abonado.__str__())

                                else:
                                    print("La lista de abonados está vacía.")


                            else:
                                print("ERROR --> Por favor, seleccione una opción válida")

                        except:
                            print("ERROR --> Seleccione una número entero")

                else:
                    pass
            else:
                print("ERROR --> Por favor, seleccione una opción válida")
        except:
            print("ERROR --> Seleccione una número entero")

    print("***** GRACIAS, HASTA PRONTO *****")

    # Falta armar el main empezando a llamar todos los métodos ya construidos


main_thread = Thread(target=iniciar())
almacen_thread = Thread(target=almacenar())

main_thread.start()
almacen_thread.start()
