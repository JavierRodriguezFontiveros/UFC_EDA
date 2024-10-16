
import Mapa_mundi_utils as mp

def main():
    
    numero_peladores_dict = {
        'Estados Unidos': {'Peleadores': 140, 'Cordenadas': [37.0902, -95.7129]},
        'Brasil': {'Peleadores': 70, 'Cordenadas': [-14.2350, -51.9253]},
        'Rusia': {'Peleadores': 32, 'Cordenadas': [61.5240, 105.3188]},
        'Inglaterra': {'Peleadores': 22, 'Cordenadas': [52.3555, -1.1743]},
        'México': {'Peleadores': 17, 'Cordenadas': [23.6345, -102.5528]},
        'Canadá': {'Peleadores': 17, 'Cordenadas': [56.1304, -106.3468]},
        'Australia': {'Peleadores': 13, 'Cordenadas': [-25.2744, 133.7751]},
        'España': {'Peleadores': 8, 'Cordenadas': [40.4637, -3.7492]},
        'Nueva Zelanda': {'Peleadores': 7, 'Cordenadas': [-40.9006, 174.8860]},
        'China': {'Peleadores': 7, 'Cordenadas': [35.8617, 104.1954]}
    }

    
    mapa = mp.crear_mapa(numero_peladores_dict)

    
    return mapa

# Ejecutar la función principal
if __name__ == "__main__":
    main()