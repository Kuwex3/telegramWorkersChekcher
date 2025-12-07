from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from dataBase.midlewares.registerCompany import regCompany

from dataBase.getMidlewares.getUniqueCode import getUnique

from dotenv import load_dotenv
import os

load_dotenv()

presaveMsg = os.getenv("FIRST_MESSAGE")

from bot.sources.keyboards import backToMainMenuBeyboard

router = Router()

@router.callback_query(F.data == "YesRegisterCompany")
async def getMainMenu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    companyName = data.get("companyName")
    ownerName = data.get("ownerName")
    ownerTgID = data.get("ownerTgID")
    mass = [companyName, ownerName, ownerTgID]
    regCompany(mass)
    code = getUnique(mass[2])
    await state.clear()
    await callback.message.edit_text(f"Вы успешно зарегистрировали компанию!\n<b>Уникальный код для сотрудников: {code[0]}</b>", parse_mode="HTML", reply_markup=backToMainMenuBeyboard)