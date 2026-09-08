---
title: Escola de TI
type: index
status: active
area: career
project: escola-de-ti
tags:
  - kind/index
  - area/career
  - project/escola-de-ti
  - resource/teaching
  - status/active
created: 2026-09-07
updated: 2026-09-07
---
# Escola de TI

Disciplina do curso de **Engenharia de Software** da **UniCesumar**, lecionada em 2026.
Simula o dia a dia de trabalho e a organização de um projeto de software, desenvolvido **em equipes**.

**Turmas em 2026:** 2 turmas.

## 🎯 Filosofia da Disciplina

- A indicação de ferramentas e metodologias é sempre uma **sugestão**.
- Os alunos são **desafiados a resolverem e explorarem seus próprios problemas**, como em um time real.

## 📂 Estrutura

| Arquivo | Descrição |
| --- | --- |
| [`note_escola_de_ti.md`](note_escola_de_ti.md) | 📋 **Visão Geral** — contexto, filosofia e artefatos exigidos por fase |
| [`note_sdlc_spec_driven.md`](note_sdlc_spec_driven.md) | 🔄 **SDLC + Spec-Driven Development** — nota de apoio para a fase de código |
| [`note_bibliography.md`](note_bibliography.md) | 📚 **Bibliografia** — 24 livros, 4 papers (DOI), artigos/guias oficiais e docs de ferramentas |
| [`evaluation/evaluation_01_artifacts.md`](evaluation/evaluation_01_artifacts.md) | 📊 **Avaliação 1** — Artefatos (sem nota direta — base e alavanca das demais avaliações) |
| [`evaluation/evaluation_02_peer_review_360.md`](evaluation/evaluation_02_peer_review_360.md) | 📊 **Avaliação 2** — Avaliação 360 (formulários quinzenais via WhatsApp) |
| [`evaluation/evaluation_03_clockify.md`](evaluation/evaluation_03_clockify.md) | 📊 **Avaliação 3** — Relatórios do Clockify (tempo × retorno, marco de 1000h/equipe) |
| [`evaluation/evaluation_04_practical_exam.md`](evaluation/evaluation_04_practical_exam.md) | 📊 **Avaliação 4** — Prova Prática (3 carreiras: SDD, Debugging, CRUD com juiz de testes) |
| [`evaluation/evaluation_05_presentation.md`](evaluation/evaluation_05_presentation.md) | 📊 **Avaliação 5** — Apresentação com o professor (60% grupo / 40% direcionadas) |
| [`evaluation/question_bank_evaluation_05.md`](evaluation/question_bank_evaluation_05.md) | ❓ **Banco de questões de exemplo** (estudo para a Avaliação 5) |
| [`evaluation/evaluation_06_jury_presentation.md`](evaluation/evaluation_06_jury_presentation.md) | 📊 **Avaliação 6** — Banca de Apresentação (auditório Dona Etelvina, com jurados) |
| [`evaluation/jury_scorecard.md`](evaluation/jury_scorecard.md) | 🏆 **Ficha dos jurados** (estilo hackathon) |
| [`classes/2026/README.md`](classes/2026/README.md) | 🏫 **Turmas 2026** — registro das equipes por turma (A: 8 equipes, B: 7 equipes) |

## 🗺️ Mapa de Navegação

Visão geral da árvore — contexto para quem (ou o que) for explorar a pasta:

```
escola-de-ti/
├── README.md                    ← você está aqui (índice)
├── note_escola_de_ti.md         ← visão geral: filosofia, fases e artefatos exigidos
├── note_sdlc_spec_driven.md     ← apoio de conteúdo: SDLC + Spec-Driven Development
├── note_bibliography.md         ← bibliografia (livros, papers, docs de ferramentas)
│
└── evaluation/                  ← TODAS as avaliações vivem aqui
    ├── evaluation_01..06      ← 6 métodos de avaliação (notas e regras de cada um)
    ├── question_bank_evaluation_05.md  ← questões de exemplo (estudo p/ Avaliação 5)
    ├── jury_scorecard.md          ← ficha hackathon dos jurados (Avaliação 6)
    │
    └── practical_exam/examples/  ← exemplos executáveis da Avaliação 4 (prova prática)
        ├── track-01-sdd/     ← prova de Spec-Driven Development
        │   ├── example-problem.md     ← enunciado de exemplo (formato, não é a prova real)
        │   ├── example-response/       ← markdowns de spec escritos por "aluno" exemplo
        │   ├── example-generated-code/  ← código gerado por agentes a partir dos specs
        │   └── example-tests/         ← suíte do professor + compose (correção containerizada)
        ├── track-02-debugging/   ← prova de debugging (Java; repo com erros, gabarito, containers)
        └── track-03-crud/    ← prova de CRUD com juiz de testes (suíte pública + implementação de referência)

classes/2026/                     ← registro das turmas de 2026
├── class_a.md                   ← 8 equipes (Anjo Nexus, Ergane, Limio, Nexus Athlete, Sauf BR, Synapse, Uniclass, Vitryne)
└── class_b.md                   ← 7 equipes (Cromocard, Lhamalog, Hospet, Mindliner, Busca Peça, Steely, Jaguara)
```

**Para agents:** o material é 100% Markdown + exemplos de código executáveis. Os arquivos de avaliação (`evaluation_0X`) são a fonte da verdade sobre notas e regras; os exemplos em `practical_exam/examples/` ilustram o formato e **não refletem os problemas reais da prova**.

> ⚖️ Pesos e composição da nota final: **a definir** (ver `note_evaluation.md` quando criado).
