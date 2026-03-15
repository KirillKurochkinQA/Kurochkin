import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "stage1":
        LOGIN = os.getenv("LOGIN_1")
        PASSWORD = os.getenv("PASSWORD")
    elif STAGE == "stage2":
        LOGIN = os.getenv("LOGIN_2")
        PASSWORD = os.getenv("PASSWORD")
    elif STAGE == "stage3":
        LOGIN = os.getenv("LOGIN_3")
        PASSWORD = os.getenv("PASSWORD")