import pandas as pd

# Lecture du .csv des données
data = pd.read_csv("data/raw/DS_ETAT_CIVIL_NAIS_COMMUNES_data.csv",
                   sep=";",
                   dtype={"GEO": str}
                   )

# Lecture du .csv des métadonnées
metadata = pd.read_csv("data/raw/DS_ETAT_CIVIL_NAIS_COMMUNES_metadata.csv",
                       sep=";",
                       dtype={"COD_MOD": str}
                       )

# Récupère seulement les données concernant les villes et les arrondissements des grandes villes (Paris, Lyon, Marseille)
data = data.query('GEO_OBJECT == "COM" or GEO_OBJECT == "ARM"')

# Ajout d'une colonne pour avoir le libéllé associé au code INSEE
data = data[["GEO", "TIME_PERIOD", "OBS_VALUE"]].merge(
    metadata[["COD_MOD","LIB_MOD"]],
    left_on="GEO",
    right_on="COD_MOD"
)

# Suppression de la colonne COD_MOD car doublon avec la colonne GEO
data = data.drop(columns=["COD_MOD"])

# On retire Paris Lyon et Marseille pour garder seulement leurs arrondissements 
data = data.query('GEO != "75056" and GEO != "69123" and GEO != "13055" and ' \
                  'GEO != "751XX" and GEO != "693XX" and GEO != "132XX"') # Arrondissement inconnu

# Transformation en tableau croisé dynamique pour avoir en colonne les années et en ligne les villes/arrondissements
data = data.pivot_table(
    index=["GEO", "LIB_MOD"],
    columns="TIME_PERIOD",
    values="OBS_VALUE",
    fill_value=0
)

# On enregistre le DataFrame en .csv en triant par code INSEE croissant pour une meilleure lisibilité
data.sort_values("GEO").to_csv("data/cleaned/DS_ETAT_CIVIL_NAIS_COMMUNES.csv")

print(data.sort_values(by=2024, ascending=False))