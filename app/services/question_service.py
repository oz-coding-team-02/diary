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
        """
        사용자에게 아직 보여주지 않은 랜덤 질문을 반환합니다.
        만약 모든 질문을 다 봤다면, 기존 질문 중에서 랜덤으로 하나를 반환합니다.
        """
        # 1. 사용자가 이미 본 질문 ID 목록을 가져옵니다.
        seen_question_ids = await self.repo.get_seen_question_ids_for_user(user_id)

        # 2. 아직 보지 않은 질문 중에서 랜덤으로 하나를 가져옵니다.
        question = await self.repo.get_random_question_excluding_ids(
            excluded_ids=seen_question_ids
        )

        # 3. 만약 새로운 질문이 있다면,
        if question:
            # 3-1. 이 질문을 봤다고 기록을 남깁니다.
            await self.repo.save_user_question_history(
                user_id=user_id, question_id=question.id
            )
            # 3-2. 스키마로 변환하여 반환합니다.
            return QuestionRead(id=question.id, content=question.content)

        # 4. 만약 새로운 질문이 없다면 (모든 질문을 다 봤다면),
        #    기존 질문 중에서 랜덤으로 하나를 가져옵니다. (이때는 기록을 남기지 않습니다.)
        question = await self.repo.get_random_question()
        if question:
            return QuestionRead(id=question.id, content=question.content)

        # 5. 데이터베이스에 질문이 아예 하나도 없다면 None을 반환합니다.
        return None


def get_question_repo() -> QuestionRepository:
    return QuestionRepository()


def get_question_service(
    repo: QuestionRepository = Depends(get_question_repo),
) -> QuestionService:
    return QuestionService(repo=repo)
