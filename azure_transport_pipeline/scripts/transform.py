import os
import json
import pandas as pd
from datetime import datetime

# Définir les chemins des fichiers
current_dir = os.path.dirname(os.path.abspath(__file__))
raw_file = os.path.join(current_dir, "..", "data", "raw", "sncf_data.json")
processed_file = os.path.join(current_dir, "..", "data", "processed", "sncf_data.csv")

def transform_sncf_data():
    """ Charge les données brutes JSON, les transforme et les enregistre en CSV """

    # Vérifier si le fichier brut existe
    if not os.path.exists(raw_file):
        print(f"Erreur : Le fichier {raw_file} n'existe pas. Exécutez extract.py d'abord.")
        return

    # Charger les données JSON
    with open(raw_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Extraire les départs
    departures = raw_data.get("departures", [])

    if not departures:
        print("Aucun départ trouvé dans les données.")
        return

    # Créer une liste d'informations structurées
    data_list = []
    for departure in departures:
        train_info = {
            "departure_time": departure["stop_date_time"]["departure_date_time"],
            "station_name": departure["stop_point"]["name"],
            "train_number": departure["display_informations"]["headsign"],
            "direction": departure["display_informations"]["direction"],
            "transport_mode": departure["display_informations"]["commercial_mode"]
        }
        data_list.append(train_info)

    # Transformer en DataFrame
    df = pd.DataFrame(data_list)

    # Convertir les timestamps en format lisible
    df["departure_time"] = pd.to_datetime(df["departure_time"], format="%Y%m%dT%H%M%S")

    # Ajouter une colonne avec l'heure de transformation
    df["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Créer le dossier processed si besoin
    processed_dir = os.path.dirname(processed_file)
    os.makedirs(processed_dir, exist_ok=True)

    # Sauvegarder en CSV
    df.to_csv(processed_file, index=False)
    print(f"✅ Données transformées et enregistrées dans {processed_file}")

if __name__ == "__main__":
    transform_sncf_data()
