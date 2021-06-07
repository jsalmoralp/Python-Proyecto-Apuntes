"""
Excepción: Error en tiempo de ejecución (durante la ejecución del un programa).
"""

numero1 = 20
numero2 = 0

try:
    resultado = numero1 / numero2
    print("La división de [0] entre {1} es {2}".format(numero1, numero2, resultado))
# except:
except ZeroDivisionError:
    print("No se puede dividir entre 0...")
finally:
    print("Yo siempre aparezco.")
