
from uuid import UUID
from ..domain.repository import CartRepository
from ..domain.entity import CartItem
from typing import List


def list_cart_items(user_id: UUID, repo: CartRepository) -> List[CartItem]:
    return repo.get_cart_items(user_id)
