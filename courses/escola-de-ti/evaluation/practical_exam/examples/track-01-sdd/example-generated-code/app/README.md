---
title: "Sistema de Reservas de Quadras (App de Exemplo)"
type: knowledge
status: done
area: resources
resource: talks
tags:
  - kind/knowledge
  - area/resources
  - resource/talks
  - status/done
created: 2026-09-08
updated: 2026-09-08
---
# Sistema de Reservas de Quadras

API REST em Python + FastAPI para gestão de quadras e reservas, com
persistência em memória. Implementa os casos de uso UC1–UC4 do
`spec.md` (cadastrar quadra, criar reserva, cancelar reserva, listar
reservas) e atende aos cenários de teste T1–T11 do `tests.md`.

## Estrutura

- `main.py` — app FastAPI e rotas (`/courts`, `/clients`, `/bookings`)
- `models.py` — dataclasses `Court`, `Client`, `Booking` e serialização camelCase
- `service.py` — regras de negócio (duração 1h–3h, passado rejeitado, sobreposição, preço com arredondamento para cima)
- `store.py` — repositório em memória com IDs sequenciais
- `test_app.py` — testes T1–T11 com `pytest` e `TestClient`

## Rodar localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A API fica disponível em <http://localhost:8000> (documentação interativa
em `/docs`).

## Rodar os testes

```bash
pytest test_app.py -v
```

## Rodar com Docker

```bash
docker build -t reservas-quadras .
docker run --rm -p 8000:8000 reservas-quadras
```

## Rodar com Podman

```bash
podman build -t reservas-quadras .
podman run --rm -p 8000:8000 reservas-quadras
```

## Contrato rápido

| Método | Rota | Descrição |
| --- | --- | --- |
| POST | `/courts` | Cadastrar quadra (201; 400 se `pricePerHour <= 0`) |
| GET | `/courts` | Listar quadras |
| POST | `/bookings` | Criar reserva (201; 400 duração/passado; 409 sobreposição) |
| GET | `/bookings?courtId={id}&date=YYYY-MM-DD` | Listar reservas ativas |
| GET | `/bookings/{id}` | Consultar reserva (404 se cancelada) |
| DELETE | `/bookings/{id}` | Cancelar reserva (204) |

Preço = `pricePerHour × duração em horas`, com fração arredondada para
cima (ex.: 1h30 → 2 × `pricePerHour`).
