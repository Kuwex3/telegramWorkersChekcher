from bot.sources.classes import WorkerReg
from bot.sources.keyboards import backToMainMenuBeyboard

from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext

from dataBase.getMidlewares.getCompanyByCode import checkCode

router = Router()

@router.message(WorkerReg.waitingToWriteCode)
async def enterCodeHandler(message: types.Message, state: FSMContext):
    print("handler start works")
    code = message.text
    result = checkCode(code)
    data = await state.get_data()
    msg = data.get("msgForEdit")
    if result[0] != "not has company":
        await msg.edit_text(f"Вы действительно хотите присоединится в компанию {result[0]}?", parse_mode="HTML", reply_markup=backToMainMenuBeyboard)