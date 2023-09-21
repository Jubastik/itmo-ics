from app.db.db_user import user_models


class User(user_models.User):
    @classmethod
    async def is_registered(cls, tg_id: int) -> bool:
        return await cls.filter(tg_id=tg_id).exists()
