from dataBase.setDbConnect import get_conn

def joinWorker(tg_user_id):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("UPDATE tg_users SET isworker = %s, WHERE tgid = %s", (True, tg_user_id))
        conn.commit()
        # curs.execute("UPDATE workers SET ")
    except Exception as ex:
        return f"error! ex: {ex}"
    finally:
        conn.close()
        curs.close()