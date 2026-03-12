from fastapi import APIRouter, status, Depends
from app.schemas.user import TokenResponse, UserBase, UserRead
from app.services.user_service import UserService, get_user_service

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def signup(data: UserBase, service: UserService = Depends(get_user_service)):
    return await service.signup_user(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserBase, service: UserService = Depends(get_user_service)):
    return await service.login_user(data)
