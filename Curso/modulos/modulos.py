# Apartado 22
"""
Módulo: Es un archivo con extensión ".py" o ".pyc" (Python compilado),
que posee su propio espacio de nombres, y que puede contener variables, funciones, clases o incluso otros módulos.

¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor.

Modularización y reutilización.
"""

"""
import funcionesMatematicas

print(funcionesMatematicas.multiplicacion(5, 6))
"""

"""
from Curso.modulos.funcionesMatematicas import suma, multiplicacion

print(suma(5, 6))
print(multiplicacion(5, 6))
"""

from Curso.modulos.funcionesMatematicas import *

print(suma(5, 6))
print(resta(5, 6))
print(multiplicacion(5, 6))
print(division(5, 6))
print(division_exacta(5, 6))
print(potencia(5, 6))
