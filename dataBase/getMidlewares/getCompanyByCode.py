from dataBase.setDbConnect import get_conn

def checkCode(user_code):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT name FROM companies WHERE uniquecode = %s", (user_code,))
        data = curs.fetchone()
        if data:
            return data
        else:
            return ["not has company"]
    except Exception as ex:
        return f"ex! {ex}"
    finally:
        conn.close()
        curs.close()