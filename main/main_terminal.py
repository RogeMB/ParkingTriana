import time
import pickle
import locale
import datetime

from entities.abonado import Abonado
from entities.cliente import Cliente
from entities.enums.tipo_vehiculo import TipoVehiculo
from entities.factura import Factura
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
lista_facturas_abonados = abonado_serv.lista_facturacion


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
        plaza_serv.guardar()
        fichero.close()
        del fichero
    with open("db/parkings.pckl", "wb") as fichero:
        pickle.dump(lista_parkings, fichero)
        parking_serv.guardar()
        fichero.close()
        del fichero
    with open("db/clientes.pckl", "wb") as fichero:
        pickle.dump(lista_clientes, fichero)
        parking_serv.guardar()
        fichero.close()
        del fichero
    with open("db/abonados.pckl", "wb") as fichero:
        pickle.dump(lista_abonados, fichero)
        abonado_serv.guardar()
        fichero.close()
        del fichero
    with open("db/facturacion.pckl", "wb") as fichero:
        pickle.dump(lista_facturas_abonados, fichero)
        abonado_serv.guardar()
        fichero.close()
        del fichero
    with open("db/facturas.pckl", "wb") as fichero:
        pickle.dump(lista_facturas, fichero)
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

                        elif opcion_sub_cliente == 1:  # consultar parking
                            helpers.limpiar_pantalla()
                            print(f'\t\t\t*****Parking {lista_parkings[0].nombre}*****"\n')
                            plaza_serv.mostrar()
                            print(f'\nPLAZAS LIBRES: {PlazasService.calcular_libres()}\n'
                                  f'PORCENTAJE OCUPADAS: {PlazasService.calcular_ocupadas()} %\n')
                            print("Presiona ENTER para volver...")
                            helpers.leer_texto()

                        elif opcion_sub_cliente == 2:  # aparcar tanto cliente como abonado
                            helpers.limpiar_pantalla()
                            plazas_libres = list(filter(lambda plaza: plaza.disponible, lista_plazas))
                            plazas_libres_turismo = list(
                                filter(lambda plaza: plaza.tipo_vehiculo == TipoVehiculo.TURISMO, plazas_libres))
                            plazas_libres_moto = list(
                                filter(lambda plaza: plaza.tipo_vehiculo == TipoVehiculo.MOTOCICLETA, plazas_libres))
                            plazas_libres_mr = list(
                                filter(lambda plaza: plaza.tipo_vehiculo == TipoVehiculo.MOVILIDADREDUCIDA,
                                       plazas_libres))

                            if len(plazas_libres) > 0:
                                try:
                                    print(f'Plazas libres actuales:{len(plazas_libres)}\n'
                                          f'Plazas libres turismo: {len(plazas_libres_turismo)}\n'
                                          f'Plazas libres motocicleta: {len(plazas_libres_moto)}\n'
                                          f'Plazas libres movilidad reducida: {len(plazas_libres_mr)}\n')
                                    print(
                                        "Por favor, pulse 1 para que el lector la lea automáticamente"
                                        " o cualquier otro número para empezar a introducirla manualmente:")
                                    opcion_matricula = int(helpers.leer_texto())
                                    matricula = ""
                                    if opcion_matricula == 1:
                                        matricula = helpers.lector_automatico_matricula()
                                    else:
                                        print("Inserte su matrícula:")
                                        matricula = helpers.leer_texto().upper()
                                        while helpers.validar_matricula_simple(matricula) is False:
                                            matricula = helpers.leer_texto()
                                    print("Matrícula validada. Comprobando base de datos...")
                                    abonado_1 = abonado_serv.buscar_matricula(matricula=matricula)
                                    cliente_1 = cliente_serv.buscar_matricula(matricula=matricula)
                                    if abonado_1:  # aparcar abonado
                                        print(f"Bienvenido,  {abonado_1.nombre}, con dni {abonado_1.dni}.\n"
                                              f"Actualizando la plaza...")
                                        plaza = abonado_1.plaza_asignada
                                        plaza_serv.guardar()
                                        time.sleep(1)
                                        print(f'Aceptada. Por favor, aparque en su plaza {plaza.id}.')
                                        time.sleep(2)
                                        salida_sub_cliente = False
                                    elif cliente_1:  # aparcar cliente
                                        print(f'Bienvenido de nuevo, \n'
                                              f'Matrícula = {cliente_1.matricula} \n'
                                              f'Tipo de vehículo = {cliente_1.tipo_vehiculo}\n')
                                        if cliente_1.tipo_vehiculo == TipoVehiculo.TURISMO and len(
                                                plazas_libres_turismo) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_turismo)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}\n")
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        elif cliente_1.tipo_vehiculo == TipoVehiculo.MOTOCICLETA and len(
                                                plazas_libres_moto) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_moto)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}\n")
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        elif cliente_1.tipo_vehiculo == TipoVehiculo.MOVILIDADREDUCIDA and len(
                                                plazas_libres_mr) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_mr)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}\n")
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        else:
                                            print("No hay plazas disponibles en este momento. Lo sentimos.")
                                            time.sleep(1)
                                            salida_sub_cliente = False
                                    else:  # aparcar nuevo cliente
                                        print(f'Bienvenido nuevo cliente\n')
                                        print("Inserte el tipo de vehículo según el siguiente menú:")
                                        menus.menu_tipo_vehiculo()
                                        tipo_v = int(helpers.leer_texto())
                                        while tipo_v not in [1, 2, 3]:
                                            print(
                                                "ERROR --> Por favor, elija una opción válida. Seleccione de nuevo:")
                                            tipo_v = int(helpers.leer_texto())
                                        tipo_v_elegido = helpers.elegir_tipo_vehiculo(tipo_v)
                                        nuevo_cliente = Cliente(matricula=matricula, tipo_vehiculo=tipo_v_elegido)
                                        cliente_serv.agregar(nuevo_cliente)
                                        if nuevo_cliente.tipo_vehiculo == TipoVehiculo.TURISMO and len(
                                                plazas_libres_turismo) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_turismo)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}\n")
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        elif cliente_1.tipo_vehiculo == TipoVehiculo.MOTOCICLETA and len(
                                                plazas_libres_moto) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_moto)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}")
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        elif cliente_1.tipo_vehiculo == TipoVehiculo.MOVILIDADREDUCIDA and len(
                                                plazas_libres_mr) > 0:
                                            print("Asignando plaza...")
                                            plaza_asignada = next(plaza for plaza in plazas_libres_mr)
                                            plaza_asignada.disponible = False
                                            plaza_serv.guardar()
                                            pin = helpers.generador_pin_aleatorio()
                                            time.sleep(1)
                                            print("Imprimiendo ticket...")
                                            nueva_factura = Factura(matricula=matricula, plaza=plaza_asignada,
                                                                    pin_salida=pin)
                                            facturas_serv.agregar(nueva_factura)
                                            print(nueva_factura)
                                            print(f"Aceptada. Por favor, aparque en la plaza {plaza_asignada.id}")
                                            print("Pulse ENTER para continuar...")
                                            helpers.leer_texto()
                                            salida_sub_cliente = False
                                        else:
                                            print("No hay plazas disponibles en este momento. Lo sentimos.")
                                            time.sleep(1)
                                            salida_sub_cliente = False
                                except:
                                    print("ERROR --> Se ha producido un error inesperado.")
                                    salida_sub_cliente = False

                        elif opcion_sub_cliente == 3:  # descupar una plaza
                            helpers.limpiar_pantalla()
                            try:
                                print("Por favor, introduzca su matrícula: ")
                                matricula_salida = helpers.leer_texto().upper()
                                while helpers.validar_matricula_simple(matricula_salida) is False:
                                    matricula_salida = helpers.leer_texto().upper()
                                print("Válido.Introduzca el id de su plaza de aparcamiento: ")
                                plaza_salida = helpers.leer_texto()
                                print("Válido. Introduzca su pin de salida: ")
                                pin_salida = int(helpers.leer_texto())
                                factura_salida = facturas_serv.buscar_factura(matricula_salida=matricula_salida,
                                                                              #  aquí peta
                                                                              plaza_salida=plaza_salida,
                                                                              pin_salida=pin_salida)
                                if factura_salida is not None:
                                    factura_salida.fecha_salida = datetime.datetime.now()
                                    factura_salida.plaza.disponible = True
                                    plaza_serv.guardar()
                                    tiempo_total = float(
                                        (factura_salida.fecha_salida - factura_salida.fecha_entrada).total_seconds() / 60)
                                    tipo_v_salida = factura_salida.plaza.tipo_vehiculo
                                    if tipo_v_salida == TipoVehiculo.TURISMO:
                                        factura_salida.precio_total = tiempo_total * 0.12
                                    elif tipo_v_salida == TipoVehiculo.MOTOCICLETA:
                                        factura_salida.precio_total = tiempo_total * 0.08
                                    elif abonado_serv.buscar_matricula(matricula_salida) is not None:
                                        factura_salida.precio_total = 0
                                    else:
                                        factura_salida.precio_total = tiempo_total * 0.10
                                    facturas_serv.guardar()
                                    print("Imprimiendo factura de salida...")
                                    time.sleep(1)
                                    print(factura_salida)
                                    print("Pulsa ENTER para salir.")
                                    helpers.leer_texto()
                                    salida_sub_cliente = False
                                else:
                                    print("ERROR --> No hay ningún vehículo estacionado.")
                                    salida_sub_cliente = False
                            except:
                                print("ERROR --> Se ha producido un error inesperado.")
                                salida_sub_cliente = False
                        else:
                            print("ERROR --> Seleccione una opción válida")
                    except:
                        print("ERROR --> Seleccione una número entero")
                        salida_sub_cliente = False

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

                            elif opcion_sub == 1:  # consultar parking
                                helpers.limpiar_pantalla()
                                print(f'\t\t\t*****Parking {lista_parkings[0].nombre}*****"\n')
                                plaza_serv.plazas = lista_plazas
                                plaza_serv.mostrar()
                                print(f'\nPLAZAS LIBRES: {PlazasService.calcular_libres()}\n'
                                      f'PORCENTAJE OCUPADAS: {PlazasService.calcular_ocupadas()} %\n')
                                print("Presiona ENTER para volver...")
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
                                print(" * * * ABONADOS EN ACTIVO * * * \n")
                                abonado_serv.mostrar()
                                print(" * * * REGISTRO DE PAGOS DE ABONADOS ACTIVOS O INACTIVOS * * * \n")
                                abonado_serv.mostrar_facturacion()
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
                                            print("Introduzca el dni del abonado:")
                                            dni = helpers.leer_texto()
                                            if helpers.validar_dni(dni, lista_abonados):
                                                print("Válido. Introduzca ahora el nombre:")
                                                nombre = helpers.leer_texto().capitalize()
                                                print("Válido. Introduzca ahora el apellido:")
                                                apellido = helpers.leer_texto().capitalize()
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
                                                        while tipo_v not in [1, 2, 3]:
                                                            print(
                                                                "ERROR --> Por favor, elija una opción válida. Seleccione de nuevo:")
                                                            tipo_v = int(helpers.leer_texto())
                                                        tipo_v_elegido = helpers.elegir_tipo_vehiculo(tipo_v)
                                                        print(
                                                            "Válido. Introduzca un número del 1 al 4 según el siguiente menú:")
                                                        menus.tipo_abono()
                                                        tipo_abo = int(helpers.leer_texto())
                                                        while tipo_abo not in [1, 2, 3, 4]:
                                                            print(
                                                                "ERROR --> Por favor, elija una opción válida. Seleccione de nuevo:")
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
                                                        print(f'f:PLAZA A ASIGNAR: {plaza}')
                                                        print("Creando abonado...")
                                                        time.sleep(1)
                                                        nuevo_abo = Abonado(matricula=matricula,
                                                                            tipo_vehiculo=tipo_v_elegido,
                                                                            tipo_abono=tipo_eleg, nombre=nombre,
                                                                            apellidos=apellido,
                                                                            email=email, num_tarjeta=num_tar,
                                                                            facturacion=pago_eleg,
                                                                            fecha_alta=fecha_alta,
                                                                            fecha_baja=fecha_baja, pin=pin,
                                                                            plaza_asignada=plaza, dni=dni)
                                                        abonado_serv.agregar(nuevo_abo)
                                                        abonado_serv.annadir_facturacion(nuevo_abo)
                                                        cliente_serv.agregar(nuevo_abo)
                                                        plaza.disponible = False
                                                        plaza.cliente = nuevo_abo.dni
                                                        plaza_serv.guardar()
                                                        helpers.limpiar_pantalla()
                                                        print(
                                                            "Abonado correctamente creado.\n Pulsa ENTER para continuar.")
                                                        helpers.leer_texto()
                                                        salida_ab = False
                                                        break
                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                salida_ab = False
                                                print(
                                                    "Este DNI ya está siendo utilizado o no es válido.\n Volviendo...")
                                                break

                                        elif opcion_abo == 2:  # Edición Abonado
                                            helpers.limpiar_pantalla()
                                            salida_ed_ab = True
                                            while salida_ed_ab:
                                                try:
                                                    print("Introduzca el dni del abonado que quiera editar:")
                                                    dni = helpers.leer_texto()
                                                    if helpers.validar_dni_edicion(dni, lista_abonados) is False:
                                                        print("Este DNI no se encuentra en la base de datos. "
                                                              "\n Volviendo...")
                                                        salida_ed_ab = False
                                                    else:
                                                        print("Dni válido. Cliente encontrado.")
                                                        abonado_a_editar = next(abonado for abonado in lista_abonados
                                                                                if abonado.dni == dni
                                                                                and abonado.fecha_baja > datetime.datetime.now() + datetime.timedelta(
                                                            hours=1))
                                                        # te deja editar siempre que sea mayor a 1 hora su fecha de baja

                                                        print("Selecciona una opción: \n"  # submenú edición
                                                              "[1]. Modificar cliente\n"
                                                              "[2]. Renovar abono")
                                                        opcion_sub_edi = int(helpers.leer_texto())
                                                        while opcion_sub_edi not in [1, 2]:
                                                            print("ERROR --> Elija una opción válida")
                                                            opcion_sub_edi = int(helpers.leer_texto())
                                                        if opcion_sub_edi == 1:
                                                            helpers.limpiar_pantalla()
                                                            print(" * * * EDICIÓN * * *")
                                                            print(
                                                                "Introduzca los siguientes datos. Para mantener los actuales pulse ENTER:")
                                                            print(f'DNI: {dni}')
                                                            abonado_a_editar.dni = helpers.leer_texto().upper() or abonado_a_editar.dni
                                                            print(f'NOMBRE: {abonado_a_editar.nombre}')
                                                            abonado_a_editar.nombre = helpers.leer_texto().capitalize() or abonado_a_editar.nombre
                                                            print(f'APELLIDOS: {abonado_a_editar.apellidos}')
                                                            abonado_a_editar.apellidos = helpers.leer_texto().capitalize() or abonado_a_editar.apellidos
                                                            print(f'NUM TARJETA: {abonado_a_editar.num_tarjeta}')
                                                            abonado_a_editar.num_tarjeta = helpers.leer_texto() or abonado_a_editar.num_tarjeta
                                                            print(f'EMAIL: {abonado_a_editar.email}')
                                                            abonado_a_editar.email = helpers.leer_texto() or abonado_a_editar.email
                                                            print("Se procede a generar un nuevo PIN:")
                                                            nuevo_pin = helpers.generador_pin_aleatorio()
                                                            abonado_a_editar.pin = nuevo_pin
                                                            print(f'PIN: {abonado_a_editar.pin}')
                                                            print(f'TIPO VEHICILO: {abonado_a_editar.tipo_vehiculo}')
                                                            abonado_a_editar.tipo_abono = abonado_a_editar.tipo_abono
                                                            print("Aquí NO pulse ENTER. Elija una opción siguiente:")
                                                            menus.menu_tipo_vehiculo()
                                                            tipo_v = int(helpers.leer_texto())
                                                            while tipo_v not in [1, 2, 3]:
                                                                print(
                                                                    "ERROR --> Por favor, elija una opción válida. "
                                                                    "Seleccione de nuevo:")
                                                                tipo_v = int(helpers.leer_texto())
                                                            tipo_v_elegido = helpers.elegir_tipo_vehiculo(tipo_v)
                                                            abonado_a_editar.tipo_vehiculo = tipo_v_elegido
                                                            print(f'MATRÍCULA: {abonado_a_editar.matricula}')
                                                            print(
                                                                "Introduzca su matrícula (formato 1111-AAA) o"
                                                                " Pulse ENTER para mantener la misma:")
                                                            abonado_a_editar.matricula = helpers.leer_texto().upper() or \
                                                                                         abonado_a_editar.matricula
                                                            plaza_antigua = abonado_a_editar.plaza_asignada
                                                            plaza = next(plaza for plaza in lista_plazas if
                                                                         plaza.disponible and plaza.tipo_vehiculo == abonado_a_editar.tipo_vehiculo)
                                                            print(f"Pulse una opción:\n"
                                                                  f"[1]. PLAZA ANTIGUA: "
                                                                  f"{abonado_a_editar.plaza_asignada.id} \n"
                                                                  f"[2]. PLAZA NUEVA: {plaza.id}")
                                                            opc = int(helpers.leer_texto())
                                                            if opc == 1:
                                                                pass
                                                            elif opc == 2:
                                                                abonado_a_editar.plaza_asignada = plaza
                                                                plaza_antigua.disponible = True
                                                                plaza.disponible = False
                                                                plaza.cliente = abonado_a_editar.dni
                                                                plaza_serv.guardar()
                                                            else:
                                                                pass
                                                            print("Pulse ENTER para completar cambios.")
                                                            helpers.leer_texto()
                                                            helpers.limpiar_pantalla()
                                                            print("GUARDANDO NUEVOS DATOS...")
                                                            abonado_serv.guardar()
                                                            time.sleep(3)
                                                            salida_ed_ab = False
                                                        elif opcion_sub_edi == 2:
                                                            try:
                                                                abonado_a_renovar = next(
                                                                    abonado for abonado in lista_abonados
                                                                    if abonado.dni == dni
                                                                    and abonado.fecha_baja > datetime.datetime.now() + datetime.timedelta(
                                                                        hours=1))
                                                                # Te deja renovar si su fecha de caducidad es mayor a 1
                                                                # hora.
                                                                helpers.limpiar_pantalla()
                                                                print(" * * * RENOVACIÓN * * *")
                                                                menus.tipo_abono()
                                                                print("Introduzca un número del 1 al 4:")
                                                                tipo_abo = int(helpers.leer_texto())
                                                                while tipo_abo not in [1, 2, 3, 4]:
                                                                    print(
                                                                        "ERROR --> Por favor, elija una opción válida."
                                                                        " Seleccione de nuevo:")
                                                                    tipo_abo = int(helpers.leer_texto())
                                                                tipo_eleg_a = helpers.elegir_tipo_abono(tipo_abo)
                                                                pago_eleg_a = helpers.elegir_pago(tipo_abo)
                                                                print("Generando fechas...")
                                                                time.sleep(1)
                                                                fecha_baja_nueva = datetime.datetime.now() + datetime.timedelta(
                                                                    days=30 * helpers.pasar_a_meses(tipo_abo))
                                                                abonado_a_renovar.tipo_abono = tipo_eleg_a
                                                                abonado_a_renovar.pago = pago_eleg_a
                                                                abonado_a_renovar.fecha_baja = fecha_baja_nueva
                                                                print(
                                                                    f'FECHA BAJA NUEVA: {fecha_baja_nueva.strftime("%A %d de %B del %Y - %H:%M")}\n'
                                                                    f'TIPO ABONO NUEVO: {tipo_eleg_a}\n'
                                                                    f'PAGO: \t\t {pago_eleg_a} €')
                                                                print("Pulsa ENTER para confirmar los cambios...")
                                                                helpers.leer_texto()
                                                                print("GUARDANDO...")
                                                                abonado_serv.annadir_facturacion(abonado_a_renovar)
                                                                abonado_serv.guardar_facturacion()
                                                                abonado_serv.guardar()
                                                                salida_ed_ab = False
                                                            except:
                                                                print("ERROR -->No se puede renovar aún a este abonado")
                                                        else:
                                                            print("ERROR --> Introduzca una opción válida.")
                                                except:
                                                    salida_ed_ab = False
                                                    print("ERROR --> No se ha podido completar con éxito la edición.")

                                        elif opcion_abo == 3:  # Borrado de abonados
                                            # print(" * * * BAJA ABONADO * * * ")
                                            try:
                                                print("Introduzca el dni del abonado que quiera dar de baja:")
                                                dni = helpers.leer_texto()
                                                if helpers.validar_dni_edicion(dni, lista_abonados) is False:
                                                    print("Este DNI no se encuentra en la base de datos. "
                                                          "\n Volviendo...")
                                                    salida_ab = False
                                                else:
                                                    print("Se procede a dar de baja al abonado. "
                                                          "Si quiere continuar pulse 1. Cualquier otro para cancelar:")
                                                    opcion = int(helpers.leer_texto())
                                                    if opcion == 1:
                                                        print("BORRANDO...")
                                                        time.sleep(1)
                                                        abonado_baja = abonado_serv.borrar(dni)
                                                        print(f'Se ha borrado con éxito al abonado:\n'
                                                              f'{abonado_baja}')
                                                        plaza = abonado_baja.plaza
                                                        plaza.disponible = True
                                                        plaza_serv.guardar()
                                                        salida_ab = False
                                                    else:
                                                        print("Cancelando operación...")
                                                        salida_ab = False
                                            except:
                                                print("ERROR --> No se ha podido completar la baja.")
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
