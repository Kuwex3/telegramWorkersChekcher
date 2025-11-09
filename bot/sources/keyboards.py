from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnRegOwner = InlineKeyboardButton(text="Владелец🤵‍♂️", callback_data="RegOwner")
btnRegWorker = InlineKeyboardButton(text="Рабочий👷‍♂️", callback_data="RegWorker")

firstStartKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnRegOwner, btnRegWorker]])