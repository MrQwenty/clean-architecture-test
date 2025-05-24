
from uuid import uuid4
from ..domain.entity import CartItem
from ..domain.repository import CartRepository


def add_item_to_cart(data: dict, repo: CartRepository) -> None:
    item = CartItem(
        id=uuid4(),
        user_id=data["user_id"],
        item_id=data["item_id"],
        quantity=data["quantity"]
    )
    repo.add_to_cart(item)
