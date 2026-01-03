from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.sources.keyboards import backToMainMenuBeyboard

from dataBase.midlewares.sendCompanyOwnerMessage import sendOwnerMessage as so
from dataBase.getMidlewares.getOwnerId import getOwnerId

router = Router()

@router.callback_query(F.data == "YesJoinToCompany")
async def JoinToCompany(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    company = data.get("companyNameForJoin")
    ownerId = getOwnerId(company)
    await so(ownerId, callback.bot, callback.from_user.first_name, callback.from_user.last_name, callback.from_user.username, callback.from_user.id, company)
    await callback.message.edit_text(f"Вы отправили заявку на присоединение к компании <b>{company}</b>!\nПодождите когда владелец его рассмотрит.", parse_mode="HTML", reply_markup=backToMainMenuBeyboard)
    await state.clear()