from pydantic import BaseModel
from datetime import date


class AfvalType(BaseModel):
    id: int
    type: str
    gewicht: int
    tijd: date

class Afval(BaseModel):
    id: int
class Users(BaseModel):
    id: int
    userName: str
    score: int
    administrator: bool



