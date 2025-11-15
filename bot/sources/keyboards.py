from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnRegOwner = InlineKeyboardButton(text="Владелец🤵‍♂️", callback_data="RegOwner")
btnRegWorker = InlineKeyboardButton(text="Рабочий👷‍♂️", callback_data="RegWorker")

btnBackMenu = InlineKeyboardButton(text="⬅️Назад", callback_data="BackToMenu")

btnYesRegisterCompany = InlineKeyboardButton(text="Да✅", callback_data="YesRegisterCompany")

firstStartKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnRegOwner, btnRegWorker]])
backToMainMenuBeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnBackMenu]])
registerCompanyKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnYesRegisterCompany, btnBackMenu]])