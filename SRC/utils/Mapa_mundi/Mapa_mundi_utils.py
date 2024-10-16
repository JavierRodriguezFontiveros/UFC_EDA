import folium
from folium.features import DivIcon

def crear_mapa(numero_peladores_dict):
    #Creando el mapa base:
    mapa_mundi = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodb positron')

    #Añadiendo círculos y marcadores para cada país en el diccionario:
    for idx, (pais, info) in enumerate(numero_peladores_dict.items(), 1): 
        Cordenadas = info['Cordenadas']
        Peleadores = info['Peleadores']

        #Defininiendo el color en función del índice
        color = 'green' if idx <= 3 else 'red'

        #Creando un marcador circular en el mapa
        folium.CircleMarker(location=Cordenadas,
                            radius=Peleadores / 2,                         
                            popup=f'{pais}: {Peleadores} peleadores',
                            color=color,
                            fill=True,
                            fill_color=color,
                            fill_opacity=0.7).add_to(mapa_mundi)

        #Añadiendo un marcador con el índice del país
        folium.Marker(location=Cordenadas,
                      icon=DivIcon(icon_size=(12, 12), 
                                   icon_anchor=(6, 6),
                                   html=f'<div style="font-size: 12px; color: black;">{idx}</div>',)).add_to(mapa_mundi)

    #Creando una leyenda
    legend_html = '''
    <div style="
        position: fixed;
        bottom: 50px; left: 50px; width: 250px; height: 275px;
        border:2px solid grey; z-index:9999; font-size:14px;
        background-color:white; padding: 10px;">
        <h2>Países y Peleadores</h2>
        <ol>
            &nbsp
            <li><b>Estados Unidos</b> - 349 </li>
            <li><b>Brasil</b> - 87 </li>
            <li><b>Rusia</b> - 32 </li>
            <li><b>Inglaterra</b> - 22 </li>
            <li><b>México</b> - 17 </li>
            <li><b>Canadá</b>- 17 </li>
            <li><b>Australia</b> - 13 </li>
            <li><b>España</b> - 8 </li>
            <li><b>Nueva Zelanda</b> - 7 </li>
            <li><b>China</b> - 7 </li>
        </ol>
    </div>
    '''

    #Añadiendo la leyenda al mapa
    mapa_mundi.get_root().html.add_child(folium.Element(legend_html))

    #Guardando el mapa en un archivo HTML
    mapa_mundi.save("mapa_mundi.html")

    return mapa_mundi

