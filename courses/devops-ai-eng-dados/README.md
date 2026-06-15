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

Disciplina para pós-graduação/especialização em Engenharia de Dados.

## 📂 Estrutura

| Arquivo                                                            | Descrição                                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| [`note_devops_mlops_eng_dados.md`](note_devops_mlops_eng_dados.md) | 📋 **Índice / Ementa** — visão geral, objetivos, pré-requisitos, projeto incremental |
| [`note_class_01.md`](note_class_01.md)                             | 📅 **Encontro 1** — Fundamentos DevOps: containers, Podman, Git, IaC                 |
| [`note_class_02.md`](note_class_02.md)                             | 📅 **Encontro 2** — CI, Kubernetes local (Kind), DataOps e data quality              |
| [`note_class_03.md`](note_class_03.md)                             | 📅 **Encontro 3** — MLOps: MLflow, DVC e model serving                               |
| [`note_evaluation.md`](note_evaluation.md)                         | 📊 **Avaliação** — rubrica, pesos, reposição de faltas, bônus                        |
| [`note_bibliography.md`](note_bibliography.md)                     | 📚 **Bibliografia** — 15 livros, 7 papers (DOI), whitepapers, docs oficiais          |
| `assets/`                                                          | 📎 Anexos (slides, diagramas, materiais de apoio)                                    |

## 🎯 Formato

- **3 encontros de ~10h** (4h teoria + 4h prática + intervalos)
- **Projeto incremental** via GitHub (pipeline de dados end-to-end)
- **Avaliação 100% prática** — sem prova teórica
- **Ferramentas open source**: Podman, Kind, GitHub Actions, MLflow, DVC
- **Operação do curso**: CI no GitHub Actions e deploy local no Kind via Makefile

## 🧰 Artefatos-base esperados

- **Repositório-template da turma** com scaffolding do projeto e TODOs para realizar.
- **Dataset-base ou API recomendada** para os labs
- **Template de ADR** para documentar decisões técnicas
- **Kit local de operação** com workflow de CI, manifests `k8s/` e `Makefile`

## 🗺️ Mapa de Navegação

```
note_devops_mlops_eng_dados (índice)
├── note_class_01 (DevOps fundamentals)
├── note_class_02 (CI + Kubernetes local)
├── note_class_03 (MLOps)
├── note_evaluation (método de avaliação)
└── note_bibliography (referências)
```

O arquivo `note_devops_mlops_eng_dados.md` é o ponto de entrada — contém wikilinks (`[[...]]`) para todas as outras notas.