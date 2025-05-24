
from uuid import uuid4
import hashlib
from ..domain.entity import User
from ..domain.repository import UserRepository


def create_user(data: dict, repo: UserRepository) -> User:
    if repo.get_by_email(data["email"]):
        raise ValueError("Email already exists")

    hashed = hashlib.sha256(data["password"].encode()).hexdigest()
    user = User(
        id=uuid4(),
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        hashed_password=hashed,
        shipping_address=data.get("shipping_address")
    )
    return repo.save(user)
