from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from logs.logsHandlers import registerOwnerLogger as rgLog
from logs.logsHandlers import registerWorkerLogger as rgWLog

from bot.sources.keyboards import backToMainMenuBeyboard
from bot.sources.classes import CompanyReg

from dataBase.checkers.isHasCompany import checkCompany

import os
import dotenv

dotenv.load_dotenv()

worker_presave_message = os.getenv("WORKER_MESSAGE")

router = Router()

@router.callback_query(F.data == "RegWorker")
async def echo_handler(callback: types.CallbackQuery, state: FSMContext):
    rgWLog.regWorkerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.edit_text(worker_presave_message, reply_markup=backToMainMenuBeyboard, parse_mode="HTML")
    result = 0
    await callback.answer()
    
@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery, state: FSMContext):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    result = checkCompany(callback.from_user.id)
    if type(result) == tuple:
        await callback.message.edit_text(f"У вас уже есть компания <b>{result[0]}</b>😉", reply_markup=backToMainMenuBeyboard, parse_mode="HTML")
    elif result == "User doesn't has company!":
        await callback.message.edit_text("Регистрация компании. Отправьте название своей фирмы!", reply_markup=backToMainMenuBeyboard)
        await state.set_data({"messageForEdit": callback.message})
        await state.set_state(CompanyReg.waitingNameCompany)
    await callback.answer()