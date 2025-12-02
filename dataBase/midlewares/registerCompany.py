from dataBase.setDbConnect import get_conn

def regCompany(mass):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("INSERT INTO companies (name, ownername, ownertgid) VALUES (%s, %s, %s)", (mass[0], mass[1], mass[2]))
        curs.execute("UPDATE tg_users SET isowner = %s WHERE tgid = %s", (True, mass[2]))
        conn.commit()
    except Exception as ex:
        return f"bad: {ex}"
    finally:
        conn.close()
        curs.close()