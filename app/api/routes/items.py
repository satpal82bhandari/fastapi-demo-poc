from fastapi import APIRouter
from app.schemas.item import ItemCreate, ItemResponse
from app.controllers.item_controller import add_item, get_item_by_id, get_all_items

router = APIRouter()

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    return await add_item(item)

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    return await get_item_by_id(item_id)

# Route to fetch all in-memory items
@router.get("/memory/")
async def get_all_items_in_memory():
    return await get_all_items()
