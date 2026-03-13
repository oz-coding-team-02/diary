from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user_service import get_current_user
from app.models.user import User
from app.repositories.diary_repo import DiaryRepo
from typing import List
from app.schemas.diary import DiaryBase, DiaryDelete, DiaryPlusID
from app.services.diary_service import DiaryService, get_diary_service


router = APIRouter()

@router.get("/me", response_model=List[DiaryPlusID])
async def get_me(
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service)
):
    return await service.get_all_diaries(user)

@router.get("/{diary_id}", response_model=DiaryPlusID)
async def get_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service)
):
    result = await service.get_diary(diary_id, user)
    if not result:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다.")

@router.post("/register", response_model=DiaryPlusID, status_code=status.HTTP_201_CREATED)
async def create_diary(
    data: DiaryBase,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service)
):
    return await service.make_diary(data, user)

@router.put("/{diary_id}", response_model=DiaryPlusID)
async def mod_diary(
    diary_id: int,
    mod_data: DiaryBase,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service)
):
    return await service.modify_diary(diary_id, mod_data, user)

@router.delete("/{diary_id}", response_model=DiaryDelete)
async def delete_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    service: DiaryService = Depends(get_diary_service)
):
    return await service.del_diary(diary_id, user)
