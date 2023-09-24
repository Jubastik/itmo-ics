import logging
from datetime import datetime, timedelta

from requests import HTTPError

from app.db.db_user import user_models
from app.dialogs.windows.login.auth import refresh_access_token

tzinf = datetime.now().astimezone().tzinfo


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
                                refresh_token=refresh_token, token_expires=datetime.now() + timedelta(minutes=25), )

    @classmethod
    async def del_user(cls):
        await cls.delete()

    @classmethod
    async def get_jwt(cls, tg_id: int) -> str:
        user = await cls.get_user(tg_id)
        if user.token_expires > datetime.now(tz=tzinf):
            return user.token
        else:
            try:
                jwt = refresh_access_token(user.refresh_token)
            except HTTPError as e:
                await user.del_user()
                logging.warning(f"Токен пользователя {user.pk} устарел, пользователь удален из БД")
                raise e
            user.token = jwt["access_token"]
            user.token_expires = datetime.now() + timedelta(minutes=25)
            return user.token
