from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

def create_order(db: Session, order: OrderCreate, user_id: int):
    db_order = Order(**order.dict(), user_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(Order).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order(db: Session, order_id: int, order_data: OrderUpdate, user_id: int):
    db_order = db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
    if db_order:
        for key, value in order_data.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int, user_id: int):
    db_order = db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
