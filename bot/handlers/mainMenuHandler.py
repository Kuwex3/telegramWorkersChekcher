from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv
import os

load_dotenv()

presaveMsg = os.getenv("FIRST_MESSAGE")

from bot.sources.keyboards import firstStartKeyboard

router = Router()

@router.callpresaveMsgback_query(F.data == "BackToMenu")
async def getMainMenu(callback: types.CallbackQuery):
    await callback.message.edit_text(f"{presaveMsg}", reply_markup=firstStartKeyboard, parse_mode="HTML")