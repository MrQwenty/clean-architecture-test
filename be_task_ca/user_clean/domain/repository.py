
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from .entity import User, CartItem


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]: ...
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]: ...
    @abstractmethod
    def save(self, user: User) -> User: ...


class CartRepository(ABC):
    @abstractmethod
    def get_cart_items(self, user_id: UUID) -> List[CartItem]: ...
    @abstractmethod
    def add_to_cart(self, item: CartItem) -> None: ...
