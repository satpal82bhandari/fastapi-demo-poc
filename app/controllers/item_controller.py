import os
from dotenv import load_dotenv

load_dotenv()

# Check storage type from the environment variable
STORAGE_TYPE = os.getenv("STORAGE_TYPE", "memory")

# Dynamically import the appropriate service based on STORAGE_TYPE
if STORAGE_TYPE == "database":
    from app.services.item_db_service import (
        add_item_db_service as add_item,
        get_item_db_service as get_item_by_id,  # Ensure this is defined in item_db_service.py
        get_all_items_db_service as get_all_items
    )
else:
    from app.services.item_memory_service import (
        add_item_memory_service as add_item,
        get_item_memory_service as get_item_by_id,  # Ensure this is defined in item_memory_service.py
        get_all_items_memory_service as get_all_items
    )
