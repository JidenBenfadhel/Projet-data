import folium, pandas as pd

map = folium.Map(location=(48.7453229,2.5073644), tiles='OpenStreetMap', zoom_start=9)

birth_data = pd.read_csv("data/cleaned/DS_ETAT_CIVIL_NAIS_COMMUNES.csv")



folium.Choropleth(
    geo_data="data/geo/communes-50m.geojson",
    name='choropleth',
    data=birth_data,
    columns=['GEO', birth_data.columns[-1]],
    key_on='feature.properties.code',
    fill_color='PuBu',
    fill_opacity=0.7,
    line_weight=1,
    legend_name='Naissance',
    nan_fill_color='white',
    nan_fill_opacity=0.1
).add_to(map)

map.save("map.html")