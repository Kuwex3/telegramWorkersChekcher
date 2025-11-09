import psycopg2 as ps
from config import HOST, DATABASE, USR, PASSWORDDB, PORT


conn = ps.connect(
    host = HOST,
    port = PORT,
    database = DATABASE,
    user = USR,
    password = PASSWORDDB
)

curs = conn.cursor()

curs.execute("INSERT INTO tg_users (name, age) VALUES (%s, %s)", ("Alex", 22))

conn.commit()

curs.close()
conn.close()