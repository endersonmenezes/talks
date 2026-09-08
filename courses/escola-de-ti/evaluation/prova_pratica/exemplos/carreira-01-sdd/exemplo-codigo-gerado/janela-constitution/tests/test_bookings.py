import pytest
from fastapi import HTTPException

from app import store
from app.routers import bookings, clients, courts
from app.routers.bookings import BookingCreate


@pytest.fixture(autouse=True)
def clean_store():
    store.reset()
    yield
    store.reset()


def _seed_court_and_client():
    court = courts.create_court(courts.CourtCreate(name="Quadra 1"))
    client = clients.create_client(clients.ClientCreate(name="Ana"))
    return court.id, client.id


def test_create_booking_success():
    court_id, client_id = _seed_court_and_client()
    booking = bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    assert booking.id == 1
    assert store.bookings[1]["court_id"] == court_id


def test_end_time_before_start_time_is_rejected():
    court_id, client_id = _seed_court_and_client()
    with pytest.raises(HTTPException) as exc:
        bookings.create_booking(
            BookingCreate(
                court_id=court_id,
                client_id=client_id,
                start_time="2026-09-10T11:00:00",
                end_time="2026-09-10T10:00:00",
            )
        )
    assert exc.value.status_code == 422


def test_end_time_equal_to_start_time_is_rejected():
    court_id, client_id = _seed_court_and_client()
    with pytest.raises(HTTPException) as exc:
        bookings.create_booking(
            BookingCreate(
                court_id=court_id,
                client_id=client_id,
                start_time="2026-09-10T10:00:00",
                end_time="2026-09-10T10:00:00",
            )
        )
    assert exc.value.status_code == 422


def test_booking_unknown_court_is_rejected():
    _, client_id = _seed_court_and_client()
    with pytest.raises(HTTPException) as exc:
        bookings.create_booking(
            BookingCreate(
                court_id=999,
                client_id=client_id,
                start_time="2026-09-10T10:00:00",
                end_time="2026-09-10T11:00:00",
            )
        )
    assert exc.value.status_code == 404


def test_booking_unknown_client_is_rejected():
    court_id, _ = _seed_court_and_client()
    with pytest.raises(HTTPException) as exc:
        bookings.create_booking(
            BookingCreate(
                court_id=court_id,
                client_id=999,
                start_time="2026-09-10T10:00:00",
                end_time="2026-09-10T11:00:00",
            )
        )
    assert exc.value.status_code == 404


def test_overlapping_booking_same_court_is_rejected():
    court_id, client_id = _seed_court_and_client()
    bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    with pytest.raises(HTTPException) as exc:
        bookings.create_booking(
            BookingCreate(
                court_id=court_id,
                client_id=client_id,
                start_time="2026-09-10T10:30:00",
                end_time="2026-09-10T11:30:00",
            )
        )
    assert exc.value.status_code == 409


def test_adjacent_bookings_do_not_overlap():
    # Borda: fim exatamente igual ao início do próximo — deve ser permitido.
    court_id, client_id = _seed_court_and_client()
    bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    second = bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T11:00:00",
            end_time="2026-09-10T12:00:00",
        )
    )
    assert second.id == 2


def test_same_period_different_court_is_allowed():
    court_id, client_id = _seed_court_and_client()
    other_court = courts.create_court(courts.CourtCreate(name="Quadra 2"))
    bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    second = bookings.create_booking(
        BookingCreate(
            court_id=other_court.id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    assert second.id == 2


def test_cancel_unknown_booking_is_rejected():
    with pytest.raises(HTTPException) as exc:
        bookings.cancel_booking(999)
    assert exc.value.status_code == 404


def test_json_uses_camel_case():
    court_id, client_id = _seed_court_and_client()
    booking = bookings.create_booking(
        BookingCreate(
            court_id=court_id,
            client_id=client_id,
            start_time="2026-09-10T10:00:00",
            end_time="2026-09-10T11:00:00",
        )
    )
    data = booking.model_dump(by_alias=True)
    assert "courtId" in data
    assert "clientId" in data
    assert "startTime" in data
    assert "endTime" in data
