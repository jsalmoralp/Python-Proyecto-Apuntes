# Apartado 28 (Métodos Accesores - GET y SET)
# Apartado 29 (Sobreescritura del métod "__str__")
class Cuenta:
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

    # Getters (métodos GET) => Nos permiten obtener el valor de una variable encapsulada.
    def get_saldo(self):
        return self.__saldo

    def get_propietario(self):
        return self.__propietario

    def get_moneda(self):
        return self.__moneda

    # Setters (métodos SET) => Nos permiten cambiar el valor de una variable encapsulada.
    def set_moneda(self, moneda):
        self.__moneda = moneda

    # El método "__str__" lo tienen todas las clases por defecto,
    #  y és el método que define como se va a devolver cuando se
    #  intenta imprimir un objeto de esa clase directamente.
    def __str__(self):
        texto = "Propietario: {0} / Saldo: {1} / Moneda: {2}"
        return texto.format(self.__propietario, self.__saldo, self.__moneda)

####
# Métodos Accesores
####
cuenta1 = Cuenta("Joan Salmoral", 15000, "Euros")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("Dólares")
print(cuenta1.get_moneda())

# [FIN] Métodos Accesores

####
# Sobreescritura del método "__str__"
####
print(cuenta1)
# [FIN] Sobreescritura del método "__str__"
