import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

#Creamos las carpetas donde se alojaran los datos
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio "+path+" ha sido creado")
    else:
        print("El directorio "+path+" ya existe")

pathestaciones="../estaciones"  
pathfiles="../files"

makedir(pathestaciones)
makedir(pathfiles)

url="https://aviationweather.gov/data/metar/?id=MMMX&hours=48&include_taf=yes"
filehtml= '../estaciones/MMMX.txt'
filein= '../estaciones/MMMX.txt'
fileout= '../files/MMMX.txt'

# #Peticion para compiar los datos del html del METAR usando request y beautifulsoupS
# try:
#     # Se realiza la solicitud
#     response = requests.get(url)
#     # Verificando la respuesta a la solicitud
#     if response.status_code == 200:
#         # Obteniendo contenido del html
#         html_content = response.text
#         soup= BeautifulSoup(html_content, "html.parser")
#         data_container = soup.find('div',{'id':'data-container'})
#         #Si existe el div
#         if data_container:
#              print(data_container.text)
#         print(data_container)
#         print("El proceso se completo con exito")
#     else:
#          print("Algo fallo")
# except KeyError as e:
#         print(f"Se presento un error. Detalles del error: {e}")

# Configuración de Selenium
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")  # Necesario en algunos sistemas
chrome_options.add_argument("--window-size=1920,1080")  # Tamaño de ventana
driver_path =  'C:/Users/meteorologia/Documents/sgirpcpythonlinux/chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = ChromeService(executable_path=driver_path)

# Crear una instancia de Selenium WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
#driver=webdriver.Chrome(service=Service(executable_path=driver_path),chrome_options=chrome_options)

# Acceder a la página con Selenium
driver.get(url)

# Esperar a que el elemento con id "data-container" esté presente en el DOM
data_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'data-container'))
)

# Imprimir el contenido del div
print(data_container.text)

# Cerrar el navegador
driver.quit()
