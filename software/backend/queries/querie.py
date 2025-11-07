get_titel_query = "SELECT * FROM boekenwinkel.boeken WHERE titel = (%s);"
get_books_query = "SELECT * FROM boekenwinkel.boeken"

insert_boekenwinkel_query = "INSERT INTO boekenwinkel.boeken(id, titel, auteur, prijs) VALUES (%s, %s, %s, %s);"
