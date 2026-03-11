from tortoise import fields, models


class TimestampModel(models.Model):
    # 모든 테이블에 공통으로 들어갈 필드들
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
