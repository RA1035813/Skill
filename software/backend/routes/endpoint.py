from fastapi import APIRouter
import database
from database import execute_sql_query
import functies.eersteFuncties
import models.models
# from models import model
from queries import querie as queries

from functies import eersteFuncties

SKILL = APIRouter()


# post

# @boekenwinkel.post("/boeken")
# def add_machine(boeken: models.model.boeken):
#     query = queries.insert_boekenwinkel_query
#     insert = database.execute_sql_query(query, (boeken.id, boeken.titel, boeken.auteur, boeken.prijs,))
#     if insert == True:
#         return boeken   else:
#         return {"error": "Something went wrong..."}
#

# GET

@SKILL.get("/type")
def get_type():
    query = queries.afval_types
    types = database.execute_sql_query(query)
    if isinstance(types, Exception):        return types, 500
    types_to_return = []
    for type in types:        dictionary = {"userName": type[0], "afvaltype": type[1], "gewicht": type[2], "maand": type[3], }
    types_to_return.append(dictionary)
    return {"types": types_to_return}


@SKILL.get("/totaal/gewicht")
def get_totaal():
    query = queries.afval_totaal
    weights = database.execute_sql_query(query)
    if isinstance(weights, Exception):        return weights, 500
    weights_to_return = []
    for weight in weights:        dictionary = {"maand": weight[0], "totaal_gewicht": weight[1], }
    weights_to_return.append(dictionary)
    return {"gewicht": weights_to_return}

# @SKILL.get("/totaal/overzicht")
# def get_overzicht():
#     query = queries.afval_overzicht
#     overzichten = database.execute_sql_query(query)
#     if isinstance(overzichten, Exception):        return overzichten, 500
#     overzichten_to_return = []
#     for overzicht in overzichten:        dictionary = {"userName": overzicht[0], "type": overzicht[1], "gewicht": overzicht[2], "maand": overzicht[3], }
#     overzichten_to_return.append(dictionary)
#     return {"overzicht": overzichten_to_return}
@SKILL.get("/totaal/overzicht")
def get_overzicht():
    query = queries.afval_overzicht
    overzichten = database.execute_sql_query(query)

    if isinstance(overzichten, Exception):
        return {"error": str(overzichten)}, 500

    overzichten_to_return = []
    for overzicht in overzichten:
        dictionary = {
            "userName": overzicht[0],
            "type": overzicht[1],
            "gewicht": overzicht[2],
            "maand": overzicht[3],
        }
        overzichten_to_return.append(dictionary)

    return {"overzicht": overzichten_to_return}



# @SKILL.get("/user")
# def get_userData(user: str, datum: str = None):
#     if datum == None:
#         datum = '2025-11'
#         # datum = functies.eersteFuncties.getDate()
#     query = queries.afval_totaal_users
#     users = database.execute_sql_query(query, (user, datum,))
#     if isinstance(users, Exception):        return users, 500
#     users_to_return = []
#     for user in users:        dictionary = {"userName": user[0], "afvaltype": user[1], "gewicht": user[2], "tijd": user[3], }
#     users_to_return.append(dictionary)
#     return {"overzicht": users_to_return}

@SKILL.get("/user")
def get_userData(user: str, datum: str = None):
    """
    Haal per user de afvaldata op van een specifieke maand.
    datum: 'YYYY-MM' format, bv '2025-11'
    """
    if datum is None:
        datum = '2025-11'

    query = """
    SELECT u.userName, t.type AS afvaltype, t.gewicht, t.tijd
    FROM Users u
    JOIN Afval a ON u.id = a.id
    JOIN AfvalType t ON a.id = t.id
    WHERE u.userName = :user AND DATE_FORMAT(t.tijd, '%Y-%m') = :datum
    ORDER BY t.tijd;
    """

    result = execute_sql_query(query, {"user": user, "datum": datum})
    if isinstance(result, Exception):
        return {"error": str(result)}, 500

    users_to_return = []
    for row in result:
        users_to_return.append({
            "userName": row[0],
            "afvaltype": row[1],
            "gewicht": row[2],
            "tijd": row[3].strftime("%Y-%m-%d %H:%M:%S") if row[3] else None
        })

    return {"overzicht": users_to_return}


# @SKILL.get("/test")
# def get_test():
#     query = queries.testQuery
#     users = database.execute_sql_query(query)
#     if isinstance(users, Exception):        return users, 500
#     users_to_return = []
#     for user in users:        dictionary = {"userName": user[0], "afvaltype": user[1], "gewicht": user[2], "tijd": user[3], }
#     users_to_return.append(dictionary)
#     return {"overzicht": users_to_return}

@SKILL.get("/test")
def get_test():
    query = queries.testQuery
    users = database.execute_sql_query(query)
    if isinstance(users, Exception):
        return users, 500
    users_to_return = []
    for user in users:
        if len(user) >= 1:   # check dat er minimaal 1 kolom is
            dictionary = {"id": user[0]}  # want Users table heeft alleen id, userName etc.
            users_to_return.append(dictionary)
    return {"overzicht": users_to_return}



# @SKILL.get("/titel/boek")
# def get_title(titel: str):
#     query = queries.get_titel_query
#     boeken = database.execute_sql_query(query, (titel,))
#     if isinstance(boeken, Exception):        return boeken, 500
#     boeken_to_return = []
#     for boek in boeken:        dictionary = {"id": boek[0], "titel": boek[1], "auteur": boek[2], "prijs": boek[3], }
#     boeken_to_return.append(dictionary)
#     return {"boeken": boeken_to_return}