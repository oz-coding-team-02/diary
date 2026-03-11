from app.models.diary import Diary
from typing import List

from app.schemas.diary import DiaryCreateRequest,DiaryBase
from app.schemas.user import UserRead
from fastapi import HTTPException, status

class DiaryRepo:
    @staticmethod
    async def create_diary(user_data:UserRead,diary_data:DiaryCreateRequest):
        diary = Diary(title=diary_data.title,content=diary_data.content,user_id=user_data.id)
        await diary.save()
        return diary

    @staticmethod
    async def check_exists(user_id:int) ->bool:
        """user_id를 인자로 받고 해당 id를 참조하는 diary가 존재하는지 bool을 반환하는 함수"""
        return await Diary.filter(id=user_id).exists()

    @staticmethod
    async def get_diaries(user_data:UserRead)->List[Diary]:
        """user_id를 인자로 받고 해당 id를 참조하는 diaries의 list를 반환하는 함수"""
        diaries = await Diary.filter(user_id=user_data.id).all()
        return diaries

    @staticmethod
    async def get_diary(diary_id:int,user_data:UserRead)->Diary:
        """diary_id와 user_id를 인자로 받아 user_id를 참조하고 diary_id를 입력함으로써 단일 조회하는 함수
    만일 해당 row가 없다면 예외처리로 에러코드를 반환하고 있다면 해당 row를 반환"""
        diary = await Diary.filter(id=diary_id,user_id=user_data.id).first()
        if not diary:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Diary not found")
        return diary

    @staticmethod
    async def update_diary(diary_id:int,mod_data:DiaryBase,user_data:UserRead)->Diary:
        """diary_id와 user_data를 입력받아 user_id를 참조하는 diary중에서 입력한 diary_id와 같은 row의
        데이터를 수정하고 수정된 row를 반환하는 함수"""
        diary = await Diary.filter(id=diary_id,user_id=user_data.id).first()
        if not diary:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Diary not found")
        diary.title = mod_data.title
        diary.content = mod_data.content
        await diary.save()
        return diary

    @staticmethod
    async def delete_diary(diary_id:int,user_data:UserRead):
        """diary_id와 user_data를 입력받아 user_id를 참조하는 diary중에서 입력한 diary_id와 같은 row의
        데이터를 삭제하고 삭제된 row의 tilte과 msg를 반환하는 함수"""
        target_diary = await Diary.filter(id=diary_id,user_id=user_data.id).first()
        if not target_diary:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Diary not found")
        await target_diary.delete()
        return {"msg":"delete success","title":target_diary.title}