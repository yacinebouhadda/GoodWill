import psycopg2 

# connection a la base de donnée
con= psycopg2.connect(
        host = "localhost",
        database = "dumps",
        user = "postgres",
        port="5432",
        password = "******")

# curseur

cur=con.cursor()

cur.execute("select physical_person.lastname,physical_person.firstname ,position.title  from impacter,physical_person, position  where position.end_date >now() and position.physical_person_id=physical_person.id and impacter.id=physical_person.impacter_id  and physical_person.lastname in (select physical_person.lastname from physical_person)") 

rows = cur.fetchall()

for r in rows:
    print (f"nom {r[0]} prenom {r[1]} titre {r[2]}")

cur.close()

#fermer la conexion

con.close()
