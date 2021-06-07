"""
Tupla: Es una estructura de datos propia de Python, que permite almacenar distintos
tipos de datos o valores, y son inmutables (es decir que no cambian una vez inicializadas.
"""
# Creamos una Tupla con parentesis.
# Tupla simple.
tupla = (1, 2, 3)
print(tupla)
# Tupla compuesta.
tupla2 = (7, "Joan", True, 450.1, 16 + 7j)
print(tupla2)
# Tupla dentro de tupla.
tupla3 = (9, 3, (4, 5, 6))
print(tupla3)  # mostramos una tupla entera.
print(tupla2[1])  # Accedemos a un elemento de una tupla.
print(tupla3[2][0])  # Accedemos al elemento de una tupla dentro de otra.

"""
# A un componente de una tupla no se le puede cambiar el valor.
tupla2[1] = "Pepi"
print(tupla2)
"""

print(tupla2[-1])  # Accedemos al ultimo elemento de una tupla.
print(tupla2[-2])  # Accedemos al segundo valor empezando por el final.
print(tupla2[0:4])  # Nos muestra un rango de elementos (rango inicial : cantidad de elementos).

a, b, c = tupla  # Volcamos los valores de la tupla a cada una de las variables.
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3  # Volcamos en una tupla nueva todos los valores de las dos tuplas.
print(tuplaFinal)

print((tuplaFinal.count(3)))  # nos cuenta la cantidad de vces que encuentra el valor especificado.
print(tuplaFinal.index(3))  # Nos muestra el indice de la primera ocurrencia con el valor especificado.
