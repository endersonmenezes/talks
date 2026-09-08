	# Contrato de exemplo — API de Tarefas (Gerenciador de Tarefas)

> Este é o tipo de documento que o aluno recebe na Carreira 03.
> A suíte do professor (2 testes públicos + testes escondidos) valida este contrato
> executando o código do aluno em container.

## Base URL

`http://localhost:8080`

## Endpoints

### Criar tarefa — `POST /tasks`

- Body JSON: `{ "titulo": string (obrigatório, não vazio), "descricao": string (opcional) }`
- Respostas:
  - `201 Created` → `{ "id": int, "titulo": string, "descricao": string, "concluida": false }`
  - `400 Bad Request` → titulo ausente ou vazio

### Listar tarefas — `GET /tasks`

- Resposta `200 OK` → array de tarefas (pode ser vazio `[]`)

### Obter tarefa — `GET /tasks/{id}`

- `200 OK` → tarefa
- `404 Not Found` → id inexistente

### Atualizar tarefa — `PUT /tasks/{id}`

- Body: `{ "titulo"?: string, "descricao"?: string, "concluida"?: boolean }`
- `200 OK` → tarefa atualizada
- `404 Not Found` → id inexistente

### Remover tarefa — `DELETE /tasks/{id}`

- `204 No Content`
- `404 Not Found` → id inexistente

## Notas

- IDs são inteiros sequenciais, começando em 1.
- Persistência pode ser **em memória** — a suíte sobe um container fresco por execução.
- Entregar `Dockerfile` com instruções de subida é **super recomendado** (evita que o
  ambiente do aluno impeça a suíte de rodar).
