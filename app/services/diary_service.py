from fastapi import Depends
from app.repositories.diary_repo import DiaryRepo

class DiaryService:
    def __init__(self, repo: DiaryRepo):
        self.repo = repo

    async def get_diary(self, diary_id: int, user):
        return await self.repo.get_diary(diary_id, user)

    async def get_all_diaries(self, user):
        return await self.repo.get_list_diaries(user)

    async def make_diary(self, data, user):
        return await self.repo.make_new_diary(data, user)

    async def modify_diary(self, diary_id, mod_data, user):
        return await self.repo.modding_diary(diary_id, mod_data, user)

    async def del_diary(self, diary_id, user):
        return await self.repo.del_r_diary(diary_id, user)

def get_diary_repo() -> DiaryRepo:
    return DiaryRepo()

def get_diary_service(repo: DiaryRepo = Depends(get_diary_repo)) -> DiaryService:
    return DiaryService(repo=repo)