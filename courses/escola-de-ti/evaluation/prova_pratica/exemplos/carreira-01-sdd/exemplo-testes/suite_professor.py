"""Suíte do professor — correção da Carreira 01 (SDD + TDD).

Roda contra a API em execução (APP_URL; default http://localhost:8000).
Na correção real, executa DENTRO do container — ver compose-testes.yaml —
para não depender da máquina do professor.

Categorias:
  A — Contrato REST (spec.md, UC1–UC4)
  B — Casos de borda "escondidos" (NÃO estão em tests.md do aluno)
  C — Requisito do enunciado que ficou FORA do spec.md (risco SDD: clientes/telefone)
  D — Checagens SDLC estáticas no repositório entregue
"""

import os
import pathlib
from datetime import datetime, timedelta

import pytest
import requests

BASE = os.environ.get("APP_URL", "http://localhost:8000").rstrip("/")
APP_DIR = pathlib.Path(__file__).resolve().parent.parent / "exemplo-codigo-gerado" / "app"

# Janela fixa no futuro para os testes de data
DAY = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")


def _dt(hhmm: str) -> str:
    return f"{DAY}T{hhmm}:00"


@pytest.fixture()
def court():
    r = requests.post(
        f"{BASE}/courts",
        json={"name": "Quadra Suíte", "type": "futebol", "pricePerHour": 100.0},
    )
    assert r.status_code == 201
    return r.json()


def _book(court_id, start, end, client="cliente-1"):
    return requests.post(
        f"{BASE}/bookings",
        json={"courtId": court_id, "clientId": client, "start": start, "end": end},
    )


# ---------------------------------------------------------------- A. Contrato REST

class TestContrato:
    def test_a1_criar_quadra_201_com_id(self, court):
        assert isinstance(court["id"], int)
        assert court["pricePerHour"] == 100.0

    def test_a2_quadra_preco_zero_400(self):
        r = requests.post(f"{BASE}/courts", json={"name": "X", "pricePerHour": 0})
        assert r.status_code == 400

    def test_a3_reserva_2h_precificada(self, court):
        r = _book(court["id"], _dt("10:00"), _dt("12:00"))
        assert r.status_code == 201
        assert r.json()["price"] == 200.0

    def test_a5_cancelar_some_da_consulta(self, court):
        b = _book(court["id"], _dt("10:00"), _dt("11:00")).json()
        requests.delete(f"{BASE}/bookings/{b['id']}")
        assert requests.get(f"{BASE}/bookings/{b['id']}").status_code == 404

    def test_a6_listar_por_quadra_filtra(self, court):
        _book(court["id"], _dt("10:00"), _dt("11:00"))
        outra = requests.post(
            f"{BASE}/courts", json={"name": "Outra", "pricePerHour": 50.0}
        ).json()
        _book(outra["id"], _dt("10:00"), _dt("11:00"))
        r = requests.get(f"{BASE}/bookings", params={"courtId": court["id"]})
        assert r.status_code == 200
        assert all(b["courtId"] == court["id"] for b in r.json())

    def test_a7_listar_por_dia_so_ativas(self, court):
        ativa = _book(court["id"], _dt("10:00"), _dt("11:00")).json()
        cancelada = _book(court["id"], _dt("14:00"), _dt("15:00")).json()
        requests.delete(f"{BASE}/bookings/{cancelada['id']}")
        r = requests.get(f"{BASE}/bookings", params={"date": DAY})
        ids = [b["id"] for b in r.json()]
        assert ativa["id"] in ids
        assert cancelada["id"] not in ids


# ------------------------------------------------- B. Bordas escondidas (juiz online)

class TestBordasEscondidas:
    def test_b1_exatamente_1h_aceita(self, court):
        assert _book(court["id"], _dt("10:00"), _dt("11:00")).status_code == 201

    def test_b2_exatamente_3h_aceita(self, court):
        assert _book(court["id"], _dt("10:00"), _dt("13:00")).status_code == 201

    def test_b3_reserva_adjacente_nao_conflita(self, court):
        assert _book(court["id"], _dt("10:00"), _dt("11:00")).status_code == 201
        assert _book(court["id"], _dt("11:00"), _dt("12:00")).status_code == 201

    def test_b4_um_minuto_a_mais_arredonda(self, court):
        r = _book(court["id"], _dt("10:00"), _dt("11:01"))
        assert r.status_code == 201
        assert r.json()["price"] == 200.0  # 100/h × ceil(1h01)

    def test_b5_sobreposicao_de_1_minuto_409(self, court):
        _book(court["id"], _dt("10:00"), _dt("11:00"))
        assert _book(court["id"], _dt("10:59"), _dt("12:00")).status_code == 409

    def test_b6_cancelada_some_de_todas_as_listagens(self, court):
        b = _book(court["id"], _dt("10:00"), _dt("11:00")).json()
        requests.delete(f"{BASE}/bookings/{b['id']}")
        por_quadra = requests.get(f"{BASE}/bookings", params={"courtId": court["id"]}).json()
        por_dia = requests.get(f"{BASE}/bookings", params={"date": DAY}).json()
        assert b["id"] not in [x["id"] for x in por_quadra]
        assert b["id"] not in [x["id"] for x in por_dia]


# -------------------------------------- C. Requisito fora do spec.md (risco SDD)

class TestRequisitoOculto:
    def test_c1_cliente_tem_telefone(self):
        """O ENUNCIADO (problema-exemplo.md) exige cliente com id, nome e telefone.
        O spec.md do exemplo NÃO tem UC de clientes — se este teste falhar,
        é exatamente a lacuna de especificação que a prova quer expor:
        o modelo só gera o que a spec manda."""
        r = requests.post(f"{BASE}/clients", json={"name": "Maria", "telefone": "44 99999-0000"})
        assert r.status_code == 201
        clientes = requests.get(f"{BASE}/clients").json()
        assert any(c.get("telefone") == "44 99999-0000" for c in clientes)


# ------------------------------------------------------- D. Checagens SDLC estáticas

class TestSDLC:
    def test_d1_dockerfile_com_expose_e_cmd(self):
        df = (APP_DIR / "Dockerfile").read_text()
        assert "EXPOSE" in df and "CMD" in df

    def test_d2_readme_com_instrucoes_container(self):
        readme = (APP_DIR / "README.md").read_text().lower()
        assert "docker" in readme or "podman" in readme

    def test_d3_requirements_declara_fastapi(self):
        req = (APP_DIR / "requirements.txt").read_text().lower()
        assert "fastapi" in req

    def test_d4_aluno_entregou_proprios_testes(self):
        """tests.md promete 11 cenários — o repo deve conter testes do aluno."""
        test_file = APP_DIR / "test_app.py"
        assert test_file.exists()
        n = test_file.read_text().count("def test_")
        assert n >= 11, f"só {n} testes encontrados (tests.md prometia T1–T11)"
