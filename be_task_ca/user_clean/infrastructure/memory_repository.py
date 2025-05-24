
from typing import Optional, List
from uuid import UUID
from ..domain.repository import UserRepository, CartRepository
from ..domain.entity import User, CartItem


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def get_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self.users.values() if u.email == email), None)

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        return self.users.get(user_id)

    def save(self, user: User) -> User:
        self.users[user.id] = user
        return user


class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self.items = []

    def get_cart_items(self, user_id: UUID) -> List[CartItem]:
        return [i for i in self.items if i.user_id == user_id]

    def add_to_cart(self, item: CartItem) -> None:
        self.items.append(item)
