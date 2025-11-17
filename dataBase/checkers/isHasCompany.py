from dataBase.config import conn, curs

def checkCompany(tgid):
    curs.execute("SELECT isowner FROM tg_users WHERE tgid = %s", (tgid,))
    data = curs.fetchone()
    print(data)
    if data == (True,):
        curs.execute("SELECT name FROM companys WHERE ownertgid = %s", (tgid,))
        companyName = curs.fetchone()
        return ["У вас уже есть активная компания: ", companyName]
    else:
        return "User doesn't has company!"