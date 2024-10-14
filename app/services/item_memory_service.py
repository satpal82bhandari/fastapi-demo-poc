from app.persistence.memory import add_item_to_memory, get_item_from_memory, get_all_items_from_memory

async def add_item_memory_service(item_data):
    return add_item_to_memory(item_data)

async def get_item_memory_service(item_id):
    return get_item_from_memory(item_id)

async def get_all_items_memory_service():
    return get_all_items_from_memory()
