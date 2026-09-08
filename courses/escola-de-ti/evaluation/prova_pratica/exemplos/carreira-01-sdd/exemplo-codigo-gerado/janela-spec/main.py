from datetime import date, datetime, timedelta
from enum import Enum
from math import ceil
from typing import Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


class CourtType(str, Enum):
    futebol = "futebol"
    volei = "vôlei"
    basquete = "basquete"


class CourtCreate(BaseModel):
    name: str = Field(..., min_length=1)
    type: CourtType
    price_per_hour: float = Field(..., gt=0)


class Court(BaseModel):
    id: str
    name: str
    type: CourtType
    price_per_hour: float


class BookingCreate(BaseModel):
    courtId: str
    clientId: str
    start: datetime
    end: datetime


class Booking(BaseModel):
    id: str
    courtId: str
    clientId: str
    start: datetime
    end: datetime
    price: float
    status: str  # "active" | "cancelled"


app = FastAPI(title="Sistema de Reservas de Quadras")

courts: dict[str, Court] = {}
bookings: dict[str, Booking] = {}


@app.post("/courts", status_code=201)
def create_court(payload: CourtCreate) -> Court:
    court = Court(id=uuid4().hex, **payload.model_dump())
    courts[court.id] = court
    return court


@app.post("/bookings", status_code=201)
def create_booking(payload: BookingCreate) -> Booking:
    if payload.courtId not in courts:
        raise HTTPException(status_code=404, detail="Quadra não encontrada")

    duration = payload.end - payload.start
    hours = duration.total_seconds() / 3600
    if hours < 1 or hours > 3:
        raise HTTPException(status_code=400, detail="Duração deve ser entre 1h e 3h")

    if payload.start < datetime.now(payload.start.tzinfo):
        raise HTTPException(status_code=400, detail="Reserva no passado não é permitida")

    for b in bookings.values():
        if b.status == "active" and b.courtId == payload.courtId:
            if payload.start < b.end and b.start < payload.end:
                raise HTTPException(
                    status_code=409, detail="Conflito com reserva existente"
                )

    court = courts[payload.courtId]
    price = court.price_per_hour * ceil(hours)
    booking = Booking(
        id=uuid4().hex,
        status="active",
        price=round(price, 2),
        **payload.model_dump(),
    )
    bookings[booking.id] = booking
    return booking


@app.delete("/bookings/{booking_id}", status_code=204)
def cancel_booking(booking_id: str):
    booking = bookings.get(booking_id)
    if booking is None or booking.status == "cancelled":
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    booking.status = "cancelled"


@app.get("/bookings")
def list_bookings(
    courtId: Optional[str] = Query(None),
    date: Optional[date] = Query(None),
) -> list[Booking]:
    result = [b for b in bookings.values() if b.status == "active"]
    if courtId is not None:
        result = [b for b in result if b.courtId == courtId]
    if date is not None:
        day_start = datetime.combine(date, datetime.min.time(), tzinfo=b.start.tzinfo)
        day_end = day_start + timedelta(days=1)
        result = [b for b in result if b.start < day_end and b.end > day_start]
    return result
