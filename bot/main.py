import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from bot.sources.keyboards import firstStartKeyboard

import bot.handlers.registerHandler as handler
import bot.handlers.mainMenuHandler as menuHan
import bot.handlers.registerCompany as regComp
import bot.handlers.registerCompanyButtonsHandler as regCpBtns
import bot.handlers.adminMenu as adminMenu
import bot.handlers.adminGetAllCompanies as adGetComp
import bot.handlers.adminGetAllWorkers as adGetWorkers
import bot.handlers.writeCodeHandler as WriteCode
import bot.handlers.joinCompanyButton as JoinButton
import bot.handlers.acceptToJoinInCompany as AcceptJoin

from dataBase.checkers.isUser import isUser

from logs.logsHandlers.startLogger import startLogger

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
FM = os.getenv("FIRST_MESSAGE")

bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_router(regComp.router)
dp.include_router(handler.router)
dp.include_router(menuHan.router)
dp.include_router(regCpBtns.router)
dp.include_router(adminMenu.router)
dp.include_router(adGetComp.router)
dp.include_router(adGetWorkers.router)
dp.include_router(WriteCode.router)
dp.include_router(JoinButton.router)
dp.include_router(AcceptJoin.router)

@dp.message(Command("start"))
async def start_handler(message: types.message, state: FSMContext):
    startLogger(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    send_msg = await message.answer(f"{FM}", parse_mode=ParseMode.HTML, reply_markup=firstStartKeyboard)
    await state.update_data(first_msg_id = send_msg.message_id)
    mass = [message.from_user.id, message.from_user.first_name]
    isUser(mass)

async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())