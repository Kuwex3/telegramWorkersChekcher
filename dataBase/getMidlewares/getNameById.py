from dataBase.setDbConnect import get_conn

def getName(tgid):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT name FROM tg_users WHERE tgid = %s", (tgid,))
        name = curs.fetchone()
        return name
    except Exception as ex:
        return f"Bad! ex:{ex}"
    finally:
        conn.close()
        curs.close()