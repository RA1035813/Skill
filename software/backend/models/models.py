# from typing import List
from pydantic import BaseModel
from datetime import datetime

class AfvalUser(BaseModel):
    userName: str
    afvaltype: str
    gewicht: int
    tijd: datetime

class Afval(BaseModel):
    id: int

class Users(BaseModel):
    id: int
    userName: str
    score: int
    administrator: bool



