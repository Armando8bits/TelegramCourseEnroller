from src.Acciones import credencial
from src.Acciones import funciones as func
from src.Acciones import plataforma
from src.Acciones import TelegramAPIConnector
import asyncio

#empezar carga desde mensaje 29343

if credencial.Credencial.EsValida(): #si las credenciales son validas, inicia

    usuario=credencial.Credencial.GetUsuario()
    contras=credencial.Credencial.GetPasswor()
    '''
    api_id=credencial.Credencial.GetApp_api_id()
    api_hash=credencial.Credencial.GetApp_api_hash()
    ChatTelegram=credencial.Credencial.GetAppChatTelegram()
    lista_cursos = asyncio.run( TelegramAPIConnector.Orquestador().GetMensajesCursos(api_id, api_hash, ChatTelegram))
    if len(lista_cursos)>0:
        dataCurso, confirmacion = func.GetDataOrga(lista_cursos)
        if confirmacion:
            plataforma.udemy.ProcesarCursos(dataCurso, usuario, contras) '''

    dataCurso="" #esta linea es ara que funcionara con lo comentado de arriba
    plataforma.udemy.ProcesarCursos(dataCurso, usuario, contras) # para probar 
    # input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script
    # driver.quit()




