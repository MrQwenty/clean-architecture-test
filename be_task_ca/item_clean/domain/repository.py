
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from .entity import Item


class ItemRepository(ABC):
    @abstractmethod
    def get_by_id(self, item_id: UUID) -> Optional[Item]: ...

    @abstractmethod
    def list_all(self) -> List[Item]: ...
