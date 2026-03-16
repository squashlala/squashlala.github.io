import json
import csv

# Entrée des chemins de fichiers
fichier_source = "./raw_bureaux.json"
fichier_destination = "./bureaux.csv"

# Charger et traiter les données
with open(fichier_source, 'r', encoding='utf-8') as f:
    donnees = json.load(f)

# Extraire et écrire en CSV
with open(fichier_destination, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Bureau', 'Nom', 'LatLon', 'Adresse'])
    
    for bureau in donnees.get('results', []):
        tags_num = [tag for tag in bureau.get('tags', []) if tag.isdigit()]
        writer.writerow([
            ', '.join(tags_num),
            bureau.get('name').replace("\n", "").replace("\r", ""),
            f"[{bureau.get('latitude')}, {bureau.get('longitude')}]",
            bureau.get('address').replace("\n", "").replace("\r", "")
        ])

print(f"Fichier CSV créé : {fichier_destination}")