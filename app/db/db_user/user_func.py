from datetime import datetime, timedelta

from app.db.db_user import user_models


class User(user_models.User):
    @classmethod
    async def is_registered(cls, tg_id: int) -> bool:
        return await cls.filter(tg_id=tg_id).exists()

    @classmethod
    async def get_user(cls, tg_id: int) -> "User":
        return await cls.get(tg_id=tg_id)

    @classmethod
    async def create_user(cls, tg_id: int, name: str, tg_username: str, token: str, refresh_token: str) -> "User":
        return await cls.create(tg_id=tg_id, name=name, tg_username=tg_username, token=token,
                                refresh_token=refresh_token, token_expires=datetime.now() + timedelta(hours=20))
