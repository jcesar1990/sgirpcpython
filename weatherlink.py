import os
import time
from datetime import date, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import credenciales

def weatherlink(estacion,url):
     # Get date
    now=datetime.now()
    fecha=(now.strftime("%d-%m-%y"))
    print(fecha)

    # Paths
    filetxt = "C:/Users/meteorologia/Desktop/files/"+estacion+".txt"
    filecsv = "C:/Users/meteorologia/Desktop/files/"+estacion+".csv"
    urlogin="https://www.weatherlink.com"
    user=credenciales.User
    pwd=credenciales.Password
    print(user)

    # Selenium configuration
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-gpu")  # Necessary on some systems
    chrome_options.add_argument("--window-size=1920,1080")  # Window size
    driver_path = 'C:/Users/meteorologia/Documents/sgirpcpythonlinux/chromedriver-win64/chromedriver-win64/chromedriver.exe'
    service = ChromeService(executable_path=driver_path)

    # Create a Selenium WebDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)


    #time.sleep(5)

    # Access the page with Selenium
    driver.get(url)
    driver.find_element(By.XPATH,'//*[@id="username"]')\
        .send_keys(user)
    driver.find_element(By.XPATH,'//*[@id="password"]')\
        .send_keys(pwd)
    driver.find_element(By.XPATH,'//*[@id="submit"]')\
        .click()
    print("Acceso a la cuenta...")

    # Data query
    print(url)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="summary-view"]/i')\
        .click()
    time.sleep(5)



    # Wait for the element with XPATH get all content into the table
    data_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="scroll-container"]'))
    )

    # Print the content of the div
    print(data_container.text)

    # Save the data to the text file
    with open(filetxt, 'w', encoding='utf-8') as file:
        file.write(data_container.text)

    # print("Los datos se han guardado en el txt", filetxt)

    # Close the browser
    print("Datos de la estacion",estacion,"obtenidos")
    driver.quit()
