from aiogram.fsm.state import State, StatesGroup

class CompanyReg(StatesGroup):
    waitingNameCompany = State()
    waitingInviteToCompany = State()
    waitingToWriteCompany = State()

class WorkerReg(StatesGroup):
    waitingToWriteCode = State()