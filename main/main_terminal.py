import time
import pickle
import locale
import datetime

from entities.abonado import Abonado
from services.abonado_service import AbonadoService
from services.factura_service import FacturaService
from services.parking_service import ParkingService
from services.plaza_service import PlazasService
from services.cliente_service import ClienteService
from threading import Thread
from views import menus
from helpers import helpers

locale.setlocale(locale.LC_ALL, 'es-ES')

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
        plaza_serv.plazas = lista_plazas
        plaza_serv.guardar()
        fichero.close()
        del fichero
    with open("db/parkings.pckl", "wb") as fichero:
        pickle.dump(lista_parkings, fichero)
        parking_serv.parkings = lista_parkings
        parking_serv.guardar()
        fichero.close()
        del fichero
    with open("db/clientes.pckl", "wb") as fichero:
        pickle.dump(lista_clientes, fichero)
        cliente_serv.clientes = lista_clientes
        parking_serv.guardar()
        fichero.close()
        del fichero
    with open("db/abonados.pckl", "wb") as fichero:
        pickle.dump(lista_abonados, fichero)
        abonado_serv.abonados = lista_abonados
        abonado_serv.guardar()
        fichero.close()
        del fichero
    with open("db/facturas.pckl", "wb") as fichero:
        pickle.dump(lista_facturas, fichero)
        facturas_serv.facturas = lista_facturas
        facturas_serv.guardar()
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
                print(" * * * Zona Cliente * * * ")
                salida_sub_cliente = True
                time.sleep(1)
                while salida_sub_cliente:
                    try:
                        helpers.limpiar_pantalla()
                        menus.menu_cliente_principal()
                        opcion_sub_cliente = int(helpers.leer_texto())
                        print("Seleccione una opción: ")
                        if opcion_sub_cliente == 0:
                            print("Volviendo al menú principal...")
                            helpers.limpiar_pantalla()
                            salida_sub_cliente = False
                            break
                        elif opcion_sub_cliente == 1:  # consultar parking
                            helpers.limpiar_pantalla()
                            print(f'\t\t\t*****Parking {lista_parkings[0].nombre}*****"\n')
                            plaza_serv.plazas = lista_plazas
                            plaza_serv.mostrar()
                            print(f'\nPLAZAS LIBRES: {PlazasService.calcular_libres()}\n'
                                  f'PORCENTAJE OCUPADAS: {PlazasService.calcular_ocupadas()} %\n')
                            print("\nPresiona ENTER para volver...")
                            helpers.leer_texto()

                        elif opcion_sub_cliente == 2:
                            helpers.limpiar_pantalla()
                            print("Aquí van operaciones de aparcamiento")

                        elif opcion_sub_cliente == 3:
                            helpers.limpiar_pantalla()
                            print("Aquí van operaciones de salida")
                        else:
                            print("ERROR --> Seleccione una opción válida")
                    except:
                        print("ERROR --> Seleccione una número entero")

            elif opcion == 2:
                helpers.limpiar_pantalla()
                print(f"Hola {user}")
                if helpers.comprobar_password():
                    salida_sub_admin = True
                    while salida_sub_admin:
                        try:
                            time.sleep(1)
                            helpers.limpiar_pantalla()
                            menus.menu_admin_principal()
                            print("Seleccione una opción: ")
                            opcion_sub = int(helpers.leer_texto())

                            if opcion_sub == 0:
                                print("Volviendo al menú principal...")
                                helpers.limpiar_pantalla()
                                salida_sub_admin = False
                                break
                            elif opcion_sub == 1:  # consultar parking
                                helpers.limpiar_pantalla()
                                print(f'\t\t\t*****Parking {lista_parkings[0].nombre}*****"\n')
                                plaza_serv.plazas = lista_plazas
                                plaza_serv.mostrar()
                                print(f'\nPLAZAS LIBRES: {PlazasService.calcular_libres()}\n'
                                      f'PORCENTAJE OCUPADAS: {PlazasService.calcular_ocupadas()} %\n')
                                print("\nPresiona ENTER para volver...")
                                helpers.leer_texto()

                            elif opcion_sub == 2:  # Mostrar facturación entre dos fechas
                                helpers.limpiar_pantalla()
                                try:
                                    print(" *** FECHA INICIAL *** ")
                                    print("Seleccione un año inicial: ")
                                    anno_inicial = int(helpers.leer_texto())
                                    print("Seleccione un mes inicial: ")
                                    mes_inicial = int(helpers.leer_texto())
                                    print("Seleccione un día inicial: ")
                                    dia_inicial = int(helpers.leer_texto())
                                    print("Seleccione una hora inicial: ")
                                    hora_inicial = int(helpers.leer_texto())
                                    fecha_inicial = datetime.datetime(anno_inicial, mes_inicial, dia_inicial,
                                                                      hora_inicial, 0, 0).strftime(
                                        "%A %d de %B del %Y - %H:%M")

                                    print(f' *** FECHA ELEGIDA --> {fecha_inicial}.')

                                    time.sleep(1)
                                    helpers.limpiar_pantalla()

                                    print(" *** FECHA FINAL *** ")
                                    print("Seleccione un año final: ")
                                    anno_final = int(helpers.leer_texto())
                                    print("Seleccione un mes final: ")
                                    mes_final = int(helpers.leer_texto())
                                    print("Seleccione un día final: ")
                                    dia_final = int(helpers.leer_texto())
                                    print("Seleccione una hora final: ")
                                    hora_final = int(helpers.leer_texto())
                                    fecha_final = datetime.datetime(anno_final, mes_final, dia_final, hora_final, 0, 0) \
                                        .strftime("%A %d de %B del %Y - %H:%M")

                                    print(f' *** FECHA ELEGIDA --> {fecha_final}.')
                                    if fecha_inicial > fecha_final:
                                        print("ERROR --> La fecha inicial no puede ser más próxima a hoy que la final.")
                                    else:
                                        print(f'La suma total de ingresos entre las fechas indicadas es de: '
                                              f'{FacturaService.calcular_ingresos(fecha_inicial, fecha_final)} €')

                                    print("\nPresiona ENTER para volver...")
                                    helpers.leer_texto()
                                except:
                                    print("ERROR --> Introduzca un formato de fecha válido.")

                            elif opcion_sub == 3:  # consultar lista abonados
                                helpers.limpiar_pantalla()
                                abonado_serv.abonados = lista_abonados
                                abonado_serv.mostrar()
                                # Cada abonado tiene un atributo llamado facturación que se va actualizando cada vez
                                # que realice un pago. Así, al imprimir los abonados también se imprimirá su facturación
                                print("\nPresiona ENTER para volver...")
                                helpers.leer_texto()

                            elif opcion_sub == 4:  # alta, baja y modificación de abonados
                                helpers.limpiar_pantalla()
                                salida_ab = True
                                while salida_ab:
                                    try:
                                        helpers.limpiar_pantalla()
                                        menus.menu_gestion_abonado()
                                        print("Seleccione una opción:")
                                        opcion_abo = int(helpers.leer_texto())
                                        if opcion_abo == 0:
                                            salida_ab = False
                                            print("Volviendo...")
                                            break
                                        elif opcion_abo == 1:  # Alta abonado
                                            print("Introduzca el dni del abonado")
                                            dni = helpers.leer_texto()
                                            if helpers.validar_dni(dni, lista_abonados):
                                                print("Válido. Introduzca ahora el nombre:")
                                                nombre = helpers.leer_texto()
                                                print("Válido. Introduzca ahora el apellido:")
                                                apellido = helpers.leer_texto()
                                                print("Válido. Introduzca ahora el email:")
                                                email = helpers.leer_texto()
                                                if helpers.validar_email(email, lista_abonados):
                                                    print("Válido. Introduzca ahora un número de tarjeta:")
                                                    num_tar = helpers.leer_texto()
                                                    print("Válido. Introduzca ahora su matrícula (formato 1111-AAA):")
                                                    matricula = helpers.leer_texto().upper()
                                                    if helpers.validar_matricula(matricula, lista_abonados):
                                                        print(
                                                            "Válido. Introduzca un número del 1 al 3 según el siguiente menú:")
                                                        menus.menu_tipo_vehiculo()
                                                        tipo_v = int(helpers.leer_texto())
                                                        tipo_v_elegido = helpers.elegir_tipo_vehiculo(tipo_v)
                                                        print(
                                                            "Válido. Introduzca un número del 1 al 4 según el siguiente menú:")
                                                        menus.tipo_abono()
                                                        tipo_abo = int(helpers.leer_texto())
                                                        tipo_eleg = helpers.elegir_tipo_abono(tipo_abo)
                                                        pago_eleg = helpers.elegir_pago(tipo_abo)
                                                        print("Generando fechas...")
                                                        time.sleep(1)
                                                        fecha_alta = datetime.datetime.now()
                                                        fecha_baja = datetime.datetime.now() + datetime.timedelta(
                                                            days=30 * helpers.pasar_a_meses(tipo_abo))
                                                        print("Generando pin...")
                                                        pin = helpers.generador_pin_aleatorio()
                                                        print(f'PIN: {pin}')
                                                        print("Asignando plaza...")
                                                        plaza = next(plaza for plaza in lista_plazas if
                                                                     plaza.disponible and plaza.tipo_vehiculo == tipo_v_elegido)
                                                        print(f'f:PLAZA: {plaza}')
                                                        print("Creando abonado...")
                                                        time.sleep(1)
                                                        nuevo_abo = Abonado(matricula=matricula, tipo_vehiculo=tipo_v_elegido,
                                                                tipo_abono=tipo_eleg, nombre=nombre, apellidos=apellido,
                                                                email=email, num_tarjeta=num_tar, facturacion=pago_eleg,
                                                                fecha_alta=fecha_alta, fecha_baja=fecha_baja, pin=pin,
                                                                plaza_asignada=plaza, dni=dni)

                                                        lista_abonados.append(nuevo_abo)

                                                        helpers.limpiar_pantalla()
                                                        print(
                                                            "Abonado correctamente creado. Pulsa ENTER para continuar.")
                                                        helpers.leer_texto()
                                                        salida_ab = False
                                                        break
                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                salida_ab = False
                                                print("Volviendo...")
                                                break
                                        else:
                                            print("ERROR --> Por favor, seleccione una opción válida.")
                                    except:
                                        print("ERROR --> Por favor, seleccione un número entero.")

                            elif opcion_sub == 5:  # consulta abonos mes y 10 días
                                helpers.limpiar_pantalla()
                                salida_cad = True
                                while salida_cad:
                                    try:
                                        helpers.limpiar_pantalla()
                                        menus.menu_admin_caducidad()
                                        opcion_cadu = int(helpers.leer_texto())
                                        if opcion_cadu == 0:
                                            salida_cad = False
                                            print("Volviendo...")
                                            break
                                        elif opcion_cadu == 1:
                                            print("Por favor, indique el mes que quiera consultar: ")
                                            mes = int(helpers.leer_texto())
                                            AbonadoService.comprobar_caducidad_mes(mes)
                                        elif opcion_cadu == 2:
                                            AbonadoService.comprobar_caducidad_dias()
                                        else:
                                            print("ERROR --> Por favor, seleccione una opción válida")
                                    except:
                                        print("ERROR --> Por favor, introduzca un número entero")

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


def __call__(self, *args, **kwargs):
    return self.cls(*args, **kwargs)
