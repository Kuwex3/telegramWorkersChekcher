from dataBase.setDbConnect import get_conn

def checkCompanyName(user_company):
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT name FROM companies")
        data = curs.fetchall()
        companies = []
        for i in data:
            companies.append(i[0])
        if user_company in companies:
            return "taken"
        else:
            return "not taken"
    except Exception as ex:
        return f"ex {ex}!"
    finally:
        conn.close()
        curs.close()