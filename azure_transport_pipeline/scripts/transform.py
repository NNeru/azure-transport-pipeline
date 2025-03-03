# scripts/transform.py
import pandas as pd
import json
from datetime import datetime

def transform_data(input_file="../data/raw/transport_data.json", output_file="../data/processed/transport_data.csv"):
    # Charger les données brutes
    with open(input_file, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    # Adapter la transformation en fonction de la structure de raw_data
    # Par exemple, supposons que raw_data["result"]["schedules"] contient une liste de dictionnaires
    schedules = raw_data.get("result", {}).get("schedules", [])
    
    if not schedules:
        print("No schedule data found.")
        return
    
    # Créer un DataFrame à partir des données
    df = pd.DataFrame(schedules)
    
    # Ajouter une colonne avec la date de transformation
    df["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Sauvegarder le DataFrame en CSV
    df.to_csv(output_file, index=False)
    print(f"Data transformed and saved to {output_file}")

if __name__ == "__main__":
    transform_data()
