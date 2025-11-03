from aiogram import F, types, Router

router = Router()

@router.message(F.text)
async def echo_handler(message: types.Message):
    await message.answer(message.html_text, parse_mode="HTML")