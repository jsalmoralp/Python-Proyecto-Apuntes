"""
Diccionarios: Son estructuras de datos que nos permiten almacenar distintos valores.
(como las tuplas o listas)
Pero en esta, los dtos se almacenan asociados a una lave única, y tenemos una relación clasve->valor.
Los elementos almacenados están en desorden, el orden es indiferente a la forma de almacenarlos.
"""

# Creamos un Diccionario con claudator.
miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"  # Si creamos una nueva clave, se crea.
print(miDiccionario)

miDiccionario["España"] = "Barcelona"  # Si la clave ya exite, se modifica el valor.
print(miDiccionario)

del miDiccionario["España"]  # Podemos eliminar una clave.
print(miDiccionario)

dic2 = {"Salmoral": "Joan", 31: True, "Sueldo": 1200.50}  # Un Diccionario puede almacenar distintos tipo de valores.
print(dic2[25])

# Podemos crear un Diccionario a partir de una Tupla.
llaves = ("España", "Francia", "Inglaterra")
dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
print(dicPaises)

# Podemos crear un Diccionario dentro d otro Diccionario.
datosPersonales = {"Apellidos": "Salmoral", "Anios": {1: 2018, 2: 2019, 3: 2020, 4: 2021}}
print(datosPersonales)
print(datosPersonales["Anios"])

# Obtenemos el valor de una clave en concreto, y si no existe obtenemos el valor por defecto.
print(datosPersonales.get("Apllidos", "Cartofas"))  # Clave que buscar, valor por defecto.

print(datosPersonales.keys())  # Obtenemos todas las claves del Diccionario en formato Lista por defecto.
print(datosPersonales.values())  # Obtenemos todos los valores del Diccionario en Formato Lista por defecto.

print(list(datosPersonales.keys()))  # Nos devuelve el resultado en formato Lista.
print(tuple(datosPersonales.keys()))  # Nos devuelve el resultado en formato Tupla.
