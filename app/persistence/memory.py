from app.schemas.item import ItemCreate, ItemResponse  # Import both schemas

# Simple in-memory storage for items
in_memory_items = []

def add_item_to_memory(item_data: ItemCreate):
    item_id = len(in_memory_items) + 1  # Generate a unique ID
    # Create a new ItemResponse object with the id and other fields
    item = ItemResponse(id=item_id, **item_data.dict())  # Pass item_data as a dictionary
    in_memory_items.append(item)  # Store the item in memory
    return item

def get_item_from_memory(item_id):
    for item in in_memory_items:
        if item.id == item_id:
            return item
    return None

def get_all_items_from_memory():
    return in_memory_items
