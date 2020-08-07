# Commandes Git


1. On utilise git pour faire l'intilialisation 
* git init
* git add nameFile
* git commit -m "first commit"
* git remote add origin https://github.com/yacinebouhadda/GoodWill 
* git push origin master
2. Aprés je suis sur vs code du coup les commit et les push se fait par vs code directement apres avoir connecter a mon github 

## Mes Requetes SQL
1. \copy (SELECT id,nom FROM nom_de_la_table) TO '/Users/Enzo/Desktop/GitHub/Projet/GoodWill/Bouhadda_Yacine_associations-extract.json' DELIMITER ',' JSON HEADER;
2. \copy (SELECT role FROM nom_de_la_table WHERE nom_de_la_table.mandat="elu") TO '/Users/Enzo/Desktop/GitHub/Projet/GoodWill/Bouhadda_Yacine_roles-extract.json' DELIMITER ',' JSON HEADER;
