from tortoise import fields
from tortoise.models import Model


class User(Model):
    tg_id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    tg_username = fields.CharField(max_length=255, null=True)
    token = fields.CharField(max_length=2000)
    token_expires = fields.DatetimeField()
    refresh_token = fields.CharField(max_length=2000)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.tg_id})"
