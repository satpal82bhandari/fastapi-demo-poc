from fastapi import FastAPI
from app.api.routes import items

app = FastAPI()

# Include routes
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Application"}
