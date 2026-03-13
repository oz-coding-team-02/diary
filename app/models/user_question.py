from tortoise import fields
from app.core.base import TimestampModel


class UserQuestion(TimestampModel):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="seen_questions")
    question = fields.ForeignKeyField("models.Question", related_name="seen_by_users")

    class Meta:
        table = "user_questions"
        unique_together = ("user", "question")  # 한 유저가 같은 질문을 여러 번 기록하지 않도록 설정
