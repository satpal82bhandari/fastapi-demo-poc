import os
from app.services.item_db_service import add_item_db_service, get_item_db_service
from app.services.item_memory_service import add_item_memory_service, get_item_memory_service, get_all_items_memory_service
from app.schemas.item import ItemCreate, ItemResponse
from dotenv import load_dotenv

load_dotenv()

STORAGE_TYPE = os.getenv("STORAGE_TYPE", "memory")
async def add_item(item: ItemCreate) -> ItemResponse:
    if STORAGE_TYPE == "database":
        return await add_item_db_service(item)
    else:
        return await add_item_memory_service(item)

async def get_item_by_id(item_id: int) -> ItemResponse:
    if STORAGE_TYPE == "database":
        return await get_item_db_service(item_id)
    else:
        return await get_item_memory_service(item_id)

# New controller function to get all in-memory items
async def get_all_items():
    if STORAGE_TYPE == "memory":
        return await get_all_items_memory_service()
    else:
        return {"error": "This feature is only available in memory mode"}
