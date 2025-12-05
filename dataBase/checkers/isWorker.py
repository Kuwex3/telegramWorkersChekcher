from dataBase.setDbConnect import get_conn
from dataBase.getMidlewares.getWorkerCompany import getWorkerCompanyName

def isWorker(mass):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT isworker FROM tg_users WHERE tgid = %s", (mass[0],))
        data = curs.fetchone()
        if data[0] == True:
            company = getWorkerCompanyName(mass[0])
            result = ["is worker", company]
            return result
        elif data[0] == None:
            result = ["not worker", "Вы не являетесь работником"]
            return result
    except Exception as ex:
        return f"bad: {ex}"
    finally:
        conn.close()
        curs.close()