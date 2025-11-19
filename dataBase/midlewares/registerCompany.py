from dataBase.config import curs, conn

def regCompany(mass):
    curs.execute("INSERT INTO companies (name, ownername, ownertgid) VALUES (%s, %s, %s)", (mass[0], mass[1], mass[2]))
    curs.execute("INSERT INTO tg_users (name, isowner, tgid) VALUES (%s, %s, %s)", (mass[1], True, mass[2]))
    conn.commit()