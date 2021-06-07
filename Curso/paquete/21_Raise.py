"""
Raise: Sirve para lanzar (de forma intencional) excepciones en Python.
Esto tambien hace que el programa, pare su ejecución como si de un error se tratara.
"""


def evaluar_nota(nota):
    if nota < 0:
        raise ValueError("No se permiten valores negativos...")  # El mensaje es personalizado.
    elif nota >= 8:
        print("Excelente")
    elif nota >= 5:
        print("Aprobado")
    else:
        print("Desaprobado")


evaluar_nota(8)

print("Esta línea se ejecuta?")
