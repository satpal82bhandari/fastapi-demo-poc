from app.persistence.database import add_item_to_db, get_item_from_db, get_all_items_from_db

async def add_item_db_service(item_data):
    return add_item_to_db(item_data)

async def get_item_db_service(item_id):
    return get_item_from_db(item_id)

async def get_all_items_db_service():
    return get_all_items_from_db()

