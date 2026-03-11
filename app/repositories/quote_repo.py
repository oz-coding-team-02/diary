from tortoise.contrib.postgres.functions import Random

from app.models.quote import Quote

class QuoteRepository:
    @staticmethod
    async def get_random_quote_one():
        return await Quote.annotate(idx=Random()).order_by("idx").first()