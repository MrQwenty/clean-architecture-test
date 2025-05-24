
from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from pydantic import BaseModel
from ..usecases.get_item_by_id import get_item_by_id
from ..usecases.list_all_items import list_all_items
from ..infrastructure.memory_repository import InMemoryItemRepository

repo = InMemoryItemRepository()
router = APIRouter()

class ItemResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity_available: int

@router.get("/items", response_model=List[ItemResponse])
def list_items():
    return list_all_items(repo)

@router.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: UUID):
    try:
        return get_item_by_id(item_id, repo)
    except ValueError:
        raise HTTPException(status_code=404, detail="Item not found")
