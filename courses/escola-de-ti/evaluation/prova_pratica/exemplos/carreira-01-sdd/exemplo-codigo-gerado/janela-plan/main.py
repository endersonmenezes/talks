from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from models import Client, Court
from service import BookingError, BookingService
from store import InMemoryRepository

app = FastAPI(title="Court Booking API")

courts = InMemoryRepository[Court]()
clients = InMemoryRepository[Client]()
bookings = InMemoryRepository()
service = BookingService(courts, clients, bookings)


class CourtIn(BaseModel):
    name: str
    hourly_price: float


class ClientIn(BaseModel):
    name: str
    email: str


class BookingIn(BaseModel):
    court_id: int
    client_id: int
    start: datetime
    end: datetime


@app.post("/courts", status_code=201)
def create_court(body: CourtIn):
    return courts.add(Court(id=0, **body.model_dump()))


@app.get("/courts")
def list_courts():
    return courts.list()


@app.post("/clients", status_code=201)
def create_client(body: ClientIn):
    return clients.add(Client(id=0, **body.model_dump()))


@app.get("/clients")
def list_clients():
    return clients.list()


@app.post("/bookings", status_code=201)
def create_booking(body: BookingIn):
    try:
        return service.create_booking(**body.model_dump())
    except BookingError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@app.get("/bookings")
def list_bookings(court_id: Optional[int] = Query(default=None)):
    return service.list_bookings(court_id)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
