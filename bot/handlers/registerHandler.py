from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from logs.logsHandlers import registerOwnerLogger as rgLog
from logs.logsHandlers import registerWorkerLogger as rgWLog

from bot.sources.keyboards import backToMainMenuBeyboard

from dataBase.checkers.isHasCompany import checkCompany

router = Router()

@router.callback_query(F.data == "RegWorker")
async def echo_handler(callback: types.CallbackQuery, state: FSMContext):
    rgWLog.regWorkerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.edit_text("Du bist a worker!", reply_markup=backToMainMenuBeyboard)
    await callback.answer()
    
@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery, state: FSMContext):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    result = checkCompany(callback.from_user.id)
    if result in "User has company:":
        await callback.message.edit_text("У вас уже есть активная компания!😉", reply_markup=backToMainMenuBeyboard)
    elif result == "User doesn't has company!":
        await callback.message.edit_text("Регистрация компании. Отправьте название своей фирмы!", reply_markup=backToMainMenuBeyboard)
        await state.set_state(waitingNameCompany = True)
    await callback.message.edit_text("Du bist soldat!", reply_markup=backToMainMenuBeyboard)
    await callback.answer()