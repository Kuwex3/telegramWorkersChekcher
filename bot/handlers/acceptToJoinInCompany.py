from aiogram import types, Router, F

from dataBase.midlewares.joinWorker import joinWorker
from dataBase.getMidlewares.getNameById import getName

router = Router()

@router.callback_query(F.data.contains("YesAcceptToCompany"))
async def acceptJoin(callback: types.callback_query):
    rawDataMass = callback.data.split("U")
    company = rawDataMass[1]
    tgid = rawDataMass[0].split("YesAcceptToCompany")[1]
    worker_name = getName(tgid)
    result = joinWorker(worker_name, tgid, company)
    print(result)