import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode

from bot.sources.keyboards import firstStartKeyboard
import bot.handlers.registerHandler as handler

from logs.logsHandlers.startHandler import startLogger

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
FM = os.getenv("FIRST_MESSAGE")

bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_router(handler.router)

@dp.message(Command("start"))
async def start_handler(message: types.message):
    startLogger(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    await message.answer(f"{FM}", parse_mode=ParseMode.HTML, reply_markup=firstStartKeyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())