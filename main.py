#from src.Acciones import login
from src.Acciones import credencial
from src.Acciones import funciones as func
#from login import Sesion
from src.Acciones import TelegramAPIConnector
import asyncio

#empezar carga desde mensaje 29343
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService #para no estar descargando el chromedriver
# from webdriver_manager.chrome import ChromeDriverManager

#if __name__ == "__main__":
if credencial.Credencial.EsValida(): #si las credenciales son validas, inicia
    #print(str(Credencial.GetUsuario())+" - "+str(Credencial.GetPasswor()))
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.maximize_window() #creo que es obvio lo que hace
    # driver.get("https://previexappdev.azurewebsites.net")

    #login.Sesion().iniciar(driver,credencial.Credencial.GetUsuario(),credencial.Credencial.GetPasswor()) #inicia los procesos comentados de abajo
    #contratoReg.Contrato().Registrar(driver)
    api_id=credencial.Credencial.GetApp_api_id()
    api_hash=credencial.Credencial.GetApp_api_hash()
    ChatTelegram=credencial.Credencial.GetAppChatTelegram()
    lista_cursos = asyncio.run( TelegramAPIConnector.Orquestador().GetMensajesCursos(api_id, api_hash, ChatTelegram))
    if len(lista_cursos)>0:
        x= func.GetDataOrga(lista_cursos)
    # input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script
    # driver.quit()

'''contrato=Contrato()
contrato.Registrar(driver)'''




