from random import choice

from aiogram.types import Message, BufferedInputFile
from aiogram_dialog import DialogManager, DialogProtocol
from app.db.db_user.user_func import User
from app.dialogs.windows.menu.my_itmo import get_raw_events, raw_events_to_calendar
from datetime import datetime, timedelta
from aiogram_dialog import ShowMode

stickers = ['👍', '👻', '😄', '🧐', '👀', '🌝', '🎫', '🔫', '📌', '📚']


async def getter_menu(dialog_manager: DialogManager, **kwargs):
    user = await User.get_user(dialog_manager.start_data.get("tg_id"))
    return {"name": user.name,
            "sticker": choice(stickers), }


async def send_ics(message: Message, dialog: DialogProtocol, manager: DialogManager):
    token = await User.get_jwt(manager.start_data.get("tg_id"))
    events = get_raw_events(token, date_start=datetime.now(), date_end=datetime.now() + timedelta(days=14))
    calendar = raw_events_to_calendar(events)
    tg_cal = BufferedInputFile(bytes("\n".join(map(str.strip, calendar)), encoding='utf8'), filename="schedule.ics")
    await message.message.answer_document(tg_cal,
                                          caption="Расписание на 2 недели\n<a href='https://calendar.google.com/calendar/u/0/r/settings/export'>*импорт*</a>")
    await message.message.delete()
    await manager.update(data=manager.dialog_data, show_mode=ShowMode.SEND)
