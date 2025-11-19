from dataBase.config import curs, conn

def regCompany(mass):
    curs.execute("INSERT INTO companies (name, ownername, ownertgid) VALUES (%s, %s, %s)", (mass[0], mass[1], mass[2]))
    conn.commit()