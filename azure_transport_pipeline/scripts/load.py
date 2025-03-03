# scripts/load.py
from azure.storage.blob import BlobServiceClient
import os

def upload_to_blob(file_path="../data/processed/transport_data.csv", container_name="transport-data"):
    # Remplace cette chaîne par ta connection string Azure (pour tester, tu peux la mettre en variable d'environnement)
    connection_string = "DefaultEndpointsProtocol=https;AccountName=your_account;AccountKey=your_key;EndpointSuffix=core.windows.net"
    
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Créer le container s'il n'existe pas
        try:
            blob_service_client.create_container(container_name)
            print("Container created.")
        except Exception as e:
            print("Container already exists or error:", e)
        
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
        
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        
        print(f"File {file_path} uploaded to Azure Blob Storage in container '{container_name}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    upload_to_blob()
