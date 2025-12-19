from dataBase.setDbConnect import get_conn

def getUnique(tg_id):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT uniquecode FROM companies WHERE ownertgid = %s", (tg_id,))
        data = curs.fetchall()
        return data[0]
    except Exception as ex:
        return f"ex! error: {ex}"
    finally:
        conn.close()
        curs.close()