from dataBase.setDbConnect import get_conn

def getAllWorkersDef():
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT name, company FROM workers")
        data = curs.fetchall()
        return data
    except Exception as ex:
        return f"bad! {ex}"
    finally:
        conn.close()
        curs.close()