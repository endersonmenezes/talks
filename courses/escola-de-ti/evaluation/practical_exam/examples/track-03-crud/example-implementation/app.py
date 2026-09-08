"""Implementação de referência mínima do example-contract.md.

Serve apenas para validar a suíte pública (public_tests.py) e mostrar
o formato de entrega esperado (API + Dockerfile). Na prova, o aluno implementa
na linguagem que escolher.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
tarefas: list[dict] = []
proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None


@app.post("/tasks", status_code=201)
def criar(body: TarefaIn):
    global proximo_id
    if not body.titulo or not body.titulo.strip():
        raise HTTPException(400, "titulo é obrigatório e não pode ser vazio")
    tarefa = {
        "id": proximo_id,
        "titulo": body.titulo,
        "descricao": body.descricao or "",
        "concluida": False,
    }
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa


@app.get("/tasks")
def listar():
    return tarefas


@app.get("/tasks/{task_id}")
def obter(task_id: int):
    for t in tarefas:
        if t["id"] == task_id:
            return t
    raise HTTPException(404)


@app.put("/tasks/{task_id}")
def atualizar(task_id: int, body: TarefaIn):
    for t in tarefas:
        if t["id"] == task_id:
            if body.titulo is not None:
                t["titulo"] = body.titulo
            if body.descricao is not None:
                t["descricao"] = body.descricao
            if body.concluida is not None:
                t["concluida"] = body.concluida
            return t
    raise HTTPException(404)


@app.delete("/tasks/{task_id}", status_code=204)
def remover(task_id: int):
    for i, t in enumerate(tarefas):
        if t["id"] == task_id:
            tarefas.pop(i)
            return
    raise HTTPException(404)
