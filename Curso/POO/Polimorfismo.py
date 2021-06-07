# Apartado 33 (Polimorfismo)
"""
Polimorfismo (poli => muchas / morfos: formas)
"""


class Estudiante:
    @staticmethod
    def describir(self):
        print("Soy un buen estudiant.")


class Docente:
    @staticmethod
    def describir(self):
        print("Me dedico a enseñar cursos.")


class Trabajador:
    @staticmethod
    def describir():
        print("Trabajo en una gran empresa.")


def describir_persona(persona):
    persona.describir()


est1 = Estudiante()
doc1 = Docente()
trab1 = Trabajador()

describir_persona(est1)
describir_persona(doc1)
describir_persona(trab1)