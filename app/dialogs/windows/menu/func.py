from random import choice

from aiogram_dialog import DialogManager
from app.db.db_user.user_func import User

stickers = ['👍', '👻', '😄', '🧐', '👀', '🌝', '🎫', '🔫', '📌', '📚']


async def getter_menu(dialog_manager: DialogManager, **kwargs):
    user = await User.get_user(dialog_manager.start_data.get("tg_id"))
    return {"name": user.name,
            "sticker": choice(stickers), }


async def send_ics(dialog_manager: DialogManager, **kwargs):
    token = await User.get_jwt()
