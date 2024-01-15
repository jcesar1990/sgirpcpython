import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# Function to create directories
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio " + path + " ha sido creado")
    else:
        print("El directorio " + path + " ya existe")

# Directories
pathestaciones = "../estaciones"
pathfiles = "../files"

makedir(pathestaciones)
makedir(pathfiles)

# URLs and file paths
url = "https://aviationweather.gov/data/metar/?id=MMMX&hours=48&include_taf=yes"
fileout = "../files/MMMX.txt"

# Selenium configuration
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")  # Necessary on some systems
chrome_options.add_argument("--window-size=1920,1080")  # Window size
driver_path = 'C:/Users/meteorologia/Documents/sgirpcpythonlinux/chromedriver-win64/chromedriver-win64/chromedriver.exe'
service = ChromeService(executable_path=driver_path)

# Create a Selenium WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Access the page with Selenium
driver.get(url)
print("Acceso a la página...")
driver.find_element(By.XPATH,'//*[@id="main-display"]/div[2]/div[4]/div[1]/label')\
    .click()
print("Deseleccionamos TAF")
driver.find_element(By.XPATH,'//*[@id="go_btn"]')\
    .click()
print("Load data")
time.sleep(5)


# Wait for the element with id "data-container" to be present in the DOM
data_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'data-container'))
)

# Print the content of the div
print(data_container.text)

# Save the data to the text file
with open(fileout, 'w', encoding='utf-8') as file:
    file.write(data_container.text)

print("Los datos se han guardado en el txt", fileout)

# Close the browser
driver.quit()