# Persistência em memória: dicts indexados por id.
# Nenhum banco de dados é usado (regra 3 da constitution).

courts: dict[int, dict] = {}
clients: dict[int, dict] = {}
bookings: dict[int, dict] = {}

_next_ids = {"courts": 1, "clients": 1, "bookings": 1}


def next_id(resource: str) -> int:
    value = _next_ids[resource]
    _next_ids[resource] += 1
    return value


def reset() -> None:
    courts.clear()
    clients.clear()
    bookings.clear()
    for key in _next_ids:
        _next_ids[key] = 1
