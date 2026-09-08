"""Suíte pública de exemplo — Carreira 03 (mini, só mostra a dinâmica).

Na prova real existem 2 testes públicos (este arquivo é o modelo) e testes
escondidos, executados pelo professor contra o container do aluno.

Uso:  pytest public_tests.py
Pré-requisito: a API do aluno rodando em http://localhost:8080
"""

import requests

BASE = "http://localhost:8080"


def test_criar_tarefa_retorna_201_com_campos():
    r = requests.post(
        f"{BASE}/tasks",
        json={"titulo": "Estudar ES", "descricao": "Prova prática"},
    )
    assert r.status_code == 201
    body = r.json()
    assert body["titulo"] == "Estudar ES"
    assert body["concluida"] is False
    assert isinstance(body["id"], int)


def test_listar_tarefas_contem_a_criada():
    requests.post(f"{BASE}/tasks", json={"titulo": "Tarefa A"})
    r = requests.get(f"{BASE}/tasks")
    assert r.status_code == 200
    titulos = [t["titulo"] for t in r.json()]
    assert "Tarefa A" in titulos
