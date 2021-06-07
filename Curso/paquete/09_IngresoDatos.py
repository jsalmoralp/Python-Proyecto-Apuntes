nombre = input("Ingrese su nombre: ")  # Input debuelve un valor de tipo string.
edad = input("Ingrese su edad: ")
sueldo = float(input("Ingrese su sueldo: "))  # Transformamos el valor string a float que debuelve el input.

print("Hola, " + nombre)
edadFutura = int(edad) + 20  # Pasamos a valor numérico edad para poder operar con ella.
print("Tu edad es: " + edad)  # Como "edad" es de tipo texto podemos concatenarlo con un "+".
print("Tu edad (dentro de 20 años) será:", edadFutura)
print("Tu sueldo es:", sueldo)  # Como "sueldo" es un tipo numérico debemos concatenar con ",".
