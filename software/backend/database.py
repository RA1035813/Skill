# import os
# from sqlalchemy import create_engine, engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
#
# load_dotenv()
#
# DB_URL = os.getenv("DB_CONNECTION")
#
# # engine = create_engine(DB_URL, echo=True, future=True)
# # SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# #
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()
#
# from sqlalchemy import text
#
# def execute_sql_query(query, params=None):
#     try:
#         with engine.connect() as conn:
#             if params:
#                 result = conn.execute(text(query), params)
#             else:
#                 result = conn.execute(text(query))
#             if query.strip().upper().startswith("SELECT"):
#                 return result.fetchall()
#             else:
#                 conn.commit()
#                 return True
#     except Exception as e:
#         print("Error executing query:", e)
#         return e

# -------------------------------------------------
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# DB_URL = os.getenv("DB_CONNECTION")
#
# # Correct engine maken
# engine = create_engine(DB_URL, echo=True, future=True)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# # def execute_sql_query(query, params=None):
# #     try:
# #         with engine.connect() as conn:
# #             if params:
# #                 result = conn.execute(text(query), params)
# #             else:
# #                 result = conn.execute(text(query))
# #             if query.strip().upper().startswith("SELECT"):
# #                 return result.fetchall()
# #             else:
# #                 conn.commit()
# #                 return True
# #     except Exception as e:
# #         print("Error executing query:", e)
# #         return e
# def execute_sql_query(query, params=None):
#     try:
#         with engine.begin() as conn:  # begin() = auto-commit voor niet-SELECT
#             if params:
#                 result = conn.execute(text(query), params)
#             else:
#                 result = conn.execute(text(query))
#
#             # SELECT queries
#             if query.strip().upper().startswith("SELECT"):
#                 return [dict(row._mapping) for row in result]
#
#             # INSERT / UPDATE / DELETE
#             return True
#     except Exception as e:
#         print("Error executing query:", e)
#         return e
#
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_CONNECTION")

# Maak de engine aan
engine = create_engine(DB_URL, echo=True, future=True)

def execute_sql_query(query, params=None):
    try:
        with engine.connect() as conn:
            if params:
                result = conn.execute(text(query), params)
            else:
                result = conn.execute(text(query))

            if query.strip().upper().startswith("SELECT"):
                # ✅ Alle rijen als dicts retourneren
                rows = result.mappings().all()
                return [dict(row) for row in rows]
            else:
                conn.commit()
                return True
    except Exception as e:
        print("Error executing query:", e)
        return e
