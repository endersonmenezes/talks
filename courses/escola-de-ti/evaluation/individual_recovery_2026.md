---
title: "Recuperação Individual — Prova Prática e Entrevista"
type: evaluation
status: active
area: career
project: escola-de-ti
tags:
  - kind/evaluation
  - area/career
  - project/escola-de-ti
  - status/active
created: 2026-11-24
updated: 2026-11-24
---
# Recuperação Individual — Prova Prática e Entrevista

Avaliação individual para consolidação das competências da disciplina, composta
por uma **prova prática online de sete dias** e uma **entrevista presencial de
até 60 minutos**. O trabalho combina pesquisa, especificação, implementação,
testes, debugging, integrações e organização do processo no GitHub.

Este guia é público e pode ser compartilhado com o aluno. O enunciado operacional
completo está na track do sistema de provas; respostas de referência e o roteiro
detalhado do entrevistador permanecem no material privado do professor.

## 1. Composição da nota

| Etapa | Formato | Valor | Peso |
| --- | --- | ---: | ---: |
| Prova prática | Online, individual, 7 dias corridos | 0–100 | 50% |
| Entrevista | Presencial, individual, até 60 minutos | 0–100 | 50% |

```text
nota final = 0,5 × nota da prova prática + 0,5 × nota da entrevista
```

O resultado final é arredondado half-up para inteiro. As duas etapas são
necessárias: a entrevista não substitui a entrega, e uma entrega sem defesa
técnica não compõe sozinha a recuperação.

## 2. Prova prática online

- **Tema:** plataforma “Conecta Comunidade”, com parceiros, projetos de extensão
  e atividades.
- **Janela:** 10.080 minutos, equivalentes a 7 × 24 horas.
- **Início:** commit do bot `chore: aplicar prova …`.
- **Entrega:** repositório Git com aplicação, testes, documentação, pesquisa e
  evidências do processo.
- **Stack:** livre, desde que seja possível executar localmente e em container
  seguindo o README.
- **Frontend:** não exigido.
- **Consulta:** permitida, com rastreabilidade obrigatória.

### O que será avaliado

| Critério | Pontos |
| --- | ---: |
| SDD, arquitetura, OpenAPI e ADRs | 15 |
| CRUD, relacionamentos e regras de negócio | 20 |
| TDD e qualidade dos testes | 15 |
| Quatro casos de debugging | 10 |
| Integrações, idempotência e resiliência | 15 |
| GitHub e organização do SDLC | 10 |
| Pesquisa aplicada | 5 |
| Containerfile | 5 |
| README | 5 |
| **Total** | **100** |

A prova foi dimensionada para exigir trabalho distribuído. O processo mínimo
inclui 8 issues significativas, 6 pull requests integrados, 18 commits úteis e
atividade em pelo menos 3 dias diferentes. Esses números não substituem qualidade
nem rastreabilidade.

### Pesquisa obrigatória

O enunciado contém 14 missões de investigação. O aluno deve responder a pelo
menos 12, reunindo:

- 15 fontes distintas;
- 8 fontes primárias/oficiais;
- 6 missões com duas fontes confrontadas;
- 10 aplicações práticas localizáveis em código, teste, ADR ou PR;
- registro completo em `docs/pesquisa.md` e `FONTES.md`.

A pesquisa precisa mostrar pergunta → aprendizado → decisão → evidência. Uma
lista de links sem aplicação não atende ao objetivo.

### Implementação e testes

A solução inclui CRUD com persistência, relatórios, consulta de CEP, publicação
em webhook, tratamento de falhas, idempotência e concorrência. Os testes devem
usar servidores simulados e **não podem depender de internet**.

São exigidos pelo menos três ciclos TDD red–green–refactor identificáveis no
histórico e 30 casos automatizados significativos, incluindo integração, erros e
casos de borda. Commits vermelhos intermediários fazem parte da evidência de TDD;
o HEAD final precisa estar verde.

## 3. Como acessar e entregar

1. Acesse o repositório que o professor criou para você a partir do template
   `endersonmenezes/exam-escola-ti`.
2. Complete a identidade e o checklist da issue “🎯 Prova”.
3. Comente:

   ```text
   /track track-05-recuperacao-individual
   ```

4. Aguarde o commit de aplicação e o comentário com a variante.
5. Clone/puxe o repositório depois da aplicação e leia o `ENUNCIADO.md` inteiro.
6. Trabalhe com issues, branches e pull requests, integrando tudo à branch
   padrão antes do encerramento.
7. Atualize `README.md`, `FONTES.md` e as evidências no estado final.
8. Execute `/auto-correcao` ao menos uma vez depois do último push.
9. Feche a issue “🎯 Prova” dentro da janela para gerar o `teacher.json`.

**Enunciado público da track:**

