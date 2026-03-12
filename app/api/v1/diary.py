from fastapi import APIRouter, Depends
from app.services.user_service import get_current_user
from app.models.user import User
from app.repositories.diary_repo import DiaryRepo
from typing import List
from app.schemas.diary import DiaryBase, DiaryDelete, DiaryPlusID

router = APIRouter()

@router.get("/me", response_model=List[DiaryPlusID])
async def get_me(
    user: User = Depends(get_current_user),
    # service: DiaryService = Depends(get_diary_service) # 서비스 주입
):
    # DiaryService.get_all_diaries(user) 대신 service 인스턴스 사용
    return await DiaryRepo.get_list_diaries(user)

@router.get("/{diary_id}", response_model=DiaryPlusID)
async def get_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    # service: DiaryService = Depends(get_diary_service)
):
    return await DiaryRepo.get_diary(diary_id, user)

@router.post("/register", response_model=DiaryPlusID)
async def create_diary(
    data: DiaryBase,
    user: User = Depends(get_current_user),
    # service: DiaryService = Depends(get_diary_service)
):
    return await  DiaryRepo.make_new_diary(data, user)

@router.put("/{diary_id}", response_model=DiaryPlusID)
async def mod_diary(
    diary_id: int,
    mod_data: DiaryBase,
    user: User = Depends(get_current_user),
    # service: DiaryService = Depends(get_diary_service)
):
    return await DiaryRepo.modding_diary(diary_id, mod_data, user)

@router.delete("/{diary_id}", response_model=DiaryDelete)
async def delete_diary(
    diary_id: int,
    user: User = Depends(get_current_user),
    # service: DiaryService = Depends(get_diary_service)
):
    return await DiaryRepo.del_r_diary(diary_id, user)
