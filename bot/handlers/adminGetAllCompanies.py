from aiogram import types, Router, F

from dataBase.getMidlewares.getAllCompanies import getCompanies

from bot.sources.keyboards import adminKeyboardInCompanyMenu as adminKb

router = Router()

@router.callback_query(F.data == "CheckAllCompanies")
async def sendCompanies(callback: types.CallbackQuery):
    data = getCompanies()
    presaveText = []
    for i in data:
        print(i[0])
        presaveText.append(f"Название компании: <b>{i[0]}</b>")
        presaveText.append(f"Имя владельца компании: <b>{i[1]}</b>")
        presaveText.append("-----------------------------------------------------")
    finallyText = "\n".join(presaveText)
    await callback.message.edit_text(f"Все компании:\n-----------------------------------------------------\n{finallyText}", parse_mode="HTML", reply_markup=adminKb)