from typing import Optional
from fastapi import Depends

from app.repositories.question_repo import QuestionRepository
from app.schemas.question import QuestionRead


class QuestionService:
    def __init__(self, repo: QuestionRepository):
        self.repo = repo

    async def get_random_question_for_user(
        self, user_id: int
    ) -> Optional[QuestionRead]:
        seen_question_ids = await self.repo.get_seen_question_ids_for_user(user_id)
        question = await self.repo.get_random_question_excluding_ids(
            excluded_ids=seen_question_ids
        )
        if question:
            return question
        return await self.repo.get_random_question()


def get_question_repo() -> QuestionRepository:
    return QuestionRepository()


def get_question_service(
    repo: QuestionRepository = Depends(get_question_repo),
) -> QuestionService:
    return QuestionService(repo=repo)
