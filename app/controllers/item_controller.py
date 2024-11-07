import os
from dotenv import load_dotenv
from app.services import item_db_service, item_memory_service
from app.services.item_memory_service import export_items_memory_service

load_dotenv()

STORAGE_TYPE = os.getenv("STORAGE_TYPE", "memory")

if STORAGE_TYPE == "database":
    from app.services.item_db_service import (
        add_item_db_service as add_item,
        get_item_db_service as get_item_by_id,
        get_all_items_db_service as get_all_items,
    )
else:
    from app.services.item_memory_service import (
        add_item_memory_service as add_item,
        get_item_memory_service as get_item_by_id,
        get_all_items_memory_service as get_all_items,
    )

# Controller to export items as an Excel file
async def export_items_to_excel():
    # Await the coroutine from the service layer
    return await export_items_memory_service()
