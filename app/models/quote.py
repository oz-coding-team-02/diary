from tortoise import fields
from app.core.base import TimestampModel


class Quote(TimestampModel):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=100, default="Anonymous")

    class Meta:
        table = "quotes"