from dataBase.setDbConnect import get_conn

def checkCompany(tgid):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT isowner FROM tg_users WHERE tgid = %s", (tgid,))
        data = curs.fetchone()
        print(data)
        if data == (True,):
            curs.execute("SELECT name FROM companies WHERE ownertgid = %s", (tgid,))
            companyName = curs.fetchone()
            print(type(companyName))
            return ["user has company!", companyName]
        else:
            return ["User doesn't has company!"]
    except Exception as ex:
        return f"bad: {ex}"
    finally:
        conn.close()
        curs.close()