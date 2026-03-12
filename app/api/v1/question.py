from fastapi import APIRouter, status, Depends

from app.schemas.question import QuestionRead
from app.services.question_service import QuestionService

router = APIRouter()


def get_question_service() -> QuestionService:
    return QuestionService()


@router.get("", status_code=status.HTTP_200_OK, response_model=QuestionRead)
async def get_question(service: QuestionService= Depends(get_question_service)):
    return service.get_random_question_or_none()
