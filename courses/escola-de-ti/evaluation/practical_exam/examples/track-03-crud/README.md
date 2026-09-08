# Exemplo — Carreira 03 (CRUD com juiz de testes)

Arquivos:

| Arquivo | O que é |
| --- | --- |
| `example-contract.md` | O documento que o aluno recebe: a suíte **define o contrato** |
| `public_tests.py` | Os 2 testes públicos (pytest + requests) — modelo da suíte |
| `example-implementation/` | **Implementação de referência mínima** (FastAPI) usada para validar a suíte pública + `Dockerfile` no formato de entrega esperado |

✅ **Validado executando de verdade**: a suíte pública rodou contra `example-implementation/` — **2/2 testes passaram**.

Como o juiz executa (na correção real, o professor faz o mesmo com o repo do aluno):

```bash
# 1. sobe a API do aluno (via Dockerfile é o caminho garantido — 15 pts na rubrica)
docker build -t crud-aluno example-implementation/   # ou o repo do aluno
docker run -d -p 8080:8080 crud-aluno

# 2. roda a suíte (pública aqui; na correção, entram os testes escondidos)
pytest public_tests.py
```

> ⚠️ Exemplo de formato: contrato, testes e valores da prova real são diferentes.
