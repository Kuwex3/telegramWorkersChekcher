from dataBase.setDbConnect import get_conn

def getUniq(tg_id):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT uniquecode FROM companies WHERE ownertgid = %s", (tg_id))
        data = curs.fetchone()
        return data
    except Exception as ex:
        return f"ex {ex}"
    finally:
        conn.close()
        curs.close()