from bot.sources.keyboards import backToMainMenuBeyboard as kb

async def sendOwnerMessage(tgid, bot):
    await bot.send_message(chat_id=tgid, text="Lorem", reply_markup=kb)