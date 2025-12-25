from aiogram.utils.keyboard import InlineKeyboardBuilder

def getKeyboard(tgid, company):
    builder = InlineKeyboardBuilder()
    builder.button(text="Принять✅", callback_data=f"YesAcceptToCompany{tgid}U{company}")
    builder.button(text="Отклонить❌", callback_data=f"NoDeniedToCompany{tgid}U{company}")
    return builder.as_markup()