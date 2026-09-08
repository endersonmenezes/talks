from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from main import app, bookings, clients, courts
from models import Client, Court

client = TestClient(app)


@pytest.fixture(autouse=True)
def seed():
    courts._items.clear()
    courts._next_id = 1
    clients._items.clear()
    clients._next_id = 1
    bookings._items.clear()
    bookings._next_id = 1
    court = courts.add(Court(id=0, name="Quadra 1", hourly_price=100.0))
    cli = clients.add(Client(id=0, name="Ana", email="ana@example.com"))
    return {"court_id": court.id, "client_id": cli.id}


def _booking_body(seed, start, end):
    return {
        "court_id": seed["court_id"],
        "client_id": seed["client_id"],
        "start": start.isoformat(),
        "end": end.isoformat(),
    }


def test_create_booking_ok(seed):
    start = datetime(2026, 9, 7, 10, 0)
    r = client.post("/bookings", json=_booking_body(seed, start, start + timedelta(hours=1)))
    assert r.status_code == 201
    assert r.json()["total_price"] == 100.0


def test_price_fraction_of_hour_rounds_up(seed):
    start = datetime(2026, 9, 7, 10, 0)
    r = client.post("/bookings", json=_booking_body(seed, start, start + timedelta(minutes=31)))
    assert r.status_code == 201
    assert r.json()["total_price"] == 100.0


def test_overlap_rejected(seed):
    start = datetime(2026, 9, 7, 10, 0)
    client.post("/bookings", json=_booking_body(seed, start, start + timedelta(hours=1)))
    r = client.post(
        "/bookings",
        json=_booking_body(seed, start + timedelta(minutes=30), start + timedelta(hours=2)),
    )
    assert r.status_code == 422


def test_end_before_start_rejected(seed):
    start = datetime(2026, 9, 7, 10, 0)
    r = client.post("/bookings", json=_booking_body(seed, start, start - timedelta(hours=1)))
    assert r.status_code == 422
