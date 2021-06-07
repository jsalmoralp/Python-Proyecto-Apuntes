# Apartado 35 (Conexion a BD de MySQL)
"""
Comandos para la instalación:
-$ pipenv install
-$ pipenv install mysql-connector-python
"""
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
        infoServer = conexion.get_server_info()
        print("Info del servidor:", infoServer)
except Error as ex:
    print("Error durante la conexión:", ex)
finally:
    if conexion.is_connected():
        conexion.close()  # Cerramos la conexión a la BD.
        print("La conexión ha finalizado.")
