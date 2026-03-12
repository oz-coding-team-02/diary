from typing import Literal

from tortoise import Tortoise
from app.db.database import TORTOISE_CONFIG
from app.models.quote import Quote
from app.models.question import Question


async def save_to_db(data_list: list, data_type: Literal['quote', 'question'] ):
    await Tortoise.init(config=TORTOISE_CONFIG)

    try:
        if data_type == "quote":
            to_create = [
                Quote(
                    author=item.get("author", "Anonymous"), content=item.get("content")
                )
                for item in data_list
            ]
            await Quote.bulk_create(to_create)



        elif data_type == 'question':
            to_create = [
                Question(content=content) for content in data_list
            ]
            await Question.bulk_create(to_create)

        print(f'[성공] {data_type} 데이터 {len(data_list)}개가 DB에 저장되었습니다.')

    except Exception as e:
        raise f'[실패] {data_type} 저장 중 오류 발생: {e}'

    finally:
        await Tortoise.close_connections()