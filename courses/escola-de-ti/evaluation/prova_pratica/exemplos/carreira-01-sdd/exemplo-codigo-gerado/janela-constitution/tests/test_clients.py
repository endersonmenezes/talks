import pytest
from fastapi import HTTPException

from app import store
from app.routers import clients
from app.routers.clients import ClientCreate


@pytest.fixture(autouse=True)
def clean_store():
    store.reset()
    yield
    store.reset()


def test_create_client():
    client = clients.create_client(ClientCreate(name="Bruno", email="bruno@example.com"))
    assert client.id == 1
    assert store.clients[1]["email"] == "bruno@example.com"


def test_get_unknown_client_returns_404():
    with pytest.raises(HTTPException) as exc:
        clients.get_client(999)
    assert exc.value.status_code == 404
