from aiogram import F, types, Router
from logs.logsHandlers import registerOwnerLogger as rgLog


router = Router()

@router.message(F.text)
async def echo_handler(message: types.Message):
    pass

@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery):
    rgLog.regOwnerLog(callback.from_user.id, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username)
    await callback.message.answer("Du bist soldat!")
    await callback.answer()