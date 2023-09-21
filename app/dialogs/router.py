import asyncio
import logging

from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent
from aiohttp import ClientConnectorError

from app.db.db_user.user_func import User
from app.dialogs.states import LoginSG, MenuSG

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    await starting_dispatcher(message, dialog_manager)


async def starting_dispatcher(message: Message, dialog_manager: DialogManager):
    is_registered = await User.is_registered(message.from_user.id)
    if is_registered:
        await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(LoginSG.mail, mode=StartMode.RESET_STACK)