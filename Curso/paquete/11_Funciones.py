"""
Función: Es un conjunto de instrucciones que realizan un proceso.
Su principal ventaja es que ns ayudan a evitar código repetido.
"""


def saludar():
    print("Salmoral")
    print("Joan")
    print("raskan")
    return "Hola"


print(saludar())


def evaluar_sueldo_minimo(sueldo):
    if sueldo == 1000:
        print("Eres un mileurista")
    elif sueldo > 1000:
        print("Tienes un sueldo por encima de la media")
    else:
        print("Tienes un sueldo por debajo de la media")
