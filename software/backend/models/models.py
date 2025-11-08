from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from functies import eersteFuncties

class AfvalUser(BaseModel):
    userName: str
    afvaltype: str
    gewicht: int
    tijd: datetime

class Afval(BaseModel):
    id: int

class Users(BaseModel):
    id: Optional[int] = None
    userName: str
    score: Optional[int] = 0
    administrator: Optional[bool] = False


# posts
class UserCreate(BaseModel):
    userName: str
    score: int = 0
    administrator: bool = False

class AfvalCreate(BaseModel):
    user_id: int
    type: str
    gewicht: int
    tijd: datetime = eersteFuncties.getDate()

