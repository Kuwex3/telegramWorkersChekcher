from dataBase.setDbConnect import get_conn

def getCompanies():
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT * FROM companies")
        data = curs.fetchall()
        return(data)
    except Exception as ex:
        return f"bad: {ex}"
    finally:
        conn.close()
        curs.close()