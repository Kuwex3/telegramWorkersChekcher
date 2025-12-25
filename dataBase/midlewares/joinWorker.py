from dataBase.setDbConnect import get_conn

def joinWorker(name, tg_user_id, company):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("UPDATE tg_users SET isworker = %s WHERE tgid = %s", (True, tg_user_id))
        conn.commit()
        curs.execute("INSERT INTO workers (name, tgid, company) VALUES (%s, %s, %s)", (name, tg_user_id, company))
        conn.commit()
        return f"Работник добавлен"
    except Exception as ex:
        return f"error! ex: {ex}"
    finally:
        conn.close()
        curs.close()