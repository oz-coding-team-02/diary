from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user_service import get_current_user
from app.models.user import User
from typing import List
from app.schemas.diary import DiaryBase, DiaryDelete, DiaryPlusID, WritingPromptResponse
from app.services.diary_service import DiaryService, get_diary_service
from app.services.quote_service import QuoteService, get_quote_service
from app.services.question_service import QuestionService, get_question_service

router = APIRouter()


@router.get(
    "/writing-prompt",
    response_model=WritingPromptResponse,
    summary="오늘의 글감(명언, 질문) 가져오기",
)
async def get_writing_prompt(
    user: User = Depends(get_current_user),
    quote_service: QuoteService = Depends(get_quote_service),
    question_service: QuestionService = Depends(get_question_service),
):
    """
    다이어리 작성 시 사용할 오늘의 명언과 질문을 랜덤으로 가져옵니다.
    """
    quote = await quote_service.get_random_quote_or_none(user.id)
    question = await question_service.get_random_question_for_user(user.id)

    quote_id = quote.id if quote else None
    quote_content = f"{quote.content} - {quote.author}" if quote else "오늘의 명언을 찾지 못했습니다."
    question_content = question.content if question else "오늘의 질문을 찾지 못했습니다."

    return WritingPromptResponse(
        quote_id=quote_id, quote=quote_content, question=question_content
    )


@router.get("/my-diaries", response_model=List[DiaryPlusID])
async def get_my_diaries(
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service),
):
    return await service.get_all_diaries(user)


@router.get("/{diary_id}", response_model=DiaryPlusID)
async def get_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service),
):
    result = await service.get_diary(diary_id, user)
    if not result:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다.")

    return result


@router.post(
    "/register", response_model=DiaryPlusID, status_code=status.HTTP_201_CREATED
)
async def create_diary(
    data: DiaryBase,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service),
):
    return await service.make_diary(data, user)


@router.put("/{diary_id}", response_model=DiaryPlusID)
async def mod_diary(
    diary_id: int,
    mod_data: DiaryBase,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service),
):
    return await service.modify_diary(diary_id, mod_data, user)


@router.delete("/{diary_id}", response_model=DiaryDelete)
async def delete_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service),
):
    return await service.del_diary(diary_id, user)
