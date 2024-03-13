import os
import json
import requests
import urllib, urllib3
import csv
from datetime import date, datetime



def conagua(parametro):

    urltemp = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getTemperatura.php?per=T30'
    urlpre = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getPrecipitacion.php?per=B30'
    urlwind = 'https://smn.conagua.gob.mx/tools/GUI/sivea_v3/php/getViento.php?per=T30'
    file = 'C:/Users/meteorologia/Desktop/files/CONAGUA'+parametro+'.json'
    filecsv =  'C:/Users/meteorologia/Desktop/files/CONAGUA'+parametro+'.csv'
    
    if parametro == 'temperatura':
        url=urltemp
    elif parametro == 'velocidad':
        url=urlwind
    elif parametro == 'precipitacion':
        url=urlpre
    
    print(url)

    #Descarga del json del portal de CONAGUA
    r = urllib.request.urlopen(url)
    f = open(file,'wb')
    f.write(r.read())
    f.close()
    print(file)
    print('JSON de CONAGUA obtenido')

    def extraer_variables(file):
        with open(file) as contenido:
            variables = json.load(contenido)
            for valores in variables:
                fechalocal=(valores.get("fecha_local"))
                estado=(valores.get("estado")) 
                estacion=(valores.get("nombre_estacion"))
                temperatura=(valores.get(parametro))
                longitud=(valores.get("longitud"))
                latitud=(valores.get("latitud"))
                extraccion=(f"{fechalocal},{estado},{estacion},{temperatura},{longitud},{latitud}")
                print(extraccion)
                #Si el archivo csv no existe, lo crea, en caso de existir, conctatenara los nuevos datos
                if not os.path.exists(filecsv):
                    with open(filecsv,'w',newline='') as csvfile:
                        csv_writer=csv.writer(csvfile)
                        csv_writer.writerow(['fecha', 'localidad', 'estacion', parametro, 'longitud', 'latitud'])
                        csv_writer.writerow([fechalocal, estado, estacion, temperatura, longitud, latitud])
                    print('Archivo guardado')
                else:
                    with open(filecsv, 'a', newline='') as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow([fechalocal, estado, estacion, temperatura, longitud, latitud])
                    print('Datos añadidos al archivo existente')
                
                    
    extraer_variables(file)

test1=conagua("temperatura")
test2=conagua("precipitacion")
test3=conagua("velocidad")