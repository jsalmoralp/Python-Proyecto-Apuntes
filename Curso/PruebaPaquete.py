# Apartado 23
"""
Paquetes:
Directorios (carpetas) donde se almacenan módulos relacionados entre sí.

¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor (modularización y reutilización).

¿Como se crea un paquete?
Crear un directorio (o carpeta) con un archivo dentro llamado "__init__.py",
que por lo general no debe tener contenido.

Lo que hace "__init__.py" es "convertir" un directorio en un módulo (paquete),
que contiene otros módulos, y esto lo hace para poder importarlos.
"""

from Paquete1.funcionesCadena import *
from Paquete1.funcionesNumericas import *

print(multiplicar(5, 6))
print(contar_letras("Joan Salmoral Parramon"))
