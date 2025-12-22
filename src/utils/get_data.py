import zipfile
import requests
import os

def get_data():
    """Récupère les données .csv contenu dans le fichier .zip renvoyé par l'API"""

    api_url = "https://api.insee.fr/melodi/file/DS_ETAT_CIVIL_NAIS_COMMUNES/DS_ETAT_CIVIL_NAIS_COMMUNES_CSV_FR"
    destination = "data/raw"
    zip_path = os.path.join(destination, "DS_ETAT_CIVIL_NAIS_COMMUNES.zip")

    response = requests.get(api_url, verify= False)
    response.raise_for_status()

    with open(zip_path, "wb") as f:
        f.write(response.content)

    # Extraction des .csv
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(destination)