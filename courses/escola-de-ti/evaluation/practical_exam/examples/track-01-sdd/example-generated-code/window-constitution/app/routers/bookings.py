from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.models import CamelModel
from app import store

router = APIRouter(prefix="/bookings", tags=["bookings"])


class BookingCreate(CamelModel):
    court_id: int
    client_id: int
    start_time: datetime
    end_time: datetime


class Booking(BookingCreate):
    id: int


def _has_overlap(court_id: int, start: datetime, end: datetime) -> bool:
    for booking in store.bookings.values():
        if booking["court_id"] != court_id:
            continue
        if start < booking["end_time"] and end > booking["start_time"]:
            return True
    return False


@router.post("", status_code=201)
def create_booking(payload: BookingCreate) -> Booking:
    if payload.end_time <= payload.start_time:
        raise HTTPException(
            status_code=422, detail="endTime must be after startTime"
        )
    if payload.court_id not in store.courts:
        raise HTTPException(status_code=404, detail="Court not found")
    if payload.client_id not in store.clients:
        raise HTTPException(status_code=404, detail="Client not found")
    if _has_overlap(payload.court_id, payload.start_time, payload.end_time):
        raise HTTPException(status_code=409, detail="Court already booked in this period")

    booking_id = store.next_id("bookings")
    booking = payload.model_dump()
    booking["id"] = booking_id
    store.bookings[booking_id] = booking
    return Booking(**booking)


@router.get("")
def list_bookings() -> list[Booking]:
    return [Booking(**booking) for booking in store.bookings.values()]


@router.get("/{booking_id}")
def get_booking(booking_id: int) -> Booking:
    booking = store.bookings.get(booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return Booking(**booking)


@router.delete("/{booking_id}", status_code=204)
def cancel_booking(booking_id: int) -> None:
    if booking_id not in store.bookings:
        raise HTTPException(status_code=404, detail="Booking not found")
    del store.bookings[booking_id]
