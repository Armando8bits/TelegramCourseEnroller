from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

class Sesion:
    def iniciar(self, driver,usuari,passwd):
        parent_guid = driver.current_window_handle
        WebDriverWait(driver,30)\
            .until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-content-layout/div/app-header/header/nav/div/button/span')))\
            .click()

        all_guid = driver.window_handles # Get the window handle ids of all the windows opened
        # iterate through the guids and if there is a parent window id skip it and switch to the new window
        for guid in all_guid:
            if guid != parent_guid:
                driver.switch_to.window(guid)
                #print(f"The child guid is: {guid}") #no es necesario
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"i0116")))\
                    .send_keys(str(usuari))
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"idSIButton9"))).click()
                WebDriverWait(driver,30,2).until(EC.element_to_be_clickable((By.ID,"i0118")))\
                    .send_keys(str(passwd)) #el 3er parametro (2) signifia que cada seguno durnte los 30 va a verificar si ya se puede clikear, lo hice así para evitar errores, ya que por defecto lo hace pero por medio segundo
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"idSIButton9"))).click()
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"idBtn_Back"))).click()
                #time.sleep(5)
                #driver.close() #en este caso esta linea no es necesaria ya que la ventana se cierra sola
                break #por siacaso hay más ventanas, no perder tiempo

        driver.switch_to.window(parent_guid) #retorna a la ventana principal
        