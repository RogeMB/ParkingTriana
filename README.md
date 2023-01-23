# PARKING TRIANA
## Proyecto práctico en Python sobre la gestión de un Parking de vehículos. **Importante**: el programa está pensado para ejecutarlo desde la consola o terminal de windows, lynux o mac. También podrás ejecutarlo desde la terminal de un IDE, pero no es lo ideal. Más abajo indicamos cómo ejecutar el programa en la terminal.

<img src="https://img.shields.io/badge/Python-3.10-green"/>

 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/800px-Python.svg.png" width="500" alt="Python Logo"/>
 
___


## **Documentación**

:point_right: Véase en la carpeta UML del proyecto.


## **Introducción** :speech_balloon:

Este es un ejercicio práctico para el desarrollo en **Python**.

También se ha prácticado el manejo de **StarUML**, **PyCharm** y la metodología ágil **SCRUM** para el reparto de tareas a través la ramificación de estas con **GitHub**.

El proyecto trata de gestionar un parking y que sus datos tengan persistencia utilizando Pickle.


Se pueden realizar las siguientes funcionalidades: 	:point_right:
* Depositar un vehículo como cliente, nuevo cliente o abonado
* Retirar un vehículo como cliente, nuevo cliente o abonado
* Consultar estado del parking (disponibilidad de plazas)
* Consultar abonados activos y un historial de facturas
* Dar de alta un abonado, editarlo o darle de baja
* Consultar la facturación en un rango de fecha determinado
* Consultar los abonos que caducan en un mes y en los próximos 10 días

---

## **Tecnologías utilizadas** 

Para realizar este proyecto hemos utilizado:

1. [Python 3.10 - utilizando librerias como math, os, re, pickle io, datatime, copy, threading,...](https://www.python.org/downloads/)
2. [PyCharm](https://www.jetbrains.com/pycharm/download/?source=google&medium=cpc&campaign=14127625862&term=pycharm&content=536947779792&gclid=CjwKCAiA2rOeBhAsEiwA2Pl7Q_UYJ0Sken1Sobe5hmtYQeBhzYOTfpUn8gFi99FW8LQLMPW7W9hlVxoCBjYQAvD_BwE#section=windows)
3. [Star UML](https://staruml.io/)
4. [GitHub](https://github.com/)




### Ejemplos del Código Usado: 

**PYTHON**:
```Python
    @staticmethod
    def comprobar_caducidad_mes(mes):
        # Comprueba que el mes sea correcto y que sea igual o mayor al mes del año actual.
        # También que la lista no esté vacía
        dt = datetime.datetime.now()
        if 1 <= mes <= 12 and dt.month <= mes:
            if len(AbonadoService.abonados) > 0:
                lista_proxima_caducidad_mes = list(
                    filter(lambda abonado: abonado.fecha_baja.month == mes and abonado.fecha_baja.year == dt.year,
                           AbonadoService.abonados))
                return print(cad for cad in lista_proxima_caducidad_mes)
            else:
                return print("*** No hay ningún abonado que caduque en esa fecha *** \n ")
        else:
            return print("ERROR --> Fecha inválida")

```


---
## **Arranque**

Realiza un *git clone* de la siguiente dirección: 
*https://github.com/RogeMB/ParkingTriana*

```console
git clone https://github.com/RogeMB/ParkingTriana.git
```

Dirígete hasta el directorio:

> cd ./ParkingTriana/


**Primero** tienes que tener instalado Python en tu PC y sería recomendable tener alguna IDE, como **PyCharm** o **VisualStudio Code**

Ejecuta el siguiente comando:
    
    python run.py -t
    
    
Si lo ejecutas desde un IDE, asegúrate de estar en el fichero que se llama run.py para ejecutarlo:
    
    run.py


___
## **Autor**

Este proyecto ha sido realizado por: 

* [Rogelio Mohigefer Barrera - GITHUB](https://github.com/RogeMB)

Estudiante de 2º Desarrollo de Aplicaciones Multiplataforma, grado 
superior de formación profesional en la ciudad de Sevilla, España.

### **Thump up :+1: And if it was useful for you, star it! :star: :smiley:**

___
## **TODO**

Tareas realizadas y cosas por hacer.

[ ] Fix possible future errors
___


