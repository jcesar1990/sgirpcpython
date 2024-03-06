import os
import json
import requests
import urllib, urllib3

url = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getTemperatura.php?per=T30'
file = 'C:/Users/jclm1/Documents/SGIRPC/datos/CONAGUA.json'
# r = urllib.request.urlopen(url)
# f = open(file,'wb')
# f.write(r.read())
# f.close()
# print(file)
# print('JSON de CONAGUA obtenido')

def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except json.JSONDecodeError:
        print(f"No se pudo decodificar el JSON en {nombre_archivo}.")

def extraer_nombres_variables(datos_json, variables):
    nombres_extraidos = {}
    for variable in variables:
        try:
            # Aquí, accedemos al primer elemento de la lista (índice 0)
            # y luego a la variable específica dentro del diccionario.
            valor = datos_json[5][variable]
            nombres_extraidos[variable] = valor
        except KeyError:
            print(f"La variable '{variable}' no se encontró en el JSON.")
    
    return nombres_extraidos

# Variables para las funciones
nombre_archivo = file
datos_json = leer_json(nombre_archivo)

# Lista de variables que quieres extraer
variables_interesantes = ["fecha_local", "estacion_m", "nombre_estacion", "temperatura","longitud","latitud"]

if datos_json:
    nombres_extraidos = extraer_nombres_variables(datos_json, variables_interesantes)
    
    if nombres_extraidos:
        print("Nombres de variables extraídos:")
        print(nombres_extraidos)
