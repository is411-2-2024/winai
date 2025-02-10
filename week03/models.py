from pydantic import BaseModel
from typing import Optional
from sqlmodel import Field, SQLModel

class Trip(BaseModel):
    name: str
    destination: str
    duration: int
    price: float
    group_size: int

class TripOut(Trip):
    id: int

class TripDB(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    destination: str
    duration: int
    price: float
    group_size: int