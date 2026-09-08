# Problema de exemplo — Sistema de Reservas de Quadras

> Este é o enunciado recebido pelo aluno na Carreira 01 (SDD + TDD).
> O repositório entregue deve conter **apenas arquivos `.md`** — ver `exemplo-resposta/`.

Uma arena esportiva precisa de um sistema de reservas de quadras.

## Requisitos

1. **Quadras**: cadastro com id, nome, tipo (futebol, vôlei ou basquete) e valor/hora.
2. **Clientes**: cadastro com id, nome e telefone.
3. **Reservas**: vinculam quadra + cliente + horário de início e fim.
4. **Regras de negócio**:
   - Duração mínima de 1h e máxima de 3h por reserva.
   - Não permitir reservas em horários passados.
   - Não permitir sobreposição de horários na mesma quadra.
   - Preço = valor/hora × duração, com frações de hora arredondadas para cima.
5. **Cancelamento**: uma reserva pode ser cancelada (ela deixa de aparecer nas listagens).
6. **Listagens**: reservas por quadra e reservas por dia.

## Contrato REST (formato de exemplo)

> Todo problema da Carreira 01 é entregue **com seu contrato publicado** — as
> rotas abaixo ilustram o formato. A prova real usa outro problema e outro contrato.

| Método | Rota | Descrição | Sucesso | Erros |
| --- | --- | --- | --- | --- |
| `POST` | `/courts` | Cadastrar quadra | `201` + JSON (camelCase) | `400` (valor/hora ≤ 0) |
| `GET` | `/bookings?courtId=` | Listar por quadra | `200` + array | — |
| `GET` | `/bookings?date=YYYY-MM-DD` | Listar por dia | `200` + array (só ativas) | — |
| `GET` | `/bookings/{id}` | Consultar reserva | `200` | `404` (cancelada/inexistente) |
| `POST` | `/bookings` | Criar reserva | `201` + preço calculado | `400` (regras), `409` (sobreposição) |
| `DELETE` | `/bookings/{id}` | Cancelar | — | `404` |

Convenções: JSON em **camelCase** (`courtId`, `pricePerHour`), datas ISO 8601,
IDs inteiros sequenciais.

## Restrições da prova

- O repositório deve conter **somente arquivos `.md`** (estrutura SDD+TDD: constitution, spec, plan, tests, tasks).
- O código será gerado por um modelo de IA a partir dos seus `.md` — a especificação precisa ser suficiente sozinha.
- O código gerado deve passar na **suíte de testes do professor**.
