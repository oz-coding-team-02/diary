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
            await self.repo.save_user_question_history(
                user_id=user_id, question_id=question.id
            )
            return QuestionRead(content=question.content)

        question = await self.repo.get_random_question()

        if question:
            return QuestionRead(content=question.content)

        return None


def get_question_repo() -> QuestionRepository:
    return QuestionRepository()


def get_question_service(
    repo: QuestionRepository = Depends(get_question_repo),
) -> QuestionService:
    return QuestionService(repo=repo)
