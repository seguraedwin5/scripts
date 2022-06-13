
from selenium import webdriver
import time

import csv
import os.path

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.binary_location='C:/Program Files/Google/Chrome/Application/chrome.exe'
driver = webdriver.Chrome('./chromedriver_win32_102/chromedriver.exe',chrome_options=options)

#Abrir netflix y realizar login (la version de chrome utilizada es la 102, puede afectar en el funcionamiento de la automatizacion)
def inicioNetflix(chrome_driver):
    chrome_driver.get('https://www.netflix.com/co/')
    time.sleep(3)

    #se debe utilizar el xpath del botón ya que no tienen un id definido
    btn_inciarsesion = chrome_driver.find_element( by= 'xpath', value='//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
    btn_inciarsesion.click()
    time.sleep(1)
    campo_login = chrome_driver.find_element(by='id',value ='id_userLoginId')
    campo_pwd = chrome_driver.find_element(by='id', value='id_password')
    campo_login.send_keys('seguraedwin5@gmail.com')
    campo_pwd.send_keys('Edwin.0000')
    btn_inciarsesion = chrome_driver.find_element(by='xpath', value ='//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    btn_inciarsesion.click()
    time.sleep(5)
    chrome_driver.quit()
    

def loadtest(chrome_driver:driver):
    #configurar ruta de archivo
    ruta = './loadtest'
    archivo_registros = 'registros.csv'
    iteraciones = 50
    ruta_completa =  os.path.join(ruta,archivo_registros)
    try:
        file =open(ruta_completa,'w',newline='') 
        writer = csv.writer(file)
        writer.writerow(['calculo_perf_backend','calculo_perf_frontend'])
    except Exception as ex:
        print(f"exception: {ex}")
    
    for i in range(iteraciones):
        chrome_driver.get('https://www.netflix.com/co')
        
        navigationStart = chrome_driver.execute_script("return window.performance.timing.navigationStart")#inicio navegacion
        responseStart = chrome_driver.execute_script("return window.performance.timing.responseStart")#tiempo de respuesta
        domComplete = chrome_driver.execute_script("return window.performance.timing.domComplete")#tiempo de carga pagina completa
        calc_backend= responseStart - navigationStart
        calc_frontend = domComplete - responseStart
        #escribir resultados en archivo

        writer.writerow([calc_backend,calc_frontend])
        chrome_driver.close()
        time.sleep(4)


inicioNetflix(driver)
#loadtest(driver) 

