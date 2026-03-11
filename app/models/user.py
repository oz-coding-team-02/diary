from tortoise import fields
from .base import TimestampModel


class User(TimestampModel):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True, index=True)
    password_hash = fields.CharField(max_length=255)

    class Meta:
        table = "users"
