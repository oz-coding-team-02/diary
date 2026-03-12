from fastapi import HTTPException, status
from typing import Optional # Optional 타입을 사용하기 위해 추가

from app.repositories.question_repo import QuestionRepository
from app.schemas.question import QuestionRead


class QuestionService:
    def __init__(self, repo: QuestionRepository):
        self.repo = repo

    async def get_random_question_for_user(self, user_id: int) -> Optional[QuestionRead]:

        seen_question_ids = await self.repo.get_seen_question_ids_for_user(user_id)
        question = await self.repo.get_random_question_excluding_ids(excluded_ids=seen_question_ids)
        if question:
            return question
        return await self.repo.get_random_question()
