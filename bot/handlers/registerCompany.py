from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from bot.sources.classes import CompanyReg
from bot.sources.keyboards import registerCompanyKeyboard, backToMainMenuBeyboard

from dataBase.checkers.isCompanyAlreadyRegister import checkCompanyName

router = Router()

@router.message(CompanyReg.waitingNameCompany)
async def regCompany(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == CompanyReg.waitingNameCompany:
        nameCompany = message.text
        data = await state.get_data()
        msgForEdit = data.get("messageForEdit")
        result = checkCompanyName(nameCompany)
        if nameCompany and result == "taken":
            await msgForEdit.edit_text(f"Компания <b>{nameCompany}</b> уже зарегистрирована, измените название!", reply_markup=backToMainMenuBeyboard, parse_mode = "HTML")
        if nameCompany and result == "not taken":
            await msgForEdit.edit_text(f"Вы хотите зарегистрировать компанию: <b>{nameCompany}</b>?", reply_markup=registerCompanyKeyboard, parse_mode = "HTML")
            await state.set_data({"companyName": nameCompany, "ownerName": message.from_user.first_name, "ownerTgID": message.from_user.id})