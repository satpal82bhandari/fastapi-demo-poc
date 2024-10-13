from app.persistence.memory import add_item_to_memory, get_item_from_memory, get_all_items_from_memory
from app.schemas.item import ItemCreate, ItemResponse

async def add_item_memory_service(item: ItemCreate) -> ItemResponse:
    memory_item = add_item_to_memory(item)
    return ItemResponse(id=memory_item["id"], **item.dict())

async def get_item_memory_service(item_id: int) -> ItemResponse:
    memory_item = get_item_from_memory(item_id)
    if not memory_item:
        return None
    return ItemResponse(id=memory_item["id"], **memory_item)

async def get_all_items_memory_service():
    items = get_all_items_from_memory()
    return items
