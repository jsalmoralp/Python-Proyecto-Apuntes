texto1 = "Hola"
texto2 = "Mundo"

textoFinal = texto1 + " " + texto2  # Concatenación de forma simple.
print(textoFinal)

print("El saludo es: %s %s" % (texto1, texto2))  # Concatenación con variables y "%".

saludoFinal = "Saludo 1: {} {}".format(texto1, texto2)  # Concatenación por posicionamiento simple.
print(saludoFinal)
saludoFinal = "Saludo 2: {0} {1}".format(texto1, texto2)  # Concatenación por posicionamiento asignado.
print(saludoFinal)
saludoFinal = "Saludo 3: {1} {0}".format(texto1, texto2)  # Conatenación por posicionamiento asignado y reposicionado.
print(saludoFinal)
saludoFinal = "Saludo 4: {x} {y}".format(x=texto1, y=texto2)  # Concatenacion asignado a variable.
print(saludoFinal)
