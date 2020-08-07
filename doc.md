# Commandes Git


1. On utilise git pour faire l'intilialisation 
* git init
* git add nameFile
* git commit -m "first commit"
* git remote add origin https://github.com/yacinebouhadda/GoodWill 
* git push origin master
2. Aprés je suis sur vs code du coup les commit et les push se fait par vs code directement apres avoir connecter a mon github 

# Mes Requetes SQL
1. connecter a pgAdmin 4 : plsql -h localhost  -p 5432 -U postgres GoodWill
2. Creer la base de données : CREATE DATABASE GoodWill;
3. monter notre base de données : \i test-JDM-dump_db_impacters.sql;
4. recuper les resultats de la premiere requete :

    \copy (SELECT location.id,location.name FROM location
           ORDER BY id ASC) 
           TO '/Users/Enzo/Desktop/GitHub/Projet/GoodWill/Bouhadda_Yacine_associations-extract.csv' DELIMITER ',' CSV HEADER ;

5. recuper les resultats de la deuxieme requete :

    \copy (SELECT position.role FROM position, impacter,physical_person 
            WHERE position.physical_person_id=physical_person.id 
            AND physical_person.impacter_id = impacter.id ;) 
            TO '/Users/Enzo/Desktop/GitHub/Projet/GoodWill/Bouhadda_Yacine_roles-extract.csv'  DELIMITER ',' CSV HEADER ;
