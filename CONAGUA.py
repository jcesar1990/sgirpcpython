#Importamos librerias
import ModuloCONAGUA
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

        #ModuloCONAGUA.proceso("TACUBAYA","TACUBAYA")   

        ModuloCONAGUA.proceso("ECOGUARDAS","ECOGUARDAS")

        ModuloCONAGUA.proceso("TEZONTLE","TEZONTLE")

        ModuloCONAGUA.proceso("CERROCATEDRAL","ISI")

        ModuloCONAGUA.proceso("ALTZOMONI","ALTZOMONI")

        ModuloCONAGUA.proceso("PRESAMADINSMN","NAU")

        ModuloCONAGUA.proceso("ESCNALCIENCIASBIOLOGICAS","ENCB")

        time.sleep(570)   # 10 minutos=600.Se le estaron un par de segundos del proceso.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()