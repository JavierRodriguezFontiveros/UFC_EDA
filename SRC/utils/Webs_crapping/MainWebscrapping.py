import Webscrapping as webs

# Función principal que engloba todo el flujo
def main(df_1):
    lista_luchadores = list(df_1["Nombre"].values)
    nacionalidad_dict = webs.obtener_nacionalidades_luchadores(lista_luchadores)
    df_nacionalidades = webs.crear_dataframe_nacionalidades(nacionalidad_dict)
    webs.guardar_csv(df_nacionalidades, 'nacionalidades_luchadores.csv')

# Ejecutar el proceso
# main(df_1)
