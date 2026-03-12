from typing import Optional

from tortoise.contrib.postgres.functions import Random

from app.models.bookmark import Bookmark
from app.models.quote import Quote


class QuoteRepository:
    def __init__(self):
        pass

    async def get_random_quote_one(self) -> Optional[Quote]:
        # Optional[Quote] -> 타입이 Quote나 None이 반환될 수 있음을 표시 -> db에 데이터가 없을 경우 None을 return함
        return await Quote.annotate(idx=Random()).order_by("idx").first()

    async def get_bookmark_or_none(self, user_id: int, quote_id: int) -> Optional[Bookmark]:
        return await Bookmark.get_or_none(user_id=user_id, quote_id=quote_id)

    async def create_bookmark(self, user_id: int, quote_id: int) -> Bookmark:
        return await Bookmark.create(user_id=user_id, quote_id=quote_id)

    async def get_bookmarked_quotes_for_user(self, user_id: int) -> list[Bookmark]:
        return await Bookmark.filter(user_id=user_id).select_related("quote").all()
