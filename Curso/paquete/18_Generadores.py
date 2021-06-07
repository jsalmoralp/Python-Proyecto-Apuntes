"""
Generadores: Permite extraer valores de una función y almacenarlos,
(de uno en uno) en objetos iterables (que se pueden recorrer),
sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.
"""

####
# Función Normal
####


def genera_multiplos_de_7(limite):
    numero = 1
    lista_numeros = []

    while numero <= limite:
        lista_numeros.append((numero * 7))
        numero += 1

    return lista_numeros  # Retorna toda la lista creada.


print(genera_multiplos_de_7(10))

# [FIN] Función normal

####
# Función aplicando concepto de Generadores
####


def generador_multiplos_de_7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
        numero += 1


# Esto debuelve un objeto de tipo generador, y no se puede ver el contenido.
obtieneMultiplos7 = generador_multiplos_de_7(10)
print(obtieneMultiplos7)
# Para ver su contenido podemos recorrerlo con un "for"
for n in obtieneMultiplos7:
    print(n)

# next(): Retorna el siguiente objeto elemento de un objeto iterable.
print(next(obtieneMultiplos7))
print("Aquí hay 300 líneas de código...")
print(next(obtieneMultiplos7))
print("Aquí hay 1000 líneas de código...")
print(next(obtieneMultiplos7))

"""
Los Generadores son más eficientes que las funciones tradicionales.
Y son muy útiles con listas de valores infinitos o muy grandes.
Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).
"""
# [FIN] Función aplicando concepto de Generadores
