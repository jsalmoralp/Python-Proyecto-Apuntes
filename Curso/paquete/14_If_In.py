print("-- Cursos --")
print("Matemáticas - Biologia - Lenguas - Ciencias")

curso = input("Ingrese el curso deseado: ")

if curso in ("Matemáticas", "Biologia", "Lenguas", "Ciencias"):
    print("Curso {0} seleccionado".format(curso))
else:
    print("Este curso no existe...")
