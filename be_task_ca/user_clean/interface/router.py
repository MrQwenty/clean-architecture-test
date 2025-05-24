
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from ..usecases.create_user import create_user
from ..usecases.add_item_to_cart import add_item_to_cart
from ..usecases.list_cart_items import list_cart_items
from ..infrastructure.memory_repository import InMemoryUserRepository, InMemoryCartRepository

repo_user = InMemoryUserRepository()
repo_cart = InMemoryCartRepository()

router = APIRouter()

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    shipping_address: Optional[str] = None

class AddToCartRequest(BaseModel):
    user_id: UUID
    item_id: UUID
    quantity: int

class CartItemResponse(BaseModel):
    id: UUID
    user_id: UUID
    item_id: UUID
    quantity: int

@router.post("/users")
def create_user_route(req: CreateUserRequest):
    try:
        user = create_user(req.dict(), repo_user)
        return {"id": str(user.id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/cart")
def add_to_cart_route(req: AddToCartRequest):
    add_item_to_cart(req.dict(), repo_cart)
    return {"status": "ok"}

@router.get("/cart/{user_id}", response_model=List[CartItemResponse])
def list_cart_items_route(user_id: UUID):
    return list_cart_items(user_id, repo_cart)
