# Query: Toon per user welke afvaltypes en totalen
afval_types = "SELECT u.userName, t.type AS afvaltype, t.gewicht, DATE_FORMAT(t.tijd, '%Y-%m') AS maand FROM Users u JOIN Afval a ON u.id = a.id JOIN AfvalType t ON a.id = t.id ORDER BY u.userName, maand;"
# Query: Totaalgewicht per maand (op basis van je schema)
afval_totaal = "SELECT DATE_FORMAT(t.tijd, '%Y-%m') AS maand, SUM(t.gewicht) AS totaal_gewicht FROM Users u JOIN Afval a ON u.id = a.id  JOIN AfvalType t ON a.id = t.id GROUP BY maand ORDER BY maand;"
# overzicht van user, afvaltype en gewicht
afval_overzicht = "SELECT u.userName, t.type, t.gewicht, DATE_FORMAT(t.tijd, '%Y-%m') AS maand FROM Users u  JOIN Afval a   ON u.id = a.id   JOIN AfvalType t ON a.id = t.id ORDER BY u.userName, maand;"

# totaalgewicht per maand over alle users
# afval_totaal_users = "SELECT DATE_FORMAT(t.tijd, '%Y-%m') AS maand,  SUM(t.gewicht) AS totaal_gewicht FROM Users u JOIN Afval a   ON u.id = a.id  JOIN AfvalType t ON a.id = t.id GROUP BY maand ORDER BY maand;"

# totaalgewicht per maand over alle users
# afval_totaal_users = "SELECT u.userName, t.type AS afvaltype, t.gewicht, t.tijd FROM Users u  JOIN Afval a ON u.id = a.id JOIN AfvalType t ON a.id = t.id WHERE u.userName = (%s)  AND DATE_FORMAT(t.tijd, '%Y-%m') = (%s)  ORDER BY t.tijd;"
afval_totaal_users = "SELECT u.userName, t.type AS afvaltype, t.gewicht, t.tijd FROM Users u  JOIN Afval a ON u.id = a.id JOIN AfvalType t ON a.id = t.id WHERE u.userName = %s AND t.tijd >= CONCAT(%s, '-01 00:00:00') AND t.tijd <  DATE_ADD(CONCAT(%s, '-01 00:00:00'), INTERVAL 1 MONTH);"


# '2025-11'

# old-query = "SELECT * FROM boekenwinkel.boeken WHERE titel = (%s);"
# get_books_query = "SELECT * FROM boekenwinkel.boeken"
#
# insert_boekenwinkel_query = "INSERT INTO boekenwinkel.boeken(id, titel, auteur, prijs) VALUES (%s, %s, %s, %s);"


testQuery = "SELECT * FROM Users;"

# insert:
# Voeg nieuwe user toe
# add_user = "INSERT INTO Users (userName, score, administrator) VALUES (%s, %s, %s);"
add_user = "INSERT INTO Users (userName, score, administrator) VALUES (:userName, :score, :administrator);"


# Voeg afval toe bij specifieke user
add_afval = "INSERT INTO AfvalType (type, gewicht, tijd) VALUES (%s, %s, %s); INSERT INTO Afval (type_id, user_id) VALUES (%s, %s);"

