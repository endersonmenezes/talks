---
title: "Evaluation 04 — Practical Exam"
type: evaluation
status: active
area: career
project: escola-de-ti
tags:
  - kind/evaluation
  - area/career
  - project/escola-de-ti
  - status/active
created: 2026-09-07
updated: 2026-09-08
---
# Avaliação 04 — Prova Prática (3 carreiras)

Prova **individual**, **sem internet**, em ambiente controlado. Duração: **1 período de aulas**
(2 aulas sequenciais — as 2 primeiras ou as 2 últimas, dependendo da turma).
Entrega via repositório Git (local ou remoto, conforme infraestrutura da sala).

> 🛤️ **Cada aluno escolhe 1 carreira** e entrega tudo dentro dela. As carreiras testam
> competências distintas — especificar, diagnosticar, implementar — e o aluno alinha
> a prova à sua trajetória.

## 🧮 Regras Comuns de Nota (valem para as 3 carreiras)

1. **Nota da prova: 0–100**, soma dos critérios da carreira escolhida. A prova
   **contabiliza na montagem da nota total** da disciplina, junto às demais avaliações
   (peso global a definir em `note_evaluation.md`).
2. **Pontuação proporcional**: em critérios baseados em testes ou em erros corrigidos,
   a nota do critério = `(itens atingidos / itens totais) × pontos do critério`.
3. **Critérios objetivos**: não há nota subjetiva. Dúvida de correção é resolvida
   **reexecutando a suíte/comando** — não por negociação.
4. **Arredondamento**: nota final da prova arredondada para o inteiro mais próximo
   (0,5 arredonda para cima).
5. **Zera a prova (nota 0)**: cópia/plágio entre alunos; acesso à internet durante a prova;
   violação da restrição da carreira 01 (código-fonte entregue fora do previsto).

---

## 🛤️ Carreira 01 — Spec-Driven Development (SDD + TDD)

**Conceito**: o aluno não escreve código diretamente. Escreve **especificações em Markdown**
que, passadas por um modelo de IA fixo, geram o código. Avalia-se a capacidade de **especificar**.

**Dinâmica**:
1. Recebe um **problema fechado** — que **inclui seu contrato publicado** (rotas, campos, status codes; ver o formato em [`examples/track-01-sdd/example-problem.md`](practical_exam/examples/track-01-sdd/example-problem.md)). O problema da prova real é **diferente** do exemplo.
2. Cria um repositório contendo **apenas arquivos `.md`**, com estrutura SDD+TDD:
   - `constitution.md` — regras persistentes do projeto (padrões, estilo, restrições)
   - `spec.md` — requisitos, casos de uso, critérios de aceite
   - `plan.md` — arquitetura, stack, decisões
   - `tests.md` — cenários de teste com casos de borda
   - `tasks.md` — decomposição em tarefas
3. Cada `.md` gerador é submetido ao **mesmo modelo, na mesma janela de contexto individual**
   (configuração idêntica para todos — a spec precisa bastar por si só).
4. O código gerado deve seguir boas práticas de SDLC e **passar na suíte de testes do professor**
   (idêntica para todos os alunos).

### 🧮 Base de Notas — Carreira 01 (0–100)

O código é gerado a partir dos `.md` do aluno e avaliado pela **suíte do professor**
(categorias A–D, executada em container — ver `example-tests/`), mais a qualidade
dos `.md` em si (critério E):

| Critério | Como é medido | Pontos |
| --- | --- | --- |
| **A — Contrato REST** | Suíte categoria A: endpoints, status codes e comportamento dos UC1–UC4 do enunciado | **30** |
| **B — Casos de borda** | Suíte categoria B: limites exatos, adjacência, arredondamento, conflitos mínimos (testes **não revelados** antes da prova) | **25** |
| **C — Requisitos do enunciado** | Suíte categoria C: tudo o que o enunciado pede **além dos casos de uso óbvios** (testes escondidos; expõe spec incompleta) | **15** |
| **D — SDLC do código gerado** | Suíte categoria D: Dockerfile com EXPOSE/CMD, README com instruções de execução, **manifesto de dependências do stack declarado** (requirements.txt, package.json, pom.xml, go.mod…), testes do próprio aluno presentes no código gerado | **15** |
| **E — Qualidade dos `.md` entregues** | **3 pts por arquivo bem criado, máximo de 5 arquivos pontuáveis** (qualquer `.md` do repo conta — não há lista obrigatória de arquivos) | **15** |

