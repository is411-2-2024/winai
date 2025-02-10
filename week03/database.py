from sqlmodel import SQLModel, create_engine, Session
from database import TripDB

engine = create_engine("sqlite:///database.db")

def initdb():
    SQLModel.metadata.create_all(engine)

def queryTrip(trip_id: int):
    with Session(engine) as session:
        trip = session.get(TripDB, trip_id).first()
        return trip
    
def queryAssignment():
    pass

def queryProject():
    pass