import os
import dotenv

class Credencial:
    usuari=""
    passwd=""
    App_api_id=""
    App_api_hash=""
    ChatTelegram=""

    @classmethod
    def EsValida(cls):
        BoolEstado=True
        dotenv.load_dotenv()  # cargamos las variables de entorno
        cls.usuari = (os.getenv('usuar')) # leemos las varaibles de entorno
        cls.passwd = (os.getenv('passw'))
        cls.App_api_id = (os.getenv('App_api_id'))
        cls.App_api_hash = (os.getenv('App_api_hash'))
        cls.ChatTelegram = (os.getenv('ChatTelegram'))
        if (cls.usuari is None or cls.passwd is None or cls.App_api_id is None or cls.App_api_hash is None or cls.ChatTelegram is None):
            print("***CREDENCIALES INVALIDAS o INEXISTENTES")
            BoolEstado=False
        return BoolEstado
    
    @classmethod
    def GetUsuario(cls):
        return cls.usuari
    
    @classmethod
    def GetPasswor(cls):
        return cls.passwd
    
    @classmethod
    def GetApp_api_id(cls):
        return cls.App_api_id
    
    @classmethod
    def GetApp_api_hash(cls):
        return cls.App_api_hash
    
    @classmethod
    def GetAppChatTelegram(cls):
        return cls.ChatTelegram
