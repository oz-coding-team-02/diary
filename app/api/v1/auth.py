from fastapi import APIRouter, status, Depends

from app.api.deps import get_current_user
from app.schemas.user import TokenResponse, UserBase, UserRead
from app.services.user_service import UserService
from app.models.user import User

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def signup(data: UserBase):
    return await UserService.signup_user(data)

@router.post('/login', response_model=TokenResponse)
async def login(data: UserBase):
    return await UserService.login_user(data)


@router.get('/me', response_model=UserRead)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user