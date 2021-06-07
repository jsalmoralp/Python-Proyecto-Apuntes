"""
Bucles: Son estructuras d control d flujo que repite 1 o varias líneas de código.
"""

for num in range(0, 20, 2):  # Empieza en 2, menor a 20, y de dos en dos.
    print("Valor actual: {0}".format(num))

for i in range(0, 11):
    print("5 X {0} = {1}".format(i, (5*i)))

for nom in ["Joan", "Pepi", "Calamardo", "Montse"]:
    print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
