from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Back
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import LoginSG
from app.dialogs.windows.login.func import handle_mail, handle_password

HI_TEXT = "🔻Для начала работы введи свой логин от my.itmo.ru🔻"

LoginMailWin = Window(
    Const(HI_TEXT),
    MessageInput(handle_mail, ContentType.TEXT),
    state=LoginSG.mail,
)

LoginPassWin = Window(
    Const("🔻Введите пароль🔻"),
    Back(Const("Назад")),
    MessageInput(handle_password, ContentType.TEXT),
    state=LoginSG.password,
)
