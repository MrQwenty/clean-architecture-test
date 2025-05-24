
from uuid import UUID
from ..domain.repository import ItemRepository
from ..domain.entity import Item


def get_item_by_id(item_id: UUID, repo: ItemRepository) -> Item:
    item = repo.get_by_id(item_id)
    if item is None:
        raise ValueError("Item not found")
    return item
