from dataBase.setDbConnect import get_conn

def checkCompany(tgid):
    conn = get_conn()
    curs = conn.cursor()
    curs.execute("SELECT isowner FROM tg_users WHERE tgid = %s", (tgid,))
    data = curs.fetchone()
    print(data)
    if data == (True,):
        curs.execute("SELECT name FROM companies WHERE ownertgid = %s", (tgid,))
        companyName = curs.fetchone()
        print(type(companyName))
        return companyName
    else:
        return "User doesn't has company!"