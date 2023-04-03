from asyncore import read
from os import close, remove, write
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
import pandas as pd
import numpy as np
from os import remove
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        espacio='-------------'

        print(espacio)
        print("Descargando datos de SIMAT")

        try:
            url1 = 'http://189.204.131.110:8002/webserviceSIMAT.asmx/Alerta_Temprana'
            file1 = r'C:\Apache24\htdocs\estacionesMet\files\simat.txt' 
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'MyApp/1.0')] 
            urllib.request.install_opener(opener)
            r = urllib.request.urlopen(url1)
            f = open(file1,'wb')
            f.write(r.read())
            f.close()
            print("Datos de calidad del aire obtenidos")
            #print(file1)
        except:
            print("Ha ocurrido un error con la descarga del archivo")

        final=datetime.now()
        print(final)
        time.sleep(590)   # 10 minutos=600.Se le estaron un par de segundos del proceso.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()