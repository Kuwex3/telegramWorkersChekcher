from dataBase.setDbConnect import get_conn

def getOwnerId(company):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT ownertgid FROM companies WHERE name = %s", (company,))
        data = curs.fetchone()
        if data[0]!= "None":
            return data[0]
        else:
            return "bad id"
    except Exception as ex:
        return f"ex {ex}!"
    finally:
        curs.close()
        conn.close()