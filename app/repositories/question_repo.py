from typing import Optional, List

from app.models.question import Question
from app.models.user_question import UserQuestion
from tortoise.contrib.postgres.functions import Random


class QuestionRepository:
    async def get_seen_question_ids_for_user(self, user_id: int) -> List[int]:
        """특정 사용자가 이미 본 모든 질문의 ID 목록을 반환합니다."""
        seen_questions = await UserQuestion.filter(user_id=user_id).values_list(
            "question_id", flat=True
        )
        return list(seen_questions)

    async def get_random_question_excluding_ids(
        self, excluded_ids: List[int]
    ) -> Optional[Question]:
        """주어진 ID 목록을 제외하고 랜덤한 질문 하나를 반환합니다."""
        question = (
            await Question.filter(id__not_in=excluded_ids)
            .annotate(order=Random())
            .order_by("order")
            .first()
        )
        return question

    async def get_random_question(self) -> Optional[Question]:
        """모든 질문 중에서 랜덤한 질문 하나를 반환합니다."""
        question = await Question.annotate(order=Random()).order_by("order").first()
        return question

    async def save_user_question_history(
        self, user_id: int, question_id: int
    ) -> None:
        """사용자가 질문을 봤다는 기록을 데이터베이스에 저장합니다."""
        await UserQuestion.get_or_create(user_id=user_id, question_id=question_id)
