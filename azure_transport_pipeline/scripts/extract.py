# scripts/extract.py
import requests
import json
from datetime import datetime
import os
import sys

# Détermine le chemin de la racine du projet
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # Remonte à la racine

# Ajoute la racine du projet à sys.path
if project_root not in sys.path:
    sys.path.append(project_root)

# Maintenant, Python peut trouver config.py
from config import SNCF_API_KEY



def fetch_sncf_data():
    # Utilise ta clé API depuis le fichier de configuration
    api_key = SNCF_API_KEY  
    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:87391003/departures"
    params = {"datetime": "20250303T163440"}
    
    try:
        response = requests.get(url, params=params, auth=(api_key, ""), timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"[{datetime.now()}] SNCF data fetched successfully.")
        return data
    except Exception as e:
        print(f"Error fetching SNCF data: {e}")
        return None

if __name__ == "__main__":
    data = fetch_sncf_data()
    if data:
        # Créer le dossier raw si nécessaire
        import os
        raw_dir = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
        os.makedirs(raw_dir, exist_ok=True)
        output_file = os.path.join(raw_dir, "sncf_data.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {output_file}")
