# Modelos de domínio (dataclasses) e serialização camelCase.
# Estrutura conforme plan.md: Court, Client, Booking.

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class CourtType(str, Enum):
    futebol = "futebol"
    volei = "vôlei"
    basquete = "basquete"


@dataclass
class Court:
    id: int
    name: str
    type: str = CourtType.futebol.value
    price_per_hour: float = 0.0


@dataclass
class Client:
    id: int
    name: str
    email: str = ""


@dataclass
class Booking:
    id: int
    court_id: int
    client_id: str
    start: datetime
    end: datetime
    price: float = 0.0
    status: str = "active"  # "active" | "cancelled"


def court_to_dict(court: Court) -> dict:
    return {
        "id": court.id,
        "name": court.name,
        "type": court.type,
        "pricePerHour": court.price_per_hour,
    }


def client_to_dict(client: Client) -> dict:
    return {"id": client.id, "name": client.name, "email": client.email}


def booking_to_dict(booking: Booking) -> dict:
    return {
        "id": booking.id,
        "courtId": booking.court_id,
        "clientId": booking.client_id,
        "start": booking.start.isoformat(),
        "end": booking.end.isoformat(),
        "price": booking.price,
        "status": booking.status,
    }
