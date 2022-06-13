
from selenium import webdriver
import time

import csv
import os.path

#Automatizacion descarga de archivo Dane
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location='C:/Program Files/Google/Chrome/Application/chrome.exe'
driver = webdriver.Chrome('./chromedriver_win32_102/chromedriver.exe',chrome_options=options)

def descarga_dane(driver):
    driver.get('http://www.dane.gov.co/files/investigaciones/boletines/exportaciones/boletin_exportaciones_abr22.pdf')
    time.sleep(4)
    driver.quit()

descarga_dane(driver)
