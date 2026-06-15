---
title: DevOps e MLOps Aplicado a Engenharia de Dados
type: index
status: active
area: career
project: devops-mlops-eng-dados
tags:
  - kind/index
  - area/career
  - project/devops-mlops-eng-dados
  - resource/devops
  - resource/mlops
  - resource/data-engineering
  - status/active
created: 2026-04-15
updated: 2026-06-14
---

# DevOps e MLOps Aplicado a Engenharia de Dados

## Visão Geral

| Item              | Detalhe                                                                       |
| ----------------- | ----------------------------------------------------------------------------- |
| **Carga horária** | 30 horas                                                                      |
| **Período**       | Junho e Julho de 2026, com o apoio da [UNICIVE](https://unicive.com/)         |
| **Formato**       | 3 encontros de ~10h (~4h teoria + ~4h prática em sala + ~2h aplicação/tarefa) |
| **Público**       | Pós-graduação / Especialização (nível misto)                                  |
| **Infra**         | Open source local (Podman, Podman Compose, Kind)                              |
| **Avaliação**     | Projeto incremental via GitHub                                                |

## Objetivo Geral

Capacitar o aluno a projetar, automatizar e operar pipelines de dados e modelos de ML utilizando práticas de DevOps/MLOps com ferramentas open source, culminando em um projeto incremental versionado no GitHub.

## Pré-requisitos

- Python básico (funções, módulos, virtualenvs)
- SQL básico (SELECT, JOIN, GROUP BY)
- Git básico (clone, commit, push, pull)
- Familiaridade com terminal Linux/macOS

## Projeto Incremental (Fio Condutor)

Um **pipeline de dados end-to-end** que evolui a cada encontro:

| Encontro | Entrega do Projeto                                                                   |
| -------- | ------------------------------------------------------------------------------------ |
| 1        | Pipeline containerizado com ingestão e transformação de dados                        |
| 2        | CI para lint/test/build + validação de manifests + deploy local no Kind via Makefile |
| 3        | Integração com modelo ML (tracking, versionamento de dados e serving)                |

> [!TIP] Foco Personalizado
> Como o conteúdo é amplo, cada pessoa pode ter um objetivo diferente ao cursar a pós. O projeto incremental pode e deve explorar o que mais importa para você: se o seu foco é **DevOps e Automação**, dedique mais atenção às pipelines de CI/CD e aos manifests Kubernetes; se o foco é **Engenharia de Dados**, aprofunde-se mais na robustez dos scripts de ingestão e transformação do lab.

Para garantir fluidez, dividimos a carga prática em **Lab Guiado em Sala** (para garantir a infra e o 'Hello World' rodando) e **Desafio de Casa / Homework** (onde você aplica o conhecimento e expande a complexidade).

A entrega é feita via **repositório GitHub** com README, Containerfile, workflow de CI (GitHub Actions), automação local via Makefile e documentação de decisões.

## Artefatos-base do curso

- **Repositório oficial** — [endersonmenezes/pos-ia-eng-devops](https://github.com/endersonmenezes/pos-ia-eng-devops). Serve de base inicial com app Python, `Containerfile`, `compose.yaml`, `Makefile`, testes e estrutura de pastas. Ponto oficial para fork, Pull Requests, Issues e atividades de reposição.
- **Dataset-base ou API recomendada** — fonte padrão para evitar perda de tempo na escolha dos dados durante os labs.
- **Template de ADR** — modelo MADR em `docs/adr/` para padronizar as 3 decisões mínimas do projeto.
- **Kit de operação local** — workflow inicial de CI, manifests `k8s/` base e targets `make deploy`, `make status` e `make rollback`.

## Encontros

- [[note_class_01|Encontro 1 — Fundamentos DevOps para Engenharia de Dados]]
- [[note_class_02|Encontro 2 — CI, Kubernetes Local e DataOps]]
- [[note_class_03|Encontro 3 — MLOps e Operacionalização de Modelos]]

## Avaliação

→ Detalhes em [[note_evaluation|Método de Avaliação]]

| Critério | Peso |
|---|---|
| Repositório GitHub (código, commits, README) | 30% |
| CI funcional + operação local | 25% |
| Pipeline de dados end-to-end | 25% |
| Documentação e decisões técnicas | 20% |

## Bibliografia

→ Lista completa em [[note_bibliography|Bibliografia e Referências]]

## Notas

- Todas as ferramentas utilizadas são **open source**.
- Cloud é mencionada superficialmente para contextualização; foco é local.
- O CI valida código, testes e manifests; o deploy do curso é **local** no Kind, via Makefile.
- Atividades de reposição disponíveis para cada encontro (via repositório template).
