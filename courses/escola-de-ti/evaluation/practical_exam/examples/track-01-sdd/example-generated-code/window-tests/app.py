from datetime import date, datetime, timedelta
from math import ceil
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

quadras: dict[int, dict] = {}
reservas: dict[int, dict] = {}
_next_quadra_id = 1
_next_reserva_id = 1

DURACAO_MINIMA = timedelta(hours=1)
DURACAO_MAXIMA = timedelta(hours=3)


class QuadraIn(BaseModel):
    nome: str
    valor_hora: float


class ReservaIn(BaseModel):
    quadra_id: int
    start: datetime
    end: datetime


@app.post("/quadras", status_code=201)
def criar_quadra(quadra: QuadraIn):
    global _next_quadra_id
    if quadra.valor_hora <= 0:
        raise HTTPException(status_code=400, detail="valor_hora deve ser maior que zero")
    id = _next_quadra_id
    _next_quadra_id += 1
    quadras[id] = {"id": id, "nome": quadra.nome, "valor_hora": quadra.valor_hora}
    return quadras[id]


@app.post("/reservas", status_code=201)
def criar_reserva(reserva: ReservaIn):
    global _next_reserva_id
    if reserva.quadra_id not in quadras:
        raise HTTPException(status_code=404, detail="quadra não encontrada")
    if reserva.end <= reserva.start:
        raise HTTPException(status_code=400, detail="end deve ser posterior a start")
    duracao = reserva.end - reserva.start
    if duracao < DURACAO_MINIMA:
        raise HTTPException(status_code=400, detail="duração abaixo do mínimo de 1h")
    if duracao > DURACAO_MAXIMA:
        raise HTTPException(status_code=400, detail="duração acima do máximo de 3h")
    if reserva.start < datetime.now(reserva.start.tzinfo):
        raise HTTPException(status_code=400, detail="start no passado")

    for r in reservas.values():
        if (
            r["quadra_id"] == reserva.quadra_id
            and not r["cancelada"]
            and reserva.start < r["end"]
            and reserva.end > r["start"]
        ):
            raise HTTPException(status_code=409, detail="conflito de horário")

    horas_cobradas = ceil(duracao.total_seconds() / 3600)
    preco = horas_cobradas * quadras[reserva.quadra_id]["valor_hora"]

    id = _next_reserva_id
    _next_reserva_id += 1
    reservas[id] = {
        "id": id,
        "quadra_id": reserva.quadra_id,
        "start": reserva.start,
        "end": reserva.end,
        "preco": preco,
        "cancelada": False,
    }
    return reservas[id]


@app.delete("/reservas/{id}", status_code=204)
def cancelar_reserva(id: int):
    if id not in reservas or reservas[id]["cancelada"]:
        raise HTTPException(status_code=404, detail="reserva não encontrada")
    reservas[id]["cancelada"] = True


@app.get("/reservas/{id}", status_code=200)
def consultar_reserva(id: int):
    if id not in reservas or reservas[id]["cancelada"]:
        raise HTTPException(status_code=404, detail="reserva não encontrada")
    return reservas[id]


@app.get("/reservas")
def listar_reservas(dia: Optional[date] = Query(None)):
    ativas = [r for r in reservas.values() if not r["cancelada"]]
    if dia is not None:
        ativas = [
            r
            for r in ativas
            if r["start"].date() == dia or r["end"].date() == dia
        ]
    return ativas
