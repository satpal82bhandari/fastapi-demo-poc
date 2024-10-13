from fastapi import APIRouter, Depends
from app.schemas.order import Order, OrderCreate
from app.services.order_service import OrderService

router = APIRouter()
order_service = OrderService()

@router.post("/", response_model=Order)
async def create_order(order: OrderCreate):
    return await order_service.create_order(order)

@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int):
    return await order_service.get_order(order_id)
