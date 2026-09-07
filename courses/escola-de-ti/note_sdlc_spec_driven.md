---
title: SDLC e Spec-Driven Development — Nota de Apoio
type: note
status: active
area: career
project: escola-de-ti
tags:
  - kind/note
  - area/career
  - project/escola-de-ti
  - resource/sdlc
  - resource/spec-driven
  - status/active
created: 2026-09-07
updated: 2026-09-07
---
# SDLC e Spec-Driven Development — Nota de Apoio

← [[note_escola_de_ti|Voltar à Visão Geral]]

Nota de apoio para as equipes sobre **gestão do ciclo de vida de desenvolvimento (SDLC)**
e o desafio opcional de **Spec-Driven Development (SDD)** na fase de código.

## 🔄 Gestão do SDLC (obrigatório como decisão, não como método fixo)

Cada equipe deve **definir e documentar seu próprio processo de desenvolvimento**,
não apenas entregar código. Espera-se que escolham e justifiquem (via ADR):

- **Fluxo de trabalho**: como uma tarefa nasce, é desenvolvida e chega até a branch principal
  (ex.: issues → branches → pull requests → code review → merge).
- **Estratégia de branches**: feature branches, trunk-based development, git flow — e por quê.
- **Integração contínua (CI)**: o que roda automaticamente a cada mudança (testes, lint, build).
- **Definition of Done**: o que significa "pronto" para a equipe (testado? revisado? documentado?).

> A cobrança é sobre a **capacidade de governar o próprio ciclo de vida** e justificar
> decisões — não sobre adotar um método específico.

## 🌱 Spec-Driven Development (desafio opcional)

O Thoughtworks Technology Radar (nov/2025) colocou SDD no anel **Assess**:
vale explorar, ainda não é padrão. Perfeito como desafio para as equipes.

Böckeler (Thoughtworks / martinfowler.com) descreve um espectro de maturidade:

| Nível | O que é |
| --- | --- |
| **Spec-first** | A spec guia a geração inicial do código e depois pode ser descartada |
| **Spec-anchored** | A spec é um artefato vivo, versionado e mantido em sincronia com o código |
| **Spec-as-source** | A spec é a fonte única da verdade, do qual o código é gerado |

### Referência prática: GitHub Spec Kit

Toolkit open source com fluxo estruturado em 4 artefatos:

1. `/speckit.specify` — gera a especificação da funcionalidade
2. `/speckit.plan` — plano técnico/arquitetura
3. `/speckit.tasks` — quebra o plano em tarefas
4. `/speckit.implement` — implementa a partir das tarefas

Inclui ainda uma **"constituição" do projeto** (regras persistentes: padrões de teste,
estilo de código, restrições de UX) aplicada a todas as specs futuras.

### 🎯 O desafio

- Escolher **um nível do espectro** (ou outra abordagem) e justificar via ADR:
  qual problema do time a spec resolve? Qual o custo de mantê-la?
- Manter as specs **versionadas junto ao código** (mesmo repositório).
- Registrar no que deu certo/errado — material para a apresentação final.

## 🔗 Ligações

- Artefatos exigidos: [[note_escola_de_ti]]
- Justificativas de decisão: ADRs (ver [[note_bibliography]])
- Avaliação: [[avaliacao_01_artefatos]]
