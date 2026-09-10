---
title: "Tests — Cenários de Teste (TDD)"
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
# Tests — Cenários de teste (TDD)

Cada item abaixo vira um teste em `test_app.py`. Os casos de borda são obrigatórios.

| # | Cenário | Tipo |
| --- | --- | --- |
| T1 | Cadastrar quadra válida retorna 201 + id | feliz |
| T2 | Cadastrar quadra com valor/hora = 0 retorna 400 | borda |
| T3 | Criar reserva de 2h retorna 201 e preço = 2 × valor/hora | feliz |
| T4 | Reserva de 30min retorna 400 (abaixo do mínimo) | borda |
| T5 | Reserva de 4h retorna 400 (acima do máximo) | borda |
| T6 | Reserva com start no passado retorna 400 | borda |
| T7 | Reserva sobreposta à mesma quadra retorna 409 | borda |
| T8 | Reserva em quadra diferente, mesmo horário, retorna 201 (não conflita) | borda |
| T9 | Reserva de 1h30 cobra 2 × valor/hora (arredonda para cima) | borda |
| T10 | Cancelar reserva e consultá-la retorna 404 | feliz |
| T11 | Listar por dia retorna apenas reservas ativas daquele dia | feliz |
