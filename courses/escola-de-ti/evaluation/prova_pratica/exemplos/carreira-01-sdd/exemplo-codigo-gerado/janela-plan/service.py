import math
from datetime import datetime
from typing import List, Optional

from models import Booking, Client, Court
from store import InMemoryRepository

MIN_DURATION_MINUTES = 30
MAX_DURATION_HOURS = 4


class BookingError(Exception):
    pass


class BookingService:
    def __init__(
        self,
        courts: InMemoryRepository[Court],
        clients: InMemoryRepository[Client],
        bookings: InMemoryRepository[Booking],
    ) -> None:
        self.courts = courts
        self.clients = clients
        self.bookings = bookings

    def create_booking(
        self, court_id: int, client_id: int, start: datetime, end: datetime
    ) -> Booking:
        if self.courts.get(court_id) is None:
            raise BookingError("court not found")
        if self.clients.get(client_id) is None:
            raise BookingError("client not found")
        if end <= start:
            raise BookingError("end must be after start")

        duration = end - start
        if duration.total_seconds() < MIN_DURATION_MINUTES * 60:
            raise BookingError("booking shorter than minimum duration")
        if duration.total_seconds() > MAX_DURATION_HOURS * 3600:
            raise BookingError("booking longer than maximum duration")

        if self._has_overlap(court_id, start, end):
            raise BookingError("booking overlaps an existing booking")

        court = self.courts.get(court_id)
        total_price = self._price(court.hourly_price, duration)
        booking = Booking(
            id=0, court_id=court_id, client_id=client_id,
            start=start, end=end, total_price=total_price,
        )
        return self.bookings.add(booking)

    def list_bookings(self, court_id: Optional[int] = None) -> List[Booking]:
        if court_id is None:
            return self.bookings.list()
        return self.bookings.filter_by("court_id", court_id)

    def _has_overlap(self, court_id: int, start: datetime, end: datetime) -> bool:
        for existing in self.bookings.filter_by("court_id", court_id):
            if start < existing.end and end > existing.start:
                return True
        return False

    def _price(self, hourly_price: float, duration) -> float:
        hours = duration.total_seconds() / 3600
        return math.ceil(hours) * hourly_price
