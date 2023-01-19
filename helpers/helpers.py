import re
import os
import platform


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
