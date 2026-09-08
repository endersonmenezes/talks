from fastapi import APIRouter, HTTPException

from app.models import CamelModel
from app import store

router = APIRouter(prefix="/courts", tags=["courts"])


class CourtCreate(CamelModel):
    name: str
    location: str | None = None


class Court(CourtCreate):
    id: int


@router.post("", status_code=201)
def create_court(payload: CourtCreate) -> Court:
    court_id = store.next_id("courts")
    court = payload.model_dump()
    court["id"] = court_id
    store.courts[court_id] = court
    return Court(**court)


@router.get("")
def list_courts() -> list[Court]:
    return [Court(**court) for court in store.courts.values()]


@router.get("/{court_id}")
def get_court(court_id: int) -> Court:
    court = store.courts.get(court_id)
    if court is None:
        raise HTTPException(status_code=404, detail="Court not found")
    return Court(**court)
