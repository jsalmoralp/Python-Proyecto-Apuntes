# Apartado 25 (Clases con constructores)
# Apartado 26 (Encapsulamiento 1 - Propiedades)
# Apartado 27 (Encapsulamiento 2 - Métodos)
class Curso():
    # Estado inicial del objeto:
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"  # Propiedad encapsulada (inaccesible desde fuera de la clase).

    def mostrar_datos(self):
        dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docente_asignado = self.__verificar_docente()
        if docente_asignado:
            print("Existe docnte asigado.")
        else:
            print("No es necesario asignar un docente...")

    def __verificar_docente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False

####
# Clases con Constructor:
####
curso1 = Curso("Matemáticas", 5, "Ingeniería Civil")
print(curso1.nombre)

curso2 = Curso("Lenguas", 4, "Ingeniería Industrial")
print(curso2.nombre)

# [FIN] Clases con Constructor

####
# Encapsulamiento:
####
curso3 = Curso("Artes Plásticas", 5, "Ingeniería Artística")
print(curso3.nombre)
curso3.mostrar_datos()

# [FIN] Encapsulamiento
