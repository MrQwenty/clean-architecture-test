
from ..domain.repository import ItemRepository
from ..domain.entity import Item
from typing import Optional, List
from uuid import UUID, uuid4


class InMemoryItemRepository(ItemRepository):
    def __init__(self):
        self.items = [
            Item(id=uuid4(), name="Laptop", description="High performance laptop", price=999.99, quantity_available=5),
            Item(id=uuid4(), name="Mouse", description="Wireless mouse", price=29.99, quantity_available=25),
        ]

    def get_by_id(self, item_id: UUID) -> Optional[Item]:
        return next((i for i in self.items if i.id == item_id), None)

    def list_all(self) -> List[Item]:
        return self.items
