#!/bin/sh

set -e  # Arrête l'exécution si une erreur survient

echo "🚀 Démarrage du pipeline ETL..."
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
echo "✅ Pipeline terminé avec succès !"
