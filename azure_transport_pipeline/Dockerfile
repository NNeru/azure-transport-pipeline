# Utiliser l'image officielle Python 3.9
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ajouter les permissions d'exécution au script d'entrée
RUN chmod +x /app/entrypoint.sh

# Définir l'entrée du conteneur
ENTRYPOINT ["/app/entrypoint.sh"]