- [README da track](exam-escola-ti/exams/2026/track-05-recuperacao-individual/README.md)
- [ENUNCIADO completo](exam-escola-ti/exams/2026/track-05-recuperacao-individual/ENUNCIADO.md)
- [Contrato máquina-legível](exam-escola-ti/exams/2026/track-05-recuperacao-individual/contrato.json)
- [Rubrica](exam-escola-ti/exams/2026/track-05-recuperacao-individual/rubrica.json)
- [Regras comuns](exam-escola-ti/docs/REGRAS.md)

## 4. Entrevista presencial

- **Duração:** até 60 minutos.
- **Formato:** conversa técnica individual, navegação no repositório, execução
  de testes/fluxos e uma pequena atividade prática no próprio código.
- **Data e local:** combinados diretamente com o professor.
- **Material permitido:** o próprio repositório, ambiente de desenvolvimento e
  consulta pontual à documentação quando autorizada pelo professor.
- **Não permitido:** agente de IA editando arquivos, executando comandos ou
  operando o GitHub no lugar do aluno.

### O que a entrevista avalia

| Dimensão | Pontos |
| --- | ---: |
| Compreensão e autoria da solução | 25 |
| SDD, CRUD e regras de negócio | 15 |
| TDD e debugging | 15 |
| Integrações, resiliência e concorrência | 20 |
| Pesquisa, GitHub e trade-offs | 10 |
| Exercício prático curto | 15 |
| **Total** | **100** |

A entrevista não exige decorar sintaxe, números de RFC ou comandos. O foco é
explicar decisões, demonstrar comportamento, diagnosticar problemas e trabalhar
sobre o código entregue.

### Como se preparar

- Deixe o projeto e as dependências funcionando no computador que será usado.
- Teste o container e a execução local antes da entrevista.
- Prepare os mocks de ViaCEP e webhook sem depender de serviços reais.
- Revise seus ADRs, ciclos de TDD, diagnósticos e PRs.
- Saiba localizar requisito → teste → implementação → issue/PR.
- Revise como sua solução trata falhas, duplicidade e concorrência.
- Esteja pronto para explicar limitações e o que faria com mais tempo.
- Não é necessário preparar slides nem levar informações sobre o afastamento.

## 5. Consulta, IA e integridade

As regras comuns da disciplina continuam valendo:

1. Sites e documentação usados devem aparecer em `FONTES.md` como linha numerada
   da tabela, com URL, conteúdo e local de aplicação.
2. IA como consulta exige conversa compartilhada por link público/acessível,
   registrada em `FONTES.md`.
3. IA como agente é proibida e zera a prova.
4. Conteúdo copiado ou gerado sem declaração configura plágio.
5. O trabalho é individual; não compartilhe código, testes ou diagnósticos.
6. Não altere `scripts/`, `.github/`, arquivos de regras, contrato, rubrica,
   track ou enunciado.
7. Não crie workflows próprios em `.github/`; utilize os Actions existentes.
8. Não versione segredos nem use dados pessoais reais em exemplos e testes.
9. Você deve conseguir explicar qualquer trecho entregue, inclusive os que
   nasceram de uma consulta.

## 6. Checklist resumido

### Antes de começar

- [ ] Li o enunciado inteiro e entendi a janela de sete dias.
- [ ] Conferi minha variante em `variante/params.json`.
- [ ] Planejei pesquisa, especificação, implementação, revisão e entrega.
- [ ] Criei o mapa inicial de issues e requisitos.

### Durante a semana

- [ ] Registrei fontes e aplicações no momento em que as utilizei.
- [ ] Fiz commits e PRs pequenos, ligados às issues e requisitos.
- [ ] Vi os testes falharem antes das implementações dos ciclos TDD.
- [ ] Testei falhas de rede, timeout, duplicidade e concorrência com mocks.
- [ ] Mantive o trabalho distribuído em pelo menos três dias.

### Antes de fechar

- [ ] Todo o trabalho está integrado à branch padrão.
- [ ] A suíte completa está verde no HEAD final.
- [ ] O container sobe em ambiente limpo e preserva dados no volume.
- [ ] OpenAPI, ADRs, pesquisa, debugging e evidências estão atualizados.
- [ ] `FONTES.md` não tem placeholder nem consulta omitida.
- [ ] O README explica execução, configuração, testes, mocks e limitações.
- [ ] Não alterei nenhum caminho protegido.
- [ ] Executei `/auto-correcao` depois do último push.

### Para a entrevista

- [ ] O projeto executa no computador que levarei.
- [ ] Consigo rodar testes e demonstrar o fluxo principal.
- [ ] Consigo explicar minhas decisões e as fontes que as influenciaram.
- [ ] Consigo modificar uma pequena parte do código com teste, sem agente de IA.
