from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

VALOR_HORA = 100.0


def _amanha(hora: int = 10) -> datetime:
    return (datetime.now() + timedelta(days=1)).replace(hour=hora, minute=0, second=0, microsecond=0)


@pytest.fixture
def quadra_id():
    resp = client.post("/quadras", json={"nome": "Quadra 1", "valor_hora": VALOR_HORA})
    assert resp.status_code == 201
    return resp.json()["id"]


# T1 — feliz: cadastrar quadra válida retorna 201 + id
def test_t1_cadastrar_quadra_valida():
    resp = client.post("/quadras", json={"nome": "Quadra A", "valor_hora": 80.0})
    assert resp.status_code == 201
    assert "id" in resp.json()


# T2 — borda: cadastrar quadra com valor/hora = 0 retorna 400
def test_t2_quadra_valor_zero():
    resp = client.post("/quadras", json={"nome": "Quadra B", "valor_hora": 0})
    assert resp.status_code == 400


# T3 — feliz: reserva de 2h retorna 201 e preço = 2 × valor/hora
def test_t3_reserva_2h_precifica_corretamente(quadra_id):
    start = _amanha()
    resp = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=2)).isoformat()},
    )
    assert resp.status_code == 201
    assert resp.json()["preco"] == 2 * VALOR_HORA


# T4 — borda: reserva de 30min retorna 400 (abaixo do mínimo)
def test_t4_reserva_30min_rejeitada(quadra_id):
    start = _amanha()
    resp = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(minutes=30)).isoformat()},
    )
    assert resp.status_code == 400


# T5 — borda: reserva de 4h retorna 400 (acima do máximo)
def test_t5_reserva_4h_rejeitada(quadra_id):
    start = _amanha()
    resp = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=4)).isoformat()},
    )
    assert resp.status_code == 400


# T6 — borda: reserva com start no passado retorna 400
def test_t6_reserva_no_passado_rejeitada(quadra_id):
    start = datetime.now() - timedelta(hours=2)
    resp = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=1)).isoformat()},
    )
    assert resp.status_code == 400


# T7 — borda: reserva sobreposta à mesma quadra retorna 409
def test_t7_reserva_sobreposta_conflita(quadra_id):
    start = _amanha()
    r1 = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=2)).isoformat()},
    )
    assert r1.status_code == 201
    r2 = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": (start + timedelta(hours=1)).isoformat(), "end": (start + timedelta(hours=2)).isoformat()},
    )
    assert r2.status_code == 409


# T8 — borda: reserva em quadra diferente, mesmo horário, retorna 201
def test_t8_outra_quadra_nao_conflita(quadra_id):
    outra = client.post("/quadras", json={"nome": "Quadra 2", "valor_hora": VALOR_HORA})
    assert outra.status_code == 201
    start = _amanha()
    r1 = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=2)).isoformat()},
    )
    assert r1.status_code == 201
    r2 = client.post(
        "/reservas",
        json={"quadra_id": outra.json()["id"], "start": start.isoformat(), "end": (start + timedelta(hours=2)).isoformat()},
    )
    assert r2.status_code == 201


# T9 — borda: reserva de 1h30 cobra 2 × valor/hora (arredonda para cima)
def test_t9_reserva_1h30_arredonda_para_cima(quadra_id):
    start = _amanha()
    resp = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=1, minutes=30)).isoformat()},
    )
    assert resp.status_code == 201
    assert resp.json()["preco"] == 2 * VALOR_HORA


# T10 — feliz: cancelar reserva e consultá-la retorna 404
def test_t10_cancelar_e_consultar_retorna_404(quadra_id):
    start = _amanha()
    r = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=1)).isoformat()},
    )
    assert r.status_code == 201
    reserva_id = r.json()["id"]
    cancel = client.delete(f"/reservas/{reserva_id}")
    assert cancel.status_code == 204
    consulta = client.get(f"/reservas/{reserva_id}")
    assert consulta.status_code == 404


# T11 — feliz: listar por dia retorna apenas reservas ativas daquele dia
def test_t11_listar_por_dia_so_ativas(quadra_id):
    start = _amanha()
    r1 = client.post(
        "/reservas",
        json={"quadra_id": quadra_id, "start": start.isoformat(), "end": (start + timedelta(hours=1)).isoformat()},
    )
    assert r1.status_code == 201
    r2 = client.post(
        "/reservas",
        json={
            "quadra_id": quadra_id,
            "start": (start + timedelta(hours=2)).isoformat(),
            "end": (start + timedelta(hours=3)).isoformat(),
        },
    )
    assert r2.status_code == 201
    cancel = client.delete(f"/reservas/{r2.json()['id']}")
    assert cancel.status_code == 204

    dia = start.date().isoformat()
    resp = client.get("/reservas", params={"dia": dia})
    assert resp.status_code == 200
    ids = [r["id"] for r in resp.json()]
    assert r1.json()["id"] in ids
    assert r2.json()["id"] not in ids
