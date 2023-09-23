import asyncio
import logging

from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent
from aiohttp import ClientConnectorError
from requests import HTTPError

from app.db.db_user.user_func import User
from app.dialogs.states import LoginSG, MenuSG

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    await starting_dispatcher(message, dialog_manager)


async def starting_dispatcher(message: Message, dialog_manager: DialogManager):
    is_registered = await User.is_registered(message.from_user.id)
    if is_registered:
        await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK, data={"tg_id": message.from_user.id})
    else:
        await dialog_manager.start(LoginSG.mail, mode=StartMode.RESET_STACK)


async def error_handler(event, dialog_manager: DialogManager):
    logging.error(event.exception)
    if isinstance(event.exception, UnknownIntent):
        # Handling an error related to an outdated callback
        await handle_start_query(event.update.callback_query, dialog_manager)
    elif isinstance(event.exception, HTTPError):
        await starting_dispatcher(event.update.callback_query, dialog_manager)
        await event.update.callback_query.answer(
            "Сервер my.itmo вернул ошибку\nВероятнее всего ваш токен устарел, авторизуйтесь заново", show_alert=True)
    elif isinstance(event.exception, ClientConnectorError):
        await event.update.callback_query.answer("Сервер недоступен", show_alert=True)
    else:
        return UNHANDLED
