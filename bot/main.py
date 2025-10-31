import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
FM = os.getenv("FIRST_MESSAGE")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.message):
    await message.answer(f"{FM}", parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())