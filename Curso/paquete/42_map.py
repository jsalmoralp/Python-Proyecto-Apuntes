"""
Map: Aplica una función a dcada elemento de una lista iterable, dvolviendo otra lista.
"""


def elevar_cuadrado(num):
    # return num * num
    return pow(num, 2)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))  # Del 1 al 10
print(numeros)

numeros_elevados = list(map(elevar_cuadrado, numeros))
