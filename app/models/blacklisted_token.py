from tortoise import models, fields


class BlacklistedToken(models.Model):
    id = fields.IntField(pk=True)
    token_hash = fields.CharField(max_length=225, unique=True)
    blacklisted_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "blacklisted_token"
