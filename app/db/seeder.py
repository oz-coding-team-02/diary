from tortoise import Tortoise
from app.db.database import TORTOISE_CONFIG
from app.models.quote import Quote
from app.models.question import Question


async def save_to_db(data_list: list, data_type: str = 'quote'):
    await Tortoise.init(config=TORTOISE_CONFIG)

    try:
        if data_type == 'quote':
            for item in data_list:
                await Quote.create(
                    author=item.get('author', 'Anonymous'),
                    content=item.get('content')
                )

        elif data_type == 'question':
            for content in data_list:
                await Question.create(content=content)

        print(f'성공적으로 {data_type} 데이터 {len(data_list)}개가 DB에 저장되었습니다.')

    except Exception as e:
        print(f'에러 발생 : {e}')

    finally:
        await Tortoise.close_connections()