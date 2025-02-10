from fastapi import FastAPI, HTTPException
from database import engine, initdb, queryTrip
from models import Trip, TripOut, TripDB

initdb()
app = FastAPI()

@app.get("/trips/{trip_id}")
async def read_trip(trip_id: int) -> TripOut:
    trip = queryTrip(trip_id)

    if trip != None:
        print(trip)
        return trip
    
    raise HTTPException(
        status_code=404,
        detail="Trip not found"
    )
