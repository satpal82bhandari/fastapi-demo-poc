from app.db.database import SessionLocal
from app.models.item import ItemModel
from app.schemas.item import ItemCreate, ItemResponse

async def add_item_service(item: ItemCreate) -> ItemResponse:
    db = SessionLocal()  # Creating a database session

    db_item = ItemModel(**item.dict())  # Create a new Item instance
    db.add(db_item)
    db.commit()  # Persist changes
    db.refresh(db_item)  # Refresh the instance with the DB values

    return ItemResponse.from_orm(db_item)


async def get_item_service(item_id: int):
    async with SessionLocal() as session:
        item = await session.get(ItemModel, item_id)  # Make sure ItemModel is defined and correct
        print(f"Fetching item with ID: {item_id}, Found: {item}")  # Debug line
        print(item)  # This should print the item if found
        return item
