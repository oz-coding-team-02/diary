from fastapi import APIRouter, Depends
from app.schemas.user import UserMeRead
from app.models.user import User
from app.services.user_service import get_current_user

router = APIRouter()


@router.get("/me", response_model=UserMeRead)
async def get_me(current_user: User = Depends(get_current_user)):
    await current_user.fetch_related('bookmarks__quote')
    return current_user
