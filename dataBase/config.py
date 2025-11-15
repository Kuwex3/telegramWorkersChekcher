import os
from dotenv import load_dotenv
import psycopg2 as ps

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
USR = os.getenv("USR")
PASSWORDDB = os.getenv("PASSWORDDB")

conn = ps.connect(
    host = HOST,
    port = PORT,
    database = DATABASE,
    user = USR,
    password = PASSWORDDB
)

curs = conn.cursor()