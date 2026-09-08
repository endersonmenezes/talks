# Testes T1–T11 conforme tests.md (spec-driven: refletem o contrato).

from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from main import app, bookings, clients, courts

client = TestClient(app)

VALOR_HORA = 100.0


@pytest.fixture(autouse=True)
def reset_store():
    courts.clear()
    clients.clear()
    bookings.clear()


def _amanha(hora: int = 10) -> datetime:
    return (datetime.now() + timedelta(days=1)).replace(
        hour=hora, minute=0, second=0, microsecond=0
    )


@pytest.fixture
def court_id():
    resp = client.post(
        "/courts", json={"name": "Quadra 1", "pricePerHour": VALOR_HORA}
    )
    assert resp.status_code == 201
    return resp.json()["id"]


def _reserva(quadra_id, start, end):
    return client.post(
        "/bookings",
        json={
            "courtId": quadra_id,
            "clientId": "cliente-1",
            "start": start.isoformat(),
            "end": end.isoformat(),
        },
    )


# T1 — feliz: cadastrar quadra válida retorna 201 + id
def test_t1_cadastrar_quadra_valida():
    resp = client.post("/courts", json={"name": "Quadra A", "pricePerHour": 80.0})
    assert resp.status_code == 201
    assert "id" in resp.json()


# T2 — borda: cadastrar quadra com valor/hora = 0 retorna 400
def test_t2_quadra_valor_zero():
    resp = client.post("/courts", json={"name": "Quadra B", "pricePerHour": 0})
    assert resp.status_code == 400


# T3 — feliz: reserva de 2h retorna 201 e preço = 2 × valor/hora
def test_t3_reserva_2h_precifica_corretamente(court_id):
    start = _amanha()
    resp = _reserva(court_id, start, start + timedelta(hours=2))
    assert resp.status_code == 201
    assert resp.json()["price"] == 2 * VALOR_HORA


# T4 — borda: reserva de 30min retorna 400 (abaixo do mínimo)
def test_t4_reserva_30min_rejeitada(court_id):
    start = _amanha()
    resp = _reserva(court_id, start, start + timedelta(minutes=30))
    assert resp.status_code == 400


# T5 — borda: reserva de 4h retorna 400 (acima do máximo)
def test_t5_reserva_4h_rejeitada(court_id):
    start = _amanha()
    resp = _reserva(court_id, start, start + timedelta(hours=4))
    assert resp.status_code == 400


# T6 — borda: reserva com start no passado retorna 400
def test_t6_reserva_no_passado_rejeitada(court_id):
    start = datetime.now() - timedelta(hours=2)
    resp = _reserva(court_id, start, start + timedelta(hours=1))
    assert resp.status_code == 400


# T7 — borda: reserva sobreposta à mesma quadra retorna 409
def test_t7_reserva_sobreposta_conflita(court_id):
    start = _amanha()
    r1 = _reserva(court_id, start, start + timedelta(hours=2))
    assert r1.status_code == 201
    r2 = _reserva(court_id, start + timedelta(hours=1), start + timedelta(hours=3))
    assert r2.status_code == 409


# T8 — borda: reserva em quadra diferente, mesmo horário, retorna 201
def test_t8_outra_quadra_nao_conflita(court_id):
    outra = client.post("/courts", json={"name": "Quadra 2", "pricePerHour": VALOR_HORA})
    assert outra.status_code == 201
    start = _amanha()
    r1 = _reserva(court_id, start, start + timedelta(hours=2))
    assert r1.status_code == 201
    r2 = _reserva(outra.json()["id"], start, start + timedelta(hours=2))
    assert r2.status_code == 201


# T9 — borda: reserva de 1h30 cobra 2 × valor/hora (arredonda para cima)
def test_t9_reserva_1h30_arredonda_para_cima(court_id):
    start = _amanha()
    resp = _reserva(court_id, start, start + timedelta(hours=1, minutes=30))
    assert resp.status_code == 201
    assert resp.json()["price"] == 2 * VALOR_HORA


# T10 — feliz: cancelar reserva e consultá-la retorna 404
def test_t10_cancelar_e_consultar_retorna_404(court_id):
    start = _amanha()
    r = _reserva(court_id, start, start + timedelta(hours=1))
    assert r.status_code == 201
    booking_id = r.json()["id"]
    cancel = client.delete(f"/bookings/{booking_id}")
    assert cancel.status_code == 204
    consulta = client.get(f"/bookings/{booking_id}")
    assert consulta.status_code == 404


# T11 — feliz: listar por dia retorna apenas reservas ativas daquele dia
def test_t11_listar_por_dia_so_ativas(court_id):
    start = _amanha()
    r1 = _reserva(court_id, start, start + timedelta(hours=1))
    assert r1.status_code == 201
    r2 = _reserva(court_id, start + timedelta(hours=2), start + timedelta(hours=3))
    assert r2.status_code == 201
    cancel = client.delete(f"/bookings/{r2.json()['id']}")
    assert cancel.status_code == 204

    dia = start.date().isoformat()
    resp = client.get("/bookings", params={"date": dia})
    assert resp.status_code == 200
    ids = [b["id"] for b in resp.json()]
    assert r1.json()["id"] in ids
    assert r2.json()["id"] not in ids
