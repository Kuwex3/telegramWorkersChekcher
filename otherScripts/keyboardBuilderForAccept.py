from aiogram.utils.keyboard import InlineKeyboardBuilder

def getKeyboard(tgid):
    builder = InlineKeyboardBuilder()
    builder.button(text="Принять✅", callback_data=f"YesAcceptToCompany{tgid}")
    builder.button(text="Отклонить❌", callback_data=f"NoDeniedToCompany{tgid}")
    return builder.as_markup()