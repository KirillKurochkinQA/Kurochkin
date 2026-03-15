import os
from dotenv import load_dotenv
load_dotenv()

STAGE = os.getenv("STAGE")

class Urls:

    HOST = "https://www.saucedemo.com"
    LOGIN_PAGE = f"{HOST}/"
    INVENTORY_PAGE = f"{HOST}/inventory.html"
    CART_PAGE = f"{HOST}/cart.html"
    CHECKOUT_STEP_ONE_PAGE = f"{HOST}/checkout-step-one.html"
    CHECKOUT_STEP_TWO_PAGE = f"{HOST}/checkout-step-two.html"
    CHECKOUT_COMPLETE_PAGE = f"{HOST}/checkout-complete.html"
