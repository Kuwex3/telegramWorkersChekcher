from dataBase.setDbConnect import get_conn

def getCompanies():
    conn = get_conn()
    curs = conn.cursor()
    curs.execute("SELECT * FROM companies")
    data = curs.fetchall()
    return(data)