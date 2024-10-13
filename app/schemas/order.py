# app/schemas/order.py

from pydantic import BaseModel

class OrderBase(BaseModel):
    item_name: str
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
