from dataBase.setDbConnect import get_conn

def getWorkerCompanyName(tgid):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT company FROM workers WHERE tgid = %s", (tgid,))
        result = curs.fetchone()
        if result:
            return result
        else:
            return "error from fetching company"
    except Exception as ex:
        return f"bad {ex}"
    finally:
        conn.close()
        curs.close()