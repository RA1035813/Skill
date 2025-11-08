from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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

class UserCreate(BaseModel):
    userName: str
    score: int = 0
    administrator: bool = False

