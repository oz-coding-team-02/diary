from app.models.diary import Diary
from app.models.user import User


# noinspection PyMethodMayBeStatic
class DiaryRepo:
    async def get_diary(self, diary_id: int, user: User):
        result = await Diary.filter(id=diary_id, user_id=user.id).first()
        return result

    async def get_list_diaries(self, user: User):
        result = await Diary.filter(user_id=user.id).all()
        return result

    async def make_new_diary(self, data, user: User):
        result = await Diary.create(
            title=data.title, content=data.content, user_id=user.id
        )
        return result

    async def modding_diary(self, diary_id, mod_data, user: User):
        result = await Diary.filter(id=diary_id, user_id=user.id).first()
        # 예외 처리: 데이터가 없을 때를 대비해 체크하는 것이 좋습니다.
        if result:
            result.title = mod_data.title
            result.content = mod_data.content
            await result.save()
        return result

    async def del_r_diary(self, diary_id, user: User):
        result = await Diary.filter(id=diary_id, user_id=user.id).first()
        if result:
            target_title = result.title
            await result.delete()
            return {"msg": "diary deleted", "target_title": target_title}
        return None
