from fastapi import APIRouter, status
from fastapi.params import Depends
from app.models.user import User
from app.services.user_service import get_current_user

from app.schemas.quote import (
    QuoteRead,
    BookmarkCreate,
    BookmarkToggleResponse,
)
from app.schemas.user import BookmarkRead
from app.repositories.quote_repo import QuoteRepository
from app.services.quote_service import QuoteService, get_quote_service

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK, response_model=QuoteRead, summary="랜덤 명언 조회")
async def get_quote(
    current_user: User = Depends(get_current_user),
    service: QuoteService = Depends(get_quote_service),
):
    return await service.get_random_quote_or_none(user_id=current_user.id)


@router.post(
    "/bookmark",
    status_code=status.HTTP_200_OK,
    response_model=BookmarkToggleResponse,
    summary="명언 북마크 등록/해제",
)
async def toggle_bookmark(
    data: BookmarkCreate,
    current_user: User = Depends(get_current_user),
    service: QuoteService = Depends(get_quote_service),
):
    data.user_id = current_user.id
    is_bookmarked = await service.toggle_bookmark(data)
    message = "북마크 추가" if is_bookmarked else "북마크 삭제"
    return {"is_bookmarked": is_bookmarked, "message": message}


@router.get(
    "/bookmarked", response_model=list[BookmarkRead], summary="북마크한 명언 목록 조회"
)
async def get_bookmarked_quotes(
    current_user: User = Depends(get_current_user),
    service: QuoteService = Depends(get_quote_service),
):
    return await service.get_bookmarked_quotes_for_user(user_id=current_user.id)
