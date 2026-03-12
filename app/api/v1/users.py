from fastapi import APIRouter, Depends
from app.schemas.user import UserRead
from app.models.user import User
from app.services.user_service import get_current_user

router = APIRouter()


@router.get('/me', response_model=UserRead)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user