import threading
from typing import Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    def __init__(self) -> None:
        self._items: Dict[int, T] = {}
        self._next_id: int = 1
        self._lock = threading.Lock()

    def add(self, item: T, id_attr: str = "id") -> T:
        with self._lock:
            setattr(item, id_attr, self._next_id)
            self._items[self._next_id] = item
            self._next_id += 1
            return item

    def get(self, item_id: int) -> Optional[T]:
        with self._lock:
            return self._items.get(item_id)

    def list(self) -> List[T]:
        with self._lock:
            return list(self._items.values())

    def filter_by(self, attr: str, value) -> List[T]:
        with self._lock:
            return [item for item in self._items.values() if getattr(item, attr) == value]
