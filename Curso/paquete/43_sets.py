"""
Sets: son colleciones desordenadas de objetos únicos.
"""

canasta = {'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
print(canasta)

numeros = {1, 3, 5, 8, 3, 4, 12, 1}
print(numeros)

# Tipo 1 de Sets: Set mutables
a = set('abracadabra')  # Mutables, se pueden añadir nuevos elementos
print(a)
a.add('g')
print(a)
a.add('a')
print(a)

# Tipo 2 de Sets: Set inmutables (no se pueden añadir nuevos elementos)
b = frozenset('perro')
print(b)
# b.add('k')  # Esto no se puede hacer!!
print(b)

# Intersecciones:
mi_set1a = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
print(mi_set1a)
mi_set1b = {1, 2, 3, 4, 5} & {3, 4, 5, 6}
print(mi_set1b)

# Union
mi_set2a = {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
print(mi_set2a)
mi_set2b = {1, 2, 3, 4, 5} | {3, 4, 5, 6}
print(mi_set2b)


mi_set3a = {1, 2, 3, 4}.difference({2, 3, 5})
print(mi_set3a)
mi_set3b = {1, 2, 3, 4} - {2, 3, 5}
print(mi_set3b)

mi_set4a = {1, 2, 3, 4}.symmetric_difference({2, 3, 5})
print(mi_set4a)

mi_set5a = {1, 2, 3, 4, 5}.issuperset({1, 2, 3})
print(mi_set5a)
mi_set5b = {1, 2, 3, 4, 5}.issubset({1, 2, 3})
print(mi_set5b)
