from fastapi import APIRouter, HTTPException

from app.models import CamelModel
from app import store

router = APIRouter(prefix="/clients", tags=["clients"])


class ClientCreate(CamelModel):
    name: str
    email: str | None = None


class Client(ClientCreate):
    id: int


@router.post("", status_code=201)
def create_client(payload: ClientCreate) -> Client:
    client_id = store.next_id("clients")
    client = payload.model_dump()
    client["id"] = client_id
    store.clients[client_id] = client
    return Client(**client)


@router.get("")
def list_clients() -> list[Client]:
    return [Client(**client) for client in store.clients.values()]


@router.get("/{client_id}")
def get_client(client_id: int) -> Client:
    client = store.clients.get(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**client)
