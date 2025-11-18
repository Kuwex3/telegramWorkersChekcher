from aiogram import types, Router
from aiogram.filters.command import Command

import os
import dotenv

dotenv.load_dotenv()

password = os.getenv("ADMINPASS")

router = Router()

@router.message(Command(f"/wakk{password}"))
async def admin_panel(message: types.Message):
    await message.answer("Админ Панель!")