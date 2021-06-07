def listar_cursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")


def pedir_datos_registro():
    codigo_correcto = False
    codigo = ''
    creditos = ''
    while not codigo_correcto:
        codigo = input("Ingrese código: ")
        if len(codigo) == 6:
            codigo_correcto = True
        else:
            print("Código incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    creditos_correcto = False
    while not creditos_correcto:
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if int(creditos) > 0:
                creditos_correcto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")

    curso = (codigo, nombre, creditos)
    return curso


def pedir_datos_actualizacion(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    creditos = ''
    codigo_editar = input("Ingrese el código del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigo_editar:
            existe_codigo = True
            break

    if existe_codigo:
        nombre = input("Ingrese nombre a modificar: ")

        creditos_correcto = False
        while not creditos_correcto:
            creditos = input("Ingrese créditos a modificar: ")
            if creditos.isnumeric():
                if int(creditos) > 0:
                    creditos_correcto = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("Créditos incorrectos: Debe ser un número únicamente.")

        curso = (codigo_editar, nombre, creditos)
    else:
        curso = None

    return curso


def pedir_datos_eliminacion(cursos):
    listar_cursos(cursos)
    existe_codigo = False
    codigo_eliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigo_eliminar:
            existe_codigo = True
            break

    if not existe_codigo:
        codigo_eliminar = ""

    return codigo_eliminar
