from unidecode import unidecode
import pandas as pd
import os

def GetDataOrga(lista_cursos):
    df = pd.DataFrame()
    IdCurso=[]
    NombreCurso=[]
    linkCurso=[]
    procesarDf=False

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
                        #print(udemy_link)
                        IdCurso.append(message_obj.id) # Obtener el ID del mensaje
                        NombreCurso.append(message_obj.message) #totulo del curso
                        procesarDf=True
    # crea el dataframe
    df = pd.DataFrame({'ID': IdCurso,
                    'TITULO': NombreCurso,
                    'ENLACE': linkCurso     })
        
    #print(df)
    if procesarDf==True: depurar(df)

    return df

def depurar(df):
    filas_coincidentes = []
    temas_no_interes = []
    if existPreferences():
        temas_no_interes = ReadPreferences()
    else:
        crearFilePreferences()
        temas_no_interes = ReadPreferences()

    for index, row in df.iterrows():
        titulo = unidecode(row['TITULO'].lower()) #quita caracteres raros y hace minuscula
        if any(tema in titulo for tema in temas_no_interes):
        # Si hay una coincidencia, agregar el índice de la fila a la lista
            filas_coincidentes.append(index)
    # Marcar con 1 las filas que contienen coincidencias
    df.loc[filas_coincidentes, 'NO_ES_DIGNO'] = 1
    #print(df)
    return df

def ReadPreferences():
    temas_no_interes = []
    with open("temas_no_interes.txt", "r") as file:
        for linea in file:
            # Eliminar los saltos de línea (\n) y espacios en blanco al inicio y al final de la línea
            linea = linea.strip()
            # Omitir las líneas vacías y las que empiezan con "--"
            if linea and not linea.startswith("--"):
                linea = unidecode(linea) #caracteres acentuados y especiales por sus equivalentes sin acentos
                temas_no_interes.append(linea.lower())
    #print(temas_no_interes)
    return temas_no_interes

def existPreferences():
    return os.path.exists("temas_no_interes.txt")

def crearFilePreferences():
    with open("temas_no_interes.txt", "w") as archivo:
            archivo.write("--Esto es un comentario\n--Puedes escribir los comentarios que necesites\n--Siempre que empiecen con dos guiones\n--escribe cada tema que no te interece en cada linea, por ejemplo:\ntarot\nprogramación neurolingüística")





