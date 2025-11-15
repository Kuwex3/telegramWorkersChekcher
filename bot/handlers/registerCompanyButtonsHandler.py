from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv
import os

load_dotenv()

presaveMsg = os.getenv("FIRST_MESSAGE")

from bot.sources.keyboards import firstStartKeyboard

router = Router()

@router.callback_query(F.data == "YesRegisterCompany")
async def getMainMenu(callback: types.CallbackQuery):
    await callback.message.edit_text("Yes!", reply_markup=firstStartKeyboard)