import asyncio

from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.input import MessageInput

from app.db.db_user.user_func import User
from app.dialogs.states import MenuSG
from app.dialogs.universal_func import del_message_by
from app.dialogs.windows.login.auth import get_access_token


async def handle_mail(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data["mail"] = message.text
    await message.delete()
    await manager.next()


async def handle_password(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data["password"] = message.text
    try:
        token, refresh_token = get_access_token(manager.dialog_data["mail"], manager.dialog_data["password"])
    except ValueError:
        warnings = await message.answer("Неверный логин или пароль 😔\nПопробуйте еще раз")
        asyncio.create_task(del_message_by(warnings, 4))
        return
    await User.create_user(message.from_user.id, message.from_user.full_name, message.from_user.username,
                           token, refresh_token)
    await message.delete()
    await manager.start(MenuSG.main, show_mode=ShowMode.EDIT, mode=StartMode.RESET_STACK)
