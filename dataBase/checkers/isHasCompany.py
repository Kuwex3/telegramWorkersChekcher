from dataBase.config import HOST, PORT, DATABASE, USR, PASSWORDDB, conn, curs
import psycopg2 as ps

def checkCompany(tgid):
    curs.execute("SELECT isowner FROM tg_users WHERE tgid = %s", (tgid,))
    data = curs.fetchone()
    if data:
        curs.execute("SELECT name FROM companys WHERE ownertgid = %s", (tgid,))
        companyName = curs.fetchone()
        return f"User has company: {companyName}"
    else:
        return "User doesn't has company!"