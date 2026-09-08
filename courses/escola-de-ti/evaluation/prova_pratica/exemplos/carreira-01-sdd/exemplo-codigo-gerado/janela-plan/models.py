from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Court:
    id: int
    name: str
    hourly_price: float


@dataclass
class Client:
    id: int
    name: str
    email: str


@dataclass
class Booking:
    id: int
    court_id: int
    client_id: int
    start: datetime
    end: datetime
    total_price: float = 0.0
