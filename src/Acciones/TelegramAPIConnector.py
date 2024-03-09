from telethon import TelegramClient
import os


class Orquestador:
    async def GetMensajesCursos(self, App_api_id, App_api_hash, ChatTelegram):
        ID_chat=None
        lastMessage=None
        parametros={}
        mensajes = []
        LIMITE=5
        print("> INICIANDO CONECCIÓN CON API DE TELEGRAM...")
        client = TelegramClient('anon', App_api_id, App_api_hash)
        await client.start()
        me = await client.get_me()
        async for dialog in client.iter_dialogs():
            if ChatTelegram == dialog.name:
                print(dialog.name, 'TIENE ID: ', dialog.id)
                ID_chat=dialog.id
                break

        await client.disconnect() #cierra cesión
        #print(ChatTelegram)
        #print(ID_chat)
        if ID_chat is not None:
            #print("puedes continuar")
            #verifica si hay registro del ultimo mensaje leido
            IdInicial = self.loadIdMessage()

            if IdInicial is None:
                #parametros["channel_id"] = ID_chat
                parametros["limit"] = LIMITE
                parametros["reverse"] = True
                print("> NO SE ENCONTRÓ ARCHIVO 'log.tce' SE LEERAN LOS ÚLTIMOS {} MENSAJES",str(LIMITE))
            else:
                #parametros["channel_id"] = ID_chat
                parametros["offset_id"] = IdInicial
                parametros["reverse"] = True
                print("> SE CARGARÁN MENSAJES DESDE: "+str(IdInicial))

            # Obtiene los mensajes no leídos del chat
            async for message in client.iter_messages(ID_chat, **parametros):
                mensajes.append(message)
                lastMessage=message.id

            print("> CARGA DE MENSAJES COMPLETA")
            
            if lastMessage is not None: self.saveIdMessage(lastMessage)

            #for item in mensajes: 
             #   print(item)
        return mensajes

    def saveIdMessage(self, ID):
        with open("log.tce", "w") as archivo:
            archivo.write(str(ID))

    def loadIdMessage(self):
        idBuscado=None
        if os.path.exists("log.tce"):
            #print("encontrè el archivo")
            with open("log.tce", "r") as archivo:
                idBuscado = int(archivo.read())
            #print("guardé el numero"+str(idBuscado))
            if idBuscado<=0: idBuscado=None
                #print("ya valiò madres")
        return idBuscado
