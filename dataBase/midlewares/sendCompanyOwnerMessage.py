from otherScripts.keyboardBuilderForAccept import getKeyboard

async def sendOwnerMessage(tgid, bot, firstname, lastname, usertag, userid, company):
    kb = getKeyboard(userid, company)
    if lastname == None and userid == None:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname}", reply_markup=kb, parse_mode = "HTML")
    elif lastname == None:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname} <b>@{usertag}</b>", reply_markup=kb, parse_mode = "HTML")
    else:
        await bot.send_message(chat_id=tgid, text=f"К вашей компании хочет присоединится {firstname} {lastname} <b>@{usertag}</b>", reply_markup=kb, parse_mode = "HTML")