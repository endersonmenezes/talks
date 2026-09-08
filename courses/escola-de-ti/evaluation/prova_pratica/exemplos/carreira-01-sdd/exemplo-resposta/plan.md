# Plan — Arquitetura e decisões

## Stack

- **Python 3.11 + FastAPI + uvicorn** (justificativa: rápido de gerar e testar; contrato REST claro).
- Persistência **em memória** com locks simples (não há concorrência real na suíte do professor).

## Estrutura de arquivos a gerar

```
main.py        # app FastAPI, rotas
models.py      # dataclasses Court, Client, Booking
service.py     # regras de negócio (duração, sobreposição, preço)
store.py       # repositório em memória
test_app.py    # testes pytest (refletem tests.md)
```

## Decisões

1. Sobreposição detectada por comparação de intervalos: `start < existing.end and end > existing.start`.
2. Fração de hora arredonda para cima via `math.ceil`.
3. IDs sequenciais simples (int), gerados no repositório.
