from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from dataBase.midlewares.registerCompany import regCompany

from dotenv import load_dotenv
import os

load_dotenv()

presaveMsg = os.getenv("FIRST_MESSAGE")

from bot.sources.keyboards import firstStartKeyboard

router = Router()

@router.callback_query(F.data == "YesRegisterCompany")
async def getMainMenu(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    companyName = data.get("companyName")
    ownerName = data.get("ownerName")
    ownerTgID = data.get("ownerTgID")
    mass = [companyName, ownerName, ownerTgID]
    regCompany(mass)
    await state.clear()
    await callback.message.edit_text("Вы успешно зарегистрировали компанию!", reply_markup=firstStartKeyboard)