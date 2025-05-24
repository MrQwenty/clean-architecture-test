
from ..domain.repository import ItemRepository
from ..domain.entity import Item
from typing import List


def list_all_items(repo: ItemRepository) -> List[Item]:
    return repo.list_all()
