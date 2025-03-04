import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer la Connection String
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")

# Vérifier que la connexion Azure est bien chargée
if not AZURE_CONNECTION_STRING:
    raise ValueError("❌ AZURE_CONNECTION_STRING est introuvable. Vérifie ton fichier .env !")

# Déterminer le chemin du fichier à envoyer
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "processed", "sncf_data.csv")

def upload_to_blob(container_name="transport-data"):
    """ Upload du fichier CSV vers Azure Blob Storage """

    try:
        # Connexion à Azure Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        
        # Vérifier si le container existe, sinon le créer
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()
            print(f"✅ Container '{container_name}' created.")
        else:
            print(f"ℹ️ Container '{container_name}' already exists.")

        # Vérifier si le fichier existe avant l'upload
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Le fichier {file_path} n'existe pas. Exécute transform.py d'abord.")

        # Définir le nom du blob (nom du fichier sur Azure)
        blob_name = os.path.basename(file_path)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload du fichier
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"✅ Fichier {file_path} uploadé vers Azure Blob Storage dans le container '{container_name}'.")
    except Exception as e:
        print(f"❌ Erreur lors de l'upload : {e}")

if __name__ == "__main__":
    upload_to_blob()
