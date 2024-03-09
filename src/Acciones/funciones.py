import pandas as pd

def GetDataOrga(lista_cursos):
    df = pd.DataFrame()
    IdCurso=[]
    NombreCurso=[]
    linkCurso=[]

    for message_obj in lista_cursos: 
        objectStr=str(message_obj)

        if "text=\'Ver\'" in objectStr : #busca "text='Ver'" ya que en la conversion a str se cambi algo
            #si entra aqui es x que es un curso gratis

            # obtiene enlace de Udemy
            start_index = objectStr.find('udemy.com')
            if start_index != -1:
                end_index = end_index = objectStr.find("\'", start_index)
                if end_index != -1:
                    udemy_link = objectStr[start_index:end_index]
                    #crea lista con los elementos
                    if(len(str(message_obj.id))>0 and len(str(message_obj.message))>0):
                        linkCurso.append(udemy_link)
                        print(udemy_link)
                        IdCurso.append(message_obj.id) # Obtener el ID del mensaje
                        NombreCurso.append(message_obj.message) #totulo del curso
    # crea el dataframe
    df = pd.DataFrame({'ID': IdCurso,
                    'Titulo': NombreCurso,
                    'Enlace': linkCurso     })
        
    print(df)

    return df



