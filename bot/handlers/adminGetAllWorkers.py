from aiogram import types, Router, F

from dataBase.getMidlewares.getAllWorkers import getAllWorkersDef

from  bot.sources.keyboards import adminKeyboardInWorkerMenu as adminkb

router = Router()

@router.callback_query(F.data == "CheckAllWorkers")
async def getAllWorkers(callback: types.CallbackQuery):
    data = getAllWorkersDef()
    await callback.message.edit_text(f"{data}", parse_mode="HTML", reply_markup=adminkb)