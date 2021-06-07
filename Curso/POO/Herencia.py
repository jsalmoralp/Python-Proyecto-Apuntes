# Apartado 30 (Herencia - Sobreescribir constructor)
# Apartado 31 (Herencia - Sobreescribir método de clase)
# Apartado 32 (Sustitución entre clases)

class Persona:
    def __init__(self, apePat, apeMat, nom):
        self.apellido_paterno = apePat
        self.apellido_materno = apeMat
        self.nombre = nom

    def mostrar_nombre_completo(self):
        txt = "{0} {1} {2}"
        return txt.format(self.nombre, self.apellido_paterno, self.apellido_materno)

    def datos(self):
        print(self.mostrar_nombre_completo())


class Estudieante(Persona):
    def __init__(self, apePat, apeMat, nom, pro):
        super(Estudieante, self).__init__(apePat, apeMat, nom)
        self.profesion = pro

    def datos(self):
        super(Estudieante, self).datos()
        print("Profesión: {0}".format(self.profesion))


####
# Herencia - Sobreescribir constructor
####
estu1 = Estudieante("Salmoral", "Parramon", "Joan", "Ingeniería Civil")
print(estu1.mostrar_nombre_completo())
print(estu1.profesion)
# [FIN] Herencia - Sobreescribir constructor

####
# Herencia - Sobreescribir método de clase
####
estu1.datos()
# [FIN] Herencia - Sobreescribir método de clase

####
# Sustitución entre clases
####
print(isinstance(estu1, Estudieante))
print(isinstance(estu1, Persona))

estu2 = Persona("Salmoral", "Parramon", "Joan")
print(isinstance(estu2, Estudieante))
print(isinstance(estu2, Persona))
# [FIN] Sustitución entre clases

