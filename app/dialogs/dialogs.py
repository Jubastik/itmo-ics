from aiogram import Dispatcher
from aiogram_dialog import Dialog

from app.dialogs.windows.login.login import LoginMailWin, LoginPassWin
from app.dialogs.windows.menu.menu import MenuMainWin


def register_dialogs(dp: Dispatcher):
    dp.include_router(LoginDLG)
    dp.include_router(MenuDLG)


LoginDLG = Dialog(LoginMailWin, LoginPassWin)
MenuDLG = Dialog(MenuMainWin)
