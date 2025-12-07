from dataBase.setDbConnect import get_conn
from otherScripts.createUniqueCode import createUniqueCode

def regCompany(mass):
    conn = get_conn()
    curs = conn.cursor()
    try:
        uniqueCode = createUniqueCode()
        curs.execute("INSERT INTO companies (name, ownername, ownertgid, uniquecode) VALUES (%s, %s, %s, %s)", (mass[0], mass[1], mass[2], uniqueCode))
        curs.execute("UPDATE tg_users SET isowner = %s WHERE tgid = %s", (True, mass[2]))
        conn.commit()
    except Exception as ex:
        return f"bad: {ex}"
    finally:
        conn.close()
        curs.close()