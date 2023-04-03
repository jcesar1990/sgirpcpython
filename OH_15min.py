from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import requests
import urllib.request
import pandas as pd
import numpy as np
from os import remove
import threading

def timer(timer_runs):
    while timer_runs.is_set():

        espacio='-------------'

        # Insertamos la fecha
        now=datetime.now()
        fecha=(now.strftime("%d/%m/%y %H:%M"))
        print(fecha)

        #Se buscan los datos en la web por medio de un request, así mismo se guarda en un csv
        print("OH")
        print(espacio)
        urlOH='https://www.oh-iiunam.mx/geojson/datospaginaquince.txt'
        fileOH = 'C:/Apache24/htdocs/estacionesMet/files/OH.csv'
        try:  
            r = urllib.request.urlopen(urlOH)
            f = open(fileOH,'wb')
            f.write(r.read())
            f.close()
            print('Datos de OH obtenidos')
        except:
            print("Se produjo un error al momento de descargar los datos")

        # Se hacen algunos cambios dentro del archivo para darle el formato correspondiente al csv y que la libreria pandas lo pueda leer correctamente
        oh=open(fileOH)
        texto=oh.read()
        texto1=texto.replace(" ", ",")
        #print(texto1)
        oh1=open(fileOH,"w")
        oh1.write(texto1)
        oh.close()
        oh1.close()

        # Este paso de lectura y guardado solo fue para asignar un indice de forma automatica
        oh=pd.read_csv(fileOH, index_col=False, header=None)
        oh.to_csv(fileOH)

        # Se renombran las columnas con ls claves requeridas
        oh=pd.read_csv(fileOH, index_col=0, header=0)
        texto1=oh.rename({'2': 'idEstacion'}, axis=1)
        texto2=texto1.rename({'3': 'lluvia'}, axis=1)
        #print(texto2)
        texto2.to_csv(fileOH)

        # Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
        OH = pd.read_csv(fileOH, index_col=0, header=0, usecols=(3,4))
        #print(OH)
        roundplaces = np.round(OH,decimals=2)
        roundplaces.to_csv(fileOH)
        print('Datos de OH obtenidos')


        # Ordenamos las estaciones alfabeticamente 
        oh=pd.read_csv(fileOH, index_col=0, header=0) 
        by_name = oh.sort_values('idEstacion')
        by_name.head()
        #print(by_name)
        by_name.to_csv(fileOH)

        # Leemos los archivos csv como dataframes

        oh=pd.read_csv(fileOH, index_col=False)
        oh['fechaHora']=np.where(oh['lluvia'] !='[]', fecha, ' ', )
        #print(oh)
        oh.to_csv(fileOH)

        oh=pd.read_csv(fileOH, usecols=(1, 2, 3), index_col=0, header=0) 
        print(oh)
        oh.to_csv(fileOH)

        final=datetime.now()
        print(final)
        time.sleep(870)   # 15 minutos=900.Se le estaron un par de segundos del proceso.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()