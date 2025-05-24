
from dataclasses import dataclass
from uuid import UUID
from typing import Optional


@dataclass
class User:
    id: UUID
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    shipping_address: Optional[str] = None


@dataclass
class CartItem:
    id: UUID
    user_id: UUID
    item_id: UUID
    quantity: int
