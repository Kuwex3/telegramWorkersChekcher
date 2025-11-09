import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
USR = os.getenv("USR")
PASSWORDDB = os.getenv("PASSWORDDB")