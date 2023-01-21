import re
import os
import random
import platform

import helpers
from views import menus


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input(">>> ")
        if longitud_min <= len(texto) <= longitud_max:
            return texto


def validar_dni(dni, lista):
    if not re.match('[0-9]{9}[A-Z]$', dni):
        print("DNI incorrecto. Introduce bien el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("Este DNI ya está siendo utilizado.")
            return False
    return True


matriculas_usadas = set()


def lector_matricula():
    while True:
        matricula = ""
        for i in range(4):
            matricula += str(random.randint(0, 9))
        matricula += "-"
        for i in range(3):
            matricula += chr(random.randint(65, 90))
        if matricula not in matriculas_usadas:
            matriculas_usadas.add(matricula)
            break
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

