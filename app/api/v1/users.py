from fastapi import APIRouter, Depends
from app.schemas.user import UserMeRead, UserRead
from app.models.user import User
from app.services.user_service import (
    get_current_user,
    get_current_admin_user,
    get_user_service,
    UserService,
)
from typing import List

router = APIRouter()


@router.get(
    "",
    response_model=List[UserRead],
    summary="전체 사용자 목록 조회 (관리자 전용)",
    dependencies=[Depends(get_current_admin_user)],
)
async def get_all_users(service: UserService = Depends(get_user_service)):
    """
    시스템에 등록된 모든 사용자 목록을 조회합니다. (관리자만 사용 가능)
    """
    return await service.get_all_users()


@router.get("/me", response_model=UserMeRead)
async def get_me(current_user: User = Depends(get_current_user)):
    await current_user.fetch_related("bookmarks__quote", "diaries")

    return current_user
