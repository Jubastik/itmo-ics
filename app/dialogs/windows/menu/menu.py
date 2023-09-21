from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Button
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import MenuSG
from app.dialogs.windows.menu.func import getter_menu

MenuMainWin = Window(
    Format("Привет {name} {sticker}"),
    Group(
        Button(Format("{not_btn_text}"), on_click=send_ics, id="notifications_btn"),
        width=2,
    ),
    getter=getter_menu,
    state=MenuSG.main,
)