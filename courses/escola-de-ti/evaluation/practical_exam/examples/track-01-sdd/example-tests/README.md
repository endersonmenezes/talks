---
title: "Correção da Carreira 01 — Exemplo Real Executado"
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
# Correção da Carreira 01 — exemplo real executado (correção multi-agentica)

> ⚠️ **Tudo nesta pasta é um EXEMPLO de formato**: o problema, o contrato, os
> casos de teste e os valores da prova real são **diferentes**. A suíte real é
> publicada apenas na correção (categorias B e C não são reveladas antes).

Esta pasta documenta e executa a correção da prova de **Spec-Driven Development (SDD + TDD)**
do repositório-modelo `../example-response/` (o "aluno"). Tudo aqui foi de fato executado.

## 🔁 O fluxo de correção (multi-agentic)

```
spec.md, plan.md, tests.md, constitution.md   (o que o ALUNO entregou — só .md)
        │
        ▼  ① cada .md sozinho, numa janela de contexto isolada (mesmo modelo p/ todos)
window-constitution/  window-spec/  window-plan/  window-tests/
        │
        ▼  ② consolidação (assembly) — resolve conflitos entre janelas
example-generated-code/app/   (+ PROVENANCE.md: de onde veio cada decisão)
        │
        ▼  ③ suíte do professor, EM CONTAINER (docker/podman) — não depende da máquina do professor
grading_suite.py → relatório A/B/C/D
```

### Por que container na correção?

`compose-tests.yaml` sobe o app do aluno + a suíte em containers. O resultado da correção
não depende do que está instalado na máquina do professor — qualquer ambiente com
Docker/Podman reproduz a mesma correção.

```bash
# Docker
docker compose -f compose-tests.yaml up --build --abort-on-container-exit
# Podman
podman-compose -f compose-tests.yaml up --build --abort-on-container-exit
```

## 📊 Resultado real deste exemplo (executado)

`16 passed, 1 failed`:

| Categoria | O que mede | Resultado |
| --- | --- | --- |
| **A — Contrato REST** (6 testes) | UC1–UC4 do spec.md: endpoints, status codes, listagens | ✅ passou |
| **B — Bordas escondidas** (6 testes) | limites exatos (1h/3h), adjacência, 1min de sobreposição, arredondamento, cancelamento | ✅ passou |
| **C — Requisito oculto** (1 teste) | enunciado pede `telefone` do cliente; **spec.md não tem UC de clientes** | ❌ falhou (proposital) |
| **D — SDLC estático** (4 testes) | Dockerfile, README com docker/podman, requirements, testes do próprio aluno | ✅ passou |

### 🎓 O que a falha de C1 ensina (e é o coração da prova)

O código gerado **só tem o que a spec manda**. Como `spec.md` não especificou o UC de
clientes com `telefone` (o enunciado pedia, mas o aluno não transformou em spec), o
modelo gerou `/clients` com `name` + `email` — e o requisito do enunciado se perdeu.

Na correção real isso vira rubrica: *a spec precisa cobrir o que o enunciado exige*.
Os testes "escondidos" (categoria B e C) são o mecanismo que pune spec incompleta —
exatamente como em juízes online.

### 🔀 Conflitos reais entre janelas (documentados em `../example-generated-code/app/PROVENANCE.md`)

- **Idioma dos endpoints**: window-tests criou `/quadras` e `/reservas`; spec/constitution usavam `/courts`, `/bookings`. O contrato venceu.
- **Regras de duração**: window-plan gerou 30min–4h; spec manda 1h–3h. A spec venceu.
- **Status codes**: window-plan mapeava tudo para 422; a spec exige 400/404/409 distintos.
- **IDs**: uuid (window-spec) vs. inteiros sequenciais (window-plan) — prevaleceu o plano.

## ⚠️ Ressalva do exemplo

A jornada é demonstrativa: numa prova real, **o aluno não tem a fase ②** — ele mesmo
instrui o modelo a montar o código (são os "comandos instruídos pelo aluno"). Aqui o
assembly separado existe só para deixar o exemplo executável e didático.
