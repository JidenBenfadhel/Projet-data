import folium, pandas as pd, numpy as np

def generate_map():
    """Génère la carte des villes de France selon leur nombre de naissance"""

    map = folium.Map(location=(48.7453229,2.5073644), tiles='OpenStreetMap', zoom_start=9)

    birth_data = pd.read_csv("data/cleaned/DS_ETAT_CIVIL_NAIS_COMMUNES.csv")
    birth_data[birth_data.columns[-1]] = np.log10(birth_data[birth_data.columns[-1]] + 1)
    folium.Choropleth(
        geo_data="data/geo/communes-50m.geojson",
        name='choropleth',
        data=birth_data,
        columns=['GEO', birth_data.columns[-1]],
        key_on='feature.properties.code',
        fill_color='Reds',
        fill_opacity=0.7,
        line_weight=0.1,
        legend_name='Naissance',
        nan_fill_color='white', # On "masque" les quelques villes manquantes
        nan_fill_opacity=0
    ).add_to(map)

    map.save("map.html")

generate_map()