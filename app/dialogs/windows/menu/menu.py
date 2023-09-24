from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import MenuSG
from app.dialogs.windows.menu.func import getter_menu, send_ics

MenuMainWin = Window(
    Format("Привет {name} {sticker}"),
    Group(
        Button(Const("Получить расписание на 2 недели"), on_click=send_ics, id="send_ics_button"),
        width=2,
    ),
    getter=getter_menu,
    state=MenuSG.main,
)
