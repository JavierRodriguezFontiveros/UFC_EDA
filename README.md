# Análisis Exploratorio: Métricas de la UFC

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9keJOlaq_Tc3s1l7GFltp6NDeKzz1wGCLhQ&s" alt="Análisis UFC"/>
</p>

## Descripción del Proyecto

Este proyecto de **Análisis Exploratorio de Datos (EDA)** se enfoca en desmitificar algunas de las preguntas más frecuentes planteadas por los *opinólogos de bar* 🍻 en el emocionante mundo de los deportes de contacto 🥋. 

Utilizando datos específicos de la **UFC**, hemos explorado diferentes hipótesis comúnmente discutidas, con el objetivo de ofrecer una **perspectiva clara y basada en datos** sobre lo que realmente influye en el éxito dentro de la jaula. 🏆

Los análisis han sido realizados a partir de **dos conjuntos de datos** 📊 encontrados en [Kaggle](https://www.kaggle.com/), complementados con técnicas de **Web Scraping** 🔍 para agregar información relevante adicional.

## Objetivo

El objetivo principal de este proyecto es proporcionar información basada en datos sobre las **características clave** que pueden influir en el éxito de un luchador dentro de la UFC. A través del análisis de estas variables, ofrecemos insights valiosos que pueden ayudar a determinar los **factores críticos** para llegar a ser campeón.

## Hipótesis Planteadas

A lo largo del análisis, se han planteado y resuelto las siguientes hipótesis, que representan algunos de los temas más debatidos sobre el rendimiento en la UFC:

1. [Relación entre la **Guardia** y el Éxito en la Carrera 🤼](#Guardia)
2. [**Probabilidad de Ganar** relacionada con una buena **Defensa de Derribo** 🥋](#Defensa)
3. [Impacto de la **Edad** en los enfrentamientos 👵👦](#Edad)
4. [¿Es más probable ganar por **KO** en divisiones de **peso pesado**? 💪⚖️](#KO's)
5. [Influencia de la **Altura y el Alcance** en los resultados 📏](#Altura)
6. [Países con más participantes en la **UFC** 🌍](#Mapamundi)



## Contenidos del Proyecto

- **Data Source:** Datasets extraídos de [Kaggle](https://www.kaggle.com/)
- **Librerías Utilizadas:**
  - `pandas` para la manipulación de datos
  - `matplotlib` y `seaborn` para visualización
  - `BeautifulSoup` para el Web Scraping de datos adicionales
- **Análisis Realizados:**
  - Exploración de las variables principales (guardia, defensa, edad, peso, altura)
  - Pruebas estadísticas para validar las hipótesis
  - Visualizaciones para facilitar la interpretación de los resultados

## Estructura del Proyecto

El análisis se organiza de la siguiente manera:

1. **Relación entre Guardia y Éxito:** Evaluamos si la postura de lucha (diestro o zurdo) tiene un impacto en la carrera de un luchador.
2. **Defensa de Derribo y Victoria:** Investigamos si una buena defensa contra los derribos aumenta las probabilidades de ganar.
3. **Edad vs Rendimiento:** Analizamos cómo la edad afecta el rendimiento de un luchador y su longevidad en el deporte.
4. **KO en Divisiones de Peso Pesado:** Estudiamos si los peleadores de peso pesado tienen más probabilidades de ganar por KO.
5. **Altura y Alcance:** Exploramos cómo la altura y el alcance de un luchador influyen en sus posibilidades de éxito.
6. **Participación por País:** Presentamos un mapa que muestra la distribución de los participantes de la UFC por país.

## Resultados y Conclusiones

Al final del proyecto, esperamos ofrecer una **visión clara y basada en datos** de los factores más influyentes en el éxito dentro de la UFC. Estas conclusiones pueden servir tanto para fanáticos del deporte como para aquellos interesados en análisis estadísticos de competiciones deportivas.



## Lenguajes y Librerías Utilizadas

En este proyecto, se han utilizado los siguientes lenguajes de programación y librerías:

### Lenguajes:
- `Python`: Para todo el análisis de datos, scraping y visualización.
- `HTML`: Para la visualizacion del mapa_mundi y visualizaciones en el notebook.
- `Markdown`: Para la estructuración y documentación del proyecto.

### Librerías:
- `pandas` para la manipulación y análisis de los datos.
- `numpy` para operaciones matemáticas y manejo de matrices.
- `requests` para hacer solicitudes HTTP y obtener datos adicionales mediante Web Scraping.
- `BeautifulSoup` para la extracción de datos de páginas web.
- `seaborn` y `matplotlib` para visualización de datos.
- `warnings` para manejar las advertencias y mejorar la legibilidad del código.



## Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/ufc-analysis.git
   cd ufc-analysis

2. **Instala las dependencias**:
   ```bash
    pip install -r requirements.txt

3. **Ejecuta el análisis**: 
    ```bash
    Abre el archivo ufc_notebook.ipynb con Jupyter Notebook o ejecuta el script principal para comenzar a explorar los datos.
