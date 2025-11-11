from aiogram import F, types, Router
from logs.logsHandlers import registerOwnerLogger as rgLog
from logs.logsHandlers import registerWorkerLogger as rgWLog


router = Router()

@router.callback_query(F.data == "RegWorker")
async def echo_handler(callback: types.CallbackQuery):
    waitingCompanyName = True
    rgWLog.regWorkerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.answer("Du bist a worker!")
    await callback.answer()
    
@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.answer("Du bist soldat!")
    await callback.answer()