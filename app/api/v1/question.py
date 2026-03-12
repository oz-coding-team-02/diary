from typing import Optional

from fastapi import APIRouter, status, Depends, Response
from app.schemas.question import QuestionRead
from app.repositories.question_repo import QuestionRepository
from app.services.question_service import QuestionService

router = APIRouter()


def get_question_service() -> QuestionService:
    repo = QuestionRepository()
    return QuestionService(repo=repo)


@router.get("", status_code=status.HTTP_200_OK, response_model=Optional[QuestionRead])
async def get_question(user_id: int, service: QuestionService= Depends(get_question_service)):
    question = await service.get_random_question_for_user(user_id=user_id)
    if question is None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return question
