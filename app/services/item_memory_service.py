from io import BytesIO
import pandas as pd
from app.persistence.memory import get_all_items_from_memory, add_item_to_memory
from fastapi.responses import StreamingResponse
from fastapi import HTTPException

async def add_item_memory_service(item_data):
    return add_item_to_memory(item_data)

async def get_item_memory_service(item_id):
    return get_item_from_memory(item_id)

async def get_all_items_memory_service():
    return get_all_items_from_memory()

# Service function to export items as an Excel file
async def export_items_memory_service():
    items = get_all_items_from_memory()
    if not items:
        raise HTTPException(status_code=404, detail="No items available to download.")

    # Convert items to DataFrame
    df = pd.DataFrame([item.dict() for item in items])

    # Convert DataFrame to Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Items")
        # writer.save()
    output.seek(0)

    # Return the Excel file as a streaming response
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=items.xlsx"}
    )
