from aiogram import Dispatcher
from aiogram_dialog import Dialog, DialogManager, StartMode

from app.dialogs.windows.login.login import LoginMailWin


def register_dialogs(dp: Dispatcher):
    dp.include_router(LoginDLG)


LoginDLG = Dialog(LoginMailWin)
