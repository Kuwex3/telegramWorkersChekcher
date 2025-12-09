from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from logs.logsHandlers import registerOwnerLogger as rgLog
from logs.logsHandlers import registerWorkerLogger as rgWLog

from bot.sources.keyboards import backToMainMenuBeyboard
from bot.sources.classes import CompanyReg, WorkerReg

from dataBase.checkers.isHasCompany import checkCompany
from dataBase.checkers.isWorker import isWorker

from dataBase.getMidlewares.getUniqueCode import getUnique

import os
import dotenv

dotenv.load_dotenv()

worker_presave_message = os.getenv("WORKER_MESSAGE")

router = Router()

@router.callback_query(F.data == "RegWorker")
async def echo_handler(callback: types.CallbackQuery, state: FSMContext):
    rgWLog.regWorkerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    user_data = [callback.from_user.id]
    result = isWorker(user_data)
    if result[0] == "not worker":
        await callback.message.edit_text("Вы не являетесь работником, отправьте уникальный код компании в которую хотите устроиться.", reply_markup=backToMainMenuBeyboard)
        state.set_state(WorkerReg.waitingToWriteCode)
    if result[0] == "is worker":
        await callback.message.edit_text(f"Вы уже работаете в компании: <b>{result[1][0]}</b>", parse_mode="HTML", reply_markup=backToMainMenuBeyboard)
    await callback.answer()
    
@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery, state: FSMContext):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    result = checkCompany(callback.from_user.id)
    if result[0] == "user has company!":
        uniqueCode = getUnique(callback.from_user.id)
        await callback.message.edit_text(f"У вас уже есть компания <b>{result[1][0]}</b>😉\nУникальный код для сотрудников: <b>{uniqueCode[0]}</b>", reply_markup=backToMainMenuBeyboard, parse_mode="HTML")
    elif result[0] == "User doesn't has company!":
        await callback.message.edit_text("Регистрация компании. Отправьте название своей фирмы сообщением!", reply_markup=backToMainMenuBeyboard)
        await state.set_data({"messageForEdit": callback.message})
        await state.set_state(CompanyReg.waitingNameCompany)
    await callback.answer()