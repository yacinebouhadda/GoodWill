import json
fichier = open("Bouhadda_Yacine_associations-extract.json" ,"rt")
personne = json.loads(fichier.read())

for mandat in personne['Mandat']
    if mandat['Mnandat']>= 1
    print(mandat['Nom'])