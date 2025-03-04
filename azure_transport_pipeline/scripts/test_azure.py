import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer la Connection String
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")

if not AZURE_CONNECTION_STRING:
    raise ValueError("❌ AZURE_CONNECTION_STRING est introuvable. Vérifie ton fichier .env !")

try:
    # Connexion à Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    print("✅ Connexion réussie à Azure Blob Storage !")
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
