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
| [`evaluation/avaliacao_01_artefatos.md`](evaluation/avaliacao_01_artefatos.md) | 📊 **Avaliação 1** — Artefatos (sem nota direta — base e alavanca das demais avaliações) |
| [`evaluation/avaliacao_02_avaliacao_360.md`](evaluation/avaliacao_02_avaliacao_360.md) | 📊 **Avaliação 2** — Avaliação 360 (formulários quinzenais via WhatsApp) |
| [`evaluation/avaliacao_03_clockify.md`](evaluation/avaliacao_03_clockify.md) | 📊 **Avaliação 3** — Relatórios do Clockify (tempo × retorno, marco de 1000h/equipe) |
| [`evaluation/avaliacao_04_prova_pratica.md`](evaluation/avaliacao_04_prova_pratica.md) | 📊 **Avaliação 4** — Prova Prática (3 carreiras: SDD, Debugging, CRUD com juiz de testes) |
| [`evaluation/avaliacao_05_apresentacao.md`](evaluation/avaliacao_05_apresentacao.md) | 📊 **Avaliação 5** — Apresentação com o professor (60% grupo / 40% direcionadas) |
| [`evaluation/banco_questoes_avaliacao_05.md`](evaluation/banco_questoes_avaliacao_05.md) | ❓ **Banco de questões de exemplo** (estudo para a Avaliação 5) |
| [`evaluation/avaliacao_06_banca_apresentacao.md`](evaluation/avaliacao_06_banca_apresentacao.md) | 📊 **Avaliação 6** — Banca de Apresentação (auditório Dona Etelvina, com jurados) |
| [`evaluation/ficha_jurados_banca.md`](evaluation/ficha_jurados_banca.md) | 🏆 **Ficha dos jurados** (estilo hackathon) |

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
    ├── avaliacao_01..06         ← 6 métodos de avaliação (notas e regras de cada um)
    ├── banco_questoes_avaliacao_05.md  ← questões de exemplo (estudo p/ Avaliação 5)
    ├── ficha_jurados_banca.md          ← ficha hackathon dos jurados (Avaliação 6)
    │
    └── prova_pratica/exemplos/  ← exemplos executáveis da Avaliação 4 (prova prática)
        ├── carreira-01-sdd/     ← prova de Spec-Driven Development
        │   ├── problema-exemplo.md     ← enunciado de exemplo (formato, não é a prova real)
        │   ├── exemplo-resposta/       ← markdowns de spec escritos por "aluno" exemplo
        │   ├── exemplo-codigo-gerado/  ← código gerado por agentes a partir dos specs
        │   └── exemplo-testes/         ← suíte do professor + compose (correção containerizada)
        ├── carreira-02-debug/   ← prova de debugging (Java; repo com erros, gabarito, containers)
        └── carreira-03-crud/    ← prova de CRUD com juiz de testes (suíte pública + implementação de referência)
```

**Para agents:** o material é 100% Markdown + exemplos de código executáveis. Os arquivos de avaliação (`avaliacao_0X`) são a fonte da verdade sobre notas e regras; os exemplos em `prova_pratica/exemplos/` ilustram o formato e **não refletem os problemas reais da prova**.

> ⚖️ Pesos e composição da nota final: **a definir** (ver `note_evaluation.md` quando criado).
