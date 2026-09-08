# PROVENIÊNCIA — Consolidação das 4 janelas de contexto

Fase de "assembly": cada janela gerou código vendo apenas um `.md`. Esta
tabela registra, para cada decisão, qual janela contribuiu e qual fonte
de verdade (`exemplo-resposta/`) prevaleceu nos conflitos.

## Decisões e origem

| Decisão | Janela de origem | Observação |
| --- | --- | --- |
| Endpoints em inglês (`/courts`, `/bookings`) | spec + plan + constitution | **Conflito:** janela-tests usou `/quadras` e `/reservas` (viu só tests.md redigido em PT). Prevalesceu `constitution.md` (inglês) e `spec.md`. |
| Campos camelCase (`courtId`, `clientId`, `pricePerHour`, `start`, `end`) | constitution (CamelModel) + spec | **Conflito:** janela-tests usava `quadra_id`/`preco`; janela-spec usava `price_per_hour` (snake_case). Consolidado em camelCase com serializadores em `models.py`. |
| IDs sequenciais `int` gerados no repositório | plan + constitution (`store.py`) + plan (`InMemoryRepository`) | **Conflito:** janela-spec usava `uuid4().hex`. Prevalesceu `plan.md` decisão 3. |
| Duração mín. 1h / máx. 3h | spec + tests (T4/T5) | **Conflito:** janela-plan usava 30min–4h (`MIN_DURATION_MINUTES = 30`, `MAX_DURATION_HOURS = 4`). Corrigido em `service.py`. |
| Status codes 400/404/409 (não 422) | tests + spec | **Conflito:** janela-plan mapeava tudo para 422. `BookingError` agora carrega o status; validação de `pricePerHour` é manual no route (pydantic retornaria 422). |
| Rejeitar `start` no passado com 400 | spec (UC2) + janela-tests (`app.py`) + janela-spec | Mantido em `service.py`; comparação com `datetime.now(start.tzinfo)`. |
| Sobreposição por comparação de intervalos `start < existing.end and end > existing.start` | plan decisão 1 + janela-spec/janela-tests | Idêntico nas três; reutilizado. |
| Sobreposição ignora reservas canceladas | janela-tests (`app.py`) | janela-spec já filtrava por `status == "active"`; equivalente. |
| Preço com fração arredondada para cima (`math.ceil`) | plan decisão 2 + todas as janelas | Unânime. `round(..., 2)` para estabilidade de ponto flutuante veio da janela-spec. |
| Cancelamento via `DELETE /bookings/{id}` → 204; cancelada some (404) | janela-tests (T10) + spec (UC3) | janela-spec não tinha `GET /bookings/{id}`; adicionado para atender T10. |
| Listagem por dia: `GET /bookings?date=YYYY-MM-DD`, só ativas, intersectam o dia | spec (UC4) + janela-spec (interseção de intervalos) | **Conflito:** janela-tests usava o parâmetro `dia` e comparação só de datas (`start.date() == dia`); janela-tests/app.py usava intervalo. Prevalesceu o parâmetro `date` do spec com interseção real de intervalos. |
| Arquitetura `main.py` / `models.py` / `service.py` / `store.py` | plan (estrutura de arquivos) | janela-constitution usava pacote `app/` com routers; janela-spec/tests monolitos. Adotada estrutura plana do plan.md. |
| `store.py` = `InMemoryRepository` genérico com lock | janela-plan | Reutilizado quase verbatim; acrescentado `clear()` para os testes. |
| `models.py` = dataclasses `Court`, `Client`, `Booking` | plan + janela-plan | **Conflito:** janela-spec usava pydantic `BaseModel`; janela-constitution exigia pydantic. Prevalesceu plan.md ("dataclasses"). Serialização camelCase feita por funções `*_to_dict`. |
| `clientId` não exige cliente cadastrado | spec (UC2 não lista UC de cliente) + janela-tests (não cadastra cliente) | **Conflito:** janela-plan exigia `client_id` existente (erro "client not found"). Como spec.md não tem UC de cadastro de cliente, `clientId` é tratado como identificador opaco. |
| Campo `type` da quadra (`futebol`/`vôlei`/`basquete`) | spec (UC1) + janela-spec (enum) | Mantido como opcional com default `futebol` para não quebrar payloads sem o campo (tests.md não o usa). |
| Quadra com `valor/hora` como campo numérico | spec (UC1) + janela-tests (float) | Nome consolidado: `pricePerHour` (float, camelCase). |
| Validação 400 de `pricePerHour <= 0` manual no route | janela-tests (`app.py`) | Necessário porque `Field(gt=0)` do pydantic (usado pela janela-spec) retorna 422, e T2 exige 400. |
| Testes T1–T11 com `TestClient` e fixture de reset | janela-tests (esqueleto) + janela-plan (fixture de reset) | Esqueleto veio da janela-tests; traduzido para o contrato (inglês/camelCase) e acrescido reset autouse entre testes. |
| Dockerfile `python:3.11-slim` + uvicorn | plan (Python 3.11 + uvicorn) | — |
| requirements: fastapi, uvicorn, pytest, httpx | tarefa de consolidação | **Conflito:** constitution.md diz "sem dependências além de fastapi, uvicorn e pytest", mas `httpx` é exigido pelo `TestClient` do FastAPI moderno; a instrução da tarefa prevalesceu. |

## Arquivos gerados em `app/`

- `main.py` — app FastAPI e rotas (UC1–UC4)
- `models.py` — dataclasses e serialização camelCase
- `service.py` — regras de negócio e códigos de erro por exceção
- `store.py` — repositório em memória (de janela-plan, + `clear()`)
- `test_app.py` — T1–T11
- `requirements.txt`, `Dockerfile`, `README.md`
