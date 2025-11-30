from dataBase.config import curs

def isWorker(mass):
    curs.execute("SELECT isworker FROM tg_users WHERE tgid = %s", (mass[0],))
    data = curs.fetchone()
    
    if data[0] == True:
        return "is worker"
    else:
        return "not worker"