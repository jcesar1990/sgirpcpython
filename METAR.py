import urllib.request
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import threading

def timer(timer_runs):
    while timer_runs.is_set():

        url="https://www.aviationweather.gov/metar/data?ids=mmmx&format=raw&date=&hours=48"
        filehtml= 'C:/Users/videowall_03/Documents/Estaciones/MMMX.txt'
        filein= 'C:/Users/videowall_03/Documents/Estaciones/MMMX.txt'
        fileout= 'C:/Apache24/htdocs/estacionesMet/files/MMMX.csv'

        #Peticion para compiar los datos del html del METAR
        
        r = requests.get(url)
        soup= BeautifulSoup(r.content, "html.parser")
        # tag=soup.find("code")
        # datos=tag.text
        # print(datos)

        r = urllib.request.urlopen(url)
        f = open(filehtml,'wb')
        f.write(r.read())
        f.close()
        #print(file1)
        print('Datos del html del METAR descargados')

        with open(filehtml,"r") as fr:
            contenido= fr.read()

        soup= BeautifulSoup(contenido,"html.parser")
        tags_code=soup.find_all("code")
        with open(filein,"w") as f:
            for etiqueta in tags_code:
                tags_content=etiqueta.text
                print(tags_content)
                f.write(tags_content + "\n")

        txt=open(filein)
        txt1=txt.read()
        #print(txt1)
        txt2=txt1.replace(" ",",")
        csv=open(fileout,"w")
        csv.write(txt2)
        txt.close()
        csv.close()

        final=datetime.now()
        print(final)
        time.sleep(1800)   # 10 minutos=600. Se le estaron un par de segundos del proceso.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
