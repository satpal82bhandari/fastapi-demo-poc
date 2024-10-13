# app/api/routes/orders.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order, get_orders
from app.api.dependencies.auth import get_current_active_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=OrderResponse)
async def create_order_controller(order_data: OrderCreate, current_user: User = Depends(get_current_active_user)):
    return create_order(order_data, current_user.id)

@router.get("/", response_model=List[OrderResponse])
async def get_orders_controller(current_user: User = Depends(get_current_active_user)):
    return get_orders(current_user.id)


# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/orders/")
# async def get_orders():
#     # Fetch orders logic
#     return [{"order_id": 1, "status": "shipped"}]
