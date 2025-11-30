from dataBase.setDbConnect import get_conn

def isUser(data):
    conn = get_conn()
    curs = conn.cursor()
    tg_id = data[0]
    name = data[1]
    try:
        curs.execute("SELECT id FROM tg_users WHERE tgid = %s", (tg_id,))
        result = curs.fetchone()
        if result is not None:
            print("BAD")
            return "is user!"
        else:
            print("REG!")
            curs.execute("INSERT INTO tg_users (tgid, name) VALUES (%s, %s)", (tg_id, name))
            conn.commit()
            return "reg!"
    except Exception as ex:
        return f"Bad {ex}"
    finally:
        conn.close()
        curs.close()