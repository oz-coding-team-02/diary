from fastapi import APIRouter, status
from app.schemas.user import TokenResponse, UserBase, UserRead
from app.services.user_service import UserService

router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def signup(data: UserBase):
    return await UserService.signup_user(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserBase):
    return await UserService.login_user(data)
