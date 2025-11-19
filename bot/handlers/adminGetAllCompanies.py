from aiogram import types, Router, F

from dataBase.getMidlewares.getAllCompanies import getCompanies

router = Router()

@router.callback_query(F.data == "CheckAllCompanies")
async def sendCompanies(callback: types.CallbackQuery):
    data = getCompanies()
    await callback.message.edit_text(f"Все компании:\n{data}")