from app.schemas.item import ItemCreate, ItemResponse
from app.persistence.database import add_item_to_db, get_item_from_db
from fastapi import HTTPException

async def add_item_db_service(item: ItemCreate) -> ItemResponse:
    db_item = add_item_to_db(item)  # No await here
    return ItemResponse.from_orm(db_item)

async def get_item_db_service(item_id: int) -> ItemResponse:
    db_item = get_item_from_db(item_id)  # No await here
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse.from_orm(db_item)
