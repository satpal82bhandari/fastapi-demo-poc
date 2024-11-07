from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.item import ItemCreate, ItemResponse
from app.controllers.item_controller import add_item, get_item_by_id, get_all_items, export_items_to_excel

router = APIRouter()

@router.post("/", response_model=ItemResponse)
async def create_item(item_data: ItemCreate):
    return await add_item(item_data)

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    return await get_item_by_id(item_id)

@router.get("/memory/")
async def get_all_items_in_memory():
    return await get_all_items()

# New route to download items as Excel
@router.get("/download/")
async def download_items_excel():
    # Await the export_items_to_excel function
    return await export_items_to_excel()
