import csv, json

csvFilePath="Bouhadda_Yacine_associations-extract.csv"
jsonFilePath="Bouhadda_Yacine_associations-extract.json"

data = {}

# lire le fichier csv et l'ajouter au dictionnaire 

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow["id"]
        data[id] = csvRow


# lire les données sur le fichier json
with open(jsonFilePath, "w" ) as jsonFile:
    jsonFile.write(json.dumps(data))

