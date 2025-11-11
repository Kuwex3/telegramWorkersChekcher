from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from logs.logsHandlers import registerOwnerLogger as rgLog
from logs.logsHandlers import registerWorkerLogger as rgWLog

from bot.sources.keyboards import backToMainMenuBeyboard

router = Router()

@router.callback_query(F.data == "RegWorker")
async def echo_handler(callback: types.CallbackQuery, state: FSMContext):
    rgWLog.regWorkerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.edit_text("Du bist a worker!", reply_markup=backToMainMenuBeyboard)
    await callback.answer()
    
@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.edit_text("Du bist soldat!", reply_markup=backToMainMenuBeyboard)
    await callback.answer()