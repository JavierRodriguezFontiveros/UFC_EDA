#Librerias:
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


#Función para obtener la nacionalidad desde Wikipedia:
def obtener_nacionalidad(luchador):
    url = f"https://es.wikipedia.org/wiki/{luchador.replace(' ', '_')}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return 'missingvalue'
    
    soup = bs(response.text, 'html.parser')
    
    try:
        infobox = soup.find('table', class_='infobox')
        if infobox is None:
            return 'missingvalue'
        
        for fila in infobox.find_all('tr'):
            if 'Nacionalidad' in fila.text:
                return fila.find('td').text.strip()
        
        return 'missingvalue'
    
    except AttributeError:
        return 'missingvalue'
    


#Función para obtener la nacionalidad de todos los luchadores:
def obtener_nacionalidades_luchadores(lista_luchadores):
    nacionalidad_dict = {}
    for luchador in lista_luchadores:
        nacionalidad_dict[luchador] = obtener_nacionalidad(luchador)
    return nacionalidad_dict



#Función para convertir el diccionario en un DataFrame:
def crear_dataframe_nacionalidades(nacionalidad_dict):
    df_nacionalidades = pd.DataFrame(list(nacionalidad_dict.items()), columns=['Luchador', 'Nacionalidad'])
    return df_nacionalidades



#Función para guardar el DataFrame en un CSV:
def guardar_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Archivo CSV '{filename}' generado exitosamente.")