import logging

import requests
from datetime import datetime, timedelta

from aiogram.types import Message
from requests import HTTPError

from app.db.db_user import user_models
from app.dialogs.windows.login.auth import refresh_access_token


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
                                refresh_token=refresh_token, token_expires=datetime.now() + timedelta(hours=20), )

    @classmethod
    async def del_user(cls):
        await cls.delete()

    @classmethod
    async def get_jwt(cls, msg: Message) -> str:
        if cls.token_expires > datetime.now():
            return await cls.token
        else:
            try:
                jwt = refresh_access_token(cls.refresh_token)
            except HTTPError as e:
                await cls.del_user()
                logging.warning(f"Токен пользователя {msg.from_user.id} устарел, пользователь удален из БД")
                raise e
            cls.token = jwt["access_token"]
            cls.token_expires = datetime.now() + timedelta(hours=20)
            return await cls.token
