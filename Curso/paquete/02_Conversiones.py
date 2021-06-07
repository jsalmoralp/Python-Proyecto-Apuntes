# Tenemos dos numeros pero en formato string, por eso se concatenan y no se suman.
numero1 = "35"
numero2 = "18"
print(numero1 + numero2)

# Pasamos los dos valores de tipo string a numérico, de esta forma ya los podemos sumar.
num1 = int(numero1)
num2 = int(numero2)
print(num1 + num2)

# Pasamos un valor de tipo decimal a entero.
sueldo = 1200.43
sueldoEntero = int(sueldo)
print(sueldoEntero)

# Pasamos un valor de tipo string a decimal, de esta forma podemos operar con el.
valor = "4500.89"
valorDecimal = float(valor)
print(valorDecimal * 3)

# a un valor de tipo numerico no se le puede contar el numero de caracteres, por eso debemos pasarlo a tipo string.
edad = 100
print(len(str(edad)))
