# Apartado 38 (Actualización de Datos en BD de MySQL)
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
        cursor.execute("""update tipo_usuario
                        set Nombre = 'Conserje',
                        Vigencia = 0
                        where Codigo = 5""")
        conexion.commit()  # Confirmamos la acción que estamos ejecutando.
        print("Registro actualizado con éxito.")
except Error as ex:
    print("Error durante la conexión:", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # Cerramos la conexión a la BD.
        print("La conexión ha finalizado.")
