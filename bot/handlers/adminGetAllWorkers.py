from aiogram import types, Router, F

from dataBase.getMidlewares.getAllWorkers import getAllWorkersDef

from  bot.sources.keyboards import adminKeyboardInWorkerMenu as adminkb

router = Router()

@router.callback_query(F.data == "CheckAllWorkers")
async def getAllWorkers(callback: types.CallbackQuery):
    data = getAllWorkersDef()
    formated_massive = []
    for i in range(len(data)):
        formated_massive.append(f"Работник: <b>{data[i][0]}</b>\nКомпания: <b>{data[i][1]}</b>")
        formated_massive.append("-----------------------------------------------------")
    formated_message = "\n".join(formated_massive)
    await callback.message.edit_text(f"Все работники:\n-----------------------------------------------------\n{formated_message}", parse_mode="HTML", reply_markup=adminkb)