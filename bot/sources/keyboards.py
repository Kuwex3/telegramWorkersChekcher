from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text="Создать", callback_data="Create")

kb1 = InlineKeyboardMarkup(inline_keyboard=[[btn1]])