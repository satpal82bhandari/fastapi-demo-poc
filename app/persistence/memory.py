import threading

items_in_memory = []  # Simple list to store items
id_counter = 1  # Global counter for item IDs
lock = threading.Lock()

def add_item_to_memory(item):
    global id_counter
    item_dict = item.dict()
    with lock:
        item_dict["id"] = id_counter
        id_counter += 1
        items_in_memory.append(item_dict)
    return item_dict

def get_item_from_memory(item_id):
    with lock:
        for item in items_in_memory:
            if item["id"] == item_id:
                return item
    return None

def get_all_items_from_memory():
    with lock:
        return items_in_memory

