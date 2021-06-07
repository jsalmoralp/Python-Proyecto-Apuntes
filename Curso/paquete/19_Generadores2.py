# Cuando indicamos un * delante del parámetro de una función,
#  estamos indicando que se va a recibir un número indeterminado
#  de valores. Además, esos valores se recibirán en forma de tupla.


def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng


lenguajesObtenidos = devuelve_lenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))

"""
def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        for letra in leng
            yield letra
            
# Y lo mismo pero más abreviado...:

def devuelve_lenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

"""
