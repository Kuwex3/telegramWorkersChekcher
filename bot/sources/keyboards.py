from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnRegOwner = InlineKeyboardButton(text="Владелец🤵‍♂️", callback_data="RegOwner")
btnRegWorker = InlineKeyboardButton(text="Рабочий👷‍♂️", callback_data="RegWorker")

btnBackMenu = InlineKeyboardButton(text="⬅️Назад", callback_data="BackToMenu")

btnYesRegisterCompany = InlineKeyboardButton(text="Да✅", callback_data="YesRegisterCompany")
btnYesJoinToCompany = InlineKeyboardButton(text="Да✅", callback_data="YesJoinToCompany")
btnYesAcceptToCompany = InlineKeyboardButton(text="Принять✅", callback_data="YesAcceptToCompany")

btnNoDeniedToCompany = InlineKeyboardButton(text="Отклонить❌", callback_data="NoDeniedToCompany")

btnCheckAllCompanies = InlineKeyboardButton(text="Все компании📋", callback_data="CheckAllCompanies")
btnCheckAllWorkers = InlineKeyboardButton(text="Все работники👷‍♂️", callback_data="CheckAllWorkers")

firstStartKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnRegOwner, btnRegWorker]])
backToMainMenuBeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnBackMenu]])
registerCompanyKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnYesRegisterCompany, btnBackMenu]])

adminKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnCheckAllCompanies, btnCheckAllWorkers, btnBackMenu]])
adminKeyboardInCompanyMenu = InlineKeyboardMarkup(inline_keyboard=[[btnCheckAllWorkers, btnBackMenu]])
adminKeyboardInWorkerMenu = InlineKeyboardMarkup(inline_keyboard=[[btnCheckAllCompanies, btnBackMenu]])

joinKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnYesJoinToCompany, btnBackMenu]])

acceptKeyboard = InlineKeyboardMarkup(inline_keyboard=[[btnYesAcceptToCompany, btnNoDeniedToCompany]])