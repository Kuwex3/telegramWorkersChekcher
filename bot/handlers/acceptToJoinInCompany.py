from aiogram import types, Router, F

from dataBase.midlewares.joinWorker import joinWorker

router = Router()

@router.callback_query(F.data.contains("YesAcceptToCompany"))
async def acceptJoin(callback: types.callback_query):
    print("successfull!")