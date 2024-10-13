# app/api/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import UserLogin, UserRegister, Token
from app.services.auth_service import authenticate_user, create_access_token, register_user
from datetime import timedelta

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/login", response_model=Token)
async def login(user_credentials: UserLogin):
    user = authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=Token)
async def register(user_data: UserRegister):
    user = register_user(user_data)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# from fastapi import APIRouter, Depends

# router = APIRouter()

# @router.post("/login/")
# async def login_user(credentials: LoginData):
#     # Authenticate user logic
#     return {"token": "jwt-token-string"}
