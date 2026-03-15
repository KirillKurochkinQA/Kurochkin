import os
from dotenv import load_dotenv
load_dotenv()

STAGE = os.getenv("STAGE")

class Urls:

    HOST = "https://www.saucedemo.com/"
    LOGIN_PAGE = f"{HOST}"
