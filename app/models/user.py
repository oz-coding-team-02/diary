from tortoise import fields
from app.core.base import TimestampModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.diary import Diary
    from app.models.bookmark import Bookmark


class User(TimestampModel):
    id = fields.IntField(pk=True)
    useremail = fields.CharField(max_length=255, unique=True)
    password_hash = fields.CharField(max_length=255)
    is_admin = fields.BooleanField(default=False)

    diaries: fields.ReverseRelation["Diary"]
    bookmarks: fields.ReverseRelation["Bookmark"]

    class Meta:
        table = "users"
