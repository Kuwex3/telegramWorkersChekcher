from dataBase.setDbConnect import get_conn

def isWorker(mass):
    conn = get_conn()
    curs = conn.cursor()
    curs.execute("SELECT isworker FROM tg_users WHERE tgid = %s", (mass[0],))
    data = curs.fetchone()
    
    if data[0] == True:
        return "is worker"
    else:
        return "not worker"