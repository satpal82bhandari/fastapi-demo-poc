from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.persistence.base import Base  # Import Base from base.py
from app.models.item import Item  # No circular dependency now
from dotenv import load_dotenv
import os

load_dotenv()

STORAGE_TYPE = os.getenv("STORAGE_TYPE", "memory")  # Default to "memory" if not set

if STORAGE_TYPE == "database":
    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set")

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_item_to_db(item_data):
    db = SessionLocal()
    try:
        db_item = Item(**item_data.dict())  # Assuming item_data is a Pydantic model
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    finally:
        db.close()

def get_item_from_db(item_id):
    db = SessionLocal()
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        return db_item
    finally:
        db.close()

def get_all_items_from_db():
    db = SessionLocal()
    try:
        db_items = db.query(Item).all()
        return db_items
    finally:
        db.close()
