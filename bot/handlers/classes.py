from aiogram.fsm.state import State, StatesGroup

class CompanyReg(StatesGroup):
    waitingNameCompany = State()