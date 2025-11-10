from aiogram import F, types, Router

router = Router()

@router.message(F.text)
async def echo_handler(message: types.Message):
    pass

@router.callback_query(F.data == "RegOwner")
async def buttonHandlers(callback: types.CallbackQuery):
    await callback.message.answer("Du bist soldat!")
    await callback.answer()