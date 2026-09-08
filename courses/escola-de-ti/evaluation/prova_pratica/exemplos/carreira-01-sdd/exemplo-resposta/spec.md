# Spec — Sistema de Reservas de Quadras

## Casos de uso

**UC1 — Cadastrar quadra**
- Entrada: nome (string, obrigatório), tipo (`futebol` | `vôlei` | `basquete`), valor/hora (decimal > 0).
- Critérios de aceite:
  - Quando o valor/hora for menor ou igual a zero, o sistema deve rejeitar com erro 400.
  - Quando válido, o sistema deve retornar a quadra criada com `id` gerado.

**UC2 — Criar reserva**
- Entrada: quadraId, clientId, start (ISO 8601), end (ISO 8601).
- Critérios de aceite:
  - A duração (end − start) deve ser de **no mínimo 1h e no máximo 3h**; fora disso, erro 400.
  - Reservas com `start` no passado devem ser rejeitadas (erro 400).
  - Se a quadra já tiver reserva que **se sobrepõe** ao intervalo, erro 409.
  - Preço calculado como `valor/hora × duração em horas`, arredondando frações **para cima** (ex.: 1h30 → 2 × valor/hora).

**UC3 — Cancelar reserva**
- A reserva cancelada não deve mais aparecer nas listagens (erro 404 se consultada).

**UC4 — Listar reservas**
- Por quadra: `GET /bookings?courtId={id}`.
- Por dia: `GET /bookings?date=YYYY-MM-DD` (retorna reservas ativas que intersectam o dia).
