from tortoise import fields
from app.core.base import TimestampModel


class UserQuestion(TimestampModel):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="received_questions", on_delete=fields.CASCADE)
    question = fields.ForeignKeyField("models.Question", related_name="received_by_users", on_delete=fields.CASCADE)

    class Meta:
        table = "user_questions"
        unique_together = (("user", "question"),)