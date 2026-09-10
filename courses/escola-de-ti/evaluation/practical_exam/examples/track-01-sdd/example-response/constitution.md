---
title: "Constitution — Regras Persistentes do Projeto"
type: knowledge
status: done
area: resources
resource: talks
tags:
  - kind/knowledge
  - area/resources
  - resource/talks
  - status/done
created: 2026-09-07
updated: 2026-09-07
---
# Constitution — Regras persistentes do projeto

1. Código e identificadores em **inglês**; documentação em português.
2. API REST: recursos no plural (`/courts`, `/clients`, `/bookings`), JSON em camelCase.
3. Framework: **Python + FastAPI**; persistência em memória (dict/indexed structures) — banco não é exigido.
4. Testes com **pytest**; cada regra de negócio deve ter ao menos um teste de borda.
5. Sem dependências além de `fastapi`, `uvicorn` e `pytest`.
