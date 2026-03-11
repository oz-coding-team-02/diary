from fastapi import APIRouter, Depends
from app.schemas.diary import DiaryCreateRequest, DiaryCreateResponse, DiaryBaseResponse

from app.core.security import get_current_user
from app.schemas.user import UserRead
from app.schemas.diary import DiaryGetResponse,DiaryBase
from app.repositories.diary_repo import DiaryRepo

diary_router = APIRouter()

@diary_router.post('/register',response_model=DiaryCreateResponse)
async def create_diaries(diary_data:DiaryCreateRequest,user_data:UserRead=Depends(get_current_user),):
    new_diary =  await DiaryRepo.create_diary(user_data,diary_data)
    return new_diary

@diary_router.get('/me',response_model=DiaryGetResponse)
async def get_all_diary(user_data:UserRead=Depends(get_current_user)):
    diaries_list = await DiaryRepo.get_diaries(user_data)
    return {
        "diaries":diaries_list,
        "user":user_data.useremail,
        "total_count":len(diaries_list),
    }

@diary_router.get('/{diary_id}',response_model=DiaryBaseResponse)
async def get_one_diary(diary_id:int,user_data:UserRead=Depends(get_current_user)):
    diary = await DiaryRepo.get_diary(diary_id,user_data)
    return diary

@diary_router.put('/{diary_id}',response_model=DiaryBaseResponse)
async def mod_diary(diary_id:int,mod_data:DiaryBase,user_data:UserRead=Depends(get_current_user)):
    diary = await DiaryRepo.update_diary(diary_id,mod_data,user_data)
    return diary

@diary_router.delete("/{diary_id}")
async def del_diary(diary_id:int,user_data:UserRead=Depends(get_current_user)):
    return await DiaryRepo.delete_diary(diary_id,user_data)




