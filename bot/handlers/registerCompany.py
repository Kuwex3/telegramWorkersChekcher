from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from bot.sources.classes import CompanyReg

from bot.sources.keyboards import registerCompanyKeyboard

router = Router()

@router.message(CompanyReg.waitingNameCompany)
async def regCompany(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == CompanyReg.waitingNameCompany:
        nameCompany = message.text
        data = await state.get_data()
        msgForEdit = data.get("messageForEdit")
        if nameCompany:
            await msgForEdit.edit_text(f"Вы хотите зарегистрировать компанию: {nameCompany}?", reply_markup=registerCompanyKeyboard)
            await state.set_data({"companyName": nameCompany, "ownerName": message.from_user.first_name, "ownerTgID": message.from_user.id})