from os import close, remove, write
import os
import time  
from datetime import date, datetime, timedelta
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove
espacio="-------------"
now = datetime.now()
fecha= date.today()
print(espacio)
"""date"""
fecha_temperaturas=fecha
#print(fecha_temperaturas)
print(espacio)
fecha_lluvias=fecha - timedelta(days=1)
print(espacio)
#print(fecha_lluvias)

fechaHora='19 March, 2024 / 20:17'

format_temp = fecha_temperaturas.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format_temp)


format_lluvia = fecha_lluvias.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format_lluvia)

def current_date_format(date):
    months = ("Junuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    day = date.strftime("%d")
    month = months[date.month - 1]
    year = date.year
    messsage = "{} - {} - {}".format(day, month, year)

    return messsage

fecha_temperaturas=fecha
fecha_final_temperaturas=(current_date_format(fecha_temperaturas))
print(fecha_final_temperaturas)

