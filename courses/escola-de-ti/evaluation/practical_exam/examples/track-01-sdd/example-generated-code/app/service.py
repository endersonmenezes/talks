# Regras de negócio (UC2–UC4): duração 1h–3h, passado rejeitado,
# sobreposição por intervalo, preço com fração arredondada para cima.

import math
from datetime import date, datetime, timedelta
from typing import List, Optional

from models import Booking, Court
from store import InMemoryRepository

MIN_DURATION = timedelta(hours=1)
MAX_DURATION = timedelta(hours=3)


class BookingError(Exception):
    def __init__(self, status_code: int, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class BookingService:
    def __init__(
        self,
        courts: InMemoryRepository[Court],
        bookings: InMemoryRepository[Booking],
    ) -> None:
        self.courts = courts
        self.bookings = bookings

    def create_booking(
        self, court_id: int, client_id: str, start: datetime, end: datetime
    ) -> Booking:
        court = self.courts.get(court_id)
        if court is None:
            raise BookingError(404, "court not found")
        if end <= start:
            raise BookingError(400, "end must be after start")

        duration = end - start
        if duration < MIN_DURATION:
            raise BookingError(400, "booking shorter than the 1h minimum")
        if duration > MAX_DURATION:
            raise BookingError(400, "booking longer than the 3h maximum")
        if start < datetime.now(start.tzinfo):
            raise BookingError(400, "start in the past")

        if self._has_overlap(court_id, start, end):
            raise BookingError(409, "booking overlaps an existing booking")

        price = self._price(court.price_per_hour, duration)
        booking = Booking(
            id=0,
            court_id=court_id,
            client_id=client_id,
            start=start,
            end=end,
            price=price,
        )
        return self.bookings.add(booking)

    def get_booking(self, booking_id: int) -> Booking:
        booking = self.bookings.get(booking_id)
        if booking is None or booking.status == "cancelled":
            raise BookingError(404, "booking not found")
        return booking

    def cancel_booking(self, booking_id: int) -> None:
        booking = self.get_booking(booking_id)
        booking.status = "cancelled"

    def list_bookings(
        self, court_id: Optional[int] = None, day: Optional[date] = None
    ) -> List[Booking]:
        active = [b for b in self.bookings.list() if b.status == "active"]
        if court_id is not None:
            active = [b for b in active if b.court_id == court_id]
        if day is not None:
            active = [b for b in active if self._intersects_day(b, day)]
        return active

    def _has_overlap(self, court_id: int, start: datetime, end: datetime) -> bool:
        for existing in self.bookings.filter_by("court_id", court_id):
            if existing.status == "cancelled":
                continue
            if start < existing.end and end > existing.start:
                return True
        return False

    def _intersects_day(self, booking: Booking, day) -> bool:
        day_start = datetime.combine(day, datetime.min.time(), tzinfo=booking.start.tzinfo)
        day_end = day_start + timedelta(days=1)
        return booking.start < day_end and booking.end > day_start

    def _price(self, price_per_hour: float, duration: timedelta) -> float:
        hours = duration.total_seconds() / 3600
        return round(price_per_hour * math.ceil(hours), 2)
