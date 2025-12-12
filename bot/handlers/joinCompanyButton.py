from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.sources.keyboards import backToMainMenuBeyboard

router = Router()

@router.callback_query(F.data == "YesJoinToCompany")
async def JoinToCompany(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    company = data.get("companyNameForJoin")
    await callback.message.edit_text(f"Вы присоединились к компании {company}!", parse_mode="HTML", reply_markup=backToMainMenuBeyboard)