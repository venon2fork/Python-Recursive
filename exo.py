import glob
import os
import json

chemin = "creer votre propre chemin qui se finit par /**"

files = glob.glob(chemin, recursive=True)


numero_de_compte = None
numero_securite_sociale = None

for f in files:
    if f.endswith(".json"):
        with open(f, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                numero_de_compte = contenu["Credit Mutuel"]["Numero de compte"]
    elif f.endswith(".txt"):
        with open(f, "r") as f:
            contenu = f.read()
            if "Numéro de sécurité sociale" in contenu:
                numero_securite_sociale = contenu.split(":")[-1]

print(numero_de_compte)          
print(numero_securite_sociale)


