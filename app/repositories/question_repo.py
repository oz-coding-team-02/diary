from typing import Optional

from app.models.question import Question
from tortoise.contrib.postgres.functions import Random

from app.schemas.question import QuestionRead  # QuestionRead 스키마를 임포트합니다.
from app.models.user_question import UserQuestion


class QuestionRepository:
    async def get_seen_question_ids_for_user(self, user_id: int) -> list[int]:
        seen_question_ids = await UserQuestion.filter(user_id=user_id).values_list(
            "question_id", flat=True
        )
        return list(seen_question_ids)

    async def get_random_question_excluding_ids(
        self, excluded_ids: list[int]
    ) -> Optional[QuestionRead]:

        question = (
            await Question.filter(id__not_in=excluded_ids)
            .annotate(idx=Random())
            .order_by("idx")
            .first()
        )
        return question

    async def get_random_question(self) -> Optional[QuestionRead]:

        question = await Question.annotate(idx=Random()).order_by("idx").first()
        if question:
            return QuestionRead(content=question.content)
        return None

    async def save_user_question_history(self, user_id: int, question_id: int) -> None:
        await UserQuestion.create(user_id=user_id, question_id=question_id)