**Detalhamento do critério E** (0–15): cada arquivo `.md` presente e "bem criado" vale 3 pts, até o teto de 5 arquivos (15 pts).
**"Bem criado" é verificado mecanicamente** por um checklist mínimo publicado com a prova — sem julgamento de estilo. Exemplo de checklist (adaptável por problema):

| Tipo de arquivo | Critério mínimo mecânico |
| --- | --- |
| `constitution.md` | ≥ 1 regra operacional (padrão, restrição ou convenção) |
| `spec.md` | ≥ 1 critério de aceite **mensurável** por caso de uso/requisito |
| `plan.md` | ≥ 1 decisão técnica com justificativa |
| `tests.md` | ≥ 1 caso de borda por regra de negócio |
| `tasks.md` | ≥ 3 tarefas decompostas |
| *outro `.md`* | conteúdo estruturado que instrua a geração de código (headers + especificação concreta) |

> O aluno decide quantos arquivos criar e como nomeá-los — pontuam os 5 melhores que satisfizerem o checklist.

**Restrição explícita**: o repositório entregue deve conter **somente `.md`**
(o código é gerado **na correção**). Inserir **snippets curtos** de código para
elucidar o agente é aceitável; **implementações completas** em blocos de código
são rejeitadas pelo prompt de correção do professor (a carreira avalia *especificar*,
não *codar de improviso*). Se o essencial da solução vier como código pronto nos
`.md`, a carreira está invalidada → **nota 0 na prova** (regra comum 5).

---

## 🛤️ Carreira 02 — Debugging (Java Maven/Spring + React)

**Conceito**: recebe um repositório que **não compila / não sobe**, com erros deliberados
em camadas. Avalia o **método de debug**, não memória de sintaxe.

**Dinâmica**:
1. Recebe uma app pequena (Spring Boot + Maven no backend, React no frontend — ex.: cadastro de produtos),
   distribuída como **projeto Container + Compose (Docker/Podman)** — o container é a
   **interface de inserção de erros**: o professor controla exatamente onde a app quebra
   (build da imagem, arquivos de configuração dentro do container, startup) e garante que
   todos os alunos debugam o **mesmo ambiente** que será usado na correção.
2. O código contém erros introduzidos em 3 camadas — mapeadas no ciclo de vida do container:
   - **Compilação** → `docker compose build` falha (imports faltantes, tipos incompatíveis, assinaturas erradas, pom.xml com versões erradas)
   - **Configuração** → build ok, mas variáveis/ports/DB do `compose.yaml` ou `application.properties` impedem a subida
   - **Startup/lógica** → sobe e cai: bean mal configurado, CORS, rota quebrada no React — diagnóstico via `docker compose logs`
3. Ciclo esperado do aluno: `docker compose up` → ler logs → isolar → corrigir → `docker compose up --build`.
4. Objetivo: `docker compose up` **saudável de ponta a ponta** (backend + frontend),
   e suíte smoke do professor passando **dentro do ambiente containerizado**.

### 🧮 Base de Notas — Carreira 02 (0–100)

A correção roda `docker compose up --build` no repositório do aluno, em ambiente
idêntico ao da prova:

| Critério | Como é medido | Pontos |
| --- | --- | --- |
| **App funcional ao final** | `docker compose up` sobe backend + frontend de ponta a ponta **e** a suíte smoke do professor passa | **30** |
| **Erros de compilação corrigidos** | Proporção dos erros da camada 1 que o build do aluno resolveu | **25** |
| **Erros de configuração corrigidos** | Proporção dos erros da camada 2 (compose/env/properties) resolvidos | **20** |
| **Erros de startup/lógica corrigidos** | Proporção dos erros da camada 3 (logs limpos, rotas funcionando) | **15** |
| **Método sistemático evidenciado** | Histórico Git (commits pequenos e mensagens que mostram hipótese→correção) **ou** relatório breve no README do repo | **10** |

