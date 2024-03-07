import os
import json
import requests
import urllib, urllib3

url = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getTemperatura.php?per=T30'
file = 'C:/Users/meteorologia/Desktop/files/CONAGUA.json'
csv =  'C:/Users/meteorologia/Desktop/files/CONAGUA.csv'
r = urllib.request.urlopen(url)
f = open(file,'wb')
f.write(r.read())
f.close()
print(file)
print('JSON de CONAGUA obtenido')

def leer_json(file):
    try:
        with open(file, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo {file} no se encontró.")
    except json.JSONDecodeError:
        print(f"No se pudo decodificar el JSON en {file}.")

indice = 0
datos_json = leer_json(file)
def extraer_nombres_variables(datos_json, variables, indice):
    nombres_extraidos = {}
    for variable in variables:
        try:
            valor = datos_json[indice][variable]
            nombres_extraidos[variable] = valor
        except KeyError:
            print(f"La variable '{variable}' no se encontró en el JSON.")
            return None  # Retorna None si no se encuentra una variable
        
    return nombres_extraidos

# Lista de variables que quieres extraer
variables_interesantes = ["fecha_local", "estacion_m", "nombre_estacion", "temperatura", "longitud", "latitud"]

while indice < len(datos_json):
    nombres_extraidos = extraer_nombres_variables(datos_json, variables_interesantes, indice)
    
    if nombres_extraidos:
        print("Nombres de variables extraídos:")
        print(nombres_extraidos)
        
        if not os.path.exists(csv):
            # Salvamos el acumulado en el archivo csvsave
            with open(csv,'w',newline='') as csvfile:
                # Creamos el arcicho
            
        
        # Incrementa el índice solo si la función se ejecutó con éxito
        indice += 1
    else:
        # Si no se encuentra una variable, termina el bucle
        break

print("Índice final:", indice)


