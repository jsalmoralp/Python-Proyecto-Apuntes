import datetime
# from datetime import datetime

fecha_actual = datetime.datetime.now()
# fechaActual = datetime.now()  # Esto con el segudo import
print(fecha_actual)

fecha_premake = datetime.datetime(2020, 11, 5)
print(fecha_premake)
fecha_premake2 = datetime.datetime(2020, 11, 5, 10, 35, 21)
print(fecha_premake2)


fecha_personalizada = datetime.datetime.strftime(fecha_actual, '%d/%m/%Y %H:%M:%S')
print(fecha_personalizada)

fecha_personalizada2 = datetime.datetime.strftime(fecha_actual, '%b %d %Y %H:%M:%S')
print(fecha_personalizada2)
# https://strftime.org/

fecha_texto = 'Dec 06 2020 12:56:11'
fecha_a_formato_datetime = datetime.datetime.strptime(fecha_texto, '%b %d %Y %H:%M:%S')
print(fecha_a_formato_datetime)

dia = datetime.datetime.strftime(fecha_actual, '%d')
print(dia)
dia_en_int = int(datetime.datetime.strftime(fecha_actual, '%d'))
print(dia_en_int)

hora_actual = datetime.datetime.strftime(fecha_actual, '%H:%M:%S')
print(hora_actual)


fecha_pasada = datetime.datetime(2020, 10, 23)
diferencia = fecha_actual - fecha_pasada
print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())


dia_delta = datetime.timedelta(days=-5)
fecha_inicial = datetime.date.today()
print(fecha_inicial)
fechaFutura = fecha_inicial + dia_delta
print(fechaFutura)


fecha_iso = datetime.datetime.now().isoformat()
print(fecha_iso)