**Regras de desempate e limites explícitos**:
- O critério "app funcional" vale **independentemente** dos demais: parcial conta
  (ex.: backend sobe, frontend não → o professor mede o que está de pé, com
  proporção dentro do critério, e os critérios por camada pontuam à parte).
- **Regressão**: se algo que funcionava na app original deixar de funcionar
  (quebrado pelo aluno), o critério "app funcional" (30 pts) vale **zero** —
  mesmo que tudo mais esteja perfeito. Debug não é "refazer a app".
- Critérios por camada contam erros corrigidos **sem quebrar outra camada**:
  um "conserto" que move o erro de camada não pontua como dois acertos.

---

## 🛤️ Carreira 03 — CRUD com suíte de testes (à la HackerRank)

**Conceito**: a suíte de testes **define o contrato**; o aluno implementa um CRUD na
linguagem/framework de sua escolha.

**Dinâmica**:
1. Recebe a **especificação do contrato** (endpoints, payloads, status codes, validações, casos de borda).
2. Implementa a API CRUD na linguagem escolhida.
3. A suíte do professor contém **2 testes públicos** (visíveis antes da prova) e **testes escondidos**
   (executados na correção, estilo juiz online) — pontos por caso de teste.
4. **Execução**: o professor clona o repositório do aluno, compila o código em **container
   (Docker/Podman)** e roda a suíte contra ele. Por isso, entregar com `Dockerfile`
   (e instruções de subida) é **super recomendado** — evita que o ambiente do aluno
   comprometa a execução da suíte.

### 🧮 Base de Notas — Carreira 03 (0–100)

| Critério | Como é medido | Pontos |
| --- | --- | --- |
| **Testes públicos** | 2 testes públicos da suíte passando (10 pts cada) | **20** |
| **Testes escondidos** | Proporção dos testes escondidos aprovados (`acertos/total × 60`) | **60** |
| **Dockerfile funcional** | Suíte sobe o container do aluno sem ajustes manuais | **15** |
| **README com instruções** | Como subir a API (local e container) documentado no repo | **5** |

**Regras explícitas**:
- **Suíte não executável = critérios de suíte valem 0**: se o código não sobe
  (nem via Dockerfile, nem seguindo o README), os 80 pts de testes **não são
  atribuídos** — não há correção manual de código nesta carreira.
- Se o código sobe **sem Dockerfile** (README permite subir manualmente), a suíte
  é executada assim mesmo, mas os 15 pts do Dockerfile valem **zero** — e o risco
  de divergência de ambiente é do aluno.
- Status code, formato de payload e validações errados contam como teste falho —
  não há "meio ponto" por estar "quase certo"; a suíte é binária por caso de teste.

---

## 📁 Exemplos

> ⚠️ **Aviso**: tudo nesta pasta existe para elucidar o **formato** da prova.
> Os problemas, contratos, suítes, valores e campos dos exemplos **não são os
> da prova real** — cada aplicação da prova usa problema e contrato próprios.

Subpasta [`practical_exam/examples/`](practical_exam/examples/) com exemplos **simples**,
só para mostrar a dinâmica de cada carreira:
- `track-01-sdd/` — problema de exemplo + mini-resposta-modelo (os 5 `.md`) + **exemplo de correção multi-agentica executada**: `example-generated-code/` (janelas isoladas → app consolidado + PROVENANCE.md) e `example-tests/` (suíte do professor A/B/C/D, com compose Docker/Podman — resultado real: 16 passaram, 1 falha proposital de requisito oculto)
- `track-02-debugging/` — arquivo Java minúsculo com 5 erros propositais + gabarito com jornada de debug verificada + exemplo de Container/Compose
- `track-03-crud/` — contrato de exemplo + suíte pública mini (pytest)

## ⚖️ Peso na Nota Total

A prova vale **0–100** e contabiliza na montagem da nota total com as demais
avaliações da disciplina. **Peso global: a definir** em `note_evaluation.md`.
