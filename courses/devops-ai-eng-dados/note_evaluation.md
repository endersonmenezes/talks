---
title: Método de Avaliação — DevOps e MLOps para Engenharia de Dados
type: knowledge
status: active
area: career
project: devops-mlops-eng-dados
tags:
  - kind/knowledge
  - area/career
  - project/devops-mlops-eng-dados
  - resource/devops
  - resource/mlops
  - resource/data-engineering
  - status/active
created: 2026-04-15
updated: 2026-06-08
---

← [[note_devops_mlops_eng_dados|Voltar ao Índice]]

# Método de Avaliação

## Filosofia

A avaliação é **100% baseada em projeto prático**, entregue via repositório GitHub. Não há prova teórica. O foco é demonstrar competência prática em DevOps/MLOps aplicado a engenharia de dados.

> **Pontuação:** Total de **100 pontos** = nota final direta. Os critérios abaixo detalham a distribuição.

## Projeto Incremental

O aluno desenvolve **um único projeto** ao longo dos 3 encontros, evoluindo-o progressivamente:

| Encontro | Incremento | Volume Estimado |
|---|---|---|
| 1 | Pipeline containerizado (ingestão + transformação) | ~30% do trabalho |
| 2 | CI (lint/test/build/validação) + operação local no Kind | ~35% do trabalho |
| 3 | MLOps (tracking, versionamento de dados e serving) | ~35% do trabalho |

> ⚠️ A tabela acima indica o **volume de trabalho** por encontro, não o peso na nota. A nota é calculada pelos **critérios de avaliação** abaixo.

## Critérios de Avaliação

### 1. Repositório GitHub (30%)

| Subcritério | Pontos | Descrição |
|---|---|---|
| Estrutura do repositório | 8 | Organização, `.gitignore`, `Makefile`/scripts |
| Qualidade dos commits | 7 | Conventional Commits, mensagens claras, histórico limpo |
| README | 10 | Instruções de setup, arquitetura, decisões técnicas |
| Licença e metadados | 5 | LICENSE, badges e descrição clara do projeto |

### 2. CI Funcional + Operação Local (25%)

| Subcritério | Pontos | Descrição |
|---|---|---|
| Pipeline de CI | 10 | lint → test → build → scan → validate |
| Testes automatizados | 8 | Unitários + data quality |
| Operação local e rollback | 7 | Validação de manifests no CI + deploy no Kind via Makefile + rollback local documentado |

### 3. Pipeline de Dados End-to-End (25%)

| Subcritério | Pontos | Descrição |
|---|---|---|
| Ingestão de dados | 6 | API → raw storage funcional |
| Transformação | 6 | Limpeza, tipagem, agregações |
| Data quality | 5 | Expectations/checks configurados |
| ML integration | 8 | Treino, tracking, serving funcional |

### 4. Documentação e Decisões Técnicas (20%)

| Subcritério | Pontos | Descrição |
|---|---|---|
| ADRs (Architecture Decision Records) | 8 | Decisões documentadas com contexto e trade-offs |
| Diagrama de arquitetura | 7 | Visual do pipeline end-to-end |
| Troubleshooting | 5 | Problemas encontrados e soluções |

## Escala de Notas

| Faixa | Conceito | Descrição |
|---|---|---|
| 90 - 100 | A | Excelente — pipeline completo, bem documentado, CI robusto e operação local consistente |
| 75 - 89,9 | B | Bom — pipeline funcional com documentação adequada |
| 60 - 74,9 | C | Suficiente — funciona mas com lacunas em qualidade/documentação |
| < 60 | D | Insuficiente — pipeline incompleto ou não funcional |

## Reposição de Faltas

- Cada encontro tem **atividade de reposição** documentada na nota do respectivo encontro.
- A reposição deve ser entregue **antes do próximo encontro** (para Encontros 1 e 2) ou em **2 semanas** (Encontro 3).
- **Nota máxima da reposição:**
  - Com justificativa documentada (atestado, trabalho...): **100%**
  - Sem justificativa: **80%** (incentivo à presença)
- A reposição inclui evidências em vídeo (5min para E1/E2, 10min para E3) explicando decisões técnicas.
- **Canal de dúvidas:** alunos em reposição podem buscar suporte via Issues no repositório da turma.

## Entrega Final

- **Formato:** Repositório público no GitHub
- **Prazo:** 2 semanas após o Encontro 3
- **Conteúdo mínimo:**
  - Código funcional (pipeline rodando via compose)
  - CI green no GitHub Actions com lint, testes e validação de manifests
  - Deploy local documentado no Kind via Makefile (`deploy`, `status`, `rollback`)
  - README completo com instruções e arquitetura
  - Pelo menos 3 ADRs documentando decisões
  - Evidência de MLflow tracking (screenshots ou export)

## Bônus (até +10 pontos extras)

> 💡 **Nota:** Os pontos bônus servem para compensar eventuais perdas em outras categorias. A nota final máxima absoluta da disciplina é estrita a 100 pontos.

| Bônus | Pontos |
|---|---|
| Implementar monitoramento de data drift | +3 |
| Adicionar Helm charts para deploy | +3 |
| Implementar pipeline com Dagster ou Airflow | +2 |
| Contribuir com melhoria no repositório template da turma | +2 |
