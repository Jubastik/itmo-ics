from tortoise import fields
from tortoise.models import Model


class User(Model):
    tg_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    tg_username = fields.CharField(max_length=255, null=True)
    itmo_token = fields.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.tg_id})"
