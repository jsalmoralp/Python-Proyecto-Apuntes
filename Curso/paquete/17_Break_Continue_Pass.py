"""
Break: Permite salir de un bucle
Continue: Deja de ejecutar el bucle actual, y continua el bucle en una nueva iteración
Pass: En Python no se puede dejar una definición sin código a ejectura, para hacerlo usamos "pass"
"""

for numero in range(1, 100):
    if numero > 10:
        break  # Cuando el numero sea mayor a 10, se saldrá del bucle.
    elif numero == 5:
        continue  # Cuando el numero sea igual a 5, continuará el bucle en la siguiete iteración.
    print("El numero es {0}".format(numero))


def funcion_cualquiera():
    # Si solo queremos declarar la función, y no queremos que de momento tenga código,
    #  no vasta con dejar un comentario de que se tiene que implementar,
    #  sino, que se tiene que poner esta cláusula, para que no nos de error el código.
    pass
