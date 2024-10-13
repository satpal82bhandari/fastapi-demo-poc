# app/api/routes/users.py

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserResponse, UserUpdate
from app.services.user_service import get_user_by_id, update_user
from app.api.dependencies.auth import get_current_active_user
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def read_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.put("/me", response_model=UserResponse)
async def update_user_me(user_data: UserUpdate, current_user: User = Depends(get_current_active_user)):
    return update_user(current_user.id, user_data)

