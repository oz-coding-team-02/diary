from fastapi import HTTPException, status

from app.repositories.question_repo import QuestionRepository
from app.schemas.question import QuestionRead


class QuestionService:
    @staticmethod
    async def get_random_question_or_none() -> QuestionRead:
        question = await QuestionRepository.get_random_question_one()

        if question is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")

        return QuestionRead(content=question.content)
