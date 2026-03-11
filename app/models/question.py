from tortoise import fields
from app.core.base import TimestampModel

class Question(TimestampModel):
    id = fields.IntField(pk=True)
    content = fields.TextField()

    class Meta:
        table = "questions"