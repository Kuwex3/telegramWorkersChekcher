import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USR = os.getenv("USR")
PASSWORDDB = os.getenv("PASSWORDDB")