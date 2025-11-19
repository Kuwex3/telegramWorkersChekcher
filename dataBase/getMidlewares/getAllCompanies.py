from dataBase.config import curs

def getCompanies():
    curs.execute("SELECT * FROM companies")
    data = curs.fetchone()
    return(data)