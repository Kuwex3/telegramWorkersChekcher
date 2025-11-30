import psycopg2
from dataBase.config import data

def get_conn():
    return psycopg2.connect(
        host = data[0],
        port = data[1],
        database = data[2],
        user = data[3],
        password = data[4]
    )