from app.models.question import Question
from typing import Optional
from tortoise.contrib.postgres.functions import Random


class QuestionRepository:
    @staticmethod
    async def get_random_question_one() -> Optional[Question]:
        return await Question.annotate(idx=Random()).order_by("idx").first()