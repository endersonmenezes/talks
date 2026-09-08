# App FastAPI: rotas REST em inglês, recursos no plural, JSON camelCase
# (conforme constitution.md e spec.md).

from datetime import date, datetime
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from models import (
    Client,
    Court,
    CourtType,
    booking_to_dict,
    client_to_dict,
    court_to_dict,
)
from service import BookingError, BookingService
from store import InMemoryRepository

app = FastAPI(title="Court Booking API")

courts = InMemoryRepository[Court]()
clients = InMemoryRepository[Client]()
bookings = InMemoryRepository()
service = BookingService(courts, bookings)


class CourtIn(BaseModel):
    name: str
    type: CourtType = CourtType.futebol
    pricePerHour: float


class ClientIn(BaseModel):
    name: str
    email: str = ""


class BookingIn(BaseModel):
    courtId: int
    clientId: str
    start: datetime
    end: datetime


@app.post("/courts", status_code=201)
def create_court(body: CourtIn):
    # Validação manual para retornar 400 (pydantic retornaria 422).
    if body.pricePerHour <= 0:
        raise HTTPException(status_code=400, detail="pricePerHour must be greater than zero")
    court = courts.add(
        Court(id=0, name=body.name, type=body.type.value, price_per_hour=body.pricePerHour)
    )
    return court_to_dict(court)


@app.get("/courts")
def list_courts():
    return [court_to_dict(c) for c in courts.list()]


@app.post("/clients", status_code=201)
def create_client(body: ClientIn):
    client = clients.add(Client(id=0, **body.model_dump()))
    return client_to_dict(client)


@app.get("/clients")
def list_clients():
    return [client_to_dict(c) for c in clients.list()]


@app.post("/bookings", status_code=201)
def create_booking(body: BookingIn):
    try:
        booking = service.create_booking(
            court_id=body.courtId,
            client_id=body.clientId,
            start=body.start,
            end=body.end,
        )
    except BookingError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)
    return booking_to_dict(booking)


@app.get("/bookings")
def list_bookings(
    courtId: Optional[int] = Query(default=None),
    date: Optional[date] = Query(default=None),
):
    result = service.list_bookings(court_id=courtId, day=date)
    return [booking_to_dict(b) for b in result]


@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int):
    try:
        return booking_to_dict(service.get_booking(booking_id))
    except BookingError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)


@app.delete("/bookings/{booking_id}", status_code=204)
def cancel_booking(booking_id: int):
    try:
        service.cancel_booking(booking_id)
    except BookingError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
