from tortoise import fields
from app.core.base import TimestampModel


class Diary(TimestampModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50)
    content = fields.TextField()

    user = fields.ForeignKeyField(
        "models.User", related_name="diaries", on_delete=fields.CASCADE
    )

    class Meta:
        table = "diaries"
