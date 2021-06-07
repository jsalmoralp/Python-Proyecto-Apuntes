"""
Listas: Son estructuras de datos que nos permiten almacenar distintos valores.
(equivalentes a los arrays en otros lenguajes de programación)
Son estructuras dinámicas, pueden MUTAR.
"""

# Creamos una Lista con llaves.
lista1 = ["Joan", 25, 98.3, True, "Pepi", 56.3]
print(lista1)

print(lista1[:])  # Toda la lista.
print(lista1[2])  # Un elemento en concreto.
print(lista1[-1])  # El último elemento.
print(lista1[0:3])  # Una porción de la lista.
print(lista1[:2])  # Desde la primera posición con dos valores.
print(lista1[3:])  # Desde la posicion 3 hasta el final.

lista1.append("Nuevo valor")  # Añadimos un nuevo valor al final de la lista.
print(lista1)
lista1.insert(4, "Valor sitio predeterminado")  # Añadimos un valor en un indice predeterminado.
print(lista1)
lista1.extend(["añadimos", "otra", "lista"])  # Fusionamos dos listas.
print(lista1)
print(lista1.index("Pepi"))  # Saber en que indice se encuentra un elemento.

lista1.remove(56.3)  # Elimina un elemento por su valor.
print(lista1)
lista1.pop()  # Elimina el ultimo elemento de una lista.
print(lista1)

lista2 = ["esto es", "otra", "lista"]
lista3 = lista1 + lista2  # Podemos almacenar en una variable todos los valores de dos listas.
print(lista3)

print(lista2 * 2)  # Podemos crear una lista que todos sus valores estan duplicados.

print("otra" in lista2)  # Devuelve true o false si el elemento que le pasamos esta dentro de la lista.
