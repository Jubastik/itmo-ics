from aiogram.fsm.state import StatesGroup, State


class LoginSG(StatesGroup):
    mail = State()
    password = State()


class MenuSG(StatesGroup):
    main = State()
