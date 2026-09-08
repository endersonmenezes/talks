import pytest
from fastapi import HTTPException

from app import store
from app.routers import courts
from app.routers.courts import CourtCreate


@pytest.fixture(autouse=True)
def clean_store():
    store.reset()
    yield
    store.reset()


def test_create_court():
    court = courts.create_court(CourtCreate(name="Quadra Central"))
    assert court.id == 1
    assert store.courts[1]["name"] == "Quadra Central"


def test_get_unknown_court_returns_404():
    with pytest.raises(HTTPException) as exc:
        courts.get_court(999)
    assert exc.value.status_code == 404


def test_list_courts_empty():
    assert courts.list_courts() == []
