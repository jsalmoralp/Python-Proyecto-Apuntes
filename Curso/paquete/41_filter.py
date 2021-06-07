"""
Filter: Funciones de orden superior (programación funcional).
Verifica que los elementos de una lista cumplan una determinada condición, devolviendo
un objeto iterable (iterador) con los elementos que cumplieron con la condición.
"""

edades = [12, 11, 24, 36, 8, 6, 10, 41, 32, 58, 14, 50, 7]


def mayor_edad(edad):
    return edad >= 18


edades_mayores_edad = list(filter(mayor_edad, edades))
print(edades_mayores_edad)

edades_menores_edad = list(filter(lambda edad: edad < 18, edades))
print(edades_menores_edad)


class Persona:
    def __init__(self, nom, eda):
        self.nombre = nom
        self.edad = eda

    def __str__(self):
        txt = "{0} tiene {1} años."
        return txt.format(self.nombre, self.edad)


personas = [
    Persona("Alberto", 32),
    Persona("Anna", 16),
    Persona("Andy", 27),
    Persona("Jesús", 25),
    Persona("Cecilia", 19),
    Persona("Laura", 30)
]

perosnas_mayores_edad = list(filter(lambda pax: pax.eadad >= 18, personas))

for per in perosnas_mayores_edad:
    print(per)
