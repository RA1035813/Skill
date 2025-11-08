from fastapi import APIRouter
import database
from database import execute_sql_query
import functies.eersteFuncties
import models.models
# from models import model
from queries import querie as queries
from models.models import UserCreate
from functies import eersteFuncties

SKILL = APIRouter()

# GET

@SKILL.get("/type")
def get_type():
    query = queries.afval_types
    types = database.execute_sql_query(query)
    if isinstance(types, Exception):        return types, 500
    types_to_return = []
    for type in types:
        dictionary = {
            "userName": type["userName"],
            "afvaltype": type["afvaltype"],
            "gewicht": type["gewicht"],
            "maand": type["maand"],
        }

    types_to_return.append(dictionary)
    return {"types": types_to_return}


@SKILL.get("/totaal/gewicht")
def get_totaal():
    query = queries.afval_totaal
    weights = database.execute_sql_query(query)
    if isinstance(weights, Exception):        return weights, 500
    weights_to_return = []
    for weight in weights:
        dictionary = {
            "maand": weight["maand"],
            "totaal_gewicht": weight["totaal_gewicht"]
        }


    weights_to_return.append(dictionary)
    return {"gewicht": weights_to_return}


@SKILL.get("/totaal/overzicht")
def get_overzicht():
    query = queries.afval_overzicht
    overzichten = database.execute_sql_query(query)

    if isinstance(overzichten, Exception):
        return {"error": str(overzichten)}, 500

    overzichten_to_return = []
    for overzicht in overzichten:
        dictionary = {
            "userName": overzicht["userName"],
            "type": overzicht["type"],
            "gewicht": overzicht["gewicht"],
            "maand": overzicht["maand"],
        }
        overzichten_to_return.append(dictionary)

    return {"overzicht": overzichten_to_return}


@SKILL.get("/user")
def get_userData(userName: str, datum: str = None):

    if datum is None:
        datum = '2025-11'
    query = queries.get_user
    # query = """
    # SELECT u.userName, t.type AS afvaltype, t.gewicht, t.tijd
    # FROM Users u
    # JOIN Afval a ON u.id = a.id
    # JOIN AfvalType t ON a.id = t.id
    # WHERE u.userName = :user AND DATE_FORMAT(t.tijd, '%Y-%m') = :datum
    # ORDER BY t.tijd;
    # """

    result = execute_sql_query(query, {"user": userName, "datum": datum})
    if isinstance(result, Exception):
        return {"error": str(result)}, 500

    users_to_return = []
    for row in result:
        users_to_return.append({
            "userName": row["userName"],
            "afvaltype": row["afvaltype"],
            "gewicht": row["gewicht"],
            "tijd": row["tijd"].strftime("%Y-%m-%d %H:%M:%S") if row["tijd"] else None
        })

    return {"overzicht": users_to_return}


@SKILL.get("/test")
def get_test():
    query = queries.testQuery
    users = database.execute_sql_query(query)
    if isinstance(users, Exception):
        return users, 500
    users_to_return = []
    for user in users:
        if len(user) >= 1:
            dictionary = {
                "id": user["id"]
            }

            users_to_return.append(dictionary)
    return {"overzicht": users_to_return}



# post



@SKILL.post("/user")
def add_user(user: UserCreate):
    query = queries.add_user
    insert = database.execute_sql_query(
        query,
        {"userName": user.userName, "score": user.score, "administrator": user.administrator}
    )
    if insert is True:
        return user
    return {"error": "Something went wrong..."}


