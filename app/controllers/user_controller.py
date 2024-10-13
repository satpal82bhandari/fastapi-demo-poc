from fastapi import APIRouter, Depends
from app.schemas.user import User, UserCreate
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await user_service.create_user(user)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    return await user_service.get_user(user_id)
