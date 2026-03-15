import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    STAGE = os.getenv("STAGE")

    if STAGE == "stage1":
        LOGIN = os.getenv("LOGIN_STANDARD")
        PASSWORD = os.getenv("PASSWORD")
    elif STAGE == "stage2":
        LOGIN = os.getenv("LOGIN_LOCKED_OUT")
        PASSWORD = os.getenv("PASSWORD")
    elif STAGE == "stage3":
        LOGIN = os.getenv("LOGIN_PROBLEM")
        PASSWORD = os.getenv("PASSWORD")