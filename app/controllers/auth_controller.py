from fastapi import APIRouter, Depends
from app.schemas.auth import AuthRequest, AuthResponse
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()

@router.post("/login", response_model=AuthResponse)
async def login(auth_request: AuthRequest):
    return await auth_service.login(auth_request)

@router.post("/signup", response_model=AuthResponse)
async def signup(auth_request: AuthRequest):
    return await auth_service.signup(auth_request)
