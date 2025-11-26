from dataBase.config import curs

def isWorker(mass):
    curs.execute("SELECT isworker, companyname FROM workers WHERE tgid = %s", (mass[0]))
    data = curs.fetchone()
    
    if data[0] == True:
        return data
    else:
        return "successfull"