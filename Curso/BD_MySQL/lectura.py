# Apartado 36 (Lectura de Datos en BD de MySQL)
import mysql.connector
from mysql.connector import Error

conexion = ''
try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='python_proyecto_apuntes'
    )

    if conexion.is_connected():
        print("Conexión extitosa.")
        cursor = conexion.cursor()
        cursor.execute("select database();")
        registro = cursor.fetchone()
        print("Conectado a la BD: ", registro)
        cursor.execute("select * from tipo_usuario;")
        resultados = cursor.fetchall()
        print("Código / Nombre / Vigencia")
        for fila in resultados:
            print("{0} / {1} / {2}".format(fila[0], fila[1], fila[2]))
        print("Total de registros: ", cursor.rowcount)
except Error as ex:
    print("Error durante la conexión:", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # Cerramos la conexión a la BD.
        print("La conexión ha finalizado.")
