from fastapi import FastAPI
from app.api.routes import items  # Adjusted import
from app.persistence.database import engine  # Corrected import path
from app.persistence.base import Base  # Import Base from base.py

app = FastAPI()

# Include routes
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Application"}

# Create all database tables
Base.metadata.create_all(bind=engine)




