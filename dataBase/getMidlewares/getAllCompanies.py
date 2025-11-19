from dataBase.config import curs

def getCompanies():
    curs.execute("SELECT * FROM companies")
    data = curs.fetchall()
    return(data)