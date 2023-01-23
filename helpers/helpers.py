import re
import os
import random
import platform

from entities.enums.tipo_abono import TipoAbono
from entities.enums.tipo_vehiculo import TipoVehiculo


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input(">>> ")
        if longitud_min <= len(texto) <= longitud_max:
            return texto


def validar_dni(dni, lista):
    if not re.match('[0-9]{8}[A-Z]$', dni):
        print("DNI incorrecto. Introduce bien el formato.")
        return False
    for abonado in lista:
        if abonado.dni == dni:
            return False
    return True


def validar_dni_edicion(dni, lista):
    if not re.match('[0-9]{8}[A-Z]$', dni):
        print("DNI incorrecto. Introduce bien el formato.")
        return False
    for abonado in lista:
        if abonado.dni == dni:
            return True
    return False


def validar_email(email, lista):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not email_regex.match(email):
        print("Formato no válido.")
        return False
    for abonado in lista:
        if abonado.email == email:
            print("Este email ya está siendo utilizado.")
            return False
    return True


def validar_matricula(matricula, lista):
    matricula_regex = re.compile(r'^[0-9]{4}-[A-Z]{3}$')
    if not matricula_regex.match(matricula):
        print("Formato no válido.")
        return False
    for abonado in lista:
        if abonado.matricula == matricula:
            print("Esta matrícula ya está siendo usada.")
            return False
    return True


def validar_matricula_simple(matricula):
    matricula_regex = re.compile(r'^[0-9]{4}-[A-Z]{3}$')
    if not matricula_regex.match(matricula):
        print("Formato no válido.")
        return False
    else:
        return True


def lector_automatico_matricula():
    matricula = ""
    for i in range(4):
        matricula += str(random.randint(0, 9))
    matricula += "-"
    for i in range(3):
        matricula += chr(random.randint(65, 90))
    return matricula


def comprobar_password():
    intentos = 3
    password = 1234
    fallo = True
    while fallo:
        print("Inserte la contraseña: ")
        contra = int(leer_texto())
        if contra != password:
            intentos -= 1
            print(f"Contraseña incorrecta, tienes {intentos} intentos")
            if intentos == 0:
                print("----->Volviendo al menú principal...")
                return False
        else:
            print("¡Bienvenido admin!")
            return True


def elegir_tipo_abono(tipo_abo):
    if tipo_abo == 1:
        tipo_elegido = TipoAbono.MENSUAL
    elif tipo_abo == 2:
        tipo_elegido = TipoAbono.TRIMESTRAL
    elif tipo_abo == 3:
        tipo_elegido = TipoAbono.SEMESTRAL
    else:
        tipo_elegido = TipoAbono.ANUAL
    return tipo_elegido


def elegir_pago(tipo_abo):
    if tipo_abo == 1:
        pago = 25
    elif tipo_abo == 2:
        pago = 70
    elif tipo_abo == 3:
        pago = 130
    else:
        pago = 200
    return pago


def pasar_a_meses(tipo_abo):
    if tipo_abo == 2:
        meses = 3
    elif tipo_abo == 3:
        meses = 6
    elif tipo_abo == 4:
        meses = 12
    else:
        meses = 1
    return meses


def generador_pin_aleatorio():
    result = random.randrange(100000, 1000000)
    return result


def elegir_tipo_vehiculo(tipo):
    if tipo == 1:
        elegido = TipoVehiculo.TURISMO
    elif tipo == 2:
        elegido = TipoVehiculo.MOTOCICLETA
    else:
        elegido = TipoVehiculo.MOVILIDADREDUCIDA
    return elegido
