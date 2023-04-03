import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import threading

def timer(timer_runs):
    while timer_runs.is_set():
        espacio='-------------'

        try:
            # Se instala de forma automatica el controlador de chrome,
            # de igual manera de establece el parametro de visualización de la pantalla y establece la dirección web
            inicio=datetime.now()
            print(inicio)
            driver=webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get('http://192.168.20.17:8080/estacionesMet/control/cargaSgirpc.php')
            driver.implicitly_wait(50)
            time.sleep(5)
            driver.close()

            print("Se han abierto la pestaña cargaSgirpc.php en el navegador de Chrome para la carga de datos en la base SQL")
        except:
            print("No se logro la carga de datos en la base SQL debido a algún fallo, revise la conexión a internet o el programa cargaSgirpc.php ")

        final=datetime.now()
        print(final)
        time.sleep(570)   # 10 minutos=600.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()