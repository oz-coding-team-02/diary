from tortoise import fields
from app.core.base import TimestampModel


class User(TimestampModel):
    id = fields.IntField(pk=True)
    useremail = fields.CharField(max_length=255, unique=True)
    password_hash = fields.CharField(max_length=255)

    class Meta:
        table = "users"