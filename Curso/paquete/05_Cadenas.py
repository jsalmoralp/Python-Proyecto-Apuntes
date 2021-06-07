texto = "Esto es un tEXto de pruebas"

print(texto)
print(texto.lower())  # Transforma el texto completo a minúsculas.
print(texto.upper())  # Transforma el texto completo a mayúsculas.
print(texto.title())  # Convierte una cadena  un formato de titulo, cada palabra nueva empieza con mayúsculas.

print(texto.find('ex'))  # Posición donde encuentra la cadena o porción.
print(texto.count("e"))  # Cantidad de ocurrencias de una letra o porción.

textoFinal = texto.replace("e", "3")  # Remplaza una cadena o porción por otra.
print(textoFinal)

valor = texto.isnumeric()  # Arroja true o false dependiendo si es un número.
print(valor)

cadenaSeparada = texto.split(" ") # Separa por un valor una cadena y debuelve un array con todas las separaciones.
print(cadenaSeparada)
