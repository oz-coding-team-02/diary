from tortoise import fields
from app.core.base import TimestampModel


class Bookmark(TimestampModel):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.User", related_name="bookmarks", on_delete=fields.CASCADE
    )
    quote = fields.ForeignKeyField(
        "models.Quote", related_name="bookmarks", on_delete=fields.CASCADE
    )

    class Meta:
        table = "bookmarks"
        unique_together = (("user", "quote"),)
