# from pydantic import BaseModel

# # Schema for creating an item
# class ItemCreate(BaseModel):
#     name: str
#     description: str | None = None  # Optional field

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "name": "Sample Item",
#                 "description": "This is a sample item."
#             }
#         }

# # Schema for returning item data
# class ItemResponse(BaseModel):
#     id: int
#     name: str
#     description: str | None = None  # Optional field

#     class Config:
#         from_attributes = True  # This allows Pydantic to work with SQLAlchemy models


from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str | None = None  # Optional field

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True  # Required for Pydantic V2
