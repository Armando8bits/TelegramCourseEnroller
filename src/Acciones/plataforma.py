import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #para no estar descargando el chromedriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

import time

class udemy:
    def ProcesarCursos(df_cursos, usuario, contras):
        print("> ACCEDIENDO A SITIO WEB...")
        options = Options()
        options.add_argument("--incognito")
        # Adding argument to disable the AutomationControlled flag 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        # Exclude the collection of enable-automation switches 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # Turn-off userAutomationExtension 
        options.add_experimental_option("useAutomationExtension", False) 
        '''El perfil de Chrome "Incognito" no verifica los certificados SSL por defecto. Esta opción es más segura que la anterior,
    ya que el perfil de incognito no guarda cookies ni historial de navegación. en lugar de usar el argumento "--ignore-certificate-errors"
    al inicio de Chrome, lo que le indicará que ignore cualquier error relacionado con los certificados SSL. pero este último no es recomendado
    ya que una práctica insegura y no se recomienda, ya que expone su conexión a posibles ataques y robo de datos. '''     
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.maximize_window() #creo que es obvio lo que hace
        driver.get("https://www.udemy.com/")

        if udemy.iniciarSesion(driver, usuario, contras):
            print("> LOGGING EXITOSO")
        else:
            print("> ERROR AL INICIAR SESIÓN")

        input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script
        driver.quit()


        return
    
    def iniciarSesion(driver,usuari,passwd):
        time.sleep(4.1)
        WebDriverWait(driver,30)\
            .until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Iniciar sesión')]")))\
            .click()
        return True