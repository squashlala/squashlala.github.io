import csv
import json
import ast

# Entrée des chemins de fichiers
fichier_source = "./resultats.csv"
fichier_destination = "./resultats.json"

# Lire le CSV et convertir en JSON
resultats = []

with open(fichier_source, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for ligne in reader:
        bureau = {}
        
        for champ, valeur in ligne.items():
            if champ == 'Geo':
                # Convertir les coordonnées en liste
                bureau['coordonnees'] = ast.literal_eval(valeur)
            elif champ == 'Bureau':
                bureau[champ.lower()] = valeur
            else:
                # Convertir les valeurs numériques en int
                try:
                    bureau[champ.lower()] = int(valeur)
                except ValueError:
                    bureau[champ.lower()] = valeur
        
        resultats.append(bureau)

# Sauvegarder en JSON
with open(fichier_destination, 'w', encoding='utf-8') as f:
    json.dump(resultats, f, ensure_ascii=False, indent=2)

print(f"Fichier JSON créé : {fichier_destination}")
print(f"Nombre de bureaux traités : {len(resultats)}")