from typing import Optional

from fastapi import APIRouter, status, Depends
from app.schemas.question import QuestionRead
from app.repositories.question_repo import QuestionRepository
from app.services.question_service import QuestionService, get_question_service
from app.services.user_service import get_current_user
from app.models.user import User


router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=Optional[QuestionRead],
    summary="랜덤 질문 조회",
)
async def get_question(
    current_user: User = Depends(get_current_user),
    service: QuestionService = Depends(get_question_service),
):
    return await service.get_random_question_for_user(user_id=current_user.id)
