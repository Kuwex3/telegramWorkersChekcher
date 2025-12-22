from bot.sources.keyboards import backToMainMenuBeyboard as kb

async def sendOwnerMessage(tgid, bot, firstname, lastname, userid):
    if lastname == None and userid == None:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname}.", reply_markup=kb, parse_mode = "HTML")
    elif lastname == None:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname} <b>{userid}</b>.", reply_markup=kb, parse_mode = "HTML")
    else:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname} {lastname} <b>@{userid}</b>.", reply_markup=kb, parse_mode = "HTML")