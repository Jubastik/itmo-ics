from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import LoginSG

HI_TEXT = "Привет 👋\n Я бот, который поможет тебе получить расписание из my.itmo.ru в формате iCal. \n\n Для начала работы введи свой логин от my.itmo.ru"

LoginMailWin = Window(
    Const(HI_TEXT),
    state=LoginSG.mail,
)
