
import pytest
from uuid import UUID
from be_task_ca.user_clean.usecases.create_user import create_user
from be_task_ca.user_clean.usecases.add_item_to_cart import add_item_to_cart
from be_task_ca.user_clean.usecases.list_cart_items import list_cart_items
from be_task_ca.user_clean.infrastructure.memory_repository import InMemoryUserRepository, InMemoryCartRepository


def test_create_user():
    repo = InMemoryUserRepository()
    data = {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice@example.com",
        "password": "secret",
        "shipping_address": "123 Street"
    }
    user = create_user(data, repo)
    assert user.email == "alice@example.com"
    assert repo.get_by_id(user.id) is not None


def test_add_and_list_cart():
    user_repo = InMemoryUserRepository()
    cart_repo = InMemoryCartRepository()

    user = create_user({
        "first_name": "Bob",
        "last_name": "Jones",
        "email": "bob@example.com",
        "password": "secure",
        "shipping_address": None
    }, user_repo)

    item_data = {
        "user_id": user.id,
        "item_id": UUID("00000000-0000-0000-0000-000000000001"),
        "quantity": 2
    }

    add_item_to_cart(item_data, cart_repo)
    items = list_cart_items(user.id, cart_repo)

    assert len(items) == 1
    assert items[0].user_id == user.id
    assert items[0].quantity == 2
